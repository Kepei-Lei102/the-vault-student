---
chinese: 数组 (shùzǔ)
prerequisites:
  - "[[RAM and the Memory Hierarchy]]"
leads_to:
  - "[[Searching]]"
  - "[[Sorting]]"
  - "[[Stacks and Queues]]"
  - "[[Linked List]]"
tags:
  - subject/computer-science
  - domain/data-structures
  - level/IGCSE
  - level/A-Level
  - level/AP
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/AP-CSA
  - curriculum/IB-CS
  - syllabus/0478-8-2
  - syllabus/9618-10-1
  - syllabus/9618-10-2
  - syllabus/AP-CSA-4-3
  - syllabus/AP-CSA-4-4
  - syllabus/IB-CS-B2-2
  - type/deep
  - notation/python
  - misconception/index-is-the-value
  - misconception/assignment-copies-an-array
  - misconception/arrays-can-grow
  - misconception/zero-is-the-only-correct-start
  - misconception/2d-array-is-a-real-grid
---

# Arrays 数组

> *Thirty students, thirty test scores. Write `s1, s2, s3, …, s30` and you have thirty perfectly good variables — and no way to loop over them, because **a loop counts, and `s1` is not a number**. That is the entire problem, and the array is the entire answer: it trades thirty names your program cannot compute for one name plus arithmetic it can. Everything else — why every element must be the same type, why the length is fixed, why `scores[999999]` is exactly as fast as `scores[0]`, even why the argument about counting from 0 or from 1 is not a matter of taste — falls out of the one formula that makes that arithmetic work.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| array | 数组 | many values of one type under one name, reached by number |
| element | 元素 | one of the values stored in the array |
| index (subscript) | 下标 / 索引 | the number that selects an element — *which box*, not what's in it |
| lower bound / upper bound | 下界 / 上界 | the first and last valid index |
| contiguous | 连续的 | laid out end-to-end in memory, no gaps |
| base address | 基地址 | where element zero begins |
| traverse / iterate | 遍历 | visit every element in turn |
| out of bounds | 越界 | an index outside the declared range |
| record | 记录 | several values of **different** types under one identifier |
| field | 字段 | one named part of a record |
| aliasing | 别名 | two names referring to the same array |

## The problem, before the tool

A tool is a superstition until you have felt the problem it kills, so start with thirty separate variables and try to do anything with them.

```python
s1 = 74; s2 = 68; s3 = 91          # ... and twenty-seven more
total = s1 + s2 + s3               # ... and twenty-seven more
```

The nuisance is the typing. The **fatal** part is that you cannot write a loop. A loop's whole mechanism is a counter that changes — 1, 2, 3 — and `s1` is not `s` at position 1; it is a name, atomic and indivisible, chosen by *you* at the moment you wrote the program. There is no arithmetic that turns the number `2` into the name `s2`, because names are fixed when the program is written and numbers are only known when it runs.

That is the hunter's reading of the whole topic. **What varies is the position; what stays the same is the operation.** *Add this score to the total* is identical for all thirty students — but it is welded to thirty different names, so it has to be written thirty times. Separate the two and the problem dissolves: keep one name for the collection, and let a *number* — something a program can compute, compare and increment — pick the element.

$$\texttt{s1, s2, …, s30} \quad\longrightarrow\quad \texttt{scores[i]}$$

An array is what you get when you make a name **computable**.

```python
scores = [0] * 30                   # one name, thirty boxes
for i in range(30):
    scores[i] = int(input())
print(sum(scores) / len(scores))
```

Three lines that do not grow if the class doubles. The loop was impossible a moment ago and is now trivial, and nothing changed except that the varying part became a number.

## The exam's own definition, and why all of it is one fact

Cambridge defines an array, in its own words, as a **fixed-length structure of elements of identical data type, accessible by consecutive index numbers**. Students memorise that as three unrelated rules to recite. It is far better than that: **all three clauses are consequences of a single formula**, and once you have the formula you never have to remember them again — you can re-derive them at the desk.

