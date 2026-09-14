---
chinese: "康托尔与克罗内克 (Kāngtuō'ěr yǔ Kèluónèikè) — 无穷有大小"
prerequisites:
  - "[[Number Sets (Vocab)]]"
leads_to:
  - "[[Russell's Paradox in the Post]]"
  - "[[Countability]]"
  - "[[Hilbert vs Brouwer]]"
tags:
  - type/story
  - subject/mathematics
  - subject/computer-science
  - domain/set-theory
  - domain/logic
  - era/19c
  - era/20c
  - cast/cantor
  - cast/kronecker
  - cast/dedekind
  - cast/hilbert
  - cast/mittag-leffler
  - region/germany
---

# Cantor vs Kronecker 康托尔与克罗内克

> *One of them believed that God had made the whole numbers and that everything else was a human fiction. The other believed he had been shown, by God, that there are more points on a line than there are whole numbers, and more subsets of those points than points, and so on without end. They had been teacher and student. The fight lasted eighteen years, and the loser spent the next twenty-seven in and out of a sanatorium — and won.*

## Cast of Characters

- **Georg Cantor** (1845–1918) — born in St Petersburg, raised in Germany, a student of Kronecker and Weierstrass in Berlin; professor at Halle for his whole career. Inventor of set theory and of the arithmetic of infinite numbers.
- **Leopold Kronecker** (1823–1891) — rich enough to do mathematics without a salary; number theorist, Berlin's most powerful mathematician after Weierstrass, and a **finitist**: nothing exists in mathematics that cannot be built from the integers in finitely many steps.
- **Richard Dedekind** (1831–1916) — Brunswick; Cantor's correspondent and the one reader who checked his proofs. Inventor of the "cuts" that define the real numbers.
- **Karl Weierstrass** (1815–1897) — Berlin; Cantor's teacher, who protected him where he could and advised him to hide his big result under a modest title.
- **Gösta Mittag-Leffler** (1846–1927) — Stockholm; founded *Acta Mathematica* and published Cantor in French when Berlin would not; then asked him to withdraw a paper, and lost him.
- **David Hilbert** (1862–1943) — Göttingen; made the continuum problem the first of his twenty-three, and later refused to be expelled from "the paradise Cantor created".
- **Julius König** (1849–1913) — Budapest; announced in front of Cantor and his daughters, at Heidelberg in 1904, that Cantor's central hypothesis was false. He was wrong within a day.

## 中文锚点

**格奥尔格·康托尔**（Georg Cantor，1845–1918）是第一个证明**无穷有大小之分**的人；**利奥波德·克罗内克**（Leopold Kronecker，1823–1891）是他在柏林的老师，也是后半生一直坚持"这不是数学"的人。争的是**什么算一个数**。克罗内克说：**整数是上帝造的，其余都是人的作品**——一个数学对象只有能用有限步构造出来才算存在。康托尔说：把全体整数当作一个**完成了的整体**来看，和它的任何一个成员一样名正言顺；一旦允许这一点，就可以把无穷集合的元素**一一配对**来比大小。1873 年他证明分数可以和整数一一配对（这张卡把他的"之字形"走法正着算、反着算了一遍），接着证明实数**不能**：不管多聪明地把实数列成一张表，总有实数不在表上——**一条线上的点比整数多**。1877 年他证明一个正方形里的点和它一条边上的点一样多，写信给戴德金说："**我看见了，但我不相信。**"1891 年他给出**对角线论证**：三行字，把表上第 $k$ 个数的第 $k$ 位改掉，就得到一个不在任何一张表上的数（这张卡真的跑了一遍）；还有那个定理：**没有一个集合能和自己的全体子集配对**——所以**没有最大的无穷**。克罗内克压他的论文、堵他去柏林的路、叫他"**败坏青年的人**"；康托尔一辈子困在哈勒这所小大学，为了摆脱柏林那帮人的掣肘，他参与创办了德国数学家联合会，从 1884 年起反复进出哈勒的疗养院——今天会诊断为**双相障碍**，这场争斗加重了病，但不是病因。他最后一个解不开的问题是**连续统假设**：整数和直线之间，还有没有一种中间大小的无穷？他既证不了也推翻不了；1940 年哥德尔和 1963 年科恩证明，标准的集合论公理**两边都定不了**。这张卡也还克罗内克一个公道：他对"构造"的坚持后来成了布劳威尔的直觉主义，又在图灵手里成了**可计算性理论**——而图灵证明"大多数实数算不出来"，用的正是康托尔的对角线，对准的正是克罗内克的整数。

