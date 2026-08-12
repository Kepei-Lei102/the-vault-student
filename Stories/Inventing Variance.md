---
chinese: 方差的发明 (fāngchā de fāmíng)
prerequisites:
  - "[[Why Probability and Statistics]]"
  - "[[Normal Distribution]]"
  - "[[Linear Combinations of Random Variables]]"
  - "[[Stories/Gauss the Prodigy]]"
leads_to:
  - "[[Sampling and Estimation]]"
  - "[[Hypothesis Tests]]"
tags:
  - type/story
  - subject/mathematics
  - era/19c
  - era/20c
  - cast/piazzi
  - cast/gauss
  - cast/legendre
  - cast/laplace
  - cast/galton
  - cast/pearson
  - cast/gosset
  - cast/fisher
  - region/europe
---

# Inventing Variance 方差的发明

> *"Without the ingenious labours and calculations of Doctor Gauss, we might perhaps never have found Ceres again." — Baron von Zach, December 1801. The number that measures doubt took a hundred and seventeen more years to get its name.*

## Cast of Characters

- **Giuseppe Piazzi** (1746–1826) — monk-astronomer of Palermo; found a planet, then lost it.
- **Carl Friedrich Gauss** (1777–1855) — twenty-four, unemployed, unbearable, right.
- **Adrien-Marie Legendre** (1752–1833) — named least squares, published it first, and was wounded for life.
- **Pierre-Simon Laplace** (1749–1827) — supplied the deep reason the whole thing worked.
- **Francis Galton** (1822–1911) — Darwin's cousin; moved the mathematics from stars to people, for a dark purpose he named himself.
- **Karl Pearson** (1857–1936) — Galton's disciple; christened the *standard deviation*; ran statistics like a fiefdom.
- **William Sealy Gosset** (1876–1937) — a brewer, publishing under a false name.
- **Ronald Aylmer Fisher** (1890–1962) — finally said the word *variance*, in a paper about peas and ancestry; feuded with Pearson until one of them died.

## 中文锚点

方差（variance）是"测量不确定性"的货币，但它的诞生用了一百多年。故事从 1801 年说起：皮亚齐在巴勒莫发现了谷神星（第一颗小行星），追踪四十一夜后病倒，星体没入太阳光辉——天文学界"丢了一颗行星"。二十四岁的高斯用手算三个月，从仅约三度的弧段推算轨道，指出它将在哪里重现；十二月，望远镜转向他指的位置，谷神星就在那里。为拟合轨道而生的**最小二乘法**（勒让德 1805 年命名并首发，高斯 1809 年声称"自 1795 年起使用"——优先权之争由此而起）把"平方误差"变成了科学的日常。这个无名的量在天文学里默默工作了一个世纪，直到高尔顿把测量从星星转向人类（他为优生学而建立这套工具——历史的阴影必须直说），皮尔逊 1893 年命名了**标准差**，费希尔 1918 年在一篇调和孟德尔与达尔文的论文里第一次写下 **variance** 这个词。你考卷上的 $\sigma^2$，就是这段历史的化石。

## The Story

### Act I — The Celestial Police, and the gatecrasher

Between Mars and Jupiter there is a gap where a planet ought to be. By 1800 the numerology of the day (the Titius–Bode pattern) had promoted that "ought" into an obsession, and in September of that year a group of astronomers meeting at Lilienthal organised themselves into a society for hunting the missing world. They divided the zodiac into twenty-four beats, one per member, and history remembers them by the name they gave themselves: the **Celestial Police**.

They were scooped by a man they hadn't finished inviting. In Palermo, on the first evening of the new century — **1 January 1801** — Giuseppe Piazzi, a Theatine monk compiling a star catalogue, noticed that one of his "stars" had moved. He followed it, cautious and half-disbelieving, announcing it first as a comet ("I have presented this star as a comet," he admitted privately, "but... it might be something better"). For **forty-one nights** he tracked it across a mere **three degrees** of sky. Then Piazzi fell seriously ill; by the time letters had crawled across a Europe at war and other astronomers knew where to look, the object — christened **Ceres**, for the patron goddess of Sicily — had drifted into the glare of the Sun.