## The one formula

An array occupies a **contiguous** run of memory: one unbroken block, elements laid end to end with no gaps. [[RAM and the Memory Hierarchy]] gives the hardware this rides on — memory is a flat sea of numbered cells, and any address is reachable in the same tiny time as any other. So if the machine knows *where the block starts* and *how big one element is*, it can compute where element $i$ lives without looking at a single other element:

$$\boxed{\ \text{address}(i) \;=\; \text{base} \;+\; (i - l) \times \text{size}\ }$$

where $\text{base}$ is the address of the first element, $l$ is the lower bound, and $\text{size}$ is the number of bytes one element occupies.

![[arrays-address-arithmetic.svg|697]]

One multiplication and one addition — a fixed amount of work, whatever $i$ is. Now read the three clauses off the formula:

| The rule | Why the formula forces it |
|---|---|
| **elements of identical data type** | The formula multiplies by $\text{size}$. Multiplication only works if $\text{size}$ is the *same* for every element — so every element must be the same width, and the simplest guarantee of equal width is equal type. |
| **consecutive index numbers** | Adding $(i-l)\times\text{size}$ assumes cell $i$ sits exactly one $\text{size}$ past cell $i-1$. Skip an index and the arithmetic lands in the wrong place. |
| **fixed length** | The block must stay unbroken. Growing it means the neighbouring memory must happen to be free — and in general it is not, so growth means moving the whole array somewhere else, and $\text{base}$ was the one thing everything relied on. |

The restrictions are not the language being fussy. They are the **price of the multiplication**, and what you buy with them is the single most important property an array has.

**Access is $O(1)$ — constant time.** Reaching `scores[999999]` costs one multiply and one add, exactly what `scores[0]` costs. The array does not *look* for the element; it **calculates** where it is. This is why [[Big-O Notation]] can treat `a[i]` as one step, and why every algorithm that indexes — [[Searching|binary search]] jumping to the middle, [[Sorting|a sort]] swapping two distant items — is fast enough to be worth writing. Take that away and half of algorithmics collapses.

> [!info] Beyond syllabus — how a list grows anyway
> Python's `list` and Java's `ArrayList` *do* grow, which seems to contradict "fixed length". They don't cheat the formula, they pay for it: the object holds a fixed array with spare room, and when it fills up it allocates a **bigger one — typically about double — and copies everything across**. That one copy is $O(n)$, but doubling means it happens rarely; spread the cost over all the appends between copies and each one averages out to constant work. This averaging is called **amortised** analysis, and it is why `append` is *usually* instant and *occasionally* not. Note what stays true underneath: at any instant there is still one contiguous block and still one formula.

## The index is an offset, not a position

Now the argument every beginner has: does counting start at 0 or at 1? Read the formula again with $l = 0$:

$$\text{address}(i) = \text{base} + i \times \text{size}$$

The index is not "which one in the queue". It is **how far from the start** — a *distance*, measured in elements. The first element is at the start, so it is zero elements away from the start, so its index is 0. Nothing arbitrary happened: 0-based indexing is what the arithmetic says when nobody adjusts it.

One-based indexing is the same formula with a compensation built in:

$$\text{address}(i) = \text{base} + (i-1)\times\text{size} = \underbrace{(\text{base} - \text{size})}_{\text{a fictional element 0}} + i \times \text{size}$$

The machine pretends the array begins one element *earlier* than it does, and everything works. So neither convention is more correct; one is the raw arithmetic and the other is the raw arithmetic plus a human courtesy. This is why languages genuinely disagree — Python, Java, C and C++ count from 0; Fortran, MATLAB, R and Lua from 1 — and why the exam's pseudocode makes you **declare your bounds explicitly** instead of assuming.

That is where the exam vocabulary comes from and it is worth being exact about it:

- **lower bound** — the smallest valid index
- **upper bound** — the largest valid index
- the number of elements is $\text{upper} - \text{lower} + 1$

That $+1$ is the **fence-post error** in disguise: a fence with posts at both ends of a 10 m run spaced 1 m apart has eleven posts, not ten. `ARRAY[1:30]` holds thirty; `ARRAY[0:30]` holds thirty-one; a loop written `for i in range(1, 30)` in Python touches twenty-nine. Almost every off-by-one bug you will ever write is this one.

## Out of bounds — where the abstraction leaks

The formula is happy to compute an address for *any* $i$. It has no idea the array ended. Ask for `scores[30]` in a thirty-element array and the arithmetic dutifully points one element past the end, at memory that belongs to something else entirely.

What happens next is the language's choice, and the two answers are worlds apart:

```python
scores = [0] * 30
scores[30]        # IndexError: list index out of range   — refuses, loudly
scores[-1]        # the LAST element: Python maps -1 to index 29
```

Python **checks** every index and raises. C and C++ do not — they compute the address and use it, so `scores[30] = 0` quietly writes over whatever lives there: another variable, a saved return address, anything. The program does not crash at the mistake; it crashes later, somewhere unrelated, or worse, it does not crash at all and simply becomes wrong. This is the **buffer overflow**, and deliberately overrunning an array to overwrite a return address has been the engine behind a large fraction of the security exploits of the last thirty years. [[Operating Systems]]' memory protection is the outer wall that stops the damage escaping the process; inside the process, the array's bounds are guarded only by whoever wrote the loop.

The teaching point is not "C is bad". It is that **bounds checking is a cost some languages pay and others refuse**, and knowing which kind you are in tells you how careful the loop has to be.

## Two dimensions — the grid that is secretly a line

A table wants two indices: `Results[team][metric]`. Declaring one is easy; the interesting part is that **memory has no second dimension**. It is still a flat sea of numbered cells, so a 2D array is stored as one long run with the rows laid one after another — **row-major order** — and the formula just grows one term:

$$\text{address}(r, c) = \text{base} + \big(r \times n_{\text{cols}} + c\big) \times \text{size}$$

![[arrays-2d-row-major.svg]]

Read it as *skip $r$ whole rows, then $c$ elements into this one*. Still one multiply-and-add shape; still $O(1)$.

```python
grid = [[0] * 3 for _ in range(2)]      # 2 rows, 3 columns
for r in range(2):                      # nested iteration: rows outside...
    for c in range(3):                  # ...columns inside
        grid[r][c] = r * 3 + c
```

> [!warning] The `[r][c]` vs `[r, c]` gap
> Exam pseudocode writes a 2D element with **one** pair of brackets, `Grid[Row, Col]`, because the notation follows the mathematics of a single indexed structure. Python writes **two**, `grid[row][col]`, because a Python "2D array" is literally a list *of lists* — `grid[row]` hands you a row object and the second bracket indexes into it. The exam-hall dialect is handed to [[Cambridge Pseudocode]]; the thing to carry across is that the comma form describes one structure and the two-bracket form describes a structure of structures. NumPy, notably, offers `m[r, c]` — because a NumPy array *is* one flat contiguous block, exactly like the diagram above.

**Row-major is not a detail — it is measurable.** The machine never fetches one value: it fetches a **cache line**, 64 bytes at a time, which is exactly eight 64-bit floats. Walk along a row and that line arrives already full of the values you are about to want, so one fetch serves eight additions. Walk down a column and every step lands in a different line, so each fetch serves *one* addition and the other seven values are dragged in and thrown away — and in a matrix bigger than the cache they are evicted long before the next column comes looking for them.

![[arrays-row-major.mp4]]

