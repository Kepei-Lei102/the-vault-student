---
chinese: 哈希表 (hāxībiǎo)
prerequisites:
  - "[[Arrays]]"
  - "[[Linked List]]"
  - "[[File Handling]]"
  - "[[Big-O Notation]]"
leads_to:
  - "[[Graphs]]"
  - "[[NoSQL and Distributed Data]]"
  - "[[Encryption]]"
  - "[[File Processing and Exception Handling]]"
tags:
  - subject/computer-science
  - domain/data-structures
  - level/A-Level
  - curriculum/Cambridge-9618
  - syllabus/9618-19-1
  - syllabus/9618-13-2
  - type/deep
  - misconception/hashing-is-encryption
  - misconception/collisions-mean-broken
  - misconception/hash-tables-always-o1
  - misconception/delete-just-empties-the-slot
---

# Hash Tables 哈希表

> *Every structure in this bay so far **searches**: the list walks, the tree halves. Only [[Arrays]] never searched — it **calculated**, `base + i × size`, straight to the cell — but only if you knew the position number. [[Linked List]] closed with an engineer's dream: give up reach-by-position, ask for reach-by-**key**, and the impossible trade becomes buyable. This card buys it. The trick is one sentence: **stop storing the key's location — manufacture it.***

## 中文锚点

快递驿站有一条上架规矩：包裹按手机号的后两位上架，尾号是 28，包裹就在 28 号格。所以店员从来不用“找”：看一眼你的手机号，算出是哪一格，直接走过去，在那一格的几件包裹里翻一下就拿到了。驿站里有一百件包裹还是一百万件，花的时间都一样，因为从头到尾没有人需要记住你的包裹放在哪儿：它的位置是用你手里的这个键算出来的。这就是哈希表：一条把每个键变成位置的规则，于是“查找”变成了“计算”。这条规则唯一防不住的情况，是两个人的尾号后两位相同。格子只有一百个，顾客远远不止一百个，所以同格不是运气不好，而是必然会发生的事；凡是这一类办法，都得决定两件包裹要进同一个位置时怎么办。这家驿站的办法是一格放好几件，店员在里面翻一翻。

### 术语对照 (Terms)

| English | 中文 | one-line meaning |
|---|---|---|
| hash function | 哈希函数 | the key-to-index recipe — the exam's own is `key MOD 100` |
| hash table | 哈希表 | an array whose indices are manufactured from keys |
| collision | 碰撞 | two keys, one index — guaranteed by pigeonholes, not a failure |
| bucket row / overflow / probing | 桶行 / 溢出区 / 线性探测 | the three ways real systems absorb collisions |
| tombstone | 墓碑 | probing's deletion marker — the slot that must not be emptied |
| load factor $\alpha$ | 装填因子 | fullness = items / slots; the dial performance hangs on |
| rehash | 重哈希 | double the slots, re-scatter everything — how a dict grows |
| dictionary (ADT) | 字典 | the promise: store by key, fetch by key — this card is its engine |

## The problem, before the tool

Put the bay's whole story in one table one last time. The array reaches cell $i$ in $O(1)$ — *by calculating* — but only understands position numbers. The linked list and the trees reach things by walking or halving: $O(n)$ or $O(\log n)$, every single time, because they **search**. And what your program actually holds is almost never a position number — it is a **key**: a student ID, a word, a username. Every lookup so far has been a negotiation between the key you have and the position the machine wants.

The hunter's question: the array's $O(1)$ came from a *formula* — address = base + index × size. The formula needed an index. **What if the index itself came from a formula?** Feed the key into a function, get an index out, and the lookup collapses into the array's oldest trick:

**Don't store where things are. Calculate where they must be.**

That function is the **hash function**, the array underneath is the **hash table**, and one worked example carries the whole idea. The exam's own hash function is `Hash(key) = key MOD 100`, over a 100-row table. Where does record 528 live? $528 \bmod 100 = 28$ — row 28, computed in one step, no walking, no halving, whether the table holds ten records or ten million. Finding it again is the *same* calculation. Average cost $O(1)$: the [[Big-O Notation]] class the whole bay has been climbing toward.

![[hash-tables-funnel.svg|720]]

