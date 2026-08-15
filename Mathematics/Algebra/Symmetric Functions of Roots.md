---
chinese: 根的对称函数 (gēn de duìchèn hánshù)
prerequisites:
  - "[[Quadratic Equations]]"
  - "[[Polynomial Division]]"
  - "[[Binomial Theorem]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/algebra
  - level/A-Level
  - curriculum/A-Level
  - curriculum/Cambridge-9231
  - syllabus/9231-1-1
  - type/deep
  - type/theorem
  - type/proof
  - notation/sigma
  - misconception/you-must-find-the-roots
  - misconception/symmetric-is-a-coincidence
  - misconception/substitution-must-be-given
  - misconception/sum-of-squares-is-square-of-sum
  - misconception/quartic-needs-new-theory
---

# Symmetric Functions of Roots 根的对称函数

> *You have been using this theorem since you were about thirteen. To factorise $x^2+5x+6$ you hunt for two numbers that **add to 5** and **multiply to 6**, and you find $2$ and $3$. Nobody ever told you why that hunt works. It works because the coefficients of a polynomial literally **are** the sums and products of its roots — and nothing in that fact cares about the degree being 2.*
>
> *Unlocked properly, it does something that looks impossible. Here is a quartic: $x^4 + 2x^3 - 1 = 0$. Find the sum of the fourth powers of its four roots. You cannot factorise it; its roots are two ugly irrationals and a complex pair, and no amount of staring will produce them. A real exam asked exactly this, allowed five marks, and expected an answer in a few lines — because **the roots were never the point.***
>
> *Everything you can legitimately ask about the roots is already sitting in the coefficients. What follows is why that is true, why it can only ever be true for certain questions, and what it buys you well beyond an exam hall — including why a scratched CD still plays.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| root | 根 | a value of $x$ making the polynomial zero |
| coefficient | 系数 | the numbers multiplying each power of $x$ |
| symmetric function | 对称函数 | an expression unchanged when the roots are swapped around |
| elementary symmetric function | 初等对称多项式 | the sums $\sum\alpha$, $\sum\alpha\beta$, $\sum\alpha\beta\gamma$, … |
| Vieta's formulas | 韦达定理 | the relations between roots and coefficients |
| substitution | 代换 | replacing $x$ to build a new equation with related roots |
| monic | 首一 | leading coefficient equal to 1 |
| permutation | 置换 | a re-labelling of the roots |
| power sum | 幂和 | $\sum\alpha^k$ — the roots each raised to the same power, added |
| discriminant | 判别式 | the symmetric quantity that is zero exactly when two roots coincide |
| eigenvalue | 特征值 | a root of a matrix's characteristic polynomial |

## The one theorem, built rather than quoted

Everything on this page comes from a single observation, and it is worth watching it happen rather than being handed the result.

If a quadratic $ax^2 + bx + c$ has roots $\alpha$ and $\beta$, then it vanishes exactly when $x = \alpha$ or $x = \beta$, so it must be a multiple of $(x-\alpha)(x-\beta)$ — and matching the leading term fixes the multiple as $a$:

$$ax^2 + bx + c = a(x-\alpha)(x-\beta)$$

Now expand the right-hand side and stare at what appears:

$$a(x-\alpha)(x-\beta) = a\Big[x^2 - (\alpha+\beta)x + \alpha\beta\Big] = ax^2 - a(\alpha+\beta)\,x + a\alpha\beta$$

Two polynomials are equal only if their coefficients match, so $b = -a(\alpha+\beta)$ and $c = a\alpha\beta$:

$$\alpha + \beta = -\frac{b}{a}, \qquad \alpha\beta = \frac{c}{a}$$

**Nothing was proved about roots. The expansion did all the work** — the coefficients of a polynomial *are* the sums and products of its roots, because that is what multiplying out brackets produces. [[Quadratic Equations]] states this case as Vieta's formulas; the point here is that it never depended on the degree being 2.

### The cubic

Same argument, one more bracket. With roots $\alpha, \beta, \gamma$:

$$ax^3+bx^2+cx+d = a(x-\alpha)(x-\beta)(x-\gamma)$$

Expanding, each term of the product picks either $x$ or $-\alpha$ from each bracket. Choose $x$ from all three and you get $x^3$; choose $-\alpha$ from exactly one and you get the $x^2$ terms, and so on:

$$= a\Big[x^3 - (\alpha+\beta+\gamma)x^2 + (\alpha\beta+\beta\gamma+\gamma\alpha)x - \alpha\beta\gamma\Big]$$

$$\boxed{\ \sum\alpha = -\frac{b}{a}, \qquad \sum\alpha\beta = \frac{c}{a}, \qquad \alpha\beta\gamma = -\frac{d}{a}\ }$$

> [!note] What the $\sum$ is doing there
> $\sum$ is shorthand for *"add up every term of this shape, over all the roots."* Unpacked for a cubic, the boxed line says exactly
> $$\alpha+\beta+\gamma = -\frac{b}{a}, \qquad \alpha\beta+\beta\gamma+\gamma\alpha = \frac{c}{a}, \qquad \alpha\beta\gamma = -\frac{d}{a}$$
> The middle one is the one to watch: it means **every distinct pair**, so three terms for a cubic and **six** for a quartic ($\alpha\beta$, $\alpha\gamma$, $\alpha\delta$, $\beta\gamma$, $\beta\delta$, $\gamma\delta$) — and a common slip is writing only $\alpha\beta+\beta\gamma+\gamma\delta+\delta\alpha$, missing the two "diagonal" pairs. The shorthand is safe precisely because the order of the terms never matters — which turns out to be the key to the entire topic.

