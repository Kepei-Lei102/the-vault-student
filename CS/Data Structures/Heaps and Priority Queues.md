---
chinese: 堆与优先队列 (duī yǔ yōuxiān duìliè)
prerequisites:
  - "[[Binary Trees]]"
  - "[[Graphs]]"
  - "[[Stacks and Queues]]"
  - "[[Big-O Notation]]"
leads_to: []
teach_together:
  - "[[Parallel and External Sorting]]"
tags:
  - subject/computer-science
  - domain/data-structures
  - domain/algorithms
  - level/university
  - type/deep
  - misconception/heap-is-sorted
  - misconception/heap-is-a-bst
  - misconception/heapify-is-n-log-n
  - misconception/priority-queue-is-fifo
---

# Heaps and Priority Queues 堆与优先队列

> *An arrow will hit in two ticks. A shield will expire in five. An enemy will spawn in five. Then a speed boost changes the arrow's arrival time. The simulation keeps asking one question: **what happens next?** Sorting the entire future after every change is an expensive way to answer such a small question.*

## Definition

### Formal

A **priority queue** is an abstract data type whose items carry ordered **keys**. It supports inserting an item, inspecting an item of highest priority, and removing that item. The application decides which key means highest priority; here **smaller keys are served first**. Equal keys require a separate tie policy.

A **binary min-heap** implements this promise with two invariants:

1. **Shape:** a complete binary tree — every level is full except possibly the last, which fills from left to right.
2. **Order:** every parent's key is less than or equal to each child's key.

A **max-heap** reverses the inequalities. Neither version requires siblings, or separate subtrees, to be sorted against one another.

### Intuitive

A heap keeps **just enough order to expose the winner**. Follow any node's parents to the root: keys never increase. Therefore the root is no greater than that node. Since this argument works for every node, the root contains a minimum. The shape guarantee makes the route short; the order guarantee makes the answer correct.

| Familiar structure | What it promises | What a heap changes |
|---|---|---|
| FIFO queue | Earliest arrival leaves first | The priority key chooses the next departure |
| Binary search tree | Every left-subtree key is smaller; every right-subtree key is larger (with a duplicate policy) | Only parent–child comparisons matter |
| Sorted array | Every earlier key is no larger than every later key | Most pairwise relationships remain unknown |

### 中文锚点

游戏里，箭什么时候命中、护盾什么时候消失、下一只敌人什么时候出现，都在等着发生。程序每次只急着知道“下一件是什么”，没必要把所有事件反复排一遍。堆就抓住了这个需要：它不把全部顺序排好，只守住父与子之间的局部规矩，让最早的事件一定在顶端。加进或取走一件事，沿一条路径调整就行。少做一点暂时用不上的整理，反而能更快找到眼下真正需要的答案。

## Notation

| Symbol / operation | Meaning | Boundary |
|---|---|---|
| `a[i]` | Key at array index $i$ | Zero-based indices |
| `peek()` | Inspect the minimum | Does not remove it |
| `push(x)` | Insert $x$ | Also called insert |
| `pop()` | Remove and return a minimum | Also called extract-min |
| $n$ | Number of entries physically stored | May exceed live tasks with lazy deletion |
| $h$ | Height, counted in edges | One node has height 0 |

## Key Facts — the tree is arithmetic

### 1. No pointers are needed

Number the complete tree level by level, starting at zero. A node at index $i$ has children at

$$\boxed{\text{left}=2i+1,\qquad\text{right}=2i+2,\qquad\text{parent}=\left\lfloor\frac{i-1}{2}\right\rfloor.}$$

Why? Each preceding parent contributes two child positions. After the root's slot, parent $i$ owns the next pair after those $2i$ positions. Solving either child equation for its parent and rounding down gives the inverse formula. A child exists only when its index is below $n$; the root has **no parent**, so never apply the parent formula at $i=0$.

![[heap-array-tree.svg|700]]

The array `[2, 5, 3, 9, 7, 8, 4]` is a valid heap. Notice `5 > 3` and `8 > 4`: the array is not sorted. Nor is it a BST: the root's left child is greater than the root. The same values may have several valid heap arrangements.

A complete tree of height $h$ has at least $2^h$ and at most $2^{h+1}-1$ nodes. Thus $2^h\le n<2^{h+1}$, giving $h=\lfloor\log_2 n\rfloor$ for $n\ge1$. Its logarithmic height follows from its **shape**, without rotations or luck.

### 2. Insert: preserve the shape, repair upward

