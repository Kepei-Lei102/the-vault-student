---
chinese: 二叉树 (èrchāshù)
prerequisites:
  - "[[Arrays]]"
  - "[[Linked List]]"
  - "[[Searching]]"
  - "[[Recursion]]"
leads_to:
  - "[[Heaps and Priority Queues]]"
  - "[[Graphs]]"
  - "[[Balanced Trees]]"
tags:
  - subject/computer-science
  - domain/data-structures
  - level/A-Level
  - curriculum/Cambridge-9618
  - syllabus/9618-19-1
  - curriculum/IB-CS
  - syllabus/IB-CS-B4-1
  - type/deep
  - misconception/binary-tree-equals-search-tree
  - misconception/left-child-smaller-is-enough
  - misconception/trees-are-automatically-log-n
  - misconception/in-order-means-insertion-order
  - misconception/null-is-always-minus-one
---

# Binary Trees 二叉树

> *[[Searching]] ended on a bargain and a catch: binary search finds one name among a million in twenty comparisons — but only in a sorted **array**, and [[Arrays]] charges a million-cell shuffle to insert one name into it. [[Linked List]] fixed the insert for two writes — and lost binary search, because halving needs to* jump to the middle *and a chain can only walk. Twenty comparisons or two writes: every structure so far made you choose. This card is about the shape that refuses to choose — and the price it quietly asks instead.*

## 中文锚点

排序数组查得快（二分查找，一百万个数二十次比较）但插入贵（要整体搬移）；链表插入便宜（改两个指针）但查得慢（只能一格格走，**就算有序也没法“跳到中间”**）。二叉搜索树是那个“两样都要”的结构，而它的核心想法出奇地简单：注意到**二分查找每次问的问题其实是固定的**——第一次永远比较中间那个数，答“更小”之后第二次永远比较左边四分之一处那个数——既然这张“决策地图”从不改变，那就把它**存下来**：每个节点带两个指针，“更小”往左走，“更大”往右走。**二叉搜索树就是被冻结成指针的二分查找。**于是查找是 $O(\log n)$（每比较一次就扔掉整整一棵子树），插入只是“走到空位、写一个指针”。但有个代价：**查找的成本等于树的高度，而树的形状由数据到来的顺序决定**——乱序到来，树是茂密的，一百万个数二十层；**按顺序到来，树退化成一条斜线，变回它本想打败的链表**。最后一个漂亮的结论：**中序遍历（左—根—右）输出的恰好是排好序的数据**——所以这棵树等于一个“随时可以便宜插入的有序数组”，这正是前两张卡片证明过“不可能免费拥有”的东西，而账单就是上面那条平衡假设。

| English | 中文 | one-line meaning |
|---|---|---|
| tree | 树 | a structure of forks: every node points onward to children |
| binary tree | 二叉树 | each node has **at most two** children — a left and a right |
| binary search tree (BST) | 二叉搜索树 | 二叉树 + 排序规则：左子树**全部**更小，右子树**全部**更大 |
| root | 根节点 | the one node everything starts from (drawn at the **top**) |
| leaf | 叶节点 | a node with no children — the chain's −1/null twice over |
| parent / child | 父节点 / 子节点 | one hop up / one hop down |
| subtree | 子树 | any node plus everything below it — a tree inside the tree |
| height | 高度 | the longest root-to-leaf path — **the price of every search** |
| traversal | 遍历 | visiting every node in a promised order(中序遍历出来就是排好序的) |
| balanced / degenerate | 平衡 / 退化 | bushy and shallow / a spine that is secretly a linked list |

## The problem, before the tool

Two cards ago the trade table was honest and grim. The sorted array answers "is `Kk` in the collection?" in $O(\log n)$ — binary search halves what's left with each comparison, and [[Big-O Notation]] priced how absurdly well that scales. But it pays for that with the million-shift insert: order stored as location, so one new item moves everything after it. The linked list inverted the deal: insert is two pointer writes, but *finding where to write* costs an $O(n)$ walk — **even when the list is sorted**, because binary search's whole trick is jumping to the middle, and a chain has no middle to jump to, only a next.

Ask the hunter's question of binary search itself: when it runs on the same sorted array over and over, **what stays the same between runs?** Everything. The first comparison is always against the same middle element. If the answer is "go left," the second comparison is always against the same quarter-point. The entire *decision map* of binary search — first ask here, then ask there — is fixed the moment the data is; only the answers differ per target. A map that never changes is begging to be **built once and stored**.

