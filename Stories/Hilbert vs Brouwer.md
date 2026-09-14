---
chinese: "希尔伯特与布劳威尔 (Xī'ěrbótè yǔ Bùláowēi'ěr) — 排中律之战"
prerequisites:
  - "[[Cantor vs Kronecker]]"
  - "[[Russell's Paradox in the Post]]"
  - "[[Logic]]"
  - "[[Topology]]"
leads_to:
  - "[[Gödel's Incompleteness Theorems]]"
  - "[[Turing Machine]]"
tags:
  - type/story
  - subject/mathematics
  - subject/computer-science
  - domain/logic
  - domain/set-theory
  - domain/topology
  - era/19c
  - era/20c
  - cast/hilbert
  - cast/brouwer
  - cast/weyl
  - cast/einstein
  - cast/godel
  - cast/gordan
  - region/germany
  - region/netherlands
---

# Hilbert vs Brouwer 希尔伯特与布劳威尔

> *One of them said that a mathematical object exists the moment its definition is shown to be free of contradiction. The other said that nothing exists in mathematics until it has been built, and that half of logic — the half that says every statement is either true or false — was a superstition inherited from finite things. They were friends. Hilbert had put Brouwer on the board of the world's leading mathematics journal; in 1928, believing he was dying, he threw him off it. Einstein, asked to take sides, called it the war of the frogs and the mice and went back to his violin.*

## Cast of Characters

- **David Hilbert** (1862–1943) — Königsberg-born, Göttingen from 1895; the most influential mathematician of his generation. Axiomatised geometry, posed the twenty-three problems, and set out to prove that mathematics could never contradict itself: **formalism**.
- **L. E. J. Brouwer** (1881–1966) — Amsterdam; a mystic who wrote a pamphlet against the world at twenty-three, then became the greatest topologist alive, then renounced the methods he had used and rebuilt mathematics without the law of excluded middle: **intuitionism**.
- **Hermann Weyl** (1885–1955) — Hilbert's most brilliant student, who went over to Brouwer in 1921 with the words "this is the revolution", and came partly back.
- **Paul Gordan** (1837–1912) — Erlangen, "the king of invariants"; a whole career of explicit computation, and the man who called Hilbert's first great theorem theology.
- **Albert Einstein** (1879–1955) — an editor of *Mathematische Annalen* in name, who refused to be an editor of it in the one week it mattered.
- **Constantin Carathéodory** (1873–1950) and **Otto Blumenthal** (1876–1944) — the editors sent to reason with Brouwer, and the managing editor who had to write the letters.
- **Kurt Gödel** (1906–1978) — twenty-four in September 1930, in Königsberg the day before Hilbert's broadcast.

## 中文锚点

这是[[Cantor vs Kronecker|康托尔与克罗内克之争]]的下一代：**大卫·希尔伯特**（David Hilbert，1862–1943）站在康托尔一边，**鲁伊兹·布劳威尔**（L. E. J. Brouwer，1881–1966）站在克罗内克一边，争的还是同一个问题——**什么叫"存在"**。希尔伯特 1888 年的第一个大定理就是一个纯粹的存在性证明：他证明某样东西一定存在，却一个都没造出来，老前辈戈丹说"**这不是数学，这是神学**"。希尔伯特的回答是：一套公理只要**不自相矛盾**，它定义的东西就存在。布劳威尔说：不，数学是心智**一步步建造**出来的，一个东西要存在，你得把它**造出来**；而"任何命题非真即假"这条**排中律**，对有限的东西成立，搬到无穷集合上就是一句没有根据的话——他 1908 年就这么写了。这不是空谈：这张卡跑了一遍那个著名的例子——"存在无理数 $a, b$ 使 $a^b$ 是有理数"，经典证法分两种情况讨论，证完了却**说不出到底是哪一对**；构造证法直接交出 $\sqrt2^{\,\log_2 9} = 3$。布劳威尔自己当年就是在世的最出色的拓扑学家（1911 年证明了维数不变性和不动点定理），随后却放弃了自己用过的那些方法。1921 年希尔伯特最得意的学生外尔倒戈："**布劳威尔——这就是革命！**"希尔伯特回击说那不过是"拿着旧手段重演一次的未遂政变"，并提出**希尔伯特纲领**：把全部数学写成形式符号，再用布劳威尔也认可的**有限方法**证明它永远不会推出矛盾——"**谁也别想把我们赶出康托尔为我们造的乐园**"。争论在 1928 年变成了一桩丑闻：希尔伯特自以为将死，把布劳威尔逐出《数学年刊》编委会；爱因斯坦拒绝签字，称之为"**青蛙和老鼠的战争**"。结局出人意料：1930 年 9 月 8 日希尔伯特在广播里说"**我们必须知道，我们终将知道**"，而就在前一天，同一座城里，24 岁的哥德尔宣布了不完备性定理——希尔伯特纲领按原样**做不成**。可布劳威尔也没赢：数学家至今照用排中律。真正的和解发生在计算机里：一个构造性证明**就是一个程序**（柯里–霍华德对应），今天的 Coq、Lean 证明检查器，内核用的正是布劳威尔的逻辑。