### The quartic, and the pattern

With roots $\alpha,\beta,\gamma,\delta$ and $ax^4+bx^3+cx^2+dx+e$:

$$\sum\alpha = -\frac{b}{a}, \qquad \sum\alpha\beta = \frac{c}{a}, \qquad \sum\alpha\beta\gamma = -\frac{d}{a}, \qquad \alpha\beta\gamma\delta = \frac{e}{a}$$

There is no fourth thing to memorise. **The pattern is forced by the expansion**: taking $k$ of the $-\alpha$'s from $n$ brackets produces every product of $k$ roots, carrying $(-1)^k$ with it. So the $k$-th relation is

$$\sum(\text{products of } k \text{ roots}) \;=\; (-1)^k \frac{\text{coefficient of } x^{\,n-k}}{a}$$

**Use it immediately, on a quartic you have never seen.** Take $3x^4 - 12x^3 + 5x^2 + 7x - 2 = 0$, so $n = 4$ and $a = 3$. Walk $k$ from 1 to 4, each time reading off the coefficient of $x^{4-k}$:

| $k$ | coefficient of $x^{4-k}$ | sign $(-1)^k$ | the relation |
|---|---|---|---|
| 1 | $x^3$: $-12$ | $-$ | $\sum\alpha = -\dfrac{-12}{3} = 4$ |
| 2 | $x^2$: $5$ | $+$ | $\sum\alpha\beta = \dfrac{5}{3}$ |
| 3 | $x^1$: $7$ | $-$ | $\sum\alpha\beta\gamma = -\dfrac{7}{3}$ |
| 4 | $x^0$: $-2$ | $+$ | $\alpha\beta\gamma\delta = \dfrac{-2}{3}$ |

Four true statements about four numbers nobody has computed, in about ten seconds. Signs alternate starting from minus; if you forget which way, re-derive the quadratic in five seconds — $(x-1)(x-2) = x^2 - 3x + 2$, sum 3 appearing as $-(-3)$, product 2 appearing as $+2$.