The model predicts eight times the memory traffic for identical arithmetic. Measured, it is gentler than that: summing a 6000 × 6000 matrix of 64-bit floats — the same 36 million additions, differing only in visiting order — takes about **21 ms along the rows and about 98 ms down the columns, four to five times slower**. The gap between the predicted eight and the measured four-and-a-half is the **hardware prefetcher**, which spots the regular stride and starts fetching ahead of the loop. It claws back roughly half the loss and cannot claw back the rest. This is [[RAM and the Memory Hierarchy]]'s locality of reference with a stopwatch on it, and it is why numerical libraries care so much about which way a loop runs.

## The name is not the box

Here is the trap that survives into professional code, and it is examined:

```python
a = [1, 2, 3]
b = a                 # NOT a copy
b[0] = 99
print(a)              # [99, 2, 3]   —  a changed
```

Assignment copied the **name**, not the array. Both `a` and `b` now hold the same base address, so they are two labels on one block of memory — **aliasing**. Why would a language do this? Because the alternative is worse: copying on assignment would mean that passing a million-element array into a function silently duplicates a million elements. Handing over the base address costs a few bytes, and the formula does the rest.

That is exactly what the exam wants said out loud. When an array is passed to a procedure, it is passed **by reference** (`BYREF`) — and a Paper 2 question that says *"the array is passed as a parameter; identify how this parameter should be specified in the procedure header"* is worth its mark for that one word.

The same fact produces Python's most famous beginner bug, and it is worth meeting once:

```python
grid = [[0] * 3] * 2      # "two rows of three"
grid[0][0] = 1
print(grid)               # [[1, 0, 0], [1, 0, 0]]   —  BOTH rows changed
```

`[x] * 2` repeats the *reference* twice, so there is one row with two names pointing at it. The fix is to build each row separately, which is what the list comprehension above does. To copy deliberately, be explicit:

```python
b = a.copy()              # or a[:], or list(a) — a new block, values copied
import copy
g = copy.deepcopy(grid)   # nested structures: copies the rows too
```

## When one type isn't enough — records

An array's uniformity is its engine, and also its limit. Store a person's last name, first name and city and everything is a string, so a 2D array works. Store a component's ID (string), reject flag (Boolean) and weight (real) and it does not — there is no single type, and therefore no single $\text{size}$ to multiply by.

The old workaround is **parallel arrays**: one array per attribute, all sharing an index, so `names[i]`, `flags[i]` and `weights[i]` describe the same component. It works, and it is fragile in a specific way — the arrays are held in step only by discipline. Sort one and forget the others and the data is silently, irrecoverably scrambled, with no error message anywhere, because each array is individually still perfectly valid.

A **record** fixes this by putting the different types under one identifier:

```python
from dataclasses import dataclass

@dataclass
class Component:
    item_id: str
    reject:  bool
    weight:  float

c = Component("X-42", False, 19.6)
print(c.weight)                      # fields are reached by NAME
```

Note precisely how a record differs from an array, because it is the same idea inverted:

| | Array | Record |
|---|---|---|
| elements are | all one type | of different types |
| selected by | an **index** — a number, computed while running | a **field name** — fixed when the program is written |
| the machine computes | $\text{base} + (i-l)\times\text{size}$ | $\text{base} + \text{a fixed offset per field}$ |
| so you can | loop over it | not loop over it — and don't need to |

**An array is indexed by something that varies; a record is indexed by something that doesn't.** Which is the same invariant-versus-variable split the whole card started from, applied one level up — and it is why they combine so well. Put records *inside* an array and you get the table you actually wanted: rows selected by a computed number, columns by a fixed name.

```python
batch = [Component("", False, 0.0) for _ in range(1000)]
batch[7].weight = 20.1
in_range = [c for c in batch if lo <= c.weight <= hi]
```

This is the shape real exam questions use — a declared record type, then an array of a thousand of them — and it is the last stop before objects: attach functions to a record and the record becomes a class.

## Worked examples

### Example 1 — bounds arithmetic, every tool named

*An array is declared with lower bound 1 and upper bound 30, each element a 4-byte integer, the block starting at address 5000. Where is element 7, and how many elements are there?*

