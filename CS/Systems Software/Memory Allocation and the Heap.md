---
chinese: 内存分配与堆 (nèicún fēnpèi yǔ duī)
prerequisites:
  - "[[Recursion]]"
  - "[[Linked List]]"
  - "[[Arrays]]"
  - "[[Operating Systems]]"
leads_to: []
tags:
  - subject/cs
  - domain/systems-software
  - domain/programming
  - level/A-Level
  - level/IB-HL
  - level/university
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - curriculum/AP-CSA
  - type/theory
  - type/hands-on
  - type/visual-tool
  - notation/malloc-free
  - misconception/heap-means-priority-queue
  - misconception/garbage-collection-is-free
  - misconception/free-space-means-room
  - misconception/python-has-no-memory-bugs
---

# Memory Allocation and the Heap 内存分配与堆

> Every variable you have ever declared was given a home without your asking. Some homes are handed out and taken back in strict order, a stack of trays; the others are a car park, where a program takes any free bay for as long as it likes and is supposed to leave it empty. The car park is the heap, and almost every memory bug a programmer ever meets, the leak, the crash on a stale pointer, the program that slows down over a week, the pause nobody wrote, lives there. This card is what the heap is, how an allocator hands out its bays and gets them back, why free space is not the same as room, and how a garbage collector decides what is rubbish.

## What this is for

[[Recursion]] traces the call stack: frames pushed on a call and popped on return, in perfect order. [[Arrays]] says a block must be *allocated* before the index formula can use it; [[Linked List]] shows allocation as a pop from a free list. [[Heaps and Priority Queues]] is a different heap altogether, a tree with a rule, and says so. What none of them explains is where the objects live that outlast the function that made them, who gives them their bytes, who takes them back, and what goes wrong. This card builds an allocator in forty lines and a garbage collector in twenty, measures the real ones in C and Python, and shows the one case reference counting cannot handle.

## Definition

### Formal

A running program's memory is divided into regions. The **code** (text) holds the instructions; the **data** segment holds globals, sized when the program was compiled; the **stack** holds each function's locals, arguments and return address in a frame that is pushed on call and popped on return; and the **heap** holds everything whose size or lifetime is decided at run time. Heap memory is obtained from an **allocator** (`malloc` in C; `new` in Java; every object creation in Python), which keeps a **free list** of unused blocks, finds one large enough, splits it, and returns its address. It is returned either by hand (`free`) or by a **garbage collector**, which finds the blocks no longer reachable from the program's variables and frees them. Two failures follow from the design. A **leak** is a block never returned, so the program's memory grows without bound; **fragmentation** is free memory split into holes too small to use, so a request fails although the total free space would satisfy it. A **dangling pointer** is an address still held after its block was freed and possibly reused.

### Intuitive

A multi-storey car park: any car takes any free bay for as long as it likes and should leave it empty when it goes, and the attendant keeps only a list of free bays. A driver who never leaves keeps a bay for ever (a leak). After a busy day the free bays are scattered singly across the building and a bus is turned away although there is room in total (fragmentation). A bay handed to a second driver while the first still believes it is theirs is an accident waiting to happen (a dangling pointer). Languages differ only in who tidies up: in C the driver must remember to leave; in Python and Java an attendant walks the floors, checks which cars still have anyone holding a ticket for them, and tows the rest. That attendant is the garbage collector, and its walk is the pause your program takes for no reason you wrote.

### 中文锚点 (Chinese Anchor)

