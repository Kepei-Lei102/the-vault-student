---
chinese: 平衡树 (pínghéngshù)
prerequisites:
  - "[[Binary Trees]]"
  - "[[Big-O Notation]]"
leads_to: []
tags:
  - subject/computer-science
  - domain/data-structures
  - level/A-Level
  - level/university
  - type/deep
  - misconception/rotations-break-the-ordering
  - misconception/balanced-means-perfect
  - misconception/avl-always-beats-red-black
  - misconception/b-tree-means-binary
---

# Balanced Trees 平衡树

> *[[Binary Trees]] closed on a confession: everything the structure promises rests on a **balance assumption** it does nothing to enforce. Feed it sorted data — the most natural input in the world — and $O(\log n)$ quietly becomes $O(n)$, with no error raised anywhere. This card is about converting that hope into a **contract**: what the degradation actually costs, the one legal move that repairs a tree without breaking its promise, the two classic machines built from that move — and the wide, stocky cousin that runs every database you have ever queried.*

## 中文锚点

上一张[[Binary Trees|卡片（二叉树）]]的结尾是一句坦白：二叉搜索树的 $O(\log n)$ 靠的是一个它自己**并不维护**的假设——树要长得平衡。数据乱序到来，树自然茂密；数据**按顺序**到来（编号、时间戳、按字母表导入的名单——这恰恰是现实里最常见的输入），树就退化成一条链。这张卡片把"希望"升级成**合同**，分四步。第一步补上**删除**（考纲里没有、但平衡机器离不开的手术）：删叶子、删一个孩子的、删两个孩子的——双孩的情况用"中序后继"顶替，而后继**必然至多只有一个孩子**，所以难题总能化归成简单题。第二步把代价**算清楚**：最坏 $O(n)$、最好 $\lceil\log_2(n{+}1)\rceil$、随机到来的平均深度约 $1.39\log_2 n$——平均不坏，但最坏并非小概率意外，而是最平常的输入。第三步是**旋转**：唯一合法的修树动作——把孩子提到父亲的位置上、三个指针换位，**中序遍历完全不变**（排序承诺毫发无损），高度却矮了一层。AVL 树给每个节点立规矩"左右子树高度差不超过 1"，插入后沿路检查、失衡就旋转（四种情况：LL、RR 单旋，LR、RL 先转孩子再转自己）——效果惊人：**把 1 到 1023 按顺序喂给普通 BST 得到高度 1023 的链；喂给 AVL 得到高度 10——正好是完美值**。红黑树是更"懒"的合同（最长路径不超过最短的两倍），换来更少的旋转次数，所以各语言的标准库选它。第四步下到磁盘：**B 树**把节点撑宽到一整个磁盘块（每块几百个键），一亿条记录三四次读盘就命中；**B+ 树**再把数据全部压到叶层、叶子串成链表——范围查询变成顺着链走——这就是 MySQL、SQLite、PostgreSQL 索引里真正住着的那棵树。

| English | 中文 | one-line meaning |
|---|---|---|
| deletion (BST) | 删除 | three cases: leaf / one child / two children — the successor swap |
| in-order successor | 中序后继 | the smallest node of the right subtree: right once, then left to the floor |
| rotation | 旋转 | the one legal move: lift a child over its parent, order preserved |
| balance factor | 平衡因子 | height(left) − height(right), the number AVL polices |
| AVL tree | AVL 树 | 1962: rebalance whenever any balance factor leaves {−1, 0, 1} |
| red-black tree | 红黑树 | the lazier contract — longest path ≤ 2 × shortest; the library favourite |
| B-tree | B 树 | hundreds of keys per node — one node = one disk block |
| B+ tree | B+ 树 | data only in the leaves, leaves chained — the database index |
| fanout / order | 扇出 / 阶 | how many children one node can have — the disk's dial |

## The unfinished business

Two debts stand open from [[Binary Trees]]. First, the missing operation: the syllabus never asked deletion, and the balancing machinery below cannot exist without it, so it gets built properly here. Second, the price that was only gestured at: "balanced → $O(\log n)$, degenerate → $O(n)$" is true, but a tree that will hold real data deserves real analysis — *how likely* is degradation, *how bad* is typical, and what does a guarantee cost? The plan: complete the toolkit, price the risk honestly, then meet the three machines that make the risk vanish — two for memory, one for disk.

