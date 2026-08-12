---
chinese: 正态的命名 (zhèngtài de mìngmíng)
prerequisites:
  - "[[Normal Distribution]]"
leads_to: []
tags:
  - type/story
  - subject/mathematics
  - era/18c
  - era/19c
  - era/20c
  - cast/de-moivre
  - cast/gauss
  - cast/quetelet
  - cast/galton
  - cast/pearson
  - region/europe
---

# The Naming of Normal 正态的命名

> *The same bell curve told Quetelet that the average man was an ideal, and told Galton that the average man was mediocre. One of those readings gave us modern statistics. The other gave us eugenics. They were the same mathematics.*

## Cast of Characters

- **Abraham de Moivre** (1667–1754) — Huguenot exile in London; first wrote down the bell curve in 1733 as an approximation to coin-tossing. Did not think of it as a law of nature.
- **Carl Friedrich Gauss** (1777–1855) — attached the curve to measurement *error* in 1809 (the method of least squares); hence "Gaussian."
- **Adolphe Quetelet** (1796–1874) — Belgian astronomer who turned the error curve on *people* and invented *l'homme moyen*, the average man. Saw the average as the ideal.
- **Francis Galton** (1822–1911) — Darwin's half-cousin; discovered regression to the mean and correlation, and inverted Quetelet's value judgment. Coined the word *eugenics* in 1883.
- **Karl Pearson** (1857–1936) — Galton's disciple; built much of modern mathematical statistics, made "normal distribution" the standard name, and later regretted it.

## 中文锚点

**正态分布**（zhèngtài fēnbù，normal distribution）的"正态"二字，和英文 "normal" 一样，**偷偷夹带了一个价值判断**——"正"是"正常、正确、正规"，言下之意偏离它的就"不正常"（abnormal）。这正是这张卡片要讲的故事：钟形曲线本身没有褒贬，但人类给它起名字、用它衡量人的时候，把"平均"和"正常""理想"划上了等号。

核心戏剧：**同一条曲线，两种相反的读法。** 比利时人 Quetelet 把"平均人"（l'homme moyen，平均人）当作大自然的**理想**，偏离都是"误差"；而 Galton 把平均当作**平庸**，真正有意思的是分布的尾巴（天才、异禀）——这一念之转，直接通向了**优生学**（eugenics，优生学，Galton 1883 年造的词）。统计学最有用的工具（相关、回归）就是在这个项目里被发明出来的。这张卡片如实记录这段纠缠——既不洗白，也不假装数学本身有罪。

## Act I — The curve before it had a name (1733–1809)

The bell curve was born with no grand meaning attached. **Abraham de Moivre**, a Huguenot refugee earning his living tutoring in London coffee-houses, derived it in 1733 as a shortcut: if you toss a fair coin a great many times, the probabilities of the different totals trace out a smooth curve, and de Moivre found its formula. It was a *computational convenience*, nothing more.

Seventy-six years later **Gauss** gave it a job. In his 1809 work on the orbits of planets, he showed that if you make many measurements of the same quantity, each spoiled by small independent errors, the errors pile up in exactly this shape — and the curve's peak is the *best estimate* of the true value (the method of **least squares**, the variance-history thread of [[Why Probability and Statistics]]). This is why the curve is still called **Gaussian**. For Gauss it was a *law of errors* — a description of how mistakes scatter around a truth. The truth was real; the spread was imperfection.

That framing — *centre = truth, spread = error* — is the seed of everything that follows. The whole story is about what happens when you point that idea at human beings instead of at planets.

## Act II — Quetelet and the average man (1835)

**Adolphe Quetelet** was a Belgian astronomer who never got his observatory finished and turned, restlessly, to a stranger telescope: society. In *Sur l'homme et le développement de ses facultés* (1835) — "social physics" — he did something audacious. He took the astronomers' law of errors and aimed it at people.

He gathered the chest measurements of **5,738 Scottish soldiers** (lifted from an army medical journal) and the heights of French conscripts, plotted them, and found the same bell curve. From this he conjured ***l'homme moyen*** — the **average man** — whose every measurement sat at the peak of the curve.

Here is the move that mattered. For Gauss, the spread was *error around a true value*. Quetelet kept that exact framing and applied it to humans: the average man was the **true type** nature was aiming at, and every actual person was a slightly botched copy, scattered around the ideal by nature's "errors." The peak was not just typical — it was *good*. Deviations were imperfections. He even caught conscripts faking short stature to dodge the draft, because a suspicious dent appeared in the curve just below the height cutoff — the bell curve as a lie detector.