## The Story

### Act I — "This is not mathematics, this is theology"

The story starts with a theorem that annoyed everyone. In 1888 David Hilbert, twenty-six and unknown, settled the central problem of nineteenth-century algebra — whether the "invariants" of any system of forms could all be generated from finitely many — and settled it for *every* case at once, in a few pages, by showing that an infinite basis would lead to a contradiction. He did not produce the basis. He did not say how to find it. He proved that it was there.

The reigning expert was **Paul Gordan** of Erlangen, who had spent twenty years computing such bases case by case, in papers that were pages of nothing but algebra, and had proved the binary case in 1868 with a method that ran to hundreds of pages. His verdict on the young man's proof was one sentence: *Das ist nicht Mathematik. Das ist Theologie.* This is not mathematics; this is theology.

![[hilbert-brouwer-theology-comic.png|720]]

*Erlangen, 1890. The box that exists but has never been opened. Gordan's remark reached the world through Hilbert's own circle, and Hilbert wore it as a badge: in 1893 he found a second, constructive proof, and Gordan is reported to have conceded that "theology also has its merits".*

Gordan's complaint was Kronecker's, one generation on: a proof that something exists without a way to build it has proved nothing a mathematician can use. Hilbert's answer to that complaint became his whole philosophy. In the 1899 *Grundlagen der Geometrie* he rebuilt Euclid as a **pure formal system** — twenty-odd axioms about undefined things called points, lines and planes, which he had once said in a Berlin railway station could just as well be called *tables, chairs and beer mugs* — and when the logician Frege objected that axioms had to be *true* of something before they could be used, Hilbert wrote back, on 29 December 1899, the sentence that made him the enemy of every constructivist alive:

> *If the arbitrarily given axioms do not contradict one another with all their consequences, then they are true, and the things defined by the axioms exist.*

Consistency **is** existence. Prove the rules cannot lead to $0 = 1$, and everything the rules talk about — infinite sets, uncountable cardinals, the point at infinity, $\sqrt{-1}$ — is as real as the integers. At the Paris congress of 1900 he made the consistency of arithmetic his **second problem**, and told the hall that in mathematics *there is no ignorabimus* — nothing we shall not know.

### Act II — The mystic from Amsterdam

**Luitzen Egbertus Jan Brouwer** was nineteen years younger, and had come to mathematics from somewhere stranger. In 1905, at twenty-three, he published *Life, Art and Mysticism*, a pamphlet that held the external world, language, science and other people to be distractions from the inner self; his thesis supervisor, Korteweg, made him cut the mystical chapters from his 1907 doctoral dissertation *On the Foundations of Mathematics*, and what remained was already the programme. Mathematics, Brouwer said, is not a language and not a set of rules. It is an **activity of the mind**, built up from a single primordial intuition — the awareness of time passing, of one moment becoming two — and every mathematical object is something a mind *constructs* from that. Logic comes afterwards, as a description of patterns in the constructions; it has no authority of its own.