> [!tip] Sanity check every time
> Write down a polynomial whose roots you know and test your formula on it. $(x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x - 6$: sum of roots $6 = -(-6)$ ✓, sum of pairs $2+6+3 = 11$ ✓, product $6 = -(-6)$ ✓. Ten seconds, and it catches every sign error you will ever make on this topic.

## Why only *symmetric* things — the question behind the question

Now the part that turns a formula sheet into understanding, and it starts with a hunter's question.

**The roots have no names.** When we write "let the roots be $\alpha, \beta, \gamma$," we are choosing labels that the equation itself does not supply. The polynomial $x^3 - 6x^2 + 11x - 6$ has roots $1, 2, 3$ — but calling them $\alpha=1,\beta=2,\gamma=3$ or $\alpha=3,\beta=1,\gamma=2$ describes the same equation equally well. The labelling is ours; the equation is indifferent.

![[roots-permutation-invariance.svg|697]]

So ask the invariant question: **what survives every re-labelling?**

- $\alpha$ alone does not. Relabel and it becomes a different number.
- $\alpha - \beta$ does not. Swap the two and it changes sign.
- $\alpha+\beta+\gamma$ **does.** Shuffle the labels however you like — the sum is the same.
- $\alpha^2+\beta^2+\gamma^2$, $\alpha\beta\gamma$, $\frac1\alpha+\frac1\beta+\frac1\gamma$ all survive too.

An expression unchanged by every re-labelling is called **symmetric**, and here is the consequence that governs this whole topic:

> **Only symmetric functions of the roots can be computed from the coefficients** — because the coefficients cannot tell the roots apart either.

That is not a rule to obey; it is a fact you can now *predict with*. It explains why every exam question on this topic asks for $\sum\alpha^2$, $\sum\alpha^3$, $\sum\frac1\alpha$, $\sum\alpha^4$ and never for $\alpha$ by itself — the second question has no answer expressible in the coefficients, so it cannot be set. It also tells you instantly whether a strange-looking request is answerable: if shuffling the labels leaves it alone, the coefficients know it.

And the four boxed relations are not just *some* symmetric functions. They are the **elementary** ones — the building blocks from which every other symmetric polynomial can be assembled by ordinary algebra. That is exactly why any of this works.

## What is it actually for?

A fair question, and "an exam asks it" is not an answer. The move being learned here — **compute the answer without ever computing the objects** — is one of the most reusable in mathematics, and these relations turn up wherever a polynomial's roots matter but nobody wants to find them.

### It is already how you factorise

"Two numbers that add to $5$ and multiply to $6$" *is* $\alpha+\beta = -b/a$ and $\alpha\beta = c/a$, with $a=1$, run backwards. You have been using the degree-2 case since the day you met quadratics. Everything on this page is that same habit with the ceiling taken off.

### A matrix hands you its eigenvalues' sum and product for free

Every square matrix has a **characteristic polynomial** whose roots are its eigenvalues $\lambda$ — the numbers describing how that matrix stretches space, and the reason matrices are used at all in mechanics, statistics, quantum theory and graphics. Finding them means solving that polynomial: a cubic for a $3\times3$. The relations say you often need not bother:

$$\sum\lambda = \operatorname{trace}(M)\ \ (\text{just add the diagonal}), \qquad \prod\lambda = \det(M)$$

Take $M = \begin{pmatrix} 2 & 1 & 0\\ 1 & 3 & 1\\ 0 & 1 & 2\end{pmatrix}$. The diagonal adds to $7$ and the determinant is $8$, so **before writing a single equation** you know the three eigenvalues sum to $7$ and multiply to $8$. (They turn out to be $1, 2, 4$ — and $1+2+4 = 7$, $1\times2\times4 = 8$.) Push one step further with the square-a-sum move: $M^2$ has eigenvalues $\lambda^2$, so $\sum\lambda^2 = \operatorname{trace}(M^2) = 21$, and indeed $1+4+16 = 21$.

This is not decoration. It is how anyone doing numerical work checks an eigenvalue computation: add the answers and see whether the trace comes back. A slip announces itself in one line.

### Engineers read stability off the coefficients

A control system — a drone holding altitude, a car's cruise control, an amplifier — is governed by the roots of a characteristic polynomial, called its **poles**. If any pole has a positive real part the system runs away, and if the poles have large negative real parts it settles fast. The sum of the poles is $-b/a$, so a single coefficient reports the total damping. Better still, the classical stability tests decide *whether every root has negative real part* from the coefficients alone, without ever locating a root — because "are they all on the correct side?" is a question the coefficients are entitled to answer.

### Why a scratched CD still plays

The best one — and small enough to run by hand. Data on a CD, a QR code, or a signal from a spacecraft carries extra symbols so that damage can be repaired: **Reed–Solomon** coding. The decoder's difficulty is that it cannot see *where* the damage is. Watch it find out. *(How anyone came to want this, from a ruined weekend in 1947 to a QR code surviving a coffee stain, is [[Stories/A Fight With the Inevitable Errors]]; the school-syllabus layer beneath it — parity, checksums, check digits — is [[Error Detection and Correction]].)*

**Work with the numbers $0$ to $10$**, adding and multiplying as usual and then taking the remainder on division by $11$ — every "$\equiv$" below means *after that remainder*.

**Name the letters before using any of them.** Schools drill *let $x$ be the number of apples* at thirteen and then quietly stop exactly when the letters start to multiply, which is where this subject loses people:

| symbol | what it stands for |
|---|---|
| $i$ | a **position** in the block, running $1$ to $10$ |
| $c_i$ | the symbol the encoder **sent** in position $i$ — $c$ for *codeword* |
| $r_i$ | the symbol that **arrived** in position $i$ — $r$ for *received*. If nothing went wrong, $r_i = c_i$ |
| $S_1, S_2$ | the two totals the **receiver recomputes** from what arrived — $S$ for *syndrome*, a symptom that betrays a hidden fault |
| $X_1, X_2$ | the two **damaged positions**. These are the unknowns, and finding them is the entire job |
| $p_1, p_2$ | the **power sums** $X_1+X_2$ and $X_1^{\,2}+X_2^{\,2}$ |
| $e_1, e_2$ | the **elementary symmetric functions** $X_1+X_2$ and $X_1X_2$ |
| $x$ | the variable of the quadratic built at the end, whose roots will be $X_1$ and $X_2$ |

Now send eight digits — $3\,1\,4\,1\,5\,9\,2\,6$ — and let the encoder append two more symbols, chosen so that two weighted totals of the sent block come out at exactly zero:

$$\sum_{i=1}^{10} c_i \cdot i \equiv 0, \qquad \sum_{i=1}^{10} c_i \cdot i^2 \equiv 0 \pmod{11}$$

The two symbols that achieve it are $7$ and $5$, so the block sent is $c = 3\,1\,4\,1\,5\,9\,2\,6\,7\,5$. Now scratch it: the symbols in **positions 3 and 7** each arrive one too big, so $X_1 = 3$ and $X_2 = 7$ — which is exactly what the receiver does *not* know. All it holds is $r$:

$$3\quad 1\quad \mathbf{5}\quad 1\quad 5\quad 9\quad \mathbf{3}\quad 6\quad 7\quad 5$$

**Step 1 — measure, then notice what you have measured.** The receiver runs the encoder's two totals again, this time on $r$ instead of $c$. They no longer vanish:

$$S_1 = \sum_{i=1}^{10} r_i \cdot i = 285 \equiv 10, \qquad S_2 = \sum_{i=1}^{10} r_i \cdot i^2 = 2115 \equiv 3 \pmod{11}$$

Why does that help? Each arrived symbol is the sent one plus whatever the scratch added, so $r_i = c_i + (\text{damage at } i)$. The $c_i$ part contributes nothing to either total — the encoder arranged precisely that — so **only the damaged positions survive**. Each is off by exactly $1$, so each contributes one copy of $i$ to $S_1$ and one copy of $i^2$ to $S_2$, and the two surviving positions are $X_1$ and $X_2$:

$$S_1 = X_1 + X_2, \qquad S_2 = X_1^{\,2} + X_2^{\,2}$$

**Read that again in the card's own language: $S_1$ and $S_2$ are $p_1$ and $p_2$** — power sums of two numbers the receiver has never seen. So it holds $p_1 = 10$ and $p_2 = 3$.

**Step 2 — power sums to elementary symmetric functions.** Technique 1's square-a-sum identity, rearranged to give $e_2$ instead of $p_2$:

$$e_1 = p_1 = 10, \qquad e_2 = \frac{p_1^{\,2} - p_2}{2} = \frac{100-3}{2} \equiv \frac{1-3}{2} = -1 \equiv 10 \pmod{11}$$

(Halving was safe here because $-2$ is even; in general one multiplies by $2^{-1} = 6$, since $2 \times 6 = 12 \equiv 1$.)

**Step 3 — build the equation whose roots are what you want.** Straight from the boxed relations: a quadratic whose roots are $X_1$ and $X_2$ is $x^2 - e_1x + e_2$, so

$$x^2 - 10x + 10 \equiv x^2 + x + 10 \pmod{11}$$

Nothing here knows what $X_1$ and $X_2$ are. The quadratic was built entirely out of $e_1$ and $e_2$, which came from $p_1$ and $p_2$, which came from $r$.

**Step 4 — solve it.** Substituting $x = 1, 2, \ldots, 10$ asks each position in turn *are you one of the roots?* Ten substitutions, and real hardware does exactly this under the name of a **Chien search**:

![[reed-solomon-locator.svg|760]]

Zero at $x=3$ and at $x=7$ — check by hand: $9-30+10 = -11 \equiv 0$ and $49-70+10 = -11 \equiv 0$. So $X_1 = 3$ and $X_2 = 7$: the damaged positions, which is what we planted at the start. Correct them, and $3\,1\,4\,1\,5\,9\,2\,6$ comes back intact — eight digits of $\pi$, repaired by a machine that never saw the damage. The quadratic pointed at it.

A real decoder carries one more unknown per error, because it must also work out *how far* each symbol is off, which doubles the syndromes it needs. The half shown here — finding **where** — is exactly this, running in every optical drive and QR scanner a few thousand times a second.

> [!tip] Would it still work counting positions from zero?
> No — and the reason is worth more than the answer.
>
> These positions are not merely labels; they get **multiplied**. Position $i$ enters $S_1$ as $i$ and enters $S_2$ as $i^2$. So a damaged symbol at position $0$ would contribute $1 \times 0 = 0$ to the first total and $1 \times 0^2 = 0$ to the second: **the syndromes would not move at all.** Damage there is perfectly invisible, and the decoder would pronounce a corrupted block clean. Rebuild the example with positions $0$ to $9$ and that is exactly what happens — corrupt the symbol at position $0$ and the receiver still measures $S_1 = S_2 = 0$.
>
> Which is why a real Reed–Solomon code labels its positions with the **powers** $\alpha^0, \alpha^1, \alpha^2, \ldots$ of a fixed element rather than with $0, 1, 2, \ldots$ — powers are never zero. The array holding the block may be 0-indexed all it likes; what has to dodge zero is the field element doing the multiplying. It is also why such a code over a field of $q$ elements tops out at $q-1$ symbols: **that "$-1$" is the excluded zero.** Ours used $q = 11$ and had exactly ten positions.
>
> Zero still earns its keep, though. If only *one* symbol is damaged then $e_2 = 0$, so the quadratic factors as $x(x - X_1)$ — a root of $0$ appears, is thrown away as not-a-position, and the decoder thereby learns it was dealing with one error rather than two. If nothing is damaged at all, both roots are $0$ and the block is declared clean. The forbidden value is what reports *fewer errors than I was built for*.
>
> Now set that beside [[Arrays]], where counting from zero is exactly **right**, and the contrast is the real lesson. There the index is an **offset added** to a base address, and adding zero is harmless — it is the identity, which is precisely why the first element sits at offset $0$. Here the index is a **multiplier**, and zero is the one number that annihilates whatever it touches. Same word, opposite verdicts, and the deciding question is only ever *is this index added, or multiplied?*

### And the habit underneath

Notice what the last three have in common: nobody solved anything. Each question was answered by finding a quantity that *cannot change* — here, cannot change when the labels are shuffled — and computing with that instead of with the thing you cannot reach. It is the same instinct as conservation of energy: you never track every molecule in a gas, you track the quantity that stays put. Learning to ask **"what is invariant here?"** before "what is unknown here?" will outlast this topic by a very long way.

## Three techniques, and when each is the right one

### 1. Rebuild it from the elementary ones

Most requests are one algebraic step from what you already have. The workhorse is the square of a sum:

$$(\alpha+\beta+\gamma)^2 = \alpha^2+\beta^2+\gamma^2 + 2(\alpha\beta+\beta\gamma+\gamma\alpha) \quad\Longrightarrow\quad \boxed{\ \sum\alpha^2 = \left(\sum\alpha\right)^2 - 2\sum\alpha\beta\ }$$

Do not memorise the rearranged version — memorise that squaring a sum produces the squares *plus twice the cross terms*, and rearrange on the spot. The same move handles the others:

| Wanted | Built from | How |
|---|---|---|
| $\sum \alpha^2$ | $\left(\sum\alpha\right)^2 - 2\sum\alpha\beta$ | square the sum |
| $\sum \dfrac{1}{\alpha}$ | $\dfrac{\sum\alpha\beta}{\alpha\beta\gamma}$ | put over a common denominator |
| $\sum \dfrac{1}{\alpha^2}$ | $\left(\sum\dfrac1\alpha\right)^2 - 2\dfrac{\sum\alpha}{\alpha\beta\gamma}$ | the same square-a-sum move, one level down |
| $(\alpha+\beta)(\beta+\gamma)(\gamma+\alpha)$ | $\sum\alpha \sum\alpha\beta - \alpha\beta\gamma$ | expand and collect |

### 2. Use the equation itself — the technique nobody expects

This one is worth more than the rest combined, and it follows from a sentence so obvious it gets skipped: **every root satisfies the equation.** If $\alpha$ is a root of $x^4+2x^3-1=0$, then

$$\alpha^4 + 2\alpha^3 - 1 = 0$$

is a true statement about $\alpha$ — a recipe for trading a high power for lower ones. Rearranged, $\alpha^4 = 1 - 2\alpha^3$. Sum that over all four roots and $\sum\alpha^4$ collapses into things you already know. Multiply the whole equation by $\alpha$ first and you reach the fifth powers:

$$\alpha^5 + 2\alpha^4 - \alpha = 0 \quad\Longrightarrow\quad \sum\alpha^5 = \sum\alpha - 2\sum\alpha^4$$

Any power you like is reachable this way, by multiplying through by whatever power of $x$ you need. It is the cheapest tool on the page and the least taught.

### 3. Build a new equation whose roots are what you want

The most powerful move, and the one the syllabus names outright. If you can construct a polynomial whose roots are exactly $\alpha^4, \beta^4, \gamma^4, \delta^4$, then **its coefficients hand you $\sum\alpha^4$ and $\sum\alpha^4\beta^4$ for free** — by the same boxed relations, applied to the new equation.

That is the insight that makes substitution more than a party trick: *a substitution is not a separate topic, it is how you compute a symmetric function that is too awkward to assemble by hand.*

## Substitution — the principle, then the three cases

**The principle is one sentence.** You want an equation whose roots are $y = f(\alpha)$ for each old root $\alpha$. Invert the relation to get $x$ in terms of $y$, substitute it into the original equation, and tidy. Every old root $\alpha$ produces a $y$ satisfying the new equation, and the degree is unchanged, so the new equation's roots are precisely the transformed ones.

Why it works, in one line: if $x = g(y)$ is the inverse relation, then $P(g(y)) = 0$ holds exactly when $g(y)$ is a root of $P$ — that is, exactly when $y$ is a transformed root.

**The syllabus warns you explicitly that for the easy cases the substitution will *not* be given.** Those three are:

| New roots | Set | Substitute |
|---|---|---|
| **reciprocals** $\dfrac{1}{\alpha}$ | $y = \dfrac1x$ | $x = \dfrac1y$ — in practice, reverse the coefficients |
| **squares** $\alpha^2$ | $y = x^2$ | $x = \sqrt{y}$, then isolate the surd and square to clear it |
| **linear shift** $k\alpha + m$ | $y = kx+m$ | $x = \dfrac{y-m}{k}$, then expand with [[Binomial Theorem\|the binomial theorem]] |

Two practical notes that cost marks:

- **Squares: never leave a $\sqrt{y}$.** Split the equation so all surd terms are on one side and everything else on the other, *then* square. Squaring a sum of two surd terms is the standard way to make a mess.
- **Shifts: expect the binomial expansion**, and expect it to be the bulk of the work. $\left(\frac{y-m}{k}\right)^4$ is a fourth-power expansion, and the marks are in doing it accurately.

## Worked examples

The examples below are two real questions — the second one in three parts — quoted with their own command words, because on this topic the command word tells you which technique is wanted, and one of them asks for two different things inside a single sentence.

### Example 1 — the theorem run backwards [6 marks]

> **9231 Paper 11, November 2021, Q1.** *It is given that $\alpha+\beta+\gamma = 3$, $\alpha^2+\beta^2+\gamma^2 = 5$, $\alpha^3+\beta^3+\gamma^3 = 6$. The cubic equation $x^3+bx^2+cx+d = 0$ has roots $\alpha, \beta, \gamma$. **Find** the values of $b$, $c$ and $d$.*

The syllabus's "problems involving unknown coefficients", and some version of it has been a whole question in six papers since 2021. Nothing new is needed — the relations are simply read right to left. The equation is monic, so $a=1$ throughout.

**Tool: the boxed relations.** $\sum\alpha = -\dfrac{b}{a} = -b$, and we are told $\sum\alpha = 3$:

$$b = -3$$

**Tool: square the sum**, since we are given $\sum\alpha^2$ and want $\sum\alpha\beta$, which is $c$:

$$\sum\alpha^2 = \left(\sum\alpha\right)^2 - 2\sum\alpha\beta \quad\Longrightarrow\quad 5 = 3^2 - 2c \quad\Longrightarrow\quad c = 2$$

**Tool: every root satisfies the equation, technique 2.** Each root obeys $\alpha^3 + b\alpha^2 + c\alpha + d = 0$. Write that statement out three times, once per root, and add the three lines — noting that the constant $d$ appears once in each, so it contributes $3d$:

$$\sum\alpha^3 + b\sum\alpha^2 + c\sum\alpha + 3d = 0$$

$$6 + (-3)(5) + 2(3) + 3d = 0 \quad\Longrightarrow\quad -3 + 3d = 0 \quad\Longrightarrow\quad d = 1$$

So the equation is $x^3 - 3x^2 + 2x + 1 = 0$. Its three roots are unpleasant irrationals, and at no point did we go anywhere near them.

### Example 2 — building a new equation [5 marks]

> **9231 Paper 13, November 2024, Q3.** *The quartic equation $x^4 + 2x^3 - 1 = 0$ has roots $\alpha, \beta, \gamma, \delta$.*
> **(a)** ***Find** a quartic equation whose roots are $\alpha^4, \beta^4, \gamma^4, \delta^4$ **and state the value of** $\alpha^4+\beta^4+\gamma^4+\delta^4$.* [5]

Two command words, two separate demands, both marked: an **equation** first, then a **value**. Before starting, read the original's relations off its coefficients ($a=1, b=2, c=0, d=0, e=-1$):

$$\sum\alpha = -2, \qquad \sum\alpha\beta = 0, \qquad \sum\alpha\beta\gamma = 0, \qquad \alpha\beta\gamma\delta = -1$$

**Tool: substitution, technique 3.** Name what the new roots are: $y = x^4$. To substitute we need $x$ written in terms of $y$, so invert that:

$$x = y^{1/4}$$

**Tool: substitute into the original, then look at the damage.** Replace every $x$ in $x^4 + 2x^3 - 1 = 0$:

$$\left(y^{1/4}\right)^4 + 2\left(y^{1/4}\right)^3 - 1 = 0 \quad\Longrightarrow\quad y + 2y^{3/4} - 1 = 0$$

This is not yet a polynomial: $y^{3/4}$ is a fourth root in disguise. **It is the same obstacle as the "squares" substitution above**, and it takes the same fix — get the fractional power alone on one side, then raise both sides to whatever power kills it.

**Tool: isolate the fractional power, then clear it.** Move everything else across, then take the fourth power of both sides:

$$2y^{3/4} = 1 - y \quad\Longrightarrow\quad \left(2y^{3/4}\right)^4 = (1-y)^4 \quad\Longrightarrow\quad 16y^3 = (1-y)^4$$

The left side came out clean because $\left(y^{3/4}\right)^4 = y^3$ — the *denominator* of the fractional exponent is what chooses the power to raise by, every time.

**Tool: the binomial theorem**, $(1-y)^4 = 1 - 4y + 6y^2 - 4y^3 + y^4$:

$$16y^3 = 1 - 4y + 6y^2 - 4y^3 + y^4 \quad\Longrightarrow\quad \boxed{\ y^4 - 20y^3 + 6y^2 - 4y + 1 = 0\ }$$

**Tool: read the answer off the new equation.** Its roots are $\alpha^4, \beta^4, \gamma^4, \delta^4$, so their sum is $-b/a$ for *this* equation:

$$\sum\alpha^4 = -\frac{-20}{1} = \boxed{20}$$

No root of anything was ever found. The five marks land on the substitution, an equation free of radicals, the binomial expansion, the equation itself — the mark scheme says in as many words that it *must be an equation*, so write the "$= 0$" — and the value.

> [!tip] The same answer without touching fractional powers
> If $y^{3/4}$ makes you uneasy, let the equation do the inverting instead. Every root satisfies $x^4 = 1-2x^3$, so $y = 1-2x^3$, which rearranges to $x^3 = \dfrac{1-y}{2}$.
>
> Now $x$ has to be eliminated, and here is the way out: $x^{12}$ is reachable from both sides of the ledger, because it is $\left(x^3\right)^4$ *and* it is $\left(x^4\right)^3 = y^3$. Twelve is the first power that both $x^3$ and $x^4$ can climb to — the lowest common multiple of 3 and 4 — so it is the meeting point where $x$ disappears. Raise $x^3 = \frac{1-y}{2}$ to the fourth power:
> $$y^3 = \left(\frac{1-y}{2}\right)^4 = \frac{(1-y)^4}{16} \quad\Longrightarrow\quad 16y^3 = (1-y)^4$$
> The same equation, one line sooner.

### Example 3 — reaching a higher power [3 marks]

> **(b)** ***Find the value of** $\alpha^5+\beta^5+\gamma^5+\delta^5$.* [3]

Continuing from Example 2 — same quartic, same four roots, and $\sum\alpha = -2$ and $\sum\alpha^4 = 20$ are now known. Note the command word has changed: "find the value of" wants a number, not an equation, so this is not another substitution.

**Tool: every root satisfies the equation, technique 2.** Multiply $x^4+2x^3-1=0$ through by $x$ to lift every power by one:

$$x^5 + 2x^4 - x = 0 \quad\Longrightarrow\quad \alpha^5 = \alpha - 2\alpha^4 \ \text{ for each root}$$

**Tool: sum over all four roots**, and use what is already known:

$$\sum\alpha^5 = \sum\alpha - 2\sum\alpha^4 = (-2) - 2(20) = \boxed{-42}$$

### Example 4 — reusing the machine [2 marks]

> **(c)** ***Find the value of** $\alpha^8+\beta^8+\gamma^8+\delta^8$.* [2]

Still continuing from Example 2, and this time the quartic built there does all the work.

**Tool: recognise it as a sum of squares.** $\alpha^8 = \left(\alpha^4\right)^2$, so this is $\sum\alpha^2$ *for the equation built in Example 2* — reuse, not new work.

**Tool: the square-a-sum identity**, applied to the $y$-equation, whose relations are $\sum\alpha^4 = 20$ and $\sum\alpha^4\beta^4 = \frac{c}{a} = 6$:

$$\sum\alpha^8 = \left(\sum\alpha^4\right)^2 - 2\sum\alpha^4\beta^4 = 20^2 - 2(6) = 400 - 12 = \boxed{388}$$

Two marks, because everything needed was already on the page. **That is why part (a) was worth building carefully: the new equation is not the answer to one question, it is a machine that answers several.**

## Common misconceptions (teaching notes)

### 1. "I need to find the roots first"

The instinct from every earlier year of algebra, and it makes the question look impossible.

**Fix:** set the topic up with a quartic that visibly will not factorise, ask for $\sum\alpha^2$, and let them fail for two minutes before showing the one-line answer. The lesson has to be *felt*: the coefficients are not a route to the roots, they are a route **past** them.

### 2. "It just happens that these formulas are symmetric"

Treated as a coincidence, so students try to compute $\alpha$, or $\alpha - \beta$, and cannot see why it fails.

**Fix:** the labelling test. Write the roots of $x^3-6x^2+11x-6$ on three cards, shuffle them, and ask which requested quantities changed. $\alpha$ changed; $\alpha+\beta+\gamma$ did not. The coefficients cannot see a difference the shuffling makes, so neither can any formula built from them.

### 3. "The substitution will be given"

It very often is on other topics, and the syllabus is explicit that here it will not be for reciprocals, squares or linear functions.

**Fix:** drill *producing* the substitution from the requested roots, separately from using it. Ask only "what would you substitute?" for six different requests, and mark nothing else, until $y = 2x+1 \Rightarrow x = \frac{y-1}{2}$ is automatic.

### 4. "$\sum\alpha^2 = \left(\sum\alpha\right)^2$"

The single most common algebraic slip on the topic.

**Fix:** two numbers, ten seconds: $\alpha = 1, \beta = 2$ gives $\sum\alpha^2 = 5$ and $\left(\sum\alpha\right)^2 = 9$. The gap is $2\alpha\beta = 4$, which is where the correction term comes from and why it is there.

### 5. "A quartic needs new theory"

Students who learned the quadratic case as three memorised formulas expect four new ones for the quartic.

**Fix:** derive the cubic in front of them by expanding the brackets, then ask them to predict the quartic before you write it. When the prediction is right, the point has landed: there is one theorem, and it does not care about the degree.

## Exam Notes

### Cambridge 9231 Further Mathematics — **Further Pure 1, Paper 1**

**§1.1, which the syllabus calls *Roots of polynomial equations*,** has two learning objectives and is a reliable early question on the paper. Paper 1 is **compulsory for both AS and A Level**, so every candidate meets this.

- **Recall and use the relations between roots and coefficients** — "to evaluate symmetric functions of the roots **or to solve problems involving unknown coefficients**." That second half is the reverse direction, and it is not a footnote: it has been an entire question in at least six papers since 2021 (N21 P11 Q1, N21 P13 Q1, N23 P11 Q3, N23 P13 Q3, N25 P12 Q2, J26 P13 Q1), always in the same shape — a few power sums given, the coefficients wanted, worth 3 to 6 marks. **Restricted to degree 2, 3 or 4 only.**
- **Use a substitution to obtain an equation whose roots are related in a simple way** — and the syllabus states plainly that **substitutions will not be given for the easiest cases**, naming reciprocals, squares and simple linear functions. Producing the substitution is part of the mark.
- **Typical shape**, from the recent papers: a quartic, then two or three parts of escalating power ($\sum\alpha^4$, then $\sum\alpha^5$, then $\sum\alpha^8$), worth 4–5, 3 and 2 marks. The later parts reuse the earlier ones — so a wrong quartic in part (a) costs the whole question, and it is worth checking that equation before moving on.
- **Read the command word — it names the technique.** "*Find a quartic equation whose roots are…*" wants a substitution and an equation. "*Find the value of…*" wants a number, so substitution is usually the wrong tool and technique 2 the right one. "*Show that a cubic equation with roots… is…*" hands you the answer and marks only the working, so nothing may be skipped. And watch for one sentence carrying two demands — "*find a quartic equation … **and state the value of** …*" is two marks in one line, and the second is the one candidates walk past.
- **The mark scheme rewards method visibly**: a mark for a correct substitution, a mark for reaching an equation free of radicals, a mark for the binomial expansion, a mark for stating an *equation* (its guidance reads, in full, "Must be an equation"). Write the "= 0".
- **MF19 gives you nothing here.** No Vieta relations, no symmetric-function identities. This is a memorise-and-derive topic — which is exactly why the derivation-by-expansion above is worth more than the table.

### Other Further Mathematics specifications

Edexcel places roots of polynomials in **Further Pure 1**, AQA and OCR in their equivalent first further-pure papers, and OxAQA 9660 examines the same material. The content is identical everywhere; only the formula-sheet support varies, and no major board gives the relations away.

### Where this is *not* examined

**Not on Cambridge 9709** — single-maths A-Level stops at the quadratic case, which [[Quadratic Equations]] covers. **Not on IB Analysis and Approaches**, HL included, beyond the quadratic. **Not on AP Calculus or AP Precalculus** as a named topic. So a student arriving from any single-maths course has seen $\alpha+\beta = -b/a$ and nothing past it — the cubic and quartic extensions are genuinely new, even though the theorem behind them is the one they already met.

> [!info] Beyond syllabus — the sums of powers have their own machine
> Computing $\sum\alpha^k$ by hand gets ugly past the fourth power, and there is a systematic alternative: **Newton's identities**, which give each power sum from the elementary symmetric functions and the *previous* power sums.
>
> **Recall the two families**, since it has been a while since either was named. The **elementary symmetric functions** are the three the coefficients hand you directly, and for a cubic they are
> $$e_1 = \sum\alpha = \alpha+\beta+\gamma, \qquad e_2 = \sum\alpha\beta = \alpha\beta+\beta\gamma+\gamma\alpha, \qquad e_3 = \alpha\beta\gamma$$
> while the **power sums** are the things questions actually ask for, $p_k = \sum\alpha^k = \alpha^k+\beta^k+\gamma^k$. With those names, a cubic obeys
> $$p_1 = e_1, \qquad p_2 = e_1p_1 - 2e_2, \qquad p_3 = e_1p_2 - e_2p_1 + 3e_3$$
> and after that $p_k = e_1p_{k-1} - e_2p_{k-2} + e_3p_{k-3}$ forever.
>
> **Watch it run on an equation whose roots you already know**, $x^3-6x^2+11x-6 = 0$ with roots $1, 2, 3$, so $e_1 = 6$, $e_2 = 11$, $e_3 = 6$:
> $$p_1 = 6, \qquad p_2 = 6(6) - 2(11) = 14, \qquad p_3 = 6(14) - 11(6) + 3(6) = 36$$
> $$p_4 = 6(36) - 11(14) + 6(6) = 98, \qquad p_5 = 6(98) - 11(36) + 6(14) = 276$$
> Now check every line directly: $1+2+3 = 6$, $1+4+9 = 14$, $1+8+27 = 36$, $1+16+81 = 98$, $1+32+243 = 276$. All five agree, and each line cost three multiplications and no thought at all — which is the point of a recursion.
>
> That recursion is exactly technique 2 in disguise: multiply the equation by $x^{k-3}$ and sum over the roots. Which is why the technique feels like it ought to have a name. It does. And Example 1 is this same machine driven **backwards** — given the $p_k$, solve for the $e_k$, which are the coefficients.

> [!info] Beyond syllabus — the discriminant, and why the quintic has no formula
> **Start where you already know the answer.** The difference of two roots, $\alpha-\beta$, is not symmetric — swap the labels and it changes sign — but its **square** is. So $(\alpha-\beta)^2$ must be expressible in the coefficients, and one square-a-sum shows exactly how:
> $$(\alpha-\beta)^2 = (\alpha+\beta)^2 - 4\alpha\beta = \frac{b^2}{a^2} - \frac{4c}{a} = \frac{b^2-4ac}{a^2}$$
> **That is the [[Discriminant|discriminant]].** The $b^2-4ac$ you have used since IGCSE is nothing but $a^2(\alpha-\beta)^2$ wearing a disguise — and everything it tells you suddenly has a reason instead of a rule. It is zero exactly when $\alpha = \beta$, because that is when the gap between the roots is zero. It is negative exactly when $\alpha-\beta$ is imaginary, which is what a conjugate pair means.
>
> **The same object exists at every degree.** For a cubic it is $a^4(\alpha-\beta)^2(\beta-\gamma)^2(\gamma-\alpha)^2$, and for the tidy form $x^3+px+q$ it works out to $\Delta = -4p^3 - 27q^2$. It answers the same question and answers it *without solving anything*: $\Delta > 0$ means three distinct real roots, $\Delta < 0$ means one real root and a complex pair, $\Delta = 0$ means a repeated root. Test it on two cubics that differ by one number — $x^3-3x+1$ gives $\Delta = -4(-27) - 27(1) = 81 > 0$, so three real roots, while $x^3-3x+3$ gives $\Delta = 108 - 243 = -135 < 0$, so only one. Check that by hand and it holds: both curves turn at $x = \pm 1$, but $x^3-3x+1$ has its local minimum at $-1$ (below the axis) so it must cross three times, while $x^3-3x+3$ has its local minimum at $+1$ (above the axis) so it crosses once and leaves. This is what software is doing when it reports "3 real roots" before showing you any of them.
>
> And it is the doorway to the deepest result in the area. Notice that $(\alpha-\beta)(\beta-\gamma)(\gamma-\alpha)$ *without* the squares is **not** symmetric — one swap flips its sign — so it is not expressible in the coefficients, yet its square is. Functions that are *almost* symmetric, classified by which re-labellings preserve them, are the whole subject of **Galois theory**, and its answer is startling: for degree 5 and above there is no formula in radicals at all. Not undiscovered — impossible. Everything on this page works precisely because degrees 2, 3 and 4 are where the symmetry stays simple enough, which is exactly why the syllabus stops at 4.

## Connections

- **Parent:** [[Quadratic Equations]] — the degree-2 case, where $\alpha+\beta=-b/a$ first appears; everything above is the same theorem with the restriction on degree removed.
- **Proof ingredient:** [[Polynomial Division]] and the factor theorem in [[Remainder and Factor Theorems]] — why a root forces a linear factor, which is what licenses writing $a(x-\alpha)(x-\beta)\cdots$ in the first place; [[Binomial Theorem]] — the expansion that does the work in every shift substitution.
- **Neighbour:** [[Substitution Equations]] — substitution used to *solve* an equation by reducing it to a familiar one; here the same tool is used to *transform the roots* of an equation nobody intends to solve.
- **Extends to:** [[Summation of Series]] — the next Further Pure 1 section, and the natural sequel: power sums are series, and the method-of-differences machinery there answers the same "sum something without evaluating its terms" instinct.
- **Where it is actually used:** [[Error Detection and Correction]] — the syllabus layer this sits on top of, from a single parity bit to the parity block that locates its own damage; and [[Stories/A Fight With the Inevitable Errors]] — the people who wanted it, and the fifty years between the question and the QR code.
- **Named instance:** [[Discriminant]] — $b^2-4ac$ met as a rule for counting roots, and revealed above as $a^2(\alpha-\beta)^2$: the smallest symmetric function that is not one of the elementary ones, and the reason its sign says what it says.
- **Where the idea leads:** [[Complex Numbers]] — a real quartic's non-real roots come in conjugate pairs, which is itself a statement about symmetry; [[Matrix]] — a matrix's characteristic equation has the same relations, so its trace is $\sum\lambda$ and its determinant is $\prod\lambda$, a fact Further Pure 2 leans on heavily.
- **For 9231 students:** [[MF19 Reference (9231)]] — and here the answer is blunt: nothing on this page is printed. Derive the relations from the expansion rather than trusting recall.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\alpha, \beta, \gamma, \delta$ | `\alpha, \beta, \gamma, \delta` | the conventional root labels, in order |
| $\sum\alpha$ | `\sum\alpha` | shorthand for the sum over all roots |
| $\sum\alpha\beta$ | `\sum\alpha\beta` | sum over all *distinct pairs* — three terms for a cubic, six for a quartic |
| $\sum\alpha^2$ | `\sum\alpha^2` | sum of squares; never $\left(\sum\alpha\right)^2$ |
| $\prod\alpha$ | `\prod\alpha` | the product of all roots |
| $(-1)^k$ | `(-1)^k` | the alternating sign in the general relation |