## Deletion — the surgery the syllabus spared you

Deleting from a chain was one write. Deleting from a tree depends entirely on **how many children the doomed node has**, and the three cases escalate beautifully.

**Case 1 — a leaf.** Null out the parent's pointer. The node vanishes; nothing else changes.

**Case 2 — one child.** The [[Linked List]] move: the parent adopts the grandchild. One pointer write, and the whole subtree below comes along intact — the promise survives because everything in that subtree stood in the correct relation to the parent already.

**Case 3 — two children.** Now the shape genuinely breaks: removing the node orphans *two* subtrees with only one vacant pointer above. The classic repair refuses to fight the shape at all. Find the node's **in-order successor** — the smallest value in its right subtree: step right once, then left until the floor. **Overwrite the doomed node's data with the successor's**, then delete the *successor* instead. Every part of this is forced by logic worth spelling out:

- The successor is the next value in sorted order, so planting it where the deleted value stood keeps every ordering relation true — everything left of the slot is still smaller, everything right still larger.
- The successor **cannot have a left child** (a left child would be smaller, and then *it* would be the successor) — so deleting it falls into case 1 or case 2, which are already solved. The hard case always reduces to an easy one, by construction.

```python
def delete(root, target):
    if root is None:
        return None                      # not found — nothing to do
    if target < root.data:
        root.left = delete(root.left, target)
    elif target > root.data:
        root.right = delete(root.right, target)
    else:                                # found it — three cases
        if root.left is None and root.right is None:
            return None                  # case 1: leaf — vanish
        if root.left is None:
            return root.right            # case 2: adopt the grandchild
        if root.right is None:
            return root.left
        succ = root.right                # case 3: right once...
        while succ.left is not None:
            succ = succ.left             # ...then left to the floor
        root.data = succ.data            # plant the successor here
        root.right = delete(root.right, succ.data)   # delete its twin below
    return root
```

*(The mirror choice — the in-order **predecessor**, largest of the left subtree — works identically; alternating between the two in long-running trees is the classic remedy for a slow leftward skew that always-successor deletion causes.)* This code survived a 2000-trial battery — thirty deletions per trial, the in-order readout compared against a sorted reference after every single one. Watch it run all three cases, the live code line lighting up as each fires:

![[balanced-trees-deletion.mp4]]

## The price, measured honestly

[[Big-O Notation]] taught the grammar; here is the full sentence for the plain BST, all three cases stated like an honest merchant:

| | find / insert / delete | when |
|---|---|---|
| **best** | $O(\log n)$ — exactly $\lceil \log_2(n+1) \rceil$ levels | perfectly balanced shape |
| **average** | $O(\log n)$ — expected depth $\approx 2\ln n \approx 1.39\,\log_2 n$ | keys arrive in **random** order |
| **worst** | $O(n)$ — the spine | keys arrive sorted, or nearly |

The average row deserves its footnote, because it is a beautiful theorem: a random insertion order builds a tree whose expected node depth is about $2 \ln n$ — only 39% worse than perfect — and the recurrence behind that number is *the same recurrence* that prices quicksort's average case in [[Sorting]], because a BST built from a random sequence and a quicksort run on it make exactly the same comparisons. Randomness is genuinely kind to this structure.

The trap is the third row's *when*. Worst-case inputs are not freak accidents — **sorted arrival is the most natural input in the world**: auto-incrementing IDs, timestamps, an alphabetised file imported record by record. The plain BST is a structure whose catastrophic input is its most common one. That is not a fixable bug in the code; it is a missing clause in the contract. Three machines below add the clause, each with a different signature.

## The rotation — the one legal move

Every self-balancing tree is built from a single primitive. A **rotation** lifts a child over its parent — three pointer writes — and its whole value lies in what it *doesn't* change.

![[balanced-trees-rotation.svg|720]]

Read the right rotation from the figure: $y$ is heavy on the left, so its left child $x$ comes up, $y$ slides down to be $x$'s right child, and $x$'s old right subtree $B$ — the only piece with a genuine decision to make — reattaches as $y$'s new left child. Now check the promise. In-order before: $A,\ x,\ B,\ y,\ C$. In-order after: $A,\ x,\ B,\ y,\ C$. **Identical.** Every rotation, anywhere in any tree, preserves the sorted order perfectly — which is why a balancer may rotate as aggressively as it likes without ever consulting the data. Shape and order have been decoupled: rotations edit the shape; the promise lives in the order.

