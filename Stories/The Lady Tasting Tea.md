---
chinese: 品茶的女士 (pǐn chá de nǚshì) — 八杯茶与百分之五
prerequisites:
  - "[[Hypothesis Tests]]"
  - "[[t-Tests]]"
  - "[[Chi-Squared Tests]]"
  - "[[Non-Parametric Tests]]"
  - "[[Why Probability and Statistics]]"
leads_to: []
tags:
  - type/story
  - subject/mathematics
  - era/20c
  - cast/fisher
  - cast/pearson
  - cast/gosset
  - cast/bristol
  - cast/neyman
  - region/europe
---

# The Lady Tasting Tea 品茶的女士

> *Eight cups. Four with the milk poured first, four with the tea. She says she can tell. The man with the thick glasses says: then we shall count the ways you could be lucky — and only a perfect score will do.*

## Cast of Characters

- **Ronald Aylmer Fisher** (1890–1962) — the near-blind Cambridge mathematician hired in 1919 to "rake over the muck heap" of seventy years of wheat data at Rothamsted; inventor of randomised experiments, analysis of variance, the 5% line, and most of the words in a modern statistics course. Brilliant, quarrelsome, and wrong about two things that mattered.
- **Muriel Bristol** (1888–1950) — algae specialist at Rothamsted, the lady who could taste which went into the cup first.
- **William Roach** — chemist, witness to the tea, later Bristol's husband.
- **Karl Pearson** (1857–1936) — founder of mathematical statistics, inventor of the $\chi^2$ test, editor of *Biometrika*, and for twenty years Fisher's enemy.
- **William Sealy Gosset** (1876–1937) — Guinness brewer, "Student", inventor of the $t$-test; friend to both Pearson and Fisher, and the only man either of them would listen to.
- **Jerzy Neyman** (1894–1981) and **Egon Pearson** (1895–1980) — who turned Fisher's test into a decision rule, and earned his last great fury.

## 中文锚点

1920年代的一个下午，英国洛桑农业试验站的茶歇上，一位女士说她能尝出一杯奶茶是先倒奶还是先倒茶。费希尔（R. A. Fisher）当场设计了实验：八杯茶，四杯先奶四杯先茶，**随机**排列，请她挑出先奶的四杯。一共 $\binom84=70$ 种挑法，全对的概率只有 $1/70\approx1.4\%$；对三杯的挑法有 16 种，加起来 $17/70\approx24\%$——所以**只有全对才算数**。这场茶歇里诞生了现代实验的三样东西：**随机化**、**零假设**（"她其实分不出来"）和**显著性水平**（多大的巧合才不算巧合）。故事的另外两条线：费希尔与皮尔逊长达二十年的决裂——$\chi^2$ 的自由度之争，皮尔逊拒登他的文章，他便自己算临界值表；今天公式表上只印 5% 与 1% 两列，正是这段恩怨的遗产——以及酿酒师戈塞特（"Student"），两人之间唯一的和事佬。两件该诚实面对的事：费希尔是坚定的优生学者，晚年又拿烟草公司的钱反对"吸烟致癌"——一个把"相关不等于因果"说得最响亮的人，最后用这句话来堵别人的嘴。

## The Story

### Prologue — the cup

Harpenden, Hertfordshire, an afternoon in the 1920s. The scientists of the Rothamsted Experimental Station take their tea together, and a man with a beard and spectacles as thick as bottle-ends pours a cup for the woman beside him. She declines it: he has put the milk in after the tea, and she prefers it the other way. He scoffs — surely it makes no difference to the taste. She says she can tell. The chemist William Roach, who will later marry her, hears the man say: *"Let's test her."*

That is the whole of the legend, and it is probably true; Roach told it that way, and so did others who were in the room. What Fisher did next is not legend. He wrote it down, fifteen years later, as the second chapter of *The Design of Experiments* (1935) — and it is, with very little exaggeration, the chapter from which every controlled experiment you have ever read about descends. [1]

### Act I — counting the ways you could be lucky

Fisher's design was this. Make eight cups: four with milk first, four with tea first. Present them in **random order** — random in the strict sense, decided by a shuffle she cannot see, so that no pattern in the serving can help her. Tell her there are four of each. Ask her to pick out the four milk-first cups.

Then ask the question that had not been asked that way before: *if she cannot tell at all — if she is guessing — how likely is what we see?* There are $\binom{8}{4} = 70$ ways to choose four cups from eight, and a guesser hits every one of the four milk-first cups in exactly one of them: **one chance in seventy**, about $1.4\%$. Getting three right is much easier — $4 \times 4 = 16$ of the seventy ways — so "three or more right" happens to a guesser $17/70 \approx 24\%$ of the time, which is not rare at all. Fisher's conclusion followed without any further machinery: **only a perfect score would do.** Three out of four, however impressive at a tea table, could not be distinguished from luck. [1]