想一想一座多层停车场。每辆来的车随便找一个空位停下，想停多久就停多久，走的时候应该把车位空出来；管理员手里只有一张"哪些车位是空的"的单子。这就是堆：程序内存里的一块地方，东西需要多久就住多久，不需要了就该腾出来。它和食堂窗口旁那摞码得整整齐齐的托盘不一样：托盘总是最后放上去的最先被拿走，绝不会有一只被落在那儿没人拿，这也正是"栈"这个名字的由来。停车场有托盘堆永远不会有的麻烦。一个忘了把车开走的司机会永远占着一个车位，这样的人一多，停车场就"满"了，可满的全是没人用的车：这叫内存泄漏。来来去去的车大小不一，忙了一天之后，空车位零零星星散在整栋楼里，一辆大巴被拒之门外，尽管把空位加起来明明够用：这叫内存碎片。而一个车位在前一个司机还以为是自己的时候，就被交给了第二个司机，那就是一场等着发生的事故。不同的语言，差别只在谁来收拾。在 C 里，司机必须自己记得把车开走；在 Python 和 Java 里，有个管理员一层层巡视，看哪些车还有人拿着票，其余的统统拖走。这个管理员就是垃圾回收器，它巡视的那一趟，就是程序有时会莫名其妙停顿一下的原因，而这停顿不是你哪行代码惹出来的。

## Notation

| Term | Meaning | Notes |
|---|---|---|
| stack frame | one function call's locals, arguments and return address | pushed on call, popped on return; [[Recursion]] |
| heap | the region for run-time-sized, run-time-lived data | not the binary heap of [[Heaps and Priority Queues]] |
| `malloc(n)`, `free(p)` | C: request $n$ bytes; return the block at $p$ | `new` / `delete` in C++; `new` alone in Java |
| block header | the bytes before a block that record its size and whether it is free | why `free` needs no size argument |
| free list | the allocator's list of unused blocks | first fit, best fit, or one list per size class |
| coalescing | merging adjacent free blocks into one | the cure for fragmentation |
| reference count | how many pointers refer to an object | Python's first mechanism |
| roots | the variables a program can reach directly: the stack, globals, registers | where a tracing collector starts |
| mark and sweep | mark everything reachable from the roots; free the rest | the collector that sees cycles |
| RSS | resident set size, the process's memory actually in RAM | what a leak makes grow |

## Part I — Where things live, measured

![[heap-process-layout.svg|1000]]

`heap-lab.c` prints one address from each region of its own process. The numbers change every run, because the operating system places the regions at random addresses on purpose ([[Data Security]] on ASLR), but their order and their directions never do. The code sits lowest, the data just above it, then the heap, growing upward as blocks are allocated: the second `malloc(100)` landed 112 bytes after the first, which is 100 rounded up to 16 plus a header. Far above sits the stack, growing downward: a local three calls deeper has a lower address than one in `main`. A 100 KB block did not land in the heap at all but in a region of its own, because large requests are mapped straight from the operating system's pages ([[Operating Systems]] on paging) rather than carved from the heap.

**What each costs.** A stack allocation is one subtraction from the stack pointer, and freeing it is an addition, done when the function returns whether or not you remember: about 1.5 ns for 64 bytes. A heap allocation is a search of the free list and some bookkeeping, then a `free` that updates it: about 19 ns for the same 64 bytes with 100 000 blocks live at once, an order of magnitude more, and a 1 MB block, which goes to the operating system and back, about 130 ns. That ratio is why compilers put everything they can on the stack, why C programmers avoid small heap allocations in tight loops, and why Python, where *every* object is on the heap, allocates an eight-element list in about 3 µs.

**What forgetting costs.** The lab allocates 200 000 blocks of 1 000 bytes and keeps none of the pointers. Nothing crashes; nothing complains; the process grows from 8 MB to 204 MB and would keep growing until the machine ran out. That is a leak, and it is invisible until the day it is not.

## Part II — An allocator, built

`heap-lab.py` builds the heap in miniature: a 4 096-byte arena, and in front of every block a 4-byte **header** holding the block's size and one bit saying whether it is free. That header is why `free(p)` needs no size: the allocator reads it from the bytes just before `p`.

```python
def malloc(self, n):
    n = (n + 7) & ~7                                 # round up to 8 bytes, like real allocators
    for off, size, free in self.blocks():            # first fit: walk the list, take the first that fits
        if free and size >= n:
            rest = size - n
            if rest > self.HDR + 8:                  # split: the remainder becomes a new free block
                self._write(off, n, False); self._write(off + self.HDR + n, rest - self.HDR, True)
            else:
                self._write(off, size, False)
            return off + self.HDR                    # the "pointer": an offset into the arena
    raise MemoryError("no free block of %d bytes" % n)
```