```python
def rot_right(y):                 # lift y's left child over y
    x = y.left
    y.left = x.right              # subtree B changes parent — the only decision
    x.right = y
    return x                      # x is the subtree's new root

def rot_left(x):                  # the mirror
    y = x.right
    x.right = y.left
    y.left = x
    return y
```

One level of height moves from the heavy side to the light side, for three writes. Everything else in this card is policy about *when* to spend those three writes. The clip below executes `rot_right` line by line — watch the in-order strip refuse to move — then runs all four AVL cases, with the LR and RL elbows straightened in slow motion:

![[balanced-trees-rotations.mp4]]

## AVL — the strict contract (1962)

The first self-balancing tree, and still the cleanest to understand. Adelson-Velsky and Landis's rule: store each node's **balance factor** — height(left) − height(right) — and demand it stay in $\{-1, 0, +1\}$ at *every* node, after *every* operation. Insert normally, then walk back up the insertion path; the first node whose factor hits ±2 gets repaired on the spot, and one repair is always enough for an insert.

The repair comes in four flavours, and they are two mirror-pairs, not four separate ideas:

- **LL** (left-left heavy): one right rotation.  **RR**: one left rotation.
- **LR** (left child is *right*-heavy): the child points the wrong way for a single rotation to fix — so rotate the **child left first** to convert LR into LL, then rotate right as before. **RL**: the mirror.

![[balanced-trees-avl-cases.svg|720]]

Watch it work on the exact input that kills a plain BST — the values $1, 2, 3, \dots$ arriving in sorted order. Insert 1, 2: fine. Insert 3: the root's factor hits −2, RR case, one left rotation — and 2 is the new root with 1 and 3 as children. The spine *cannot form*; every third step or so, the tree snaps back. Run it to the end (this card's test battery did): **1 to 1023 fed in sorted order builds a plain BST of height 1023 — and an AVL tree of height 10, which is perfect.** Not "better." *Optimal*, on the adversarial input, automatically.

![[balanced-trees-see-it-run.mp4]]

How strong is the guarantee in general? The worst AVL tree — maximally lopsided while still legal — has every node's factor at +1, and its node count obeys $N(h) = N(h-1) + N(h-2) + 1$: the **Fibonacci recurrence**, one level maximally tall and the other one shorter. Fibonacci numbers grow like powers of the golden ratio $\varphi \approx 1.618$, and inverting that gives the celebrated bound:

$$h \le 1.4405\,\log_2(n + 2) - 0.33$$

An AVL tree is never more than 44% taller than perfect — the golden ratio, of all things, standing guard over a data structure. And you do not have to take the bound on faith: **`balanced-trees-verify.py`, committed beside this card, seeds itself from today's date** and builds three hundred random trees of 10 to 20,000 keys, checking the golden-ratio bound, the BST property and every balance factor on each — then measures the plain BST's average-case ratio for good measure. Today's run: worst height ratio **1.324** against the allowed 1.44, and average BST depth at **0.90 × 2 ln n**, right where the theorem points. Run it tomorrow and it tests trees nobody has ever built; the bound will hold, because it is a theorem, not luck. One caution before the comfort settles in: **real-world numbers are *not* this random.** IDs, timestamps and alphabetised imports arrive sorted; the friendly average case quietly leaves the room, and that gap is precisely why the machines on this card exist. The cost of AVL's guarantee: every insert and delete pays $O(\log n)$ rebalancing bookkeeping on the way back up, and write-heavy workloads feel it.

## Red-black — the lazy contract the libraries chose

AVL polices height *tightly* and rotates often. The **red-black tree** (1972/78 lineage) polices it *loosely* and rotates rarely — a different point on the same trade curve. Every node is coloured red or black under rules whose combined effect is one inequality: **no path from root to leaf may be more than twice as long as any other.** (The mechanism: every root-to-leaf path must contain the same number of *black* nodes, and red nodes may never stack two-in-a-row — so the longest possible path alternates red-black while the shortest is all black, a factor of two at most.)