What makes a hash function good is exactly what makes `MOD` a sensible school choice: **deterministic** (same key, same index, forever — the whole scheme dies without this), **fast** (it runs on every operation), and **spreading** (keys should scatter evenly across the rows, not pile up). For string keys the naive recipe — add up the character codes, then `MOD` — is deterministic and fast but fails the third test in a way worth savouring: addition doesn't care about order, so **`listen` and `silent` hash identically, always** (both land on 55 in a 100-slot table — every anagram is a guaranteed pile-up). Real string hashes fix it by making position matter: multiply the running total by a constant before each new character, so `ab` and `ba` part company. Same three tests, better mixing.

## Collisions — not a failure, a certainty

A hash table has finitely many rows and the keys are effectively unlimited, so **two keys sharing an index is guaranteed by the pigeonhole principle** — the only questions are *when* and *what to do*. And "when" comes shockingly early: this is the birthday paradox from [[Probability Basics]] wearing a lab coat. With 100 slots, random keys have a better-than-even chance of a collision by the **13th insertion** (56%, machine-checked) — not the 50th. A collision policy isn't a contingency plan; it is half the data structure.

Real systems have settled on three families of answer — give the crowded slot room, send the latecomer elsewhere, or slide to the next free slot. All three run the world; Cambridge has now put each of them on a paper.

![[hash-tables-collisions.svg|740]]

**Policy 1 — chaining (bucket rows).** Give each hash value room for *several* records: hang a growable chain off every slot. This is industry's default answer — Java's `HashMap` hangs a [[Linked List]] off each slot (and quietly converts a chain into a tree when it passes eight — the [[Balanced Trees]] machinery as a safety valve); a dynamic array per slot works just as well, growing exactly as long as its pile needs, at the usual amortised price. The exam's version fixes the chain length instead: the November 2025 Paper 41 table is two-dimensional, `HashTable[100][10]` — each hash value owns a *row* of ten slots; insert walks along its row to the first free slot, find walks the same row comparing keys, and the question's "you can assume no more than 10" clause is the contract making the fixed row safe.

**Policy 2 — the overflow area.** Keep the main table one slot per hash value; when a slot is taken, put the newcomer in a separate spill zone. This is how **hashed files on disk** have handled it for decades — a full block sends its latecomers to an overflow block, the file-shelf story below. The June 2025 Paper 42 shape is exactly this in miniature: a 1D table plus a `Spare` array. Simple, and honest about its cost: every unlucky lookup now searches the *entire* overflow area linearly — fine while it stays short, degrading toward $O(n)$ as it fills.

**Policy 3 — linear probing (open addressing).** No second structure at all: if slot $h$ is taken, try $h+1$, then $h+2$, wrapping round with `MOD` — the [[Stacks and Queues]] ring trick, reused — until a free slot appears. The table *is* everything, which is why cache-loving implementations choose it — **Python's own `dict` is open addressing**, so every lookup you have ever written in Python probed this way. It is also the shape the theory paper expects you to describe, and it carries two famous costs: occupied slots form **clusters** that grow and merge, so one collision breeds more; and deletion holds a genuine trap, worth its own paragraph.

> [!warning] Probing's deletion trap — the slot you must not empty
> Under probing, `find` walks from the home slot until it hits the key **or an empty slot** — empty means "if your key existed, it would have been here; stop." Now delete a key by simply emptying its slot, and every key that once probed *past* it is orphaned: the search hits your new hole, reads it as "not present", and honestly reports a lie. The repair is the **tombstone**: a marker meaning *something was here — keep walking*. Finds step over tombstones; inserts may reuse them. The bay has met this shape twice before — the popped value that stays as a ghost, the unlinked node that isn't erased — and here the ghost is finally *load-bearing*: the structure fails without it.

```python
class HashTable:                              # chaining: a list per slot
    def __init__(self, slots=8):
        self.slots = slots
        self.table = [[] for _ in range(slots)]
        self.count = 0

    def _hash(self, key):
        return key % self.slots               # the exam's own function

    def insert(self, key, value):
        chain = self.table[self._hash(key)]
        for pair in chain:
            if pair[0] == key:
                pair[1] = value               # same key: update, don't duplicate
                return
        chain.append([key, value])
        self.count += 1
        if self.count / self.slots > 0.75:    # load factor tripwire
            self._rehash()

    def find(self, key):
        for k, v in self.table[self._hash(key)]:
            if k == key:
                return v
        return None                           # honest miss

    def delete(self, key):                    # chaining deletes without tombstones
        chain = self.table[self._hash(key)]
        for i, (k, v) in enumerate(chain):
            if k == key:
                chain.pop(i)
                self.count -= 1
                return True
        return False

    def _rehash(self):                        # double, re-scatter everything
        old = [pair for chain in self.table for pair in chain]
        self.slots *= 2
        self.table = [[] for _ in range(self.slots)]
        for k, v in old:
            self.table[k % self.slots].append([k, v])
```