The consequence, spelled out in a 1908 paper called *The Unreliability of the Logical Principles*, is the one that mattered. The **law of excluded middle** — every statement $A$ is either true or false, so $A$ *or not*-$A$ always holds — is a habit picked up from finite collections, where you can check every case. Applied to an infinite set it asserts something nobody has done: that a search which may never end has already returned an answer. Brouwer did not say the law was false. He said it was **not yet proved**, and that a proof which uses it has proved less than it claims.

![[hilbert-brouwer-what-is-a-proof.svg|760]]

*The two standards, side by side. Every line of the right-hand column is stricter than the left; the last line is where they part. Hilbert's images for the excluded middle — the telescope, the fists — are from his 1927 Hamburg lecture.*

The difference is not philosophical fog. Here is the standard example, run in `hilbert-brouwer-excluded-middle.py`. *Claim: there exist irrational numbers $a$, $b$ with $a^b$ rational.* The classical proof: consider $\sqrt2^{\sqrt2}$. Either it is rational — then $a = b = \sqrt2$ — or it is not — then take $a = \sqrt2^{\sqrt2}$, $b = \sqrt2$, and $a^b = \sqrt2^{\,2} = 2$. Done; and you have no idea which pair works. The constructive proof: $a = \sqrt2$, $b = \log_2 9$, and $a^b = 2^{\log_2 3} = 3$, with $b$ irrational because no power of $2$ is $9$. The script computes both; the first proof leaves it holding two candidates, the second hands it a $3$. (The undecided case was decided in 1934, by Gelfond and Schneider: $\sqrt2^{\sqrt2}$ is transcendental. It took a theorem, not a law of logic.)

Brouwer's own favourite example was cheekier. Nobody in 1908 knew whether the digits $0123456789$ ever appear, in that order, in the decimal expansion of $\pi$. Define a number $x$ whose $n$-th digit copies $\pi$'s until such a block appears, and is $0$ from then on. Is $x = 0$? Classically, yes or no. Constructively, nobody could say — so "$x = 0$ or $x \neq 0$" was, for the time being, not a theorem. `hilbert-brouwer-pi-digits.py` finds $0$, $01$, $012$, $0123$, $01234$ and $012345$ in the first half-million digits (the last at position 447 855) and gives up on the rest. The full block was found in 1997, at position 17 387 594 880. Brouwer's number is not zero. He had never said it was.

### Act III — The topologist who took it all back

What makes Brouwer impossible to dismiss as a crank is what he did next. Between 1909 and 1913 he became the best topologist in the world. He proved that **dimension is a topological invariant** — a line cannot be continuously and reversibly deformed into a square, which is exactly the fact that had made Cantor write *I see it, but I do not believe it* when he paired their points off; Cantor's pairing exists, and Brouwer showed that no *continuous* one can. He proved the **fixed-point theorem** in [[Topology]]: every continuous map of a disc into itself leaves some point where it was. He invented the mapping degree. Hilbert, who recognised talent when he saw it, campaigned for a Göttingen chair for him and put him on the editorial board of *Mathematische Annalen* in 1915.

And every one of those theorems was proved with the excluded middle, by showing that a map *without* a fixed point leads to a contradiction, with no way of finding the point. Brouwer knew it. From 1918 he rebuilt mathematics on his own terms — an **intuitionist set theory** with "choice sequences", numbers that are never finished — and in 1924 proved a theorem that is *false* in Hilbert's mathematics: **every function on $[0, 1]$ is uniformly continuous**. A step function, defined by "$0$ if $x < \tfrac12$, else $1$", is not a function at all for Brouwer, because deciding whether a never-finished real is less than $\tfrac12$ is an excluded-middle question. Intuitionism was not a cautious subset of classical mathematics. It was a different mathematics with different theorems, and in 1952, at seventy-one, Brouwer published a paper showing that his own fixed-point theorem does not hold in it.

### Act IV — "Brouwer — that is the revolution!"

