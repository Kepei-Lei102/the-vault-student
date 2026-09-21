---
chinese: 质数 (zhìshù)
prerequisites:
  - "[[Number Sets (Vocab)]]"
  - "[[Prime Factorisation (Vocab)]]"
  - "[[Proof by Induction]]"
leads_to:
  - "[[Sophie Germain and the Borrowed Name]]"
  - "[[Privacy-Preserving Computation]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - level/A-Level
  - level/university
  - curriculum/Cambridge-0580
  - curriculum/OxAQA-9260
  - curriculum/A-Level
  - curriculum/IB-AA
  - syllabus/0580-E1-1
  - syllabus/9260-N4
  - type/definition
  - type/proof
  - type/algorithm
  - notation/divides
  - misconception/one-is-prime
  - misconception/euclid-number-always-prime
  - misconception/primality-is-factorisation
---

# Prime Numbers 质数

> Twelve chairs can make two equal rows of six, or three of four. Thirteen chairs refuse every rectangular arrangement except one row of thirteen.
>
> That small refusal turns out to organise multiplication. Every whole number greater than one can be taken apart into primes—and however you take it apart, the final ingredients agree.

## Definition — multiplication's indivisible pieces

A **prime number** is an integer greater than $1$ with exactly two **positive divisors**: $1$ and itself. A **composite number** is an integer greater than $1$ with a nontrivial factorisation $n=ab$, where $1<a,b<n$.

$$2,3,5,7,11,13,17,19,23,29,\ldots$$

The first prime is $2$, the only even prime: every larger even number has $2$ as a divisor different from $1$ and itself. Oddness is necessary for primes beyond $2$, but not sufficient: $9=3\times3$ and $15=3\times5$.

**One is neither prime nor composite.** It has one positive divisor, not two. Its role in multiplication is to leave other numbers unchanged. If we counted $1$ as a prime ingredient, $6=2\times3=1\times2\times3=1\times1\times2\times3$ would give arbitrarily many ingredient lists. Excluding $1$ lets unique factorisation say exactly what we want it to say.

The positive-integer convention also excludes zero and negative numbers from this classification. When factoring a negative integer, separate out a factor $-1$ and factor its positive magnitude.

### 中文锚点

摆教室的椅子时，12把可以摆成两排、每排6把，也可以摆成三排、每排4把。换成13把，想让每排一样多、不剩椅子，而且不只摆一排，也不让每排只有一把，就怎么摆都不成。这种“没法再整齐拆开”的数量，就是质数。它不是说13个东西不能分，而是说：你一旦要求分成同样大的整组，就只剩“一整组”和“每组一个”这两条路。

## Notation — “divides” is a statement

| Notation | Meaning | Example |
|---|---|---|
| $a\mid b$ | $b=ak$ for some integer $k$ | $3\mid12$ because $12=3\times4$ |
| $a\nmid b$ | No such integer $k$ exists | $5\nmid12$ |
| $\gcd(a,b)$ | Greatest common divisor, also HCF | $\gcd(12,18)=6$ |
| $a\equiv r\pmod m$ | $a$ and $r$ leave the same remainder modulo $m$ | $17\equiv2\pmod5$ |
| $\pi(x)$ | Number of primes at most $x$ | $\pi(10)=4$; unrelated to the circle constant |

The vertical bar is not a fraction bar: $3\mid12$ is true or false; $12/3$ is a number. **Coprime** means a pair has gcd $1$; neither number must be prime. For instance, $8$ and $15$ are coprime composites.

## 1. Finding a prime — why the square root is the stopping point

Suppose $n=ab$ is composite. If both positive factors exceeded $\sqrt n$, then

$$ab>\sqrt n\sqrt n=n,$$

contradicting $ab=n$. At least one factor is therefore at most $\sqrt n$; that factor has a prime divisor no larger than itself.

So to test $n>1$, it is enough to check **prime divisors up to and including $\sqrt n$**. The equality matters: missing it would misclassify $49=7^2$.

**Original worked example — is $97$ prime?**

*Trigger: one number to classify. Tool: the square-root divisor bound.* Since $9^2<97<10^2$, only $2,3,5,7$ need testing. The number is odd; its digit sum is $16$; its last digit is not $0$ or $5$; and $97=7\times13+6$. None divides it, so $97$ is prime. We did not need to try $11$, let alone $96$.

### Many primes at once — the sieve of Eratosthenes

Trial division tests one candidate at a time. A **sieve** reverses the direction: start with a range of candidates and remove numbers already known to be products.