Astronomy now held a unique embarrassment: it had discovered a planet and *lost* it. When Ceres emerged from the Sun's glare months later, nobody could find it — an orbit fitted from three degrees of arc was hopelessly underdetermined, and the small errors in Piazzi's hand-measured positions could swing the predictions across whole constellations. The problem, note, was not too little data but *disagreeing* data: every observation carried its own small error, and the science of what to do about that barely existed. (Within living memory, respectable astronomers had solved the problem of disagreeing measurements by picking the one they trusted and discarding the rest — there had been serious argument over whether averaging *compounded* errors rather than cancelling them.)

### Act II — The twenty-four-year-old and the three degrees

In Brunswick sat a twenty-four-year-old with no academic post, living on a duke's stipend: Carl Friedrich Gauss — the same young man who, five years earlier, had settled his choice between languages and mathematics on the morning he constructed the [[Heptadecagon|seventeen-gon]]. Orbit recovery was exactly the kind of problem he liked: publicly declared near-impossible, and reducible to calculation.

Through October and November of 1801 he calculated — by hand, inventing method as he went, including what became his machinery for determining an orbit from minimal observations. Where other astronomers' predictions scattered, Gauss's prediction pointed somewhere else entirely — and in early December, Baron von Zach swung his telescope to Gauss's coordinates and found Ceres, confirming it definitively on **31 December 1801: one year to the night after Piazzi first saw it**. Olbers found it independently the next evening. Gauss woke up famous across scientific Europe.

![[inventing-variance-ceres-comic.png|660]]

The moral hiding in the melodrama: Gauss did not beat the other computers of Europe by *observing* better — he had no telescope worth the name. He won by taking the **errors** seriously: treating the scatter in Piazzi's forty-one imperfect positions not as noise to be argued away but as a thing with structure, to be balanced against itself. The instinct that measurements *disagree by law, not by accident* is the founding instinct of statistics.

### Act III — The ugly little method, and the wounded Frenchman

The tool that grew out of this work is one your calculator uses daily: **least squares** — declare the best fit to be the one minimising the *sum of squared errors*. Squares, note, not absolute values: partly because squares punish a big error more than four small ones, and mostly for the unglamorous reason that squares *differentiate cleanly*, so the minimisation collapses into solvable linear equations. The philosophical dressing came later; the choice was engineering ([[Why Probability and Statistics]] carries that argument in full).