For a decade the two men's disagreement was polite. What made it a war was a defection. **Hermann Weyl** — Hilbert's most gifted student, already the author of a book on Riemann surfaces and the standard text on general relativity — had written *Das Kontinuum* in 1918, a constructive analysis of his own; in 1921 he read Brouwer, abandoned his own version, and published *On the New Foundational Crisis of Mathematics* in the *Mathematische Zeitschrift*:

> *Brouwer — das ist die Revolution!*

The word was chosen. It was 1921; there had been revolutions in Munich and Berlin two years before, and Weyl's paper was written in their vocabulary — Brouwer as the one who would tear down the "paper economy" of formal mathematics. Hilbert, who had spent the war years and their aftermath keeping Göttingen the centre of the mathematical world, took it exactly as it was meant. His reply, a lecture in Hamburg in 1922, is the most political text he ever wrote:

> *What Weyl and Brouwer are doing amounts, in essence, to following the path once taken by Kronecker: they seek to ground mathematics by throwing overboard everything that troubles them … No: Brouwer is not, as Weyl believes, the revolution, but only the repetition, with old means, of an attempted Putsch — one that in its day was undertaken with greater verve and yet failed completely.*

And then the counter-programme. **Hilbert's programme**, worked out through the 1920s with Bernays and Ackermann, conceded Brouwer's ground in order to keep everything on it. Yes, he said: the only *absolutely* reliable reasoning is finite, concrete, about actual marks on paper — Brouwer's and Kronecker's standard. So write **all** of mathematics down as marks on paper, a formal system with explicit rules; then reason about that system, finitely, and prove that its rules can never derive a contradiction. The infinite would be retained as an "ideal element", like the points at infinity in projective geometry — a fiction the finite proof licenses. Brouwer's scruples would be honoured *once*, in the metatheory, and never again. In the 1925 Münster lecture *On the Infinite* he gave the programme its motto: *No one shall expel us from the paradise that Cantor has created for us.* In 1927, again in Hamburg, its rhetoric: to take the excluded middle from the mathematician would be like *denying the astronomer his telescope, or the boxer the use of his fists.*

Brouwer's answer to the programme was one sentence, from 1923, and it is the sharper: a consistency proof does not make a theory true, *"just as a criminal policy is none the less criminal even if it cannot be checked by any court that would curb it."*

### Act V — The war of the frogs and the mice

By 1928 the quarrel had left the journals. In January 1927 Brouwer lectured in Berlin, Hilbert's own country, to large audiences; in March 1928 in Vienna, where a young Wittgenstein sat in the hall and, by his own account, went back to philosophy because of it. Hilbert had meanwhile nearly died. Diagnosed in 1925 with pernicious anaemia, then a death sentence, he was kept alive by the raw-liver therapy discovered in Boston in 1926, obtained for him through Courant's American connections. He was sixty-six and did not expect many more years.

The fuse was the International Congress of 1928 in **Bologna** — the first since the war to which Germans were admitted, and admitted under the auspices of a Union that had excluded them since 1920. **Brouwer**, a Dutchman with a fierce sense of German grievance, campaigned with Bieberbach for a German boycott. Hilbert, ill, led a delegation of sixty-seven Germans into the hall to a standing ovation, and told the congress that all limits, especially national ones, are contrary to the nature of mathematics. Then, in October, he wrote to his fellow editors of *Mathematische Annalen* that Brouwer must be removed from the board — for his conduct over Bologna, and, he said plainly, because of *the incompatibility of our views on fundamental matters*; he feared that after his death the journal would fall to Brouwer.

He had no power to do it alone. The *Annalen* had a masthead of principal editors — Hilbert, Blumenthal, Carathéodory, **Einstein** — and a wider board on which Brouwer sat. Carathéodory went to Brouwer's house in Blaricum to persuade him to resign quietly; Brouwer refused, and answered Blumenthal's circular with a furious letter to every member of the board. Einstein was asked to sign. He would not. It was, he wrote in November, a *Frosch-Mäusekrieg* — the Battle of the Frogs and the Mice, the mock-Homeric epic in which two armies of small animals fight to the death over nothing — and he begged to be left out of it; in the same weeks, van Dalen reports, he told Hilbert that Brouwer struck him as an involuntary witness for Lombroso's theory on the kinship of genius and madness.

