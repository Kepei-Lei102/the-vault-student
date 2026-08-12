---
chinese: 群论 (qúnlùn)
prerequisites:
  - "[[Symmetry (Vocab)]]"
  - "[[Stories/Galois at Twenty]]"
  - "[[Stories/Abel the Other Boy Who Died Young]]"
  - "[[Abel the Other Boy Who Died Young]]"
  - "[[Galois at Twenty]]"
leads_to:
  - "[[Roots of Unity]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/A-Level
  - level/university
  - curriculum/A-Level
  - curriculum/Edexcel-Further
  - type/definition
  - type/theorem
  - notation/group
  - misconception/groups-must-be-numbers
  - misconception/groups-are-commutative
  - misconception/algebra-is-only-solving-equations
---

# Group Theory 群论

> *A group is the mathematics of symmetry — of every action you can undo and combine. It is what is left when you ask "what doesn't change?" and write the answer down as an object.*

Two boys died young to open this door — [[Stories/Galois at Twenty|Galois]] in a duel at twenty, [[Stories/Abel the Other Boy Who Died Young|Abel]] of tuberculosis at twenty-six — and what they were reaching for is one of the simplest and most powerful ideas in all of mathematics. A **group** is a set with *one* operation obeying *four* rules. That is the entire definition. From those four rules unfolds the language of symmetry itself: why the quintic has no formula, why a Rubik's cube can be solved, why energy is conserved, and how the arithmetic under AES and every QR code works.

The seed is the hunter's question from [[Forward Reading and Problem Discovery]]: *what doesn't change?* A symmetry of an object is a transformation that leaves it looking the same. Collect **all** such transformations for a given object, and that collection is not a random pile — it has a rigid internal arithmetic. Group theory is the study of that arithmetic, stripped of the object, kept as pure structure.

## 中文锚点

**群 (qún)** = a group：一个集合 $G$ 配上**一个**二元运算 $*$，满足**四条公理**——封闭性、结合律、有单位元、每个元素有逆元。注意：**不要求交换律**。满足交换律的群叫**交换群 / 阿贝尔群 (Abelian group)**，以 [[Stories/Abel the Other Boy Who Died Young|阿贝尔]] 命名。

群论是**对称的代数**。一个物体的所有"对称"（保持它不变的变换）合在一起，就构成一个群——这正是猎人式提问"**什么没有改变？**"（[[Forward Reading and Problem Discovery]]）写成的对象。

核心概念：**阶** ($|G|$)、**循环群** ($C_n$，由一个生成元的幂构成，如单位根)、**对称群** ($S_n$，$n$ 个对象的全部置换)、**子群**、**拉格朗日定理** (子群的阶整除群的阶)、**同构** (换了外衣的同一个群)。终点：**可解群**——五次方程可用根式求解当且仅当其伽罗瓦群可解，而 $A_5$ 不可解，所以五次方程没有公式（见 [[Cubic Graphs]]）。

> "代数"有两层含义：中学里的**初等代数**（解方程、求 $x$）和这里的**抽象代数 (abstract algebra)**——把运算满足的**规则**抽出来、把数字丢掉，单独研究这套"骨架"。二者其实是同一件事的两层深度（见下节）。

---

## First — this is not "solve for $x$"

If you arrived expecting quadratics and factorising, pause for one minute, because the mismatch hides one of the best ideas in mathematics. **The word "algebra" comes in two sizes.**

- **Elementary (school) algebra** — the one you know. It was born as *al-jabr* ("restoration — the reunion of broken parts") in al-Khwārizmī's Baghdad around 820 CE: the craft of carrying an *unknown number* through the same arithmetic that ordinary numbers obey, and solving for it. Letters standing in for numbers. (His name also gives us the word *algorithm* — the man is load-bearing.)
- **Abstract (modern) algebra** — the one on this page. Here the letters **no longer stand for numbers at all.** You keep only the *rules* an operation obeys — associativity, an identity, inverses — throw the numbers away, and study whatever **structure** those bare rules define. A group is the leanest such structure.

Here is the bridge, and it is worth the detour: **you have been doing abstract algebra all along without noticing.** Every time you trusted that $x + y = y + x$, or rewrote $x(y+z) = xy + xz$, you were leaning on *rules the real numbers happen to satisfy* — you just never peeled the rules off the numbers. School algebra is, quietly, the study of **one** structure: the real numbers under $+$ and $\times$. Abstract algebra is what happens the instant you realise the structure can be **swapped out** — that a clock, the symmetries of a triangle, the roots of unity, and a Rubik's cube each run their own version of the same skeleton.

So this *is* algebra — the original meaning, in fact. Al-Khwārizmī's *al-jabr* was never about the letter $x$; it was about **the moves you are allowed to make.** This is a card about the moves, and nothing else. And you already live inside one of these structures: $(\mathbb{Z}, +)$, the integers under addition, is a group. You have known a group your whole life.

---

## The four axioms

A **group** is a set $G$ together with a binary operation $*$ (a rule that takes two elements and returns one) satisfying:

| Axiom | Statement | What it means |
|---|---|---|
| **Closure** | For all $a, b \in G$, $\;a * b \in G$ | combining two members never escapes the set |
| **Associativity** | $(a * b) * c = a * (b * c)$ | grouping doesn't matter; $a*b*c$ is unambiguous |
| **Identity** | there is $e \in G$ with $e * a = a * e = a$ for all $a$ | a "do-nothing" element exists |
| **Inverse** | for each $a$ there is $a^{-1}$ with $a * a^{-1} = a^{-1} * a = e$ | every action can be undone |

That is the whole definition. Read it as a description of **reversible actions you can perform one after another**: you can always do one then another (closure), the order you *bracket* them doesn't matter (associativity), doing nothing is allowed (identity), and everything can be undone (inverse).

> [!warning] Commutativity is *not* an axiom
> Nowhere does the definition demand $a * b = b * a$. This is the single most important thing about groups, and the reason the whole theory is rich rather than trivial. Order often matters: putting on socks then shoes is not the same as shoes then socks. A group in which $a*b = b*a$ *always* holds is given a special name — **abelian** (交换群), after [[Stories/Abel the Other Boy Who Died Young|Niels Henrik Abel]], whose quintic proof turned on exactly this property. Abelian groups are the tame, commutative minority; the wild and interesting groups are **non-abelian**.

The number of elements $\lvert G \rvert$ is the **order** of the group (finite or infinite). A one-element group $\{e\}$ is the *trivial* group.