So store it. Give every element a pointer to the element you'd compare against next on a "smaller" answer, and another for a "larger" answer. The middle element becomes the start. The quarter-points hang off it. What you have built is binary search's decision map made out of [[Linked List]]'s honest primitive — and it has a name.

**A binary search tree is binary search, frozen into pointers.**

And because it is made of pointers, it inherits the pointer's gift: inserting a new element is, as always, a matter of *wiring, not moving*. Order without geography, and $O(\log n)$ search anyway. The catch — there is a catch — comes later, and it is the best lesson in the card.

## Anatomy — the chain forks

[[Linked List]] ended one sentence short of this card: a node with **two** next-pointers — call them `left` and `right` — is no longer a chain but a fork, and a structure of forks is a **tree**.

The vocabulary is a family portrait drawn upside down, because computing's trees grow downward — the botany is the mnemonic's only casualty. The **root** is the single node at the top, the one address from which everything is reachable (the head pointer's heir). Each node points down to at most two **children**; the node above is its **parent**; a node with no children is a **leaf**, its two pointers both null. Any node, taken with everything below it, is a **subtree** — a tree in its own right, which single fact is why [[Recursion]] and trees fit each other like a key in a lock. The **height** is the longest walk from root to leaf. A **binary tree** is any tree that keeps to the at-most-two rule.

A **binary search tree** adds the promise that makes it a search instrument:

> At **every** node: everything in the **entire left subtree** is smaller than the node; everything in the **entire right subtree** is larger.

Read that carefully, because the exam reads it carefully. The rule is not "the left *child* is smaller" — it is the **whole subtree**, every node all the way down. A tree can satisfy the child-by-child version and still be broken: put 25 as the right child of 10, under a root of 20, and each parent-child pair looks fine locally (25 > 10 ✓) while 25 squats illegally in 20's left subtree. The promise is global on the subtree, and it is exactly what makes search work: one comparison at the root doesn't discard a *node*, it discards an entire **subtree** — half the world, in one question, without looking at it.

![[binary-trees-anatomy.svg|720]]

> [!info] One node more than edges — structural induction's home turf
> Recall from [[Proof by Induction]] that any recursively built world supports induction on *shape*: prove the claim for the atoms, prove each construction rule preserves it. Claim: **every non-empty binary tree has exactly one more node than it has edges.** Atom: a lone leaf has 1 node, 0 edges — holds. Construction: a tree is a root plus up to two subtrees, each attached by one new edge; if each subtree has $n_i$ nodes and $n_i - 1$ edges, the whole has $1 + \sum n_i$ nodes and $\sum ((n_i - 1) + 1) = \sum n_i$ edges — one apart, always. No tree of any shape or size escapes, and nobody checked them one by one. That is structural induction earning its keep on the simplest honest example.

## Insert — walk to a null, write once

To insert, play the search you are freezing: compare, go left or right, repeat — until the pointer you would follow is null. That null *is* the vacancy; the new node's address overwrites it. One write. (The bay's rule of thumb survives a third structure: **change is pointer-wiring, never moving.**)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None          # a leaf is two Nones

class BST:
    def __init__(self):
        self.root = None           # empty tree: the root points nowhere

    def insert(self, data):
        if self.root is None:      # first node IS the root
            self.root = Node(data)
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)   # the null was the vacancy
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(data)
                    return
                current = current.right
```

Run it on five values — `20, 10, 26, 22, 8`, in that order. 20 arrives first and is the root. 10 is smaller: left child of 20. 26: right child of 20. 22 is larger than 20, smaller than 26: left child of 26. 8: left, then left again — left child of 10.

```
            20
           /  \
         10    26
        /     /
       8    22
```

**The order of arrival decides the shape.** Those same five values inserted as `8, 10, 20, 22, 26` produce no bush at all — each value is larger than everything before it, every insert turns right, and the "tree" is a right-leaning spine: a linked list wearing a tree's clothes. Same data, same code, different arrival order, different structure. Hold that thought; it is the catch.

![[binary-trees-two-orders.svg|720]]

## Find — every question discards a subtree

Search is the same walk with a different exit condition:

```python
    def find(self, target):
        current = self.root
        while current is not None:
            if target == current.data:
                return True
            if target < current.data:
                current = current.left     # everything right of here just vanished
            else:
                current = current.right    # everything left of here just vanished
        return False                       # walked off a leaf: not present
