---
chinese: 链表 (liànbiǎo)
prerequisites:
  - "[[Arrays]]"
  - "[[Stacks and Queues]]"
leads_to:
  - "[[Binary Trees]]"
tags:
  - subject/computer-science
  - domain/data-structures
  - level/A-Level
  - curriculum/Cambridge-9618
  - syllabus/9618-10-4
  - syllabus/9618-19-1
  - type/deep
  - misconception/nodes-sit-together-in-memory
  - misconception/delete-erases-the-node
  - misconception/lists-allow-jumping-to-item-i
  - misconception/null-means-error
  - misconception/linked-beats-array-always
---

# Linked List 链表

> *Keep a sorted array of a million names and insert one that belongs in the middle: a million-item shuffle, every later name copied one cell to the right, to make room for one. Now ask the hunter's question — **what actually needed to change?** Not a single name moved in the alphabet. Only one fact changed: who comes after whom. The array was paying a million moves because it stores order and location as the same thing, and they are not the same thing. The linked list is what you get when you stop conflating them — and to build it, you have to dig one level closer to what memory really is.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| linked list | 链表 | items chained by pointers — order without adjacency |
| node | 节点 | one link of the chain: the data plus the address of the next |
| pointer | 指针 | an address stored as a value — a *name for a place* |
| null pointer | 空指针 | the deliberate "nowhere" that ends the chain |
| head pointer | 头指针 | the one address from which the whole list is reachable |
| traverse | 遍历 | walk the chain, one `next` at a time |
| insert / delete | 插入 / 删除 | rewire pointers — two writes / one write |
| free list | 空闲链表 | the empty cells, themselves chained into a list |
| singly / doubly linked | 单向链表 / 双向链表 | one pointer per node / forward-and-back pointers |

## The problem, before the tool

Tools earn their existence by the problems they kill, so start with the problem. An ordered collection that *changes* — a waiting list taking new arrivals, a dictionary absorbing new words, an index of anything that grows. Store it in an array and every mid-list insertion pays the shuffle: everything after the new item copies one cell rightward, O(n) work to record one fact. Deletion pays the same shuffle in reverse, closing the hole.

The hunter reads the failure forwards, tracing the cause. When D is inserted between C and E, what *is* the new fact? Only this: **C's successor is now D, and D's successor is E.** Two relationships. The other 999,998 names have exactly the same successors they had before — yet the array moved them all. Why? Because an array encodes "B comes after A" as "B sits *physically next to* A" — it stores **order** as **location**. Conflate two facts and you pay for changes to one with rewrites of the other. The fix, as always once the invariant is seen, is to *separate what changed from what didn't*: let every item say, explicitly, who comes next — and then location can stop mattering entirely.

## One level closer to the truth — what memory really is

To let items "say who comes next," look at what memory actually offers. [[RAM and the Memory Hierarchy]] tells the truth of it: RAM is not rows and columns of neat boxes — it is one **flat sea of numbered cells**, every cell reachable by its number in the same time as any other. The tidy array was always a *convention* laid over that sea: "element $i$ lives at $\text{base} + i \times \text{size}$" — a formula, not a fact about the hardware. Convenient, but it is exactly the convention that welded order to location.

The honest primitive underneath is the **address**: every cell has a number, and a number can be *stored in another cell*. An address kept as data is called a **pointer**, and it is one of the most consequential ideas in computing — a value that names a *place* rather than a thing. The moment you can store "where the next one lives," order no longer needs adjacency. The chain can wander the sea.

## The node and the chain

A **node** is a small record holding two things: the **data**, and a pointer to the **next** node. A **head pointer** holds the address of the first node; the last node's `next` holds the **null pointer** — a deliberate, reserved "nowhere" that means *the chain ends here* (Python spells it `None`; the exam's array form spells it −1, and [[Stacks and Queues]]' keystone argument is the same one: the end-marker must be a value that cannot be a real address).

![[linked-list-two-truths.svg|700]]

Hold both panels of that picture at once, because the card lives in the gap between them. The *logical* list — head to A to B to C to nowhere — is the story the pointers tell. The *physical* nodes are scattered wherever there happened to be room. **Order lives in the pointers now, not in the geography** — which is precisely why changing the order will no longer require moving anything.

In Python, honestly:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None          # None: the deliberate nowhere