Quetelet's average man was a hopeful, almost utopian idea: study the average, improve the average, and you improve humanity. The bell curve, for him, pointed at a centre worth celebrating.

## Act III — Galton turns it upside down (1869–1889)

Then **Francis Galton** — polymath, geographer, Darwin's half-cousin — read Quetelet and kept the mathematics while flipping the meaning completely.

Galton was obsessed with the *exceptional*: genius, talent, "hereditary ability" (*Hereditary Genius*, 1869). When he looked at the same bell curve, he did not see an ideal at the centre. He saw **mediocrity** at the centre, and everything interesting out in the tails. Where Quetelet venerated the average man, Galton rather pitied him.

![[naming-of-normal-two-readings-comic.png|620]]

In pursuing how exceptional traits pass down generations, Galton discovered something genuinely deep. Measuring sweet-pea seeds (1875) and then the heights of parents and their grown children (*Regression towards Mediocrity in Hereditary Stature*, 1886), he found that **tall parents tend to have tall children — but closer to the average than the parents were**, and short parents likewise have short-but-closer-to-average children. He named the effect **regression** (originally "regression towards mediocrity"); it is the ancestor of the whole field of *regression analysis*, and of **correlation**, which he also invented.

![[naming-of-normal-regression.svg]]
*Galton's regression to the mean. Each point is a family: mid-parent height across, child height up. If children simply matched their parents, the cloud would hug the dashed $y=x$ line. Instead the best-fit line (solid) is **shallower** — its slope is about $\tfrac{2}{3}$, not $1$. Exceptionally tall parents have tall children who are, on average, a little closer to the population mean; exceptionally short parents, likewise. The extremes pull back toward the middle every generation. Galton found this disappointing — he wanted the exceptional to breed true.*

