---
chinese: P 与 NP 问题 (P yǔ NP wèntí)
prerequisites:
  - "[[Turing Machine]]"
  - "[[Big-O Notation]]"
leads_to: []
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/theory-of-computation
  - domain/complexity-theory
  - level/A-Level
  - level/university
  - type/deep
  - type/cross-domain
  - misconception/np-means-non-polynomial
  - misconception/np-complete-means-unsolvable
  - misconception/quantum-solves-np
  - misconception/p-vs-np-is-settled
---

# P vs NP P 与 NP 问题

> *Some problems are hard to **solve** but easy to **check**. Sudoku is agony to fill in and trivial to verify once filled. A jigsaw takes an afternoon to assemble and a glance to confirm. The deepest unsolved question in computer science asks whether that gap is real: **is finding an answer fundamentally harder than recognising one?** A proof either way is worth a million dollars — and nobody, in over fifty years, has found one.*

## The one question

Here is the whole problem in a sentence: **if a solution can be *verified* quickly, can it also be *found* quickly?**

That distinction — **finding** vs **checking** — is the entire subject, so hold onto a concrete case. A filled-in Sudoku grid can be checked for correctness in seconds: scan each row, column, and box for duplicates. But *finding* the solution to a blank hard Sudoku can take a person an hour of backtracking, and a 100×100 generalisation can defeat a computer. Checking is cheap; finding looks expensive. The question **P vs NP** asks whether that appearance is the truth, or whether — for *every* problem whose answers are easy to check — there is some clever fast method to find them that we simply haven't discovered yet.

Almost every computer scientist believes finding really is harder than checking (that **P ≠ NP**). Almost none of them can prove it. That gap between universal belief and total absence of proof is what makes this the most famous open problem in the field.

## 中文锚点

**P 与 NP 问题**问的是一句话：**如果一个答案能被快速*验证*，它能不能也被快速*找到*？**

- **P** = 能在**多项式时间**内**解出**的问题（"易解"/可行）。
- **NP** = 给一个候选答案，能在多项式时间内**验证**对错的问题。（NP = *Nondeterministic Polynomial*，**不是** "Non-Polynomial"——这是头号误解。每个 P 问题都在 NP 里：$P \subseteq NP$。）
- **核心问题：$P = NP$ 吗？** 即"验证容易"是否意味着"求解也容易"。
- **NP-complete（NP 完全）**：NP 里**最难**的一类——所有 NP 问题都能在多项式时间内**归约**到它。只要其中**任何一个**有多项式解法，$P=NP$ 全部解决。
- **NP-hard（NP 困难）**：至少和 NP 里最难的一样难，但本身**不一定**在 NP 里。

类比：填数独很难，验证已填好的数独很容易。**找** vs **验**，就是这个问题的全部。绝大多数人相信 $P \neq NP$，但无人能证明——它是七个**千禧年大奖难题**之一，悬赏一百万美元。

## P — the problems we can actually solve

> Recall that [[Big-O Notation]] sorts algorithms by how their cost grows with input size $n$, and draws one line above all others: between **polynomial** time $O(n^k)$ for some fixed power $k$ ("tractable") and **exponential** time $O(2^n)$, $O(n!)$ ("intractable" — a wall no faster computer climbs).

**P** is the class of decision problems (yes/no questions) a normal computer can solve in **polynomial time**. Sorting a list ($O(n \log n)$), searching it ($O(\log n)$), checking whether a number is prime (polynomial, since 2002), finding the shortest path through a road network (Dijkstra, polynomial) — all in P. "In P" is the formal version of "we have a genuinely usable algorithm." When a problem is in P, scaling the input ten-fold scales the work by a fixed polynomial factor, not by exploding.

## NP — the problems we can at least *check*

**NP** is the class of problems where, *given a candidate answer*, you can **verify** it in polynomial time. The candidate is called a **certificate** (or "witness"): a piece of evidence that, if you had it, would let you confirm the "yes" answer fast.

- **Sudoku:** the certificate is a filled grid; checking it is polynomial.
- **The travelling salesman (decision form):** "is there a route visiting all cities with total length under $k$?" The certificate is a specific route; adding up its length and comparing to $k$ is trivial.
- **Boolean satisfiability (SAT):** "is there an assignment of true/false to these variables making this logical formula true?" The certificate is the assignment; plugging it in and evaluating is fast.

