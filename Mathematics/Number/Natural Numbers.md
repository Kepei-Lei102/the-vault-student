---
chinese: 自然数 (zìránshù)
prerequisites:
  - "[[Number Sets (Vocab)]]"
  - "[[Set]]"
leads_to:
  - "[[Integers]]"
teach_together:
  - "[[Proof by Induction]]"
  - "[[Recursion]]"
tags:
  - subject/mathematics
  - domain/number
  - domain/set-theory
  - domain/logic
  - level/IGCSE
  - level/university
  - curriculum/Cambridge-0580
  - curriculum/IB-AA
  - curriculum/IB-AI
  - syllabus/0580-E1-1
  - type/definition
  - type/proof
  - notation/natural-numbers
  - misconception/zero-not-natural
  - misconception/successor-is-already-addition
  - misconception/infinity-is-a-natural-number
---

# Natural Numbers 自然数

> You know that $1+1=2$. But if someone took away the meanings of **1**, **+** and **2**, what would you need to build them again?
>
> A starting point. A way to take one more step. And a rule saying there are no hidden numbers outside the construction.

## Definition — counting before calculating

We use

$$\mathbb N=\{0,1,2,3,\ldots\}.$$

A natural number describes the **size of a finite collection**, including an empty one. It can also specify a position or a number of repeated steps. [[Number Sets (Vocab)]] locates these numbers among integers, rationals and reals.

For foundations, the dots need explaining. Begin with a distinguished object **0** and an operation **successor**, written $S$. Its job is to supply the next number:

$$1:=S(0),\qquad2:=S(1),\qquad3:=S(2).$$

At this stage, $S(n)$ is primitive. Writing “$n+1$” would borrow addition before we have defined it. Eventually we will prove that $S(n)=n+1$.

### 中文锚点

往空书包里放书：一本都还没放，就是零本；放进一本，再放一本，就有了一、二、三……自然数要回答的就是“有几个”——数的是书、苹果还是人，都不影响这个数量。包里已有三本，再放两本，就是从三接着数两步：四、五。我们熟悉的加法，原来可以从这么朴素的“再来一个”长出来。这里从零开始，因为“一个也没有”同样是数量。

## Familiar number, unfamiliar representation

| Familiar idea | Foundational version | What it buys us |
|---|---|---|
| Start counting | Distinguished object $0$ | Empty collections have a size |
| One more | Successor $S(n)$ | A primitive step, before addition |
| Add three | Apply successor three times | A definition of addition |
| Prove every case | Base and successor step | A finite proof with infinite reach |
| Store a number | Choose an encoding | Meaning can survive a change of representation |

**Convention matters:** some authors use $\mathbb N=\{1,2,\ldots\}$. Neither notation settles a philosophical dispute. Here $0\in\mathbb N$; write $\mathbb N_{>0}$ when you mean positive naturals. Read a source's own convention before using its symbols.

## 1. Five conditions that make the counting structure

A convenient **Peano-style formulation** describes a set $N$, an element $0$, and a successor operation $S$:

1. **Start:** $0\in N$.
2. **Continue:** if $n\in N$, then $S(n)\in N$.
3. **No return to the start:** $S(n)\ne0$ for every $n\in N$.
4. **No merging:** if $S(a)=S(b)$, then $a=b$. Successor is **injective**.
5. **No extra territory:** if a subset $A\subseteq N$ contains $0$ and contains $S(n)$ whenever it contains $n$, then $A=N$.

The fifth condition is induction in set language. Let $A$ be the numbers for which a statement is true. Prove the statement at zero; prove that truth passes to successor. Then $A=N$.

The first four conditions alone do not exclude a separate, unreachable chain. Imagine the ordinary $0,1,2,\ldots$ alongside a disjoint copy of **all integers**, with successor moving one step right on each chain. Nothing maps to the distinguished zero; no two inputs merge. Yet the ordinary chain is a proper subset containing zero and closed under successor. Condition 5 rejects the extra chain.

![[natural-numbers-axioms.svg|700]]

*The extra chain extends indefinitely in both directions. Its labels are names in a disjoint copy, not identifications with ordinary natural numbers.*

### Why there is no last natural number