**A first sanity check.** The identity is unique (if $e$ and $e'$ both work, $e = e * e' = e'$), and inverses are unique (if $b$ and $c$ both invert $a$, then $b = b*e = b*(a*c) = (b*a)*c = e*c = c$). Both facts fall straight out of the axioms — a taste of how much structure four rules force.

---

## Concrete first — groups you already know

Abstraction is worthless without examples. You have been computing in groups your whole life.

- **$(\mathbb{Z}, +)$** — the integers under addition. Identity $0$; inverse of $n$ is $-n$; associative and closed. **Abelian, infinite.** (Note $(\mathbb{Z}, \times)$ is *not* a group — $2$ has no integer inverse.)
- **$(\mathbb{Z}_n, +)$** — integers modulo $n$, i.e. clock arithmetic. On a $12$-hour clock, $9 + 5 = 2$. Identity $0$, inverses wrap around ($9^{-1} = 3$ since $9+3=12\equiv 0$). **Abelian, order $n$.** This is the **cyclic group** $C_n$.
- **The $n$-th roots of unity** $\{1, \omega, \omega^2, \dots, \omega^{n-1}\}$, $\omega = e^{2\pi i/n}$, under multiplication (see [[Complex Numbers]], [[Roots of Unity]]). Multiplying two of them adds their exponents mod $n$ — *the very same arithmetic as the clock.* Another copy of $C_n$.
- **Symmetries of a shape** — the rotations and reflections that map a regular polygon onto itself (see [[Symmetry (Vocab)]]). This is where groups become *non-abelian*, and it deserves its own picture.

---

## Order — two things it counts

One word gets used constantly from here on, and it means two related things. Pin both down now, on a clock, before the first real example.

**Order of a group**, written $\lvert G \rvert$, is simply *how many elements it has*. The 12-hour clock $(\mathbb{Z}_{12}, +)$ has order $12$; the trivial group $\{e\}$ has order $1$; $(\mathbb{Z}, +)$ has infinite order.

**Order of an element** $g$ is *how many times you apply it to get back to the identity* — the smallest $k > 0$ with $g^k = e$ (for an additive group, the smallest $k$ with $g + g + \cdots + g$, $k$ times, equal to $e$).

Watch it on the clock $(\mathbb{Z}_6, +)$, identity $0$:

| element $g$ | keep adding it… | back to $0$ after | **order** |
|---|---|---|---|
| $2$ | $2,\;4,\;0$ | 3 steps | $3$ |
| $3$ | $3,\;0$ | 2 steps | $2$ |
| $1$ | $1,2,3,4,5,0$ | 6 steps | $6$ |
| $0$ | already $0$ | — | $1$ |

An element's order is **the length of the cycle it traces.** Element $1$ traces the whole group before returning — hold that thought for cyclic groups. And notice every order here — $1, 2, 3, 6$ — **divides** the group order $6$. That is not a coincidence; it is Lagrange's theorem, proved below.

---

## The smallest interesting group: symmetries of a triangle

![[group-triangle-symmetries.svg|620]]
*Animation — watch the numbered corners rotate by $0°, 120°, 240°$ and land the triangle back on itself each time: three rotations that are symmetries. The three dashed lines are the reflection axes (flip across each). Three rotations + three reflections = six symmetries, the group $D_3$ (= $S_3$).*

Take an equilateral triangle. The transformations that leave it occupying the same space are: the identity (do nothing), rotation by $120°$, rotation by $240°$, and reflection across each of the three axes through a vertex. That is **six** symmetries — so this group has **order $6$** (the count you just met). Compose any two — do one, then the other — and you always get another of the six (closure). Each undoes ($r_{120}$ and $r_{240}$ invert each other; every reflection is its own inverse). This is the **dihedral group** $D_3$, the smallest non-abelian group.

Watch the non-commutativity directly. Label a reflection $s$ and the $120°$ rotation $r$, and do the *same two moves in the opposite order*:

![[group-noncommutativity.svg|620]]
*Left: rotate ($r$), then reflect ($s$). Right: reflect ($s$), then rotate ($r$). Same two moves, opposite order — and corners $1,2,3$ land in **different** final positions. So $sr \ne rs$: in a group, order of operations can change the answer.*

Doing $r$ **then** $s$ lands the triangle differently from $s$ **then** $r$ — watch corner $1$ end up in different places in the two columns. Order matters. That single fact — that symmetries need not commute — is what ultimately blocks a quintic formula; we get to exactly why below.

> [!info] $D_n$ vs $S_n$ — a warning that saves confusion later
> $D_n$ (order $2n$) is the symmetries of a regular $n$-gon: rotations **and** reflections. $S_n$ (order $n!$) is **all** permutations of $n$ labelled objects. They coincide only at $n=3$ ($D_3 = S_3$, both order $6$), because with three points *every* rearrangement is achievable by a rigid symmetry. From $n=4$ on they part ways: $D_4$ has $8$ elements, $S_4$ has $24$.

---

## Cyclic groups — one element runs the whole show

Recall element $1$ on the clock $(\mathbb{Z}_6,+)$: adding it repeatedly walked through *every* element before coming home. A group where some single element does that is **cyclic**, and that element is a **generator**. Write $G = \langle g \rangle$ — "the group generated by $g$."

Make it fully concrete with $C_4 = (\mathbb{Z}_4, +)$, taking $g = 1$ and reading $g^k$ as "add $1$, $k$ times":
$$g = 1,\qquad g^2 = 1{+}1 = 2,\qquad g^3 = 2{+}1 = 3,\qquad g^4 = 3{+}1 = 0 = e.$$
One element, applied over and over, visited all four and returned to the identity on the fourth step. **That is what "cyclic" means** — the whole group is a single cycle. The generator's order ($4$) equals the group's order ($4$), and that is the definition sharpened: *a group is cyclic exactly when it has an element whose order is $\lvert G\rvert$.* (In $C_4$ the generators are $1$ and $3$, both order $4$; the element $2$ only reaches $\{0,2\}$, order $2$, so it is not a generator.)

$C_n$ works the same way for every $n$: $\langle g \rangle = \{e, g, g^2, \dots, g^{n-1}\}$ with $g^n = e$. And you have already met three copies of $C_4$ without noticing.

![[group-three-costumes.svg|697]]
*One group, three costumes. The cyclic group $C_4$ appears as the fourth roots of unity $\{1, i, -1, -i\}$ under multiplication, as the rotations of a square, and as the clock $\{0,1,2,3\}$ under addition mod $4$. Different sets, different operations, **identical structure** — each is $\langle g\rangle$ with $g^4 = e$. Group theory studies the structure, not the costume.*

Cyclic groups are always **abelian** (powers of one element commute: $g^a g^b = g^{a+b} = g^b g^a$). They are the simplest groups there are — one for each order $n$ — and, as Lagrange will show, the *only* groups of prime order.

---

## Permutations — rearrangements, and why $D_3 = S_3$

Go back to the triangle animation. Every symmetry did exactly one thing: it **rearranged the three corners.** A rearrangement of a set is a **permutation**, and *all* the permutations of $\{1, 2, \dots, n\}$ form a group under "do one, then the other" — the **symmetric group** $S_n$, of order $n!$.

Count for $n = 3$: there are $3! = 6$ ways to rearrange three corners — and the triangle had exactly $6$ symmetries. They line up one-for-one. **That is *why* $D_3 = S_3$:** with only three corners, every possible rearrangement is achievable by some rotation or reflection. (From four corners on, a square has just $8$ symmetries but $4! = 24$ rearrangements, so $D_4 \ne S_4$ — most rearrangements of a square's corners are *not* rigid symmetries.)

**Cycle notation, slowly.** The rotation that sends corner $1\to2$, $2\to3$, $3\to1$ is written $(1\;2\;3)$ — read "one goes to two goes to three goes back to one," one closed loop. A reflection that swaps $1\leftrightarrow2$ and fixes $3$ is written $(1\;2)$ — a two-element swap, called a **transposition**. So the six elements of $S_3$ split exactly as the triangle's symmetries did:
$$\underbrace{e,\ (1\,2\,3),\ (1\,3\,2)}_{\text{the 3 rotations}}, \qquad \underbrace{(1\,2),\ (1\,3),\ (2\,3)}_{\text{the 3 reflections}}.$$

**Even vs odd — count the swaps.** Any rearrangement can be reached by a sequence of transpositions (swaps of two). A single swap like $(1\,2)$ takes **one** swap — *odd*. A 3-cycle $(1\,2\,3)$ takes **two** (do $(1\,3)$, then $(1\,2)$ — check it) — *even*.

![[group-permutation-parity.svg|697]]
*Watch the parity. Top: the transposition $(1\,2)$ is a single swap — **odd**. Bottom: the 3-cycle $(1\,2\,3)$ takes two swaps to build — **even**. The even permutations form a subgroup of exactly half the size, the **alternating group** $A_n$.*

Here $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$ — precisely the triangle's **rotations**. So the rotations are the even half of the triangle's group, and the reflections are the odd half. (This is not a coincidence of the triangle: for every $n$, the even permutations are exactly half of $S_n$, an index-$2$ subgroup.)

> [!info] The toy in your hands — 15-puzzle parity
> Sliding a tile in the 15-puzzle is always an *even* permutation, so the reachable arrangements are exactly $A_{15}$, never the full $S_{15}$. That is why the "swap only the 14 and 15" position — an *odd* permutation — can never be reached by sliding. The full story is in [[Stories/Galois at Twenty]]; the parity that forbids the swap is the *same* structural fact ($A_n$ inside $S_n$) that forbids a quintic formula.

---

## The Cayley table — a group's whole multiplication table on one grid

Everything about a finite group fits in a single grid: the **Cayley table**, which records the result of *every* "do $a$, then $b$." It is the group's complete DNA — hand someone the table and you have handed them the group. But a table is only useful if you can read one, so start with the friendliest possible example.

Here is $C_4 = (\mathbb{Z}_4, +)$. The entry in row $a$, column $b$ is just $a + b \pmod 4$:

| $+$ | **0** | **1** | **2** | **3** |
|---|---|---|---|---|
| **0** | 0 | 1 | 2 | 3 |
| **1** | 1 | 2 | 3 | 0 |
| **2** | 2 | 3 | 0 | 1 |
| **3** | 3 | 0 | 1 | 2 |

Read one cell to get the habit: row $2$, column $3$ gives $2 + 3 = 5 \equiv 1$. Now notice the two things *every* group table shows, both plainly visible here:

- **Each symbol appears once in every row and once in every column** — a **Latin square**, exactly like a completed Sudoku. The axioms force this: if $a * x = a * y$ you can cancel (multiply by $a^{-1}$) to get $x = y$, so no symbol can repeat in a row.
- **This table is symmetric across the main diagonal** — cell $(1,2)$ and cell $(2,1)$ both read $3$ — because $C_4$ is **abelian**. *Symmetry across the diagonal is a one-glance test for commutativity.*

Now the contrast that makes the point. Here is $S_3$ — same kind of table, six elements, but painted one colour per element so the structure reads at a glance instead of drowning in symbols:

![[group-s3-cayley.svg|697]]
*The Cayley table of $S_3$, colour-coded. The **Latin-square** pattern survives — every colour appears once per row and once per column. But the table is **not** symmetric across the diagonal: cell $(r, s)$ and cell $(s, r)$ carry different colours. That visible asymmetry *is* non-commutativity — $S_3$ is non-abelian. It is the same kind of object as the $C_4$ table above, just too large to read comfortably in symbols, so colour carries the structure.*

---

## Subgroups and Lagrange's Theorem — the first deep result

A **subgroup** $H \le G$ is a subset that is itself a group under the same operation (it contains $e$, and is closed under the operation and inverses). The rotations $\{e, r, r^2\}$ sit inside $D_3$ as a subgroup of order $3$; the even integers sit inside $(\mathbb{Z}, +)$.

**Lagrange's Theorem.** *If $G$ is finite and $H \le G$, then $\lvert H \rvert$ divides $\lvert G \rvert$.*

**See it work first.** Take $G = S_3$ (order $6$) and, for $H$, the rotation subgroup $\{e, r, r^2\}$ (order $3$). Slice $G$ into **left cosets** $gH$ — "everything you reach by doing $g$, then a rotation":

- $eH = \{e,\, r,\, r^2\}$ — this is $H$ itself, the three **rotations**.
- $sH = \{s,\, sr,\, sr^2\} = \{(1\,2),\, (1\,3),\, (2\,3)\}$ — the three **reflections**.

Two cosets, three elements each, no overlap, and together they account for all six elements of $S_3$:

![[group-lagrange-cosets.svg|697]]
*Lagrange in action. The subgroup $H$ (the rotations) and its one other coset (the reflections) tile $S_3$ into two equal blocks of $3$. So $6 = 2 \times 3$, and $\lvert H\rvert = 3$ divides $\lvert G\rvert = 6$ — not by luck, but because the cosets are always equal-sized and always tile the group.*

That is the whole theorem in one picture: a subgroup's cosets cut the group into equal blocks the size of the subgroup, so the subgroup's order *must* divide the group's. The proof just shows those two facts — equal size, clean tiling — hold for every finite group.

This is the first genuinely surprising theorem of the subject, and its proof is a small masterpiece — worth following move by move.

**Proof.** For $g \in G$, define the **left coset** $gH = \{g * h : h \in H\}$.

1. *Every coset has exactly $\lvert H \rvert$ elements.* The map $h \mapsto g*h$ is a bijection from $H$ to $gH$: it is onto by definition, and one-to-one because $g*h_1 = g*h_2 \Rightarrow h_1 = h_2$ by cancellation.
2. *Two cosets are either identical or disjoint.* Suppose $g_1 H$ and $g_2 H$ share an element $x$. Then $x = g_1 h_1 = g_2 h_2$, so $g_1 = g_2 (h_2 h_1^{-1})$, and since $h_2 h_1^{-1} \in H$, every element $g_1 h$ of $g_1 H$ equals $g_2 (h_2 h_1^{-1} h) \in g_2 H$. So $g_1 H \subseteq g_2 H$, and by symmetry they are equal.
3. *The cosets cover $G$* (each $g$ lies in $gH$, since $e \in H$).

So the cosets **partition** $G$ into disjoint blocks, each of size $\lvert H \rvert$. If there are $k$ of them, then $\lvert G \rvert = k \lvert H \rvert$. Hence $\lvert H \rvert$ divides $\lvert G \rvert$. $\;\blacksquare$

The number of cosets $k = \lvert G \rvert / \lvert H \rvert$ is the **index** $[G:H]$.

**Two corollaries fall straight out**, and they are the payoff:

- **The order of any element divides $\lvert G \rvert$.** (The powers of $g$ form a cyclic subgroup $\langle g\rangle$ whose order is the order of $g$; apply Lagrange.) *Example:* recall the clock $(\mathbb{Z}_6, +)$, whose element orders were $1, 2, 3, 6$ — every one divides $6$, and now you see *why*: each element lives inside the cyclic subgroup it generates, and Lagrange forces that subgroup's size to divide $6$. In $S_3$ the same bite: $r$ has order $3$, $s$ has order $2$, both dividing $6$ — and an element of order $4$ or $5$ is **impossible** in *any* group of order $6$, before you even look. That is the theorem predicting, not just describing.
- **Every group of prime order $p$ is cyclic.** Its only subgroup orders are $1$ and $p$ (the divisors of $p$), so any non-identity element $g$ generates a subgroup of order $p$ — all of $G$. There is essentially only *one* group of each prime order.

---

## Isomorphism — same group, different costume

Two groups are **isomorphic** ($G \cong H$) if there is a bijection $\varphi : G \to H$ preserving the operation: $\varphi(a * b) = \varphi(a) \cdot \varphi(b)$. Such a map is an **isomorphism**; when it need not be a bijection it is a **homomorphism** (a structure-respecting map, allowed to collapse information).

Isomorphism is the statement that two groups are *the same group wearing different clothes*. The three faces of $C_4$ above — roots of unity, square rotations, clock arithmetic — are pairwise isomorphic; a group theorist regards them as one object. This is why the subject can be about "structure, not costume": the classification questions ("how many groups of order 8 are there?") count *isomorphism classes*.

> [!info] Cayley's Theorem — permutations are universal
> **Every** group is isomorphic to a subgroup of some symmetric group $S_n$. (Each element $g$ acts on the group by "multiply by $g$," which is a permutation of the elements; this action embeds $G$ into the symmetric group on its own members.) So the permutation groups $S_n$ are not just one example among many — they contain a copy of *every* finite group. Galois's instinct to study permutations of roots was, it turns out, the fully general move.

---

## The payoff — the Galois group, and why the quintic breaks

Every group so far came from a symmetry you can *see* — a triangle, a clock. The one that finally answers the 300-year quintic question is hidden, and it is the deepest idea on this page: the symmetry group of the **roots of a polynomial**, called the **Galois group**.

### First, meet the Galois group — on a quadratic

Take $x^2 - 2 = 0$. Its roots are $\sqrt2$ and $-\sqrt2$. Now the strange, load-bearing fact: **using only rational numbers and $+,-,\times,\div$, you cannot tell those two roots apart.** Every equation with rational coefficients that one root satisfies, the other satisfies too — both obey $r^2 = 2$, and together they obey $r_1 + r_2 = 0$ and $r_1 r_2 = -2$. Rational algebra simply cannot distinguish $\sqrt2$ from $-\sqrt2$.

So there is a **symmetry of the roots**: *swap $\sqrt2 \leftrightarrow -\sqrt2$* and every rational relation among them still holds. That swap, together with "do nothing," is the **Galois group** of $x^2 - 2$ — and it has exactly **two** elements. It is $S_2$, order $2$.

That answers *"why is a quadratic order 2?"* cleanly: **a quadratic has two roots that rational algebra cannot distinguish, so the only root-symmetries are *leave them* or *swap them* — two of them.** The Galois group is the hunter's question ([[Forward Reading and Problem Discovery]]) one more time: *which permutations of the roots leave every rational relation unchanged?* It is the invariance group of the roots, and it measures how tangled they are.

### Climbing the degrees

A degree-$n$ polynomial has $n$ roots, so its Galois group is some group of permutations of those $n$ roots — a subgroup of $S_n$. For a *generic* polynomial (no accidental relations among its roots) it is **all** of $S_n$:

| Degree | Roots to permute | Generic Galois group | Order | Solvable? | Formula in radicals? |
|---|---|---|---|---|---|
| 2 | 2 | $S_2$ | 2 | yes | quadratic formula |
| 3 | 3 | $S_3$ | 6 | yes | Cardano (1545) |
| 4 | 4 | $S_4$ | 24 | yes | Ferrari (1545) |
| 5 | 5 | $S_5$ | 120 | **no** | **impossible** |

The quintic's group is $S_5$, of order $120$ — but **the size $120$ is a red herring.** What decides everything is the group's *structure*.

### First, what lets you peel a layer: normal subgroups

"Peeling off a layer" means forming a **quotient** — collapsing a subgroup to a single point and asking what group the leftover cosets make. That only works for a special kind of subgroup, called **normal**.

**Definition.** A subgroup $N \le G$ is **normal** if conjugation leaves it fixed: $gNg^{-1} = N$ for every $g \in G$. (Conjugation by $g$ — the map $x \mapsto g x g^{-1}$ — is "relabel everything from $g$'s point of view"; $N$ is normal when that relabelling never knocks it off itself. Equivalently, its left and right cosets agree, $gN = Ng$.)

**Concrete, on the triangle group $S_3$** — two subgroups, opposite behaviour:

- **The rotations $A_3 = \{e, r, r^2\}$ *are* normal.** Conjugate a rotation by anything and you get a rotation back — a reflection can never turn a rotation into a reflection. (Check: $s r s^{-1} = r^2$, still a rotation.) Because $A_3$ sits symmetrically like this, you *can* collapse it: the quotient $S_3 / A_3$ has just two elements — $\{\text{rotations}\}$ and $\{\text{reflections}\}$ — and they multiply like $C_2$ (even $\cdot$ even $=$ even, even $\cdot$ odd $=$ odd, …). That two-element quotient *is* one clean abelian layer, exactly the kind a square root peels off. It is the same rotations-vs-reflections split you saw tile $S_3$ in the Lagrange diagram — now revealed to be a group in its own right.
- **A single reflection $\{e, s\}$ is *not* normal.** Conjugate $s$ by the rotation $r$ and you land on a *different* reflection: $r s r^{-1} = (2\,3)$, not $s = (1\,2)$. So $r\{e, s\}r^{-1} = \{e, (2\,3)\} \ne \{e, s\}$ — the subgroup got moved. You cannot cleanly divide by it; the "quotient" would not be a group at all.

Normal subgroups are precisely the ones you are allowed to divide out. So the whole peeling process is a chain of *normal* subgroups.

### The atoms — simple groups

Now the concept everything hinges on. What about a group with **no** normal subgroup to divide out — none except the two every group trivially has, itself and $\{e\}$? Such a group cannot be peeled at all. It is called **simple**, and simple groups are the **atoms** of group theory: exactly as every whole number factors into primes, every finite group breaks into simple pieces, and the peeling bottoms out on them.

The entire quintic question turns on *which kind* of atom you hit:

- **Abelian atoms are friendly.** The cyclic group $C_p$ of **prime** order is simple — by Lagrange it has no proper subgroup at all (the only divisors of $p$ are $1$ and $p$), so certainly no normal one. These *are* the clean abelian layers a radical peels: $C_2$ for a square root, $C_3$ for a cube root, and so on.
- **Non-abelian atoms are the killers.** $A_5$ (order $60$) is the smallest group that is simple **and** non-abelian. It has no normal subgroup to peel off, and it is not itself commutative — so there is no abelian layer anywhere inside it to strip.

That sharpens the whole problem to one line: **a group is solvable exactly when every one of its atoms is abelian** (every simple piece a $C_p$). The peeling below is how you run that test — and how $S_5$ fails it.

### Solvable = strips into abelian layers

A radical formula builds the roots by adjoining roots one at a time — $\sqrt{\;}$, then $\sqrt[3]{\;}$, and so on. Each adjoined radical peels off exactly **one clean, commutative (abelian) layer** of the root-symmetry. So a formula in radicals exists **if and only if** the Galois group can be taken completely apart, one abelian layer at a time, down to nothing. Such a group is called **solvable**: it admits a chain $G \rhd N_1 \rhd N_2 \rhd \cdots \rhd \{e\}$ in which each subgroup is **normal** in the one above it (so each step is a legal division) and every successive **quotient is abelian** (so each peeled layer is commutative).

> [!info] The one fact borrowed from field theory
> Why does adjoining a radical correspond to peeling an *abelian* layer? That precise link between *equations* and *groups* is the **Galois correspondence** (subfields of the number system ↔ subgroups of the Galois group), and proving it is the content of a first university course in Galois theory. We take just that one bridge on faith here — adjoining an $n$-th root contributes exactly a cyclic, hence abelian, layer $C_n$ — and everything else is the pure group theory built above. The human drama behind it all is in [[Stories/Galois at Twenty]].

Walk up the table and watch it peel — and jam:

- **$S_2$** is already abelian: one layer, done. → the quadratic formula (one square root).
- **$S_3$** (order 6) strips as $S_3 \rhd A_3 \rhd \{e\}$, quotients of order $2$ and $3$, both abelian. Solvable. → Cardano.
- **$S_4$** (order 24) strips through a slightly longer chain — explicitly $S_4 \rhd A_4 \rhd V_4 \rhd \{e\}$, dropping through a four-element subgroup $V_4$ — with every quotient abelian. Solvable. → Ferrari.
- **$S_5$** (order 120) **jams.** Inside it sits $A_5$ (order $60$, the even permutations of $5$ things) — and $A_5$ is exactly the killer just named: a **non-abelian atom** (simple, so there is no normal subgroup to peel; and non-commutative, so no abelian layer hides inside). The dismantling halts dead at $A_5$, so $S_5$ is **not** solvable.

**So the "why" is structure, not size.** It is not that $S_5$ is *large* — a group can be huge and perfectly solvable (indeed $S_4$, order 24, strips cleanly). It is that $S_5$'s chain of abelian pieces *breaks* at the atom $A_5$. And this only gets worse: $A_6, A_7, \dots$ are all simple too, so **every** $S_n$ with $n \ge 5$ is unsolvable, of any size.

The conclusion is absolute: **no tower of $+, -, \times, \div, \sqrt[n]{\;}$ can ever produce the roots of the general quintic** — not "no one has found the formula yet," but *there is provably none* — because the roots' symmetry group contains an indivisible non-abelian atom. That is [[Stories/Abel the Other Boy Who Died Young|Abel]]'s 1824 impossibility and [[Stories/Galois at Twenty|Galois]]'s *why*, in one word: $A_5$.

---

## Group theory in your hands — solving a Rubik's cube

Set the abstractions aside for a problem millions of people actually meet: you have solved most of a Rubik's cube, and now you must fix the **last few pieces without wrecking everything you already did.** Turn faces at random and you destroy your progress. So how do the tutorials' memorised "algorithms" move three pieces and leave the other fifty-odd untouched? Group theory — the exact ideas on this page.

**The cube is a group.** Each move (a quarter-turn of one face) is an element; doing moves in sequence is the operation; undoing a move is its inverse; the solved cube is the identity $e$. A scramble is just some element $g$, and *solving* is finding a sequence of moves whose product is $g^{-1}$ — a word in the six face-turn generators that returns you to $e$. The whole group has about $4.3 \times 10^{19}$ elements, so blind trial is hopeless; you need structure.

**The trick every method uses is the commutator.** Do a short sequence $A$, then $B$, then undo $A$ (that is $A^{-1}$), then undo $B$ ($B^{-1}$): written out, $[A, B] = A\,B\,A^{-1}B^{-1}$. If $A$ and $B$ *commuted*, this would collapse to the identity — nothing would happen. They don't (the cube group is wildly non-abelian), and the beauty is that the *leftover* is **tiny and local**: a well-chosen commutator disturbs only a handful of pieces — often it cycles exactly **three** of them — and leaves the entire rest of the cube untouched. That is precisely the surgical tool the endgame needs. Every "algorithm" a speedcuber drills is a commutator, or a **conjugate** $A B A^{-1}$ ("set the pieces up, do the move, undo the setup") — the same two constructions, doing real work in your hands.

**And parity returns to tell you what is impossible.** You can *never* find a legal sequence that swaps just two pieces and fixes everything else — for the very same reason the [[Stories/Galois at Twenty|15-puzzle]] cannot swap its 14 and 15. A single swap is an **odd** permutation; legal cube moves only ever build **even** rearrangements of the pieces, so the smallest thing available is a $3$-cycle. If you have ever solved a cube down to exactly two swapped corners and been certain it was broken — it *was*: someone had popped a piece out and pushed it back wrong, landing the cube in a state the group forbids. Group theory told you, before you touched it, which end-states are reachable and which cannot exist.

That is group theory as a *tool*, not decoration: it hands you the exact moves that solve the cube, and explains why a "stuck" position genuinely cannot be solved. (And the same $\mathbb{Z}_{12}$ that runs the clock runs **music** too — transposing a song into a singable key is adding a constant mod $12$ to every note. You compute in a cyclic group every time you move a capo.)

---

## Where groups run the world

- **Noether's theorem — symmetry *is* conservation.** Every continuous symmetry of the laws of physics yields a conserved quantity; the symmetries form a (Lie) group. Time-translation → energy, space-translation → momentum, rotation → angular momentum. This is the exact content of the [[Angular Momentum|Noether trio]] in the mechanics bay — a group is the mathematical object *behind* "continuous symmetry."
- **The Standard Model** is built on the gauge group $U(1) \times SU(2) \times SU(3)$; the forces of nature are the bookkeeping of these symmetry groups.
- **Crystallography** — there are exactly **230** distinct space groups, and every crystal on Earth belongs to one. The classification is pure group theory.
- **Galois fields $\mathrm{GF}(p^n)$** — finite fields whose additive and multiplicative structures are groups; the arithmetic under Reed–Solomon error correction (every QR code, CD, deep-space probe) and the AES cipher. Galois's teenage toy, now guarding your traffic — the [[Stories/Galois at Twenty|full cash-out]] sits in his story.
- **Elliptic curves** carry a group law — you can "add" points on the curve — and that group, over a finite field, is the engine of **elliptic-curve cryptography**. Abel's elliptic functions and Galois's finite fields, meeting two centuries later inside your bank login.
- **The classification of finite simple groups** (completed ~2004, thousands of pages) lists every indivisible atom of finite symmetry — and ends with the **Monster**, a sporadic group of about $8\times10^{53}$ elements whose unexpected links to number theory ("monstrous moonshine") are still being mined.

---

## Worked examples

**Example 1 — a full small group.** Take $(\mathbb{Z}_6, +)$, order $6$. Element orders: $0$ has order $1$; $1$ and $5$ have order $6$ (generators); $2$ and $4$ have order $3$; $3$ has order $2$. Every one of these — $1, 2, 3, 6$ — **divides $6$**, as Lagrange demands. The subgroups are $\{0\}$ (order 1), $\{0,3\}$ (order 2), $\{0,2,4\}$ (order 3), and all of $\mathbb{Z}_6$ (order 6): exactly one for each divisor of $6$, a special feature of cyclic groups.

**Example 2 — non-abelian in two lines.** In $S_3$, let $r = (1\,2\,3)$ and $s = (1\,2)$. Then $rs = (1\,2\,3)(1\,2) = (1\,3)$, while $sr = (1\,2)(1\,2\,3) = (2\,3)$. Since $(1\,3) \ne (2\,3)$, $\;rs \ne sr$ — the group is non-abelian. (Compose right-to-left; check by tracking where each number goes.)

**Example 3 — spotting an isomorphism.** The fourth roots of unity $\{1, i, -1, -i\}$ under multiplication and $(\mathbb{Z}_4, +)$ under addition are isomorphic via $i^k \mapsto k$: multiplying roots adds exponents mod $4$, which is exactly addition mod $4$. Both are $C_4$.

**Example 4 — Lagrange as a lock.** A group of order $7$ has no proper non-trivial subgroup, because the only divisors of $7$ are $1$ and $7$. Therefore any non-identity element generates the whole group: **every group of order $7$ is cyclic**, isomorphic to $C_7$. The same holds for any prime order.

---

## Exam Notes

Group theory sits **beyond the core** A-Level and is absent from IB and AP, but it is a named topic on several **Further Mathematics** specifications, and a first-year university staple.

### A-Level Further Mathematics

- **Edexcel Further Pure 2 (9FM0, option paper)** — *Groups*: the four axioms; order of a group and of an element; **cyclic groups** and generators; **subgroups**; **Lagrange's theorem** and its use to constrain possible subgroup orders; the group tables (Cayley tables) of small groups; **isomorphism** of groups (matching Cayley tables / preserving structure). Typical questions: "Show that the given set forms a group under the stated operation," "list the subgroups and verify Lagrange," "show these two groups of order $n$ are (not) isomorphic."
- **AQA / MEI Further Pure options** carry a comparable groups unit (axioms → cyclic → Lagrange → isomorphism).
- **Not** on Cambridge 9231 (current Further Pure), IB AA/AI, or AP.

### Beyond high school — University

A first abstract-algebra course develops normal subgroups, quotient groups, the isomorphism theorems, group actions and orbit–stabiliser, Sylow's theorems, and leads into **Galois theory** (the solvability payoff above) and **representation theory** (groups acting as matrices — the bridge to physics).

---

## Connections

- **Prerequisite:** [[Symmetry (Vocab)]] — the concrete rotations/reflections of polygons, turned here from "the symmetries of a shape" into $D_n$, $C_n$, and the abstract group.
- **Prerequisite / motivation:** [[Stories/Galois at Twenty]] + [[Stories/Abel the Other Boy Who Died Young]] — the human origin; the two boys who opened the door and the theorem ($A_5$ unsolvable) their deaths bought.
- **Foundational bridge:** [[Forward Reading and Problem Discovery]] — a group *is* the hunter's "what doesn't change?" made into an object; invariance as a computable structure.
- **Components:** [[Roots of Unity]] — the $n$-th roots as the cyclic group $C_n$; [[Complex Numbers]] — where those roots live.
- **Application (physics):** [[Angular Momentum]] — the Noether trio; continuous symmetry groups and conservation laws.
- **Application (constructibility):** [[Heptadecagon]] — a regular $n$-gon is constructible iff the Galois group of $x^n-1$ is a $2$-group; Gauss's 17-gon is proto-group-theory.
- **Application (the quintic):** [[Cubic Graphs]] §"The Galois Bombshell" — solvability by radicals as a statement about the Galois group.
- **Application (CS):** finite fields $\mathrm{GF}(2^n)$ (additive groups) are the arithmetic under Reed–Solomon and AES — the cash-out detailed in [[Stories/Galois at Twenty]].
- **Cross-domain:** [[Information Theory]] — the vault's information-and-coding half, where structure like this guards modern communication.
- **Eponymy:** [[Stories/Stigler's Law of Eponymy]] — "abelian," the honest lowercase eponym for the commutative case.

---

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $(G, *)$ | `(G, *)` | a group: set $G$ with operation $*$ |
| $\lvert G \rvert$ | `\lvert G \rvert` | order (number of elements) of $G$ |
| $e$ | `e` | identity element |
| $a^{-1}$ | `a^{-1}` | inverse of $a$ |
| $\langle g \rangle$ | `\langle g \rangle` | cyclic group generated by $g$ |
| $C_n$ | `C_n` | cyclic group of order $n$ |
| $D_n$ | `D_n` | dihedral group of order $2n$ (symmetries of a regular $n$-gon) |
| $S_n$ | `S_n` | symmetric group: all permutations of $n$ objects, order $n!$ |
| $A_n$ | `A_n` | alternating group: even permutations, order $n!/2$ |
| $H \le G$ | `H \le G` | $H$ is a subgroup of $G$ |
| $[G:H]$ | `[G:H]` | index: number of cosets of $H$ in $G$ |
| $G \cong H$ | `G \cong H` | $G$ is isomorphic to $H$ |
| $G/N$ | `G/N` | quotient of $G$ by a normal subgroup $N$ |
| $G \rhd N$ | `G \rhd N` | $N$ is a **normal** subgroup of $G$ (the links of a solvable chain) |
| $\mathbb{Z}_n$ | `\mathbb{Z}_n` | integers modulo $n$ under addition ($\cong C_n$) |
