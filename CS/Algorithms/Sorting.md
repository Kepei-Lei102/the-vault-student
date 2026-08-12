---
chinese: 排序 (páixù)
prerequisites:
  - "[[Arrays]]"
  - "[[Searching]]"
  - "[[Recursion]]"
  - "[[Sequences]]"
leads_to:
  - "[[Big-O Notation]]"
  - "[[Parallel and External Sorting]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/algorithms
  - domain/sorting
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
  - syllabus/9618-19-1b
  - syllabus/AP-CSA-4-15
  - syllabus/AP-CSA-4-17
  - type/deep
  - type/algorithm
  - notation/python
  - misconception/bubble-sort-is-good
  - misconception/sorting-is-free
  - misconception/selection-fewer-comparisons
  - misconception/one-true-sort
---

# Sorting 排序

## Definition

**Sorting** is the problem of rearranging a collection into order — ascending or descending, by some key. It is the workhorse of computing: spreadsheets, leaderboards, search engines, database indexes, and the contacts in your phone are all sorted, and they are sorted because *order is what makes everything afterwards fast.*

That "afterwards" is the link back to [[Searching]]. Binary search is dramatically faster than linear search — but it has one precondition: **the list must be sorted.** Sorting is the price you pay, once, to unlock that speed forever after. So the two cards are two halves of one idea: sorting *creates* the order, searching *spends* it.

There is no single "sort algorithm." There are many, and they make different trade-offs between *how simple they are to write* and *how much work they do*. This card builds the four that the syllabuses ask for — **bubble, selection, insertion,** and **merge** — on a single shared example so you can watch the same five numbers fall into line four different ways. Then it adds a fifth, **quicksort**, which no exam board requires but every programmer meets — it's the sort most languages reach for under the hood.

### 中文锚点

**排序**（páixù, sorting）：把一组数据按大小（升序 ascending / 降序 descending）重新排列。

- **冒泡排序**（màopào páixù, bubble sort）：相邻两个比较，逆序就交换；最大的像气泡一样「浮」到最后。
- **选择排序**（xuǎnzé páixù, selection sort）：每次从未排序部分**选出最小**的，放到前面。
- **插入排序**（chārù páixù, insertion sort）：像理扑克牌，把每张牌**插入**到前面已排好的位置。
- **归并排序**（guībìng páixù, merge sort）：**分**成两半，各自排好，再**合并**——这是 [[Recursion]] 的分治思想。
- **快速排序**（kuàisù páixù, quicksort，**考纲外**）：选一个**基准** pivot，比它小的放左、大的放右，再对两边递归——和归并一样是分治，但**按值**分而不是按位置分，且**原地**排序。实战中最常用。

一句话：前三种简单但慢（约 $n^2$ 次操作），归并排序和快速排序用「分而治之」做到约 $n\log n$ —— 和二分查找同一个 $\log$。**为什么愿意先排序？** 因为排好一次，之后每次 [[Searching|二分查找]] 都快得飞起。

## The shared example

Every algorithm below sorts the **same** five-element list into ascending order:

$$A = [\,5,\ 1,\ 4,\ 2,\ 8\,] \quad\longrightarrow\quad [\,1,\ 2,\ 4,\ 5,\ 8\,].$$

Same input, same output, four different routes. Watch *how* each one gets there — that's where the personalities differ.

## Bubble sort 冒泡排序

The simplest to describe: walk the list comparing **adjacent** pairs, and swap any that are out of order. One full pass drags the largest remaining value to the end (it "bubbles up"). Repeat until a pass makes no swaps — then you know it's sorted.

```python
def bubble_sort(A):
    n = len(A)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):       # the last i items are already in place
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]   # swap neighbours
                swapped = True
        if not swapped:                  # a clean pass → already sorted
            break
    return A
```

The `swapped` flag is the **early-exit optimisation**: if a whole pass moves nothing, the list is sorted and we stop. Tracing `A = [5, 1, 4, 2, 8]`:

| Pass | Comparisons | Swaps | List after the pass |
|---|---|---|---|
| 1 | 4 | 3 | `[1, 4, 2, 5, 8]` — `8` bubbled to the end |
| 2 | 3 | 1 | `[1, 2, 4, 5, 8]` — `5` now in place |
| 3 | 2 | 0 | `[1, 2, 4, 5, 8]` — no swaps → **early exit** |

Each pass guarantees one more value parks permanently at the right end, which is why pass $i$ can stop $i$ places early.

![[sort-bubble.mp4]]
*Bubble sort on 50 random bars. Amber = the adjacent pair being compared; green = bars already locked at the right. Watch the sorted region creep in from the right one pass at a time — and how long the grind takes (≈1,200 comparisons). Press play.*

## Selection sort 选择排序

Different instinct: don't fuss with neighbours — **scan the whole unsorted part for the smallest value**, then drop it into the next position with a single swap.

```python
def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):        # search the unsorted tail
            if A[j] < A[smallest]:
                smallest = j
        A[i], A[smallest] = A[smallest], A[i]   # one swap puts it home
    return A
```

Tracing `A = [5, 1, 4, 2, 8]` — the **bold** value is the minimum found in the unsorted tail:

| Step `i` | Minimum found | List after the swap |
|---|---|---|
| 0 | **1** (index 1) | `[1, 5, 4, 2, 8]` |
| 1 | **2** (index 3) | `[1, 2, 4, 5, 8]` |
| 2 | **4** (index 2) | `[1, 2, 4, 5, 8]` (already home, no move) |
| 3 | **5** (index 3) | `[1, 2, 4, 5, 8]` |

Selection sort makes the *fewest swaps* of the three quadratic sorts — at most $n-1$ of them — but it never gets to quit early: it always scans the entire tail, even on an already-sorted list.

![[sort-selection.mp4]]
*Selection sort on 50 random bars. Each pass scans the whole unsorted region for the smallest bar (amber), swaps it into the next slot, and locks it (green). Few swaps, but the green block grows slowly — it still scans everything every pass. Press play.*

## Insertion sort 插入排序

How you sort a hand of playing cards. Keep a sorted prefix on the left; take the next card and **slide it back** until it sits in the right spot.

```python
def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]                       # the card we're placing
        j = i - 1
        while j >= 0 and A[j] > key:     # shift bigger items one step right
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key                   # drop the card into the gap
    return A
```

Tracing `A = [5, 1, 4, 2, 8]` — `key` is the card being inserted into the sorted prefix:

| Step `i` | `key` | List after inserting |
|---|---|---|
| 1 | 1 | `[1, 5, 4, 2, 8]` |
| 2 | 4 | `[1, 4, 5, 2, 8]` |
| 3 | 2 | `[1, 2, 4, 5, 8]` |
| 4 | 8 | `[1, 2, 4, 5, 8]` (8 ≥ 5, no shift) |

Insertion sort has a lovely property: on a list that's **already nearly sorted**, each card barely moves, so it's close to linear. It's the sort real libraries fall back on for small or almost-ordered inputs.

![[sort-insertion.mp4]]
*Insertion sort on 50 random bars. The left block (green) is the sorted hand; each step lifts the next bar (amber) and slides it back into place. Notice it speeds up wherever the data already happens to be in order. Press play.*

## Merge sort 归并排序

The first three are *quadratic*: roughly $n^2$ operations, because each element is compared against many others. Merge sort breaks that ceiling with the idea from [[Recursion]] — **divide and conquer**:

1. **Divide** the list into two halves.
2. **Conquer** — sort each half (by calling merge sort on it: that's the recursion).
3. **Combine** — *merge* two already-sorted halves into one sorted list by repeatedly taking the smaller front element.

```python
def merge_sort(A):
    if len(A) <= 1:              # base case: 0 or 1 element is already sorted
        return A
    mid = len(A) // 2
    left  = merge_sort(A[:mid])  # recurse on the left half
    right = merge_sort(A[mid:])  # recurse on the right half
    return merge(left, right)    # combine two sorted halves

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # take the smaller front element
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])      # one side is exhausted; append the rest
    result.extend(right[j:])
    return result
```

The recursion splits `[5, 1, 4, 2, 8]` down to single elements, then merges back up:

```
            [5, 1, 4, 2, 8]
           /               \
       [5, 1]            [4, 2, 8]
       /    \            /       \
     [5]   [1]        [4]       [2, 8]
       \   /            \       /    \
       [1, 5]          [4]    [2]   [8]
          \              \      \   /
           \              \     [2, 8]
            \              \    /
             \            [2, 4, 8]
              \           /
              [1, 2, 4, 5, 8]
```

The **merge** is the clever part. Because both halves are *already* sorted, combining them is one linear scan: keep comparing the two front elements and take the smaller. That's why the splitting (≈ $\log_2 n$ levels of halving — the same $\log$ as binary search in [[Searching]]) times the linear merge at each level gives merge sort its **$n\log n$** cost.

![[sorting-merge-tree.svg|697]]
*Merge sort on `[5, 1, 4, 2, 8]`: divide down to singletons (which are trivially sorted), then merge sorted pairs back up. Each merge zips two ordered lists into one in a single pass. The number of levels is $\log_2 n$ — the same halving that powers binary search.*

![[sort-merge.mp4]]
*Merge sort on 50 random bars. Each **box** marks a stretch that's already sorted; watch the boxed runs fuse pairwise into longer boxed runs (the amber box is the merge happening right now) until one box wraps the whole array — and it finishes in a fraction of the comparisons bubble or selection needs. Press play.*

## Quicksort 快速排序

> [!info] Beyond syllabus — but worth it
> Quicksort is on **none** of the three CS boards (0478, 9618, AP CSA). It's here because it's the sort your programming language almost certainly uses under the hood, and because it's the most instructive *other* way to be divide-and-conquer.

Merge sort divides by **position** (cut the list in half regardless of values) and does its real work in the *merge*. Quicksort flips that: it divides by **value** and does its real work in the *split*, so there's nothing left to merge afterwards.

The plan: pick one element as the **pivot**, then **partition** the rest into "less than the pivot" and "greater than the pivot." The pivot is now in its final sorted position — everything smaller is left of it, everything larger is right of it. Recurse on each side.

```python
def quick_sort(A):
    if len(A) <= 1:                      # base case: 0 or 1 element is sorted
        return A
    pivot   = A[len(A) // 2]             # choose a pivot (here: the middle element)
    less    = [x for x in A if x < pivot]
    equal   = [x for x in A if x == pivot]
    greater = [x for x in A if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)
```

Tracing `A = [5, 1, 4, 2, 8]` with the middle element `4` as the first pivot:

```
quick_sort([5, 1, 4, 2, 8])      pivot = 4
   less = [1, 2]   equal = [4]   greater = [5, 8]
        quick_sort([1, 2])       pivot = 2  → [1] + [2] + []      = [1, 2]
        quick_sort([5, 8])       pivot = 8  → [5] + [8] + []      = [5, 8]
   → [1, 2] + [4] + [5, 8]                                        = [1, 2, 4, 5, 8]
```

> [!warning] The readable version above is *not* how quicksort is normally written
> Building three new lists (`less`/`equal`/`greater`) makes the idea crystal clear, but it throws away quicksort's headline advantage: real quicksort **partitions in place**, swapping elements within the one array using no extra storage. That in-place partition is exactly why quicksort is the *practical* champion — it's cache-friendly and memory-light where merge sort needs an extra $O(n)$ scratch array. Learn the idea from the clear version; reach for an in-place partition (Lomuto or Hoare) in real code.

**Cost.** When the pivot splits the list roughly in half each time, quicksort has $\log_2 n$ levels of partitioning, each costing a linear scan — so **average $n\log n$**, the same league as merge sort. But a *bad* pivot — say, always picking the smallest or largest element (which happens if you naively pivot on the first element of an already-sorted list) — splits off just one element at a time, collapsing to $n$ levels and a **worst case of $n^2$**. Practical implementations dodge this by choosing the pivot well (median-of-three, or a random element), making the bad case astronomically unlikely.

**Merge vs quick — two divide-and-conquer twins.** Both are $n\log n$ on average and both are recursion at full size, but they trade off oppositely:

| | Merge sort | Quicksort |
|---|---|---|
| Divides by | position (always in half) | value (around a pivot) |
| Work happens in | the **merge** (combine step) | the **partition** (divide step) |
| Worst case | $n\log n$ (guaranteed) | $n^2$ (bad pivots) |
| Extra memory | $O(n)$ scratch array | $O(\log n)$ — sorts **in place** |
| Stable? | yes | usually no |

That's why libraries pick by context: merge-sort-family (Timsort) when stability and a worst-case guarantee matter, quicksort when raw in-place speed wins.

![[sort-quicksort.mp4]]
*Quicksort on 50 random bars. The **pivot is red**; each partition flings the other values to its left (smaller) or right (larger), then the pivot drops into its final slot and turns green — and the sorted regions spread out from those locked pivots. Finishes in roughly the same few-hundred comparisons as merge sort. Press play.*

## Why some sorts are slow and others fast — feel the cost

You don't need formal notation to feel the gap; you just need to count *roughly how many comparisons* each does on a list of $n$ items.

- **Bubble, selection, insertion** compare (almost) every item against (almost) every other: about $\tfrac{n(n-1)}{2}\approx n^2/2$ comparisons. Double the list, and the work **quadruples**.
- **Merge sort and quicksort** do $\log_2 n$ levels of halving, each level costing one linear $n$-element pass (merge sort in the merge, quicksort in the partition): about $n\log_2 n$. Double the list, and the work barely more than doubles. (Quicksort hits this on average; merge sort guarantees it.)

| List size $n$ | Quadratic sort (≈ $n^2$) | Merge / quicksort (≈ $n\log_2 n$) |
|---|---|---|
| 10 | ~100 | ~33 |
| 1,000 | ~1,000,000 | ~10,000 |
| 1,000,000 | ~1,000,000,000,000 | ~20,000,000 |

At a million items the quadratic sorts are doing a *trillion* operations — minutes to hours — while the $n\log n$ sorts do tens of millions, a blink. That is exactly why real systems sort with $n\log n$ algorithms. (The simple sorts still earn their place: they're easy to write correctly, and on tiny or nearly-sorted lists the constant-factor overhead of merge sort isn't worth it.)

Don't take the numbers on faith — watch it. All five sorts below run on the **same** shuffled 50-element array at once, each counting its own comparisons:

![[sort-race.mp4]]
*The same 50 bars, five sorts, started together (one comparison = one tick, so the bars race on equal terms). Merge and quicksort finish and freeze while bubble, selection, and insertion are still grinding — and the comparison counters tell the story in numbers: a few hundred for the $n\log n$ sorts versus well over a thousand for the quadratic ones. This is the $n^2$-vs-$n\log n$ gap, made into a race. Press play.*

> [!info] We are deliberately not saying "O(n²)" or "O(n log n)" yet
> You'll soon compress "about $n^2/2$ comparisons, quadrupling when the list doubles" into a single symbol, $O(n^2)$, and "$n\log n$, barely more than doubling" into $O(n\log n)$. That formal language — and *why* we throw away the constant $\tfrac12$ and the lower-order terms — is the subject of [[Big-O Notation]]. It only earns its keep once you have real algorithms like these five to compare. You now have them; the notation is just the name for what you already feel here.

## The trade-off — which sort, when?

The four aren't ranked best-to-worst; they answer different questions:

- **Tiny list (a handful of items)?** Any of them. Insertion sort is the usual pick — simplest correct code, and fast in practice on small inputs.
- **Almost-sorted data?** Insertion sort, which glides through nearly-ordered lists close to linearly.
- **Large list, performance matters?** Merge sort (or another $n\log n$ method like quicksort/heapsort). The $n\log n$ vs $n^2$ gap is decisive at scale.
- **Memory is tight?** Bubble/selection/insertion sort **in place** (no extra array); classic merge sort needs an extra $O(n)$ of scratch space to merge into. That space cost is merge sort's hidden rent.

And the headline reason to sort at all: **so you can [[Searching|binary-search]] afterwards.** Sort once ($n\log n$), then every later lookup is $\log n$ instead of $n$. If you only ever search once, don't bother sorting — just linear-scan. If you'll search again and again, sorting pays for itself almost immediately.

## Worked examples

### Example 1 — one bubble pass by hand

Do a single pass of bubble sort on `[3, 8, 2, 5]`. Compare `(3,8)` — in order. `(8,2)` — swap → `[3, 2, 8, 5]`. `(8,5)` — swap → `[3, 2, 5, 8]`. After one pass: `[3, 2, 5, 8]`; the largest value `8` has bubbled to the end. (A second pass fixes `(3,2)`; a third makes no swaps and the early-exit triggers.)

### Example 2 — selection vs insertion on the same step

On `[7, 3, 9, 4]`: **selection** sort's first move scans for the minimum (`3`) and swaps it to the front → `[3, 7, 9, 4]`. **Insertion** sort's first move takes `key = 3` and slides it past `7` → `[3, 7, 9, 4]`. Same result here, but for opposite reasons: selection *pulls the smallest forward*; insertion *pushes the current card back*.

### Example 3 — the merge step

Merge two already-sorted lists `[1, 4, 7]` and `[2, 3, 8]`. Compare fronts: `1<2` → take 1. `4>2` → take 2. `4>3` → take 3. `4<8` → take 4. `7>... ` take from left: `7<8` → take 7. Left exhausted → append the rest of right: `8`. Result `[1, 2, 3, 4, 7, 8]` — one clean linear pass, no back-tracking, because both inputs were sorted.

## Common Misconceptions (Teaching Notes)

### 1. "Bubble sort is a good sort"

Bubble sort is the most *taught* sort because it's the easiest to explain — not because it's good. It's among the slowest in practice (lots of swaps), and no serious system uses it. Its value is pedagogical: it makes "compare and swap" visible.

**Fix.** Learn bubble sort to understand the *idea* of comparison sorting; reach for insertion sort (small/nearly-sorted) or an $n\log n$ sort (everything else) in real code.

### 2. "Sorting is basically free"

Sorting is *not* free — the quadratic sorts cost ≈ $n^2$, and even the fast ones cost $n\log n$. The whole reason binary search is worth it is that you **amortise** the sort over many searches. Sort once to search many times; never sort just to do a single lookup.

**Fix.** Ask "how many times will I search this?" One search → linear scan, don't sort. Many searches → sort once, then binary-search.

### 3. "Selection sort is faster because it makes fewer swaps"

Selection sort does make the fewest *swaps* (≤ $n-1$), but swaps aren't the bottleneck — **comparisons** are, and it still makes ≈ $n^2/2$ of them, scanning the whole unsorted tail every time. Fewer swaps, same quadratic comparison cost.

**Fix.** Count the operation that dominates. For these sorts it's comparisons, and all three simple sorts are quadratic in comparisons.

### 4. "There's one correct sorting algorithm"

There are dozens, and the "best" one depends on the data and the constraints — size, how nearly-sorted it already is, available memory, whether equal elements must keep their original order (*stability*). Choosing the right sort for the situation is the actual skill.

**Fix.** Match the algorithm to the input: small/nearly-sorted → insertion; large → merge/quick/heap; memory-limited → an in-place sort.

## Exam Notes

### Cambridge 0478 (IGCSE CS)

**§7.4 — Standard methods of solution**, a closed "limited to" list of five: linear search, **bubble sort**, totalling, counting, and finding maximum / minimum / average values. This card closes the bubble-sort item; linear search is [[Searching]]'s; totalling, counting and the max/min/average sweep are covered by neither, so the row stays partial rather than closing on the pair.

You must be able to describe the method and **trace it with a trace table** (§7.7), including that each pass fixes one more value at the end and that a pass with no swaps means the list is sorted. **Merge, selection and insertion sort are not on 0478** — the list is closed, so offering one where a bubble sort was asked for scores nothing. The data will be in an array, so the index and bounds vocabulary of [[Arrays]] is assumed, and §7.8's identify-the-errors questions plant array-shaped bugs into sort code: a loop running to the upper bound instead of one short of it, or a swap that loses a value by assigning in the wrong order.

### Cambridge 9618 (A-Level CS)

**§10.2 — Arrays** is where sorting first appears, and it appears in disguise: the LO is "write pseudocode to **process array data** — sort using a bubble sort". At AS the sort is a *thing you do to an array*, so the marks are for the nested loop and the swap, not for naming a strategy. **Bubble is the only sort named at AS.** The row as a whole belongs to [[Arrays]] — bounds, terminology and choosing 1D or 2D — and this card supplies its processing half.

**§19.1 — Algorithms** promotes it, and the verb becomes **write**: an algorithm for **insertion sort** and an algorithm for **bubble sort**, plus the observation that **performance may depend on the initial order of the data** as well as the number of items. Both are examined again at a keyboard on Paper 4. This card closes both rows.

That initial-order bullet is the one students drop. It is asking for the almost-sorted case — where insertion sort finishes in near-linear time and bubble sort's no-swaps flag lets it exit after a single pass — and it is the whole reason both sorts are on the syllabus rather than one. The *formal* cost comparison is §19.1's Big O bullet, in [[Big-O Notation]]; linear and binary search, the other half of both rows, are in [[Searching]].

### AP Computer Science A

**Unit 4.15 — Sorting:** **selection sort, insertion sort,** and **merge sort** (the recursive divide-and-conquer one). This card closes 4.15. The recursive structure of merge sort also completes **4.17 (Recursive Searching and Sorting)** alongside [[Recursion]] and [[Searching]] (recursive binary search). AP frames cost informally ("informal run-time comparisons") — the [[Big-O Notation]] card carries the formal version for students going further.

### IB Computer Science (B2.4)

**Bubble and selection sort are the named IB pair** (SL) — trace, describe, and compare; merge/quick stay enrichment there just as merge stays the 9618 extension. The pass-fixes-one-value and no-swaps-means-sorted observations earn marks in identical words; efficiency comparisons lean on the Big-O framing of [[Big-O Notation]].

## Connections

- **Prerequisite:** [[Arrays]] — the structure being sorted; every swap here is two indexed writes, and the constant-time indexing is what makes them cheap. [[Searching]] — the sibling algorithm and the reason sorting matters (binary search needs sorted data). [[Recursion]] — merge sort *is* a divide-and-conquer recursion; its base case (a 1-element list) and recursive case (sort each half) are the canonical pattern. [[Sequences]] — the mathematical view of an indexed list.
- **Next:** [[Big-O Notation]] — the formal language for the $n^2$ vs $n\log n$ gap this card makes you feel; it comes *after* you have algorithms to compare.
- **Bay:** the second card in `CS/Algorithms/`, following [[Searching]]. Together they close the search-and-sort core that every CS syllabus tests.
- **Application:** sorting underlies database indexes, leaderboards, deduplication, and — most directly — making [[Searching|binary search]] possible.

---

## Beyond Syllabus

### The rest of the $n\log n$ family

Merge sort and **quicksort** (above) aren't the only fast sorts. **Heapsort** uses a binary-heap structure to achieve a *guaranteed* $n\log n$ while sorting in place — quicksort's memory thrift without quicksort's $n^2$ worst case, at the cost of being slower in practice and unstable. Real-world libraries usually ship a **hybrid**: Python's and Java's **Timsort** is merge sort fused with insertion sort, tuned to detect and exploit already-ordered "runs" in real-world data (which is rarely random). When you call `sorted()` in Python, that's Timsort doing the work.

### Parallel and external merge sort — why the big systems lean on merge

Here's a hook worth leaving for later, well past any syllabus. Quicksort is often the fastest sort *in memory, on a single core* — yet step up to **huge data or many cores and merge sort takes over.** Two reasons, both structural. First, merge sort's two halves are completely independent, so you can sort them on different cores (or different *machines*) and combine afterward; its divide-and-conquer shape parallelizes cleanly, where quicksort's partition is awkward to split and load-balance. Second, the **$k$-way merge** is the natural way to stitch together already-sorted chunks streaming off disk when the data is far too big for RAM. Put together, that's **external / parallel merge sort** — the workhorse behind how databases and big-data systems sort terabytes. It's also why several languages make a *merge*-based sort their default (Python's and Java's **Timsort**), trading a little raw speed for stability, a guaranteed worst case, and adaptivity to the partly-ordered data real programs actually see. Quicksort isn't beaten — it's still the default for in-memory, unstable sorting of primitives (C++'s `std::sort`) — so the honest headline is subtler than "merge beats quick": **merge wins where stability, worst-case guarantees, or parallelism matter; quick wins raw single-core speed.** The full story — parallel sorting, external sorting, and how MapReduce-style systems sort at scale — is a card of its own: [[Parallel and External Sorting]].