Then the wound. **Legendre published the method first** — 1805, in a memoir on comet orbits, with a clean exposition and the name that stuck (*méthode des moindres carrés*). Gauss, publishing his own account in 1809, added one sentence of acid: he had been using "our principle" **since 1795**. Legendre's reply survives, and it still stings to read: *"There is no discovery that one cannot claim for oneself by saying that one had found the same thing some years previously... it is by publication alone that a claim is established."* Gauss never yielded; he did this to other men too, and being usually *right* about the private priority made it crueller, not kinder. (Historians, for the record, still argue how much of the December miracle was least squares proper and how much Gauss's orbit machinery — what is certain is what each man printed, which is why the method obeys [[Stories/Stigler's Law of Eponymy]] twice over: "Gaussian" least squares named for the second publisher, the "Gaussian" curve named for neither of its inventors.)

In that 1809 book Gauss also gave least squares its justification: *if* measurement errors follow a particular bell-shaped law, then least squares is exactly what a rational person should do. Which bell-shaped law? The one that makes the humble arithmetic mean the best combination of repeated measurements — he reverse-engineered the error curve from the mean's good reputation. It was half-circular and he knew it; **Laplace** closed the loop within a year with the deeper theorem: sum many small independent causes and the bell curve emerges *regardless* of the causes' own shapes — the Central Limit Theorem. An observation's error is exactly such a sum (a tremor of the hand, a shimmer of air, a worn screw thread), and each small independent nudge adds in the perpendicular-arrows way that [[Linear Combinations of Random Variables]] proves. The quantity doing the bookkeeping in every one of these arguments — the thing that *adds* when causes combine — was the mean of squared deviations. It had no name. It would work nameless for a hundred years.

### Act IV — From stars to people: the shadow

The scene change is the uncomfortable part of this story, and the vault's rule is to keep difficult figures difficult.

**Francis Galton** — gentleman-scientist, Darwin's half-cousin, compulsive measurer of everything from boredom at lectures to the efficacy of prayer — took the astronomers' error mathematics and pointed it at *human beings*. He grew generations of sweet peas and weighed their seeds; he set up a laboratory at a London exhibition where Victorians **paid threepence to be measured** — height, strength of grip, keenness of sight — nine thousand of them, walking data points; and in the scatter of parents against children he found "regression toward mediocrity" and, later, the correlation coefficient. The spread of a population had become a measurable object.

And the purpose was never neutral. Galton built this apparatus in order to argue that human ability is inherited, and to advocate breeding humans accordingly — a programme he named himself, in 1883: **eugenics**. The statistics of human variation was not innocently discovered and later misused; substantial parts of it were *forged for that use*. The tools outgrew and outlived the purpose — every fair test and honest survey now runs on them — but the origin stands, and pretending otherwise would be worse statistics than anything in this story.

### Act V — The christening, and the thirty years' war

**Karl Pearson**, Galton's disciple and heir, industrialised the new science — and in 1893 gave the square root its name: the **standard deviation**, $\sigma$, chosen so the number lives in the same units as the data. (No relation, for any Edexcel student wondering, to the Pearson that prints textbooks and owns the exam board — that company grew out of S. Pearson & Son, a Yorkshire construction firm founded in 1844, which built railways and drained Mexico City long before it printed a page. The coincidence's punchline: the company's exam papers are full of this Pearson's inventions.) Pearson built the first statistics department, founded the journal *Biometrika*, invented the $\chi^2$ test in 1900 — and held the whole field in a grip that did not welcome correction. (He also directed the Galton Laboratory for National Eugenics; the shadow of Act IV runs straight through him.)

A brewer interrupts, briefly and charmingly: **W. S. Gosset** of Guinness — yes, *that* Guinness, the stout — working out how to draw conclusions from *tiny* samples of barley and yeast. The brewery had banned employee publications outright after an earlier paper leaked trade secrets, so its scientists wrote under aliases; Gosset, reportedly weighing "Pupil" first, published the mathematics in 1908 as **"Student"** — and science's most-used small-sample tool still wears the disguise. His $t$ lives on every formula sheet as *Student's t*, one more entry for Stigler's law.

Then **R. A. Fisher**. In 1918 — in a paper about *heredity*, not stars — he reconciled Mendel's discrete genes with the smooth, continuous variation Galton's school measured: many discrete inherited factors, each of small effect, summing to a bell curve — the Central Limit Theorem wearing a genome. (Notice the echo: just as [[Continuous Random Variables]] tells it, de Moivre had invented the continuous as a shortcut through the discrete in 1733; Fisher now showed biology's continuous traits *are* summed discreteness. Same bridge, crossed in the opposite direction.) To run the argument he needed to split a population's spread into addable inherited and environmental parts, and a quantity that *adds* deserved to be named for itself, not as somebody's square. In that paper the mean squared deviation finally got its word: **variance**. Analysis of variance — ANOVA, the workhorse of every experimental science — grew from the same root.

Fisher and Pearson then fought for the rest of Pearson's life — over the degrees of freedom in Pearson's own $\chi^2$ (Fisher was right; Pearson never conceded an inch), over journals used as weapons, over who had insulted whom first. Fisher carried his own shadows: a eugenics man himself, and in old age a tobacco-industry-funded voice insisting smoking had not been *proven* to cause cancer — the century's greatest statistician flunking the century's most important statistical question. Keep him difficult too.

## Cultural ripples

![[inventing-variance-timeline.svg|700]]

- **The ± is the fossil.** Every lab report's error bar, every poll's "margin of error", every GPS reading settling from a cloud of guesses — all of it is Gauss's Ceres bookkeeping, domesticated. The physics lab's [[Repeated Measurements]] and [[Error Propagation]] are this story's direct descendants.
- **A concept, engineered.** Variance was not *found*, it was *chosen* — over range, over mean absolute deviation — because it differentiates cleanly and it adds under independence. The lesson generalises: even the most fundamental-looking definitions in mathematics are winners of a usefulness contest ([[Why Probability and Statistics]] makes this the headline).
- **The word arrived last.** Practice (1801) → publication (1805) → justification (1809–1810) → institutionalisation (1890s) → *name* (1918). A hundred and seventeen years between the tool and its christening — worth remembering whenever a definition seems to have fallen from the sky.
- **The exam connection runs forward:** the unbiased $s^2$ and the sampling distributions of [[Sampling and Estimation]], the tests of [[Hypothesis Tests]], Student's $t$ and Pearson's $\chi^2$ — the cast of this story wrote the second half of the P6 and 9231 syllabuses between them.

## Where this surfaces in the vault

- [[Why Probability and Statistics]] — keeps the pedagogy this story dramatises: *why squared* (differentiability + additivity), and the two-distributions-same-mean puzzle that motivates spread.
- [[Linear Combinations of Random Variables]] — the additivity that made variance the winner, proved: independent noises add like perpendicular arrows.
- [[Normal Distribution]] and [[Stories/The Naming of Normal]] — the error curve at the centre of Act III, and its own naming saga.
- [[Continuous Random Variables]] — de Moivre inventing the continuous as a shortcut through the discrete; Fisher's 1918 paper crosses the same bridge the other way.
- [[Discrete Random Variables]] — where $\mathrm{Var}(X) = E(X^2) - \mu^2$ does its exam-day work.
- [[Sampling and Estimation]] and [[Hypothesis Tests]] — the machinery this cast built, syllabus-shaped.
- [[Repeated Measurements]] · [[Error Propagation]] — the physics lab as the story's living museum.
- [[Heptadecagon]] — the morning the protagonist chose mathematics.
- [[Stories/Stigler's Law of Eponymy]] — satisfied twice in one story (least squares, the Gaussian), then a third time by Student's $t$.

## Receipts

- S. M. Stigler, *The History of Statistics: The Measurement of Uncertainty before 1900* (1986) — the backbone: pre-history of combining observations, Legendre–Gauss, Galton, Pearson.
- D. Teets & K. Whitehead, "The Discovery of Ceres: How Gauss Became Famous," *Mathematics Magazine* 72 (1999) — the 1801 computation, and the scholarly caution about how much least squares it actually contained.
- R. L. Plackett, "Studies in the History of Probability and Statistics XXIX: The discovery of the method of least squares" (1972) — the priority dispute; Legendre's 1809 letter.
- F. von Zach, *Monatliche Correspondenz* (1801–02) — the recovery announcements; the epigraph quote as translated in the Ceres literature.
- R. A. Fisher, "The Correlation between Relatives on the Supposition of Mendelian Inheritance," *Trans. Roy. Soc. Edinburgh* 52 (1918) — the word's birth certificate.
- K. Pearson, "Contributions to the Mathematical Theory of Evolution" (1894) and lectures 1893 — "standard deviation" christened.
- F. Galton, *Natural Inheritance* (1889); the anthropometric laboratory records, International Health Exhibition 1884; *Inquiries into Human Faculty* (1883) — where "eugenics" is coined.
- "Student" [W. S. Gosset], "The Probable Error of a Mean," *Biometrika* 6 (1908).
- Piazzi's "something better" remark: his correspondence of January 1801, as quoted in the Ceres discovery literature (Foderà Serio, Manara & Sicoli, in *Asteroids III*, 2002).