![[hilbert-brouwer-frogs-mice-comic.png|720]]

*November 1928, as Einstein saw it. The frog with the Panama hat and the moustache is Hilbert; the barefoot mouse with the finger raised is Brouwer; the journal is in the water. The man with his back to it all is not neutral out of cowardice — he simply thought the whole thing beneath the people fighting it.*

The way out was a lawyer's. The publisher, Ferdinand Springer, dissolved the entire editorial structure and refounded the journal with Hilbert, Blumenthal and Hecke as its only editors. Brouwer was not expelled; the board he sat on had simply ceased to exist. Einstein and Carathéodory declined seats on the new one. Brouwer withdrew from mathematics for years, and in 1934 founded his own journal, *Compositio Mathematica*, with an international board that pointedly excluded no one.

### Act VI — Königsberg, 7 and 8 September 1930

Hilbert retired in 1930, and his home city of Königsberg gave him honorary citizenship. He accepted it on 8 September with an address to the Society of German Scientists and Physicians, *Logic and the Knowledge of Nature*, whose final four words were broadcast on radio and are carved on his grave:

> *Wir müssen wissen. Wir werden wissen.* — We must know. We will know.

The day before, in the same city, a smaller conference had been held on the foundations of the exact sciences — Carnap spoke for logicism, Heyting for intuitionism, von Neumann for Hilbert's formalism — and in the closing discussion on 7 September a thin young Viennese logician named **Kurt Gödel** remarked, almost in passing, that one could give examples of true arithmetical statements that are not provable in the formal system of *Principia Mathematica*. Only von Neumann understood what he had heard; he cornered Gödel afterwards, and within weeks had drawn the second consequence himself. Hilbert was not in the room. The two men never met that week.

![[hilbert-brouwer-konigsberg-comic.png|720]]

*The old man at the microphone announcing there is nothing we shall not know; the young man at the café table, the day before, with the sentence that says otherwise. Hilbert's rays pass over Gödel's head. They did in life, too: the conferences were in different buildings.*

Gödel's 1931 paper, worked out in full in [[Gödel's Incompleteness Theorems]], has two halves. Any consistent formal system rich enough for arithmetic contains true statements it cannot prove. And — the half that killed the programme — such a system cannot prove *its own consistency*. Hilbert's plan had been to prove arithmetic consistent by finite means, and the finite means were themselves part of arithmetic; the proof he wanted would have been a proof arithmetic could not contain. His assistant Bernays had to explain it to him. He was, Reid records, angry at first, then quiet.

The programme was not quite dead. In 1936 Gerhard Gentzen proved arithmetic consistent after all — by a method that goes one careful step beyond the finite, induction up to the ordinal $\varepsilon_0$, which most intuitionists accept as a construction. The rescue, when it came, wore Brouwer's clothes. And in the same year Alan Turing answered the last of Hilbert's decision questions, the *Entscheidungsproblem*, with a [[Turing Machine]] and a diagonal: there is no mechanical procedure that decides every mathematical statement. Which is the excluded middle's missing witness. Brouwer had said in 1908 that "$A$ or not-$A$" claims a decision nobody has made; Turing showed in 1936 that for arithmetic as a whole, nobody can.

### Act VII — Who won

Nobody, in the way either man wanted. Working mathematicians use the excluded middle every day and prove existence by contradiction without a second thought; Hilbert's formalisation is how every proof assistant and every set-theory course is written, and Cantor's paradise has never been evacuated. Brouwer's mathematics stayed a minority pursuit, and he spent his last decades embittered, suspended from his chair in 1945 over accusations of wartime collaboration (he had advised students to sign the occupier's loyalty declaration so that they could keep studying), reinstated, isolated. He died on 2 December 1966, hit by a car while crossing the road outside his house in Blaricum.