Append the new item to the array. This creates exactly the next permitted leaf. Every old edge is still valid; the only possible violation is between the new item and its parent.

If the child is smaller, swap them and repeat at the parent's index. Stop at the root or at a parent no larger than the moving item. This is **sift-up**.

Why does moving the parent downward not break the repaired branch? Before insertion, that parent was no larger than everything below it. The new item has travelled upward through that same branch; moving an old ancestor down restores a position above keys it already dominated. The only unresolved comparison moves upward with the new item.

### 3. Remove: fill the hole, repair downward

Save the root's value. Remove the **last** array entry and, if anything remains, put it at the root. Shape is now correct; each child subtree remains a heap. Only the replacement's downward relationships may be wrong.

Choose the **smaller child**. If that child is smaller than the replacement, swap and continue down its branch; otherwise stop. This is **sift-down**.

Why the smaller child? It must become no greater than **both** children after promotion. Choosing the larger child could leave its smaller sibling above the new parent in priority. Promoting the smaller child fixes the upper position; any remaining violation travels downward with the displaced key. Both repairs terminate because every swap crosses one level of a finite tree.

![[heap-sift-animation.mp4]]

Follow the same key in both representations. Insertion adds a leaf and moves `1` along indices `7 → 3 → 1 → 0`; removal then moves the final leaf to the root and repairs downward. The lines are index relationships, not separately stored pointers.

### 4. Costs — name the operation, not just the structure

| Implementation of a min-priority queue | Insert | Inspect minimum | Remove minimum |
|---|---|---|---|
| Unordered array | $O(1)$ append | $O(n)$ scan | $O(n)$ scan, then swap with last |
| Array sorted largest to smallest | $O(n)$ shifting | $O(1)$ at last slot | $O(1)$ at last slot |
| Binary min-heap | $O(\log n)$ sift | $O(1)$ at root | $O(\log n)$ sift |

These are worst-case **structural** costs with constant-time key comparisons and sufficient array capacity. For a Python dynamic list, append is amortised $O(1)$; an occasional resize can make an individual heap insertion $O(n)$ in elapsed work. List contraction can likewise add occasional copying on removal. The logarithmic bound describes heap comparisons and swaps; implementation/allocation costs must be named separately. Long strings or large integers can also make one comparison cost more than constant time.

An ordinary heap does **not** support finding an arbitrary key in $O(\log n)$. A target larger than the current node could lie in either subtree. A failed search can inspect all $n$ entries. If ordered search is the job, [[Balanced Trees]] offers a different bargain.

### 5. Build an entire heap: why the answer is linear

Repeated insertion works, with a worst-case $O(n\log n)$ bound. But if all items are already available, we can do better.

Leaves are already one-node heaps. The last parent is at `n//2 - 1`: its left child must satisfy $2i+1<n$. Work backwards from that parent to index 0, calling sift-down at each position. When a parent is processed, both child subtrees have already been repaired. Sift-down therefore makes the entire subtree rooted there a heap. Induction over the backwards loop finishes at the root.

**The tempting wrong count:** $n$ nodes times $\log n$ levels. That gives every leaf the root's travel budget, even though a leaf cannot move downward at all.

**Count the available downward steps instead.** A node can sink at least $k$ levels only if its leftmost descendant $k$ levels below exists. That descendant has index $2^k(i+1)-1$, so there are exactly $\lfloor n/2^k\rfloor$ possible starting nodes with that much height. Summing heights by counting the first step, second step, and so on gives

$$\sum_i \operatorname{height}(i)=\sum_{k\ge1}\left\lfloor\frac{n}{2^k}\right\rfloor < n\left(\frac12+\frac14+\frac18+\cdots\right)=n.$$

Each level costs at most two key comparisons: select the smaller child, then compare it with the parent. Even a terminating no-swap check consumes one of those available levels. Thus bottom-up heap construction uses fewer than $2n$ comparisons for nonempty heaps. Copying/visiting the input also costs linear time: **the complete build is $\Theta(n)$**. The logarithm has disappeared because most nodes are near the bottom.

## Runnable Python — build the mechanism

This implementation accepts mutually comparable keys and owns a copy of the input. The comparison counter measures key comparisons only. `valid()` is a diagnostic linear scan, not part of the fast operations.