```

*Tool: the subtree promise.* Each comparison sends the walk down one child and — this is the entire point — **legitimately ignores the other child's whole subtree**, because the promise guarantees the target cannot be there. One question, half the remaining world gone. That is binary search's halving, reborn out of pointers; the walk from root to wherever the search ends is exactly the sequence of middles binary search would have probed.

So what does a search cost? One comparison per level: **the cost of every find and every insert is the height of the tree.** The structure has no other price. Which makes the next question the only one that matters.

## The height is the price

How tall is a binary tree holding $n$ items? **It depends who built it** — and the honest answer is the card's centre of gravity.

**Best case — balanced.** If every level is full before the next begins, each level doubles the capacity: 1, 2, 4, 8… A tree of height 20 holds $2^{20} - 1 \approx 1\,000\,000$ nodes. Read backwards: **a million items, twenty comparisons** — the $O(\log n)$ that [[Searching]] promised, now with two-write inserts attached. Both bills paid at once.

**Worst case — degenerate.** Feed the tree already-sorted data and every insert turns the same way, as the five-values demo showed. Height $n$, every search a full walk: $O(n)$. The structure built to beat the linked list has *become* the linked list — plus an unused pointer per node as decoration. There is something almost moral about the failure mode: the BST extracts its speed from the **disorder** of its input; hand it perfectly ordered data — the one input that looks most helpful — and you starve it of the randomness it feeds on.

**Typical case.** Random arrival order gives height within a small constant of $\log_2 n$ (a seeded run in this card's test battery: 1023 keys in random order → height 25, against the perfect 10 and the catastrophic 1023). Good enough for real work, never guaranteed. The guarantee can be *bought* — trees that rebalance themselves as they insert — and [[Balanced Trees]] sells three versions of the contract, prices included.

| operation | balanced BST | degenerate BST | sorted array | linked list |
|---|---|---|---|---|
| find | $O(\log n)$ | $O(n)$ | $O(\log n)$ | $O(n)$ |
| insert (once found) | $O(\log n)$ | $O(n)$ | $O(n)$ — the shuffle | $O(1)$ — two writes |
| read out in order | $O(n)$ — in-order walk | $O(n)$ | $O(n)$ — already there | $O(n)$ if kept sorted |

The justify-the-choice sentence the table compresses: **choose a BST when the collection must stay ordered *and* keeps growing** — a sorted array wants data that arrives once and is searched forever; a linked list wants change without search; the tree is for the collection that must do both, and its fine print is the balance assumption.

## The exam's engine — a tree built out of arrays

§19.1d's discipline, third time around: an ADT is a *promise*, and any machinery that keeps the promise is a legal implementation. The Python classes above are one engine. Cambridge's Paper 4 engine is the same one that ran the stack, the queue and the linked list — **arrays and integers**, because an exam must run on paper.

One 2D array, `BinaryTree[0..99][0..2]`, each row one node: `[left pointer, data, right pointer]`, where a pointer is *an array index* and **−1 is the null** (the [[Stacks and Queues]] keystone, fourth appearance: a valid index can be 0, so "nowhere" must be a number no index can be). Two global integers steer it: `TreeRootPointer`, the index of the root (−1 while the tree is empty), and `FirstFreeNodePointer`, the index of the next unused row.

The five-value tree above, as the exam prints it:

| index | left pointer | data | right pointer |
|---|---|---|---|
| 0 | 1 | 20 | 2 |
| 1 | 4 | 10 | −1 |
| 2 | 3 | 26 | −1 |
| 3 | −1 | 22 | −1 |
| 4 | −1 | 8 | −1 |

with `TreeRootPointer = 0` and `FirstFreeNodePointer = 5`. Note what the rows are: **arrival order**, top to bottom — because allocation is a bump: each new node takes row `FirstFreeNodePointer`, which then increments. The *tree* lives entirely in the pointer columns; the row order remembers only history. (Cover the pointer columns and you cannot reconstruct the tree; cover the row order and you can.)

Notice what this engine *doesn't* have: [[Linked List]]'s free list. A free list exists to recycle deleted nodes — and the 9618 tree never deletes (the syllabus asks delete for stack, queue and linked list only; the reason it spares the tree is genuinely interesting and lives in Beyond the syllabus). No deletion, no holes, no recycling: a bump pointer is a complete allocator. When `FirstFreeNodePointer` runs off the end, the tree is full — same overflow discipline, same marked guard, as every structure in the bay.

```python
BinaryTree = [[-1, -1, -1] for i in range(100)]   # all nodes initialised null
TreeRootPointer = -1
FirstFreeNodePointer = 0