This engine — and a full linear-probing engine with tombstones — ran a 2,500-trial battery against Python's own `dict`: random inserts, updates, finds and deletes, every answer compared. Never a disagreement. (The probing engine's tombstone logic is exactly where naive implementations fail the battery — remove it and the fuzz catches the lie within a few trials.) The whole battery is **`hash-tables-verify.py`, committed beside this card and seeded from today's date** — run it any morning for fresh keys and the same guarantees, including the measured probe costs and the birthday numbers. The usual caution travels with it: fuzz keys are random, and **real-world keys are not** — which for a hash table is mostly *good* news (sorted arrival scatters just as evenly through `MOD`), with the one exception of an adversary crafting collisions on purpose.

![[hash-tables-see-it-run.mp4]]

## The load factor — the dial everything hangs on

How full is the table? The **load factor** $\alpha = \dfrac{\text{items}}{\text{slots}}$ is the single number that prices a hash table, and the measurement (this card's test battery, probing, 1024 slots) tells the story:

| $\alpha$ | measured average probes | theory $\tfrac12\!\left(1 + \tfrac{1}{1-\alpha}\right)$ |
|---|---|---|
| 0.25 | 1.17 | 1.17 |
| 0.50 | 1.48 | 1.50 |
| 0.75 | 2.44 | 2.50 |
| 0.90 | 4.73 | ~5.5 |

Half-full costs about a probe and a half; at 90% the clusters have merged into causeways and the "one-step" structure is quietly walking. The remedy is the **rehash**: allocate a table twice the size and re-insert everything (every index changes, because `MOD slots` changed — nothing can stay put). One expensive evening buys a long cheap era, and averaged over all operations the cost stays $O(1)$ — the same amortised argument as the array-doubling behind Python's list. Which is not hypothetical: **Python's `dict` is an open-addressing hash table that resizes when about two-thirds full**, and a dictionary lookup — the most-executed data-structure operation on Earth, running under every attribute access and every module import — is this page's calculation.

So the honest Big-O row, stated like the merchant the bay has trained: **average $O(1)$** for insert, find and delete, resting on two assumptions (a spreading hash function, a controlled load factor); **worst case $O(n)$**, when every key lands in one slot — a terrible hash function, or an adversary choosing keys on purpose (a real attack class; real languages randomise their string hashes against it).

## The dictionary — the promise this engine keeps

Step back up to the ADT level, because the syllabus asks for it by name. A **dictionary** is a promise, in the bay's standard form: *store values under keys; fetch, update and delete by key; no order promised.* Nothing about hashing appears in the promise — hashing is the **engine**, and §19.1d's phrasing ("demonstrate how a dictionary can be implemented from appropriate built-in or other ADTs") is asking for exactly what this card has built: **an array for the slots, linked lists for the chains, a hash function as the address-manufacturer**. Two structures the bay already owns, welded by one formula. Python's `dict`, Java's `HashMap`, JavaScript's objects are all this promise kept by this engine — and [[Compilers and Interpreters]]' own identifier table, where a compiler looks up every variable name you ever wrote, is a dictionary doing its day job.

**What the $O(1)$ costs: order.** A good hash function *scatters* — that is its virtue — so the table has no first, no next, no in-between. No sorted readout, no range queries, no "all keys from 17 to 74": walking a hash table visits keys in hash-scramble order. This is the final panel of the bay's trade gallery: [[Balanced Trees]] sells *order* at $O(\log n)$; the hash table sells *speed* at $O(1)$ and cannot sell order at any price. (Python's `dict` remembering insertion order since 3.7 is a separate bookkeeping list riding alongside the table — the welded hybrid [[Linked List]] promised — not the hash finding manners.)

## Hashing on disk — §13.2's file shelf

The same idea, one level down, is the syllabus's file-organisation story. A file of records can be shelved three ways:

- **Serial** — records appended in arrival order. Writing is trivial; finding one record means reading from the top: the file-world linked list.
- **Sequential** — records kept sorted by a key field. Batch jobs that process everything in key order fly; finding one record still means scanning (or maintaining an index).
- **Random (direct)** — *a record's position in the file is computed from its key by a hashing algorithm*: hash the key, get a block address, read that block. **One seek, one read** — the hash table stretched onto [[File Handling]]'s permanent shelf, which is why §13.2's own words ask you to "describe and use hashing algorithms to read and write data to a random file".

Access follows organisation: serial and sequential files are read sequentially; random files directly; a sequential file can also be accessed directly if an index or hash maps keys to positions. Choosing is the same trade as in memory: **the payroll run that touches every record wants sequential; the ATM that needs *your* record now wants hashed.** Collisions exist on disk too — a block fills and the record goes to an overflow area, which is exactly the June 2025 `Spare` policy wearing a filesystem coat.

## Worked examples — the two real Paper 4 shapes

### Example 1 (November 2025 Paper 41 Q3 — bucket rows, the full build)

> Records (`Key : Integer`, `Data : String`) are stored in a 2D array `HashTable[100][10]`. The hash value is `key MOD 100`; colliding records take the next space in the same row (at most 10 per row, given). Write: the `Record` class, `InitialiseHashTable()`, `Hash()`, `InsertData()`, and `GetRecord()` — plus `ReadData()`, which loads 200 `key,string` lines from a file.

*Tool: the engine above, reshaped to the paper's contract.* The parts that carry the marks:

```python
class Record:                               # (a) public attributes
    def __init__(self, Key, Data):
        self.Key = Key                      # Integer
        self.Data = Data                    # String

HashTable = []                              # global table

def InitialiseHashTable():                  # (b) 100 independent rows
    global HashTable
    HashTable = [[None] * 10 for _ in range(100)]

InitialiseHashTable()

def Hash(Key):
    return Key % 100                            # (c) the paper states the formula

def InsertData(NewRecord):                      # (d) hash once, then walk the ROW
    Row = Hash(NewRecord.Key)
    for i in range(10):
        if HashTable[Row][i] is None:           # first free space in that row
            HashTable[Row][i] = NewRecord
            return

def GetRecord(Key):                             # (f) same walk, comparing keys
    Row = Hash(Key)
    for i in range(10):
        if HashTable[Row][i] is not None and HashTable[Row][i].Key == Key:
            return HashTable[Row][i].Data
    return "Not found"                          # the paper specifies this exact string

def ReadData():                             # (e) key,string on each line
    with open("HashTableData.txt", encoding="utf-8") as source:
        for line in source:
            key, data = line.rstrip("\n").split(",", 1)
            InsertData(Record(int(key), data))
```

The recurring joints: **hash once, store the row, then loop the row** (recomputing the hash inside the loop is the classic flapping answer); the free-slot test against the null record; and `GetRecord` needing *both* conditions — slot occupied **and** key matching — because a row holds several keys by design. `ReadData()` is [[File Handling]]'s lifecycle verbatim: open, read each line, `split(",")` into key and data, construct, insert, close. The audit checks this displayed code with a 200-record fixture, collisions through the last bucket position, reinitialisation and absent-key searches. The miss result must be exactly `"Not found"`, as the question specifies; an empty string is a different contract.

### Example 2 (June 2025 Paper 42 Q2 — the overflow area)

> A 1D hash table stores records; the hash is `key MOD` table size. `InsertIntoHash()`: compute the index; **if the slot is empty, store there; otherwise store in the array `Spare`** (assume `Spare` never fills). [6]

*Tool: the same skeleton, different collision clause.* The six marks split across: the function header taking the record; calling `Hash()` (not re-deriving it); the empty-slot test; the store-in-place branch; the overflow branch appending to `Spare`'s next free element (which needs its own free-slot walk or counter); and keeping the two branches *exclusive*. The comparison with Example 1 is the exam's real lesson: **the hash-and-test skeleton is identical; only the "else" differs.** Learn the skeleton once, read each paper's collision clause fresh.

### Example 3 (theory shape — trace, and the deletion question)

> A table has 10 slots, hash = `key MOD 10`, linear probing. Insert 42, 17, 27, 12. State where each is stored. Then explain why deleting 17 by clearing its slot breaks the table.