```python
class MinHeap:
    def __init__(self, values=()):
        self.a = list(values)
        self.comparisons = 0
        for i in range(len(self.a) // 2 - 1, -1, -1):
            self._down(i)

    def __len__(self):
        return len(self.a)

    def _less(self, i, j):
        self.comparisons += 1
        return self.a[i] < self.a[j]

    def peek(self):
        if not self.a:
            raise IndexError('peek from empty heap')
        return self.a[0]

    def push(self, value):
        self.a.append(value)
        i = len(self.a) - 1
        while i > 0:
            p = (i - 1) // 2
            if not self._less(i, p):
                break
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i = p

    def _down(self, i):
        n = len(self.a)
        while 2 * i + 1 < n:
            child = 2 * i + 1
            if child + 1 < n and self._less(child + 1, child):
                child += 1
            if not self._less(child, i):
                break
            self.a[i], self.a[child] = self.a[child], self.a[i]
            i = child

    def pop(self):
        if not self.a:
            raise IndexError('pop from empty heap')
        answer = self.a[0]
        last = self.a.pop()
        if self.a:
            self.a[0] = last
            self._down(0)
        return answer

    def valid(self):
        return all(not self.a[i] < self.a[(i - 1) // 2]
                   for i in range(1, len(self.a)))

h = MinHeap([9, 2, 7, 1])
h.push(3)
assert h.valid()
assert [h.pop() for _ in range(len(h))] == [1, 2, 3, 7, 9]
```

`child + 1 < n` handles the lone-left-child case. `if self.a` after removing the last entry handles a one-element heap. The empty checks make underflow explicit. Duplicate values are allowed: an equal key need not move.

**Run the companion:** `python3 heaps-priority-queues.py`. It contains the same implementation, the event scheduler below with rescheduling/cancellation, and independent checks against sorted results and Python's library. No third-party package is required.

## Worked Examples

### 1. One new arrival, then one departure

Start with `[2, 5, 3, 9, 7, 8, 4]`; insert `1`, then remove the minimum.

1. **Trigger: one item arrives → tool: append to preserve completeness.** The array becomes `[2, 5, 3, 9, 7, 8, 4, 1]`.
2. **Trigger: the new leaf outranks its parent → tool: sift-up.** Index 7 compares with 3: swap `1` and `9`, giving `[2, 5, 3, 1, 7, 8, 4, 9]`. Then swap at indices 3 and 1: `[2, 1, 3, 5, 7, 8, 4, 9]`. Finally swap at 1 and 0: `[1, 2, 3, 5, 7, 8, 4, 9]`.
3. **Trigger: extract-min → tool: save root, replace with last.** Return `1`; the temporary array is `[9, 2, 3, 5, 7, 8, 4]`.
4. **Trigger: child subtrees are heaps, root may violate order → tool: sift-down.** Choose `2`, not `3`: `[2, 9, 3, 5, 7, 8, 4]`. Then choose `5`, not `7`: `[2, 5, 3, 9, 7, 8, 4]`. The moving `9` reaches a leaf. Both invariants hold.

The heap returns to its initial arrangement in this example; insertion followed by removal need not generally restore an identical arrangement when ties allow alternatives.

### 2. The counter is evidence, not a proof

**Trigger: compare construction methods → tool: count comparisons on identical data.** The companion builds descending inputs both ways:

| $n$ | Bottom-up build | Repeated insertion |
|---|---|---|
| 31 | 52 | 98 |
| 127 | 240 | 642 |
| 511 | 1004 | 3586 |
| 2047 | 4072 | 18434 |

Descending input forces each newly inserted minimum towards the root. Bottom-up work stays below $2n$; insertion work grows with the accumulated depths. These measurements illustrate the proved bounds. They do not establish a universal wall-clock speed ranking, which also depends on language, allocation and cache behaviour.

## Where this is the working tool — the game's future

A **discrete-event simulation** stores scheduled changes, then advances simulated time directly to the next event. It need not ask every object “anything happened yet?” at every empty tick. This is useful for combat simulations, factory models and network simulations. A real game's rendering/physics loop can still use frames; the event queue handles a particular scheduling job, not every part of an engine.

Here is a complete small example using the Python standard library:

```python
import heapq
from itertools import count

future = []
tickets = count()

def schedule(tick, description):
    heapq.heappush(future, (tick, next(tickets), description))

schedule(5, 'shield expires')
schedule(2, 'arrow hits')
schedule(5, 'enemy spawns')
while future:
    now, ticket, event = heapq.heappop(future)
    print(now, event)
    if event == 'arrow hits':
        schedule(now + 1, 'impact spark fades')
# 2 arrow hits
# 3 impact spark fades
# 5 shield expires
# 5 enemy spawns
```

