---
chinese: 统计谎言名人堂 (tǒngjì huǎngyán míngrén táng)
prerequisites:
  - "[[Why Probability and Statistics]]"
  - "[[Sampling and Estimation]]"
  - "[[Scatter Diagrams]]"
  - "[[Averages and Spread]]"
  - "[[The Lady Tasting Tea]]"
leads_to:
  - "[[Ethics and Ownership]]"
  - "[[Interpreting Data]]"
  - "[[Hypothesis Tests]]"
  - "[[Forward Reading and Problem Discovery]]"
tags:
  - type/story
  - type/meta
  - type/methodology
  - subject/mathematics
  - era/19c
  - era/20c
  - cast/farr
  - cast/snow
  - cast/nightingale
  - cast/gallup
  - cast/wald
  - cast/huff
  - cast/fisher
  - cast/bradford-hill
  - cast/anscombe
  - cast/bickel
  - region/europe
  - region/america
---

# Stats Lies Hall of Fame 统计谎言名人堂

> *Every exhibit in this hall is a number that was **correct**. The cholera really did fall with elevation. The bombers really did come back riddled in the wings. Berkeley really did admit 44% of the men and 35% of the women. Not one figure here was faked, and every one of them misled a room full of intelligent people — until somebody asked the only question that matters: **what got thrown away before this number was made?***

## Cast of Characters

- **William Farr** (1807–1883) — England's first medical statistician; found the "elevation law" of cholera and believed it proved bad air. Nightingale's statistical tutor. Changed his mind in 1866.
- **John Snow** (1813–1858) — anaesthetist to Queen Victoria and, in his spare time, the man who mapped the Broad Street pump and ran the first great natural experiment.
- **Florence Nightingale** (1820–1910) — nurse, administrator, and the first woman elected to the Royal Statistical Society; drew the chart that changed army medicine, and drew it wrong the first time.
- **George Gallup** (1901–1984) — the pollster who beat a survey fifty times larger than his in 1936, and was beaten by his own method in 1948.
- **Abraham Wald** (1902–1950) — Austrian mathematician, refugee, member of Columbia's Statistical Research Group; the bombers.
- **Darrell Huff** (1913–2001) — journalist; wrote the best-selling statistics book of all time, then used its tricks for the tobacco industry.
- **R. A. Fisher** (1890–1962) and **Austin Bradford Hill** (1897–1991) — the founder of modern statistics on the wrong side of the smoking question, and the epidemiologist who wrote the rules for the right side.
- **Frank Anscombe** (1918–2001) — four data sets, one set of numbers, 1973.
- **Peter Bickel, Eugene Hammel, J. William O'Connell** — the Berkeley statisticians who took their own university's discrimination statistics apart, 1975.

## 中文锚点

学校官网写着"我校毕业生平均年薪 30 万"。数字没造假，但它是**回收问卷**算出来的：混得好的愿意填，混得差的懒得回——这是**幸存者偏差**，二战时沃尔德就是靠它把弹孔的故事翻了个面：回来的飞机机翼上全是洞，那是因为**打中发动机的飞机根本没回来**，所以装甲要加在没有弹孔的地方。再看"平均年薪"这三个字本身：班上 30 个人，只要有一个月薪十万的，就能把平均值拉上天，**中位数**才是"典型的那个人"。再看"男生录取率高于女生，所以歧视"：伯克利 1973 年正是这样被告的，可按系一拆，六个大系里四个是女生录取率更高——是女生扎堆报了竞争最激烈的系，这就是**辛普森悖论**：把关键的那个变量平均掉，结论就翻转。这一整座"名人堂"里的每一个数字都是**真的**，骗人的不是数字，是**在算出这个数字之前被扔掉的东西**：谁没被算进去、按什么分组、分布长什么样、图的刻度和比例是什么、还有谁付了钱。猎人的问题只有一个：**这个数是怎么来的？**

## The Story

![[stats-lies-timeline.svg|1100]]

