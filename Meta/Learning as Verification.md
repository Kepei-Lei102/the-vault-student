---
chinese: "学习即验证 (xuéxí jí yànzhèng) — 会检查，比会做重要"
prerequisites:
  - "[[The Feynman Technique]]"
  - "[[Chain of Thought]]"
  - "[[P vs NP]]"
  - "[[Chi-Squared Tests]]"
leads_to:
  - "[[Credit Is the Currency]]"
  - "[[Program Development Life Cycle and Testing]]"
tags:
  - subject/methodology
  - subject/philosophy
  - subject/computer-science
  - subject/mathematics
  - domain/cognition
  - domain/learning
  - domain/complexity-theory
  - level/life
  - type/methodology
  - type/meta
  - type/cross-domain
---

# Learning as Verification 学习即验证

> *An engineer ten years out of university cannot integrate by parts any more. Hand her a solution and she will still tell you in thirty seconds whether it is wrong: the units do not match, the sign is backwards, it does not reduce to the known case when the damping is zero. She forgot the recipe and kept the thing that mattered. Now that machines produce the recipe on demand, that is the thing to learn.*

## What this card is for

For most of the history of schooling, *learning a method* meant being able to **produce** its output: run the integration, fit the model, write the program, and arrive at the answer. That was the scarce skill, so that is what was taught and tested. It is no longer scarce. A calculator produces the arithmetic, a computer-algebra system the integral, a statistics package the fitted model, and a language model the essay, the code and the proof sketch, on request and at once.

What did not become cheap is knowing whether the output is **right**. That skill is older than the machines and separate from producing: the person who checks a bridge design is not the person who drew it, the referee did not write the paper, the examiner did not sit the exam. And it turns out to be, in a precise sense, *easier* than producing — which is the reason it can be learned as a skill of its own and the reason it survives after the recipe has faded.

This card makes three claims. **Checking is a different skill from producing, and usually a cheaper one** (Part I, with the theorem that says so). **It has a toolkit — a ladder of checks, cheapest first** (Part II), of which one rung, *counting*, deserves its own treatment (Part III), and one, *the check designed in*, is already in your wallet (Part IV). And **it has a characteristic failure, the verifier who nods**, which is the whole danger of the age the machines have opened (Part V). The engineer's calculus is the model throughout: what to keep when you are allowed to forget.

### 中文锚点

**学习即验证 (xuéxí jí yànzhèng)** = 当机器随时能给出答案，人真正要学的不是**做出**答案，而是**判断答案对不对**。

一个毕业十年的工程师早就不会分部积分了，可你把一份解答递给她，三十秒内她就能说出错在哪：**单位对不上**、**符号反了**、阻尼取零时**退化不成**已知的公式。她忘掉的是配方，留下的是要紧的东西。这张卡的三个主张：第一，**检查和做题是两种不同的本事，而且检查通常便宜得多**——这有定理撑腰：一个数独填起来要几万步，验一遍只要扫一眼；一个 23 位数分解要将近一秒，验证一对因数只要零点几微秒（这张卡真的实测过）。第二，检查有自己的**工具箱**，一架从便宜到贵的梯子：先看单位和量纲，再看符号和数量级，再让参数取 0 或无穷看公式是否退化为已知情形，再数约束、代回原题、换一条路、干脆模拟一遍——大多数错误在头三级就死了，代价只是瞥一眼。第三，验证最典型的失败是**点头的检查员**：机器给的答案看起来太像对的，于是检查变成了走过场。费曼说过，**第一条原则是不要骗自己，而最容易被你骗的人就是你自己**。所以要向机器要的不是结论，而是**可以核对的证据**——代入、单位、极限——然后自己核对。

---

## Part I — Finding is hard; checking is easy. That is a theorem.

Start with the fact that makes the whole card possible. Take any hard puzzle — a sudoku, a jigsaw, a factorisation. Producing the answer may take hours; **confirming** an answer someone hands you takes a glance. The rows and columns add up or they do not. The pieces fit or they do not. Multiply the two claimed factors and see whether you get the number. [[P vs NP]] is the formal name for that asymmetry: NP is precisely the class of problems whose answers can be *checked* quickly given a certificate, and the universal belief that P ≠ NP is the belief that for many of them the checking really is easier than the finding.