class LinkedList:
    def __init__(self):
        self.head = None          # empty list: the head points nowhere

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next   # one hop along the chain
```

Traversal is the price of the scattered life: to reach the fifth item you must walk through four `next` pointers — there is no formula that jumps to item $i$, because location was the thing we gave up. **A linked list trades random access for cheap change.** Whether that trade is right is a question the situation answers, never the structure alone.

## The operations — two writes, one write

### Insert: two pointer writes

To insert D between C and E: point D at E, then point C at D. Two assignments. The million other items are untouched *because nothing about them changed* — the structure now pays exactly in proportion to the facts being recorded. Watch it, then watch the array pay its old price for the same fact:

![[linked-list-insert.mp4]]

The **order discipline** carries real marks: **the new node grips the chain before the chain is broken.** Set `new.next = prev.next` *first*, `prev.next = new` *second*. Reverse them and `prev.next` is overwritten before anyone recorded where it pointed — the entire tail of the list is orphaned in the sea, unreachable, gone. The clip above makes the mistake on purpose so you never have to: watch the tail drift away the moment C lets go too early. (One pointer is the only thread to everything downstream of it; the hunter treats every pointer overwrite as the question *"is anyone still holding the old value?"*)

```python
def insert(self, value):                  # keep an ordered list ordered
    new = Node(value)
    if self.head is None or self.head.data >= value:
        new.next = self.head              # grip first...
        self.head = new                   # ...then relink
        return
    prev = self.head
    while prev.next is not None and prev.next.data < value:
        prev = prev.next                  # walk to the insertion point
    new.next = prev.next                  # grip first...
    prev.next = new                       # ...then relink
```

### Delete: one pointer write

To delete B, no one needs to touch B: point B's *predecessor* past it — `prev.next = prev.next.next`. One write. B still sits in memory holding its data and its pointer, but nothing points to it anymore: it has become **unreachable** — the same ghost [[Stacks and Queues]]' popped values became. *Unlinked is not erased*; it is removed from the story, not from the sea.

```python
def delete(self, value):
    if self.head is None:
        return False
    if self.head.data == value:
        self.head = self.head.next        # unlink the first node
        return True
    prev = self.head
    while prev.next is not None and prev.next.data != value:
        prev = prev.next
    if prev.next is None:
        return False                      # not found: report honestly
    prev.next = prev.next.next            # one write; the node is a ghost
    return True
```

## The exam's engine — arrays underneath, and the free list

9618's named implementation builds the linked list *out of arrays* — and it is worth doing not as an exam chore but as a truth-dig: it makes **allocation** visible. Two parallel arrays, `data[]` and `next[]`, where "pointer" means *index into the same arrays*, −1 means null, and — the beautiful part — **the empty cells are themselves chained into a linked list**, the **free list**:

```python
class ArrayLinkedList:                    # the exam's implementation
    def __init__(self, size):
        self.data = [None] * size
        self.next = list(range(1, size)) + [-1]   # every cell chained...
        self.head = -1                    # the list: empty
        self.free = 0                     # ...into the free list: all cells

    def push_front(self, value):
        if self.free == -1:
            return False                  # no cells left: the sea is full
        cell = self.free                  # allocate = POP the free list
        self.free = self.next[cell]
        self.data[cell] = value
        self.next[cell] = self.head       # grip first...
        self.head = cell                  # ...then relink
        return True

    def delete_front(self):
        if self.head == -1:
            return None
        cell = self.head
        self.head = self.next[cell]       # unlink from the live list
        self.next[cell] = self.free       # deallocate = PUSH onto the free list
        self.free = cell
        return self.data[cell]