## The Story

### Act I — Berlin, and the teacher

Cantor was born in St Petersburg in 1845 to a Danish-born merchant and a Russian mother from a family of musicians; the family moved to Germany when he was eleven, and his father — devout, ambitious, and ill — steered him from the violin toward engineering and from engineering, in the end, toward mathematics, with letters urging him to become "a shining star on the horizon of science". The father died in 1863. That autumn Cantor entered Berlin, where three men ran mathematics: Kummer, Weierstrass, and **Leopold Kronecker** — small, brilliant, independently wealthy, and certain that the only honest mathematics was the arithmetic of whole numbers and whatever could be built from them by explicit finite rules. Cantor's doctorate, in 1867, was a piece of number theory in exactly that spirit. Kronecker had no reason to think he had trained his own opponent.

Berlin did not keep him. In 1869 he took the only post on offer, at **Halle**, a provincial university two hours south, and stayed there for forty-nine years, applying for Berlin, and Göttingen, and being refused. In 1872, on holiday in Switzerland, he met **Richard Dedekind**, and began the correspondence in which everything below was first written down.

### Act II — 1873: a question in a letter

On 29 November 1873 Cantor wrote to Dedekind with a question he said was of no practical importance: can the whole numbers $1, 2, 3, \dots$ be paired off, one to one, with the real numbers? He already knew the surprising half. The **fractions** can be: lay them out in a grid, $p$ across and $q$ down, walk the diagonals, skip the repeats, and every fraction receives a number.

![[cantor-zigzag.svg|640]]

*Cantor's walk. The script `cantor-zigzag.py` turns it into a function you can call both ways: $3/7$ sits at position 28, and $355/113$ at position 66 676. The fractions, which seem to crowd every interval, are no more numerous than the whole numbers. The word for this is **countable**.*

Eight days later, on 7 December, he wrote again: the reals cannot. His first proof was not the famous one. Take any list of real numbers $x_1, x_2, x_3, \dots$ and any interval; pick inside it the first two listed numbers, take the interval between them, pick the next two inside *that*, and so on; the nested intervals close on a point that is inside every one of them and so was never listed. *Any* list of reals misses a real; the line is **uncountable**. Between the whole numbers and the line there is a gap of a kind nobody had named.

He published it in 1874 in Crelle's journal, under a title chosen with Weierstrass's advice to attract no attention: *On a Property of the Collection of All Real Algebraic Numbers*. The property was that they were countable; the uncountability of the reals was slipped in as a corollary, and its most startling consequence — that since the algebraic numbers are a mere list, *almost every* real number is transcendental — was stated in one sentence. Kronecker had the ear of the journal's editor, and Cantor had learned to be careful.

### Act III — "I see it, but I do not believe it"

The next question was dimension. A line has one, a square two; surely the square has "more" points. In 1877 Cantor found a pairing between the points of a unit square and the points of a unit segment — interleave the decimal digits of the two coordinates into one number, and un-interleave to go back — and on 29 June 1877 wrote to Dedekind, in French, the sentence every mathematician knows: *"Je le vois, mais je ne le crois pas."* I see it, but I do not believe it.

![[cantor-i-see-it-comic.png|720]]

*Halle, June 1877. The pairing that should not exist, drawn on the page; the letter half-written. Dedekind found a flaw in the first version — decimals like $0.4999\ldots$ and $0.5000\ldots$ are the same number — and Cantor patched it. The theorem survived: dimension is not about how many points there are.*