`learning-as-verification-asymmetry.py` measures it on this machine:

![[learning-as-verification-asymmetry.svg|900]]

*Three tasks, each timed both ways. Recovering two primes from their 23-digit product takes the best general algorithm most of a second; confirming a claimed pair takes a third of a microsecond, three million times less. Signing a message needs the 512-bit private exponent; verifying the signature needs the public exponent 65537 and is thirty times faster, and a signature one bit off is refused. Solving the sudoku takes 37 000 trial placements; checking the filled grid takes 27 comparisons of sorted rows, and a grid with two cells swapped is refused.*

The second pair is the one the world runs on. A digital signature is an answer that *only* the key-holder can produce and *anyone* can check — the verifier needs no secret, no skill, no idea how the signature was made, and can still refuse a forgery with certainty. Every software update, every bank login and every certificate in the [[Encryption]] card rests on that split between producing and checking being a one-way door.

Mathematics discovered the same door from the inside. When Appel and Haken proved the Four Colour Theorem in 1976, the proof ran to hundreds of pages of case analysis and a thousand hours of computer time, and the mathematical world was uneasy: no human could *check* it. The resolution, in 2005, was not a shorter proof. It was a **smaller checker**: Gonthier rebuilt the proof inside Coq, whose trusted kernel is a few thousand lines that a careful reader can audit in a week, and the kernel confirmed every step. That principle — make the *checker* small and trusted, and let the *prover* be as large and clever as it likes — is the de Bruijn criterion, and it is the design of every proof assistant since ([[Hilbert vs Brouwer]] tells where the kernels' logic came from). Notice what it says about learning: the mathematician of 2005 did not need to be able to *produce* a four-colour proof. She needed to trust a checker she could read.

The oldest verification technology is older than any of this, and it is in a ledger.

![[learning-as-verification-pacioli-comic.png|720]]

*Venice, 1494. Luca Pacioli's* Summa *printed the method Venetian merchants had used for a century: every transaction entered **twice**, as a debit in one account and a credit in another, so that the two columns must always sum to the same total. The trial balance does not know what the business did. It knows only that if the books disagree, somebody made a mistake — and it catches it without anyone re-doing a single transaction. Double-entry bookkeeping is the check digit of Part IV, five hundred years early.*

An examiner is a verifier too. Look at any mark scheme in this vault's Exam Notes: *M1* for a correct method, *A1* for the accurate value, *B1* for a stated fact. The marker never solves the question; the scheme is a **verification protocol**, a list of certificates the candidate must exhibit, and it is designed so that a marker who could not produce the solution can still confirm one line by line. Learning to read a mark scheme is learning to verify.

---

## Part II — The ladder: eight checks cheaper than redoing

Verification is not "do it again and see if you agree". Redoing is the most expensive check there is, and it fails against exactly the errors a *method* makes, because the second run makes them too. The working verifier climbs a ladder, cheapest rung first, and most wrong answers die on the bottom three.

![[learning-as-verification-ladder.svg|760]]

Each rung, with a place in this vault where it does real work:

1. **Units and dimensions.** Every term in a physical equation must have the same dimensions — [[Physical Quantities and Units]] makes this the central principle, and its opening story is the *Mars Climate Orbiter*, lost in 1999 because one team's software produced pound-force seconds and the other's consumed newton seconds. Nobody re-derived anything wrong; nobody checked the units at the seam. A ten-second rung.
2. **Sign and size.** Is the answer the right way round, and roughly the right size? A Fermi estimate — powers of ten, no calculator — is the cheapest independent computation there is, and [[Estimation (Vocab)]] is the school version of it. A drift velocity of $0.07$ mm s$^{-1}$ in [[Electric Current]] surprises a student; a drift velocity of $70$ m s$^{-1}$ should alarm one.
3. **Limits and special cases.** Set a parameter to $0$, $1$ or $\infty$ and demand that the formula collapse to the case you already know. The resonant amplitude in [[Resonance]], $A = (F_0/m)/\sqrt{(\omega_0^2-\omega^2)^2+4\gamma^2\omega^2}$, must give the static deflection $F_0/k$ at $\omega = 0$, must fall as $1/\omega^2$ for large $\omega$, and must blow up at $\omega = \omega_0$ when $\gamma = 0$. A formula that fails any of those is wrong before you have found the slip.
4. **Symmetry and counting.** Swap the labels the problem treats alike and the answer must not care; count the constraints and the answer must respect them. The number of independent loop equations a circuit needs in [[Kirchhoff's Laws]] is $E - V + 1$, a count, so a student who wrote five equations for a circuit that admits three has found an error without checking any of them. Part III is this rung grown to full size.
5. **Substitute back.** The oldest check in algebra: a root must satisfy its equation, a particular integral must satisfy its differential equation. It is the certificate of Part I made literal, and it catches the errors that a *method* cannot catch about itself.
6. **An independent route.** A second derivation that shares no steps with the first. The resonant amplitude was found by algebra in [[Resonance]] Part II and by an energy balance in Part IV; that they agree is worth more than either alone, because a slip in one cannot propagate to the other.
7. **Simulate.** Brute-force the situation and compare. This vault's habit: the driven oscillator integrated by Runge–Kutta beside its formula, the diagonal argument run on real lists, a DNS query hand-assembled and sent. Simulation is expensive in machine time and cheap in *your* time, which is the currency that matters, and it is the rung the machines have made free.
8. **Redo it.** The last resort, and the only rung that costs as much as producing. Reserve it for when the ladder has found a fault and you need to locate it.

The order is the point. A wrong answer that survives rungs 1–3 is rare; a verifier who *starts* at rung 8 has spent the whole budget on the check least likely to be needed.

---

## Part III — "Why is it minus one, minus one?"

One rung deserves a card of its own, because it is the one students most often replace with a rule. In [[Chi-Squared Tests]] the degrees of freedom are

$$\nu = (\text{cells}) - 1 - (\text{parameters estimated from the data}),$$

and the question every class asks is *why minus one, and then minus one again?* The rule-answer is "because that is the formula". The verification-answer is a **count**: each miss $O_i - E_i$ is a number the data was free to make, *except* that the misses must obey one equation for every constraint the expected values were built to satisfy. The expected counts were made to sum to $N$ — that is one equation, so one miss is fixed by the others: minus one. If a parameter was estimated from the same data, the expected counts were also made to match, say, the sample mean — a second equation, a second miss no longer free: minus one again. A student who can *count the equations* can verify $\nu$ for a table she has never seen; a student who has the rule can only hope she remembered it.

And the count can itself be checked, by rung 7. `learning-as-verification-nu.py` draws four thousand samples from a Poisson distribution, fits the mean from each sample, bins the counts into six cells, computes $X^2$, and asks which chi-squared curve the four thousand statistics follow:

![[learning-as-verification-nu.svg|900]]

*The statistics sit on the curve with $\nu = 6 - 1 - 1 = 4$ (Kolmogorov–Smirnov $p = 0.54$) and refuse the one with $\nu = 5$, the rule that forgot the fitted parameter ($p < 0.001$). The script then builds a $3 \times 4$ contingency table and confirms $(r-1)(c-1) = 6$ the same way: twelve cells, minus one for the total, minus two and three for the fitted row and column proportions.*

That is the whole method of this card in one example. The recipe (look up the formula) was replaced by a countable argument, and the argument was then checked against a simulation that knew nothing about the argument. Either half alone is knowledge; together they are *verified* knowledge, and the student who has done this once will never again be unsure whether the parameter costs a degree of freedom.

---

## Part IV — The check designed in

Take out a bank card. The sixteenth digit stores nothing about you. It was chosen, when the number was issued, so that a small sum over all sixteen digits comes to a multiple of ten — the **Luhn** algorithm, patented in 1954 — and its only purpose is to let a terminal that knows nothing about the account refuse a mistyped number. An ISBN's last character does the same with weights $10, 9, \ldots, 1$ and a modulus of $11$. `learning-as-verification-checkdigit.py` generates the digit, then makes the two commonest human errors on purpose:

| Error | Luhn (bank card) | ISBN-10 |
|---|---|---|
| One wrong digit, any position | caught 144 of 144 | caught 81 of 81 |
| Two adjacent digits swapped | caught 13 of 14 — misses only 09 ↔ 90 | caught 9 of 9 |

ISBN's modulus is prime and its weights are all different, which is why it catches every transposition; Luhn's is not, which is why it misses one. **A check is a piece of engineering**: it is designed to be cheap, to be independent of the thing it checks, and to catch the errors that are actually likely. The same three requirements design every check on the ladder — and they are the reason a *test* written before the code (test-driven development), an *assertion* inside a program, and the trial balance of 1494 all work the same way: a small independent computation whose disagreement is louder than the agreement it usually reports.

The lesson for the learner is to build the check in at the moment of producing. Before solving, write down what the answer must satisfy — its units, its sign, its limit, the equation it must fit back into. Then the check costs nothing, because it was designed in, and an answer that arrives from anywhere — your own working, a calculator, a model — meets the same gate.

---

## Part V — The verifier who nods

Every verification system has one failure mode, and it is not a wrong check. It is a check that is *not run*, because the answer looked right. The pilots who watched the autopilot fly into the ground had instruments that would have told them; the field is called **automation complacency**, and its central finding is that the better the machine, the less the human looks. An answer from a fluent model has the same property: it arrives formatted, confident and plausible, and plausibility is precisely what a verifier must not accept as evidence.

![[learning-as-verification-units-comic.png|720]]

*The machine did the work; she does the checking. The ruler against the screen is rung 1 — and the see-saw with a metre on one side and a stopwatch on the other is what she found.*

Feynman's rule for scientists, from the 1974 lecture on cargo-cult science, is the rule for this age: *the first principle is that you must not fool yourself — and you are the easiest person to fool.* Three habits follow.

- **Ask for the certificate, not the conclusion.** A model that says "the answer is 4.0 Hz" has given you nothing to check. A model that says "the period on the graph is 0.25 s, so $f = 1/0.25$" has given you a substitution you can verify in five seconds, and if the period is really 0.5 s you will see it. Demand the working in the form the ladder can climb: the units, the limit, the equation substituted back.
- **A check you cannot fail is not a check.** If you read an answer and nod, you have not verified it; you have re-read it. Decide *before* looking what would make it wrong — a unit, a sign, a limit — and then look for that. The Pacioli merchant did not read the ledgers; he compared two totals that had to agree.
- **Verify the method, not the instance, once.** The engineer does not re-derive the resonant amplitude every time; she verified it once, thoroughly, and kept the limits as a fingerprint. Rung 7 on a method you will use a hundred times is the best-spent hour in a course. That is what [[The Feynman Technique]]'s rebuild-from-scratch is *for*: not to memorise the derivation, but to earn the right to trust the result.

---

## How to use this card

1. **Before solving anything, write the gate.** Units, sign, expected size, at least one limit, and the equation the answer must satisfy. Thirty seconds. Every answer — yours, the calculator's, the model's — passes the same gate or does not.
2. **Climb from the bottom.** When an answer arrives, run rungs 1–3 before reading the working. Most errors die there; reading the working first is how the verifier starts nodding.
3. **Replace every rule with a count where one exists.** *Minus one, minus one*; $E - V + 1$ loops; $n - 1$ for a sample variance. If you can count it, you can verify it on a case you have never seen.
4. **Ask machines for certificates.** Not "what is the answer" but "show the substitution", "give the units", "what does this become when $x = 0$". Then check the certificate, which is cheap, instead of the answer, which is not.
5. **Verify each method once, properly, then keep the fingerprint.** Simulate it, derive it a second way, find its limits. After that, the fingerprint is the check, and the recipe may be allowed to fade — that is the engineer's calculus.
6. **Never accept a check you did not decide on in advance.** Agreement you were hoping for is not evidence; disagreement you were looking for is.

---

## Misconceptions

1. **"Verifying is just doing it again."** Redoing is rung 8, the most expensive check and the weakest against a method's own errors. The ladder exists because seven cheaper checks catch most faults first, and because a second run of the same method repeats its mistakes.
2. **"If I can check it, I could have done it."** Part I's theorem says otherwise: checking a factorisation, a signature or a proof needs neither the secret nor the skill that produced it. That is the whole reason verification can be the retained skill after the recipe is gone.
3. **"With AI, I don't need to understand the method at all."** You need to understand it *enough to verify it* — its units, limits, counts and certificates. That is less than producing it and more than nothing, and the difference is exactly what this card teaches.
4. **"A confident, well-formatted answer is probably right."** Confidence and formatting are properties of the *producer*, not of the answer, and a verifier who weights them has stopped verifying. The machine's fluency is the reason to check, not the reason not to.
5. **"A check that always passes is reassuring."** A check that cannot fail is measuring nothing. Design checks that *would* fail on the likely errors — the transposition, the dropped parameter, the wrong unit — as Luhn and ISBN were designed.
6. **"Verification is for exams."** The mark scheme is one verifier; the bank terminal, the proof kernel, the trial balance and the pilot's instruments are the same idea. The exam is where a student first meets it, not where it lives.

---

## Connections

- **Parents:**
   - [[The Feynman Technique]] — rebuilding from scratch is how a method is verified *once*; this card is what to keep afterwards.
   - [[Chain of Thought]] — the trigger, not the technique: naming what selected a tool is the certificate a verifier reads first.
   - [[P vs NP]] — the theorem behind Part I: NP is the class of quickly checkable answers, and the belief that P ≠ NP is the belief that checking is the easier half.
   - [[Chi-Squared Tests]] — the *minus one, minus one* of Part III, and the card whose review produced this one.

- **Children:**
   - [[Credit Is the Currency]] — a promise becomes currency when it is *verified* to have come true; the ledger of Part I is where credit was first kept.

- **Cross-domain:** [[Encryption]] — the digital signature as producing-versus-checking made into infrastructure; [[Physical Quantities and Units]] — rung 1 and the Mars Climate Orbiter; [[Kirchhoff's Laws]] — the loop count as a rung-4 check; [[Resonance]] — rungs 3, 6 and 7 all run on one formula; [[Hilbert vs Brouwer]] — where the small trusted kernel got its logic; [[Program Design]] — testing as the software profession's ladder; [[Compression Is Intelligence]] — the sibling: that card says understanding is *prediction*, this one says the retained skill is *checking*, and a good predictor is the cheapest verifier there is.

- **Misconception traps cleared:** verifying is redoing; if I can check it I could have done it; AI removes the need to understand; confident answers are probably right; a check that always passes is reassuring; verification is for exams.

## Sources

- S. A. Cook, *The complexity of theorem-proving procedures* (1971); L. Levin (1973) — NP as the class of problems with polynomial-time checkable certificates. The timings in Part I were made on 2026-09-14 by `learning-as-verification-asymmetry.py`.
- R. L. Rivest, A. Shamir and L. Adleman, *A method for obtaining digital signatures and public-key cryptosystems* (1978) — signing with the private key, verifying with the public one.
- K. Appel and W. Haken, *Every planar map is four colorable* (1977). G. Gonthier, *Formal proof — the Four-Color Theorem*, Notices of the AMS 55 (2008) — the Coq verification and the small-kernel argument; the de Bruijn criterion is named in H. Barendregt and F. Wiedijk, *The challenge of computer mathematics* (2005).
- Luca Pacioli, *Summa de arithmetica, geometria, proportioni et proportionalità* (Venice, 1494), the tractate *Particularis de computis et scripturis* — the first printed account of double-entry bookkeeping and the trial balance.
- NASA, *Mars Climate Orbiter Mishap Investigation Board Phase I Report* (1999) — pound-force seconds against newton seconds at the software seam.
- H. P. Luhn, US Patent 2 950 048, *Computer for verifying numbers* (filed 1954, granted 1960). The ISBN-10 check is ISO 2108 (1970). Both are run in `learning-as-verification-checkdigit.py`.
- R. Parasuraman and D. H. Manzey, *Complacency and bias in human use of automation: an attentional integration*, Human Factors 52 (2010). R. P. Feynman, *Cargo Cult Science*, Caltech commencement address (1974) — "you must not fool yourself".
- The degrees-of-freedom simulation of Part III was run on 2026-09-14 by `learning-as-verification-nu.py` (4 000 Poisson samples of 300; a $3 \times 4$ multinomial table), with SciPy's `chi2_contingency` as the independent count.