### Act I — The law of elevation and the two water companies (1849–1855)

In 1852 William Farr, compiler of abstracts at the General Register Office and the best medical statistician alive, published his analysis of the cholera epidemic of 1848–49. He had done what nobody before him could: tabulated deaths for every district of London against every variable he could obtain. One variable stood out with the cleanness of a physical law. **Cholera mortality fell as the ground rose.** The districts on the Thames flats died at ten times the rate of the districts on the northern heights, and the numbers in between fell off so regularly that Farr fitted a formula to them — mortality roughly inversely proportional to elevation — and printed it beside Boyle's law as a specimen of what statistics could find.

It was true. It is still true of that epidemic. And it was the best evidence anyone had for the wrong theory, because to Farr and to almost every physician in Europe the reason low ground killed was obvious: *miasma* — the foul air of the marshes, of the sewers, of the river at low tide — pooled where the land was low and thinned where it was high. The correlation was correct. The cause was underneath it, unmeasured: the low districts drank the tidal Thames.

John Snow thought the cause was in the water and had said so since 1849, to no effect. In September 1854 the Broad Street outbreak in Soho killed over five hundred people in ten days within a few hundred yards of one pump. Snow took the death registers, walked the streets, plotted each death as a black bar against its house, and found the bars clustering around the Broad Street pump — with the tell-tale exceptions a hunter loves: the workhouse with its own well, almost untouched; the brewery whose men drank beer, untouched; the widow in Hampstead who had the Broad Street water fetched to her because she liked its taste, dead. On 7 September he put this to the parish Board of Guardians, and on the 8th the pump handle was removed.

![[stats-lies-snow-pump-comic.png|640]]

Snow himself was honest about what that proved: the outbreak was already declining, because everyone who could had fled. The handle is the scene a student retells; the *evidence* was his other study, the one the textbooks call the Grand Experiment. Two companies supplied South London, their pipes running down the same streets, into neighbouring houses, sometimes into opposite sides of one court — the Southwark and Vauxhall Company drawing from the Thames at Battersea, among the sewer outfalls, and the Lambeth Company, which in 1852 had moved its intake upriver to Thames Ditton, above the tide. Same air, same elevation, same poverty, same streets; only the water differed, and *the customers had not chosen it*. Snow went door to door asking which company each dead household paid, and where the householder did not know he tested the water for salt. In the first seven weeks of the 1854 epidemic, Southwark and Vauxhall customers died at **315 per 10,000 houses**; Lambeth customers at **37**. An eight-and-a-half-fold difference, with the confounders held fixed by the accident of the pipes.

The Board of Health's own committee rejected his theory in 1855, and the pump handle went back. But Farr — to his lasting credit — was the kind of statistician who lets the data outvote him. When cholera came again in 1866 he traced the East London deaths to the East London Water Company's unfiltered reservoir at Old Ford, and said so in print. The elevation law was never false. It was a correlation that had a cause hiding under it, and the man who found it was the man who eventually found the cause.

### Act II — Nightingale draws it twice (1855–1858)

Farr's other pupil was a nurse. Florence Nightingale reached the barrack hospital at Scutari in November 1854 and found the arithmetic of the Crimean War: in **January 1855, 2,761 soldiers died of disease, 83 of wounds, and 324 of other causes, from an army of 32,393**. Turn that into her unit, deaths per thousand per year, and disease alone was running at **1,023 per thousand** — a rate at which the entire British army in the East would have been dead in under a year. Over the whole war the ratio was **eight dead of disease for every one dead of a wound** (`stats-lies-nightingale.py` recomputes every figure from her tables).

She knew that a table of these numbers would be read by no one who mattered. Back in London, working with Farr on the evidence for the Royal Commission, she designed a diagram to do what the table could not — in her own words, to affect through the eyes what they had failed to convey through the public's "word-proof ears". Twelve wedges for twelve months, arranged round a circle like the petals of a flower; blue for the deaths from disease, red for wounds, black for the rest. The eye takes in a year of dying in one look, and sees that the blue dwarfs the red in every month.