def AddNode(NodeData):
    global TreeRootPointer, FirstFreeNodePointer
    if FirstFreeNodePointer > 99:                  # the full guard: a marked point
        print("The tree is full")
        return
    New = FirstFreeNodePointer                     # bump allocation
    BinaryTree[New] = [-1, NodeData, -1]           # a newborn node is a leaf
    FirstFreeNodePointer = FirstFreeNodePointer + 1
    if TreeRootPointer == -1:                      # empty-tree guard: first node is root
        TreeRootPointer = New
        return
    Current = TreeRootPointer
    while True:                                    # the frozen binary search
        if NodeData < BinaryTree[Current][1]:
            if BinaryTree[Current][0] == -1:
                BinaryTree[Current][0] = New       # parent's left now names the newcomer
                return
            Current = BinaryTree[Current][0]
        else:
            if BinaryTree[Current][2] == -1:
                BinaryTree[Current][2] = New
                return
            Current = BinaryTree[Current][2]
```

This code and the class version were run head-to-head through a 3000-trial battery — random data in, every find answer compared, every read-out compared — and never disagreed. Two engines, one promise, and the user of the ADT cannot tell which one is underneath: §19.1d, worn as a demonstration for the third time.

![[binary-trees-exam-engine.svg|720]]

> [!warning] The null is a convention, not a constant
> This bay has said "−1 means null" so often it can start to sound like physics. It is a *contract term*, and each paper writes its own: the same exam board that uses −1 in one paper's tree question has used **0** as the null in another's, where node indices started at 1. The first thing to read in any data-structure question is its null convention and its index range — the answer's correctness is graded against the question's contract, not the bay's habit.

## Walking the tree — traversals, and the payoff

A chain has one natural walk. A tree, at every node, has a choice: deal with the node, the left subtree, and the right subtree — *in which order?* Three sensible answers, named by where the node itself comes:

- **pre-order** — node, then left subtree, then right subtree
- **in-order** — left subtree, then node, then right subtree
- **post-order** — left subtree, right subtree, then node

Each is three lines of [[Recursion]], and this is recursion's home ground — the function's shape *is* the data's shape (a tree is "a node plus two smaller trees", so the natural procedure is "handle a node plus two recursive calls"), and the backtracking that walking a tree seems to require is done by nobody: the call stack remembers every fork for free.

```python
def in_order(node):
    if node is not None:           # the leaf's None is the base case
        in_order(node.left)        # everything smaller, first
        print(node.data)           # then me
        in_order(node.right)       # everything larger, last
