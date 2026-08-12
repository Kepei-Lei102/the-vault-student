---
chinese: 查找 (cházhǎo)
prerequisites:
  - "[[Arrays]]"
  - "[[Recursion]]"
  - "[[Sequences]]"
  - "[[Logarithms]]"
leads_to:
  - "[[Sorting]]"
  - "[[Big-O Notation]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/algorithms
  - domain/searching
  - level/IGCSE
  - level/A-Level
  - level/AP
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/AP-CSA
  - curriculum/IB-CS
  - syllabus/IB-CS-B2-4
  - syllabus/0478-7-4
  - syllabus/9618-10-2
  - syllabus/9618-19-1a
  - syllabus/AP-CSA-4-14
  - syllabus/AP-CSA-4-17
  - type/deep
  - type/definition
  - type/algorithm
  - notation/python
  - misconception/binary-search-on-unsorted
  - misconception/binary-search-off-by-one
  - misconception/binary-search-always-better
  - misconception/binary-search-needs-random-access
---

# Searching 查找

## Definition

**Searching** is the problem of finding whether a target value is present in a collection — and if so, *where*. It is the first real *algorithm* most people meet, and the cleanest place to feel a truth that runs through all of computer science: **two programs that compute the same answer can take wildly different amounts of work.**

Two foundational algorithms, and the gap between them is the whole lesson:

- **Linear search** — walk through the list one element at a time until you find the target (or run out). Works on *any* list. In the worst case it looks at all $n$ elements.
- **Binary search** — only on a *sorted* list: look at the middle, decide which half the target must be in, throw the other half away, and repeat. Each step **halves** what's left, so it finishes in about $\log_2 n$ looks.

### 中文锚点

**查找**（cházhǎo）/ 搜索（sōusuǒ）：在一组数据里找目标值在不在、在哪里。

- **线性查找**（xiànxìng cházhǎo, linear search）：从头一个一个看，最多看 $n$ 个。**不要求有序**，任何列表都行。
- **二分查找**（èrfēn cházhǎo, binary search）：**必须先排好序**。每次看**中间**那个，砍掉一半，重复 —— 大约 $\log_2 n$ 次就够了。

一句话对比：线性查找简单但慢（看 $n$ 个）；二分查找快得多（看 $\log_2 n$ 个），代价是**数据必须有序**。一百万个数据，线性查找最多看一百万次，二分查找只要约 **20** 次（因为 $2^{20}\approx 10^6$）。这个差距，就是我们愿意先排序的全部理由。

## The phone-book intuition

