---
chinese: 整数 (zhěngshù)
prerequisites:
  - "[[Natural Numbers]]"
  - "[[Number Sets (Vocab)]]"
  - "[[Four Operations (Vocab)]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/number
  - domain/algebra
  - level/IGCSE
  - level/university
  - curriculum/Cambridge-0580
  - curriculum/OxAQA-9260
  - curriculum/IB-AA
  - curriculum/IB-AI
  - syllabus/0580-E1-1
  - type/definition
  - type/proof
  - notation/integers
  - misconception/negative-times-negative
  - misconception/subtraction-is-always-decrease
---

# Integers 整数

## Definition — a number system in which subtraction can always answer

You have £2 and owe £5. Counting the coins answers one question. **Your net position is −£3**, which answers another: after accounting for the debt, how far are you above or below zero?

The **integers** extend the natural numbers with additive opposites:

$$\boxed{\mathbb Z=\{\ldots,-3,-2,-1,0,1,2,3,\ldots\}.}$$

For every integer $a$, its **additive inverse** $-a$ satisfies $a+(-a)=0$. Subtraction becomes addition of that inverse:

$$\boxed{a-b=a+(-b).}$$

This makes $x+b=a$ solvable for every pair of integers $a,b$. In $\mathbb N=\{0,1,2,\ldots\}$, it fails whenever $a<b$. We keep the familiar addition and multiplication laws while giving those previously unanswered subtractions a home.

The listing above tells us which numbers we mean. Later we will **construct** them from natural numbers, without assuming negative numbers already exist.

### 中文锚点

你有两元，却欠朋友五元，账面上就是负三元。朋友忽然说：“那五元不用还了。”你手里的硬币一枚没多，却一下轻松了五元，账面也从负三元变成了正二元。负数记下的不是“有几枚负的硬币”，而是相对于零还差多少；减掉一笔欠款，当然会让处境变好。把“拥有”和“欠着”放到同一本账里，原本数硬币回答不了的问题，就能用同一套加减法说清楚了。

### Familiar value, new representation

| Familiar description | Pair of natural numbers | Same net value |
|---|---|---|
| Own 2, owe 5 | $(2,5)$ | $-3$ |
| Own 4, owe 7 | $(4,7)$ | $-3$ |
| Own nothing, owe 3 | $(0,3)$ | $-3$ |
| Own 3, owe 3 | $(3,3)$ | $0$ |

These are equivalent **for the net balance**, not for every financial purpose: owning cash and owing a debt can differ from owning nothing because of interest, due dates and liquidity. The mathematical model deliberately keeps only the difference.

## Notation

| Symbol / word | Read as | Meaning |
|---|---|---|
| $\mathbb Z$ | the integers | whole-number values, including zero and negatives |
| $-a$ | the opposite of $a$ | the unique number which adds to $a$ to give zero |
| $a-b$ | $a$ minus $b$ | a two-input operation; distinct from the one-input negation $-a$ |
| $\lvert a\rvert$ | absolute value of $a$ | distance from zero, always non-negative |
| $[(a,b)]$, abbreviated $[a,b]$ | the class of $(a,b)$ | all equivalent records representing the same integer |
| $\sim$ | is equivalent to | the relation used to identify those records |

**A minus sign is not a promise that the result is negative.** If $a=-4$, then $-a=4$. Opposite is an operation, not a mood.

## 1. On the number line: position, movement and distance

Adding $b$ translates a position by $b$: right for positive $b$, left for negative $b$. Subtracting $b$ undoes that translation, so it moves by $-b$.

Thus $-3-(-5)=2$: start at $-3$ and undo a movement five units left. You move five units right.

![[integers-number-line.svg|700]]

*Blue marks the starting value. The green arrow is the change, not the distance of the start from zero. Reflection in zero sends every $a$ to $-a$.*

The order is spatial: $-5<-2$ because $-5$ lies further left. But $\lvert-5\rvert>\lvert-2\rvert$ because $-5$ is farther **from zero**. Position and distance answer different questions.

Formally,

$$|a|=\begin{cases}a,&a\ge0,\\-a,&a<0.\end{cases}$$