Notice what is *not* in the experiment: no measurement, no bell curve, no assumption about the lady's palate. The null hypothesis — *she has no discrimination* — fixes the probability of every outcome by **counting arrangements**, and the verdict is a threshold on how rare the observed arrangement is. It is a permutation test, the grandfather of every test in [[Non-Parametric Tests]]; it is also, with the arrangements written in a $2 \times 2$ table, *Fisher's exact test*, the one the Beyond of [[Chi-Squared Tests]] recommends when the counts are too small for Pearson's curve. And the *randomisation* is not decoration: it is what makes the count honest. If the cups had been served milk-first-four-then-tea-first-four, the lady might have noticed the pots were poured in that order — and the seventy-ways calculation would be about a different experiment from the one she actually faced.

![[lady-tasting-tea-comic.png|697]]

Did she pass? Fisher, writing the chapter, does not say. The people who were there did: she got them all. [2]

### Act II — the muck heap, and the 5%

Fisher had come to Rothamsted in 1919 because he had turned down Karl Pearson. Pearson, the grand old man of British statistics, had offered the young man a post at the Galton Laboratory — on condition that he publish only what Pearson approved. Fisher took the agricultural job instead, at a station whose claim to fame was Broadbalk: a wheat field that had been harvested and fertilised in recorded plots every year since 1843. Seventy years of yield figures, rain, manure and weather sat in the ledgers, and the director, John Russell, wanted to know whether they meant anything. Fisher's own description of the task was that he had been hired to rake over the muck heap. [3]

What he found in it was that almost nothing could be concluded, because the old experiments had never been designed to let chance be priced. A plot that did better might have done so because of the fertiliser or because it lay at the better-drained end of the field; without randomisation the two could not be told apart. So he invented the machinery to tell them apart: randomised plots, replication, the Latin square, the *analysis of variance* that splits the scatter of yields into the part the treatment explains and the part it does not. The tea-tasting afternoon is the toy version; Broadbalk is the real one.

In 1925 he put the machinery into a book for people who were not mathematicians — *Statistical Methods for Research Workers* — and on one page set down a sentence that has governed science ever since:

> *"The value for which P = .05, or 1 in 20, is 1.96 or nearly 2; it is convenient to take this point as a limit in judging whether a deviation is to be considered significant or not."* [4]

*Convenient.* He never claimed more for it. Five per cent was a line a working biologist could remember — about two standard errors — and Fisher himself moved it freely, asking for $1\%$ when the claim was surprising. What happened next was not his doing and would have appalled him: the line hardened into law. Journals accepted $p < 0.05$ and rejected $p = 0.06$; careers were built on which side of $1/20$ a number fell; a century later the American Statistical Association would have to issue a formal statement reminding the world that the number was a convenience and not a verdict. [5] The tea table had taught that *how rare must the coincidence be?* is a question you must answer before you look; the textbooks taught that the answer was always twenty.

### Act III — the feud, and the table you are given in the exam

There is a reason *Statistical Methods for Research Workers* contains tables of the kind that sit on a formula sheet — a handful of critical values at 5% and 1% — rather than the full tables of probabilities a scholar might want. The full tables existed. Karl Pearson had published them in *Biometrika*, and Pearson held the copyright, and **Pearson would not let Fisher use them**. So Fisher computed what he needed himself and printed only the percentage points. The slim critical-value table — *the row for $\nu$, the column for $5\%$* — that every 9231 student reads off MF19 for the $t$, the $\chi^2$ and the Wilcoxon tests is, in its format, a fossil of a refused permission. [6]

The feud had been running since 1917. Pearson had publicly criticised Fisher's first major paper; the Royal Society of London — with Pearson as a referee — had declined his 1918 paper reconciling Mendel's genetics with Galton's continuous heredity (the Royal Society of Edinburgh printed it instead, at the urging and partly at the expense of Darwin's son Leonard); and in 1922 Fisher published the correction that sits on every student's formula sheet without comment — that Pearson's $\chi^2$ test for a contingency table has $(r-1)(c-1)$ degrees of freedom and not $rc - 1$, and that every parameter fitted from the data costs one more. Pearson was sixty-five, Fisher thirty-two, and Pearson had been wrong for twenty-two years. He replied in his own journal, in his own voice, and never conceded. Fisher stopped submitting to *Biometrika*; Pearson stopped citing Fisher; the two men shared a country and a science and did not speak. ([[Chi-Squared Tests]] tells the mathematical half of this; the human half is that Fisher was right, knew it, and could not help saying so.) [7]

### Act IV — the brewer in the middle