*Tool: probe, wrap, and the tombstone argument.* 42 → slot 2. 17 → slot 7. 27 → slot 7 **taken** → probe 8. 12 → slot 2 **taken** → probe 3. Now clear slot 7 and search for 27: it hashes to 7, finds the slot *empty*, and stops — reporting 27 absent while 27 sits in slot 8. The empty slot is `find`'s stop signal, so deletion must leave a **tombstone** ("occupied-but-deleted: keep walking") instead of a hole. Writing those two sentences — *empty means stop; a hole created by deletion lies* — is the whole mark.

## Common Misconceptions (Teaching Notes)

### 1. "Hashing is encryption"

Different job, different promise. A table hash must be *fast* and *spreading*; nobody cares that `MOD 100` is trivially reversible-ish, because secrecy was never the point — **finding things is**. Cryptographic hashes (SHA-256 and family) must be irreversible and collision-*resistant* against an adversary, and are thousands of times slower — the resisting-noise vs resisting-an-opponent split [[Error Detection and Correction]] draws, on the same word. Password storage uses the cryptographic kind; your `dict` uses the fast kind; calling both "hashing" is the language being economical, not the ideas being the same.

### 2. "A collision means the hash function is broken"

Collisions are **guaranteed** — pigeonholes: unlimited keys, finite slots. With 100 slots, thirteen random keys already make a collision more likely than not. A good function makes collisions *rare and scattered*; only a policy makes them *survivable*. An exam answer that treats collisions as an error state has missed the design: the collision policy is half the structure.

### 3. "Hash tables are O(1), full stop"

Average $O(1)$, resting on a spreading function and a controlled load factor — and **worst case $O(n)$** when either assumption dies. Let the load factor crawl toward 1 and probing degenerates into a linear scan wearing a formula; give an adversary your hash function and they can *manufacture* the worst case. The examiners' phrase "with reference to efficiency" wants the average-case claim *with its fine print attached*.

### 4. "To delete under probing, just empty the slot"

The trap in Example 3: an empty slot is the probe sequence's stop signal, so a deletion-hole truncates every search path that ran through it — the table then lies about keys it still holds. Tombstones fix it; chaining never suffers it (deletion is just a list-removal, the [[Linked List]] move). Knowing *which policy has the trap* is the discriminating mark.

### 5. "The table keeps things in some order"

Scatter *is the mechanism*. There is no first, no next, no range — iterate a raw hash table and keys emerge in hash-scramble order, which changes when the table rehashes. Need sorted output or ranges? That is [[Balanced Trees]]' product, sold at $O(\log n)$. Python's insertion-ordered `dict` keeps a separate order list beside the table — a welded hybrid, not an ordered hash.

## Where this runs the world

The strongest claim available: **the hash lookup is the most-executed data-structure operation on Earth.** Every Python attribute access, every JavaScript property read, every module import, every HTTP header parse walks a hash table; interpreters are dictionaries in motion. One level up, **every cache is a hash table with a clock** — the DNS cache resolving this page's hostname, the CPU-adjacent caches keyed by address, a CDN keyed by URL. Databases run the idea twice: hash *indexes* for pure equality lookups, and the **hash join** — build a table from the smaller side, stream the larger side through it — as the workhorse behind `JOIN`. And [[Compilers and Interpreters]]' four stages lean on it at stage one: the identifier table mapping every name in your program to what it means is the dictionary ADT, usually hashed. The structure earned its ubiquity the honest way: almost everything a computer does begins with *find me this, by name, now*.

## Beyond the syllabus