The distance between integer positions $a$ and $b$ is $|a-b|$. Translating both positions by the same amount preserves their order and separation. Negating both reflects the line and reverses order: $a<b$ implies $-a>-b$.

## 2. Why removing a negative adds a positive

An additive inverse is unique. If $a+x=0$ and $a+y=0$, add $-a$ to each equation and use associativity to get $x=y$.

Since $(-a)+a=0$, the inverse of $-a$ is $a$:

$$-(-a)=a.$$

Now use the definition of subtraction:

$$a-(-b)=a+\bigl(-(-b)\bigr)=a+b.$$

The debt example makes that result imaginable. **Uniqueness of the additive inverse makes it necessary.**

![[integers-cancellation.mp4]]

*Watch a debt disappear, then watch matching positive/negative counters accumulate without changing their net value. The final sequence derives the multiplication signs from distributivity.*

## 3. Why negative times negative must be positive

Here is the promise we are keeping: multiplication must still **distribute over addition**. These proofs show what that promise forces; the construction in §4 will show that such a system actually exists.

### First, multiplication by zero

Distributivity gives $a(0+0)=a0+a0$. But $0+0=0$, so $a0=a0+a0$. Add the inverse of $a0$ to both sides:

$$a0=0.$$

### Next, one negative factor

Because $b+(-b)=0$,

$$ab+a(-b)=a\bigl(b+(-b)\bigr)=a0=0.$$

So $a(-b)$ is the additive inverse of $ab$:

$$\boxed{a(-b)=-(ab).}$$

Commutativity also gives $(-a)b=-(ab)$.

### Finally, two negative factors

Apply the one-negative identity with $-a$ in place of $a$:

$$(-a)(-b)=-\bigl((-a)b\bigr)=-\bigl(-(ab)\bigr)=ab.$$

Therefore

$$\boxed{(-a)(-b)=ab,\qquad\text{in particular }(-1)(-1)=1.}$$

The identity holds for **all integers** $a,b$. The everyday phrase “negative times negative is positive” takes $a,b>0$.

> [!tip] Two reversals help you picture the answer
> Multiplication by $-1$ reflects the number line in zero. Doing it twice returns every point to its start, so $(-1)(-1)$ acts like multiplication by $1$. The reflection is an interpretation of the proved law, not a replacement for the distributive-law argument.

“Repeated addition” directly explains $3\times(-2)$: three copies of $-2$. It does not literally explain a **negative number of copies**. The extension to a negative multiplier comes from preserving the algebraic laws.

## 4. Build integers without sneaking negatives into the definition

Recall that natural-number addition and multiplication already exist. We assume their usual laws, cancellation and order; [[Natural Numbers]] explains how arithmetic begins with successor and recursion. We will use only natural-number operations to build the new objects.

### Same difference, without subtraction

A pair $(a,b)\in\mathbb N\times\mathbb N$ is a record that we intend to mean “$a$ minus $b$.” Two records should mean the same thing precisely when

$$\boxed{(a,b)\sim(c,d)\quad\Longleftrightarrow\quad a+d=b+c.}$$

For example, $(2,5)\sim(4,7)$ because $2+7=5+4$. **The test uses no negative numbers and no potentially impossible subtraction.**

It is an equivalence relation:

1. **Reflexive:** $a+b=b+a$, so every record is equivalent to itself.
2. **Symmetric:** if $a+d=b+c$, then $c+b=d+a$; the comparison works both ways.
3. **Transitive:** suppose $a+d=b+c$ and $c+f=d+e$. Adding gives $a+d+c+f=b+c+d+e$. Cancel $c+d$ using natural-number cancellation: $a+f=b+e$. Thus $(a,b)\sim(e,f)$.

An **equivalence class** is the whole collection of records that pass this test with one another. Define $\mathbb Z$ to be the set of these classes. Write $[a,b]$ for the class containing $(a,b)$.

![[integers-equivalent-pairs.svg|650]]

*Add the same count to both columns: the record changes, the represented integer does not. A single pair is a representative; the integer is its equivalence class.*

### Define the operations on records

