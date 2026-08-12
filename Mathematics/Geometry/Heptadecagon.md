---
chinese: 正十七边形 (zhèng shíqī biānxíng)
prerequisites:
  - "[[Geometrical Constructions (Vocab)]]"
  - "[[Prime Factorisation (Vocab)]]"
  - "[[Surds]]"
  - "[[Complex Numbers]]"
  - "[[Euler's Formula and De Moivre's Theorem]]"
leads_to:
  - "[[Polygons]]"
  - "[[Stories/Gauss the Prodigy]]"
  - "[[Gauss the Prodigy]]"
tags:
  - subject/mathematics
  - domain/geometry
  - domain/number
  - level/Beyond-Syllabus
  - level/A-Level
  - type/deep
  - type/historical
  - type/proof
  - type/visualization
  - notation/F_n
  - notation/cos
  - misconception/all-regular-polygons-are-constructible
  - misconception/Gauss-actually-drew-it
---

# Heptadecagon 正十七边形

> [!info] Beyond syllabus — and worth every minute of it
> The regular 17-gon is the first surprise on the list of constructible polygons. The story is small enough to fit in one card and beautiful enough to change how a student feels about mathematics. Read this when the syllabus is closed for the day.

## Definition

A **heptadecagon** (or **17-gon**) is a polygon with 17 sides. The **regular heptadecagon** is the one where every side has the same length and every interior angle is equal — and it is, against all reasonable intuition, **constructible with ruler and compass alone**.

The name is Greek: *hepta-* (seven) + *deca-* (ten) + *-gon* (angle). Seven-and-ten-angled.

### 中文锚点

正十七边形 (zhèng shíqī biānxíng) 是边数为 17 的正多边形。"惊喜" 在哪里？数到 17 之前，我们已经会用尺规作出正三角形、正方形、正五边形、正六边形、正八边形、正十边形… 但 7、9、11、13 都不行。一直到 17，又是可以的——而且高斯（Gauss）在 1796 年才**首次证明**这件事。这个发现让 19 岁的高斯决定一辈子做数学家。

---

## The Punchline (in one paragraph)

Some regular $n$-gons are constructible (3, 4, 5, 6, 8, 10, 12, 15, 16, 17, …) and some are not (7, 9, 11, 13, 14, …). The exact rule was unknown for two thousand years. **Gauss settled it in 1796, age 19**: a regular $n$-gon is constructible if and only if $n$ is a power of 2 multiplied by distinct **Fermat primes**. The Fermat primes that anyone has ever found are $3,\;5,\;17,\;257,\;65537$ — only five of them — so 17 sits at the edge of what a human can reasonably draw, and Gauss showed it could be done.

The construction is real: an explicit ruler-and-compass procedure (the cleanest version is Richmond, 1893) builds every vertex exactly. The animation below shows it.

---

## Why 17? — Gauss–Wantzel

The classical Greeks could construct the 3-gon, 4-gon, 5-gon, 6-gon, 8-gon, 10-gon, 15-gon… and any polygon you can get from those by **doubling** (bisecting arcs gives 12-gon from 6-gon, 16-gon from 8-gon, 30-gon from 15-gon, etc.). Past those, they stopped, and "is the regular 7-gon constructible?" stayed open for two millennia. Most people *assumed* 17 was as hopeless as 7.

Gauss proved (1796 — sufficiency) and Wantzel proved (1837 — necessity):

> **Gauss–Wantzel Theorem.** A regular $n$-gon is constructible with ruler and compass if and only if
> $$n = 2^{k}\,p_{1}p_{2}\cdots p_{m}$$
> where $k \geq 0$ and the $p_i$ are **distinct Fermat primes**.

A **Fermat prime** is a prime of the form $F_{n} = 2^{2^{n}} + 1$. The known Fermat primes are
$$F_{0}=3,\quad F_{1}=5,\quad F_{2}=17,\quad F_{3}=257,\quad F_{4}=65537.$$

That's all anyone has found. Fermat conjectured every $F_n$ was prime; Euler punctured the conjecture in 1732 by factoring $F_5 = 4294967297 = 641 \times 6700417$. No further Fermat primes have been discovered, and we don't know whether finitely many or infinitely many exist.

The number 17 lands on this list as $F_2 = 2^{4} + 1$. That single fact — the "$+1$" matching a power-of-2 exponent — is what makes the 17-gon constructible while the 11-gon and 13-gon are not.

