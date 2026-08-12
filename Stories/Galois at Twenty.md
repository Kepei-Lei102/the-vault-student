---
chinese: 二十岁的伽罗瓦 (èrshí suì de Jiāluówǎ) — 一夜写完，十一年无人能读
prerequisites:
  - "[[Cubic Graphs]]"
  - "[[Complex Numbers]]"
leads_to:
  - "[[Group Theory]]"
tags:
  - type/story
  - subject/mathematics
  - subject/computer-science
  - era/19c
  - era/20c
  - cast/galois
  - cast/abel
  - cast/ruffini
  - cast/cauchy
  - cast/fourier
  - cast/poisson
  - cast/liouville
  - cast/jordan
  - region/europe
---

# Galois at Twenty  二十岁的伽罗瓦

> *"Je n'ai pas le temps."* — "I have not the time." — scrawled in the margin of the manuscript he wrote the night before he died.
>
> *"Ne pleure pas, Alfred! J'ai besoin de tout mon courage pour mourir à vingt ans."* — "Don't cry, Alfred! I need all my courage to die at twenty."

There is a legend that Évariste Galois invented modern algebra in a single night, feverishly racing the dawn of the duel that would kill him. The legend is false. The truth is worse, and far more beautiful: **he had already done the work — three times over, across three years — and no one alive would read it.** The all-night letter was not a creation. It was a will.

He died at twenty. It took the world eleven years to open the envelope, and another thirty to understand it. When they finally did, they found that this boy — twice rejected from university, expelled, imprisoned, dead in a field over a woman — had answered a question mathematicians had been beating their heads against for three hundred years, and to answer it he had invented an idea so deep that it is now the language of symmetry itself: from the Rubik's cube in a child's hands to the gauge groups of the Standard Model.

![[galois-twenty-years.svg|760]]
*Twenty years, two threads. The mathematics (above the line) and the life (below) run in parallel and both end at the duel — 30 May 1832. Every manuscript he submitted was lost, rejected, or ignored while he lived. The vindication (green, 1846) arrives eleven years after the line stops.*

## Cast of Characters

- **Évariste Galois** (1811–1832) — French mathematician, republican revolutionary. Founder of group theory and Galois theory. Dead at twenty in a pistol duel, his life's work summarised in a letter written the night before.
- **Niels Henrik Abel** (1802–1829) — Norwegian mathematician who, in 1824, proved *that* the general quintic has no formula in radicals. Died of tuberculosis at twenty-six, in poverty, two days before the letter offering him a professorship arrived. Galois's near-twin in genius and in early death.
- **Paolo Ruffini** (1765–1822) — Italian mathematician and physician who published a proof of the quintic's unsolvability in **1799**, twenty-five years before Abel. It had a gap, and almost no one read it. The "Abel–Ruffini theorem" gives him half a name.
- **Augustin-Louis Cauchy** (1789–1857) — the towering French analyst who refereed Galois's first memoir. Long blamed for *losing* it; the record is kinder and stranger than that.
- **Joseph Fourier** (1768–1830) — secretary of the Académie des Sciences, of heat-equation fame. Took Galois's prize memoir home and **died**, and it was never found among his papers.
- **Siméon Denis Poisson** (1781–1840) — the third referee, who read Galois's masterwork and pronounced it *"incomprehensible."* He was not wrong that it was hard. He was wrong that this was Galois's fault.
- **Joseph Liouville** (1809–1882) — the mathematician who, in 1843, finally sat down with the dead boy's papers, understood them, and published them in 1846. The reason we know any of this.
- **Camille Jordan** (1838–1922) — whose 1870 *Traité des substitutions* built Galois's scattered testament into the systematic theory that conquered mathematics.

## 中文锚点

**核心论题**：伽罗瓦（1811–1832）在**二十岁**死于一场决斗。传说他在决斗前一夜"发明了整个近世代数"——这是**假的**。真相更残酷也更动人：他的工作早在三年间就写好了、投出去了**三次**，却没有一个活着的人愿意读它。那封通宵写就的信不是"创造"，而是一份**遗嘱**。