```

There is a pencil version worth owning: trace the tree's outline anticlockwise from the root — the **contour walk**. Each node is passed three times: down its left flank, under its bottom, up its right flank. Emit each node at the *left flank* and you have pre-order; at the *bottom*, in-order; at the *right flank*, post-order. Three traversals, one walk, three flag positions.

Now the payoff, and it deserves its own line:

**The in-order traversal of a binary search tree emits the data in sorted order.**

It has to: at every node, in-order does everything-smaller first, the node itself second, everything-larger last — that *is* sortedness, applied recursively. (The 3000-trial battery checked in-order output against Python's `sorted()` on every trial: never a disagreement.) This is the card's opening bargain, settled in full: the BST is a structure you can insert into for two writes *and* read out sorted at any moment — **a sorted array that accepts newcomers**, which is exactly the thing the first two cards proved impossible to have for free. The fee, as the height section confessed, is the balance assumption.

The other two orders earn their keep elsewhere. **Pre-order** (node first) is the *copying* order — emit a tree pre-order, insert the values into an empty BST in that sequence, and the identical shape rebuilds, root before children. **Post-order** (node last) is the *demolition* order — children dealt with before their parent, so nothing is freed while something below it still needs the pointer. And post-order has a second life this vault has already met: draw the expression $(3+4)\times 5$ as a tree — operators as internal nodes, numbers as leaves — and its post-order reads `3 4 + 5 ×`, which is precisely the Reverse Polish Notation of [[Compilers and Interpreters]]. RPN is not a separate invention; **it is the post-order traversal of the expression tree**, which is why the compiler's stack could evaluate it without ever needing brackets.

![[binary-trees-traversal-walk.svg|720]]

![[binary-trees-see-it-run.mp4]]

## Worked examples

### Example 1 (Paper 3 shape — complete the tree, real June 2025 question)

> A linked list of nodes stores an ordered list of strings; each node is a left pointer, data, and a right pointer, organised as a binary tree. **0 is used to represent a null pointer.** The tree holds `Pp` at the root, with children `Gg` and `Rr`; `Gg`'s right child is `Kk` (its left is null). Complete the tree, **including null pointers**, after `Aa, Mm, Ss, Xx` are added. [4]

*Tool: the frozen search — walk each newcomer from the root, keep the whole-subtree promise.*

- `Aa` < `Pp` → left to `Gg`; `Aa` < `Gg`, whose left is null → **`Aa` becomes `Gg`'s left child.**
- `Mm` < `Pp` → `Gg`; `Mm` > `Gg` → `Kk`; `Mm` > `Kk`, right null → **`Kk`'s right child.**
- `Ss` > `Pp` → `Rr`; `Ss` > `Rr`, right null → **`Rr`'s right child.**
- `Xx` > `Pp` → `Rr`; `Xx` > `Rr` → `Ss`; `Xx` > `Ss`, right null → **`Ss`'s right child.**

The four placement marks are exactly those four sentences. The remaining credit is the phrase the question bolded: *including null pointers* — every childless slot on the finished drawing must show its 0, because a pointer field is never blank, only null. And note the contract: **this paper's null is 0, not −1** — the convention callout above, live in a real question.

### Example 2 (Paper 4 shape — write `AddNode`, real June 2026 question)

> The binary tree is a global 2D array of 100 nodes `[left, data, right]`, null = −1, with `TreeRootPointer` (initialised −1) and `FirstFreeNodePointer` (initialised 0). Write `AddNode()`: take the integer to store; handle the empty tree by updating the root pointer; output `"The tree is full"` when full; otherwise store the data in the next free node, walk left/right from the root to the appropriate leaf, and update the parent's pointer to the new node. [7]

*Tool: the exam engine, written above in full.* The seven marks land on recognisable joints, and the published scheme names them almost line for line: the header taking the parameter and the `FirstFreeNodePointer` increment; the empty-tree branch (store in first element, update root); the full guard with its message; storing the data with both pointers −1; comparing against the current node; repeating leftward when smaller; repeating rightward when greater; stopping at a leaf; and writing the newcomer's index into the **correct parent pointer**. That last mark is where casual answers die: the loop must remember *which* null it found — left or right of *which* node — because the one write that performs the insert happens in the parent's row, not the new node's.

### Example 3 (justify + Big-O — the §19.1 comparison question)

> A system stores customer IDs, which arrive continuously and must be searchable at all times. Compare a sorted array, a linked list, and a binary search tree for this task, using Big-O notation. [4]

*Tool: the trade table, argued not recited.* A sorted array searches in $O(\log n)$ but each arriving ID pays the $O(n)$ shuffle — wrong for continuous arrivals. A linked list inserts in $O(1)$ once positioned, but positioning — and every search — is an $O(n)$ walk. The BST does both in $O(\log n)$ **provided it stays balanced**, and the caveat is a creditworthy point, not a weakness of the answer: state that already-ordered arrivals degrade it to $O(n)$, and (for the final mark's flourish) that in-order traversal still yields the sorted listing a report would need in $O(n)$.

## Common Misconceptions (Teaching Notes)

### 1. "Binary tree and binary search tree are the same thing"

A binary tree is only the *shape rule* — at most two children. The ordering promise is extra, and it is the promise, not the shape, that buys $O(\log n)$ search. An expression tree is a binary tree with no ordering at all and no interest in being searched. On the exam, the phrase "stores data in ascending order" or "organised as a binary tree" in a linked-list costume is the signal that the search promise is in force.

### 2. "Each node just has to be bigger than its left child"

The promise binds the **entire subtree**, not the child. The counterexample to memorise: root 20, left child 10, and 25 as 10's *right* child — every parent-child pair looks legal, but 25 sits in 20's left subtree claiming to be smaller than 20. A find for 25 would turn right at 20 and honestly report *not present* while 25 sits in the building. Local correctness, global lie.

### 3. "Trees are automatically $O(\log n)$"

Balance is earned, not conferred. Sorted input builds the spine; $O(\log n)$ silently becomes $O(n)$; and no error is raised anywhere, because a spine is a perfectly legal BST. The examiner's version of this misconception is the "state a condition for the efficiency claim" mark. The engineer's version is a production database that got slower every month because IDs arrive in increasing order.

### 4. "In-order traversal means the order they were inserted"

The name refers to where the *node* comes relative to its subtrees (in between), and its output is **sorted order** — that is the whole miracle. Arrival order is a different thing, and in the exam's array engine it is visible in a different place: the row order of the table, top to bottom, because allocation bumps. One table, both histories: rows remember arrival, pointers remember order.

### 5. "Null is −1"

Null is *whatever the question's contract says* — this bay's habit is −1, and a real Paper 3 tree question has used 0 (with indexing from 1) in the same season another paper used −1. Copying a memorised convention over the question's stated one throws marks away on work that is otherwise perfect. First read of any structure question: the null value, the index range, the initialisations.

## Where trees run the world

The claim "trees are everywhere" is cheap; here is the load-bearing instance. Every serious **database index** is a tree, and every indexed query walks one. When a query asks `WHERE customer_id = 774631` against a table of a hundred million rows, the database does not scan; it descends an index in a handful of steps — the frozen-search idea at industrial scale. The production version is the **B-tree**, the BST's stocky cousin: instead of two children per node it packs *hundreds* of keys and children into each node, because the index lives on [[Secondary Storage]] and the expensive unit there is not a comparison but a **block read** — so the tree is fattened until one node is exactly one block, and a hundred million rows resolve in three or four reads. Same promise, same walk, node width set by the hardware's pricing. The directory structure a [[File Systems]] card walks, the DOM a browser renders, the parse tree inside every compiler ([[Compilers and Interpreters]] stage 2), and the Huffman coding tree already built in [[Compression]] §"Huffman coding — charge less for the common" are the same shape doing four other jobs — but the index is the one where *the tree is the product*: the entire reason your query returns in milliseconds.

## Beyond the syllabus

> [!info] Deletion — the operation the syllabus quietly spared you
> The syllabus asks deletion for stacks, queues and linked lists, but not trees, and the omission is a mercy with a lesson in it. Deleting a **leaf** is one write (null out the parent's pointer). Deleting a node with **one child** is the linked list's move (parent adopts grandchild). But deleting a node with **two children** breaks the shape: two orphaned subtrees, one vacant pointer. The classic repair is elegant — overwrite the doomed node's data with its **in-order successor** (the smallest node in its right subtree: go right once, then left to the floor), then delete *that* node instead, which by construction has at most one child and falls to the easy cases. Correct, subtle, and exactly the kind of pointer surgery where one swapped line orphans a subtree — the grip-before-relinking discipline, at tree scale. The full operation, built and fuzz-verified, opens [[Balanced Trees]].

> [!info] The tree that tidies itself
> The degenerate spine is not a fate, it is a maintenance failure — and self-balancing trees fix it with one tool: the **rotation**, a three-pointer rewrite that lifts a child over its parent while preserving the in-order sequence (the promise survives; only the shape changes). **AVL trees** (1962, the first) rotate whenever siblings' heights differ by two; **red-black trees** rotate more lazily but guarantee the same bound. Both cap the height at $O(\log n)$ *no matter what order the data arrives in* — the balance assumption converted from a hope into a contract. That is what actually sits inside the standard libraries: C++'s `std::map` and Java's `TreeMap` are red-black trees; feed them sorted data all day and they never degrade. The whole machine — the rotation, AVL's four cases, why the libraries chose red-black, and the B+ tree under every database — runs in [[Balanced Trees]].

> [!info] The heap — a binary tree with a different promise, and no pointers at all
> [[Stacks and Queues]] left a door open: the priority queue, "usually implemented as a *heap*, a structure this card is the gateway to". Step through: a **heap** is a binary tree that swaps the BST's left-right ordering for a vertical one — *every parent outranks its children* — and keeps its shape always-complete (levels filled left to right). It answers only one question, "who is most urgent?", but answers it in $O(1)$ with $O(\log n)$ maintenance. And because its shape is rigid, it needs **no pointers whatsoever**: pack the levels into a plain array and the wiring becomes [[Arrays]]-style arithmetic — node $i$'s children live at $2i+1$ and $2i+2$, its parent at $\lfloor (i-1)/2 \rfloor$. A tree stored as pure calculation: the bay's two great primitives, the pointer and the formula, meeting in one structure — [[Heaps and Priority Queues]] takes it from here.

## Exam Notes

### Cambridge 9618 — §19.1 (A2)

The tree lives in Papers 3 and 4, and the two papers ask it differently:

- **Paper 3 (theory):** draw or complete a BST after given insertions — *including null pointers*, which carry marks (Example 1 is the June 2025 shape verbatim); state the promise; trace a find; justify tree vs array vs linked list with Big-O (§19.1's comparison LO, Example 3). Read the paper's null convention — 0 and −1 have both appeared.
- **Paper 4 (practical):** write the array engine in your submitted language — §19.1c names exactly **find** and **insert** for the binary tree (deletion is *not* required for trees). The June 2026 `AddNode` (Example 2) is the canonical seven-marker; its published scheme's mark points are the joints named in the example. §19.1d asks the tree to be built "from appropriate built-in types or other ADTs" — the 2D-array engine and the class engine above are that LO's two answers, demonstrated equivalent.
- **Traversals are not in the 2027–29 learning objectives**, and no Paper 3 in this vault's corpus has asked one — but *in-order gives sorted output* remains a legitimate and strong justify-the-choice point, and the concept is assumed cultural literacy at university. Learn them; just don't expect a dedicated trace question.
- The pseudocode guide lists the binary tree among its **composite data types** — declarations follow the record-of-pointers pattern [[Cambridge Pseudocode]] documents.

### IB Computer Science (2027 course)

**B4.1 — Fundamentals of ADTs** names trees alongside stacks, queues and linked lists: expect define-the-promise, trace-an-insertion and compare-structures questions in the same style as the Cambridge theory paper, with the balance caveat as the HL-flavoured discriminator. (First assessment 2027; the paper corpus is still empty, so this section is built from the subject guide alone.)

### Not examined

- **Cambridge 0478** — no tree content anywhere in the IGCSE syllabus; its data-structures ceiling is the 1D/2D array and the file.
- **AP CSA** — the current course stops at `ArrayList` and 2D arrays; trees were dropped with the old AB course. A CSA student meets trees at university.

## Connections

- **Builds on:** [[Linked List]] — the pointer machinery, one fork per node instead of one link, and the promised buyback delivered: $O(\log n)$ search restored to a pointer structure; [[Searching]] — binary search is the algorithm this structure freezes; [[Arrays]] — the exam engine's substrate, and the row-order-vs-pointer-order double truth; [[Recursion]] — traversal is structural recursion, the call stack doing the backtracking.
- **Leads to:** [[Heaps and Priority Queues]] — the vertical promise, array-packed; [[Graphs]] — loosen "at most two children, no cycles" to "any connections whatsoever" and the map of structures completes: array → list → tree → graph.
- **Kindred:** [[Compilers and Interpreters]] — the expression tree whose post-order *is* RPN, and the parse tree of stage 2; [[Compression]] — Huffman's coding tree, a binary tree built from frequencies; [[Big-O Notation]] — the language of the height argument; [[Proof by Induction]] — structural induction, demonstrated here on nodes-vs-edges; [[Stacks and Queues]] — the −1 keystone and the overflow guard, inherited unchanged.

## LaTeX Reference

| symbol | LaTeX | meaning here |
|---|---|---|
| $O(\log n)$ | `O(\log n)` | cost of find/insert in a **balanced** BST |
| $O(n)$ | `O(n)` | the degenerate spine's price; also any full traversal |
| $2^{h} - 1$ | `2^{h} - 1` | maximum nodes in a binary tree of height $h$ |
| $\lfloor (i-1)/2 \rfloor$ | `\lfloor (i-1)/2 \rfloor` | a heap node's parent, by arithmetic alone |