The paper went to Crelle's in July 1877 and did not appear until 1878. **Kronecker held it up.** Dedekind talked Cantor out of withdrawing it; when it finally appeared Cantor never sent Crelle's another paper, and the fight had a date.

### Act IV — God made the integers

Kronecker's objection was not personal to begin with. He believed that a mathematical object exists only if it can be constructed from the whole numbers in finitely many steps, and that a proof which shows something exists without showing how to build it — Cantor's nested intervals, which locate an unlisted point only "in the limit" — proves nothing. Irrational numbers themselves he regarded as a convenient fiction; he once told Lindemann that his proof that $\pi$ is transcendental was beautiful but pointless, since irrational numbers do not exist. The summary he gave a Berlin audience in 1886 is the most quoted sentence in the philosophy of mathematics:

> *Die ganzen Zahlen hat der liebe Gott gemacht, alles andere ist Menschenwerk.* — God made the whole numbers; all the rest is the work of man.

![[cantor-kronecker-integers-comic.png|720]]

*Berlin, 1886. The integers with a halo; everything Cantor had built, crossed out. The sentence was reported by Heinrich Weber in his obituary of Kronecker in 1893, and has been quoted in every direction since.*

Against that creed Cantor's 1883 *Grundlagen* was a provocation: infinite **ordinal numbers** $\omega, \omega + 1, \omega + 2, \dots, \omega \cdot 2, \dots, \omega^\omega, \dots$, defined as finished objects and manipulated like integers, with a philosophical introduction defending "the actual infinite" against Aristotle, Gauss and — unnamed — Kronecker. Kronecker's reply was conducted in corridors. He blocked Cantor's hope of a Berlin chair; he is reported, by Cantor and by Schoenflies after him, to have called Cantor a "scientific charlatan", a "renegade", and a *Verderber der Jugend* — a corrupter of youth — the charge against Socrates. Cantor's response was to go around Berlin: **Mittag-Leffler** in Stockholm printed the *Grundlagen* in French in *Acta Mathematica* in 1883, and in 1890 Cantor was the driving founder and first president of the **Deutsche Mathematiker-Vereinigung**, a national society built in part so that German mathematics would have a centre that was not Kronecker's seminar.

Then Mittag-Leffler faltered. In 1885 he asked Cantor to withdraw a paper on order types from *Acta* — the ideas, he wrote, were "about a hundred years too soon" — and Cantor, who had lost Berlin and now felt he had lost Stockholm, never forgave him. In May 1884 he had already been in the Halle **Nervenklinik** for the first time.

![[cantor-timeline.svg|960]]

*Two tracks. The blue stems are the theorems; the amber ones the feud; the red bands the hospital, from `cantor-timeline.py`. The first breakdown, in 1884, came while he was trying and failing to prove the continuum hypothesis, and three months after a courteous exchange of letters with Kronecker that both men called a reconciliation. The bands lengthen after 1899, when his youngest son died at thirteen — and after Kronecker had been dead for eight years.*

### Act V — The diagonal

Kronecker died on 29 December 1891. Cantor's answer to him was already in press — in the first volume of the new society's own journal — and it is the three lines the rest of mathematics and computing has run on ever since.

Take any list of real numbers between 0 and 1, written as decimals. Build a new number whose **first** digit differs from the first digit of the **first** number, whose **second** digit differs from the second digit of the **second** number, and so on down the **diagonal**. The new number differs from every number on the list, each at its own digit, so it is not on the list. The list was arbitrary; therefore no list contains all the reals.

![[cantor-diagonal.svg|860]]

*The script `cantor-diagonal.py` takes any rule you like for the list — here the $k$-th entry is $(k+1)/(k+7)$ — reads the diagonal, changes every digit, and checks the result against every entry. It never looks at what the rule is. That is why the argument cannot be dodged by a cleverer list.*