他要回答的问题有三百年历史：**五次方程有没有求根公式？**（二次有，三次、四次也有——见 [[Cubic Graphs]]。）阿贝尔在 1824 年证明了"一般五次方程**没有**根式解"。伽罗瓦更进一步，回答了**为什么**、以及**哪些**方程有解：他把每个方程配上一个"对称群"（他造的词 *groupe*），方程可用根式求解 **当且仅当** 这个群是"可解群"。五次方程的群 $S_5$ 里藏着一个"打不碎的对称原子" $A_5$——它非交换、且单——于是没有公式。

最深的一条线索，正是本库反复讲的**猎人式提问**：伽罗瓦不问"根是什么"，他问"**哪些置换让根之间所有的（有理）关系保持不变？**"——问的是**不变量**，不是未知数（见 [[Forward Reading and Problem Discovery]]）。这就是伽罗瓦群的定义，也是全部代数结构的种子。

十一年后 Liouville 才读懂并发表了它。今天，从魔方到粒子物理的规范群，对称群是描述"对称"的通用语言。

---

## Act I — The boy who read Legendre like a novel

Évariste Galois was born on 25 October 1811 in Bourg-la-Reine, a village just south of Paris. His father, Nicolas-Gabriel Galois, was a cultured republican who became the town's mayor; his mother, Adélaïde-Marie, was the educated daughter of a jurist, and she taught her son at home until he was twelve — Latin, Greek, and a diet of classical Stoic virtue that would, twenty years later, tell him exactly how to die.

There was no mathematics in this childhood. It arrived like a detonation. At the Lycée Louis-le-Grand — a grim Parisian boarding school with the discipline of a barracks — the fifteen-year-old Galois, bored and mediocre in his ordinary classes, picked up Legendre's *Éléments de Géométrie*. Legendre wrote it as a two-year course. Galois, the story goes, read it **like a novel**, cover to cover, and never needed to open it again.

Then he did the thing that defines him. He skipped the textbooks entirely and went straight to the **masters** — reading Lagrange's original memoirs on the algebraic solution of equations, and soon Abel, in the raw. He was fifteen, reading the frontier of research as bedtime material. His teachers were baffled and irritated. Reports called him *singular, bizarre, withdrawn, original.* One noted he was possessed by "the fury of mathematics." His other subjects collapsed, because he had decided they did not matter.

Here is the trait that made him and destroyed him, already fully formed at fifteen: **impatience with anything beneath the essential.** He would not walk the ladder rung by rung for the benefit of slower minds — not textbooks, not examiners, and, fatally, not readers. The same refusal that let a boy read Lagrange for pleasure would, within five years, make his greatest work "incomprehensible" to the finest mathematician in France.

## Act II — Two slammed doors

The dream was the **École Polytechnique** — the fountainhead of French mathematics, and a hotbed of republican politics. In 1828, a year early and unprepared, Galois sat the entrance exam. He **failed.**

Then, in the summer of 1829, the world caved in. On **2 July 1829**, his father — hounded by a village priest who had forged the mayor's signature onto malicious verses mocking his own relatives — killed himself in Paris. At the funeral a riot broke out. Évariste was seventeen, and had just watched the establishment, wearing the mask of a churchman, destroy an honest man with a lie.

Days later, still raw, he sat the Polytechnique exam a **second and final time.** He failed again. The legend — impossible to verify, too fitting to omit — is that when an examiner pressed him to spell out steps he found trivial, Galois threw the chalkboard eraser in his face. Whether or not the eraser is real, the barrier was: two attempts were all anyone was allowed, and the door to Polytechnique was now shut forever.

He fell back on the **École Normale**, the lesser school for training schoolteachers. He was in. He had also learned, at seventeen, the lesson that would organise the rest of his short life: *authority does not reward the truth; it protects itself.*

## Act III — The three manuscripts no one would read

Run alongside the political ruin a second, quieter catastrophe — the one that actually breaks your heart.

Galois's mathematics was, by 1829, already extraordinary. He had solved the problem of the ages: not just *that* higher equations resist a formula, but the exact machinery of *why*. He wrote it up. And then the manuscript went into the great sorting engine of the Académie des Sciences and vanished — three times.