1. List the integers from $2$ to a chosen bound $B$.
2. The smallest surviving unprocessed number $p$ is prime. If it were composite, a smaller prime factor would already have removed it.
3. Retain $p$, but cross out its multiples from $p^2$ onward. Earlier multiples $2p,3p,\ldots,(p-1)p$ already have smaller prime factors.
4. Continue until the next surviving $p$ has $p^2>B$. The square-root argument guarantees that every remaining number is prime.

![[prime-numbers-sieve.mp4]]

Watch $2,3,5,7$ remove the composites up to $100$. Green numbers survive; dim red numbers are removed. The next survivor is $11$, whose square exceeds the bound. The second half explains that stopping rule and then builds a number that escapes a finite list of primes. **The sieve proves a finite classification; the infinitude proof below has a different job.**

## 2. Why there must always be another prime

A long list of primes does not prove that primes continue forever. A proof must defeat **every possible finite list**, however long.

The invariant to exploit is **divisibility**. Multiply the numbers on a proposed list, and the product is divisible by each one. Add $1$, and every listed prime now leaves remainder $1$.

### Euclid's argument, in contradiction form

**Implication to test:** if $p_1,\ldots,p_k$ were all the primes, then every integer greater than $1$ would have a prime divisor on that list. Call that conclusion $Q$.

We will construct **not $Q$**: an integer greater than $1$ with no prime divisor on the list.

1. **Assume there are finitely many primes**, and list all of them as $p_1,\ldots,p_k$.
2. Form $P=p_1p_2\cdots p_k$ and $N=P+1$.
3. Since $N>1$, it has a prime divisor $q$. Only **existence** of a prime factor is needed here, not uniqueness: repeatedly split a composite into smaller factors until a prime is reached.
4. Every listed $p_i$ divides $P$. If it also divided $N$, it would divide their difference $N-P=1$.
5. A prime is greater than $1$, so it cannot divide $1$. Thus **no listed prime divides $N$**.
6. The prime divisor $q$ therefore lies outside the supposedly complete list: **not $Q$**.
7. The assumption forced $Q$ but our construction gave not $Q$. It is false: there are infinitely many primes. $\square$

**What the “+1” accomplishes:** it does not make $N$ prime. It makes $N$ escape divisibility by every prime you listed.

For the first six primes,

$$2\cdot3\cdot5\cdot7\cdot11\cdot13+1=30031=59\cdot509.$$

The new number is composite. Both its prime factors are new to the list. The proof succeeds anyway.

![[prime-numbers-euclid.svg|740]]

There is also a direct reading: **give me any finite list of primes, and I can establish that some prime is missing.** Euclid's *Elements* IX.20 is an ancient source for this idea; the arbitrary-list algebra is modern notation. [Euclid IX.20](https://mathcs.clarku.edu/~djoyce/elements/bookIX/propIX20.html)

## 3. Why different factor trees reach the same ingredients

[[Prime Factorisation (Vocab)]] teaches how to build a factor tree. [[Proof by Induction]] §“Strong induction” proves that a prime factorisation **exists**: either $n$ is prime, or it splits into smaller numbers already covered by the induction hypothesis.

But existence does not give **uniqueness**. Two different trees might, in principle, finish with different prime ingredients. We need a reason that cannot happen.

![[prime-numbers-factor-trees.svg|740]]

The diagram shows two decompositions of $60$. Their leaves agree after reordering. It illustrates the claim; two trees alone do not prove it for every integer.

### The hinge — Euclid's lemma

For a prime $p$,

$$\boxed{p\mid ab\quad\Longrightarrow\quad p\mid a\ \text{or}\ p\mid b.}$$

A prime cannot be assembled partly from one factor and partly from another without dividing one of them. This fails for a composite: $6\mid2\cdot3$, yet $6$ divides neither $2$ nor $3$.

**Avoid a circular proof.** Saying “look at the prime factors of $a$ and $b$” and assuming those lists are unique would use the very theorem we are trying to establish. Instead, we will prove the lemma using a small fact about gcds.

### Why coprime integers can combine to make $1$

**Bézout's identity, coprime case:** if positive integers $a,b$ have gcd $1$, there exist integers $x,y$ such that $ax+by=1$. The coefficients may be negative.

Here is a proof, using the well-ordering principle behind [[Natural Numbers]].

1. Consider all **positive** integers of the form $ax+by$, with integer $x,y$. At least one exists: $a=a\cdot1+b\cdot0$.
2. Let $d=ax_0+by_0$ be the smallest such positive integer.
3. Divide $a$ by $d$: $a=kd+r$, where $0\le r<d$.
4. Then $r=a-k(ax_0+by_0)=a(1-kx_0)+b(-ky_0)$, another integer combination.
5. If $r>0$, it would be a smaller positive combination than $d$. Therefore $r=0$, so $d\mid a$.
6. Applying the same reasoning to $b$ gives $d\mid b$.
7. Since $a,b$ have no common divisor greater than $1$, $d=1$. Thus $ax_0+by_0=1$. $\square$