> [!info] Credit
> The parallel-merge-sort angle here — and the nudge that it's the real reason industry leans on merge at scale — comes from **Modric Wang**. Thanks, Modric.

### The $n\log n$ lower bound

Here's a genuinely deep result: *any* sort that works only by **comparing** elements must make at least about $n\log n$ comparisons in the worst case — you cannot beat merge sort's order by cleverness alone. The proof is a counting argument: there are $n!$ possible orderings, each comparison has two outcomes, so a decision tree distinguishing all $n!$ cases needs depth at least $\log_2(n!) \approx n\log_2 n$ (by Stirling's approximation). Comparison sorting has a *speed limit*, and merge sort already hits it.

### Sorting without comparing

That lower bound only binds *comparison* sorts. If you know something about the data — say, they're integers in a small range — you can sort **without comparing at all**, in linear $O(n)$ time, using **counting sort** or **radix sort** (which sorts digit by digit, the way old punch-card machines did). It's the same lesson as the hash table in [[Searching]]: stepping outside "compare two things" can break a barrier that looks fundamental.

### Stability

A sort is **stable** if equal elements keep their original relative order. It sounds like a technicality until you sort a table by one column and want ties broken by the previous sort order — then stability is exactly what lets you sort by surname, then by first name, and get the result you expect. Merge sort and insertion sort are naturally stable; selection sort and many quicksorts are not.

## Python / Notation Reference

| Symbol | Meaning |
|--------|---------|
| `A[i]` | the element at index `i` of list `A` (0-based) |
| `len(A)` | the number of elements in `A` |
| `A[i], A[j] = A[j], A[i]` | Python's one-line **swap** of two elements |
| `A[:mid]`, `A[mid:]` | list **slices** — the left and right halves |
| `//` | integer (floor) division — used for the midpoint |
| `key` | the element insertion sort is currently placing |
| `pivot` | the value quicksort partitions around |
| `[x for x in A if x < pivot]` | a Python **list comprehension** — builds the sublist of elements less than the pivot |
| $n\log_2 n$ | merge/quicksort comparison count — $\log_2 n$ halving levels × linear pass per level |
| $n^2$ | the rough comparison count of bubble / selection / insertion sort |