**First (1829): Cauchy.** Galois submitted his early results to the Academy, and Augustin-Louis Cauchy was assigned to referee. For a century the story was that Cauchy carelessly *lost* the papers. The historian René Taton found the truth in 1971 and it is more poignant: Cauchy read them, thought well enough of them to **advise Galois to combine and expand his work** and submit it for the Academy's Grand Prix in mathematics — and then, distracted, failed to present them as scheduled. Not malice. Just a great man who was too busy, and a boy whose one shot slipped between the cracks.

**Second (1830): Fourier.** Galois followed the advice and submitted a full memoir for the Grand Prix. It went to the Academy's secretary, Joseph Fourier, who took it home to read — and **died**, in May 1830. The manuscript was never found among his papers. The prize was awarded jointly to Abel (already dead) and Jacobi. Galois was not even mentioned.

**Third (1831): Poisson.** He rewrote it once more — *"Mémoire sur les conditions de résolubilité des équations par radicaux,"* the founding document of group theory — and submitted it to Siméon Poisson. Poisson was honest and diligent. He read it, could not follow it, and reported that the argument was *"not sufficiently clear nor sufficiently developed for us to judge its rigour,"* suggesting the author expand it. The word that survives is **"incomprehensible."**

![[galois-at-twenty-three-rejections-comic.png|560]]

Sit with the cruelty of the pattern. It was not stupidity that buried him, and not, mostly, spite. It was that his ideas ran fifty years ahead of the vocabulary needed to receive them, and the one gift that might have bridged the gap — patient, generous exposition — was the exact gift this boy, constitutionally, did not have. He could see the group behind the equation instantly. He could not bring himself to slow down and *show* you.

## Act IV — The republican

While the manuscripts sank, Galois threw the whole of his ferocious intensity at revolution.

In July 1830 Paris rose and overthrew Charles X in three days. The Polytechnique students famously poured into the streets and onto the barricades. The École Normale students — Galois among them — were **locked inside** by the director, Guigniault, to keep them out of the fighting. Galois never forgave it. He fired off a letter denouncing the director in a newspaper, signed it, and was promptly **expelled** from the school in early 1831.

Now a full-time radical, he joined the Artillery of the National Guard — a republican-leaning unit the new king soon disbanded as a threat. At a banquet on **9 May 1831**, Galois rose to give a toast to the king holding an open knife; it was heard as a threat on Louis-Philippe's life. Arrested. **Acquitted** in June — his lawyer argued the rest of the toast ("*if he betrays*") had been drowned by the noise, and a sympathetic young jury let him go.

A month later, on **Bastille Day**, he was arrested again — leading a demonstration, armed to the teeth, wearing the banned uniform of the dissolved Guard. This time he was convicted, and sent to the prison of **Sainte-Pélagie.** He kept doing mathematics behind bars. He also, by one account, drunk and despairing, attempted his own life while the other prisoners talked him down. In March 1832, with cholera sweeping Paris, he was transferred to a private sanitarium for the final weeks.

## Act V — Stéphanie, and the letter

At the sanitarium he fell in love. Her name was **Stéphanie-Félicie Poterin du Motel**, connected to the resident physician. Fragments of her letters survive, copied out in Galois's own agonised hand; they are cool, and they are a refusal. Whatever happened — a genuine broken heart, a quarrel among republicans, a trap laid by political enemies; the historians still argue — it produced a **challenge to a duel.** Pistols, at dawn, 30 May 1832. His opponent was most likely a fellow republican, Pescheux d'Herbinville. Galois believed he would lose. *"I die,"* he wrote, *"the victim of an infamous coquette and her two dupes."*

On the night of **29 May**, he sat up and wrote. Letters to his republican friends. And a long mathematical testament to his friend **Auguste Chevalier**, laying out the theory of equations, the conditions for solvability, the seeds of group theory, and notes reaching toward elliptic functions and a "theory of ambiguity" he would never finish. In the margins, against the equations, in a hand running out of time, he wrote the three words that outlived him: **"Je n'ai pas le temps"** — *I have not the time.* He asked Chevalier to send the work to Gauss or Jacobi, "not to give their opinion on the truth, but on the **importance**, of these theorems."