**Tool: the element count — $\text{upper} - \text{lower} + 1$.**
$30 - 1 + 1 = \boxed{30}$ elements. (The $+1$ is the fence-post: both ends are included.)

**Tool: the address formula — $\text{address}(i) = \text{base} + (i-l)\times\text{size}$.**
$$\text{address}(7) = 5000 + (7-1)\times 4 = 5000 + 24 = \boxed{5024}$$

**Tool: the offset reading — the index is a distance, not a position.** Element 7 is the *seventh* element but only *six* elements from the start, which is why the answer is $5000+24$ and not $5000+28$. Confusing those two is the same mistake as the fence-post, met from the other side.

### Example 2 — a 2D traversal that names its loops

*Ten teams, each with games won, drawn and lost. Compute each team's points at 3 for a win and 1 for a draw.*

```python
WON, DRAWN, LOST = 0, 1, 2                 # name the columns; magic numbers hide bugs
results = [[0] * 3 for _ in range(10)]
points  = [0] * 10

for team in range(10):                     # Tool: outer loop walks the rows...
    w = results[team][WON]                 # ...inner index picks the column
    d = results[team][DRAWN]
    points[team] = 3 * w + 1 * d           # Tool: the operation that doesn't vary
```

The outer loop is the thing that varies (which team); the body is the thing that doesn't (how points are computed). Naming the columns costs one line and removes an entire class of bug — `results[team][1]` is unreadable six months later, and unreviewable today.

### Example 3 — the half-empty array

*A 35-element array holds sandwich fillings, but only some elements are used. Unused ones hold `""` and may appear anywhere. Pick a random used filling.*

This is a genuinely awkward exam favourite, and the awkwardness is the lesson: **a fixed-length array has no idea how full it is.** The length is a property of the declaration, not of the data, so "how many are real?" is a question the array cannot answer — you must either keep a separate counter, or mark unused cells with a value that could never be real data (a **sentinel**) and check for it.

```python
import random
usable = [f for f in fillings if f != ""]     # Tool: filter by the sentinel
choice = random.choice(usable)
```

The sentinel only works while the marker is impossible as genuine data. `""` is safe for a filling name; `0` is *not* safe for a temperature, and `-1` is *not* safe for a bank balance. Choosing a sentinel is choosing a promise about your data, and the promise is worth stating out loud when you make it.

## Common misconceptions (teaching notes)

### 1. Confusing the index with the value

Asked for the third score, the student writes `3` — or reads `scores[3] = 91` as "the score is 3". The index says *which box*; the value is *what is in it*.

**Fix:** make the two visibly different types — a `names` array where the index is a number and every value is a word. `names[2]` cannot possibly be `2`. Then return to numbers with the habit intact. The address formula reinforces it: the index goes *into* the arithmetic, never comes out of it.

### 2. "`b = a` makes a copy"

The student copies an array to keep an original, modifies the copy, and is baffled when the original changes too. This survives well into professional code.

**Fix:** run the four-line demo above and let them watch `a` change. Then give the reason — one base address, two names — because the mechanism is what makes it predictable rather than spooky. Finish on the `[[0]*3]*2` grid trap, which is the same fact wearing a disguise and will otherwise bite them within a week.

### 3. "The array will just grow"

Declared as 30, they store a 31st and expect it to stretch. Python's list *does* grow, which quietly teaches the wrong intuition for every exam and every other language.

**Fix:** ask *where* the 31st element would physically go, given that the block is contiguous and the memory next door already belongs to someone. The answer — it must all move — is exactly why fixed length is in the definition, and exactly what the doubling trick is paying for.

### 4. "Counting from 0 is correct / counting from 1 is correct"

Taken as a rule to obey, and then applied to the wrong language.

**Fix:** derive it rather than decreeing it. The index is a distance from the start, so 0 is the arithmetic's own answer; 1 is a courtesy that costs one subtraction. Then the real habit follows: *read the declaration*, since the exam's pseudocode states its bounds precisely so the question is never open.