Walking the whole arena for every request is **first fit**, the simplest policy and the slowest; real allocators keep separate lists per size class, so that a 64-byte request goes straight to a list of 64-byte holes, which is why the C measurement above is nanoseconds rather than microseconds. But the arithmetic of holes is the same at every scale, and the lab shows it:

![[heap-fragmentation.svg|1000]]

Thirty-two blocks of 120 bytes fill the arena. Free every other one and 2 044 bytes are free, yet `malloc(400)` fails: no single hole is larger than 124. Free the rest as well, so that 3 964 of 4 096 bytes are free, and it still fails, because the allocator sees thirty-two adjacent holes and not one big one. **Coalescing**, merging each free block with a free neighbour, turns them into one hole of 4 092 bytes and the request succeeds. This is **fragmentation**: the total free space never decides whether a request succeeds; the largest hole does. Real allocators coalesce on every `free`, keep size classes to stop small and large blocks interleaving, and still lose a few per cent of memory to holes in a long-running process, which is one reason a server is restarted on a schedule.

## Part III — Getting it back: two collectors, built

Freeing by hand is the C way, and Part I's leak and Part IV's dangling pointer are what it costs. The alternative is to let the runtime decide what is rubbish, and there are two ways to decide.

**Reference counting.** Every object carries a count of how many references point at it; assignment increments, reassignment and scope exit decrement, and at zero the object is freed at once, decrementing everything it pointed to in turn. Python does this for every object: `sys.getrefcount(x)` on a list bound to two names reports 3, the third being the call's own argument. It is simple, immediate and cheap per object, and it has one hole.

![[heap-mark-and-sweep.mp4]]

The lab's object graph: the roots point to A and F, A to B and D, B to C, and D and E point to each other. The program then drops its reference from A to D and the root's reference to F. F's count falls to zero and reference counting frees it. D and E each still have a count of 1, from each other, and nothing the program can reach points at either of them. They are garbage that reference counting will never collect: a **cycle**.

**Mark and sweep** asks a different question, not "how many things point at you?" but "can the roots reach you?". Mark: start from the roots and follow every reference, marking each object reached. Sweep: walk the whole heap and free everything unmarked.

```python
def mark_sweep(roots, heap):
    for o in heap: o.marked = False
    stack = list(roots)
    while stack:                                       # mark: everything reachable from a root
        o = stack.pop()
        if not o.marked:
            o.marked = True; stack.extend(o.refs)
    return [o for o in heap if not o.marked]           # sweep: everything else is garbage
```

The marking is a depth-first traversal of [[Graphs]], and on the lab's graph it reaches A, B and C and sweeps D, E and F, cycle and all. Its price is the walk: the program must stop, or be carefully interleaved, while the collector traverses every live object, and that pause grows with the size of the heap. Python uses both: reference counting for the common case, freeing most objects the instant they die, and a cycle collector that runs periodically to catch what counting misses. The lab makes ten thousand two-object cycles with the collector switched off: 20 000 objects stay alive; one `gc.collect()` reports 20 000 freed. Java and C# use tracing collectors only, made generational because most objects die young, and their pauses are the subject of an entire engineering literature.

## Part IV — The bugs

**The leak.** In C, a `malloc` without its `free`; in Python and Java, where nothing is ever freed by hand, a reference kept by accident: a cache that is never trimmed, a list that only grows, a listener never unregistered. The lab appends 20 000 strings to a global list and `tracemalloc` shows 1.3 MB still reachable and therefore uncollectable. A garbage collector frees what is *unreachable*, not what is *unused*, and a program that keeps a reference to everything it ever saw leaks exactly as a C program does.