> [!warning] The honest edge — the legend is a lie, and the truth is better
> The romantic myth — that Galois *invented group theory in that single desperate night* — was cemented by E. T. Bell's *Men of Mathematics* (1937) and repeated for generations. It is false, and it slanders him. As Tony Rothman showed in 1982, **the mathematics was already three years old.** He had written it, and submitted it, and had it lost by Cauchy, buried with Fourier, and rejected by Poisson. The letter of 29 May was a *summary and a plea* — a man frantically pointing at a body of finished work he was terrified would die with him. The real tragedy is not that he had one night. It is that he had *three years*, and no one would read the papers.
>
> And yet the night still earns its legend — for a different reason than the myth claims. It was the night the work was **rescued.** Without that frantic transmission to Chevalier, Galois's papers scatter with a dead radical's effects, and the wait is not eleven years but forever. He did not *create* that night. He made sure it would survive him. That is the true weight of it.

![[galois-at-twenty-legend-vs-record-comic.png|620]]

At dawn he was shot in the abdomen and left in the field; his seconds were gone and there was no doctor. A passing peasant found him. He was taken to the Cochin hospital, where his younger brother Alfred arrived weeping. *"Don't cry, Alfred,"* he said — the boy raised on Roman virtue, dying like a Roman — *"I need all my courage to die at twenty."* He refused a priest. He died of peritonitis on **31 May 1832**, aged twenty, and was buried in a common grave whose location is lost. Days later Paris erupted into the June Rebellion — the barricades of *Les Misérables* — and Galois's own funeral had nearly touched it off.

## Act VI — Eleven years of silence, then Liouville

The papers went to Chevalier and to brother Alfred, who copied them faithfully and sent them into the world. They reached Gauss. They reached Jacobi. **Neither answered.** The greatest mathematicians alive held the founding document of modern algebra in their hands and let it lie.

For eleven years, nothing.

Then, in 1843, **Joseph Liouville** — an established mathematician with the patience Galois never had — took up the manuscripts, worked through them, and grasped what he was holding. He announced to the Academy that the dead boy had solved the solvability problem completely. In **1846** he published Galois's memoirs in his *Journal de Mathématiques.* The envelope, at last, was open.

From there it detonated. Camille Jordan's 1870 *Traité des substitutions* turned the testament into a systematic theory and named the central object the *groupe de Galois.* By the end of the century, **group theory** — the mathematics of symmetry itself — was everywhere, and it has only grown: the classification of crystals, the conservation laws of physics (via Noether), the gauge symmetries of the Standard Model, error-correcting codes, the Rubik's cube. The word *groupe*, coined by a teenager to explain why the quintic has no formula, became one of the load-bearing words of all of science.

---

## The mathematics, made intuitive

What did he actually *do*? Here is the whole idea, without the machinery.

**The three-hundred-year problem.** To "solve by radicals" means to write the roots using $+,-,\times,\div$ and $n$-th roots. Quadratics fell to the Babylonians. Cubics and quartics fell in Renaissance Italy (see [[Cubic Graphs]] for that bloody drama). The **quintic** resisted for 250 years. In 1799 Ruffini, and completely in 1824 Abel, proved the general quintic has **no such formula**. But *that* it fails is not *why* it fails — and it leaves the sharper question untouched: *which particular equations are solvable, and which aren't?*

**Galois's leap: stop looking at the equation. Look at its symmetries.** Take a polynomial's roots. They secretly satisfy relations with rational coefficients — for $x^2 - 2$, the roots $\sqrt2$ and $-\sqrt2$ obey $r_1 + r_2 = 0$ and $r_1 r_2 = -2$. Now ask the **hunter's question** — *what doesn't change?* Which relabellings (permutations) of the roots leave **every** rational relation among them still true?

For $\sqrt2$: swapping $\sqrt2 \leftrightarrow -\sqrt2$ preserves everything a rational equation could say — which is *exactly why* ordinary algebra can never tell the two roots apart. That invisible symmetry, $\{\text{identity}, \text{swap}\}$, **is the Galois group** of the equation. It is not a property of the answer; it is a measure of how *tangled* the answer is. (This is the same reflex as [[Forward Reading and Problem Discovery]]: name the invariant, not the unknown. The Galois group is invariance made into an object.)

