---
chinese: 并行排序与外部排序 (bìngxíng páixù yǔ wàibù páixù)
prerequisites:
  - "[[Sorting]]"
  - "[[Recursion]]"
  - "[[Big-O Notation]]"
leads_to:
  - "[[Concurrency]]"
  - "[[Stories/Dual-Core Craft]]"
  - "[[Dual-Core Craft]]"
tags:
  - subject/computer-science
  - domain/algorithms
  - domain/sorting
  - domain/parallel-computing
  - level/A-Level
  - curriculum/Cambridge-9618
  - type/deep
  - type/algorithm
  - notation/python
  - misconception/parallel-always-faster
  - misconception/more-cores-proportional-speedup
  - misconception/parallelism-reduces-work
  - misconception/python-threads-parallelize
---

# Parallel and External Sorting 并行排序与外部排序

> *[[Sorting]] taught five ways to order a list that fits in memory on one processor. Real systems break both of those assumptions: a phone has 8 cores sitting idle, a database has to sort a file far larger than its RAM, and Google sorts petabytes across thousands of machines. This card is about what sorting becomes when you have **many workers** (parallel) or **too much data for memory** (external) — and it answers the question [[Sorting]] left hanging: why does industry quietly lean on **merge sort** at scale? The surprise at the centre is that throwing more cores at a problem can make it **slower**, and that even when it helps, ten cores almost never give you ten times the speed.*

## Definition — two ways "bigger" breaks an ordinary sort

A textbook sort assumes one processor and that the whole array fits in memory. Drop either assumption and you get a different problem:

- **Parallel sorting** — many processors (cores, or whole machines) sort *at the same time*, then combine their results. The goal is **wall-clock time**: finish sooner by doing work simultaneously.
- **External sorting** — the data is far too big to hold in RAM, so it lives on disk (or across disks), and the sort is organised to **minimise slow disk reads/writes** rather than comparisons.

Both problems have the same hero, and it is not the single-core champion quicksort — it is **merge sort**, because its two halves are *completely independent*: they can be sorted on different cores or streamed off different disks and then stitched together by a merge. That independence is the structural property the rest of this card exploits.

### 中文锚点

**并行排序**（bìngxíng páixù）：多个处理器（多核，或多台机器）**同时**排序再合并，目标是缩短**实际耗时**（wall-clock time）。
**外部排序**（wàibù páixù）：数据太大放不进内存，存在磁盘上，排序的目标是**减少慢速磁盘读写**而非比较次数。

核心结论：能扩展（scale）的是**归并排序**（merge sort），因为它的两半**互相独立**——可以丢到不同核心/机器/磁盘上分别排序，再合并。但有两个反直觉的真相：(1) 给小数据加核心反而**更慢**（开销 overhead 大于收益）；(2) 即使有用，10 个核心也几乎拿不到 10 倍加速（**Amdahl 定律**）。

## Why merge sort is the one that scales

Recall from [[Sorting]] that merge sort **splits** the list in half, **recursively sorts each half**, then **merges** the two sorted halves. The split makes no decisions about *values* — it just cuts the array in two. So the two halves share nothing; sorting the left half cannot affect the right. That is exactly the property you need to hand the halves to different workers:

- **Fork:** split the array into one chunk per core.
- **Sort:** every core runs an ordinary sort on its own chunk, all at the same time.
- **Join:** merge the sorted chunks back together.

This is the **fork–join** pattern, and merge sort's recursion tree (see [[Recursion]]) *is* the fork–join tree. Quicksort, the single-core speed king, resists this: its **partition** step has to scan and rearrange the whole array around a pivot *before* it knows where to cut, and a bad pivot can hand one worker almost everything and the others nothing. Merge sort splits blindly and evenly, so the work divides cleanly. That is why the languages that prize predictability default to a merge-based sort (Python's and Java's Timsort).

## Parallelism is not free — the crossover

Here is the result that surprises everyone the first time. The plot below is **real data**: the *same* merge sort, run sequentially (one core) and in parallel (ten cores), across dataset sizes from 100 to 10 million. (Generate it yourself with [`parallel-sort-benchmark.py`](parallel-sort-benchmark.py).)

![[parallel-sort-crossover.svg|680]]