```

Look at what allocation turned out to be: **taking a cell from the free list is a pop; returning one is a push — the free list is a stack, built out of the very structure it supplies cells to.** The allocator is made of the thing it allocates. This is not an exam curiosity: real memory allocators — the machinery under `malloc`, under Python's object heaps, inside [[Operating Systems]]' memory management — run on free lists at their core. The A-Level's toy is the industry's engine, undersized but honest.

## The promises, kept by the third engine

[[Stacks and Queues]] proved the "A" in ADT by swapping engines; the linked list is the engine that frees both structures from the array's walls. A **stack** on a linked list is push-at-head and pop-at-head — two of the operations above, O(1), and *overflow stops existing* (the structure grows until memory itself runs out). A **queue** keeps a head pointer *and* a tail pointer — enqueue at the tail, dequeue at the head, O(1) both, and the walking-queue bug never happens because there is no wall to walk into and no `MOD` to wrap: the inchworm problem was an artifact of living in a fixed corridor, and the corridor is gone. Same promises, third machinery, and the user of the ADT — as ever — cannot tell.

## The honest price — and the modern twist

*Tool: no structure is free; find where each one pays.*

| | **array** | **linked list** |
|---|---|---|
| reach item $i$ | O(1) — one formula | O(n) — walk the chain |
| insert / delete mid-list | O(n) — the shuffle | O(1) — two writes / one write *(once you're there)* |
| size | fixed at creation | grows and shrinks freely |
| memory per item | the data alone | the data **plus a pointer** |
| where items live | contiguous — order *is* location | scattered — order is *stored* |

And one price the table hides, because it is a fact about modern hardware rather than about the abstraction: [[RAM and the Memory Hierarchy]]'s caches reward *contiguity*. An array scan streams through cache lines; a chain walk hops across the sea, and every hop risks a cache miss costing hundreds of cycles. This is why the "lists" of working languages — Python's `list`, Java's `ArrayList` — are dynamic *arrays* underneath, and why systems programmers reach for linked lists more rarely than the textbooks of 1985 did. The abstraction's truth didn't change; the machine under it did. A hunter keeps both layers in view: the linked list *teaches* pointer-craft that trees, graphs and allocators are built from, even where a smarter array wins the benchmark.

## Worked examples — every tool named

### Example 1 (AS — read the engine)

> A linked list of characters is stored with `head = 3` and the two arrays below. List the items in order.

| index | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| `data` | R | E | A | H | T |
| `next` | −1 | 4 | 0 | 1 | 2 |

*Tool: start at the head; follow `next` until −1.*
`head = 3` → H. `next[3] = 1` → E. `next[1] = 4` → T. `next[4] = 2` → A. `next[2] = 0` → R. `next[0] = −1`: stop. The list reads **H, E, T, A, R** — and notice the indices wandered 3 → 1 → 4 → 2 → 0: the order and the geography agree nowhere, and the list doesn't care.

### Example 2 (A2 §19.1c — write the algorithm)

> Write a method to insert a value into an ordered linked list so it remains ordered.

*Tool: walk with a trailing pointer; grip before relinking.* The `insert` method above is the full answer: the `prev` walk stops at the last node smaller than the new value; then the two writes in the only safe order — `new.next` takes the chain before `prev.next` lets it go. (Exam-dialect version at [[Cambridge Pseudocode]]; the guard order and the two writes are the marks either way.)

### Example 3 (A2 — the free list, traced)

> Using `ArrayLinkedList` with `size = 4`, trace: `push_front('B')`, `push_front('A')`, `delete_front()`, and state `head`, `free`, and both arrays after.

*Tool: allocate = pop the free list; deallocate = push it back.*
Start: `head = −1`, `free = 0`, `next = [1, 2, 3, −1]`.
`push_front('B')`: cell 0 allocated (`free ← 1`), `data[0] = 'B'`, `next[0] = −1`, `head = 0`.
`push_front('A')`: cell 1 allocated (`free ← 2`), `data[1] = 'A'`, `next[1] = 0`, `head = 1`.
`delete_front()`: returns 'A' — `head ← next[1] = 0`, and cell 1 goes back: `next[1] = 2`, `free = 1`.
Final: `head = 0`, `free = 1`, `data = ['B', 'A', None, None]`, `next = [−1, 2, 3, −1]` — and the ghost 'A' still sits in `data[1]`, unreachable from `head`, first in line to be overwritten.

## Common Misconceptions (Teaching Notes)

### 1. "The nodes sit next to each other in memory"

They sit wherever allocation found room — the chain's whole point is that they don't have to be anywhere in particular. **Fix:** the two-truths picture; Example 1's wandering indices (3 → 1 → 4 → 2 → 0). If the nodes had to be adjacent, insertion would still pay the shuffle and the structure would be pointless.

### 2. "Deleting a node erases it"

Deletion is *unlinking* — one pointer write on the predecessor. The node remains in memory as an unreachable ghost until reused. **Fix:** Example 3's final state, ghost included; the same lesson as pop's ghost in [[Stacks and Queues]] — the structure's state is its pointers, not its cells.

### 3. "Get me item number 5"

There is no item number 5 — there is only *the item after the item after…* Random access is the thing the linked list traded away. **Fix:** the trade table; ask "how would you *find* cell number 5 when the cells are scattered?" — the only map is the chain itself.

### 4. "A null pointer is an error"

Null in the `next` field is the *design* — the deliberate end-of-chain marker, exactly as −1 was the stack's deliberate empty-marker. (Dereferencing null — *walking past* the end — is the error.) **Fix:** every traversal's loop condition is literally "while not null": the marker is what makes stopping possible.

### 5. "Linked lists are just better than arrays"

They buy cheap change with random access, pointer overhead, and (on modern hardware) cache locality. **Fix:** the trade table plus the modern twist — and the justify-the-choice discipline from [[Stacks and Queues]]: name what the scenario *does most often*. Frequent mid-list change, unknown size → list. Frequent lookup by position, tight memory, scan-heavy work → array.

## Exam Notes

### Cambridge 9618 — §10.4 (AS)

- The linked list completes §10.4's named trio (stack, queue, linked list): **describe key features** (nodes, pointers, head, null terminator), **justify** for a scenario (the trade table — cheap insertion/deletion and free growth vs no direct access), **use** the structure (add, edit, delete on given diagrams — Examples 1 and 3's shape), and **describe the array implementation** — `data[]`/`next[]`, −1 as null, and the **free list** threading the empty cells. Trace questions expect `head`, `free`, and both arrays tracked per operation.

### Cambridge 9618 — §19.1 (A2)

- §19.1c: **write** the algorithms — find an item (the `while` walk), insert, delete — with the pointer-order discipline (grip before relinking) and the not-found/empty guards carrying marks. §19.1d: the linked list **built from arrays** (the free-list engine above) *and* serving as the machinery other ADTs are built from — the stack and queue of "The promises, kept by the third engine," and [[Binary Trees]] next.
- **On dialect:** the paper speaks Cambridge's strict-grammar pseudocode; this card, like the vault, writes real Python — the logic is identical, and [[Cambridge Pseudocode]] owns the translation table.

### Other boards

- **AP CSA:** linked lists are not in the Java subset — but *reference semantics* (two variables holding the same object) are, and this card's grip-before-relinking reasoning is the cleanest place to learn them.
- **IB CS:** linked lists were named objects of the legacy HL syllabus's abstract-data-structures topic; in the 2027 outline they sit inside the programming themes rather than as named statements — depth behind that strand.

## Beyond the syllabus

> [!info] Give a node a second pointer
> The whole next chapter of data structures is one sentence away: a node with **two** `next` pointers — call them `left` and `right` — is no longer a chain but a fork, and a structure of forks is a **tree**. [[Binary Trees]] takes that one extra pointer and buys back the thing this card traded away: O(log n) search *through* pointer-machinery, order without geography *and* without the O(n) walk. Then a node with *any number* of pointers is a graph, and the map of structures is complete: array → list → tree → graph, each one loosening the previous one's constraint.

> [!info] Doubly linked, circular — and the OS's favourite shape
> Give each node a `prev` as well as a `next` and you can walk both ways and delete a node given only *itself* (no predecessor hunt): the **doubly linked list**. Bend the last node's pointer back to the first and there is no null at all: the **circular list** — the natural shape for anything served in rotation, which is why [[Operating Systems]]' round-robin scheduler runs its processes on exactly this structure. The Linux kernel's most-used data structure is a circular doubly-linked list; the toy in this card is holding up the machine you're reading it on.

> [!info] The free list all the way down
> The `malloc` under C, the object allocators under Python and Java, the page-frame managers inside operating systems — at the bottom of each sits some elaborated cousin of Example 3's free list: freed memory chained through itself, allocation popping, liberation pushing. When memory "leaks," it means a program lost every pointer to a node without returning it to the free list — the ghost problem at industrial scale. The hunter's pointer-overwrite question ("is anyone still holding the old value?") is, in reverse, the question every garbage collector exists to answer.

> [!info] The engineer's dream — can't we have both?
> Recall the trade table: the array reaches in O(1), the list changes in O(1), and each pays for its gift with the other's price. The obvious wish is a hybrid where *both* are O(1) — and on those exact terms the wish is provably unbuyable: a structure that allows insert-anywhere lets every later item's position number shift, and keeping "where is item $i$?" instantly answerable while the numbering keeps sliding is the very O(n) bookkeeping the list escaped. (That this is a hard *theorem*, not a failure of imagination, was proved in 1989.) The best any structure does at both jobs is O(log n)-ish: a balanced [[Binary Trees|binary tree]] that stores subtree counts, or a **skip list** — a linked list wearing express lanes over express lanes, the engine inside Redis. But there is one hunter's move left: *change what "reach" means.* Give up reach-by-position and ask for reach-by-**key**, and a [[Hash Tables|hash table]] welded to a linked list delivers O(1) lookup *and* O(1) ordered insertion and deletion simultaneously. That welded hybrid is not exotic — it is Python's `dict` (insertion-ordered by design since 3.7) and Java's `LinkedHashMap`. You cannot beat the trade on its own terms; you can renegotiate the terms.

## Connections

- **Builds on:** [[Arrays]] — the contiguous convention this card un-welds, and the raw material of the exam's `data[]`/`next[]` engine; [[Stacks and Queues]] — the bay's opener: the ADT-as-promise thesis, the ghost lesson, and the −1 keystone this card's null continues.
- **Leads to:** [[Binary Trees]] — one more pointer per node and the chain forks; search comes back at O(log n).
- **Kindred:** [[RAM and the Memory Hierarchy]] — the flat sea of cells this card finally uses honestly, and the cache hierarchy that gives arrays their modern revenge; [[Operating Systems]] — free lists in the allocator, circular doubly-linked lists in the scheduler; [[Recursion]] — a linked list is a recursively defined object (a list is a node whose `next` is a list), and recursive traversals fall out of that definition.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $O(1)$ | `O(1)` | insert/delete once positioned — the structure's purchase |
| $O(n)$ | `O(n)` | the traversal walk — the structure's price |
| $O(\log n)$ | `O(\log n)` | what [[Binary Trees]] buys back with one more pointer |