The one person on speaking terms with both was a brewer. William Sealy Gosset ran experiments for Guinness in Dublin on barley and hops with samples too small for Pearson's large-sample theory, and in 1908 — under the pen-name "Student", because Guinness did not permit its staff to publish — he had worked out, half by algebra and half by drawing cards from a hat, the distribution that small samples actually follow. ([[t-Tests]] tells it: the curve with the fatter tails, and the 1.96 that becomes 2.26 when you only have ten.) Pearson, whose laboratory Gosset had visited, published it and did not think much of it; small samples were for brewers.

In 1912 a Cambridge undergraduate named Fisher read Student's paper, proved the result properly — in $n$ dimensions, which Gosset cheerfully admitted he could not follow — and sent Gosset the proof. Gosset forwarded it to Pearson, who filed it. It was Fisher who, a decade later, saw what Student had actually done: given every experimental scientist with ten measurements a valid test, and given the whole subject its first *exact* small-sample distribution. Fisher made the $t$-test the centrepiece of *Statistical Methods*, named it, tabulated it, and called Gosset "the Faraday of statistics" — the experimenter who found the thing the theorists would spend a generation explaining. [8]

Gosset, for his part, spent the 1920s writing gentle letters to both men — to Fisher, whose proofs he could not always follow and whose temper he could; to Pearson, whose tables he used and whose pride he understood — and remained, until his death in 1937, the only bridge between them. It is a curious fact of the subject that its three founding quarrels were mediated by a man whose day job was beer.

### Act V — the decision rule, and the last fury

Fisher's test answered one question: *is this sample surprising enough, under the null, to be worth reporting?* In 1928–33 Egon Pearson — Karl's son — and the Polish mathematician Jerzy Neyman asked a different one: *if you must decide, between this hypothesis and that one, what rule minimises how often you are wrong in the long run?* Out of that came the two kinds of error, the power of a test, the "reject / do not reject" vocabulary, and the idea that a significance level is the rate of false alarms you agree to tolerate across many decisions — the "trace and threshold" reading in [[Why Probability and Statistics]].

Fisher loathed it. To him a test was an act of scientific inference about *this* experiment, not a quality-control rule for a factory of experiments; he wrote, acidly, that the Neyman–Pearson approach treated science the way a Soviet five-year plan treated a farm. The two frameworks were never reconciled in his lifetime. What students learn today — *state $H_0$ and $H_1$, fix the level, compute, compare, conclude* — is a hybrid that neither side would quite have signed, with Fisher's significance level and Neyman's alternative hypothesis bolted together. It works; it is also why the conclusion sentence in an exam is so carefully hedged. The hedging is the seam between two men who did not agree about what a test *is*. [9]

### Epilogue — the hunter who stopped tracing

Two honest edges, because Fisher's story has them and the vault does not sand them off.

**The eugenics.** Fisher was a committed eugenicist from his student days — a founder of the Cambridge University Eugenics Society in 1911, a man who believed the fall of civilisations was caused by the "better" classes having fewer children, and who with his wife Eileen had eight children partly as a matter of principle. The last third of *The Genetical Theory of Natural Selection* (1930), the book that otherwise founded modern evolutionary theory, is an argument about differential fertility that reads very badly now and did not read well to everyone then. He never repudiated it. [10]

**The tobacco.** In 1950 Richard Doll and Austin Bradford Hill published the study that linked smoking to lung cancer; by the mid-1950s the evidence was overwhelming. Fisher — a pipe smoker — spent his last years arguing in letters and articles that the correlation might not be causal: perhaps a common genetic factor made people both smoke and develop cancer. The argument was not stupid; *correlation is not causation* is a sentence he did more than anyone to teach. But he did not pursue it as a hunter pursues a trace — gathering the evidence that would settle it either way. He took a paid consultancy from the Tobacco Manufacturers' Standing Committee, and he kept saying the same thing as the evidence piled up against him. The man who had built the whole apparatus for pricing coincidence chose, at the end, not to price this one. He died in 1962, in Adelaide, of cancer of the colon. [11]

That is the edge worth keeping in view when the tea story is told as a triumph. Fisher gave science the tool for telling luck from signal — and then showed, in his own last decade, that the tool does not work on a man who has decided in advance what he wants it to say. The hunter's spirit is not the apparatus. It is the willingness to keep tracing.

## Cultural ripples