The same paper contains the deeper theorem, and its proof is the diagonal in disguise. For **any** set $S$, the collection of all its subsets, $\mathcal P(S)$, is strictly bigger: no function $f$ from $S$ to $\mathcal P(S)$ can reach every subset, because the subset $D = \{x : x \notin f(x)\}$ is never hit — if $D = f(a)$ then $a \in D$ exactly when $a \notin D$. The script tries every one of the 65 536 functions from a four-element set to its sixteen subsets; none is onto, and the missing subset is always $D$. Apply the theorem to an infinite set and you get a bigger infinity; apply it again and again and the ladder of infinities — the **alephs** $\aleph_0, \aleph_1, \aleph_2, \dots$ of his 1895 *Beiträge* — never ends. Kronecker had said there was one kind of number. Cantor had shown there was no top to the tower.

### Act VI — The question that had no answer

One rung of the tower would not hold still. $\aleph_0$ is the size of the whole numbers; $2^{\aleph_0}$, the size of the line. Is the line the *very next* size, $\aleph_1$, or is there something in between? Cantor was sure there was not — the **continuum hypothesis** — and in 1884 he announced a proof, then a disproof, then withdrew both, then broke down. Hilbert made it the first of his twenty-three problems in Paris in 1900. In August 1904, at the International Congress in Heidelberg, **Julius König** read a paper proving the hypothesis *false* in a stronger form — the continuum could not even be well-ordered — to a hall that contained Cantor and his two daughters. Cantor, who had come to the congress against his doctors' advice, sat through it; within a day Zermelo had found the error, a lemma of Bernstein's used outside its range, but Cantor took it as a public humiliation before his children and believed for the rest of his life that God had let it happen to test him.

![[cantor-heidelberg-comic.png|720]]

*Heidelberg, August 1904. König at the lectern; Cantor, fifty-nine, between his daughters in the front row. The refutation lasted twenty-four hours. The humiliation, in his own account, lasted the rest of his life.*

