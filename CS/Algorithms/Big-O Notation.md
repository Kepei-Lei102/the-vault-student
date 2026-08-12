---
chinese: 大O记号 (dà-O jìhào)
prerequisites:
  - "[[Searching]]"
  - "[[Sorting]]"
  - "[[Logarithms]]"
  - "[[Recursion]]"
  - "[[Sequences]]"
leads_to:
  - "[[P vs NP]]"
  - "[[Parallel and External Sorting]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/algorithms
  - domain/complexity
  - level/A-Level
  - level/AP
  - curriculum/Cambridge-9618
  - curriculum/AP-CSA
  - curriculum/IB-CS
  - syllabus/IB-CS-B2-4
  - syllabus/9618-19-1
  - syllabus/AP-CSA-2-12
  - type/deep
  - type/definition
  - notation/big-o
  - misconception/big-o-means-worst-case
  - misconception/big-o-ignores-constants-in-practice
  - misconception/big-o-is-actual-speed
  - misconception/lower-big-o-always-faster
---

# Big-O Notation 大O记号

## Definition

**Big-O notation** describes how an algorithm's cost grows as its input gets larger. It throws away the details that depend on your computer — the exact operation count, the constant factors, the lower-order terms — and keeps only the one thing that's intrinsic to the *algorithm*: the **shape** of its growth.

You have already *felt* this twice. In [[Searching]] you watched binary search beat linear search by a margin that exploded with list size — that's $O(\log n)$ versus $O(n)$. In [[Sorting]] you watched merge sort finish while bubble sort ground on — that's $O(n \log n)$ versus $O(n^2)$. This card is the name for that feeling. Big-O is the language computer scientists use to say *"how does the work grow when the problem grows?"* — and it is, by a wide margin, the most load-bearing idea in all of algorithms.

The single most important sentence: **a better Big-O beats a faster computer.** At small sizes the constants win; at large sizes the *order* wins, and it wins so decisively that no amount of hardware can rescue a bad algorithm.

### 中文锚点

**大O记号**（dà-O jìhào, Big-O notation）/ **时间复杂度**（shíjiān fùzádù, time complexity）：描述算法的工作量**如何随着输入规模 $n$ 增长**。它故意**扔掉常数和低次项**，只保留增长的「**量级**」——因为常数取决于你的电脑，量级取决于算法本身。

- $O(1)$ 常数：和 $n$ 无关（数组取下标、哈希查找）
- $O(\log n)$ 对数：每步砍一半（[[Searching|二分查找]]）
- $O(n)$ 线性：看一遍（线性查找）
- $O(n\log n)$ 线性对数：最优的比较排序（[[Sorting|归并/快速排序]]）
- $O(n^2)$ 平方：每个元素配每个元素（冒泡/选择/插入排序）
- $O(2^n)$ 指数 / $O(n!)$ 阶乘：暴力枚举，规模一大就**彻底没救**

一句话：**好的复杂度胜过快的电脑。** $n$ 小的时候常数说了算；$n$ 大的时候量级说了算，而且大到任何硬件都救不回来。

## Why we throw away the details

Suppose one algorithm does exactly $f(n) = 3n^2 + 5n + 200$ operations. As $n$ grows, which term matters?

| $n$ | $3n^2$ | $5n$ | $200$ | which dominates |
|---|---|---|---|---|
| 10 | 300 | 50 | 200 | all comparable |
| 100 | 30,000 | 500 | 200 | $3n^2$ already 98% |
| 10,000 | $3\times10^8$ | 50,000 | 200 | $3n^2$ is everything |

For large $n$ the $3n^2$ term swamps the rest, so we write $f(n) = O(n^2)$ and drop the $5n$ and the $200$. We also drop the **constant 3**, because:

- The constant depends on *implementation and hardware* — a faster CPU, a better compiler, or a tighter loop changes the 3, but it cannot change the $n^2$. The order is the part that belongs to the *algorithm*; the constant is the part that belongs to the *machine*.
- Doubling the input multiplies $3n^2$ by 4 regardless of the 3. The **growth behaviour** — "double the input, quadruple the work" — is what $O(n^2)$ captures, and it's true whatever the constant.

So Big-O answers a deliberately coarse question — *what happens as $n \to \infty$?* — and that coarseness is exactly what makes it portable across computers and decades.

