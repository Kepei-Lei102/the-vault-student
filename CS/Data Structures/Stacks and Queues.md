---
chinese: 栈与队列 (zhàn yǔ duìliè)
prerequisites:
  - "[[Arrays]]"
  - "[[Compilers and Interpreters]]"
leads_to:
  - "[[Linked List]]"
  - "[[The Call Stack]]"
tags:
  - subject/computer-science
  - domain/data-structures
  - level/A-Level
  - curriculum/Cambridge-9618
  - syllabus/9618-10-4
  - syllabus/9618-19-1
  - type/deep
  - misconception/top-starts-at-zero
  - misconception/pop-erases-the-value
  - misconception/linear-queue-reuses-space
  - misconception/full-and-empty-look-alike
  - misconception/any-structure-would-do
---

# Stacks and Queues 栈与队列

> *Close twenty browser tabs, then reopen them — they come back in reverse order. Nobody wrote a "reverse the tabs" feature; the reversal falls out of the structure they were stored in. You have been using stacks and queues all your life: every Ctrl-Z, every Back button, every printer that serves the person who asked first. This card's promise is the demystifying one: a stack is an array and one integer; a queue is an array and two integers. Everything else — the guarantees, the exam questions, the bugs — grows from those pointers and the discipline they enforce.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| abstract data type (ADT) | 抽象数据类型 | a collection of data **plus the set of operations allowed on it** |
| stack | 栈 / 堆栈 | last in, first out — one open end |
| push / pop | 入栈（压栈）/ 出栈（弹栈） | add to the top / remove from the top |
| top pointer | 栈顶指针 | the one integer that *is* the stack's state |
| LIFO | 后进先出 | last in, first out |
| queue | 队列 | first in, first out — add at one end, remove at the other |
| enqueue / dequeue | 入队 / 出队 | join at the rear / leave from the front |
| front (head) / rear (tail) | 队头 / 队尾 | where items leave / where items join |
| FIFO | 先进先出 | first in, first out |
| circular queue | 循环队列 | the array bent into a ring so freed space is reused |
| overflow / underflow | 上溢 / 下溢 | pushing into a full structure / popping from an empty one |

## The problems, before the tools

A structure chosen before its problem is a superstition — so, first, the problems.

**The stack's problem is interruption.** Real work interrupts itself: reading a chapter you chase a footnote, mid-footnote you look up a definition — and when the definition is done you are back in the footnote, and when the footnote is done, back in the chapter. Nobody legislated that order; **nesting forces it**: the most recently interrupted thing is always the first you *can* resume, because everything newer had to finish first. Brackets inside brackets, functions calling functions, an undo history, your twenty tabs — wherever work nests, a last-in-first-out shape already exists *in the problem*. The stack doesn't impose LIFO; it **names** it.

**The queue's problem is mismatched speeds.** Two machines meet and one is faster: fingers versus the CPU, ten laptops versus one printer, a thousand requests versus one server. The surplus must wait somewhere — and if the waiting is to be *fair*, nobody overtaken and nothing starved, then departures must copy arrivals. First-in-first-out is what fairness looks like once you build it; the waiting line ran the world's bakeries for millennia before anyone coded one.

That is the hunter's reading of this whole bay: **these structures are discovered, not invented.** Each is the shape of an invariant already present in the world — the resume order that nesting fixes, the arrival order that fairness fixes — and the card's job is to make the shape visible enough that you recognise it inside the next problem you meet, before you write a line of code.

## What an ADT actually is

The syllabus definition is compact and worth memorising as-is: an **abstract data type is a collection of data together with a set of operations on that data**. The second half is the point. An array lets you touch any cell any time; an ADT deliberately *takes freedoms away* — the stack forbids everything except touching the top, the queue forbids everything except joining at the rear and leaving from the front — and in exchange for each freedom surrendered you receive a **guarantee**. Restrict access to one end and you are *guaranteed* reverse order out. Restrict to opposite ends and you are *guaranteed* arrival order out. The discipline is not a limitation of these structures; the discipline **is** the product.