**Solvable by radicals = the group dismantles into abelian layers.** Adjoining one radical (one $n$-th root) peels off one clean, commutative layer of symmetry. So an equation has a radical formula **if and only if** its Galois group can be taken apart, layer by abelian layer, down to nothing — a *solvable group.*

| Degree | Generic Galois group | Order | Solvable? | Formula? |
|---|---|---|---|---|
| 2 | $S_2$ | 2 | yes | quadratic formula |
| 3 | $S_3$ | 6 | yes | Cardano (1545) |
| 4 | $S_4$ | 24 | yes | Ferrari (1545) |
| 5 | $S_5$ | 120 | **no** | **impossible** |
| $\ge 5$ | $S_n$ | $n!$ | **no** | **impossible** |

The wall is a single object. Hiding inside $S_5$ is the group $A_5$ (order 60) — the smallest **non-abelian simple** group, an *atom of symmetry* with no normal piece you can peel off. It cannot be dismantled into abelian layers, so no tower of radicals can ever reach the roots. **That is why the quintic has no formula** — not bad luck, but the indivisibility of $A_5$.

### The toy in your hands

![[fifteen-puzzle-parity.svg|697]]
*The 15-puzzle. Left: the solved board — reachable. Right: the same board with only the 14 and 15 swapped — **you can never reach it by sliding.** Sliding a tile is always an* even *permutation, so the positions you can reach are exactly half of all arrangements — the group $A_{15}$, never the full $S_{15}$. Sam Loyd offered \$1000 in the 1890s for a solution to the swapped board. It was safe: the group forbids it.*

That is the Galois idea in a plastic toy: **the group decides what is reachable.** The even/odd split ($A_n$ living inside $S_n$) that makes the 14–15 swap impossible is the *same* structural fact — the simplicity of the alternating group — that makes the quintic unsolvable. Hold the puzzle, and you are holding a shard of what a twenty-year-old saw in a field of equations.

### The cash-out he never saw

In an 1830 paper on number theory, Galois also built the **finite fields** now called **Galois fields**, $\mathrm{GF}(p^n)$ — arithmetic on a finite set that still behaves like the rationals. He had no possible use for them. Today they are everywhere the CS half of this vault lives: every QR code, CD, DVD, and deep-space transmission is protected by [[Error Detection and Correction|Reed–Solomon error-correction]] built on $\mathrm{GF}(2^8)$, and the AES cipher encrypting your traffic does its mixing in the same field. A construction with *no application in 1830* is the quiet arithmetic under the internet, and the same information-counting logic that runs through [[Information Theory]]. And the symmetry groups he opened now name the deepest structures in physics — the gauge groups of the Standard Model are Galois's idea grown to describe the forces of nature.

---

## Cultural ripples

**Symmetry became a *thing* you can compute with.** Before Galois, symmetry was an aesthetic — a property a shape *had* (see [[Symmetry (Vocab)]]). After him, a symmetry group is an **object** with its own arithmetic, and "what are the symmetries of this?" became one of the most powerful questions in science. Crystallography, quantum mechanics, particle physics, and the Rubik's cube (a group of order $4.3\times10^{19}$) are all downstream.

**Two boys, dead young, who redrew mathematics.** [[Stories/Abel the Other Boy Who Died Young|Abel]] (26, tuberculosis, penniless) and Galois (20, a duel) died within three years of each other, both unrecognised, both proved right after death — and both lost by the same referee, Cauchy. The quintic's impossibility carries both their names because the field could not decide which tragedy to honour. The two stories are meant to be read together.