![[stats-lies-nightingale-coxcomb.svg|1100]]

Here is why she belongs in a hall of *lies*. Her first version of the diagram made each wedge's **radius** proportional to the death rate. A wedge's area grows with the *square* of its radius, so every ratio the eye reads off it is squared: the peak disease rate was **8.8 times** the peak wounds rate, and the radius-scaled chart shows it as **78 times**. The right-hand figure above is that chart. Nightingale caught the error herself, withdrew the diagram, and redrew it with the **area** of each wedge proportional to the rate — the left-hand figure, the one printed in her 1858 *Notes*. Her cause was just and her numbers were true, and the chart still had to be corrected, because a picture has a scale whether or not its author has thought about it.

The second rose in her original diagram — the year after the Sanitary Commission of March 1855 flushed the sewers and ventilated the wards — has wedges a third the size. Disease deaths fell from **11,157** in the first year to **3,319** in the second. The chart persuaded; the persuasion was earned.

### Act III — Two million four hundred thousand wrong answers (1936)

The *Literary Digest* had called every presidential election since 1916. In 1936 it mailed **ten million** ballots and received **2.4 million** back — still the largest poll ever taken — and announced that Alf Landon would beat Franklin Roosevelt with 57% of the vote. Roosevelt took 61% and forty-six of forty-eight states.

The mailing list came from telephone directories and automobile registrations, and in the seventh year of the Depression a household with a telephone and a car was not a household chosen at random. Worse — and this is the half that the textbooks skip — the people who *returned* the ballot were not the people who received it: the angry answer back, the contented do not. Sampling frame and non-response, both tilted the same way, and no quantity of ballots could untilt them. George Gallup, with a sample of about fifty thousand chosen by quota to *look like* the country, called Roosevelt — and, in July, had published a prediction of what the *Digest* would wrongly say. The magazine folded within two years. [[Sampling and Estimation]] carves the lesson over its door: **size cures noise and does nothing for bias.**

The hall keeps the sequel too. In 1948 Gallup's quota method had its own catastrophe — "Dewey Defeats Truman" — because interviewers filling quotas chose whom to stop, and chose the well-dressed. The cure was to take the choosing out of human hands altogether. Random sampling is not a preference; it is what is left when every way of choosing has been caught lying.

### Act IV — The holes that were not there (1943)

![[stats-lies-wald-bomber-comic.png|640]]

The Statistical Research Group met in a Columbia University building on West 118th Street and worked, under wartime contract, on any problem the armed services brought. Its roster reads like a later century's Nobel list, and its most unlikely member was Abraham Wald — a mathematician from Cluj who had been barred from a university post in Vienna for being Jewish, had fled after the Anschluss in 1938, and was now, as an enemy alien, formally forbidden to read the classified reports his own work went into.

The problem the Air Forces brought was armour. Armour is heavy, and every pound of it is a pound less of fuel or bombs, so it had to go only where it mattered. The bombers coming back from Europe were surveyed for damage, and the pattern was clear: hits clustered on the wings, the fuselage, the tail gunner's position — and were sparse on the engines and the cockpit. The engineers' first instinct was the obvious one: armour where the hits are.

Wald's answer, worked out in a series of memoranda that stayed classified until 1980, was that the survey was a census of **the planes that had come back**. A plane hit in the engine had gone into the Channel; it was not in the hangar to be counted. The clean patches on the survivors were not the places the enemy failed to hit — they were the places where a hit was fatal. Armour the engines. His actual memoranda did more than the anecdote remembers: he built a method for estimating, region by region, the probability that a hit there downs the plane, using the damage distribution of the survivors together with the known fraction of planes lost, so that the missing data could be *reconstructed* rather than merely noticed. But the anecdote has survived because its one sentence is the hunter's whole discipline: **whose data is this, and whose is missing?**