Regression to the mean is one of the most under-appreciated ideas in all of statistics — it is why "the rookie of the year slumps in season two," why "the speed camera that gets installed after a bad year sees fewer crashes the next year (whether or not it works)," and why so much of what looks like cause-and-effect is just extremes drifting back to ordinary. (See [[Why Probability and Statistics]] for why spotting it is a hunter's reflex.) Galton found the real thing. But the reason he went looking was a project that curdled.

## Act IV — The word "normal" (1873–1895)

The curve still had no settled name. Around 1875 three people reached for the same word almost simultaneously: **Charles Sanders Peirce** in America (1873), **Wilhelm Lexis** in Germany (1877), and **Galton** himself (1877) all began calling it the **"normal"** curve. The word originally meant something innocent and geometric — "normal" as in *perpendicular*, the "normal equations" of least squares — but it slid, fast, into its everyday meaning: *normal* as in *typical, proper, the way things ought to be*.

**Karl Pearson**, Galton's brilliant and forceful disciple, did not coin the term but fixed it in place. His relentless, exclusive use of "normal distribution" through his field-defining papers of the 1890s made it the standard, and it has never come loose since.

Late in life Pearson saw the trap he had helped spring. He wrote that the name had the unfortunate effect of making people believe "*that all other distributions of frequency are in one sense or another 'abnormal.'*" He was right. The word smuggles a verdict. To call this one curve **normal** is to quietly imply that everything that isn't bell-shaped — and everyone who isn't near the average — is *abnormal*. A neutral name ("Gaussian") was available. The field chose the loaded one, and we have lived inside its connotations ever since. (Chinese inherited the same freight: **正态** literally means "the proper/upright state.")

![[naming-of-normal-pearsons-regret-comic.png|560]]

## Act V — The eugenics shadow (honest edges)

This is the part that has to be told straight.

Galton's interest in the tails of the bell curve was never idle. From the 1860s he argued that human ability was hereditary and that society should encourage the "fit" to breed and discourage the "unfit." In 1883 he gave the program a name: **eugenics** (from the Greek for "well-born"). The same fascination that produced regression and correlation produced this.

And the connection is not incidental. **Much of modern mathematical statistics was built, by eugenicists, as a tool for eugenics.** Galton founded a laboratory for it; Pearson directed it and developed the correlation coefficient, the chi-squared test, and the machinery of biometrics substantially in its service; Ronald Fisher, who later founded modern experimental statistics and population genetics, was also a committed eugenicist. Correlation and regression — the daily bread of every science today — were partly born as instruments for ranking human worth.

What that program licensed in the wider world is the genuine horror. Eugenic argument fed directly into compulsory-sterilization laws across the United States from 1907; the U.S. Supreme Court upheld them in *Buck v. Bell* (1927), with Oliver Wendell Holmes writing "three generations of imbeciles are enough." Nazi Germany's 1933 sterilization law was explicitly modelled on the American statutes, and the logic ran on into the Holocaust.

The honest position is not that the mathematics is therefore tainted. Regression to the mean is true; the correlation coefficient is indispensable; the normal distribution really is the limit of [[Normal Distribution|almost everything]]. The honest position is that **these tools did not descend from a neutral heaven** — they were forged inside a project to sort human beings, by people who believed some humans were worth more than others, and the comfortable word *normal* was part of the same instinct. Knowing that is not a reason to distrust the statistics. It is a reason to stay alert to what gets smuggled in when a society decides what counts as "normal," and who doesn't. The vault keeps difficult biographies difficult rather than smoothing them — the same practice as [[Stories/Newton vs Hooke]], [[Stories/The Calculus Priority Dispute]], [[Stories/The Bernoulli Family]], and, most closely, [[Stories/Lewis Carroll the Mathematician]], whose honest-edges section is this card's peer.

## Cultural ripples

**The tyranny of the average.** Quetelet's average man is still everywhere. His "Quetelet index" — weight divided by height squared — is now the **BMI** printed on every medical chart, still treating a population average as a personal ideal, still criticised for exactly Quetelet's original sin. Standardised testing, IQ scores, growth percentiles, and the phrase "perfectly normal" all run on the same equation of *average* with *right*.

**The reckoning.** Around 2020 several institutions confronted the inheritance directly: University College London stripped Galton's and Pearson's names from its buildings and lecture theatres after a review of its eugenics history, and statistics curricula increasingly teach the eugenic origins of correlation and regression rather than hiding them.

**The word we can't take back.** Pearson's regret notwithstanding, "normal distribution" is permanent. Every statistics student still learns that one curve is normal and the rest, by quiet implication, are not — a four-letter value judgment baked into the most-used object in all of statistics.

## Where this surfaces in the vault

- [[Normal Distribution]] — the pedagogical home; the §"Why 'normal'?" section carries the load-bearing CLT answer (the curve is the universal limit of sums of independent influences). This Story carries the human drama and the honest edges.
- [[Why Probability and Statistics]] — the variance/least-squares history (Gauss) and the hunter's reflex of asking whether things are really independent; the regression-to-the-mean idea is a worked instance of that reflex.
- [[Stories/Lewis Carroll the Mathematician]] — the honest-edges peer card: a difficult Victorian biography handled by stating the facts, naming the modern unease, and declining both to whitewash and to over-pathologize. Same practice, different subject.
- [[Stories/Stigler's Law of Eponymy]] — the naming of this curve is a textbook eponymy tangle in its own right: De Moivre wrote it first (1733), Gauss's name ended up on it ("Gaussian"), and "normal" was coined three times independently before Pearson fixed it. A natural sibling to the eponymy cases that card collects.

## Receipts

- Abraham de Moivre, *Approximatio ad Summam Terminorum Binomii* (1733); the bell curve as a binomial approximation.
- C. F. Gauss, *Theoria Motus Corporum Coelestium* (1809) — least squares and the error law.
- Adolphe Quetelet, *Sur l'homme et le développement de ses facultés, ou Essai de physique sociale* (1835); the chest measurements of 5,738 Scottish soldiers and *l'homme moyen*.
- Francis Galton, *Hereditary Genius* (1869); *Inquiries into Human Faculty and Its Development* (1883), which coins "eugenics"; "Regression towards Mediocrity in Hereditary Stature," *Journal of the Anthropological Institute* (1886); *Natural Inheritance* (1889).
- On the naming: Charles S. Peirce (1873), Wilhelm Lexis, *Theorie der Massenerscheinungen* (1877), and Galton, "Typical Laws of Heredity" (1877), independently; Karl Pearson's 1890s usage fixed it, and his later remark on "abnormal" is widely quoted in histories of statistics.
- Stephen M. Stigler, *The History of Statistics: The Measurement of Uncertainty before 1900* (Harvard, 1986) — the standard scholarly account of Quetelet, Galton, and the naming.
- *Buck v. Bell*, 274 U.S. 200 (1927) — the U.S. Supreme Court sterilization decision; Holmes's "three generations of imbeciles are enough."
- Aubrey Clayton, *Bernoulli's Fallacy* (2021), and the *Nautilus* essay "How Eugenics Shaped Statistics" (2020) — on the eugenic origins of correlation and regression; UCL's 2020 denaming of the Galton and Pearson buildings.