$$\begin{aligned}
[a,b]+[c,d]&=[a+c,b+d],\\
-[a,b]&=[b,a],\\
[a,b]-[c,d]&=[a+d,b+c],\\
[a,b][c,d]&=[ac+bd,ad+bc].
\end{aligned}$$

Addition pools the two positive counts and the two negative counts. Negation exchanges their roles. The multiplication formula is suggested by formally expanding $(a-b)(c-d)$, **but the definition itself uses only sums and products in $\mathbb N$**. Its validity does not rely on already having negative multiplication.

### Why choosing another record cannot change the answer

This is the crucial **well-definedness** check. A calculation on an integer must not depend on which representative we happened to write.

Every pair $(a,b)$ is equivalent to $(a+t,b+t)$. Adding such a padding to the first input pads both entries of its sum by $t$; negating merely exchanges them. Multiplying the padded input by $(c,d)$ changes the output from

$$(ac+bd,ad+bc)$$

to

$$(ac+bd+t(c+d),\ ad+bc+t(c+d)).$$

Both entries increase by the same amount, so the output stays equivalent. The multiplication formula is symmetric in its two inputs, so padding the second input is harmless too.

**Does padding cover every equivalent pair?** Yes. If $(a,b)\sim(a',b')$, pad the first pair by $b'$ and the second by $b$. Their second entries both become $b+b'$, and their first entries are equal because $a+b'=a'+b$. They reach a common record. Thus independence under padding proves independence under every change of representative.

### Recover the familiar integers and laws

Embed a natural number $n$ as $[n,0]$. This is injective: $[n,0]=[m,0]$ forces $n=m$. Addition and multiplication agree with their old values because

$$[n,0]+[m,0]=[n+m,0],\qquad[n,0][m,0]=[nm,0].$$

Zero is $[0,0]$, one is $[1,0]$, and $-[n,0]=[0,n]$. Also

$$[a,b]+[b,a]=[a+b,a+b]=[0,0].$$

If $a\ge b$, there is a unique natural $k$ with $a=b+k$, and $[a,b]=[k,0]$. If $a<b$, write $b=a+k$ with $k>0$, and $[a,b]=[0,k]$. These are exactly the familiar zero, positive integers and negative integers.

The order can also be defined without subtraction: $[a,b]\le[c,d]$ exactly when $a+d\le b+c$. Padding both entries preserves this comparison.

The ring laws are inherited by expanding natural-number sums/products. For example, both bracketings of $[a,b][c,d][e,f]$ give

$$[ace+bde+adf+bcf,\ acf+bdf+ade+bce].$$

That checks multiplication's associativity. Distributivity follows by expanding $[a,b]([c,d]+[e,f])$: both sides give $[ac+ae+bd+bf,ad+af+bc+be]$. Addition's laws follow component by component. **The promised consistent arithmetic has now been built.** [Construction references](https://www.southampton.ac.uk/~wright/1001/extending-mathbb-n-to-mathbb-z.html) · [University of Hawai‘i notes](https://math.hawaii.edu/~pavel/aluffi_321/NZ.pdf).

## 5. What integers fix—and what they do not

Integers are **closed under addition, subtraction and multiplication**: those operations stay in $\mathbb Z$. Division need not. $3/2$ is not an integer; solving $2x=3$ asks for another extension, the rational numbers.

For $b\ne0$, an integer quotient $a/b$ exists exactly when $b$ divides $a$. Division by zero does not become valid: $0x=a$ has no solution for $a\ne0$, and every $x$ is a solution for $a=0$, so it never defines a unique quotient.

Unlike $\mathbb N$, the usual integer order has no least element: $a-1<a$ for every integer $a$. A decreasing **integer** counter need not terminate. The natural-valued stopping measure in [[Natural Numbers]] needs a lower bound; “it decreases” alone is insufficient.

> [!info] Beyond syllabus — the first ring
> Recall that integers have addition, additive inverses and distributive multiplication. This structure is a **commutative ring with identity**. It is not a field, because most nonzero integers have no multiplicative inverse inside $\mathbb Z$.

[[Group Theory]] develops the idea of an operation with inverses; [[Prime Numbers]] develops divisibility. Neither word requires us to change how $2+3$ works.

## 6. Where integers are the working tool

### Money stored in minor units

A program can store a whole number of cents or pence in an integer: £12.34 becomes $1234$, and a £5 charge is a change of $-500$. Adding a list of such changes computes a balance exactly in those units. Undoing an erroneous debit means adding its opposite. This handles exact addition; percentages, currency conversion and fractions of a penny still need an explicit rounding policy.

### Pixel movement and game worlds

An integer grid location can change by $(\Delta x,\Delta y)=(3,-2)$. The signs encode direction; addition composes movements, and negation undoes one. Screen coordinates often increase **downwards** along the vertical axis, so “negative means down” is not universal. Declare the coordinate convention.

### Mathematical integers versus machine integers

$\mathbb Z$ has no largest or smallest member. An $n$-bit two's-complement word has only $2^n$ patterns and the signed range $-2^{n-1}$ to $2^{n-1}-1$. In an 8-bit wrapping model, $127+1$ decodes as $-128$. This is a representation limit, not a new law of integer addition. Real languages differ in overflow behaviour; see [[Two's Complement]] and [[Overflow and Underflow]].