You already do binary search; you just never named it. To find "Watanabe" in a paper phone book, **nobody** starts at page 1 and reads every name (that's linear search). You flip to the middle, see you're in the "M"s, and throw away the first half. You flip to the middle of what's left, land in "T", throw away another half. A few flips and you're there.

That instinct works *only because the phone book is sorted*. Hand someone a phone book with the names in random order and they're stuck reading every entry — back to linear search. The entire trade of binary search is right there: **it buys enormous speed with the single precondition that the data is in order.**

## Linear search

```python
def linear_search(A, target):
    for i in range(len(A)):
        if A[i] == target:
            return i          # found it, at index i
    return -1                 # walked the whole list, never found it
```

Nothing required of `A` — it can be sorted, shuffled, anything. Best case the target is first (1 look); worst case it's last or absent ($n$ looks). On average, about $n/2$. Simple, universal, and — for a single search of unsorted data — exactly the right tool.

## Binary search

The precondition: **`A` must be sorted** (say, ascending). The idea: track a window `[low, high]` that must contain the target if it's anywhere; each step shrinks the window by half.

```python
def binary_search(A, target):          # A sorted ascending
    low, high = 0, len(A) - 1
    while low <= high:
        mid = low + (high - low) // 2  # midpoint (overflow-safe form; see note below)
        if A[mid] == target:
            return mid                 # found
        elif A[mid] < target:
            low = mid + 1              # target is to the right → drop the left half
        else:
            high = mid - 1             # target is to the left  → drop the right half
    return -1                          # window emptied → not present
```

### A trace

Search for **23** in the sorted array `A = [1, 5, 8, 12, 17, 23, 29, 35, 40]` (indices 0–8):

| Step | low | high | mid | `A[mid]` | decision |
|---|---|---|---|---|---|
| 1 | 0 | 8 | 4 | 17 | $17 < 23$ → go right, `low = 5` |
| 2 | 5 | 8 | 6 | 29 | $29 > 23$ → go left, `high = 5` |
| 3 | 5 | 5 | 5 | **23** | found at index 5 ✓ |

Three comparisons. Linear search would have checked `1, 5, 8, 12, 17, 23` — **six**. On nine elements the gap is small; on nine *million* it is the difference between a flicker and a freeze.

![[searching-linear-vs-binary.svg]]
*The same search, two ways. Linear search (top) walks the array and checks six cells. Binary search (bottom) looks at the middle, throws away the half that can't contain the target, and repeats — the live window (blue) halves each step until 23 is cornered in three looks. The faded cells are the ones each step discards.*

## Why $\log_2 n$ — feel the halving

This is the heart of the card, and it is worth getting in your bones *before* any formal notation. Each comparison throws away **half** of what's left:

$$n \;\to\; \frac{n}{2} \;\to\; \frac{n}{4} \;\to\; \cdots \;\to\; 1.$$

The question "how many halvings take you from $n$ down to 1?" is exactly the question "$2^k = n$, solve for $k$" — and that is the definition of the **logarithm**, $k = \log_2 n$ (see [[Logarithms]]). So:

| List size $n$ | Linear search (worst) | Binary search (worst) |
|---|---|---|
| 1,000 | 1,000 | ~10 |
| 1,000,000 | 1,000,000 | ~20 |
| 1,000,000,000 | 1,000,000,000 | ~30 |

Look at the last column. **Going from a thousand to a billion — a million-fold more data — adds only twenty comparisons.** Better still: every time you *double* the data, binary search needs just **one more** look. Linear search, doubling the data, doubles the work. That contrast — "double the data, add one step" versus "double the data, double the work" — is the single most important reason computer scientists sort things, and the reason this card comes before the one that names it.

Watch it happen. Both searches start at the same instant and spend the *same* time on each look — but linear starts at the left edge and trudges, while binary starts in the **middle** and throws half the list away every step:

![[searching-race-linear-vs-binary.svg|697]]
*A live race on a 16-element list (target 57, at index 12). Linear (top, amber bar) checks all 13 cells up to the target. Binary (bottom, green bar) looks only at the 4 cells it needs — the middle, then the middle of what's left — dimming the half it discards each step. Binary is done in about a third of the time, and the cost bars tell the whole story: the more you'd scale the list up, the more lopsided that race becomes. (Loops; the animation plays in Obsidian's preview and any browser.)*

> [!info] We are deliberately not saying "O(log n)" yet
> You will soon learn to compress "about $\log_2 n$ comparisons, growing one step per doubling" into three characters: $O(\log n)$. That formal language — and the whole vocabulary of $O(n)$, $O(n^2)$, $O(2^n)$ — is the subject of [[Big-O Notation]], and it only earns its keep *once you have algorithms like these two to compare*. Meet the algorithms first; let the notation name what you already feel. (This ordering is intentional — Big-O before any real algorithm is a measuring tape with nothing to measure.)

## Binary search *is* recursion

Binary search is the purest example of **divide and conquer**: solve the problem by discarding half the input and solving the same problem on what remains. Written recursively, its structure is naked:

```python
def binary_search(A, target, low, high):
    if low > high:                       # base case: empty window → not here
        return -1
    mid = low + (high - low) // 2
    if A[mid] == target:                 # base case: found
        return mid
    elif A[mid] < target:
        return binary_search(A, target, mid + 1, high)   # recurse on the right half
    else:
        return binary_search(A, target, low, mid - 1)    # recurse on the left half
```

This is the canonical recursive algorithm from [[Recursion]] — two base cases (empty window, or hit) and one recursive case that shrinks the input. The recursion's "tree" is a single path that halves each step, which is *why* the cost is $\log_2 n$ — as [[Recursion]] puts it, *the shape of the recursion tree is the time cost.* (The iterative `while`-loop version above does the identical work without the call stack; for binary search either form is fine, but the recursive one shows the idea.)

## The precondition is the whole trade

Binary search's speed is not free — it is *rented*, and the rent is **sorted data**. That changes the engineering question from "which search is faster?" to "what am I actually doing?":

- **Searching unsorted data once?** Just linear-search it. Sorting first would cost *more* than the single scan you're trying to avoid.
- **Searching the same collection many times?** Sort it **once** (see [[Sorting]]), then binary-search forever after. The sort is a one-time investment that every later lookup repays.

So the two algorithms aren't really rivals; they answer different questions. Binary search wins when order already exists or will be reused; linear search wins for one-off lookups and tiny lists. *Knowing which situation you're in is the actual skill.*

## Worked examples

### Example 1 — linear search

Find `7` in `A = [3, 9, 7, 1, 5]` (unsorted). Check `A[0]=3` ✗, `A[1]=9` ✗, `A[2]=7` ✓ → return index 2. Three comparisons; no sorting needed.

### Example 2 — binary search, "not found"

Find `10` in sorted `A = [1, 5, 8, 12, 17]`. `low=0, high=4, mid=2 → A[2]=8 < 10 →` `low=3`. `low=3, high=4, mid=3 → A[3]=12 > 10 →` `high=2`. Now `low(3) > high(2)` → window empty → returns **-1** (not found). The collapsing window is how binary search reports absence.

### Example 3 — "guess my number, 1 to 100"

A friend picks a number 1–100; each guess they say "higher" or "lower." The optimal strategy *is* binary search: guess **50**, halve the range each time. Worst case you need **7** guesses, because $2^7 = 128 \ge 100 > 64 = 2^6$. Most people play this game by instinct and never realise they've been running an $O(\log n)$ algorithm since childhood.

## Common Misconceptions (Teaching Notes)

### 1. Running binary search on unsorted data

It will happily return a confident, *wrong* answer (or miss a value that's present). The "sorted" precondition isn't a suggestion.

**Fix.** Before binary search, the question is always "is this sorted?" If not: sort it first (and only if you'll search repeatedly), or use linear search.

### 2. The off-by-one / overflow bug

Binary search is famous for being *easy to write and hard to write correctly* — by one account most published versions were buggy for years. The traps: updating `low`/`high` to `mid` instead of `mid ± 1` (infinite loop), or using `<` instead of `<=` in the loop condition (misses the last element).

**Fix.** Memorise a known-correct template, update strictly to `mid + 1` / `mid - 1`, keep `low <= high`, and compute `mid = low + (high - low) // 2`. That last form avoids a real bug: in fixed-width-integer languages (Java, C, Go) the naive `(low + high) // 2` can *overflow* when both indices are large, silently wrapping to a negative midpoint. Python's integers are arbitrary-precision, so the overflow can't happen here — but the `low + (high - low) // 2` habit is worth keeping, because the day you port the idea to Java it matters.

### 3. "Binary search is always better"

Only when the data is sorted *and* you'll search it enough to amortise the sort. For a single lookup of unsorted data, or a list of five items, linear search is simpler and just as fast in practice.

**Fix.** Ask "sorted already? searching repeatedly?" If not both, linear search is the right call.

### 4. Thinking it works on any data structure

Binary search needs **random access** — jumping to `A[mid]` in one step. That's true for an array, but *not* for a linked list, where reaching the middle means walking from the front (so binary search on a linked list is no faster than linear).

**Fix.** Binary search belongs to arrays (and array-backed structures); for linked structures the fast-lookup tool is something else (a balanced tree or hash table).

## Exam Notes

### Cambridge 0478 (IGCSE CS)

**§7.4 — Standard methods of solution**, whose "limited to" list is exactly five items: **linear search, bubble sort, totalling, counting, and finding maximum / minimum / average values**. This card closes the *search* item; the sort item is [[Sorting]]'s; the remaining three — totalling, counting and the max/min/average sweep — belong to none of them, which is why the row stays partial. Linear search is examinable as pseudocode plus a trace table (§7.7 is the trace-table row, §7.9 the write-and-amend row), and it will be asked over an array, so the indexing vocabulary of [[Arrays]] is assumed.

**Binary search is not on 0478 at all** — the "limited to" list is closed, so a binary search offered where a linear one was asked for earns nothing. This is the sharpest board difference on the card: the algorithm this whole card builds toward is A-Level only.

### Cambridge 9618 (A-Level CS)

**§10.2 — Arrays** is where searching first appears: the LO is "write pseudocode to **process array data** — search using a linear search". So at AS the search is a *thing you do to an array*, and the mark is for the loop over indices, not for a named algorithm. The row itself belongs to [[Arrays]] — the bounds, the index vocabulary and the choice of structure — and this card supplies only the processing half of it.

**§19.1 — Algorithms** is where it becomes the algorithm itself, and the verb changes to **write**: an algorithm for linear search, an algorithm for binary search, **the conditions necessary for binary search**, and **how binary-search performance varies with the number of data items**. Both are also examined at a keyboard on Paper 4. This card closes both rows — linear and binary, each with correctness reasoning and an iterative trace.

Two traps worth knowing. The conditions question wants *sorted* **and** *random access* — a sorted linked list defeats binary search, and that is the discriminator. And "algorithmic efficiency" is **not** an AS row: the formal comparison lives in §19.1's Big O bullet, handled in [[Big-O Notation]]. Bubble and insertion sort, the other half of both rows, are in [[Sorting]].

### AP Computer Science A

**Unit 4.14 — Searching:** linear search and binary search (explicitly "binary search requires a sorted list"). This card closes 4.14. The recursive binary-search form also feeds **4.17 (Recursive Searching and Sorting)**, alongside [[Recursion]].

### IB Computer Science (B2.4)

Both searches are **named statements**: linear and binary search at SL, with the compare-efficiency framing ("why does binary need a sorted list, and what does it buy?"). The 9618 trace discipline transfers whole — IB asks the same walk-through in scenario dress, usually alongside its sorting siblings. The `curriculum/IB-CS` claim here is exactly this subsection.

## Connections

- **Prerequisite:** [[Arrays]] — the structure both algorithms walk, and the reason binary search is possible at all: jumping straight to the middle element is the array's constant-time indexing. [[Recursion]] — binary search is its canonical divide-and-conquer example (Recursion reserves this card as the place that pays that promise off). [[Logarithms]] — the $\log_2 n$ that the halving produces. [[Sequences]] — the mathematical view of an indexed list.
- **Next:** [[Sorting]] — the algorithm that *creates* the sorted order binary search depends on (selection / insertion / merge). [[Big-O Notation]] — the formal language for the $n$-vs-$\log n$ gap this card makes you feel; it comes *after* you have algorithms to compare.
- **Bay:** the first card in `CS/Algorithms/`. Its quiet partner is [[Recursion]] (over in `CS/Foundations/` — the *algorithm of algorithms*, the control structure this catalogue is written in). Neighbours in the wider CS tree: [[Logic Gates]] and [[Information Theory]].

---

## Beyond Syllabus

### Searching without comparing — hash tables

Both algorithms here *compare* the target against stored values. There's a faster idea that doesn't: a **hash table** computes *where* a value would be stored directly from the value itself, giving average **$O(1)$** lookup — find-without-searching. The cost is that it gives up order (you can't ask "what's the next-biggest?") and it leans on probability to avoid collisions (the same Birthday-Problem mathematics noted in [[Combined Probability]]). Sorted arrays + binary search vs hash tables is one of the first real *data-structure trade-offs* a programmer makes.

### Binary-searching the answer, not the array

The deepest version of the idea: binary search works on **any monotonic yes/no question**, not just a sorted array. "What is the smallest machine that finishes the job in time?" — if "can a machine of size $x$ finish in time?" flips from *no* to *yes* exactly once as $x$ grows, you can binary-search $x$ itself. This "binary search on the answer" is a workhorse of competitive programming and optimisation, and it's the same halving logic pointed at an abstract space instead of a list.

### git bisect

When a bug appears somewhere in thousands of commits, `git bisect` binary-searches your project's history: check the middle commit, ask "is the bug here?", discard half the timeline, repeat. ~20 checks locate the guilty commit among a million. It is the phone-book trick aimed at *time* — and a perfect example of [[Forward Reading and Problem Discovery]]'s causal-tracing, made $\log n$ instead of $n$.

## Python / Notation Reference

| Symbol | Meaning |
|--------|---------|
| `A[i]` | the element at index `i` of list `A` (0-based) |
| `len(A)` | the number of elements in `A` |
| `low`, `high` | the inclusive bounds of the current search window |
| `mid` | the midpoint index, `low + (high - low) // 2` |
| `//` | integer (floor) division |
| `return -1` | the sentinel returned when the target is absent (Python's idiomatic "not found") |
| $\log_2 n$ | number of halvings from $n$ to $1$ — the binary-search comparison count |