Wald did not live to see his memoranda declassified. In December 1950, on a lecture tour of India at the invitation of the Indian government, he and his wife died when their aircraft flew into the Nilgiri hills.

### Act V — The field guide, and the expert witness (1954–1965)

In 1954 a magazine journalist named Darrell Huff published a small, funny book called *How to Lie with Statistics*, illustrated with cartoons of gullible readers and sharp-eyed salesmen. It has sold more copies than any statistics book ever written. Its chapters are the hall's floor plan: the well-chosen average (mean where the median would embarrass), the sample with the built-in bias, the gee-whiz graph (a truncated axis that turns a 3% rise into a cliff), the one-dimensional picture (a moneybag drawn twice as tall — and twice as wide, so four times the area), the semi-attached figure (a true number about the wrong thing), and the *post hoc* chapter on correlation and cause, with its example of storks and babies. Read it at fifteen and you are inoculated for life.

![[stats-lies-huff-hearing-comic.png|640]]

Which is what makes the sequel the hall's most uncomfortable exhibit. In 1965, as the United States Congress debated the first health warnings on cigarette packets, the expert witness who appeared to argue that the statistical case against smoking was unproven was Darrell Huff. He used his own book — the storks, the semi-attached figure, the "mere correlation" — to make the evidence of Doll and Hill sound like a magician's trick. The tobacco industry's own files, opened by litigation decades later, show it had paid him, and had commissioned from him a companion volume, *How to Lie with Smoking Statistics*, that was never published. The man who taught the world to spot the lie had hired himself out to tell one, with the same tools.

He was not alone, and the other name is heavier. R. A. Fisher — the inventor of the significance test, the randomised experiment and half of modern statistics, whose own story is told in [[The Lady Tasting Tea]] — spent his last years arguing that the smoking–cancer correlation might be explained by a genotype that inclined people both to smoke and to cancer, and did so as a paid consultant to the Tobacco Manufacturers' Standing Committee. His methodological point was correct: correlation *is* not causation, and a confounder *can* produce one. What he would not concede was that the point has an answer.

The answer came from Austin Bradford Hill, in a 1965 lecture that every epidemiologist still learns: nine "viewpoints" by which an association earns the right to be called a cause — its **strength** (smokers' lung-cancer death rate was ten to twenty times non-smokers'), its **consistency** across studies and countries, its **specificity**, its **temporality** (the smoking came first), its **biological gradient** (the more cigarettes, the more cancer — a dose–response curve), its **plausibility**, its **coherence** with what else is known, **experiment** (doctors who quit saw their risk fall over the following years, which no genotype can explain), and **analogy**. None is a proof; together they are the machinery by which a correlation is *interrogated* rather than either swallowed or waved away. Hill and Doll's British Doctors Study ran from 1951 to 2001 and answered every one of them.

### Act VI — Four data sets, one number (1973)

Frank Anscombe was tired of statisticians who computed and did not look. In 1973 he published four small data sets of eleven points each. They have the same mean of $x$, the same mean of $y$, the same variances, the same correlation coefficient of 0.82, and the same regression line, $y = 3 + 0.5x$, to two decimal places — `stats-lies-anscombe.py` recomputes all of it. Then he plotted them.

![[stats-lies-anscombe-quartet.svg|900]]

One is the well-behaved cloud the numbers imply. One is a perfect curve that a straight line insults. One is a perfect straight line with a single point pulling the fit off it. One is ten points with the same $x$ and one point, far away, that *is* the correlation single-handed. Every summary statistic in [[Scatter Diagrams]] is a compression, and a compression throws information away by design; the quartet is the proof that what it throws away can be everything. The modern encore, from 2017, is a set of twelve data sets with identical statistics one of which is a dinosaur.

### Act VII — The university that discriminated in aggregate and nowhere in particular (1973–1975)

In autumn 1973 the University of California, Berkeley admitted **44% of the 8,442 men** who applied to its graduate programmes and **35% of the 4,321 women**. The difference was far too large to be chance, the university feared a lawsuit, and three of its own statisticians were asked to find where the discrimination was.