Python's `int` expands as needed, subject to available memory, rather than overflowing at a fixed word size. Its `/` and `//` also answer different questions: `-7 / 3` is a floating-point quotient; `-7 // 3` is `-3`, rounded down. Python gives `-7 % 3 == 2`, keeping `-7 == (-3)*3 + 2`. These are programming conventions to inspect, not consequences of the word “integer.” [Python numeric types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex).

## Worked examples — choose the operation before chasing signs

These are original worked examples, not attributed past-paper questions.

### 1. Reverse an erroneous charge

An account's net balance is $-1200$ cents. A $350$-cent debit was entered twice; remove one copy.

**Trigger:** undo one recorded change. **Tool:** add its additive inverse. The erroneous change was $-350$, so

$$-1200-(-350)=-850\text{ cents}.$$

**Check:** the balance improves by 350 cents but remains negative. Removing debt does not necessarily make the whole balance positive.

### 2. Multiply two classes using different representatives

Find $[1,4][2,5]$.

**Trigger:** the inputs are classes. **Tool:** the pair multiplication rule.

$$[1,4][2,5]=[1\cdot2+4\cdot5,\ 1\cdot5+4\cdot2]=[22,13]=[9,0].$$

**Trigger:** representative choice should not matter. **Tool:** cancel matching counts first. Both inputs equal $[0,3]$, so $[0,3][0,3]=[9,0]$ again. Two negative threes give positive nine in the constructed system itself.

### 3. Position is not distance

A lift goes from level $-3$ to level $4$, with equally spaced levels and ground labelled 0.

**Trigger:** change from a start to an end. **Tool:** displacement $=$ end $-$ start.

$$4-(-3)=7\text{ levels upward}.$$

Returning gives $-3-4=-7$ levels of displacement, but distance travelled is $|-7|=7$ levels. The signed change reverses; the distance does not.

## Hands-on — calculate with natural pairs

Save no special dependencies: these functions run in Python. Each input is a pair of non-negative integers; the comparison never decodes it to a negative number.

```python
def equal(x, y):
    a, b = x
    c, d = y
    return a + d == b + c

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def opposite(x):
    return (x[1], x[0])

def multiply(x, y):
    a, b = x
    c, d = y
    return (a*c + b*d, a*d + b*c)

assert equal((2, 5), (4, 7))
assert equal(add((2, 5), opposite((2, 5))), (0, 0))
assert equal(multiply((0, 3), (0, 3)), (9, 0))
```

The adjacent `integers-lab.py` checks representative changes, ring identities, ordering and the finite-word contrast. Predict first: adding 100 to **both** components of an input changes its raw product pair dramatically. Does it change the represented answer? A finite check can catch a coding mistake; the proof in §4 is what covers every pair.

## Common misconceptions