**The tie is a design decision.** Tuples compare from left to right. An increasing ticket serves equal-time events in insertion order and prevents comparison from reaching arbitrary event payloads. It is a deterministic convention, not proof that this is the right physics: simultaneous events may need to be processed as a batch or assigned explicit phases. A heap by itself is not stable.

**Rescheduling is not an assignment into the old tuple.** Changing a key in place can break order. The companion `EventQueue` assigns each event ID a new ticket when scheduled and records the live ticket in a dictionary. On pop, it discards an entry whose ticket is obsolete. Schedule the arrow for tick 2, then replace it with tick 1: the old tick-2 entry remains physically present but is no longer a live event. The resulting trace is `1 arrow → 2 spark → 5 shield → 5 enemy`.

Cancellation deletes the live dictionary entry. `compact()` filters out obsolete entries and heapifies the survivors. The simulation rejects scheduling into its past. These are application rules built **around** the heap invariant.

With $m$ physical entries, each heap push/pop costs $O(\log m)$ structural work; one request for a live event may discard many stale entries, so it is **not** guaranteed $O(\log n)$ in the number of live tasks. Every obsolete entry is removed at most once, but memory and delay can grow until compaction. Rebuilding costs $O(m)$ and is a deliberate maintenance trade-off.

The same “serve the best frontier candidate” operation powers [[Graphs]]'s Dijkstra and A*: keys are tentative distance $g$, or estimate $g+h$. [[Parallel and External Sorting]] uses a heap of stream fronts; [[Compression]]'s Huffman construction repeatedly combines the two least frequent candidates. The structures share an operation even though their applications look unrelated.

## Try It — predict, then change the rules

1. Before running anything, trace inserting `0` into `[2, 5, 3, 9, 7, 8, 4]`. Name every compared pair, then check `valid()` and the popped order.
2. Change `_down` to choose the **larger** child. Find the smallest heap on which a removal now fails. Explain the broken parent–child edge before reading any test failure.
3. In the event scheduler, schedule two dictionaries at the same tick. Remove the ticket field in a scratch copy: why does comparison reach the payload? Decide whether equal-time combat events should use insertion order or a simultaneous batch.

> [!tip] Checks after your attempt
> The new `0` travels through indices `7 → 3 → 1 → 0`. For the wrong-child bug, start with `[1, 2, 3, 4]`: after removing `1`, promoting `3` produces `[3, 2, 4]`, which violates the root's left edge. With equal times and no ticket, Python tries to order the dictionaries and raises `TypeError`. A unique ticket resolves comparison; it cannot decide the simulation's rules for you.

## Special Cases and Common Misconceptions

- **“Priority queue means FIFO with an extra label.”** Test arrivals `(priority 5, A)` then `(priority 1, B)`. A min-priority queue serves B first. FIFO applies only if the chosen tie policy says so for equal priorities.
- **“The next-smallest value is at array index 1.”** In `[2, 5, 3, 9, 7, 8, 4]`, it is at index 2. Compare the root's children; do not assume the left side wins.
- **“Use binary search on the heap array.”** The array is not sorted. Try searching for `4` in that example and identify the missing sorted-order premise.
- **“Complete means every node has two children.”** The final parent may have only a left child. Draw six nodes, then apply the child-index guards.
- **“Minimum and highest priority contradict each other.”** A smaller timestamp is an earlier event. Decide the meaning of the key before choosing min-heap versus max-heap.
- **“Any numeric key is safe.”** NaN does not obey the ordinary total-order assumptions. Validate keys and avoid mixing incomparable types; our event scheduler accepts integer ticks.
- **“Heap means dynamic memory.”** The binary-heap data structure and a process's allocation heap are distinct uses of the word.

## Exam Notes

### Cambridge 9618 and 0478

**Binary heaps, heap construction and heapsort are enrichment, not named requirements** in the checked 9618 2027–29 and 0478 2026–28 syllabuses. 9618 §10.4 introduces stack/queue/linked-list ADTs; §19.1 adds algorithm construction, binary trees, graphs and complexity. A FIFO queue is not a heap-backed priority queue. Use [[Stacks and Queues]], [[Binary Trees]] and [[Graphs]] for those specified outcomes. 0478's arrays, algorithms and named searches/sorts do not add heaps as a prescribed structure.

### IB Computer Science — first assessment 2027