They could not find it. Department by department — and admissions decisions are made by departments, not by the university — the pattern dissolved. In the six largest departments, which `stats-lies-berkeley.py` reproduces from their paper, women were admitted at a *higher* rate than men in four of the six, and in the largest department of all by twenty points. The aggregate said 44 against 30; the parts said, if anything, the reverse.

![[stats-lies-berkeley-simpson.svg|900]]

The figure shows where the aggregate came from. The departments women applied to in large numbers — C, D, E, F, at the right of the picture — were the departments that rejected almost everyone, of either sex; the departments men applied to — A and B, at the left — took two-thirds of all comers. Women were not being rejected more often *where they applied*; they were applying where rejection was the norm. Run the counterfactual and it is stark: had the women applied to departments in the men's proportions, their overall admission rate would have been **52%**, higher than the men's. This is **Simpson's paradox** — a trend that reverses when a lurking variable is conditioned on — and Bickel, Hammel and O'Connell's 1975 paper in *Science* is its founding document.

Their conclusion is the part worth carrying away, because it is not "no bias". The aggregate number was true, and the bias it pointed at was real — but it was not in the admissions committees. It was upstream, in whatever had steered women, long before they applied, towards the crowded and underfunded fields. The paradox does not make the discrimination vanish; it moves it to the place where it actually happened, which is the only place it could ever have been fixed. That is what conditioning on the right variable *does*: it is not a trick for making an inconvenient number go away, it is the act of asking where the number came from.

## The hunter's checklist — what was thrown away

Every exhibit above was caught by one of six questions, and a student who carries them is armoured against most of what will be said to them with a number attached. Each is a specific form of the single question [[Forward Reading and Problem Discovery]] asks of everything: *what produced this?*