He was in the clinic in 1899, 1902, 1904, 1907, 1911 and from May 1917. Between stays he lectured on the theory that Bacon had written Shakespeare, published pamphlets on it, and corresponded with Catholic theologians about whether the transfinite numbers infringed on the infinity of God (he held that they did not, and that the **Absolute** — the collection of all sets, which his own theorem showed could not be a set — was God's alone). He died in the Halle sanatorium on 6 January 1918, underfed in the last winter of the war. The continuum hypothesis outlived him by forty-five years and then did something no one expected: **Gödel** proved in 1940 that it cannot be disproved from the standard axioms of set theory, and **Paul Cohen** in 1963 that it cannot be proved from them either. The question Cantor could not answer has no answer at that level. He had been asking the axioms for something they did not contain.

Hilbert's verdict, in a 1926 lecture, is the one that stuck: *"No one shall expel us from the paradise that Cantor has created for us."* And the small print of that paradise is Kronecker's. **Brouwer** took up Kronecker's demand that existence mean construction and built intuitionism on it; **Turing** in 1936 defined the numbers a machine can actually compute — the reals Kronecker would have accepted — and then showed, by Cantor's diagonal argument applied to the list of all programs, that almost every real number is not among them. The two men's positions turned out to be the two halves of one subject.

## Honest edges

- **The madness was not Kronecker's doing.** E. T. Bell's 1937 *Men of Mathematics* made "Kronecker drove Cantor mad" the standard story. The medical records Grattan-Guinness examined in 1971 show a recurring manic-depressive illness whose episodes track his own cycles, not the feud's: the first came three months *after* the 1884 reconciliation, the worst ones after Kronecker was dead and Cantor was the most honoured mathematician in Germany. The feud was real; it was not the cause.
- **Cantor gave as good as he got.** The *Grundlagen*'s introduction attacked Kronecker's philosophy in print before Kronecker had attacked Cantor's; his letters call Kronecker a tyrant and Mittag-Leffler a traitor; he broke with Dedekind in 1882 when Dedekind declined a post at Halle. The 1884 reconciliation, with cordial letters on both sides, is left out of most tellings because it spoils them.
- **Kronecker was not a crank.** Finitism is a coherent position that a large part of twentieth-century logic and all of computer science live inside; Kronecker's "only what can be constructed" is the working definition of a computable number. This card gives him the comic and the last word for a reason.
- **The "corrupter of youth" line is hearsay.** It reaches us through Cantor's letters and through Schoenflies in 1927; no text of Kronecker's contains it. The 1886 sentence about the integers is second-hand too, from Weber's obituary.
- **The theology and the Shakespeare are not comic relief.** For Cantor the transfinite was a revelation and the Absolute was God; the Bacon pamphlets were pursued with the same seriousness and the same certainty. The card keeps them beside the mathematics because he did.

## Cultural ripples

- **Hilbert's Hotel** (1924) — the infinite hotel that is full and still has room — is the countability of the integers turned into a parable, and every popular account of infinity since has used it.
- The **diagonal argument** is the most reused proof in mathematics: Russell's paradox (1901), Gödel's undecidable sentence (1931), Turing's halting problem (1936), and the incompressible strings of information theory are the same three lines aimed at sets, proofs, programs and files.
- **Aleph** as a symbol of the infinite — Borges's story *El Aleph* (1945) takes its title from Cantor's notation, and says so.
- The **continuum hypothesis** became the founding example of a mathematical question that is neither true nor false but *independent*, and Cohen's method, forcing, is now a discipline of its own.

## Where this surfaces in the vault

- **[[Number Sets (Vocab)]]** — the countability of the algebraic numbers and the uncountability of the reals, stated there, proved here; [[Countability]] carries the full arguments.
- **[[Russell's Paradox in the Post]]** — the diagonal pointed at the set of all sets; Cantor's own "inconsistent multiplicities" of 1899 are the same discovery a year before Russell.
- **[[Gödel's Incompleteness Theorems]]** and **[[Turing Machine]]** — the diagonal pointed at proofs and at programs; Turing's computable numbers are Kronecker's numbers, and the uncomputable ones are found by Cantor's method.
- **[[Hilbert vs Brouwer]]** — the same argument a generation later, with Kronecker's position in Brouwer's hands and Cantor's in Hilbert's.
- **[[Galois at Twenty]]** and **[[Abel the Other Boy Who Died Young]]** — the folder's other mathematicians the establishment refused; Cantor is the one who lived long enough to be vindicated and could not enjoy it.

## Receipts

- Joseph Dauben, *Georg Cantor: His Mathematics and Philosophy of the Infinite* (1979) — the letters to Dedekind of 29 November and 7 December 1873 and 29 June 1877, the 1874 title and Weierstrass's advice, the 1878 delay, the Mittag-Leffler withdrawal request, the DMV, Heidelberg 1904, the theology and the Bacon pamphlets.
- Ivor Grattan-Guinness, *Towards a Biography of Georg Cantor*, Annals of Science 27 (1971) — the Halle clinic records and the diagnosis; the case against the Bell legend.
- Georg Cantor, *Über eine Eigenschaft des Inbegriffes aller reellen algebraischen Zahlen*, J. reine angew. Math. 77 (1874); *Ein Beitrag zur Mannigfaltigkeitslehre*, ibid. 84 (1878); *Grundlagen einer allgemeinen Mannigfaltigkeitslehre* (1883); *Über eine elementare Frage der Mannigfaltigkeitslehre*, Jahresbericht der DMV 1 (1891) — the diagonal argument and the power-set theorem, run in `cantor-diagonal.py`; *Beiträge zur Begründung der transfiniten Mengenlehre* (1895, 1897).
- Heinrich Weber, *Leopold Kronecker*, Jahresbericht der DMV 2 (1893) — the "God made the integers" sentence. Arthur Schoenflies, *Die Krisis in Cantor's mathematischem Schaffen*, Acta Mathematica 50 (1927) — the reported insults.
- David Hilbert, *Über das Unendliche*, Mathematische Annalen 95 (1926) — the paradise. Kurt Gödel, *The Consistency of the Continuum Hypothesis* (1940). Paul Cohen, *The Independence of the Continuum Hypothesis*, PNAS 50–51 (1963–64).
- Alan Turing, *On Computable Numbers* (1936) — the diagonal on the list of machines; the bridge between the two men's positions.