Read the two curves. The sequential line is almost straight on log–log axes — that is the familiar $n\log n$ cost growing steadily. The parallel line is the strange one: it is **flat** at about $0.07\,\text{s}$ for every small input. Sorting 100 numbers takes the parallel version the *same* time as sorting 10,000 — because at those sizes it is not really sorting. It is paying a **fixed overhead**: starting up ten worker processes, splitting the array, copying each chunk across to a worker, and merging the results back. That setup costs ~0.07 s whether the job is tiny or not.

So for small data the overhead is the whole story and parallel **loses badly** — at $N=100$ it was about **880× slower** than just sorting on one core. The two lines cross near $N \approx 60{,}000$: below that, parallel is a waste; above it, the sorting work finally outgrows the fixed overhead and parallel pulls ahead, reaching about **5× faster** at 10 million.

The animation makes the symmetry vivid — the *same ten cores*, 5× slower on a small job and 5× faster on a big one:

![[parallel-sort-race.mp4]]

This is why a task-management app should **never** parallelize its little sorts (a few dozen to-do items): you would pay 70 milliseconds of overhead to save microseconds. Parallelism is a tool for **big** data, and "big" here means *tens of thousands of elements at least*, measured — not assumed.

## Amdahl's law — why ten cores don't give ten times

If ten cores cooperate perfectly, the work should finish in one-tenth the time: a **10× speed-up**. The benchmark got **5×**. Where did the other half go?

![[parallel-sort-speedup.svg|680]]

The answer is **Amdahl's law**, the single most important idea in parallel computing. Almost no task is *entirely* parallelizable: some fraction must run on one worker. In our sort, the final **merge of the ten sorted chunks happens in one process** — it cannot be split, because merging *is* the act of combining everyone's work. That serial tail sets a ceiling.

Write $p$ for the fraction of the work that can run in parallel and $(1-p)$ for the stubbornly serial part. With $c$ cores, the parallel part finishes in $p/c$ of its old time while the serial part is unchanged, so the speed-up is

$$\boxed{\;S(c) = \dfrac{1}{(1-p) + \dfrac{p}{c}}\;}$$

Back-solve from the measurement: $S = 5.08$ at $c = 10$ gives $p \approx 0.89$. So about **89% of the work parallelized and ~11% was stuck in the serial merge** — and that 11% is brutal. Take the cores to infinity ($c \to \infty$) and the formula collapses to

$$S_{\max} = \frac{1}{1-p} \approx \frac{1}{0.11} \approx 9\times.$$

A thousand cores would *still* only sort this about 9× faster than one. The serial fraction, not the core count, is the wall you hit. The whole craft of high-performance parallel code is **shrinking $1-p$** — here, by using a smarter *parallel* merge instead of a single-process one.

## The invariant: parallelism changes *time*, never *work*

When a problem gets confusing, a [[Forward Reading and Problem Discovery|hunter asks what does not change]]. Add nine more cores to the sort and one thing stays exactly fixed: the **number of comparisons**. The benchmark counted them — about **18.7 million** comparisons to sort a million elements — and that figure is identical whether the work runs on one core or ten. Parallelism does not *delete* any work; it **redistributes the same work across time**, doing several comparisons at the same instant instead of one after another.

That reframes both halves of this card. Speed-up is never "fewer operations" — it is "the same operations, overlapped." And it explains the overhead penalty cleanly: overlapping work has a coordination cost (spawn, split, ship, merge), and if the work you saved by overlapping is smaller than that cost, you come out behind. The comparison count is the invariant; the wall-clock time is the variable you are trading for.

## External sorting — when the data won't fit in memory

Now the second wall. Suppose you must sort a **1 TB** file on a machine with **16 GB** of RAM. You cannot load it, so the in-memory sorts simply do not apply. The cost that matters is no longer comparisons — it is **disk I/O**, because reading from disk is thousands of times slower than reading from RAM. **External merge sort** is the standard answer, and it is merge sort again, reshaped around the memory limit:

1. **Sort runs.** Read as much of the file as fits in RAM (say 16 GB), sort that chunk in memory with an ordinary fast sort, and write the sorted chunk back to disk as a **"run."** Repeat until the whole file has become, say, 64 sorted runs on disk.
2. **Merge runs.** Open all 64 runs at once and do a **$k$-way merge**: keep one small buffer per run, repeatedly take the smallest element across the buffer fronts, and stream the merged output to disk. A **min-heap** — the structure behind a [[Heaps and Priority Queues|priority queue]] — finds the smallest of the $k$ fronts in $\log k$ time, however large each run is.

The merge only ever holds $k$ small buffers in memory, never the whole file — so 1 TB sorts in 16 GB. The design goal is to **minimise the number of passes over the data** (each pass is a full read + write of 1 TB), which is why real systems tune the run size and the merge fan-out $k$ carefully. This is exactly how a database executes `ORDER BY` on a table bigger than RAM, and how the Unix `sort` command handles enormous files.

### The $k$-way merge, in code

The heart of every external (and parallel) merge sort is the **$k$-way merge**: fold $k$ already-sorted streams into one. The trick is a **min-heap** holding the current *front* element of each run — so the smallest of all $k$ fronts is always one `pop` away, and each output element costs only $\log k$, no matter how large the runs are:

```python
import heapq

def k_way_merge(runs):
    """Merge k already-sorted sequences into one sorted list.
    A min-heap holds one 'front' per run, so each output element is O(log k)."""
    heap = []                                  # entries: (value, run_index, position)
    for i, run in enumerate(runs):
        if run:                                # seed the heap with each run's first element
            heapq.heappush(heap, (run[0], i, 0))
    out = []
    while heap:
        value, i, pos = heapq.heappop(heap)    # smallest front across all k runs
        out.append(value)
        if pos + 1 < len(runs[i]):             # refill from the SAME run, keeping it sorted
            heapq.heappush(heap, (runs[i][pos + 1], i, pos + 1))
    return out

runs = [[1, 5, 9], [2, 3, 8], [4, 6, 7]]
print(k_way_merge(runs))                       # -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The `run_index` in each heap entry is a tiebreaker (so equal values never force Python to compare anything awkward) *and* tells you which run to refill from. In a real external sort the `runs` are **files on disk** read a buffer at a time, not lists in memory, so the heap never holds more than $k$ elements however large the file. Python ships exactly this as `heapq.merge(*runs)` — a lazy $k$-way merge over any iterables — which is what the benchmark used to stitch the parallel chunks back together.

The animation traces the merge step by step: the heap's **root** is always the smallest of the four fronts, so it leaves to the output; the next element of that run rises into the root; and a **sift-down** (swapping with the smaller child until order is restored) re-floats the new minimum to the top. Watch the output fill in perfect sorted order while the heap never holds more than $k=4$ items.

![[parallel-sort-kway-merge.mp4]]

## Sorting at planetary scale — MapReduce

Push further: the data is so big it does not fit on **one machine's disks**. Now you spread it across a cluster, and sorting becomes a *distributed* problem. The famous **MapReduce** model (and its descendants like Spark) has a hidden sort at its heart — the **shuffle** phase, which groups every key together, is a giant distributed sort across the network. The benchmark **TeraSort** measures exactly this: how fast a cluster can sort a terabyte (the record is seconds). The shape is *still* the same idea — partition the data across machines, sort each partition locally, merge — just with the network as the new bottleneck the way disk was for external sort and the merge was for parallel sort.

> [!info] Credit
> The thread running through this card — that parallel and external merge sort are the real reason industry leans on merge at scale — comes from **Modric Wang**, who first pushed the point in the [[Sorting]] card. Thanks, Modric.

## The benchmark, in numbers

The data behind the plots (mean of repeated runs, 10 cores, pure-Python merge sort sequential vs across-process parallel). Comparisons are the *work*; seconds are the *time*.

| N | sequential | parallel (10 cores) | speed-up | comparisons (either way) |
|---:|---:|---:|---:|---:|
| 100 | 0.00008 s | 0.071 s | 0.001× (880× slower) | 540 |
| 10,000 | 0.014 s | 0.069 s | 0.20× (5× slower) | 120,000 |
| 100,000 | 0.168 s | 0.114 s | 1.48× | 1,540,000 |
| 1,000,000 | 2.03 s | 0.47 s | 4.30× | 18,700,000 |
| 10,000,000 | 24.9 s | 4.90 s | 5.08× | — |

The flat parallel floor (small $N$), the crossover near 60,000, and the Amdahl ceiling at ~5× are all visible in one table.

## Common Misconceptions

### 1. "More cores means proportionally more speed"
Amdahl's law forbids it. The serial fraction caps the speed-up no matter how many cores you add; here 10 cores bought 5×, and infinite cores would buy only ~9×. Doubling cores past a point buys almost nothing.

### 2. "Parallel is always faster — it's more power"
Only above the crossover. Below it (small data) the fixed cost of spawning workers and shipping data dwarfs the work saved, and parallel is dramatically *slower* — 880× slower at $N=100$ in the benchmark. Parallelism is for big data, and you should **measure** the crossover, not guess it.

### 3. "Parallelism reduces the amount of work"
No — it reduces *time*, not *work*. The same 18.7 million comparisons happen to sort a million elements whether on 1 core or 10; they are merely done at the same time instead of in sequence. Work is the invariant; time is what you trade.

### 4. "I'll just use threads in Python to parallelize my sort"
Python's **GIL** (Global Interpreter Lock) stops threads from running Python bytecode truly simultaneously, so threads give *no* speed-up for CPU-bound work like sorting. You must use **multiprocessing** (separate processes) — which is *why* the overhead is so high: each process is a fresh interpreter, and data must be **pickled** and copied across the process boundary. That copying cost is much of the flat floor in the plot.

### 5. "External sorting is just running a normal sort on a file"
The point of external sorting is not the comparisons — it is **minimising disk passes**, because disk is thousands of times slower than RAM. An algorithm with more comparisons but fewer passes over the data wins. It is an I/O-cost problem wearing a sorting costume.

## Exam Notes

This is **enrichment** — it sits beyond every A-Level/IGCSE/AP syllabus row, and no exam will ask you to implement a parallel or external sort.

### Cambridge 9618 (A-Level CS) — the understanding behind §15.1
The required sorting (bubble, insertion, merge, quicksort) is closed by [[Sorting]] and [[Big-O Notation]]. This card is the *why* behind **§15.1** (processors and **parallel processing** — multi-core, SISD/SIMD/MISD/MIMD, massively parallel). The syllabus treats that as vocabulary to memorise; **Amdahl's law and the overhead crossover are the actual ideas** those words point at, and knowing them turns rote acronyms into something you understand. Worth reading for any A2 student who wants the concepts beneath §15.1 to make sense.

### Cambridge 0478 (IGCSE CS)

Not examined, in any form. §7 stops at bubble sort, insertion sort and the two searches on a single machine with everything in memory — neither *parallel* nor *external* appears anywhere in the syllabus. The one adjacent row is §3.3's storage hierarchy, which is the *reason* external sorting exists: this card is what that hierarchy costs you once the data outgrows RAM.

### IB Computer Science (first assessment 2027)

Not examined. The published outline names bubble and selection sort, linear and binary search, and efficiency comparison at the level of "which is faster and why" (B2.4) — the same quartet closed by [[Sorting]], [[Searching]], [[Big-O Notation]] and [[Recursion]]. There is no theory-of-computation or parallel-algorithms statement to attach this to. HL's system-fundamentals content touches multi-core hardware as *architecture* vocabulary, not as algorithm design, so Amdahl's law sits behind that vocabulary rather than inside any assessed statement.

### AP Computer Science A

Not examined. AP CSA is single-threaded Java throughout — `ArrayList` and array sorting at §4.14–4.17, with no concurrency, no `Thread`, no parallel streams, and no external storage model. (AP CSP mentions parallel and distributed computing at the level of "speedup" as a *concept*; even there, nothing here is assessed.)

*Enrichment cards get an explicit not-examined line for every board rather than silence — silence reads as an oversight rather than a verdict.*

## Connections

- **Prerequisite:** [[Sorting]] — merge sort is the hero here precisely because of the independent-halves property introduced there; this card is the "card of its own" that [[Sorting]] promised. [[Recursion]] — fork–join *is* divide-and-conquer recursion, the recursion tree mapped onto cores. [[Big-O Notation]] — Amdahl's law is the parallel analogue of asymptotic limits: a ceiling you cannot optimise past.
- **Leads to:** [[Concurrency]] — once many workers share work, coordinating them (race conditions, mutual exclusion) becomes its own subject.
- **Relies on (reserved):** [[Heaps and Priority Queues]] — the $k$-way merge is built on a min-heap; that abstract data type and its array implementation belong to the planned **Data Structures** bay (it is *used* here, not yet taught).
- **Cross-domain:** [[Information Theory]] — the $n\log n$ comparison lower bound from [[Sorting]] still binds *each core*, so even a perfect parallel sort can't escape the information cost of ordering; it only spreads that cost across workers.
- **Hardware:** [[Pipelining and Simultaneous Multithreading]] — the machine this algorithm runs on: multi-core, SMT, and the GPU's SIMD lanes a GPU sort exploits. Amdahl's law lives in both cards — here as the algorithm's ceiling, there as the processor's.
- **Story:** [[Stories/Dual-Core Craft]] — this card's thesis as history. Why *StarCraft* runs its whole world on one core ("Dual-Core Craft"), how the deterministic-lockstep contract makes a real-time strategy simulation the canonical *serial* workload, and how the industry clawed parallelism back with job systems and ECS — Amdahl's law wearing a Zerg costume.
- **Application:** database `ORDER BY` on huge tables (external merge sort), the MapReduce/Spark **shuffle** (distributed sort), GPU sorting, and every multi-core library sort.
- **For 9618 / A2 students:** the concept layer beneath §15.1 (parallel processing) — read it for understanding, not for an exam answer.

---

## Beyond Syllabus

### Gustafson's law — the optimistic mirror of Amdahl
Amdahl asks "fixed problem, more cores — how much faster?" and gives a gloomy ceiling. **Gustafson's law** asks the question industry actually faces: "more cores — how much *bigger a problem* can I solve in the same time?" In practice you don't sort the same million items on a supercomputer; you sort a billion. As the problem grows, the parallel fraction $p$ grows with it (the serial setup stays roughly fixed), so the *effective* speed-up keeps climbing. Both laws are true; they answer different questions. Our benchmark shows both faces — Amdahl's ceiling at fixed $N$, and the speed-up *rising* with $N$ toward that ceiling.

### Work, span, and why the serial merge hurts
Theorists measure a parallel algorithm by two numbers: **work** $W$ (total operations $= \Theta(n\log n)$, the same as the sequential cost) and **span** $T_\infty$ (the longest chain of dependent steps — the time on *infinitely many* cores). The best possible speed-up is the **parallelism** $W / T_\infty$. Merge sort with a *sequential* merge has span $\Theta(n)$ (the final merge alone touches all $n$ elements one after another), so its parallelism is only $\Theta(\log n)$ — which is why our single-process merge capped the gain. Replace it with a **parallel merge** (split both halves at the median and merge the quarters concurrently) and the span drops to $\Theta(\log^2 n)$, unlocking far more cores. Shrinking the span is shrinking Amdahl's $1-p$.

### Bitonic sort and the GPU
GPUs have thousands of tiny cores but hate branches and irregular memory access — so they don't run merge sort well. They use **sorting networks** like **bitonic sort**: a *fixed* pattern of compare-and-swap operations, identical regardless of the data, that a GPU can execute in lockstep. It does more comparisons than merge sort ($\Theta(n\log^2 n)$) but its perfectly regular, data-independent structure maps beautifully onto data-parallel hardware — a reminder that the "best" algorithm depends on the machine, not just the Big-O.

## Python / Notation Reference

| Symbol / term | Meaning |
|---|---|
| fork–join | split work to many workers (fork), recombine results (join) |
| $p$ | fraction of the work that can run in parallel |
| $S(c) = \dfrac{1}{(1-p)+p/c}$ | Amdahl's law — speed-up on $c$ cores |
| $S_{\max} = \dfrac{1}{1-p}$ | the ceiling as $c \to \infty$ |
| run | a sorted chunk written to disk in external sort |
| $k$-way merge | merge $k$ sorted streams at once via a heap ($\log k$ per element) |
| work $W$ | total operations $=\Theta(n\log n)$ — the invariant |
| span $T_\infty$ | longest dependent chain — time on infinite cores |
| GIL | Python's Global Interpreter Lock — why CPU-bound threads don't parallelize |