> [!info] Beyond syllabus — Galois theory in one sentence
> The deep reason a regular $n$-gon is constructible iff $n = 2^{k}\prod p_{i}$ (Fermat primes) is that ruler-and-compass operations only let you take **square roots**, so the [[Group Theory|Galois group]] of the splitting field of $x^{n} - 1$ over $\mathbb{Q}$ has to be a 2-group — and that happens exactly when $\varphi(n)$ is a power of 2, which forces the prime factorisation above. This is the topic of a first-year university Galois theory course; we mention it here so the magic word "constructible" lands in the right family later.

---

## The Algebraic Miracle

The heart of the proof: $\cos(2\pi/17)$ can be written using **only square roots** — no cube roots, no fourth roots, no transcendental moves. Gauss's actual formula, which he derived at 19, is

$$
\boxed{\;
16\cos\!\dfrac{2\pi}{17} \;=\; -1 + \sqrt{17} + \sqrt{34 - 2\sqrt{17}} + 2\sqrt{17 + 3\sqrt{17} - \sqrt{34 - 2\sqrt{17}} - 2\sqrt{34 + 2\sqrt{17}}}.
\;}
$$

Stare at it. There are square roots inside square roots inside square roots — but **only square roots**, all the way down. That's the entire reason ruler and compass can build the angle: every time you intersect a circle with a line (or another circle), you are solving a quadratic, which means taking a square root. Nesting is fine, the compass doesn't care. What the compass *cannot* do is solve a cubic, and that is exactly what would be needed for the 7-gon, 9-gon, 11-gon, and 13-gon. (See [[Surds]] for the algebra of nested radicals.)

The way Gauss derived this formula is itself a marvel. He looked at the 17 roots of $x^{17} - 1 = 0$ — the 17 vertices of the polygon, viewed as complex numbers — and split them into clever **Gaussian periods**: pairs, then pairs of pairs, then pairs of pairs of pairs. Each split is solvable by a single quadratic. Four nested quadratics later, you have a length expressed in nested square roots. (The four levels of nesting in the formula are the four splittings.)

---

## Richmond's Construction (1893)

Gauss's 1796 proof showed the 17-gon was constructible *in principle* but didn't give a clean drawing recipe. The cleanest practical construction is due to **Herbert William Richmond**, an English mathematician who published it in 1893.

The animation below walks through the full construction: the algebraic preamble, Richmond's specific points, the moment the first new vertex is found, and the final closing of the figure.

![[heptadecagon.mp4]]

> [!tip] Reading Richmond's construction
> Each landmark point ($B$, $C$, $D$, $K$, $N_3$, $N_5$) is the geometric realisation of one of the four nested quadratics in Gauss's formula. The points "encode" the nested square roots: $B$ comes from the outermost quadratic, $C$ from the next layer, and so on. By the time you reach $N_3$, all four square-roots have been taken — and dropping a perpendicular from $N_3$ to the unit circle lands on a real heptadecagon vertex.

The construction in words:

1. Draw the circle with centre $O$. Mark a point $V_{0}$ on it (this becomes the first vertex).
2. Draw the diameter through $V_{0}$ and the perpendicular diameter; call the top point $A$.
3. On $OA$, mark the point $B$ with $OB = \tfrac{1}{4}OA$.
4. Bisect the angle $\angle OBV_{0}$ twice to find $C$ on $OV_{0}$ with $\angle OBC = \tfrac{1}{4}\angle OBV_{0}$.
5. On $OV_{0}$ extended past $O$, mark $D$ with $\angle CBD = 45^{\circ}$ (rotated from $BC$ away from $V_{0}$).
6. Draw the circle on $DV_{0}$ as diameter — it meets $OA$ at $K$ (Thales' theorem guarantees a right angle at $K$).
7. Draw the circle centred at $C$ with radius $CK$. It cuts the diameter through $V_{0}$ at two points, $N_{3}$ and $N_{5}$.
8. Erect the perpendicular to the diameter at $N_{3}$; it meets the original circle at $V_{3}$ — the **fourth** vertex of the heptadecagon (counting $V_{0}$ as the first).

That's it for the construction proper. To get the rest of the polygon, you use the chord $V_{0}V_{3}$ as the compass setting and **step it around** the circle. Because $\gcd(3, 17) = 1$, repeating this step seventeen times visits every vertex exactly once before returning to $V_{0}$. (See [[Geometrical Constructions (Vocab)]] for the basic compass operations.)

> [!info] Why $V_{3}$ and not $V_{1}$?
> Richmond's construction lands on $V_{3}$ because the algebra tied to that vertex's $x$-coordinate — namely $\cos(6\pi/17)$ — comes out cleaner from the nested-quadratic decomposition than $\cos(2\pi/17)$ itself. Stepping by 3 from $V_{0}$ to recover all 17 vertices is the geometric way of "unwinding" that algebraic shortcut.

---

## The Other Constructible Fermat-Prime $n$-gons

The Gauss–Wantzel theorem says **every** Fermat prime gives a constructible $n$-gon. Beyond 17 there are exactly three more known cases:

- **Pentagon ($n=5$)** — the Greeks already had this; it's the inscribed-pentagon trick using the golden ratio.
- **Heptadecagon ($n=17$)** — Gauss, this card.
- **257-gon ($n=257$)** — Friedrich Julius Richelot constructed it explicitly in 1832. The construction takes hundreds of steps.
- **65537-gon ($n=65537$)** — **Johann Gustav Hermes** spent **roughly ten years** of his life producing the explicit construction by hand. The manuscript fills a 200-page chest, archived at the University of Göttingen. Whether anyone has ever read all of it is open to debate.

If a sixth Fermat prime exists, no human has found it (and computer searches have ruled out existence up to extremely large bounds). So the list of "honest" Fermat-prime $n$-gons might be complete at five.

> [!info] Beyond syllabus — 65537 in computer science (the second life of $F_4$)
> The same prime $F_4 = 65537$ that makes the 65537-gon constructible is, by no coincidence at all, **the standard public exponent in RSA encryption** — the value of `e` you'll find in nearly every TLS certificate, SSH keypair, and PGP key on the internet today. Why this number? RSA needs an `e` that is (a) prime and (b) has a *sparse binary representation*, because the public encryption operation $m \mapsto m^{e} \pmod{n}$ is fast only if $e$ has few 1-bits. Fermat primes nail both: $F_4 = 2^{16} + 1 = $ `0b10000000000000001` — only two bits are set, so the modular exponentiation reduces to 16 squarings and a single multiplication. The very same "$2^{2^k} + 1$" structure that powered Gauss's 1796 constructibility theorem also powers 1977's RSA. One number-theoretic property, two applications a century and a half apart. (Bridge to a planned CS folder: `[[RSA]]`, `[[Modular Exponentiation]]`.)
>
> A further bonus for computer scientists: $65537 = 2^{16} + 1$ is the smallest positive integer that *doesn't* fit in an unsigned 16-bit field — it sits exactly one above $65535$, the maximum 2-byte word. So whenever you see the magic number $65537$ in a hex dump or a port range, you're probably looking at a Fermat prime in disguise.

> [!info] Doubling and combining
> Once you have one constructible polygon, you can **double** it by bisecting each arc — so the 17-gon gives the 34-gon, 68-gon, 136-gon, … And you can **combine** two coprime constructible polygons (e.g., the 5-gon and the 17-gon) to get the 85-gon, because $\gcd(5,17)=1$. So the constructible $n$-gons are exactly $n = 2^{k} \cdot 3^{a} \cdot 5^{b} \cdot 17^{c} \cdot 257^{d} \cdot 65537^{e}$ with each Fermat-prime exponent at most 1. There are infinitely many.

---

## Common Misconceptions

1. **"Gauss drew the 17-gon by hand."** He didn't. He proved it was *constructible* — that there exists a finite ruler-and-compass procedure. He never published the procedure. Richmond's much later construction (1893) is what people actually draw. Gauss himself reportedly asked for a regular 17-gon on his tombstone, but the engraver refused, claiming the result would look like a circle to anyone walking past. The statue base of the Gauss monument in Brunswick is engraved with a 17-pointed star instead.
2. **"All regular polygons are constructible."** Famously not. The regular 7-gon, 9-gon, 11-gon, 13-gon, 14-gon, 18-gon, 19-gon, 21-gon, 22-gon, 23-gon, 25-gon, … are all *not* constructible with ruler and compass. (See [[Geometrical Constructions (Vocab)]] for what counts as a "construction".)
3. **"$2^{k}+1$ being prime is enough."** Almost — but $k$ itself must be a power of 2. Otherwise $2^{k}+1$ is automatically composite. (Quick proof: if $k = ab$ with $b$ odd and $b > 1$, then $2^{a} + 1$ divides $2^{ab} + 1 = (2^{a})^{b} + 1$, factoring it.) That's why Fermat primes have the form $F_{n} = 2^{2^{n}}+1$, with the inner exponent itself a power of 2.
4. **"Cube roots are just nested square roots."** They are not. A cube root cannot be expressed as any finite combination of rational numbers, square roots, and field operations — that is the deep result needed to prove the 7-gon is *not* constructible. Cube-rooting is genuinely a different operation, and the compass cannot perform it. (See [[Surds]].)

---

## Exam Notes

This topic is **beyond syllabus** for 0580, 0606, 9260, A-Level core, IB, and AP. It will not appear on a written exam.

It does, however, appear as enrichment material in:
- **A-Level Further Mathematics** — sometimes referenced when introducing the unit circle and complex roots of unity.
- **STEP / MAT** — occasionally as a starting point for a problem about constructible numbers.
- **Olympiad training** — the Gauss–Wantzel theorem is a standard result for IMO-prep students working on number theory.
- **University admissions interviews** — Cambridge and Oxford maths interviewers like to ask "which regular polygons are constructible, and why?" precisely because the answer has a beautiful algebraic core.

For day-to-day teaching, the heptadecagon is the **delight card**: the one you bring out when a student asks "what's the most surprising thing about geometry?" or "why did Gauss decide to be a mathematician?". The story has a complete arc — confused conjecture for 2000 years, sudden algebraic insight at age 19, exact ruler-and-compass procedure 100 years later — that lands well even with students who don't follow the Galois-theoretic punchline.

---

## Connections

- **Prerequisite:** [[Geometrical Constructions (Vocab)]] — the basic compass operations (perpendicular bisector, angle bisector, perpendicular at a point) on which Richmond's construction is built
- **Prerequisite:** [[Prime Factorisation (Vocab)]] — Fermat primes are a specific shape of prime; understanding prime factorisation is the door
- **Prerequisite:** [[Surds]] — the algebra of nested square roots; Gauss's formula for $\cos(2\pi/17)$ is a four-level nested radical
- **Sibling:** [[Polygons]] — the regular polygon family in general; this card is the famous outlier
- **Application:** Galois theory (university) — the Gauss–Wantzel theorem is the pin-up example of the Galois correspondence
- **Story:** [[Stories/Galois at Twenty]] — the boy who founded that theory, dead in a duel at twenty. Gauss's 1796 trick here — splitting the 17th roots of unity into nested pairs, each solvable by one quadratic — is the same idea (a tower of solvable steps) thirty years before Galois named it
- **History:** Gauss's diary, 30 March 1796 — the dated entry "Principia quibus innititur sectio circuli, ac divisibilitas eiusdem geometrica in septemdecim partes etc." marks the moment he settled on a mathematical career
- **Bridge to physics:** Crystallography rules out 5-fold and 7-fold symmetry in repeating patterns (the "crystallographic restriction"). The 17-gon doesn't tile the plane — but its constructibility is what made Gauss notice the deep link between *number-theoretic* (Fermat-prime) and *geometric* (constructible) constraints.
- **Bridge to computer science:** [[RSA]] uses $F_4 = 65537$ as its standard public exponent for the same reason Gauss could construct the 65537-gon — Fermat primes have a sparse binary representation, which makes modular exponentiation fast. See also [[Modular Exponentiation]].

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $F_{n}$ | `F_{n}` | The $n$-th Fermat number |
| $\cos\!\tfrac{2\pi}{17}$ | `\cos\!\tfrac{2\pi}{17}` | The cosine of the central angle |
| $\sqrt{34 - 2\sqrt{17}}$ | `\sqrt{34 - 2\sqrt{17}}` | Nested radical (one level) |
| $\varphi(n)$ | `\varphi(n)` | Euler's totient — equals $n-1$ for $n$ prime |
| $\gcd(3,17)$ | `\gcd(3,17)` | Greatest common divisor — equals 1 here |
| $\angle ABC$ | `\angle ABC` | Named angle at vertex $B$ |