**Now prove Euclid's lemma.** Suppose $p\mid ab$. If $p\mid a$, we are done. Otherwise, the only positive divisors of $p$ are $1,p$, so $\gcd(p,a)=1$. Bézout gives $xp+ya=1$. Multiply by $b$:

$$b=xpb+yab.$$

Both terms on the right are divisible by $p$: the first contains $p$ explicitly, and the second uses the hypothesis $p\mid ab$. Hence $p\mid b$. $\square$

The structure is reusable: **coprime with one factor → that factor cannot supply the divisibility → the other factor must supply it.**

### The Fundamental Theorem of Arithmetic

Every integer $n>1$ is a product of primes, **uniquely apart from their order**. Equivalently,

$$\boxed{n=p_1^{a_1}p_2^{a_2}\cdots p_r^{a_r},\qquad p_1<\cdots<p_r,\quad a_i\ge1,}$$

with exactly one choice of primes and exponents.

Existence came from splitting/strong induction. For uniqueness, suppose two prime products give the same $n$:

$$p_1p_2\cdots p_r=q_1q_2\cdots q_s.$$

- The prime $p_1$ divides the right-hand product. Repeated use of Euclid's lemma says it divides some $q_j$.
- Since $q_j$ is prime and $p_1>1$, this forces $p_1=q_j$.
- Reorder that matching factor to the front and cancel it from both sides.
- Repeat on the shorter products. If one side ran out first, we would have $1$ equal to a nonempty product of primes, which is impossible.
- Both sides therefore contain the same primes with the same multiplicities. $\square$

**The takeaway:** factor trees may branch differently, but a prime on one side must find an identical partner on the other. The freedom is in the route, not the destination.

## 4. The exponent view — multiplication becomes bookkeeping

Once the primes are fixed, a positive integer can be described by its prime exponents. For example,

$$72=2^3\cdot3^2,\qquad120=2^3\cdot3\cdot5.$$

Multiplying numbers adds matching exponents. Exact division subtracts them. This turns several familiar methods into consequences of one structure:

| Task | What the exponents must do | Why |
|---|---|---|
| $a\mid b$ | Each prime exponent of $a$ is at most its exponent in $b$ | The quotient must have nonnegative integer exponents |
| HCF / gcd | Take the smaller exponent for each prime | Largest collection of ingredients both possess |
| LCM | Take the larger exponent for each prime | Smallest collection containing both |
| Perfect square | Every prime exponent is even | Squaring doubles every exponent |
| Perfect $k$th power | Every prime exponent is a multiple of $k$ | Taking the $k$th power multiplies every exponent by $k$ |

Absent primes have exponent zero. This is why the HCF/LCM rules in [[Factors and Multiples (Vocab)]] work, and why prime factorisation helps simplify [[Surds]].

**Original worked example — make $540$ a square.** Find the smallest positive integer $m$ such that $540m$ is a perfect square.

*Trigger: a whole-number square. Tool: every prime exponent must be even.* Since $540=2^2\cdot3^3\cdot5$, only the exponents of $3$ and $5$ are odd. Supply one of each:

$$m=3\cdot5=15,\qquad540\cdot15=8100=90^2.$$

Why smallest? Any valid multiplier must supply an odd exponent of both $3$ and $5$, so it is divisible by $15$. Extra pairs of primes only make it larger.

## 5. A real exam: “always” can fall to one example

**Pearson Edexcel IAL P2, January 2021, WMA12/01 Q5(ii), 1 mark.** Disprove the claim that any three successive entries in the prime-number sequence sum to a multiple of five. [Question paper](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Exam-materials/WMA12_01_que_20210304.pdf)

*Trigger: a universal claim to disprove. Tool: one counterexample.* The consecutive primes $5,7,11$ have sum $23$, which is not divisible by $5$. Therefore the claim is false. This is the example accepted in the published scheme.

“Consecutive primes” means neighbours in the **prime sequence**, not consecutive integers. Also, $2+3+5=10$ does not help: one successful case cannot establish “always.” A counterexample must break the conclusion while still satisfying the premise.

**Transfer challenge:** prove every prime $p>3$ has the form $6k-1$ or $6k+1$. Then explain why the converse fails.