### 5. "A 2D array is a grid"

It is drawn as a grid, so it is imagined as one — and then row-major order, the single-bracket exam notation, and the four-fold speed difference between traversal directions all look like arbitrary trivia.

**Fix:** draw the flat run of memory *underneath* the grid picture, with the rows laid end to end, and compute one address by hand. The grid is a helpful lie told by the notation; the line is the truth, and everything odd becomes obvious the moment the line is visible.

## Exam Notes

### Cambridge 9618 (A Level)

Arrays are **§10.2** and records are **§10.1**, both AS content examined on **Paper 2** — but the topic is genuinely everywhere, because almost every Paper 2 and Paper 4 scenario stores its data in an array.

- **§10.1 Data Types and Records** — select appropriate data types (integer, real, char, string, Boolean, date); state the **purpose of a record structure** (to hold data of *different* types under *one* identifier — that phrase is the mark); define a record structure; read from and write to one. A recurring easy mark: a table of variables asking for each one's data type, where an *array index* is always `INTEGER`.
- **§10.2 Arrays** — use the technical terms **index, upper bound, lower bound**; choose 1D or 2D for a task and justify it; write 1D and 2D array pseudocode; and **process array data with a bubble sort and a linear search** — the algorithms themselves live in [[Sorting]] and [[Searching]], but this is their AS home.
- **Declaration questions are worth two marks** and they split predictably: one for the dimensions and bounds, one for the rest of the statement. A 100-row, 2-column string table earns both only if the bounds are right.
- **Passing an array to a module is `BYREF`** — a one-mark question in its own right, and the reason is the aliasing section above. Worth knowing that this makes §10.2 quietly dependent on §11.3's parameter passing.
- **Arrays of records** are the standard A-Level scenario shape: a `TYPE` declaration, then `ARRAY[1:1000] OF ThatType`, then modules that search or update it. Expect "suggest how an unused element could be indicated" — a sentinel-value question.
- Watch for the neat trick where **the index itself carries meaning** (an array indexed by score, so no search is needed at all). Recognising it is the whole question.
- The exam's strict pseudocode dialect — `DECLARE`, `ARRAY[1:30] OF INTEGER`, the comma form for 2D — belongs to [[Cambridge Pseudocode]].

### Cambridge 0478 (IGCSE)

Arrays are **§8.2**, examined on **Paper 2**, and unusually explicit about what is expected:

- **Declare and use 1D and 2D arrays**; understand the use of arrays; **write values into and read values from an array using iteration**, explicitly *including nested iteration* and *including the use of variables as indexes*. That last phrase is the syllabus quietly stating the whole idea: the point of an array is an index that a program computes.
- The syllabus states plainly that **the first index can be zero or one** — so a question will tell you, and reading the declaration is the whole job.
- **Error-identification questions on array code are standard**, and the planted errors are array-shaped: a declared type that cannot hold the data (a names table declared `OF REAL`), a counter initialised outside the lower bound, a loop that runs past the upper bound.
- Also examined: how to stop the number of stored elements exceeding the array's size, and how to make output stop when the *data* ends rather than when the *array* does — both of them the "an array doesn't know how full it is" problem from Example 3.
- **Records are not on 0478.** Where A-Level would declare an array of records, IGCSE uses parallel arrays or a 2D array — worth knowing so the fragility of parallel arrays gets taught, since the fix is off-syllabus.
- 0478 Paper 2 answers must be given in **pseudocode**, and a correct program-language solution scores nothing outside the scenario question — a board-specific hazard covered in [[Cambridge Pseudocode]].

### AP CSA (Java)

Unit 4: **§4.3 array creation and access** (`int[] a = new int[10]`, literals, and `.length` as an attribute — no brackets, unlike `String.length()`), **§4.4 traversals** (indexed `for` and the enhanced for-each), **§4.5 array algorithms**, and **§4.10/§4.13 2D arrays** (`int[][]`, row-major and column-major traversal). One free-response question is always 2D arrays and another is always `ArrayList`.