**Trigger: successor always exists. Tool: distinguish successive iterates.** If two iterates $S^i(0)$ and $S^j(0)$ were equal with $i<j$, injectivity would cancel $i$ successor steps. We would obtain $0=S^{j-i}(0)$, contrary to condition 3. Thus all the finite iterates are different. Every one has a further successor.

There is no final natural called “infinity.” Each natural is finite; the collection of all naturals is infinite. A procedure can terminate on **every individual input** without having one finite bound that works for all inputs.

> [!info] Beyond syllabus — which induction axiom?
> Recall that condition 5 quantifies over **every subset** of $N$. Read with full second-order semantics, it determines the natural-number structure up to a relabelling that preserves zero and successor. **First-order Peano arithmetic (PA)** instead uses an induction *schema*: one axiom for each formula in its language. PA has nonstandard models; its schema must not be described as excluding every externally imagined subset or extra element. This distinction matters when discussing [[Gödel's Incompleteness Theorems]]. [Open Logic Text, §39.2](https://builds.openlogicproject.org/open-logic-complete.pdf#page=609)

## 2. Build the numbers from sets

The axioms describe the structure. A **model** supplies objects that realise it. In the von Neumann construction,

$$\boxed{0:=\varnothing,\qquad S(n):=n\cup\{n\}.}$$

Read the braces carefully: $n$ is the set of earlier numbers, while $\{n\}$ is a singleton containing that entire set as **one new element**.

$$\begin{aligned}
0&=\varnothing,\\
1&=\{0\}=\{\varnothing\},\\
2&=\{0,1\}=\{\varnothing,\{\varnothing\}\},\\
3&=\{0,1,2\}.
\end{aligned}$$

Each number is the set of all its predecessors. The representation makes $n$ a set with exactly $n$ elements. For these finite ordinals, $m<n$ precisely when $m\in n$; also $m\le n$ precisely when $m\subseteq n$.

**Do not replace union with an extra pair of braces.** $S(2)=2\cup\{2\}=\{0,1,2\}$ has three elements. But $\{2\}$ has just one element: the number 2. [[Element]], [[Subset]] and [[Cardinality]] separate these questions.

![[natural-numbers-construction.mp4]]

*First, preserve the earlier elements and add the old number as one new element. Then use successor repeatedly to compute $2+3$. Labels such as “2” abbreviate the sets already constructed; they are not extra primitive ingredients.*

### Where does the infinite set come from?

Constructing $0$, then $1$, then $2$, and any requested finite number does **not by itself** establish that all these objects form a set.

In standard ZF set theory, the **axiom of infinity** supplies a set $I$ containing $\varnothing$ and closed under $x\mapsto x\cup\{x\}$. Such a set is called *inductive*. Define $\omega$ as the intersection of all inductive subsets of $I$. This intersection is a set, contains zero and is closed under successor.

Why does induction hold for $\omega$? If $A\subseteq\omega$ contains zero and is successor-closed, then $A$ is one of those inductive subsets of $I$. So $\omega\subseteq A$. Combined with $A\subseteq\omega$, this gives $A=\omega$. In this construction, $\mathbb N=\omega$.

This is a foundation **within an axiomatic theory of sets**, not a proof that arithmetic emerges without any assumptions. Infinity is doing real work. Other encodings can realise the same arithmetic structure; the natural number 3 is not intrinsically obliged to wear these particular braces. [Open Logic Text, §65.6–65.8](https://builds.openlogicproject.org/open-logic-complete.pdf#page=868)

## 3. Recursion defines; induction proves

A recursive definition gives a starting value and a rule for each next value:

$$f(0)=a,\qquad f(S(n))=g(n,f(n)).$$

The **recursion theorem for natural numbers** says that, for a specified set of outputs, starting output $a$ and total step function $g$, exactly one such function exists. The full set-theoretic existence proof is a theorem about compatible finite constructions; we use that theorem here.

Uniqueness is easier to see. If $f$ and $h$ follow the same rules, then $f(0)=h(0)=a$. If $f(n)=h(n)$, applying the same $g$ gives $f(S(n))=h(S(n))$. Induction says they agree everywhere.

**Recursion supplies a value. Induction supplies a reason the values obey a claim.** They share the shape because both follow the way the input is built. [Further reading: Logic and Proof, natural numbers and recursion](https://leanprover.github.io/logic_and_proof_lean3/the_natural_numbers_and_induction.html)

### Addition: repeat successor

Fix $a$. Define addition by recursion on the **second argument**:

$$\boxed{a+0=a,\qquad a+S(b)=S(a+b).}$$

Now the promised identity follows:

$$a+1=a+S(0)=S(a+0)=S(a).$$

No appeal to a pre-existing addition operation was needed to name successor. The order of definitions matters.

**Worked construction: $2+3$. Trigger: the right argument is a successor. Tool: the recursive definition.**

$$\begin{aligned}
2+3&=2+S(2)=S(2+2)\\
&=S(S(2+1))\\
&=S(S(S(2+0)))\\
&=S(S(S(2)))=5.
\end{aligned}$$

Every line either peels a successor off the second input or uses the zero clause.

### Multiplication: repeat addition

With addition available, define

$$\boxed{a\cdot0=0,\qquad a\cdot S(b)=a\cdot b+a.}$$

Thus $2\cdot3=(2\cdot2)+2=((2\cdot1)+2)+2=((0+2)+2)+2=6$.

This is the distinction between **three successor steps** and **three additions of a two-item group**. Repeated addition defines multiplication on naturals; extensions to fractions and reals require broader definitions.

## 4. The familiar laws now have to earn their place

Our addition definition treats left and right differently. We cannot use commutativity to prove commutativity.

### First prove $0+n=n$

**Trigger: the definition recurses on the right input. Tool: induction on $n$.**

- Base: $0+0=0$ by the zero clause.
- Step: assume $0+n=n$. Then $0+S(n)=S(0+n)=S(n)$, using the recursion rule and the hypothesis.

Therefore $0+n=n$ for all $n$. This is a **theorem**, whereas $n+0=n$ was our defining clause.

### Next prove $S(a)+b=S(a+b)$

Fix $a$ and induct on $b$.

- Base: $S(a)+0=S(a)=S(a+0)$.
- Step: assume $S(a)+b=S(a+b)$. Then

$$S(a)+S(b)=S(S(a)+b)=S(S(a+b))=S(a+S(b)).$$

The middle equality uses the hypothesis; the others use addition's definition. This lemma lets a successor on the *left* pass through addition.

### Now prove $a+b=b+a$

Fix $a$ and induct on $b$.

- Base: $a+0=a=0+a$, using the definition and the first theorem.
- Step: assume $a+b=b+a$. Then

$$a+S(b)=S(a+b)=S(b+a)=S(b)+a.$$

The last equality uses the successor-on-the-left lemma, not a hidden assumption of commutativity. Hence

$$\boxed{a+b=b+a.}$$

### Associativity is a separate claim

Fix $a,b$ and induct on $c$. At zero, $(a+b)+0=a+b=a+(b+0)$. If $(a+b)+c=a+(b+c)$, then

$$(a+b)+S(c)=S((a+b)+c)=S(a+(b+c))=a+S(b+c)=a+(b+S(c)).$$

So $(a+b)+c=a+(b+c)$. Reordering and regrouping are different permissions, each justified rather than silently borrowed.

## 5. Order, least elements and stopping

Define

$$a\le b\quad\Longleftrightarrow\quad b=a+c\text{ for some }c\in\mathbb N.$$

This says that $b$ is reachable from $a$ by some number of successor steps. Define $a<b$ when $a\le b$ and $a\ne b$. In the von Neumann model this agrees with membership.

Every **nonempty subset of $\mathbb N$ has a least element**: the well-ordering principle. Here is the induction argument in slow motion.

**If a subset $A$ is nonempty, then $A$ has a least element.** To contradict the conclusion, suppose $A$ has **no least element**. We will show $A$ must be empty.

- $0\notin A$, since otherwise zero would be its least element.
- Suppose none of $0,\ldots,n$ belongs to $A$. Then $n+1\notin A$: if it belonged, it would be the least element, because every smaller natural has already been excluded.
- Induction excludes every natural from $A$. Thus $A=\varnothing$, contradicting the nonempty premise.

The initial-segment property used here follows from successor order; it is the familiar order on the finite ordinals. Well-ordering does **not** hold for all familiar ordered sets: the positive real numbers have no least member, because half of any candidate is smaller and still positive.

### Real-world use: prove a loop finishes

A task queue contains $r\in\mathbb N$ unprocessed jobs. Each completed iteration removes exactly one, and no jobs are added. The value $r$ is a **decreasing natural-number measure**. It cannot decrease forever while staying nonnegative, so the loop finishes—provided each individual iteration itself finishes.

```python
def drain(jobs):
    pending = list(jobs)
    completed = []
    while pending:
        completed.append(pending.pop())
    return completed
```

The measure is `len(pending)`. It starts finite and drops by one each iteration. `len(pending) + len(completed)` stays constant: a simple **invariant** tracking where the jobs went. An invariant helps establish correctness; a decreasing measure helps establish termination.

“Decreases” alone is insufficient. Starting at 1 and repeatedly halving gives $1,\tfrac12,\tfrac14,\ldots$, a positive real sequence that never reaches zero. Starting a loop at $-1$ and repeatedly subtracting 1 also never reaches zero. The domain and stopping test are part of the argument.

### Real-world use: a proof assistant's arithmetic

Lean's logical `Nat` has zero and successor constructors. Inductive definitions support recursive functions and proofs about them. This structure is a working tool for machine-checked mathematics, not merely historical vocabulary. Its implementation uses efficient integer representations and arithmetic primitives: logical successor does not require allocating a chain of a billion boxes to represent a billion. [Lean reference: natural numbers, logical model and implementation](https://lean-lang.org/doc/reference/latest/Basic-Types/Natural-Numbers/)

## 6. Hands-on — build two representations

Run the adjacent `natural-numbers-model.py` with Python 3. It implements:

- finite von Neumann numbers as immutable sets;
- unary naturals as empty tuples and one-element tuples;
- addition and multiplication by structural recursion;
- a countdown measure and a finite-word wraparound counterexample.

```python
ZERO = ()

def succ(n):
    return (n,)

def add(a, b):
    return a if b == ZERO else succ(add(a, b[0]))

def mul(a, b):
    return ZERO if b == ZERO else add(mul(a, b[0]), a)
```

These functions assume well-formed unary natural inputs. The tuple `()` represents zero; `((),)` represents one. This is **not** the von Neumann encoding: the two implementations deliberately separate structure from representation. The model file checks that they yield the same small arithmetic results.

Predict before running:

1. Does `succ(succ(ZERO))` have two top-level tuple elements? **No:** one outer element; two successor layers.
2. Does the von Neumann representation of 2 have two elements? **Yes:** 0 and 1.
3. Can these recursive functions efficiently multiply very large inputs? **No:** unary size and recursion depth are serious costs. They illustrate definitions, not production arithmetic.
4. Does an unsigned 8-bit counter satisfy all five conditions? **No:** after 255 it wraps to 0, violating the no-return condition. Mathematical naturals have no largest value.

## Common misconceptions

- **“Zero is not natural.”** It depends on convention; state yours. Zero is indispensable as the size of an empty collection.
- **“A natural number is a digit.”** Digits are symbols in a representation. The same number can be written $5$, binary $101$, or $S(S(S(S(S(0)))))$.
- **“The empty set and its singleton are the same.”** One has no elements; the other has one. Ask what is *inside the outermost braces*.
- **“Induction is testing lots of cases.”** Testing checks a finite sample. The successor step proves a general implication.
- **“Defining arithmetic makes its laws arbitrary.”** Once the structure and recursive definitions are fixed, theorems follow from them. Commutativity was not an extra switch we flipped.
- **“An infinite set contains an infinite natural.”** Every member of $\mathbb N$ is finite. The size of the whole set is a different question; see [[Countability]].

## Beyond syllabus — where the foundation has limits

Recall that first-order PA has an induction schema, whereas the full-subset condition above is stronger as a semantic characterisation. **Goodstein's theorem** is a concrete arithmetic statement true in the standard naturals but not provable in PA. [Kirby and Paris (1982)](https://doi.org/10.1112/blms/14.4.285) established that independence result. This does not invalidate ordinary induction proofs. It limits what that particular formal system can derive. [[Gödel's Incompleteness Theorems]] explains the distinction between truth in an intended structure and provability in a system.

Axioms let us identify our starting commitments. They do not remove the need for starting commitments. Building naturals inside set theory moves that responsibility into set theory; it does not prove the consistency of all mathematics from nowhere.

## Exam Notes

### Cambridge 0580 — C1.1 / E1.1

The 2025–2027 syllabus explicitly requires identifying and using natural numbers alongside integers, primes and other number types. **That vocabulary is examined; Peano axioms, the von Neumann construction and recursive derivations of arithmetic are enrichment.** The syllabus's number-type list does not itself settle a universal zero convention; follow a question's definition.

### OxfordAQA 9260 and Cambridge 0606

9260 **N4** names even/odd/prime vocabulary, factors, multiples, HCF/LCM and prime factorisation. It does not prescribe an axiomatic construction of natural numbers. [[Factors and Multiples (Vocab)]], [[Prime Factorisation (Vocab)]] and [[Number Sets (Vocab)]] supply that elementary scope. The 0606 syllabus uses sets, sequences and positive integer exponents; it does not require Peano axioms or this set-theoretic construction.

### A-Level mathematics

Cambridge **9231 §1.7** examines proof by induction, and §2.5 uses it for de Moivre's theorem. [[Proof by Induction]] supplies the exam method. The foundations here explain why the method has its form; constructing $\mathbb N$ is not a required 9231 task. Cambridge **9709**, OxfordAQA **9660** and the inspected Edexcel **IAL** specification do not name Peano axioms or von Neumann naturals as content requirements. Edexcel IAL's notation list starts $\mathbb N$ at **1**; use that convention when reading it.

### IB mathematics

AA and AI list number systems as prior learning. **AA HL AHL1.15** includes mathematical induction; this does not turn Peano axioms, nonstandard models or Goodstein's theorem into required syllabus material. Neither guide names those foundational treatments as required content. [IB AA guide](https://www.ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-analysis-and-approaches-guide-en.pdf) · [IB AI guide](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-applications-and-interpretation-guide-en.pdf)

### AP and scope boundary

The inspected AP Calculus AB/BC CED does not prescribe Peano arithmetic, set-theoretic number construction or proof by induction as a named method. Do not treat “use integer indices” as an axiomatic-foundations requirement. This is primarily a foundations enrichment treatment; the worked constructions are original mathematical examples, not invented past-paper questions. No specialised exam formula is being added to memorisation lists.

## Connections

- **Prerequisites:** [[Number Sets (Vocab)]] — the number-system vocabulary; [[Set]] — membership and collections.
- **Teach together:** [[Proof by Induction]] — proving every case; [[Recursion]] — computing from base and step.
- **Set machinery:** [[Empty Set]], [[Element]], [[Subset]], [[Union]], [[Cardinality]] — what the construction's braces actually mean.
- **Extensions:** [[Integers]] — make subtraction generally possible; [[Countability]] — compare infinite collections.
- **Limits:** [[Gödel's Incompleteness Theorems]] — distinguish formal proof from truth in the intended naturals.
- **Story:** [[von Neumann the Martian]] — the mathematician behind the standard set representation, alongside very different work in computing.
- **Method:** [[Forward Reading and Problem Discovery]] — follow the changing state, preserve the invariant and identify what makes progress irreversible.

## LaTeX Reference

| Expression | LaTeX | Meaning |
|---|---|---|
| $\mathbb N$ | `\mathbb N` | Naturals, including zero here |
| $S(n)$ | `S(n)` | Successor |
| $n\cup\{n\}$ | `n\cup\{n\}` | von Neumann successor |
| $\omega$ | `\omega` | Set of finite von Neumann ordinals |
| $a+S(b)=S(a+b)$ | `a+S(b)=S(a+b)` | Recursive addition clause |
| $a\cdot S(b)=a\cdot b+a$ | `a\cdot S(b)=a\cdot b+a` | Recursive multiplication clause |