But the war ended in a place neither man could have looked. Look at the right-hand column of the figure again. *A proof of "$A$ or $B$" is a proof of one of them that says which. A proof of "some $x$ has $P$" is a particular $x$, with its certificate. A proof of "$A$ implies $B$" is a method turning proofs of $A$ into proofs of $B$.* Every line describes a **program**: a value tagged with which case it is, a pair of a witness and a check, a function. That observation — Curry in 1934, Howard in 1969, now the **Curry–Howard correspondence** — says that a constructive proof *is* a program and a proposition *is* a type, and it is the foundation on which the proof assistants Coq, Agda and Lean are built. Their kernels run on Brouwer's logic, because a proof the machine can check is a proof the machine can run. The four-colour theorem, whose proof is too long for any human to read, was verified in Coq in 2005. The map has one colouring per proof, and the proof hands it over.

So the modern settlement is Hilbert's frame with Brouwer's contents: write everything formally, as Hilbert demanded; and wherever a proof must be *executed*, demand the construction, as Brouwer did. Kronecker's integers, Cantor's paradise, and a compiler in between.

## Honest edges

- **The quotations are real but not all in the men's own hand.** Gordan's "theology" reached print through Hilbert's circle (Blumenthal's 1935 memoir and Reid's biography), not through Gordan; Weyl's "revolution", Hilbert's "Putsch", the paradise and the telescope are in the published lectures. Einstein's "frog-mouse war" and the Lombroso remark are from his letters as reported in van Dalen's biography of Brouwer.
- **Hilbert was not defending sloppiness, and Brouwer was not a Luddite.** Hilbert *accepted* Brouwer's standard for the one proof that mattered — the consistency proof — and asked for nothing else to meet it; that is the whole design of the programme. Brouwer proved his theorems with the classical logic he attacked, knew it, and said so.
- **The Annalen affair had a politics the mathematics does not excuse.** Hilbert's letter names the philosophical incompatibility as a reason for removing an editor, which is not a reason. Brouwer's campaign for the German boycott of Bologna was itself nationalist, and Bieberbach, his ally in it, went on to found the Nazi "Deutsche Mathematik" in 1936 and to sort intuitionism and formalism into racial types — a use Brouwer neither sought nor repudiated loudly. Both men come out of 1928 smaller.
- **Königsberg was not a confrontation.** Hilbert and Gödel did not meet; Hilbert learned of the theorem later, from Bernays. The drama of "the day before" is real, but it was a coincidence of calendars, not a duel.
- **Gödel did not refute Hilbert's programme in every form.** He refuted the version in which finitary reasoning is formalisable within arithmetic; whether "finitary" can be stretched, as Gentzen stretched it, is a live question in proof theory to this day.
- **Intuitionism is not "mathematics without proof by contradiction".** Brouwer's logic keeps *not*-$A$ from "$A$ leads to absurdity"; what it refuses is the step from *not not*-$A$ to $A$. Refuting the non-existence of a fixed point is fine; concluding that a fixed point therefore exists is the move he will not make.

## Cultural ripples

- **Wittgenstein's return.** Brouwer's Vienna lecture of March 1928 is, by Feigl's account, the evening Wittgenstein decided to do philosophy again; the later Wittgenstein's insistence that mathematics is something people *do* is Brouwer's thesis in another accent.
- **"We must know, we will know"** became the motto of scientific optimism in the twentieth century — and its irony, that it was broadcast the day after Gödel spoke, is the standard opening of every popular book on incompleteness.
- **Proofs as programs.** The type systems of Haskell, Rust and every dependently-typed language are Brouwer's proof conditions written as data structures; an `Option` type is a constructive "or"; the verified compiler CompCert and the Lean mathematical library are the Grundlagenstreit's unexpected heirs.
- **Weyl's regret**, the closing line of the affair, from his last philosophical book: with Brouwer mathematics gains its highest intuitive clarity, and the mathematician watches with pain as the greater part of his towering theories dissolves into mist.

## Where this surfaces in the vault