Java differences worth flagging: arrays are strictly **0-based** with no choice, `.length` is fixed at creation, and out-of-bounds throws `ArrayIndexOutOfBoundsException` rather than corrupting memory. `ArrayList` is the growable version — the doubling trick above, wrapped in an object.

### IB Computer Science

Arrays sit in **B2.2 data structures** alongside lists. IB emphasises *choosing* a structure and justifying it against alternatives rather than the low-level layout, so the trade derived above — constant-time access bought with fixed length and a uniform type — is exactly the material an IB answer wants.

### Where this is *not* examined

Neither Cambridge board examines memory addresses, cache behaviour, or the amortised cost of a growing list — the address formula here is the *explanation*, not a mark scheme. Multi-dimensional arrays beyond 2D appear on none of the four boards. Records are 9618-only; dynamic arrays are AP-only.

> [!info] Beyond syllabus — the array is the substrate of numerical computing
> Everything above scales up unchanged into the tooling behind modern science and machine learning. A **tensor** is an array with more indices; a NumPy array or a PyTorch tensor is one contiguous block plus a small table of *strides* — literally the multipliers in the address formula, stored so the same block can be read as a matrix, its transpose, or a slice, with **no data copied at all**. Transposing a large matrix in NumPy costs nothing because it just swaps two numbers in that table. And a GPU is, in the most useful one-line description, a machine built to apply the same operation to every element of an enormous array at once — which is only possible because "every element" is uniform, evenly spaced and computable-by-index. The three restrictions that looked like limitations at IGCSE are the exact reason the hardware can be built.

> [!info] Beyond syllabus — indexing by things that aren't numbers
> The array's one weakness is that the index must be an integer in a known range. Wanting `stock["apples"]` leads to the **associative array** — dictionary, map, hash table — which keeps the $O(1)$ promise by *computing a number from the key* with a hash function and then indexing an ordinary array with it. Python's `dict` and Java's `HashMap` are this. It is a beautiful move: rather than abandoning the address formula, it manufactures an index so the formula still applies.

## Connections

- **Built on:** [[RAM and the Memory Hierarchy]] — the flat sea of equally-reachable numbered cells that makes $\text{base} + i \times \text{size}$ worth computing, and the locality of reference behind row-major order.
- **Enables:** [[Searching]] — linear search traverses one; binary search *needs* the $O(1)$ jump to the middle that only indexing provides. [[Sorting]] — every comparison sort here swaps elements by index.
- **Disciplined into:** [[Stacks and Queues]] — a stack is this plus one integer, a queue this plus two; the pointers are array indices.
- **Contrast:** [[Linked List]] — what you get by refusing the contiguity: order stored as pointers instead of location, trading constant-time access for constant-time insertion.
- **Cost model:** [[Big-O Notation]] — the $O(1)$ access assumption every array algorithm's analysis rests on.
- **Exam dialect:** [[Cambridge Pseudocode]] — `DECLARE`, bounds, and the single-bracket 2D form.
- **Maths bridge:** [[Matrix]] — a 2D array is how a matrix is stored; row-major order is why matrix libraries care which index runs fastest.
- **Where the leak leads:** [[Operating Systems]] — memory protection as the wall that contains an out-of-bounds write once the array's own bounds have failed.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\text{base} + (i-l)\times\text{size}$ | `\text{base} + (i-l)\times\text{size}` | the address of element $i$; $l$ is the lower bound |
| $O(1)$ | `O(1)` | constant time — the array's defining property |
| $u - l + 1$ | `u - l + 1` | number of elements from the bounds; the $+1$ is the fence-post |
| $r \times n_{\text{cols}} + c$ | `r \times n_{\text{cols}} + c` | flattened index of a 2D element in row-major order |