> [!info] The formal definition (beyond syllabus, but it's not scary)
> We say $f(n) = O(g(n))$ if there exist positive constants $c$ and $n_0$ such that
> $$f(n) \le c\,g(n) \quad\text{for all } n \ge n_0.$$
> In words: *past some point $n_0$, $f$ is bounded above by a constant multiple of $g$.* That's the whole idea — "eventually grows no faster than $g$, up to a constant." For $f(n)=3n^2+5n+200$, pick $g(n)=n^2$, $c=4$, $n_0=205$ and the inequality holds forever after. The definition is just the rigorous version of "the dominant term, without its constant."

## The hierarchy — the classes you actually meet

Ordered from best to worst, each tied to an algorithm you already know:

| Big-O | Name | "Double the input →" | Example in this vault |
|---|---|---|---|
| $O(1)$ | constant | no change | array index `A[i]`; a hash-table lookup |
| $O(\log n)$ | logarithmic | $+1$ step | [[Searching\|binary search]]; height of a balanced tree |
| $O(n)$ | linear | doubles | [[Searching\|linear search]]; one pass over a list |
| $O(n \log n)$ | linearithmic | a bit more than doubles | [[Sorting\|merge sort]], quicksort (avg); the comparison-sort floor |
| $O(n^2)$ | quadratic | quadruples | [[Sorting\|bubble / selection / insertion sort]]; all-pairs comparison |
| $O(n^3)$ | cubic | $\times 8$ | naive matrix multiplication; triple-nested loops |
| $O(2^n)$ | exponential | *squares* | naive recursive Fibonacci; trying every subset |
| $O(n!)$ | factorial | hopeless | brute-force travelling salesman; trying every ordering |

The jump that matters most is the one between the **polynomial** classes ($O(n^k)$ for some fixed $k$ — "tractable") and the **exponential** classes ($O(2^n)$, $O(n!)$ — "intractable"). That line is the subject of the deepest open problem in computer science (see Beyond Syllabus).

## Feel the growth — concrete numbers

Operations needed at each size (rounded). This is the whole argument for caring:

| $n$ | $\log_2 n$ | $n$ | $n\log_2 n$ | $n^2$ | $2^n$ |
|---|---|---|---|---|---|
| 10 | 3 | 10 | 33 | 100 | 1,024 |
| 100 | 7 | 100 | 664 | 10,000 | (a 31-digit number) |
| 1,000 | 10 | 1,000 | ~9,970 | 1,000,000 | (hopeless) |
| 1,000,000 | 20 | 1,000,000 | ~$2\times10^7$ | $10^{12}$ | (hopeless) |

Read the bottom row. On a million items, an $O(n\log n)$ sort does about **20 million** operations — a couple of hundredths of a second. An $O(n^2)$ sort does **a trillion** — about **17 minutes** on the same machine. And an $O(2^n)$ algorithm on a mere $n=100$ would need roughly $1.3\times10^{30}$ operations: at a billion operations per second, that's about **$4\times10^{13}$ years — nearly three thousand times the age of the universe.** No supercomputer, no quantum leap, no Moore's-Law decade saves you from an exponential algorithm. You need a *better algorithm*.

![[big-o-growth-curves.svg]]
*The shape of each class. $O(1)$ and $O(\log n)$ stay almost flat; $O(n)$ and $O(n\log n)$ rise gently; $O(n^2)$ curves up hard; $O(2^n)$ goes nearly vertical almost immediately. The crossings are the point: a "slower-looking" curve with a lower order always wins once $n$ is big enough.*

## How to read the Big-O off your code

You usually don't need the formal definition — you read the **dominant loop structure**:

```python
def f1(A):                 # O(n) — one pass
    for x in A:
        print(x)

def f2(A):                 # O(n^2) — a loop inside a loop, each n long
    for x in A:
        for y in A:
            print(x, y)

def f3(A):                 # O(log n) — the counter HALVES the distance each step
    i = len(A)
    while i > 1:
        i = i // 2

def f4(A):                 # O(n) — two SEPARATE passes: O(n) + O(n) = O(n)
    for x in A: print(x)
    for x in A: print(x)
```

The rules behind those readings:

- **Sequential** blocks **add**, and the sum keeps only its biggest term: $O(n) + O(n) = O(n)$; $O(n^2) + O(n) = O(n^2)$.
- **Nested** loops **multiply**: a loop of length $n$ inside a loop of length $n$ is $O(n^2)$; a binary search ($O(\log n)$) inside a pass over the list ($O(n)$) is $O(n\log n)$.
- A counter that **halves** (or doubles) toward the limit is $O(\log n)$ — the same halving as [[Searching|binary search]], the same reason its cost is a logarithm ([[Logarithms]]).
- **Drop constants and lower-order terms at the end:** $O(2n^2 + 3n + 7) = O(n^2)$.

## Why $n\log n$? — the cost students find hardest

Of all the classes, $n\log n$ is the one that feels like it came from nowhere. $O(n)$ is "look at each thing once"; $O(n^2)$ is "every thing against every other thing." But $n\log n$? It isn't a natural picture — until you see where it comes from. Use [[Sorting|merge sort]].

Merge sort does two things: it **splits** the list in half over and over, then **merges** the sorted pieces back up. Lay the recursion out as levels (this is exactly the tree drawn in [[Sorting]]):

| Level | pieces | size of each | total merge work at this level |
|---|---|---|---|
| 0 (top) | 1 | $n$ | $\sim n$ |
| 1 | 2 | $n/2$ | $2\cdot \tfrac{n}{2} = n$ |
| 2 | 4 | $n/4$ | $4\cdot \tfrac{n}{4} = n$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
| $k$ | $2^k$ | $n/2^k$ | $n$ |
| bottom | $n$ | $1$ | $n$ |

Two observations carry the whole result:

1. **Every level costs $n$.** At any level the pieces tile the entire array, so merging *all* of them touches all $n$ elements exactly once — $O(n)$ per level, no matter how deep you are. (The pieces got smaller, but there are proportionally more of them; the total stays $n$.)
2. **There are $\log_2 n$ levels.** Each level halves the piece size, and the number of halvings from $n$ down to $1$ is exactly $\log_2 n$ ([[Logarithms]]) — the very same halving that gives binary search its $\log n$ in [[Searching]].

Multiply them:

$$\underbrace{n}_{\text{work per level}} \;\times\; \underbrace{\log_2 n}_{\text{number of levels}} \;=\; \boxed{O(n\log n)}.$$

![[big-o-nlogn-levels.svg|697]]
*Why merge sort is $n\log n$. Each row is one level of the recursion: the pieces get smaller but more numerous, so every row's boxes still tile the whole array — total $n$ work per level. Count the rows and you get $\log_2 n$ of them (the halving depth). $n$ per level times $\log_2 n$ levels is the whole answer.*

That is the entire secret. The $n$ is the merge sweep; the $\log n$ is the splitting depth; $n\log n$ is **one linear sweep at each level of a halving.** It sits between $n$ and $n^2$ because it's $n$ done $\log n$ times instead of $1$ time ($O(n)$) or $n$ times ($O(n^2)$).

**Quicksort is the same story, on average, for the same reason.** Each round of partitioning touches all $n$ elements ($O(n)$ per level), and a *good* pivot halves the range — so $\log n$ levels, giving $n\log n$. Its worst case is the punchline of this whole framing: a *bad* pivot peels off one element at a time, so there are $n$ levels instead of $\log n$, and the cost becomes $n \times n = O(n^2)$. **Same work per level; different number of levels.** That single sentence is why pivot choice is the whole game in [[Sorting|quicksort]]. (The [[#Beyond Syllabus|Master Theorem]] below is the formula that generalises this level-counting to any divide-and-conquer recurrence.)

## Space complexity — the other axis

Big-O measures **memory** the same way it measures time. [[Sorting|Merge sort]] needs an extra $O(n)$ scratch array; quicksort sorts **in place** in $O(\log n)$ extra space (just the recursion stack); the simple quadratic sorts use $O(1)$ extra space. When people say "an algorithm's complexity" they usually mean *time*, but the time–space trade-off is real: hash tables buy $O(1)$ lookup with $O(n)$ memory; that's the deal noted in [[Searching]].

## Best, worst, average — and the cousins of $O$

Big-O is an **upper bound on a growth function** — it does not, by itself, mean "worst case." You state *which case* you're bounding:

- Linear search is $O(1)$ in the **best** case (target first), $O(n)$ in the **worst** (target last/absent), $O(n)$ on **average**.
- Quicksort is $O(n\log n)$ on average but $O(n^2)$ in the worst case (bad pivots).

> [!info] Big-O vs Big-Θ vs Big-Ω (beyond syllabus)
> $O(g)$ is an **upper** bound ("grows no faster than $g$"). $\Omega(g)$ is a **lower** bound ("grows no slower than $g$"). $\Theta(g)$ is **both at once** — a *tight* bound. Strictly, merge sort is $\Theta(n\log n)$ (always), while quicksort is $O(n^2)$ and $\Omega(n\log n)$. In everyday use people write $O$ where they mean $\Theta$; now you know the difference, which is enough.

## Worked examples

**1 — Read the order.** A function loops over a list once ($O(n)$), then sorts it with merge sort ($O(n\log n)$), then does a binary search ($O(\log n)$). Total: $O(n) + O(n\log n) + O(\log n) = O(n\log n)$ — the sort dominates.

**2 — Sort-then-search beats repeated linear search.** Searching an unsorted list $k$ times is $O(kn)$. Sorting once then binary-searching $k$ times is $O(n\log n + k\log n)$. For large $k$ the second wins decisively — the exact "sort once, search forever" argument from [[Searching]] and [[Sorting]], now in one line of Big-O.

**3 — Why exponential is a wall, not a hill.** A password of length $L$ from an alphabet of 26 letters has $26^L$ possibilities — brute force is $O(26^L)$, exponential in $L$. Adding *one* character multiplies the work by 26. That's not "a bit harder," it's a different universe — which is exactly why password length matters more than complexity.

## Common Misconceptions (Teaching Notes)

### 1. "Big-O means the worst case"

Big-O is an upper bound on *whichever* growth function you point it at. You can give the Big-O of the best case, the worst case, or the average case — you just have to say which. Conflating "$O$" with "worst case" is the single most common error.

**Fix.** Always pair Big-O with a case: "$O(n^2)$ in the worst case," "$O(n\log n)$ on average."

### 2. "Constants and lower-order terms never matter"

In Big-O they're dropped — but in *practice*, for **small** $n$, they absolutely matter. Insertion sort ($O(n^2)$) beats merge sort ($O(n\log n)$) on tiny arrays because its constant is tiny; that's why real libraries switch to insertion sort below ~16 elements. There are even "**galactic algorithms**" with a beautiful Big-O whose constants are so monstrous they're never faster on any input that fits in the universe.

**Fix.** Big-O tells you who wins *as $n\to\infty$*. For small or fixed $n$, measure.

### 3. "A lower Big-O is always faster"

Only eventually. $O(n\log n)$ with a huge constant can lose to $O(n^2)$ with a tiny one until $n$ is large enough. Big-O ranks *scaling*, not absolute speed.

**Fix.** Ask "how big is $n$, really?" before declaring a winner.

### 4. "Big-O is the running time"

It's the *growth* of the running time, in operations — not seconds. The same $O(n^2)$ algorithm runs at different speeds on different machines; what's invariant is that doubling $n$ quadruples the work on *every* machine.

**Fix.** Big-O is a property of the *algorithm*; wall-clock time is a property of the algorithm *plus the machine*.

## Exam Notes

### Cambridge 9618 (A-Level CS)

**§19.1 (Algorithms)** asks you to compare algorithms that perform the same task by criteria such as time taken and memory used, **"including use of Big O notation to specify time and space complexity"** — so the space column above is examinable, not decoration. The rest of §19.1 is the searches and sorts and the abstract data types; the ones whose complexity you are expected to quote are **linear search, binary search, bubble sort and insertion sort**, and finding or inserting in a **linked list** and a **binary tree**. Be able to read a complexity off simple code (single loop, nested loops, halving loop) and to explain why constants and lower-order terms are dropped. **Quicksort and merge sort are not assessed on 9618** — they are here because the $n \log n$ family is where the idea gets interesting, and because [[Sorting]] builds them.

### AP Computer Science A

**§2.12 (Informal Run-Time Comparisons)** teaches the *idea* — counting operations, "this loop runs $n$ times, that one $n^2$ times" — but **deliberately avoids the $O(\,)$ notation.** So for AP this card is *enrichment*: the reasoning (which algorithm scales better) is examinable; the symbol $O(n^2)$ is not required. Learn it anyway — it's the universal language the moment you go past AP. Searching and sorting cost comparisons are at [[Searching]] / [[Sorting]].

*(Not on Cambridge 0478 IGCSE — there, algorithmic efficiency stays informal, as comparison/swap counting in [[Searching]] and [[Sorting]].)*

### IB Computer Science (B2.4)

Efficiency comparison is B2.4's **named third leg** beside its searches and sorts: rank algorithms by behaviour as input grows, in exactly this card's language (linear vs binary search, bubble vs merge). Formal Big-O manipulation beyond the comparison level is enrichment IB-side — the *reasoning* is examinable, the notation gymnastics are not.

## Connections

- **Prerequisite / pays off:** [[Searching]] — $O(n)$ vs $O(\log n)$, the first gap you felt. [[Sorting]] — $O(n^2)$ vs $O(n\log n)$, the second. This card names both. [[Logarithms]] — the $\log n$ that the halving in binary search and merge sort produces; Big-O is where logarithms earn their keep in CS.
- **Bay:** the third and closing card of `CS/Algorithms/`, by design *after* [[Searching]] and [[Sorting]] — you don't hand someone a measuring tape before they have something to measure.
- **Recursion:** [[Recursion]] — the shape of the recursion tree *is* the time cost ($O(n)$ for factorial, $O(\log n)$ for binary search, $O(\varphi^n)$ for naive Fibonacci); the Master Theorem (below) reads complexity straight off a recurrence.
- **Extends to:** [[P vs NP]] — the polynomial-vs-exponential frontier as the deepest open question in CS; the explosive classes $O(2^n)$, $O(n!)$ live on the far side of it.

---

## Beyond Syllabus

### The Master Theorem — complexity from a recurrence

Divide-and-conquer algorithms obey recurrences like $T(n) = a\,T(n/b) + O(n^d)$: split into $a$ subproblems of size $n/b$, plus $O(n^d)$ to divide and combine. Merge sort is $T(n) = 2T(n/2) + O(n)$ ($a=b=2$, $d=1$). The **Master Theorem** reads the answer off $a, b, d$: compare $d$ with $\log_b a$. For merge sort $\log_2 2 = 1 = d$, the "balanced" case, giving $T(n) = O(n^d \log n) = O(n\log n)$ — the $n\log n$ you measured, derived in one line.

### P vs NP — the million-dollar line

Problems solvable in polynomial time $O(n^k)$ form the class **P** ("tractable"). Problems where a proposed solution can be *checked* in polynomial time form **NP**. Thousands of important problems (the travelling salesman, circuit satisfiability, protein folding) are **NP-complete** — the hardest in NP, all equivalent — and for none of them do we know a polynomial algorithm; the best known are exponential. **Does P = NP?** — i.e., is checking really easier than finding? — is the central open problem of computer science and one of the seven Clay Millennium Prize Problems ($1 000 000 for a proof). Almost everyone believes P ≠ NP; nobody can prove it. The whole drama lives on the polynomial/exponential boundary this card draws. The full development — verify-vs-solve, NP-completeness, reductions, and why a proof is so hard — is its own card: [[P vs NP]].

### Amortised analysis

Sometimes a single operation is occasionally expensive but *cheap on average over a sequence*. Appending to a dynamic array is usually $O(1)$, but occasionally $O(n)$ when it must grow and copy — yet across $n$ appends the total is $O(n)$, so the **amortised** cost per append is $O(1)$. Averaging cost over a run, rather than taking the worst single step, is its own small art.

### The comparison-sort lower bound

Recall from [[Sorting]] that *any* sort using only comparisons must make at least about $n\log n$ of them in the worst case — a $\Omega(n\log n)$ lower bound proved by counting the $n!$ possible orderings. Merge sort is therefore **optimal** among comparison sorts: it meets the floor. Big-O describes how fast you go; this lower bound describes how fast you *could possibly* go.

## Python / Notation Reference

| Symbol | Meaning |
|--------|---------|
| $O(g(n))$ | grows *no faster than* $g(n)$, up to a constant, for large $n$ (upper bound) |
| $\Omega(g(n))$ | grows *no slower than* $g(n)$ (lower bound) |
| $\Theta(g(n))$ | grows *exactly like* $g(n)$ — both bounds at once (tight) |
| $n$ | the input size (list length, number of items) |
| $\log n$ | base-2 logarithm in CS unless stated — number of halvings ([[Logarithms]]) |
| $c,\ n_0$ | the constant multiplier and threshold in the formal definition |
| `//` | integer (floor) division — a halving counter `i = i // 2` signals $O(\log n)$ |