> [!info] What a grown-up hash function looks like
> `MOD` is only the *last* step. An industrial hash function runs two stages: a **mixing stage** that stirs every bit of the key into every bit of the output, so that keys differing in one character land nowhere near each other (Java's `String.hashCode` is the multiply-by-31 polynomial from the anagram fix run to completion; MurmurHash and xxHash are the heavy-duty mixers inside databases and filesystems), then a **compression stage** that squeezes the mixed number into a table index — the `MOD`, or a single bitmask when the slot count is a power of two. The mixing is what earns the cheap compression: `MOD` alone inherits every pattern in the raw keys (all-even keys on an even table size use only half the slots — one reason old-school table sizes are prime), while a well-mixed hash makes any table size safe.

> [!info] The two-thirds rule, and the dict's private life
> CPython's `dict` is open addressing with a twist: the probe sequence mixes in the hash's high bits (a *perturbation*), so clustering stays mild even with simple hashes, and the table resizes at roughly two-thirds full. String hashing is **randomised per process** — a defence adopted across languages after 2011, when researchers showed you could nail web servers by POSTing thousands of keys crafted to collide: the worst case as a weapon, patched by making the hash function a secret.

> [!info] When you can promise no collisions at all
> If the key set is *fixed and known in advance* — a language's keywords, a chip's opcode table — you can search for a **perfect hash function**: one with zero collisions on exactly that set, letting the table run at $\alpha = 1$ with no policy at all. Compilers and assemblers ([[Assembly Language]]'s mnemonic lookup) do exactly this. The general problem allows no such luck; the fixed-set special case is a reminder that the pigeonhole argument needs *unbounded* keys.

> [!info] The set, for one line
> Keep the keys and drop the values and the same engine implements the **set** ADT — membership at $O(1)$ — which is Python's `set`, and the reason `x in huge_set` is instant while `x in huge_list` crawls. One engine, two promises.

## Exam Notes

### Cambridge 9618

The hash table lives on **three papers**:

- **Paper 4 (practical), the §19.1d dictionary made real:** the two most recent seasons are Examples 1 and 2 — build the table (2D bucket rows in November 2025; 1D + `Spare` overflow in June 2025), write `Hash()` from a stated formula (always `MOD` so far), insert with the paper's collision clause, retrieve by key, and load records from a text file ([[File Handling]]'s lifecycle inside a hash question). The recurring joints: hash once then loop; test the null record; match on *key*, return *data*.
- **Paper 3 (theory), §13.2:** file organisation (serial / sequential / random) and access methods, with hashing as the mechanism of **direct access** — describe a hashing algorithm, explain collisions and an overflow strategy, and *select with justification* the right organisation for a scenario (batch-everything → sequential; one-record-now → random/hashed).
- **§19.1d's own words** — "demonstrate how a dictionary can be implemented from built-in types or other ADTs" — are this card's array-plus-chains build; with it, every named structure in that learning objective now has its implementation demonstrated.
- Note the boundary: §19.1c's *write find/insert* list names linked list and binary tree, **not** the dictionary — the dictionary's algorithms are examined through Paper 4's practical shapes rather than P3 prose.

### IB Computer Science (first assessment 2027, higher level)

- **B4.1.6, "Explain the core principles of ADTs"**, names "the underlying mechanics of hash tables, including hashing functions, collision resolution strategies and load factors", then the mechanics of sets, and `dict` and `set` in Python (`HashMap` and `HashSet` in Java). All three are taught above: the hash function under "The problem, before the tool", the strategies under "Collisions", and the load factor under its own heading. B4.1.5 asks separately for the set as an ADT, with its operations in code.

### Not examined

- **Cambridge 0478** — no hashing anywhere (its nearest neighbour is the file topic, unhashed).
- **AP CSA** — `HashMap` is outside the tested Java subset; a CSA student meets this card at university.

## Connections

- **Builds on:** [[Arrays]] — the calculate-don't-search trick, now with manufactured indices, plus the amortised-doubling argument rehashing borrows; [[Linked List]] — the chains hanging from each slot, and the engineer's-dream callout this card cashes in full; [[File Handling]] — the text-file lifecycle inside every Paper 4 hash question, and the shelf §13.2 hashes onto; [[Big-O Notation]] — average vs worst case, stated with fine print.
- **Leads to:** [[Graphs]] — the bay's last structure: loosen every constraint and only connections remain (and adjacency lists are dictionaries of neighbours).
- **Kindred:** [[Balanced Trees]] — the counterpart product: order at $O(\log n)$ vs speed at $O(1)$, the bay's closing trade; [[Stacks and Queues]] — the MOD ring reused as probing's wrap, and the ghost lesson graduating into the load-bearing tombstone; [[Compilers and Interpreters]] — the identifier table as the dictionary's day job; [[Error Detection and Correction]] — the other meaning of "hash", and the noise-vs-adversary split; [[Probability Basics]] — the birthday paradox pricing the first collision.

## LaTeX Reference

| symbol | LaTeX | meaning here |
|---|---|---|
| $\alpha = n / m$ | `\alpha = n / m` | load factor: items over slots |
| $\tfrac12\left(1 + \tfrac{1}{1-\alpha}\right)$ | `\tfrac12\left(1 + \tfrac{1}{1-\alpha}\right)` | expected probes for a successful probing lookup |
| $O(1)$ average, $O(n)$ worst | `O(1)`, `O(n)` | the honest pair, fine print included |