B2.2.3–4 explicitly name **stacks and FIFO queues**. HL B4.1 covers ADTs, linked lists, BSTs, sets and hashing, but does not prescribe binary heaps or priority-queue implementation. B2.4.1's complexity reasoning transfers to this example; that does not turn heap algorithms into a named requirement. Treat the implementation and proofs as enrichment.

### AP Computer Science A / Principles

Neither checked course framework prescribes binary heaps, priority-queue implementation or heapsort. AP CSA's Java arrays, `ArrayList`, searching/sorting and recursion are adjacent foundations; Python `heapq` is not its exam language. AP CSP's list abstraction and algorithm-efficiency work likewise do not require this data structure. An unfamiliar problem may explain a structure and ask students to reason about it; “not prescribed” does not prohibit such a scenario.

**Where it is not examined as required heap machinery:** Cambridge 0478/9618, IB CS 2027, AP CSA and AP CSP. The worked examples above are original enrichment examples, not attributed examination questions.

## Beyond Syllabus — ask less, maintain less

### Heapsort: use the winner repeatedly

Recall that removing a heap's root reveals the next winner after repair. Build a **max-heap**, swap its root with the final active element, shrink the active heap by one and sift-down. The removed maximum now sits in its final position at the right. Repeat: the sorted suffix grows leftward until the whole array is ascending.

Bottom-up build costs $O(n)$; at most $n-1$ removals each cost $O(\log n)$, giving worst-case $O(n\log n)$. Iterative in-place heapsort uses $O(1)$ auxiliary space and is not generally stable. Our `MinHeap` constructor copies its input, and repeatedly popping into a new output list also uses $O(n)$ storage: do not call that version in-place.

### Keep only the best $k$

Recall that a min-heap exposes its weakest retained candidate. To retain the largest $k>0$ scores from a stream, keep a min-heap of at most $k$ values. Fill it first; thereafter discard any score no greater than the root, otherwise replace the root and repair. Every discarded score has at least $k$ retained candidates no worse than it. Processing $n$ scores costs $O(n\log(k+1))$ time and $O(k)$ storage, without storing the entire stream. Add a tie policy if the identities of equal-scoring entries matter.

### Find the median while the data arrives

Maintain a max-heap of the lower half and a min-heap of the upper half. Keep every lower-half value no greater than every upper-half value, and sizes differing by at most one. Insert on the correct side and transfer a root if needed. The median is one root or the mean of the two roots. Each arrival needs logarithmic maintenance; reading the median needs constant time. Two partial orders answer a question that neither alone can answer.

### When priorities change constantly

Recall that a heap's arbitrary-item search can be linear. An **indexed heap** keeps an additional map `item_id → array index`; every swap updates both map entries. Then decrease-key finds the item directly and sifts it upward, in $O(\log n)$ structural time (assuming constant-time map access). Arbitrary deletion replaces the located item with the last entry and repairs upward or downward as needed. This trades more bookkeeping for avoiding the stale-entry pile. Lazy replacement and indexed heaps solve different engineering constraints; neither is a universal winner.

## Connections

- **Builds on:** [[Binary Trees]] — the shape; [[Stacks and Queues]] — an ADT's behaviour versus its implementation; [[Big-O Notation]] — count the work actually possible.
- **Motivated by:** [[Graphs]] — the efficient frontier behind Dijkstra and A*.
- **Teach together:** [[Parallel and External Sorting]] — merge many streams while keeping only their fronts in memory.
- **Applications:** [[Compression]] — repeated minimum-frequency selection; [[Operating Systems]] — scheduling policy versus the data structure that implements it.
- **Contrast:** [[Balanced Trees]] — preserve searchable order rather than only exposing an extremum; [[Hash Tables]] — the locator map in an indexed heap.
- **Thinking tool:** [[Forward Reading and Problem Discovery]] — follow what can have changed; repair only the newly broken relationship.

## Sources and Further Reading

- [Python `heapq` documentation](https://docs.python.org/3/library/heapq.html) — library API and version details; the examples above use min-heap operations available before Python 3.14. Native max-heap helpers were added in 3.14.
- [Princeton Algorithms — Priority Queues](https://algs4.cs.princeton.edu/24pq/) — an alternative one-based, max-heap presentation for comparison with the zero-based min-heap developed here.

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $\lfloor x\rfloor$ | `\lfloor x\rfloor` | greatest integer no larger than $x$ |
| $\Theta(n)$ | `\Theta(n)` | linear upper and lower growth bounds |
| $\sum_{k\ge1}\lfloor n/2^k\rfloor$ | `\sum_{k\ge1}\lfloor n/2^k\rfloor` | total available downward steps |