1. **Who is missing?** The planes that did not come back; the households without a telephone; the ballots that were not returned; the graduates who did not answer the salary survey. A number is a census of *those who were counted*, and the uncounted are usually the point. (Wald, the *Literary Digest*.)
2. **Which subgroup?** An aggregate averages over a structure. Ask what the whole was made of, and whether the parts agree with it. (Berkeley.)
3. **What shape is the distribution?** A mean is a single point standing in for a whole shape, and for a skewed shape it stands in badly — the median is the typical case; the mean is the typical case plus the billionaire who walked in. ([[Averages and Spread]], Huff's well-chosen average.)
4. **What scale is the picture on?** Areas square the ratio; a truncated axis multiplies the slope; a two-dimensional icon for a one-dimensional quantity lies by a power of two. (Nightingale's first chart, the gee-whiz graph.)
5. **What else moves with it?** A correlation is two things that vary together; ask what third thing could be moving them both, and then ask — Hill's nine viewpoints — whether the case for cause has been *made* rather than assumed or dismissed. (Farr's elevation, Fisher's genotype.)
6. **Who paid for the number?** Not because paid numbers are false — Nightingale's were paid for by the War Office and were true — but because the answer tells you which of the other five questions to ask first. (Huff, 1965.)

And one habit above the six: **plot it.** Anscombe's quartet is the standing proof that the numbers can agree while the pictures disagree, and the picture is the one that is right.

## Cultural ripples

- **Every polling organisation on earth is a descendant of 1936 and 1948.** Random sampling, response-rate reporting and the published margin of error are all scars from specific lies in this hall.
- **"Survivorship bias" has become an ordinary phrase**, applied to venture-capital success stories, to the buildings that survived from antiquity, to the advice of the successful — every one of them Wald's bombers with the engines off-screen.
- **Simpson's paradox is now a legal argument.** It appears in discrimination cases, in medical trials where a treatment helps each subgroup and harms the whole, and in every attempt to compare hospitals by their raw death rates without asking who they admit.
- **Bradford Hill's viewpoints are the standard by which a correlation is now allowed to become a cause** — in medicine, in environmental regulation, in the courts — and the tobacco hearings are the reason the standard was written down.
- **Huff's book is still in print and still assigned.** Its author's second career is a footnote most editions omit, which is itself a semi-attached figure.

## Where this surfaces in the vault

- [[Why Probability and Statistics]] — the hunter test, *stats lie, causality tends not to*; its three classic lies are Acts IV, VII and the well-chosen average, told there as method and here as history.
- [[Sampling and Estimation]] — the *Literary Digest* callout and the hunter's gallery of tilted spoons; bias versus noise, and why size fixes only one.
- [[Scatter Diagrams]] — correlation, regression, Anscombe's quartet and the Datasaurus; **plot it**.
- [[Averages and Spread]] — mean, median and the skewed distribution that makes the choice matter.
- [[Interpreting Data]] — the IGCSE skill this hall is the museum for: reading a chart for what its author chose to leave out.
- [[Hypothesis Tests]] — Fisher's 5% and the p-hacking it invited; the test as a gate that a determined liar can walk through twenty times.
- [[The Lady Tasting Tea]] — Fisher's genius and its final blind spot, told in full.
- [[Forward Reading and Problem Discovery]] — a hunter is someone who can constantly trace causality; this card is that rule applied to numbers.

## Receipts

1. W. Farr, *Report on the Mortality of Cholera in England, 1848–49* (General Register Office, 1852) — the elevation law and its miasmatic reading; Farr's 1866 report on the East London epidemic for his change of mind.
2. J. Snow, *On the Mode of Communication of Cholera*, 2nd ed. (1855) — the Broad Street map, his own caveat that the outbreak was declining, and the South London comparison of the two water companies (315 vs 37 deaths per 10,000 houses in the first seven weeks).
3. F. Nightingale, *Notes on Matters Affecting the Health, Efficiency and Hospital Administration of the British Army* (1858) — the monthly tables and the polar-area diagram; H. Small, "Florence Nightingale's statistical diagrams" (1998), on the withdrawn radius-scaled version. Data as tabulated in the `HistData::Nightingale` set; `stats-lies-nightingale.py`.
4. P. Squire, "Why the 1936 *Literary Digest* poll failed", *Public Opinion Quarterly* 52 (1988) — frame bias and non-response weighed against each other; the 1936 and 1948 Gallup episodes.
5. A. Wald, *A Method of Estimating Plane Vulnerability Based on Damage of Survivors* (Statistical Research Group memoranda, 1943); reprinted with commentary in M. Mangel & F. Samaniego, *Journal of the American Statistical Association* 79 (1984). W. A. Wallis, "The Statistical Research Group, 1942–1945", *JASA* 75 (1980), for the group and its members.
6. D. Huff, *How to Lie with Statistics* (1954). A. Reinhart, "Huff and puff", *Significance* 11 (2014), and the Truth Tobacco Industry Documents archive, for the 1965 testimony and the unpublished *How to Lie with Smoking Statistics*.
7. R. Doll & A. B. Hill, "Smoking and carcinoma of the lung", *BMJ* (1950); R. A. Fisher, "Cancer and smoking", *Nature* 182 (1958); A. B. Hill, "The environment and disease: association or causation?", *Proceedings of the Royal Society of Medicine* 58 (1965); R. Doll et al., "Mortality in relation to smoking: 50 years' observations on male British doctors", *BMJ* 328 (2004).
8. F. J. Anscombe, "Graphs in statistical analysis", *The American Statistician* 27 (1973) — the four data sets; J. Matejka & G. Fitzmaurice, "Same stats, different graphs" (CHI 2017) — the Datasaurus Dozen. `stats-lies-anscombe.py`.
9. P. J. Bickel, E. A. Hammel & J. W. O'Connell, "Sex bias in graduate admissions: data from Berkeley", *Science* 187 (1975) 398–404 — the aggregate figures, the six-department table and the "shunted upstream" conclusion. `stats-lies-berkeley.py`.