**The dangling pointer.** `heap-lab.c` frees the block holding `"alice"`, allocates 16 bytes for `"mallory"`, and reads through the old pointer: it says `"mallory"`, because the allocator handed the same block to the new request. The read is undefined behaviour; today it returns the new tenant's data, tomorrow it crashes, and in the wrong program it is a security hole (use-after-free is among the commonest classes of exploited vulnerability in browsers and operating systems). Garbage-collected languages cannot have it, because an object with a reference to it is by definition not freed. That guarantee, not convenience, is the reason they exist.

**The double free.** Returning the same block twice corrupts the free list; the lab's `free` asserts on it. Real allocators may not notice until much later, which is what makes the bug hard.

**Fragmentation over time.** A process that allocates and frees many sizes for days develops holes it cannot use. The remedies are size classes, coalescing, and, in collected languages, **compaction**: the collector moves live objects together and updates every reference to them, which C cannot do because it cannot find every pointer.

## Where this is the working tool

**Every long-running program.** A web server, a game, a phone app and a browser tab all live or die by their allocator: a leak of a kilobyte per request is a crash after a million requests, which is an afternoon. The tools that find it, `valgrind` and AddressSanitizer for C, `tracemalloc` for Python, heap profilers for Java, all do the same thing the lab does: record every allocation and ask who still holds it.

**Why Python is slow and Java pauses.** Every Python integer, string and list is a heap allocation with a header and a reference count, and the 3 µs per small list in Part I is a large part of why a Python loop runs fifty times slower than the same loop in C. Java's allocation is fast, a pointer bump in a young generation, but its collector must stop the world to trace, and a trading system or a game engine budgets those pauses in milliseconds.

**Rust's answer.** A third way, neither hand-freeing nor a collector: the compiler tracks who owns every heap block and inserts the `free` at the point the owner goes out of scope, refusing to compile a program with a dangling reference. It is the reason the language exists, and the cost is that the programmer must prove ownership to the compiler.

**Hands-on.** Build and run `heap-lab.c` and read the addresses; run `heap-lab.py`. Then: change the toy allocator's policy to best fit (the smallest hole that fits) and see whether the 400-byte request survives longer; give `part_b` a second root pointing at D and watch mark and sweep keep the cycle; in Python, `import gc; gc.disable()` at the top of a program that builds cyclic structures and watch its memory with `tracemalloc`.

## Worked examples

### Example 1: where does it live

*In a Python function, `n = 5`, `s = "hello" * n` and `t = [s] * 3` are executed. Where do `n`, `s`, `t` and their contents live, and what happens to each when the function returns?*

**Trigger:** "where" is a question about lifetime; anything that must outlive a frame, or is sized at run time, is on the heap. **Tool: the region rule of Part I; reference counts from Part III.**

The *names* `n`, `s` and `t` are entries in the frame, on the stack. The integer 5 is a heap object Python already holds (small integers are shared); the string `"hellohellohellohellohello"` is a new heap object, sized at run time; the list is a heap object holding three references to that one string, so its count is 4 (three list slots and `s`). On return the frame is popped: the names go, the list's count reaches zero and it is freed, which decrements the string three times; the string's count reaches zero and it is freed. Nothing was freed by the programmer; everything was freed at once.

### Example 2: fragmentation arithmetic

*An allocator has 1 000 bytes free in blocks of 100, 300, 250, 200 and 150, not adjacent. Requests for 260, 260 and 120 bytes arrive in that order. Which succeed under first fit? Under best fit?*

**Trigger:** total free (1 000) exceeds total requested (640), so the question is about holes, not space. **Tool: the policy applied hole by hole, from Part II.**

First fit takes the first hole that fits in list order: 260 → the 300 (leaving 40); the second 260 → nothing else fits (250, 200, 150), it fails; 120 → the 250. Best fit takes the smallest hole that fits: 260 → the 300; the second 260 → fails likewise; 120 → the 150 (leaving 30), keeping the 250 whole for a later request. Either way a 260-byte request fails with 740 bytes free: fragmentation, and coalescing cannot help because the holes are not adjacent.