**The fictionalised genius.** Galois is the patient zero of the "tortured romantic genius scribbling through the night" myth — the version E. T. Bell sold and Hollywood loves. The real story, recovered by careful historians, is a rebuke to the myth: genius is not enough. The work also has to be *received*, and reception is a human, political, fallible thing that failed a boy three times over. (The vault fights this fictionalisation everywhere — see [[Stories/Stigler's Law of Eponymy]].)

**"I have not the time."** The three margin words have become a mathematician's memento mori — printed on posters, quoted in eulogies, carried by every researcher who has ever felt a good idea outrunning the years left to write it down.

---

## Where this surfaces in the vault

- [[Cubic Graphs]] §"The Galois Bombshell" — the load-bearing mathematics: Abel 1824, why $S_5$ is unsolvable, the Renaissance cubic/quartic backstory. Read that for the math; come here for the life. (Dual residency: that card keeps the *what*, this one carries the *who* and *why it went unread*.)
- [[Stories/Abel the Other Boy Who Died Young]] — the twin tragedy. Abel proved the quintic *impossible* (1824) three years before Galois explained *why*; dead at twenty-six of tuberculosis, his masterpiece also mislaid by Cauchy, a rescue arriving two days too late. Two boys, one wall, both names on it.
- [[Group Theory]] — the field Galois founded: symmetry itself made into an object with its own arithmetic, from the Rubik's cube to the gauge groups of physics. Where the group idea grows up, and the pure-mathematics continuation of everything here.
- [[Complex Numbers]] — the roots Galois permutes live in $\mathbb{C}$; the Fundamental Theorem of Algebra guarantees there are $n$ of them to shuffle.
- [[Heptadecagon]] — Gauss in 1796 constructed the 17-gon by splitting the 17th roots of unity into nested pairs — *proto-Galois theory*, thirty years early. Constructibility with ruler and compass is one of the pin-up applications of the Galois correspondence.
- [[Forward Reading and Problem Discovery]] — Galois's founding move ("which symmetries leave every relation invariant?") is the hunter's "what doesn't change?" made into a whole theory. The deepest bridge of them all.
- [[Stories/The Argument for i]] — cites the same Rothman (1982) myth-correction that anchors the honest edge above; and the cubic formula whose casus irreducibilis births $i$ is the equation whose *symmetries* Galois studies.
- [[Stories/Stigler's Law of Eponymy]] — Ruffini (1799) proved the quintic unsolvable a quarter-century before Abel, and the theorem still leads with Abel's name.
- [[Information Theory]] — the CS half of the vault; Galois fields $\mathrm{GF}(2^n)$ are the arithmetic under [[Error Detection and Correction|Reed–Solomon codes]] and AES: the abstract twenty-year-old's toy running the modern internet.

---

## Receipts

**Primary and near-primary:**
- Galois's last letter to Auguste Chevalier, 29 May 1832, and the *"Mémoire sur les conditions de résolubilité des équations par radicaux"* — collected in *Écrits et mémoires mathématiques d'Évariste Galois*, ed. Robert Bourgne and Jean-Pierre Azra, Gauthier-Villars, 1962.
- Liouville's 1846 publication of Galois's memoirs, *Journal de Mathématiques Pures et Appliquées*, vol. XI.
- Camille Jordan, *Traité des substitutions et des équations algébriques*, Gauthier-Villars, 1870 — where "groupe de Galois" becomes systematic.

**Myth-correction and biography:**
- Tony Rothman, "Genius and Biographers: The Fictionalization of Évariste Galois," *American Mathematical Monthly* 89 (1982): 84–106. The essential debunking of the one-night legend.
- René Taton, "Les relations d'Évariste Galois avec les mathématiciens de son temps," *Revue d'histoire des sciences* 1 (1947); and his 1971 work reappraising Cauchy's actual (helpful) role.
- Laura Toti Rigatelli, *Evariste Galois, 1811–1832*, Birkhäuser, 1996.
- Mario Livio, *The Equation That Couldn't Be Solved*, Simon & Schuster, 2005 — group theory, symmetry, Abel and Galois for general readers.

**Mathematics:**
- John Stillwell, *Mathematics and Its History*, 3rd ed., Springer, 2010 — clean on radicals, $A_5$, and solvability.
- Ian Stewart, *Galois Theory*, 4th ed., CRC Press, 2015 — the standard undergraduate text.
- W. W. Johnson and W. E. Story, "Notes on the '15' Puzzle," *American Journal of Mathematics* 2 (1879): 397–404 — the parity proof that the 14–15 swap is unreachable.