- **“Minus always means take away.”** In $-a$ it means take the opposite; in $a-b$ it specifies subtraction. Parse the expression before using a sign mnemonic.
- **“Negative means smaller in magnitude.”** $-100<-2$, but $|-100|>|-2|$. Compare positions or distances according to the question.
- **“Two minuses always make a plus.”** $-3+(-2)=-5$. The multiplication identity does not replace the addition rule.
- **“The sign can be ignored when squaring.”** $(-3)^2=9$, while $-3^2=-(3^2)=-9$: the brackets decide what is squared.
- **“$(2,5)$ and $(4,7)$ are the same pair.”** They are different records in the same class. Equality of represented values does not mean equality of representations.
- **“The net-balance model captures every detail of a debt.”** It deliberately forgets terms and timing; retain them separately when they matter.

## Exam Notes

### Cambridge 0580 — Core and Extended

The 2025–27 syllabus requires integer vocabulary in **C1.1/E1.1**, ordering in **C1.5/E1.5**, and the four operations, including negative numbers and operation order, in **C1.6/E1.6**. The number-line, opposite and signed-arithmetic explanations support these outcomes. Papers 1/2 are non-calculator; Papers 3/4 allow calculators. The pair construction, equivalence classes and ring proofs are enrichment, not prescribed tasks.

### OxfordAQA 9260 — N1, N2 and N3

**N1** orders signed integers, decimals and fractions and includes a number line. **N2** requires four operations on positive and negative numbers, including contextual questions; **N3** includes inverse operations and operation order. Both tiers need these foundations. N4's even/odd/prime vocabulary is a different outcome; it is not the reason for the deeper construction here.

### Cambridge 0606 and A-Level mathematics

0606, 9709 and 9231 explicitly assume earlier mathematics. Pearson Edexcel IAL and OxfordAQA 9660 also use signed arithmetic throughout algebra and later topics; this describes mathematical dependence, not an entry requirement (9660 states that it has no previous-learning requirement). Their inspected specifications do not prescribe constructing $\mathbb Z$ from equivalence classes or deriving its ring laws. Proof by induction, divisibility or negative indices appearing elsewhere in these courses does not turn this construction into a required assessment topic.

### IB AA and AI — prior learning, SL and HL

The guides for first assessment 2021 explicitly include number systems, basic absolute value and operations on integers among **prior learning** assumed by examination questions. This is not a new HL-only topic. The formal construction is enrichment. [AA guide](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-analysis-and-approaches-guide-en.pdf) · [AI guide](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-applications-and-interpretation-guide-en.pdf).

### AP and scope boundary

AP Calculus AB/BC assumes fluent algebraic arithmetic; integer construction is not a named CED outcome. The mathematical integers and the bounded `int` type used in AP CSA should not be conflated; the language-specific treatment belongs with [[Java Values and Expressions]]. No equivalence-class construction or ring-law proof is prescribed on the school-board specifications named above. The elementary arithmetic remains examinable wherever a calculation uses it.

## Connections

- **Parents:** [[Natural Numbers]] — successor, recursion and the arithmetic being extended; [[Number Sets (Vocab)]] — where $\mathbb Z$ sits; [[Four Operations (Vocab)]] — operation language.
- **Structure:** [[Group Theory]] — addition with inverses.
- **Applications:** [[Two's Complement]], [[Overflow and Underflow]] and [[Java Values and Expressions]] — finite representations and language rules; [[Cartesian Coordinates (Vocab)]] — signed positions.
- **Next questions:** [[Prime Numbers]] — divisibility inside $\mathbb Z$; [[Fractions (Vocab)]] — making nonzero division possible.

## LaTeX Reference

| Symbol | LaTeX | Use |
|---|---|---|
| $\mathbb Z$ | `\mathbb Z` | integers |
| $\mathbb N\times\mathbb N$ | `\mathbb N\times\mathbb N` | ordered natural-number pairs |
| $(a,b)\sim(c,d)$ | `(a,b)\sim(c,d)` | equivalent representatives |
| $[(a,b)]$ | `[(a,b)]` | equivalence class |
| $\lvert a-b\rvert$ | `\lvert a-b\rvert` | distance; safe absolute-value delimiters in a table |