### Example 3: the cycle

*Two Python objects each hold a reference to the other, and the only outside reference to either is dropped. Trace what reference counting does and what the cycle collector does.*

**Trigger:** a reference between two objects that is not from a root. **Tool: Part III's two questions, "how many point at you?" and "can a root reach you?".**

Before the drop, one object has count 2 (the outside reference and its partner's) and the other has 1. Dropping the outside reference leaves both at 1. Neither reaches zero, so reference counting frees nothing, and the pair is unreachable from any root. The cycle collector, when it next runs, traces from the roots, fails to reach the pair, and frees both. Until it runs, they are a leak; if `gc.disable()` was called, they are a leak for ever.

### Example 4: leak or not

*A Python web server keeps `seen = {}` at module level and does `seen[request.id] = request` on every request "so that duplicates can be detected". Is this a leak?*

**Trigger:** a reference kept by a global with no removal. **Tool: reachable means uncollectable, from Part IV.**

Yes. Every request object, with its body, stays reachable from the module's dictionary for the life of the process, so the collector can never free one, and memory grows by one request per request. The fix is not a better collector but a bounded structure: keep only the ids, and only the last $N$ of them.

### Example 5: cost of a design

*A C program allocates one 64-byte record per event and frees it at the end of processing, at two million events per second. Using Part I's measurements, what fraction of a core does allocation alone consume, and what would a stack or a pool change?*

**Trigger:** a per-event cost times a rate. **Tool: the measured 19 ns per heap allocation and release; 1.5 ns on the stack.**

$2 \times 10^{6} \times 19\ \text{ns} = 38\ \text{ms}$ per second, about 4 % of a core, before the program does any work. A stack allocation, if the record dies within the function, costs $3\ \text{ms}$; a **pool** (allocate one large block, hand out fixed 64-byte slots from a free list, never return them to the system) costs about the same and also removes fragmentation, which is why game engines and network stacks use pools for everything with a fixed size.

## Common Misconceptions (Teaching Notes)

### 1. "The heap is the priority queue"

Two unrelated things share the word. [[Heaps and Priority Queues]] is a binary tree with an ordering rule, stored in an array. This heap is a region of memory with no order at all; the name means "a pile". A "heap allocation" has nothing to do with a heap sort.

### 2. "Garbage collection means no memory bugs"

It removes the dangling pointer and the double free. It does not remove leaks: anything reachable is kept, and Part IV's global dictionary leaks in Python exactly as a forgotten `free` leaks in C. It also adds a cost, the pause, that C does not have.

### 3. "Free space means room"

Part II's arena had 3 964 free bytes and could not serve 400. Allocation needs a *contiguous* hole; free space in small pieces is fragmentation, and only coalescing or compaction turns it back into room.

### 4. "The stack and the heap are different kinds of memory"

They are two regions of the same RAM, distinguished by discipline: the stack is freed in the reverse order it was allocated, by the return instruction; the heap in any order, by `free` or a collector. The 13× cost difference in Part I comes from the discipline, not the hardware.

### 5. "Python has no pointers, so it has no memory management"

Every Python name is a reference to a heap object, every object carries a count and a header, and the interpreter runs an allocator and two collectors under every line. The programmer does not manage it; the runtime manages it constantly, and knowing that is what turns "my script gets slower" into a diagnosis.

## Exam Notes

### Cambridge 9618 (A Level)

The allocator and the collector are not examined. What is: §5.1 lists "memory management" among the key management tasks of the operating system (AS), and §16.1 asks candidates to "Show understanding of virtual memory, paging and segmentation for memory management" and "the difference between paging and segmentation" (A2), which [[Operating Systems]] carries. The stack examined in §19 is the abstract data type, and the call stack appears only through recursion in §19.2, which [[Recursion]] carries. This card's Part I is the physical picture behind those rows.

### IB Computer Science (2027 guide)

B2.2.1 "Compare static and dynamic data structures" names "their underlying mechanisms for memory allocation and resizing" and asks for advantages and disadvantages "considering factors such as speed, memory usage, flexibility"; Parts I and II are those mechanisms. A1.3 lists memory management among the operating system's roles. The guide's linking question for B2, "Why is an understanding of variables and their scope important for effective memory management in computer systems", is Example 1.

### AP Computer Science A

The course description says that when a constructor is called "memory is allocated for the object" and that a reference variable holds "the memory address of that object"; garbage collection, the heap and allocation are not examined. Every `new` in the Java companions is a heap allocation of this card's kind, and Java's collector is why the companions never free anything.

### Where this is *not* examined

Cambridge 0478 examines virtual memory (§3.3 row 4) and nothing else here. No board examines an allocator, fragmentation, reference counting or mark and sweep; the card exists because "heap", "leak" and "garbage collection" are words every programmer meets and no syllabus explains.

## Beyond the syllabus

> [!info] Generational collection
> Recall that mark and sweep must trace every live object. Most objects die young (the temporaries of a single expression) and the few that survive tend to live long, so modern collectors keep a small **nursery** for new objects, collect it often and cheaply, and promote survivors to an older generation collected rarely. Java's and .NET's collectors, and Python's three-generation cycle collector, all rest on that observation.

> [!info] Why a pool beats the allocator
> Recall that first fit walks a list and that size classes are the cure. A **pool** is the limit of that idea: one size, one block, a free list threaded through the unused slots exactly as in [[Linked List]]'s array implementation. Allocation is a pop and release is a push, a few nanoseconds each, with no fragmentation because every slot is the same size. It is the allocator inside most game engines, network stacks and database buffers.

## Connections

- **Built on:** [[Recursion]] (the stack frame and its discipline), [[Linked List]] (the free list; allocation as a pop), [[Arrays]] (a contiguous block must be allocated before indexing works), [[Operating Systems]] (paging, virtual memory and the process's address space).
- **Tools used:** [[Graphs]] (marking is a depth-first traversal), [[Data Security]] (ASLR; use-after-free as an exploit class), [[Big-O Notation]] (first fit is linear in the number of blocks).
- **Beside:** [[Heaps and Priority Queues]] (the other heap; the cards agree the word is overloaded), [[Object-Oriented Programming]] (every object is a heap allocation), [[Programming Paradigms]] (ownership as a third discipline).

## Sources

- Knuth, D. E. (1997). *The Art of Computer Programming, Vol. 1* (3rd ed.), §2.5 "Dynamic storage allocation". First fit, best fit, boundary tags and coalescing.
- Wilson, P. R., Johnstone, M. S., Neely, M., & Boles, D. (1995). Dynamic storage allocation: a survey and critical review. *IWMM 1995*, 1–116. Fragmentation and allocator policies.
- McCarthy, J. (1960). Recursive functions of symbolic expressions and their computation by machine, Part I. *Communications of the ACM*, 3(4), 184–195. Mark and sweep, invented for Lisp.
- Collins, G. E. (1960). A method for overlapping and erasure of lists. *Communications of the ACM*, 3(12), 655–657. Reference counting.
- Jones, R., Hosking, A., & Moss, E. (2012). *The Garbage Collection Handbook*. CRC Press. Generational and concurrent collectors.
- Python documentation: `gc`, `sys.getrefcount`, `tracemalloc`; "Design and History FAQ: how does Python manage memory?". CPython's reference counting plus cycle collector.
- Measurements: `heap-lab.c` (Apple clang, `-O1`) and `heap-lab.py` (Python 3.11) on an Apple M1 Max, 2026-09-22; outputs saved in `heap-lab-c.txt` and `heap-lab.json`.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\text{rc}(o)$ | `\text{rc}(o)` | Reference count of object $o$; freed when it reaches $0$ |
| $\text{reach}(R)$ | `\text{reach}(R)` | The set of objects reachable from the roots $R$; the sweep frees its complement |
| $O(b)$ | `O(b)` | First fit: linear in the number of blocks $b$ |