Twice-perfect is worse balance than AVL's 1.44 — red-black trees run a little deeper, and searches pay a few extra comparisons. What they buy is cheaper *change*: the rotation bill is **capped per operation** — at most two rotations on any insert, three on any delete — where AVL deletions can cascade rotations all the way back to the root; the rest of each repair is recolouring, which touches no pointers. (Honest measurement, from this card's own harness: on random input the repairs split roughly half-and-half between recolourings and rotations — the win is the *cap*, not a rotation famine.) That trade — slightly worse reads, meaningfully cheaper writes — is why the standard libraries picked it: C++'s `std::map`, Java's `TreeMap`, the Linux kernel's scheduler queues are all red-black trees. Watch the machine refuse the spine — sorted feed, live counters, paint and rotation each taking their share:

![[balanced-trees-redblack.mp4]]

(The full insert algorithm, with the four invariant checks it must pass — root black, no red-red, equal black-height everywhere, height within $2\log_2(n+1)$ — lives in `balanced-trees-verify.py`: the card describes, the harness proves.) (The deletion rebalancing cases are also legendarily fiddly — a rite of passage in university courses, and the honest reason this card demonstrates AVL and *describes* red-black.) A tidy secret for later study: a red-black tree is exactly a **2-3-4 tree** — a small B-tree — with each wide node exploded into a little cluster of binary ones, the red edges marking which nodes are fragments of the same cluster. The two machines below and above this paragraph are one idea at two scales.

## B-trees — balance goes to disk

Move the tree from RAM to [[Secondary Storage]] and the pricing model flips: a disk read fetches a whole **block** (kilobytes) in the time it takes to do millions of comparisons, so the expensive unit is no longer the comparison — it is the *hop*. A binary node wastes a block-read on a single key. The **B-tree** (Bayer & McCreight, 1972) refuses the waste: widen each node until it fills the block — hundreds of keys and children per node — and the tree becomes short and stocky. The arithmetic is the whole argument: with 256 children per node, $10^8$ keys need a tree of height about **4**; at fanout 1024, height **3**. A hundred million records, three or four disk reads, guaranteed.

Two design choices keep it balanced with no rotations at all:

- **Nodes split upward.** Insert into a full node and it splits in two, promoting its middle key to the parent; if the parent overflows it splits too, and if the *root* splits, the tree gains a level **at the top**. All leaves therefore sit at exactly the same depth forever — the B-tree is the one tree in this card that grows *upward*, and perfect balance is a structural inevitability rather than a policed invariant.
- **Nodes run half-full minimum**, so space and height stay bounded even under deletions (which merge or borrow, the split's mirror).

And the name? Bayer and McCreight never said what the **B** stands for — Boeing (where they worked), balanced, broad, bushy, Bayer himself — and McCreight's eventual answer was that the more you think about what the B could mean, the more you learn about B-trees. The refusal is deliberate and, by now, tradition ([[A, B, C]] would approve).

## The B+ tree — what your database actually uses

Production databases run a refinement worth knowing by name. In a **B+ tree**:

- **Interior nodes hold only routing keys** — signposts, no data. Thinner entries mean *more* of them fit per block, so the fanout climbs and the tree gets even shorter.
- **All data lives in the leaves**, and — the masterstroke — **the leaves are chained left-to-right into a linked list.**

![[balanced-trees-bplus.svg|720]]

That one chain changes the structure's character. A point query (`WHERE id = 774631`) descends three or four levels as before. But a **range query** (`WHERE date BETWEEN …`) descends *once* to the first match and then simply walks the leaf chain sideways — a sequential scan of exactly the answer, no tree navigation at all. [[Linked List]]'s humble follow-the-pointer walk, welded to the bottom of a tree, is what makes `ORDER BY` and range scans cheap. This is the index structure inside MySQL's InnoDB, SQLite, and PostgreSQL, and the same wide-node logic organises the file systems under NTFS, APFS and Btrfs — which wears the name on its sleeve. When [[Binary Trees]] said "every serious database index is a tree," this is the tree it meant. Watch the order-4 tree grow at the root as full nodes split, then the B+ leaf chain swallow a range query whole:

![[balanced-trees-btree.mp4]]

## Choosing, honestly

| structure | search | insert/delete | its natural habitat |
|---|---|---|---|
| plain BST | $O(\log n)$ *hoped* | cheap | throwaway trees over data known to arrive shuffled |
| AVL | $O(\log n)$ guaranteed, tightest | rotation-heavy | read-mostly data, lookups dominate |
| red-black | $O(\log n)$ guaranteed, looser | cheapest of the balanced | general purpose — the library default |
| B / B+ | $O(\log_m n)$ — 3–4 **block reads** | splits/merges, block-priced | disk and databases; B+ adds cheap range scans |

And the reminder from the map of structures: every row above still pays $O(\log n)$-ish. If the collection never needs *order* — no ranges, no sorted readout, only "is it there?" — a [[Hash Tables|hash table]] answers in $O(1)$ and this whole card is the wrong tool. Order is precisely what trees sell.

## Common Misconceptions (Teaching Notes)

### 1. "Rotations must corrupt the ordering sometimes"

Never — and it is provable in one line: a rotation permutes the pieces $(A, x, B, y, C)$ back into the same in-order sequence $A, x, B, y, C$. The balancer never inspects the data because it cannot break what it cannot touch: order and shape are decoupled, and rotations edit only shape.

### 2. "Balanced means perfectly balanced"

Each machine sells a different looseness: AVL allows a 1.44 factor over perfect, red-black allows 2. "Balanced" is a *contract term* meaning "height provably $O(\log n)$", not a promise of the prettiest possible tree. Only the B-tree keeps all leaves at exactly equal depth — and it achieves that by growing at the root, not by rotating.

### 3. "AVL is strictly better — it's more balanced"

Tighter balance is a *cost*, paid at every write. Read-heavy data rewards AVL's shorter paths; write-heavy data rewards red-black's constant-rotation repairs. That both survive seventy years on is the proof that neither dominates — it is a genuine trade, and the libraries picking red-black tells you which side most real workloads sit on.

### 4. "The B in B-tree means binary"

The opposite in spirit: a B-tree node has *hundreds* of children precisely to escape binary's one-key-per-block waste on disk. The B was never officially defined — and a B-tree of order 4 *contains* the binary red-black tree as its exploded view, so the family relation runs through width, not the alphabet.

## Exam Notes

**Not examined at school level, anywhere in the vault's boards — this is a university-preview card.** Cambridge 9618 stops at the plain BST's find and insert (§19.1, [[Binary Trees]]' Exam Notes carry the detail); deletion, rotations, AVL, red-black and B-trees appear nowhere in the 2027–29 syllabus. Cambridge 0478 has no trees at all. AP CSA stops at `ArrayList`. IB CS's B4.1 covers ADT fundamentals; its published outline does not name self-balancing machinery. Where this material *is* the syllabus: first-year university data-structures courses (AVL insertion with rotation cases is a canonical exam question; red-black deletion a canonical homework horror), database-systems courses (B+ mechanics), and software-engineering interviews. One honest exam-adjacent payoff at A-Level: the phrase "**provided the tree remains balanced**" in a 9618 Big-O justification is worth a mark, and this card is what that clause actually means.

## Connections

- **Builds on:** [[Binary Trees]] — the structure whose balance assumption this card converts into a contract, and whose missing delete is built here; [[Big-O Notation]] — the pricing language, now with best/average/worst stated in full.
- **Kindred:** [[Sorting]] — the random-BST average-depth recurrence is quicksort's analysis wearing pointers; [[Linked List]] — the leaf chain that gives B+ its range scans, and case 2's adopt-the-grandchild delete; [[Secondary Storage]] — the block pricing that dictates B-tree width; [[Hash Tables]] — the escape hatch when order isn't wanted; [[A, B, C]] — computing's other great refused naming.
- **Leads back to:** [[Heaps and Priority Queues]] — the *other* way to discipline a binary tree, with shape fixed and a vertical promise instead.

## LaTeX Reference

| symbol | LaTeX | meaning here |
|---|---|---|
| $h \le 1.4405\,\log_2(n+2)$ | `h \le 1.4405\,\log_2(n+2)` | the AVL height guarantee (golden-ratio bound) |
| $2 \ln n$ | `2 \ln n` | expected depth in a random-order BST |
| $O(\log_m n)$ | `O(\log_m n)` | B-tree height at fanout $m$ |
| $\varphi$ | `\varphi` | the golden ratio, hiding in the worst AVL tree |