- **[[Cantor vs Kronecker]]** — the first act of the same war: Kronecker's "only what can be constructed" is Brouwer's creed, and the paradise Hilbert refused to leave is Cantor's.
- **[[Russell's Paradox in the Post]]** — the paradox of 1902 is why Hilbert wanted a consistency proof at all; it is the crack the programme was built to seal.
- **[[Logic]]** — the law of excluded middle and proof by contradiction as the school uses them; this card is the story of the one mathematician who refused them, and why he was not simply wrong.
- **[[Topology]]** — Brouwer's fixed-point theorem and the invariance of dimension are stated there; here is the man, and the fact that he proved them by a method he later disowned.
- **[[Gödel's Incompleteness Theorems]]** — the theorem that ended Act VI, worked in full.
- **[[Turing Machine]]** — the *Entscheidungsproblem* was Hilbert's question; Turing's 1936 answer is the excluded middle's missing decision procedure, shown not to exist.
- **[[Four Colour Theorem]]** — the proof nobody can read, checked by a machine running Brouwer's logic.

## Receipts

- Dirk van Dalen, *L. E. J. Brouwer — Topologist, Intuitionist, Philosopher: How Mathematics Is Rooted in Life* (2013; the one-volume edition of *Mystic, Geometer, and Intuitionist*, 1999–2005) — the thesis and Korteweg's cuts, *Life, Art and Mysticism*, the 1908 paper, the Annalen affair with Hilbert's October 1928 letter, Carathéodory's visit, Einstein's letters, Springer's refounding, the 1945 suspension, the death in Blaricum.
- Constance Reid, *Hilbert* (1970) — Gordan's "theology", the beer mugs, the pernicious anaemia and the liver therapy, Bologna, Königsberg 1930, Bernays explaining Gödel.
- David Hilbert, letter to Frege of 29 December 1899, in Frege's *Philosophical and Mathematical Correspondence*; *Neubegründung der Mathematik*, Abh. Math. Sem. Hamburg 1 (1922) — the Putsch; *Über das Unendliche*, Math. Ann. 95 (1926) — the paradise; *Die Grundlagen der Mathematik*, Abh. Math. Sem. Hamburg 6 (1928) — the telescope and the fists; *Naturerkennen und Logik* (1930) — *Wir müssen wissen*.
- L. E. J. Brouwer, *Over de grondslagen der wiskunde* (1907); *De onbetrouwbaarheid der logische principes*, Tijdschrift voor Wijsbegeerte 2 (1908); *Begründung der Mengenlehre unabhängig vom logischen Satz vom ausgeschlossenen Dritten* (1918); *Über die Bedeutung des Satzes vom ausgeschlossenen Dritten* (1923) — the criminal policy; *Beweis, dass jede volle Funktion gleichmässig stetig ist* (1924); *An intuitionist correction of the fixed-point theorem on the sphere* (1952). English versions in van Heijenoort, *From Frege to Gödel* (1967) and Mancosu, *From Brouwer to Hilbert* (1998).
- Hermann Weyl, *Über die neue Grundlagenkrise der Mathematik*, Math. Z. 10 (1921) — the revolution; *Philosophy of Mathematics and Natural Science* (1949) — the mist.
- Kurt Gödel, *Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I*, Monatshefte 38 (1931). John Dawson, *Logical Dilemmas* (1997) — the Königsberg discussion of 7 September 1930 and von Neumann's reaction.
- Alan Turing, *On Computable Numbers, with an Application to the Entscheidungsproblem* (1936). W. A. Howard, *The formulae-as-types notion of construction* (1969, published 1980). Georges Gonthier, *A computer-checked proof of the Four Colour Theorem* (2005).
- Yasumasa Kanada's 1997 computation of $\pi$ — the position 17 387 594 880 of the block $0123456789$; the smaller blocks are found by `hilbert-brouwer-pi-digits.py`. Gelfond (1934) and Schneider (1934) — the transcendence of $\sqrt2^{\sqrt2}$, checked against `hilbert-brouwer-excluded-middle.py`.