*Tool: exhaustion by remainders modulo $6$.* Remainders $0,2,4$ give an even number; remainder $3$ gives a multiple of $3$. For $p>3$, only $1$ or $5$ remains. But $25=6\cdot4+1$ is composite. The filter keeps every prime above $3$; it also keeps some composites.

## 6. Where primes do work — computing with remainders

A prime modulus has a useful guarantee: **every nonzero remainder has a multiplicative inverse**. For prime $p$ and $1\le a<p$, we have $\gcd(a,p)=1$. Bézout gives $ax+py=1$, so reducing modulo $p$ gives

$$ax\equiv1\pmod p.$$

For example, $3\times5=15\equiv1\pmod7$, so multiplying by $5$ undoes multiplying by $3$ modulo $7$. Modulo $6$, multiplying by $2$ loses information: $2\cdot1\equiv2\cdot4\equiv2$. There is no inverse for $2$ there.

This ability to divide by any nonzero element is the structure of a **finite field**. It supports polynomial interpolation and error-correcting codes: a receiver uses enough surviving values to reconstruct missing information. [[Symmetric Functions of Roots]] develops the polynomial/error-correction connection. Many practical Reed–Solomon systems use fields with $2^8$ elements; these are **not** ordinary arithmetic modulo $256$. Prime fields are the simplest doorway, not a description of every implementation. [RFC 5510, finite-field arithmetic](https://www.rfc-editor.org/rfc/rfc5510)

**RSA uses a different feature.** Its modulus is deliberately a product of two large primes. Knowing the factors lets the key generator calculate the structure needed for a private key; publishing their product does not publish those factors. [[Encryption]] works an RSA example. Multiplication, primality testing and factorisation are three different tasks: there are fast practical tests for primality even when finding the factors of a large composite is difficult. This is not a proof that factoring must be hard, nor that every encryption system uses prime-factorisation security. [NIST FIPS 186-5, RSA key generation](https://doi.org/10.6028/NIST.FIPS.186-5)

## 7. Hands-on — let the proof tell the program when to stop

```python
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True

def sieve(limit):
    if limit < 2:
        return []
    survives = [True] * (limit + 1)
    survives[0] = survives[1] = False
    for p in range(2, isqrt(limit) + 1):
        if survives[p]:
            for multiple in range(p * p, limit + 1, p):
                survives[multiple] = False
    return [n for n in range(2, limit + 1) if survives[n]]

assert is_prime(97) and not is_prime(49)
assert sieve(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

`isqrt(n)` computes the integer square root exactly; the extra `+1` includes the boundary divisor. The sieve's starting point `p*p` comes straight from the argument above. Try bounds $0,1,2,49,100$ before trying a million.

Run `python3 prime-numbers-lab.py` for the companion checks: compare independent primality methods, factor the $30031$ counterexample, inspect modular inverses and reproduce the perfect-square calculation. This classroom code is intended for learning, not cryptographic key generation. Trial division performs about $\sqrt n$ divisibility tests; expressed in the number of input bits, that is exponential growth. See [[Big-O Notation]] and [[P vs NP]].

## Common misconceptions

- **“Prime means odd.”** $2$ is prime and $9$ is not. Use the divisor definition.
- **“The product plus one must be prime.”** $30031=59\cdot509$. A prime divisor outside the list is sufficient.
- **“Different factor trees mean different prime factorisations.”** Intermediate splits differ; the final multiset of prime factors does not.
- **“If $a\mid bc$, then $a$ divides $b$ or $c$.”** This is guaranteed when $a$ is prime. The counterexample $6\mid2\cdot3$ shows why the hypothesis matters.
- **“A sieve that found a million primes proves infinity.”** It proves only a finite statement. Euclid defeats an arbitrary proposed finite list.
- **“Testing for primality means finding all the factors.”** A yes/no question and a search for factors can have very different computational costs.

## Exam Notes

### Cambridge 0580 — Core and Extended

**C1.1/E1.1:** prime vocabulary, factors/multiples, prime factorisation and HCF/LCM are shared arithmetic content. The definition, small-number tests and exponent bookkeeping support it. The general uniqueness proof, Bézout's identity, finite fields and cryptographic theory are enrichment, not prescribed IGCSE proofs.

### OxfordAQA 9260

**N4 Core** names prime numbers, factors/divisors, multiples, HCF/LCM and prime factorisation with product/index notation. It does not require a proof of the Fundamental Theorem of Arithmetic or Euclid's infinitude proof. Distinguish knowing the classification from proving the global theorem.

### Edexcel International A-Level

**P4 §1.1 explicitly names infinity of primes as an example of proof by contradiction.** Show the finite-list assumption, product-plus-one construction, prime-divisor argument and contradiction; do not claim that the constructed number must itself be prime. P2 §1 covers proof structure and counterexamples; Q5(ii) above is a verified example of that shorter task. Unique factorisation and the Bézout proof here provide enrichment.

### IB Mathematics

**AA HL AHL1.15 explicitly includes Euclid's infinitude proof** among contradiction examples. It also includes counterexamples, with an explanation of why the example refutes the claim. Prime/factor/multiple vocabulary is prior learning in AA and AI; do not transfer AA HL's named proof requirement to AA SL or AI. These references are to the first-assessment-2021 guides, not the forthcoming 2029 courses. [Official AA guide](https://www.ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-analysis-and-approaches-guide-en.pdf)

### Other boards and formula sheets

**Cambridge 0606/9709/9231, OxfordAQA 9660 and AP Calculus AB/BC:** the inspected specifications do not name the infinity-of-primes or unique-factorisation theorem as a required result. Divisibility can be used as a setting for proof—for example, 9231 induction—but that does not make all number theory prescribed content. The proofs here must be understood and constructed; no special prime-number formula is supplied by a reference sheet. [[MF19 Reference (9709)]] and [[Edexcel IAL Reference]] cover the respective formula-book boundaries.

## Beyond syllabus — order without a simple pattern

> [!info] Sparse, but never exhausted
> Recall that Euclid proves there are infinitely many primes without telling us how often they occur. The **prime number theorem** says $\pi(x)\sim x/\ln x$: the ratio of the true count to this estimate tends to $1$. It is an asymptotic density statement, not an exact formula or a certificate for a particular number. Near a large $x$, the heuristic prime frequency is about $1/\ln x$. That helps explain why large-prime searches can work despite the sparsity. [PrimePages: the prime number theorem](https://primes.utm.edu/glossary/page.php?sort=PrimeNumberThm)
>
> **Long gaps are easy to force.** For any integer $m\ge2$, the numbers $(m+1)!+2,\ldots,(m+1)!+(m+1)$ are $m$ consecutive composites: the term with added $j$ is divisible by $j$. Infinitely many primes can coexist with arbitrarily long prime-free stretches.
>
> **Unique factorisation depends on the number system.** In the integers, primes and irreducible multiplication pieces coincide. In other rings, that need not hold. In $\mathbb Z[\sqrt{-5}]$, $6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5})$ leads to genuinely different irreducible factorizations. Why are these factors irreducible? The norm $N(a+b\sqrt{-5})=a^2+5b^2$ is multiplicative, and no element has norm $2$ or $3$. The four factors have norms $4,9,6,6$; a proper factorisation of any would require a factor of norm $2$ or $3$. The only units are $\pm1$, so these two lists cannot be turned into each other by reordering and sign changes. The integer proof's hinge—Euclid's lemma—cannot simply be assumed in a new system. [[Group Theory]] opens the door to such structural questions.

## Connections

- **The person pursuing the primes:** [[Sophie Germain and the Borrowed Name]] — how special prime remainders became a route toward Fermat’s Last Theorem, and why her plan needed infinity.

- **Prerequisites:** [[Prime Factorisation (Vocab)]] supplies the procedures; [[Proof by Induction]] supplies the existence proof and induction logic.
- **Foundations:** [[Natural Numbers]] explains well-ordering; [[Logic]] separates implication, contradiction and counterexample.
- **Arithmetic tools:** [[Factors and Multiples (Vocab)]], [[Powers and Roots (Vocab)]], [[Surds]]—prime exponents explain their tests and simplifications.
- **Arithmetic modulo a prime at work:** [[Privacy-Preserving Computation]] — secret shares, Shamir's polynomials and zero-knowledge proofs all live in the integers modulo a prime, where every non-zero number has an inverse.
- **Computing:** [[Encryption]], [[P vs NP]], [[Big-O Notation]]—primality, factorisation and efficient algorithms are distinct questions.
- **Polynomial bridge:** [[Symmetric Functions of Roots]]—finite-field structure supports exact reconstruction and error correction.
- **Human story:** [[Erdős the Wandering Mathematician]]—the fascination of primes and the search for unexpected elementary proofs.

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $p\mid n$ | `p\mid n` | $p$ divides $n$ |
| $p\nmid n$ | `p\nmid n` | $p$ does not divide $n$ |
| $\gcd(a,b)$ | `\gcd(a,b)` | Greatest common divisor |
| $a\equiv b\pmod p$ | `a\equiv b\pmod p` | Congruence modulo $p$ |
| $\pi(x)\sim x/\ln x$ | `\pi(x)\sim x/\ln x` | Prime-counting asymptotic |