The name is the most misunderstood acronym in computing. **NP stands for *Nondeterministic Polynomial*, not "Non-Polynomial."** It comes from an equivalent definition using the [[Turing Machine|nondeterministic Turing machine]] from the previous card — a machine allowed to *branch* and explore all possibilities at once, accepting if *any* branch succeeds. Such a machine could "guess" the certificate and check it in polynomial time. So NP is "solvable in polynomial time *if you're allowed to guess perfectly*."

Two facts pin NP in place:

- **$P \subseteq NP$.** Every problem you can *solve* quickly you can also *check* quickly — just solve it yourself and compare. So P sits entirely inside NP.
- **The open question is whether the containment is strict.** Is there anything in NP that is *not* in P — a problem easy to check but genuinely hard to solve? Or does $P = NP$, with every checkable problem secretly solvable?

## What "P = NP" would actually mean

If $P = NP$, then for every problem whose answers we can recognise, we could also *generate* them just as fast. The consequences are so sweeping they are the main reason people believe it's **false**:

- **Mathematics would change character.** A formal proof is *checkable* in polynomial time (that's what "formal" means). If $P=NP$, then *finding* a proof would be about as easy as *checking* one — a computer could discover proofs of theorems as fast as it can verify them. Mathematical creativity would become a search you can automate.
- **So would every creative search.** As Scott Aaronson puts it: if $P=NP$, then "everyone who could appreciate a symphony would be Mozart; everyone who could recognise a good investment strategy would be Warren Buffett." Recognising genius and producing it would collapse into the same difficulty.
- **Cryptography as we know it would break** (more below).

A world where finding is as easy as checking is a world too good — and too strange — to be true. That intuition is not a proof, but it is why the betting is so lopsided.

## NP-complete — the hardest problems in NP, and "solve one, solve all"

Here is the idea that turned P vs NP from a question into a *structure*. Some problems in NP are **NP-complete**: they are the **hardest problems in NP**, in a precise sense — *every* problem in NP can be **reduced** to any one of them in polynomial time. They are universal. And that universality has a staggering consequence:

> **If even one NP-complete problem has a polynomial-time algorithm, then $P = NP$ — every problem in NP falls at once.** Conversely, if any NP problem is genuinely intractable, then *all* the NP-complete ones are too.

The thousands of NP-complete problems are, deep down, the *same problem* wearing different clothes. Crack any single one efficiently and the whole edifice collapses into P. Fifty years of the world's best algorithmists attacking them from every angle, with not one cracked, is the strongest *practical* evidence that $P \neq NP$.

This wasn't obvious — it's a theorem. In 1971 **Stephen Cook** (and independently **Leonid Levin** in the USSR) proved the first one: **SAT**, Boolean satisfiability, is NP-complete — every NP problem reduces to it. A year later **Richard Karp** showed 21 more classic problems are NP-complete, and the floodgates opened. The roster now runs to thousands: the travelling salesman, graph colouring, the knapsack problem, clique-finding, Hamiltonian paths, subset-sum, scheduling, protein folding. They are everywhere precisely because so many real tasks are secretly the same hard problem.

### Reductions — the lever that does all the work

A **reduction** from problem $A$ to problem $B$ (written $A \le_p B$) is a polynomial-time procedure that **translates any instance of $A$ into an instance of $B$** such that the answers agree. Its power is a single logical move:

> If $A \le_p B$ and you have a fast solver for $B$, you have a fast solver for $A$ (translate, then solve $B$). **Contrapositive:** if $A$ is known to be hard, then $B$ is at least as hard.

![[p-vs-np-reduction.svg|620]]
*A reduction turns a solver for $B$ into a solver for $A$. So a reduction carries **easiness forward** ($B$ easy $\Rightarrow A$ easy) and **hardness backward** ($A$ hard $\Rightarrow B$ hard). To prove a new problem $B$ is NP-hard, you reduce a problem already known to be hard **into** $B$ — showing $B$ is at least as tough as the worst of NP.*

This is the same spirit as the [[Turing Machine|halting-problem]] argument, where one impossible problem was used to prove others impossible by reduction. There the currency was *undecidability*; here it is *intractability*. Reduction is how a single hard problem (SAT) propagates its hardness across an entire field.

## NP-hard — at least as hard, but maybe not in NP

The last piece of vocabulary. A problem is **NP-hard** if *every* NP problem reduces to it — it is at least as hard as everything in NP — **but it need not be in NP itself.** It might not even be a yes/no question, and it might not be checkable in polynomial time at all.

The relationships click together cleanly:

- **NP-complete = NP **and** NP-hard.** The NP-complete problems are exactly the ones that are *both* hard enough (NP-hard) *and* still checkable (in NP).
- **Some NP-hard problems sit beyond NP entirely.** The *optimisation* travelling salesman — "find the **shortest** tour" (not just "is there one under $k$?") — is NP-hard but not in NP, because verifying that a tour is *the* shortest is not obviously a quick check. The [[Turing Machine|halting problem]] is NP-hard too — and, being undecidable, lies hopelessly outside NP. NP-hard reaches up past the checkable into the genuinely impossible.

## The map — two possible worlds

Everything above lives in one picture, and the whole drama is **which of two worlds we are in**:

![[p-vs-np-worlds.svg|680]]
*Left — the world almost everyone believes ($P \neq NP$): P sits **strictly inside** NP, the NP-complete problems form NP's hardest layer (the overlap with NP-hard), and a no-man's-land of **NP-intermediate** problems sits between. Right — the collapse ($P = NP$): P, NP, and NP-complete become **one and the same class**; only the NP-hard problems outside NP (like the halting problem) remain beyond reach. We do not know which world is real.*

## Problems you can feel

The classes click into place once you hold real problems — and the most instructive cases are **pairs of nearly-identical problems that fall on opposite sides of the line.** Here is the quick map, then the worked detail.

| Problem | Class | Finding an answer | Checking a given answer |
|---|---|---|---|
| Shortest route from A to B | **P** | fast (Dijkstra) | fast |
| "Is $N$ prime?" | **P** | fast (AKS, 2002) | fast |
| "What are $N$'s prime factors?" | **NP-intermediate** (suspected) | hard (RSA bets on it) | fast (just multiply) |
| Sudoku ($n^2 \times n^2$) | **NP-complete** | hard (backtracking) | trivial (scan rows/cols/boxes) |
| SAT (satisfy a Boolean formula) | **NP-complete** | hard (up to $2^n$ tries) | trivial (plug in) |
| TSP: "a tour shorter than $k$?" | **NP-complete** | hard | trivial (add up the legs) |
| TSP: "**the** shortest tour" | **NP-hard** | hard | not even easy to check |
| "Does this program halt?" | **NP-hard** + undecidable | impossible | impossible |

### Shortest path is easy; *longest* path is not (P vs NP-hard)

**Shortest path** is the friendliest hard-sounding problem in computing, because it isn't hard at all. Ask a map app for the quickest way from A to B and **Dijkstra's algorithm** answers in a heartbeat: start at A, repeatedly extend the cheapest-so-far frontier outward like water spreading across the map, and the first time the flood reaches B you are *provably* done. On a map with $n$ junctions it runs in about $O(n \log n)$ — squarely in **P**. The reason it's easy is **optimal substructure**: any slice of a shortest path is itself a shortest path, so the algorithm never has to gamble — the greedy choice is always safe.

Now change one word. Ask for the **longest** path that visits no junction twice. It looks like the same problem with a sign flipped — and it is **NP-hard**. The substructure that saved us is gone: a slice of a longest *simple* path need not be longest, so greed leads you into dead ends, and the "visit nothing twice" rule means you may have to weigh exponentially many routes against each other. One word — *shortest* to *longest* — carries you clean across the P-vs-NP divide. Two problems a child could tell apart, and we can solve one in a blink and not the other. That is the whole mystery, in miniature.

### "Is it prime?" is easy; "what are the factors?" may not be (P vs NP-intermediate)

Hand a computer a 300-digit number and ask **"is it prime?"** — it answers in well under a second. Since the **AKS algorithm (2002)**, primality testing is provably in **P**: you can certify a number prime *without ever finding a factor*. But ask **"what are its prime factors?"** and the same computer may grind for longer than the universe has existed. Factoring is in NP (a proposed factor is checked by a single multiplication) yet is *not believed* to be in P — the prime suspect for **NP-intermediate**. The whole of **RSA encryption** lives in this crack: a public key is the product of two enormous primes — easy to *multiply* (anyone can lock a message) and believed hard to *factor* (only the holder of the primes can unlock it). The padlock on a bank login is a working bet that finding is harder than checking — the P-vs-NP question, deployed.

### Sudoku — the asymmetry in your hands (NP-complete)

You have already *felt* P vs NP if you've ever done a hard Sudoku. **Checking** a finished grid is the work of a moment: scan each row, each column, each box, and confirm 1–9 appear once. A few hundred glances — and for the generalised $n^2 \times n^2$ board it stays polynomial. **Solving** a blank grid is another world: you pencil in a digit, follow its consequences, hit a contradiction, rub it out and try again (**backtracking**), and the puzzles rated "hard" are hard precisely because they force the search deep before it collapses. Generalised Sudoku is **NP-complete** — the newspaper puzzle is a bite-sized instance of a problem that, scaled up, *the entire field cannot solve quickly.* The minutes-to-solve-versus-seconds-to-check gap you feel at the kitchen table **is** the open problem, sitting in your hands.

### SAT — the problem every other NP problem hides inside (NP-complete)

**SAT** (Boolean satisfiability) is the keystone of the chapter: the *first* problem proven NP-complete, and the one everything else reduces to. The question — given a logical formula over true/false variables, is there an assignment that makes it **true**? Take

$$(x_1 \lor x_2) \;\land\; (\lnot x_1 \lor x_3) \;\land\; (\lnot x_2 \lor \lnot x_3)$$

three clauses joined by AND, each clause an OR of variables or their negations. **Finding** a satisfying assignment means searching: 3 variables give $2^3 = 8$ combinations; 100 variables give $2^{100}$ — more than the atoms in the observable universe. But **checking** a proposed answer is instant. Try $x_1=\text{T},\, x_2=\text{F},\, x_3=\text{T}$: clause 1 is $\text{T} \lor \text{F} = \text{T}$, clause 2 is $\text{F} \lor \text{T} = \text{T}$, clause 3 is $\text{T} \lor \text{F} = \text{T}$ — all true, confirmed in three glances. Finding is exponential; checking is trivial. There it is again.

Why is SAT *the* universal hard problem? Here is the felt version of the **Cook–Levin theorem**. Every problem in NP has a polynomial-time **verifier** — and a verifier is nothing but a circuit of AND/OR/NOT [[Logic Gates|gates]] reading the input together with a candidate certificate. "Does there exist a certificate that makes this verifier output *yes*?" is **literally a SAT question** about that circuit. So *every* NP problem can be rewritten as a SAT instance — SAT is the **assembly language of hardness**. Crack SAT efficiently and all of NP falls at once ($P = NP$). The twist the engineers love: despite the worst case being intractable, modern **SAT solvers** routinely dispatch instances with *millions* of variables — they verify microchips and schedule airlines every day. "NP-complete" bites in the *worst* case, not in every case.

### The travelling salesman — where NP-complete becomes NP-hard

The salesman ties the last knot: the precise difference between NP-complete and NP-hard, in one scenario. He must visit $n$ cities and return home.

- **Decision form** — *"is there a route shorter than $k$ kilometres?"* — is **NP-complete.** A "yes" comes with a certificate (the route); you verify it by adding up the legs and comparing to $k$. Finding it is the hard part: $n$ cities allow $(n-1)!/2$ distinct tours — 15 cities is already 43 billion, 20 cities is about $10^{16}$. Brute force dies young.
- **Optimisation form** — *"what is **the** shortest route?"* — is **NP-hard but not in NP.** Hand me a tour and claim it is *the* shortest, and I cannot verify that quickly: to be sure, I'd have to rule out every other tour. The optimisation version sits *above* NP — at least as hard as the decision version, and not even efficiently *checkable*.

That one step — from "is there one under $k$?" to "which is best?" — is the step from NP-complete to NP-hard. And NP-hard reaches further still: the [[Turing Machine|halting problem]] is NP-hard too, yet **undecidable** — not merely expensive but impossible, the far country beyond NP entirely.

## Why it matters — the internet is built on the gap

This is not a curiosity for theorists. A great deal of the modern world quietly *depends* on $P \neq NP$:

- **Cryptography.** Public-key encryption (the padlock securing every bank login and message) rests on certain problems being easy to check but hard to solve — easy to verify a key works, hard to find it. If $P = NP$ with a practical algorithm, much of that hardness evaporates and secure communication as we know it collapses. The security of the internet is a *bet* that finding is harder than checking.
- **Optimisation is everywhere, and most of it is NP-hard.** Routing delivery trucks, scheduling airlines and factories, laying out microchips, folding proteins, packing cargo — all NP-hard. We don't solve them exactly; we lean on **heuristics** and **approximation algorithms** that get *good* answers, not provably *optimal* ones. A constructive $P=NP$ proof would hand us exact solutions to all of them and reshape logistics, medicine, and engineering overnight.
- **The philosophical stakes.** P vs NP is, at bottom, a question about whether *creativity can be mechanised* — whether the leap of discovery is fundamentally harder than the labour of verification. Most of us feel, in our bones, that it is. Proving it is another matter.

## What we know — and why it's so stubborn

- **The status.** Formalised in 1971; open ever since. Repeated polls of experts (Gasarch's surveys, 2002 / 2012 / 2019) find a large majority expect $P \neq NP$. It is one of the seven **Clay Millennium Prize Problems** — \$1,000,000 for a correct proof either way.
- **We have proven *why proving it is hard*.** Three "barrier" results show whole families of techniques *cannot* settle it: **relativization** (Baker–Gill–Solovay, 1975), **natural proofs** (Razborov–Rudich, 1994), and **algebrization** (Aaronson–Wigderson, 2008). Each says, roughly, "any proof using only *these* tools would prove too much, or contradict known facts." A solution will need genuinely new mathematics — which is part of why the prize is still unclaimed.
- **There may be a middle.** **Ladner's theorem (1975):** *if* $P \neq NP$, then there must exist **NP-intermediate** problems — in NP, but neither in P nor NP-complete. **Factoring** integers and **graph isomorphism** are the famous suspects: in NP, not known to be in P, but not believed to be NP-complete either. (This matters for the quantum point below.)

> [!warning] "Quantum computers will solve NP-complete problems."
> This is the most common modern misconception, and it's false (as far as anyone knows). **Shor's algorithm** factors integers fast on a quantum computer — which is why it threatens RSA — but **factoring is *not* NP-complete** (it's a suspected NP-intermediate problem). For genuine NP-complete problems, the best quantum tool, **Grover's algorithm**, gives only a *quadratic* speedup (searching $N$ possibilities in $\sqrt{N}$ steps) — which turns $2^n$ into $2^{n/2}$, still exponential. The class quantum computers solve efficiently (**BQP**) is **not** believed to contain NP-complete problems. Quantum computing breaks *specific* problems; it does not collapse P vs NP.

## The lineage — from "can it be done?" to "how fast?"

This card is the third step of an arc that began with the [[Turing Machine]]:

1. **Computability** (Turing, 1936): *which* problems can be solved at all? The [[Turing Machine|halting problem]] is the first that **cannot** — undecidable, full stop.
2. **Complexity** (this card): among the problems that *can* be solved, **how fast**? P vs NP draws the line between tractable and (believed) intractable.

The halting problem is *impossible*; NP-complete problems are *possible but (probably) infeasible*. Same machine, two different hard edges — one absolute, one about cost.

And there is a quieter, human echo. [[Forward Reading and Problem Discovery]] argues that **verification and discovery are different cognitive acts** — that backward-trained education teaches you to *check* a given answer (the easy direction) while a hunter learns to *find* one nobody handed them (the hard direction). That is P vs NP in cognitive form: checking is NP, finding is the open question. If you have ever felt that recognising a good idea is far easier than having one, you have felt, first-hand, why everyone believes $P \neq NP$.

## Common Misconceptions

> [!warning] "NP means non-polynomial / not solvable in polynomial time."
> NP stands for **Nondeterministic Polynomial**. NP problems are exactly the ones whose answers are *checkable* in polynomial time, and **every P problem is also in NP** ($P \subseteq NP$). Many NP problems (all of P) are perfectly easy. The hard ones are the NP-complete ones — and even those are only *believed* hard.

> [!warning] "NP-complete means impossible / unsolvable."
> NP-complete problems are **decidable** — you can always solve them, e.g. by brute force. The issue is *speed*: the only known algorithms take exponential time in the worst case. That's "infeasible for large inputs," not "impossible." (Contrast the [[Turing Machine|halting problem]], which truly *cannot* be solved at all.)

> [!warning] "P = NP is roughly 50–50 / probably true."
> The expert consensus is heavily toward $P \neq NP$. Believing $P = NP$ means believing that for *thousands* of intensely-studied problems, a fast algorithm exists and the entire field has missed it for fifty years — and that finding a symphony is no harder than recognising one.

> [!warning] "NP-hard problems can never be tackled in practice."
> "NP-hard" is a statement about **worst-case** time. Real instances are often solved well by **heuristics, approximation algorithms, and SAT/TSP solvers** that handle millions of variables. Hardness lives in the worst case; the typical case is frequently manageable. (Modern SAT solvers are an engineering miracle built on top of an "intractable" problem.)

## Exam Notes

P vs NP is **not a named topic** on Cambridge IGCSE 0478 or A-Level 9618 — like the [[Turing Machine]] and [[The Turing Test]], it is theory-of-computation enrichment. But it is one short step beyond content the boards *do* test, and it is the natural destination of the [[Big-O Notation|Big-O]] card:

- **Cambridge 9618 / AP CSA** — both teach Big-O / run-time growth (9618 §19.1; AP CSA §2.12). The polynomial-vs-exponential boundary those topics draw *is* the P-vs-NP line; this card is where "why does exponential matter so much?" gets its real answer.
- **AP Computer Science Principles** — Big Idea on algorithms explicitly includes that some problems are **"unreasonable time"** (no known efficient solution) and must be tackled with heuristics. NP-completeness is the rigorous version of that bullet.
- **IB CS (2027)** — **not a named statement**: the published outline's algorithm content stops at efficiency in the Big-O sense, and no theory-of-computation topic exists. Depth behind the examined efficiency material, exactly as for Cambridge and AP.
- **University** — P, NP, NP-completeness, Cook–Levin, and reductions are the core of every algorithms / theory-of-computation course. This card is the on-ramp; the standard text is Sipser's *Introduction to the Theory of Computation*.
- **General literacy** — "NP-hard" is used (and misused) constantly in software. Knowing it means "no known fast algorithm for the worst case," *not* "impossible," is the difference between giving up and reaching for a good-enough heuristic.

## Connections

- **Prerequisites:** [[Turing Machine]] — P vs NP is phrased in its language (deterministic vs nondeterministic machines, polynomial-time reductions); the beyond-syllabus "doorway to P vs NP" callout there opens straight into this card. [[Big-O Notation]] — supplies the polynomial-vs-exponential measuring stick the whole question rests on.
- **Sibling enrichment (the Turing-review trio):** [[The Turing Test]] — *can a machine think?*; [[Gödel's Incompleteness Theorems]] — *what can be proven?*; this card — *what can be solved efficiently?* Three hard edges seeded by one 1936 machine.
- **The cognitive twin:** [[Forward Reading and Problem Discovery]] — verification-vs-discovery is P-vs-NP for the human mind; the "P vs NP, in cognitive form" callout there is this card's philosophical mirror.
- **Where the hardness is used on purpose:** [[Information Theory]] — cryptography turns the *difficulty* of certain NP / NP-intermediate problems into security; the gap P vs NP asks about is the gap the internet is built on.
- **Foundation it draws on:** [[Logic Gates]] — SAT, the first NP-complete problem, is satisfiability of exactly the Boolean circuits that card builds.

## Glossary / Notation Reference

| Symbol / term | Meaning |
|------|---------|
| **P** | decision problems **solvable** in polynomial time $O(n^k)$ — "tractable" |
| **NP** | decision problems whose answers are **verifiable** in polynomial time (Nondeterministic Polynomial) |
| certificate / witness | the candidate answer a verifier checks for an NP problem |
| $P \subseteq NP$ | every solvable-fast problem is also checkable-fast (P sits inside NP) |
| **NP-complete** | the hardest problems *in* NP; all of NP reduces to each; solve one fast $\Rightarrow P=NP$ |
| **NP-hard** | at least as hard as all of NP, but **not necessarily in NP** (may be unverifiable, or undecidable) |
| NP-intermediate | (if $P \neq NP$) in NP but neither in P nor NP-complete — e.g. suspected factoring, graph isomorphism |
| $A \le_p B$ | $A$ **polynomial-time reduces to** $B$: translate $A$-instances to $B$-instances; $B$ easy $\Rightarrow A$ easy |
| **SAT** | Boolean satisfiability — the first problem proven NP-complete (Cook–Levin, 1971) |
| BQP | problems a quantum computer solves efficiently — **not** believed to contain NP-complete problems |