- **Every controlled trial.** Randomise, replicate, fix the null, fix the level *before* you look — the tea table's four rules are the protocol of every clinical trial, agricultural trial and A/B test run since. The phrase *randomised controlled trial* is Fisher's afternoon, industrialised.
- **"Statistically significant"** entered ordinary English from a 1925 handbook for biologists, and the *convenient* line at 1 in 20 became the gatekeeper of publication in every empirical science. The replication crisis of the 2010s — thousands of published results that would not repeat — is in large part the bill for treating Fisher's convenience as a law; the 2016 ASA statement and the journals that have since banned the phrase are the slow correction. [5]
- **The format of the formula sheet.** Critical-value tables — percentage points only — exist because one man would not let another reprint his tables. You read Pearson's refusal every time you look up $t_9$ at 5%.
- **Fisher's exact test** — the eight-cups calculation, generalised — remains the standard for small $2\times2$ tables a century on, and the permutation idea behind it ("if the labels don't matter, shuffle them") is how modern computers test almost anything.
- **"The Lady Tasting Tea"** became the title of David Salsburg's 2001 history of twentieth-century statistics, and the phrase by which the whole field now names its founding scene.

## Where this surfaces in the vault

- [[Hypothesis Tests]] — the five-step ritual is the tea table formalised; the significance level as a threshold chosen *before* the data is the lesson of Act I.
- [[Non-Parametric Tests]] — the eight-cups test is a permutation test: *count the ways* under the null; the Wilcoxon tables are built exactly so.
- [[Chi-Squared Tests]] — Pearson's invention, Fisher's correction, and Fisher's exact test for the small tables where the curve fails; the quarrel of Act III told from the mathematical side.
- [[t-Tests]] — Gosset's distribution, Fisher's proof, the "Faraday of statistics".
- [[Why Probability and Statistics]] — *the trace and the threshold* (Fisher vs Neyman–Pearson) and *counted, not measured* (the tea test as the purest case); the Epilogue is that card's hunter, failing.
- [[Permutations and Combinations]] — $\binom84 = 70$, the whole test.

## Receipts

1. R. A. Fisher, *The Design of Experiments* (Oliver & Boyd, 1935), ch. II, "The Principles of Experimentation, Illustrated by a Psycho-Physical Experiment" — the eight cups, the seventy arrangements, the randomisation argument, and the sentence *"a lady declares that by tasting a cup of tea made with milk she can discriminate whether the milk or the tea infusion was first added to the cup."*
2. Joan Fisher Box, *R. A. Fisher: The Life of a Scientist* (Wiley, 1978), p. 134 — the Rothamsted afternoon, Bristol and Roach; David Salsburg, *The Lady Tasting Tea* (Freeman, 2001), ch. 1, reporting H. Fairfield Smith's account that she got them all right.
3. Box (1978), chs. 4–5 — the offer from Pearson with its publication condition, the move to Rothamsted in 1919, "rake over the muck heap".
4. R. A. Fisher, *Statistical Methods for Research Workers* (Oliver & Boyd, 1925), the chapter on the normal distribution — the "P = .05 … convenient" sentence.
5. R. L. Wasserstein & N. A. Lazar, "The ASA's Statement on p-Values: Context, Process, and Purpose", *The American Statistician* 70 (2016); Open Science Collaboration, "Estimating the reproducibility of psychological science", *Science* 349 (2015).
6. Box (1978) and Salsburg (2001) both record Pearson's refusal to let Fisher reprint the *Biometrika* tables and Fisher's consequent printing of percentage points only — the origin of the critical-value table format.
7. R. A. Fisher, "On the interpretation of χ² from contingency tables, and the calculation of P", *J. Royal Statistical Society* 85 (1922); Pearson's reply, *Biometrika* 14 (1922); Fisher's 1918 paper, "The correlation between relatives on the supposition of Mendelian inheritance", *Trans. Royal Society of Edinburgh* 52.
8. "Student" (W. S. Gosset), "The probable error of a mean", *Biometrika* 6 (1908); Fisher's 1912 letter and proof — Box (1978), ch. 3; Fisher's obituary "Student", *Annals of Eugenics* 9 (1939), the "Faraday of statistics" phrase.
9. J. Neyman & E. S. Pearson, "On the problem of the most efficient tests of statistical hypotheses", *Phil. Trans. Royal Society A* 231 (1933); R. A. Fisher, *Statistical Methods and Scientific Inference* (1956), ch. 4 — the five-year-plan remark; E. L. Lehmann, *Fisher, Neyman, and the Creation of Classical Statistics* (Springer, 2011).
10. R. A. Fisher, *The Genetical Theory of Natural Selection* (Clarendon, 1930), chs. VIII–XII; Box (1978) on the Cambridge Eugenics Society and the eight children.
11. R. Doll & A. B. Hill, "Smoking and carcinoma of the lung", *BMJ* (1950); R. A. Fisher, "Cancer and smoking", *Nature* 182 (1958) and *Smoking: The Cancer Controversy* (1959); P. D. Stolley, "When genius errs: R. A. Fisher and the lung cancer controversy", *American Journal of Epidemiology* 133 (1991) — the consultancy, the argument, and the verdict of history.