"Abstract" means the promise is separate from the machinery: *what* the operations do is fixed, *how* is a private matter. This card implements both structures with arrays (the syllabus's named implementation), then **proves the abstraction by swapping engines** — the same contract kept by a built-in dynamic type, and by [[Linked List]]'s nodes after that. Same promises, different machinery, and the user can't tell.

## The stack — an array and one integer

![[stacks-queues-two-integers.svg|700]]

A stack is an array `Contents[0..Max-1]` plus one integer, `Top` — the index of the most recently added item. All the traffic happens at that one end: **push** to add, **pop** to remove, **LIFO** (last in, first out) as the resulting law. The plate pile in the canteen: new plates land on top, the next plate taken *is* the newest one there.

**The keystone detail: `Top` starts at −1, not 0.** `Top` holds the index of the current top item — so what value says "there is no top item"? Not 0: index 0 is a perfectly valid cell, and `Top = 0` must mean "one item, sitting in cell 0." The honest empty-marker is a value that *cannot* be a real index: **−1**. Push then becomes *increment, then store*; pop becomes *read, then decrement* — and the two motions are exact mirrors:

```python
class Stack:
    def __init__(self, max_size):
        self.contents = [None] * max_size   # the array
        self.max = max_size
        self.top = -1                       # the one integer

    def push(self, item):
        if self.top == self.max - 1:        # full? refuse: overflow
            return False
        self.top += 1                       # increment, then store
        self.contents[self.top] = item
        return True

    def pop(self):
        if self.top == -1:                  # empty? refuse: underflow
            return -1
        value = self.contents[self.top]     # read, then decrement
        self.top -= 1
        return value
```

Notice what pop does **not** do: it never erases `Contents[Top]`. The value stays in the array as a ghost; it is merely *unreachable*, because the only legal door is `Top` and `Top` has moved past it. The next push will overwrite it. The stack's entire state is one integer — which is why the exam can ask "state the value of `Top` after these operations" and mean it as a complete description.

## The queue — an array and two integers

A queue is an array plus **two** integers — the exam's own names are `HeadPointer` (the front: where items *leave*) and `TailPointer` (the rear: where items *join*), both starting at the empty-marker. One pointer per door: **enqueue** at the tail, **dequeue** at the head, **FIFO** (first in, first out) as the law. The canteen line itself, this time: you join at the back, you are served from the front, and *nobody overtakes* — that no-overtaking promise is precisely what the structure sells.

The two disciplines differ by exactly one decision — *which end do removals use?* Same end as additions: stack. Opposite end: queue. Everything downstream (reversal vs preservation of order, undo vs fairness) follows from that single choice.

## The bug every linear queue has — and the ring that fixes it

Run the plain array queue for a while: enqueue, dequeue, enqueue, dequeue. Every enqueue moves `TailPointer` right; every dequeue moves `HeadPointer` right; **neither ever moves left**. The queue — even one holding two items — *walks up the array* like an inchworm, leaving a wasteland of dequeued ghost-cells behind it, until `TailPointer` hits the end wall. Now the queue is **"full" and nearly empty at the same time**: no room to join, almost nothing in it, and a desert of reusable space the pointers can never revisit.

![[stacks-queues-circular.mp4]]

The fix is not to shuffle every item down one cell per dequeue (correct, but every customer shuffling forward on every serve is O(n) work for nothing). The fix is geometric: **bend the array into a ring.** When a pointer steps past the last cell, wrap it back to cell 0 — one `MOD` does it:

```text
TailPointer ← (TailPointer + 1) MOD Max
```

This is the **circular queue**, and the wrap creates one famous new problem: if the ring can fill completely, then *"full" and "empty" look identical* — in both, `HeadPointer` and `TailPointer` collide. The standard exam fix is honest bookkeeping: keep a third variable, `NumberInQueue`, incremented on enqueue and decremented on dequeue; empty is `NumberInQueue = 0`, full is `NumberInQueue = Max`. (The alternative — sacrifice one slot and call the ring full at `Max − 1` — trades a cell for a variable; real systems use both conventions.)

```python
class CircularQueue:
    def __init__(self, max_size):
        self.contents = [None] * max_size
        self.max = max_size
        self.head = 0                    # HeadPointer: where items leave
        self.tail = -1                   # TailPointer: where items join
        self.count = 0                   # the tie-breaker

    def enqueue(self, item):
        if self.count == self.max:       # overflow
            return False
        self.tail = (self.tail + 1) % self.max
        self.contents[self.tail] = item
        self.count += 1
        return True

    def dequeue(self):
        if self.count == 0:              # underflow
            return -1
        value = self.contents[self.head]
        self.head = (self.head + 1) % self.max
        self.count -= 1
        return value
```

## Overflow and underflow — not edge cases, *the* questions

Every operation above opens with a refusal check, and this is where the marks live. **Overflow**: adding to a full structure. **Underflow**: removing from an empty one. A trace question will steer you into one of them deliberately; a write-the-pseudocode question awards its first marks for the two `IF` guards before any pointer moves. Treat the checks not as decoration but as the operation's first half: *a push is a question ("is there room?") followed by an action; a pop is a question ("is there anything?") followed by an action.*

One subtlety the best students catch: `Pop` and `Dequeue` above signal "empty" by returning **−1** — a value *inside* the data's own type. That only works because the scenario promised the stored data was positive; the sentinel lives **in-band**, and if −1 were ever legal data the signal would be a lie. The cleaner design returns a BOOLEAN success flag and passes the value out by reference — which is why exam signatures vary, and why you must *read the promise the question makes about its data* before choosing how to report failure. ([[Compilers and Interpreters]] met the same idea from the other side: a design is only safe relative to a stated contract.)

## Proof of the "A" — same promise, different machinery

If "abstract" means the promise is separate from the engine, the honest way to *show* it is to swap the engine and watch nothing break. Here is the same `Stack` contract kept by a completely different implementation — no array, no `max`, no `top`:

```python
class Stack:                        # same promise, different engine
    def __init__(self):
        self.items = []             # Python's own list does the storage

    def push(self, item):
        self.items.append(item)
        return True                 # this engine grows: never full

    def pop(self):
        if not self.items:
            return -1
        return self.items.pop()
```

Any code that used the array version runs unchanged on this one — push in, pop out, LIFO holds. That *interchangeability* is what the "abstract" in ADT means: the user of the structure cannot tell, and must not need to know, which machinery is inside. Three engines, one promise: the **array + pointer** (the syllabus's named implementation, fixed-size, overflow a real event), a **built-in dynamic type** (this one — the freedoms differ at the edges: it never overflows, because the engine reallocates), and **linked nodes** ([[Linked List]] rebuilds both structures that way — no fixed size, no walking bug, no `MOD`, one pointer chase per operation). This is also §19.1d's actual sentence — *ADTs built from built-in types or other ADTs* — worn as a demonstration instead of a definition.

## Which one? — reading the situation

§10.4's favourite verb is **justify**: here is a scenario, choose the structure and defend it. The invariant question that decides it: **does the situation care about *recency* or about *arrival order*?** — which is the opening section's pair of problems asked as a diagnostic: *is this scenario's shape nesting, or waiting?*

| the situation rewards… | structure | canonical examples |
|---|---|---|
| the most recent thing first (recency) | **stack** | undo (Ctrl-Z), the Back button, reversing a sequence, matched brackets `([{}])`, backtracking out of a maze |
| first come, first served (fairness) | **queue** | print jobs, the keyboard buffer, simulation of any waiting line, requests to a server, breadth-first exploration |

The justification pattern that scores: name the discipline (LIFO/FIFO), tie it to the scenario's need in one sentence, and — for the third mark — say what the *other* structure would do wrong ("a stack would print the most recently submitted document first, starving early jobs").

## Where you have already met both

- **The stack's second citizenship** is the most important object in computing you've never directly seen: **the call stack**. Every running program keeps its function calls on a stack — [[Recursion]] traces `factorial(4)`'s frames pushing and popping, [[Compilers and Interpreters]] evaluates RPN by pushing operands and popping pairs, and *stack overflow* names exactly this card's overflow happening to a program's own machinery. [[The Call Stack]] carries the full story: frames, return addresses, why recursion physically works.
- **The queue's second citizenship** is [[Operating Systems]]: the scheduler's **ready queue** (First-Come-First-Served is literally this card's discipline as government policy), the printer's **spool queue**, the **keyboard buffer** — a circular queue in the wild, quietly wrapping while you type ahead of a busy machine.

## Worked examples — every tool named

### Example 1 (AS — use the structure)

> An empty stack has `Max = 5`. State the value of `Top` and the stack contents after: Push(8), Push(3), Push(5), Pop(), Push(9), Pop(), Pop().

*Tool: `Top` starts at −1; push = increment-then-store; pop = read-then-decrement.*

| operation | Top after | contents (bottom → top) |
|---|---|---|
| — | −1 | *empty* |
| Push(8) | 0 | 8 |
| Push(3) | 1 | 8, 3 |
| Push(5) | 2 | 8, 3, 5 |
| Pop() → 5 | 1 | 8, 3 |
| Push(9) | 2 | 8, 3, 9 |
| Pop() → 9 | 1 | 8, 3 |
| Pop() → 3 | 0 | 8 |

Final answer: `Top = 0`, one item (8). *(And cell 1 still physically holds a ghost 3 — unreachable, waiting to be overwritten.)*

### Example 2 (A2 §19.1c — write the algorithm)

> A stack of positive integers is stored in `Contents[0..19]` with `Top` marking the top item (−1 when empty). Write a function `Pop()` that returns the top item, or −1 if the stack is empty.

*Tool: the question before the action — underflow guard first.*

```python
def pop(self):
    if self.top == -1:
        return -1
    value = self.contents[self.top]
    self.top -= 1
    return value
```

*Tool: read the data's promise.* Returning −1 is only a valid empty-signal because the stem says **positive** integers — quote that promise in any explain-your-design part. (On the paper itself you'd write this in the exam's own dialect — [[Cambridge Pseudocode]] holds the translation table; the *logic*, guard-then-move, is identical symbol for symbol.)

### Example 3 (A2 — the circular trace)

> A circular queue uses `Contents[0..3]` (`Max = 4`), with `HeadPointer = 2`, `TailPointer = 3`, `NumberInQueue = 2`. Trace: Enqueue(7), Enqueue(4), Dequeue(), Enqueue(6), and state all three variables after.

*Tool: pointers move by `(p + 1) MOD 4`; the count is the only truth about full/empty.*
Enqueue(7): Tail ← (3+1) MOD 4 = **0**, store 7, count 3. Enqueue(4): Tail ← 1, store 4, count 4 — **now full**. Dequeue(): read `Contents[2]`, Head ← 3, count 3. Enqueue(6): Tail ← (1+1) MOD 4 = 2, store 6, count 4.
Final: `HeadPointer = 3`, `TailPointer = 2`, `NumberInQueue = 4` — the tail has lapped the head, and only the count knows the ring is full.

## Common Misconceptions (Teaching Notes)

### 1. "`Top` starts at 0"

Then what does `Top = 0` mean — empty, or one item in cell 0? It must mean the latter, because 0 is a real index. **Fix:** the empty-marker must be an *impossible* index: −1. Rehearse the mirror: push = increment **then** store; pop = read **then** decrement.

### 2. "Pop removes the value from the array"

Pop moves a pointer; the value stays as an unreachable ghost until overwritten. **Fix:** the structure's state *is* the pointer(s). A trace answer that shows the popped cell "emptied" claims machinery the pseudocode doesn't have.

### 3. "When an item leaves a linear queue, the space is reused"

Not without help — both pointers only move right, so dequeued cells are abandoned and the queue inchworms into the end wall. **Fix:** show the walking-queue trace once (full *and* nearly empty simultaneously); the circular fix then feels necessary rather than clever.

### 4. "In a circular queue, `HeadPointer = TailPointer` means empty"

It can equally mean **full** — the collision looks identical from the pointers alone. **Fix:** the count variable (or the sacrificed slot) exists precisely to break this tie; any full/empty test written on the pointers alone is wrong.

### 5. "Stack or queue — either would work here"

Then reversal-vs-order doesn't matter in the scenario, which is almost never true. **Fix:** ask the invariant question — recency or arrival order? — and state what the wrong choice would *do* (print the newest job first; undo the oldest edit). The structures aren't containers; they are **promises**, and the scenario tells you which promise is being bought.

## Exam Notes

### Cambridge 9618 — §10.4 (AS)

- The ADT definition verbatim: *a collection of data and a set of operations on those data*; stack, queue and linked list are the three named examples. **Describe key features and justify the choice for a scenario** (the recency-vs-arrival table is the answer bank); **use** the structures — add, edit, delete data in given diagrams/traces (Example 1's shape); **describe the array implementation** (this card's pointers-and-array pictures). The AS promise, stated in the syllabus: *candidates will not be required to write pseudocode for these structures* — describing and tracing suffice.
- Trace questions are pointer-bookkeeping: state `Top` / `HeadPointer` / `TailPointer` values, not just contents. The mark scheme's variable names are the ones used here.

### Cambridge 9618 — §19.1 (A2)

- The AS promise expires: §19.1c requires **writing** the algorithms — insert (push/enqueue) and delete (pop/dequeue) for stack and queue, with the overflow/underflow guards carrying early marks (Examples 2–3 are the examined shape; recent Paper 4s have asked for `Enqueue` against a given signature, judged mark-point by mark-point). §19.1d asks how these ADTs are **built from built-in types or other ADTs** — the array implementations here, the built-in-list engine of the abstraction-proof section, the linked-list implementations in [[Linked List]], and the two-stacks queue in Beyond.
- **On dialect:** Paper 2/3 answers are written in Cambridge's strict-grammar pseudocode; this card — like the whole vault — writes real, runnable Python, because the logic is the knowledge and the dialect is a formality. [[Cambridge Pseudocode]] is the one card that owns the exam dialect (keywords, `←`, `ENDFUNCTION`, declaration forms); translate at the exam door.
- The circular queue is main-line A2 material: the `MOD` wrap, and the full-vs-empty disambiguation via a count.

### Other boards

- **AP CSA:** stacks and queues are not in the exam's Java subset (lists and 2-D arrays are its ceiling) — this card is depth behind its recursion unit's call-stack reasoning.
- **IB CS:** named stack/queue objects were examined under the legacy HL syllabus's abstract-data-structures topic; in the 2027 outline they sit inside the programming themes rather than as named statements — treat this card as depth behind that strand.

## Beyond the syllabus

> [!info] Building one from the other — §19.1d's favourite party trick
> A queue can be built from **two stacks**: enqueue by pushing onto stack A; dequeue by popping everything from A onto B (reversing it), popping B's top, and pouring back — or, in the efficient version, only re-pouring when B runs dry. Each item crosses at most twice, so the *average* dequeue is still O(1). The trick generalises the card's real lesson: an ADT is a promise, and promises can be kept by unexpected machinery. (Interviewers have been asking this one for decades.)

> [!info] The wider family
> Loosen one rule and the family grows: a **deque** (double-ended queue) opens both doors both ways; a **priority queue** serves not the earliest arrival but the most urgent one — the structure behind [[Operating Systems]]' priority scheduling, hospital triage, and Dijkstra's algorithm, usually implemented as a *heap*, a structure [[Binary Trees]] is the gateway to.

> [!info] Ring buffers run the real world
> The circular queue's grown-up name is the **ring buffer**, and it is everywhere hardware meets software at mismatched speeds: the keyboard buffer, network cards handing packets to the CPU, audio pipelines feeding a sound chip that must *never* starve. The reason is the card's own arithmetic: fixed memory, O(1) at both ends, no shuffling — the only queue you can safely service inside an interrupt handler ([[Interrupt Handling]]).

## Connections

- **Builds on:** [[Arrays]] — the raw material both implementations discipline; the pointers are array indices.
- **Leads to:** [[Linked List]] — the same promises rebuilt on nodes and pointers, freeing them from fixed size (and §10.4's third named ADT); [[The Call Stack]] — the machine's own stack: frames, return addresses, recursion made physical, stack overflow as a lived error.
- **Kindred:** [[Recursion]] — its `factorial(4)` trace is this card's stack discipline running a program; [[Compilers and Interpreters]] — RPN evaluation is pure push-pop choreography; [[Operating Systems]] — the ready queue, the print spool, and the keyboard's ring buffer; [[Big-O Notation]] — every operation here is O(1), which is the whole engineering point.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $O(1)$ | `O(1)` | constant time — push, pop, enqueue, dequeue all qualify |
| $O(n)$ | `O(n)` | the cost of the naive shuffle-forward queue the ring avoids |
