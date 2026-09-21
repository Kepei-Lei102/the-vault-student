---
chinese: 抱歉，作业交晚了 (bàoqiàn, zuòyè jiāo wǎn le)
prerequisites:
  - "[[Hypothesis Tests]]"
  - "[[Graphical Inequalities (Vocab)]]"
leads_to: []
tags:
  - type/story
  - subject/mathematics
  - subject/computer-science
  - domain/history-of-science
  - domain/statistics
  - domain/optimisation
  - era/20c
  - cast/dantzig
  - cast/tobias-dantzig
  - cast/neyman
  - cast/von-neumann
  - cast/koopmans
  - cast/kantorovich
  - region/north-america
---

# Sorry the Homework Is Late 抱歉，作业交晚了

> *"A few days later I apologized to Neyman for taking so long to do the homework — the problems seemed to be a little harder to do than usual."* — George Dantzig, recalling 1939

## Cast of Characters

- **George Bernard Dantzig** (1914–2005) — named after a playwright by a father who hoped for a writer. Failing algebra in the ninth grade.
- **Tobias Dantzig** — his father. Attended Poincaré's lectures in Paris, then felled trees in Oregon; later a professor, and the author of *Number: The Language of Science*.
- **Anne Dantzig** — married George in 1936 and was in the room for most of this.
- **Jerzy Neyman** — the leading mathematical statistician of his day, newly arrived at Berkeley. He wrote things on blackboards.
- **John von Neumann** — considered by many the best mathematician alive. Short of time.
- **Tjalling Koopmans** and **Leonid Kantorovich** — two economists who went to Stockholm in 1975.
- **Nine clerks with desk calculators** — the first computer ever to run the simplex method.

## 中文锚点

你上课迟到了，黑板上写着两道题，你以为是作业，抄下来带回家。题有点难，你多花了几天，交的时候还向老师道了歉。几个星期以后你才知道，那两道根本不是作业，而是老师举的例子：整个领域里还没有人解出来的题。要是一开始就有人告诉你“这两道题没人解得出”，你很可能连试都不会试；不是因为你不够聪明，而是因为“没人做得出”这几个字，会让人还没动笔，就先把自己劝退了。可故事讲到这儿还不算完。他之所以做得出来，是因为此前他已经做过上万道几何题，功夫早就在手上了；不知道题目的来头，只是让这份功夫没有被吓回去。

## Act I — Ten thousand problems

Tobias Dantzig came to America twice. The first time he worked as a pedlar for an aunt in South Carolina, decided there was no future in it, and went back to Paris, where he met Anja Ourisson, a Polish student of mathematics at the Sorbonne. The second time they came together, to Oregon, and the man who had sat in Poincaré's lecture hall earned his living as a lumberjack, then on a road gang, then painting houses. On his son's birth certificate, in 1914, his occupation is "painter". He believed his Russian accent shut him out of any university. One day in a public library he fell into conversation with the head of mathematics at Reed College, who told him he was crazy, and that with his credentials any university would have him. Indiana did.

He named his first son George Bernard, after Shaw, hoping for a writer. He named his second Henri Poincaré Dantzig. The family was poor for decades. In 1919 the children wore second-hand shoes. In second grade George won a long-division contest whose prize was the class photograph, which was on sale to everyone else. Winning was the only way the family could have had it.

The boy hoped for by a mathematician, named for a playwright, reached the ninth grade and found himself failing algebra.

> "I remember walking home one day, furious with myself. How is it, I asked myself, that I, a son of a mathematician, do poorly while all the other kids in the class do so much better?"

After that, he said, he sailed through. Then geometry "really turned me on", and he began asking his father for problems. Tobias would hand one over. George would come back with a solution. Tobias would hand over another. At first he checked the answers; after a while he simply took them as correct and reached for the next.

> "I would say over ten thousand... It was I who asked for the problems. I believe he gave them to me just to get rid of me."

Eventually the supply ran out, and Tobias had to go to the Library of Congress to dig up more. George's own verdict, fifty years on: solving thousands of problems while his brain was still growing "did more than anything else to develop my analytic power", and problems in any other subject would probably have done as well.

## Act II — Two problems on a blackboard

He took his degree at Maryland, because his father taught there and nobody had money for anywhere else. He tried graduate school at Michigan, found the statistics "just a bag of tricks" and everything else so abstract that he had "but one desire: to quit", and did. In 1937, still the Depression, he landed a job as a clerk at the Bureau of Labor Statistics. The desk had just been vacated by a young man called Milton Friedman.

There he was handed a paper by Jerzy Neyman to review, and met for the first time statistics built on reasons. Neyman and Egon Pearson had turned the hypothesis test into a precise bargain between two kinds of error, the machinery of [[Hypothesis Tests]], over the furious objections of R. A. Fisher; [[The Lady Tasting Tea]] has that quarrel. Dantzig wrote to Neyman, who had just moved to Berkeley, and asked to finish a doctorate under him.

In his first year there, 1939, he arrived late to one of Neyman's classes. Two problems were on the board. He assumed they were homework and copied them down.

> "A few days later I apologized to Neyman for taking so long to do the homework — the problems seemed to be a little harder to do than usual. I asked him if he still wanted it. He told me to throw it on his desk. I did so reluctantly because his desk was covered with such a heap of papers that I feared my homework would be lost there forever."

Six weeks passed.

![[homework-late-sunday-door-comic.png|620]]

> "One Sunday morning about eight o'clock, Anne and I were awakened by someone banging on our front door. It was Neyman. He rushed in with papers in hand, all excited: 'I've just written an introduction to one of your papers. Read it so I can send it out right away for publication.' For a minute I had no idea what he was talking about."

The two problems had not been homework. Neyman had written them up as examples of famous *unsolved* problems in statistics.

**What they were.** The first concerns the test in [[t-Tests]]. When you test a claim about a mean without knowing the population's spread $\sigma$, your chance of noticing a real difference depends on $\sigma$: the noisier the population, the harder any effect is to see. Statisticians had hoped for a cleverer test whose power did not depend on the unknown $\sigma$. Dantzig proved that none exists. It appeared in 1940 under his name alone. The second extended Neyman and Pearson's fundamental lemma, the theorem that says which test is *best*, to the case where the best test must satisfy several conditions at once.

A year later he went to Neyman worried about a thesis topic. Neyman shrugged, and told him to put the two problems in a binder.

The second one had an afterlife. Around 1950 Abraham Wald, one of the great statisticians of the century, posted Dantzig the final proofs of a paper about to go to press. Someone had just pointed out to Wald that his main result was Dantzig's second homework problem. Dantzig suggested they publish together. Wald "simply inserted my name as coauthor into the galley proof."

## Act III — Seventy men, seventy jobs

Dantzig did not finish the doctorate then. In June 1941, six months before Pearl Harbor, he went to Washington and was hired on a street corner to help count the Air Force's aeroplanes, which at that moment numbered fewer than a hundred and which nobody had accurately counted. He spent the war building the reporting system for sorties, losses and bombs, and became expert at what the Air Force called *programming*: working out schedules of training, supply and deployment. The computers were people with hand-cranked desk calculators. (That is the "programming" in **linear programming**. It has nothing to do with code, and it is why the word is there.)

In 1946 he went back to Berkeley, defended the thesis, turned down Berkeley's job offer "because it paid too little", and returned to the Pentagon. Two colleagues, hoping to keep him, set him a challenge: mechanise the planning.

He explained the difficulty with an example every student can check. Assign 70 men to 70 jobs, one each, as well as possible. There are only 140 rules to obey. But the number of possible assignments is
$$70! \approx 1.2 \times 10^{100}.$$
A machine checking a billion assignments a second since the Big Bang would by now have examined about $4 \times 10^{26}$ of them, which is nothing. So nobody examined them. Planning ran instead on what Dantzig called ground rules, handed down by someone senior.

> "Those in charge often do a hand-wave and say, 'I've considered all the alternatives,' but this is so much garbage. They couldn't possibly look at all possible combinations."

His first step was one that sounds like nothing: he insisted that the plan have an **objective**, a single quantity to be made as large or as small as possible, with all the ground rules rewritten as linear inequalities. That turns planning into geometry. You have met it in two dimensions as [[Graphical Inequalities (Vocab)]]: each inequality removes half the plane, what survives is a polygon, and the best point is always at a corner.

Try one. Maximise $3x + 2y$ subject to $x + y \le 4$, $\;x + 3y \le 6$, $\;x \le 3$ and $x, y \ge 0$. The corners of the region are $(0,0)$, $(3,0)$, $(3,1)$ and $(0,2)$, where $3x + 2y$ is $0$, $9$, $11$ and $4$. The best is $(3, 1)$.

With thousands of variables there is no picture, and the corners are as numerous "as the stars in the heavens". In the summer of 1947 Dantzig wrote down the obvious method: start at any corner, step along an edge to a neighbouring corner that is better, and stop when no neighbour is. In the example that is $(0,0) \to (3,0) \to (3,1)$, and stop. **He rejected it at once**, as any mathematician would. It would surely wander for ever.

What changed his mind was his homework. His thesis on the Neyman–Pearson lemma had made him look at such problems through the geometry of the *columns* of the table instead of its rows, and in that picture the same edge-walking looked quick. He tried to invent a problem with $m$ equations that it could not finish in about $m$ steps, and found it "extremely difficult". The second blackboard problem, it turned out, had been a linear programme in disguise, with infinitely many variables. He had been practising for eight years on something he had taken for an exercise.

He still did not believe it. He handed the method to his staff and went on looking for a better one.

## Act IV — "Oh, that"

On 3 October 1947 he took the problem to John von Neumann in Princeton, and began explaining it "as I would describe it to an ordinary mortal".

> "'Get to the point,' he snapped. I said to myself, 'Okay, if this man wants a quickie, then that's what he'll get.' In less than a minute I slapped the geometric and the algebraic versions of my problem on the blackboard. He stood up and said, 'Oh, that.'"

Von Neumann then lectured for an hour and a half on the mathematical theory of linear programmes, a subject on which Dantzig had searched the literature and found nothing. Seeing his visitor "with my eyes popping and my mouth open", von Neumann explained that he was not a magician: he had just finished a book on the theory of games, and was guessing that the two problems were the same problem. They were. That day Dantzig learned duality. Every linear programme has a twin, and solving either solves both.

He wrote up his own proof for his office and never published it. Asked years later why not: "Because it was not my result — it was von Neumann's."

Meanwhile the method needed a test. The economist George Stigler had posed a puzzle in 1945: from 77 foods, find the cheapest diet that meets nine nutritional requirements for a year. Stigler had found by ingenuity and trial a diet costing \$39.93 a year at 1939 prices, and remarked that there seemed to be no direct way to find the true minimum. In the autumn of 1947 Jack Laderman at the National Bureau of Standards gave the problem to **nine clerks with desk calculators**. They ran the simplex method by hand for about 120 person-days.

![[homework-late-clerks-diet-comic.png|620]]

The answer was \$39.69. Stigler had been 24 cents out. The optimal diet was wheat flour, cabbage, spinach, dried navy beans and a little beef liver, every day, for a year. The mathematics was flawless. Nobody had told it that people need to want to eat.

By June 1948 his staff asked him why he was still searching for a better algorithm when this one kept solving problems with $m$ equations in $2m$ or $3m$ steps.

> "In brief, one's intuition in higher dimensional space is not worth a damn!"

## Act V — The sermon

The simplex method went on to schedule airlines, blend petrol, route freight, plan diets for cattle who do not complain, and sit inside almost every piece of optimisation software written since. In 2000 the journal *Computing in Science & Engineering* named it one of the ten algorithms of the century.

The homework story had its own career. On an aeroplane Dantzig sat next to the Reverend Robert Schuller, who was writing a book on positive thinking, and told him about the blackboard. In Schuller's printed version the homework had become a final examination with ten questions, the two extra problems were ones "even Einstein" could not solve, and the grateful professor gave Dantzig a job. Dantzig called it "a bit garbled and exaggerated but essentially correct". Years later his Stanford colleague Donald Knuth pulled up beside him on a bicycle: "Hey, George — I was visiting in Indiana recently and heard a sermon about you in church." The scene eventually reached cinema as the opening of *Good Will Hunting*, with a janitor and a corridor blackboard.

The sermon's moral was that if he had known the problems were famous, he would have been discouraged and never solved them. Dantzig repeated the moral to his interviewers without quarrelling with it.

But look at what the sermon leaves out. It leaves out the ten thousand geometry problems, the two years as a clerk learning what real data looks like, and a teacher good enough to write open problems on the board. Not knowing the problems were hard did not solve them. It removed one obstacle, the one that stops people before they start, from the path of someone who was otherwise ready. Most people who arrive late and copy down an unsolved problem hand in nothing at all.

And notice his own account of the timing: "there was no particular deadline, and you know how graduate students take their time." It was not done overnight.

## Honest edges

- **The Nobel Prize.** In 1975 the prize in economics went to Koopmans and Kantorovich "for their contributions to the theory of optimum allocation of resources", which is linear programming. Dantzig was not included. Koopmans, who had seen the significance of Dantzig's model "in a lightning flash" in June 1947, said he regretted the omission. Dantzig received the National Medal of Science that year instead.
- **Kantorovich was first.** In Leningrad in 1939, the very year of the blackboard, Leonid Kantorovich formulated linear programmes for a plywood trust and gave a method for solving them. His work was ignored at home, where prices computed by mathematics were ideologically unwelcome, and was unknown in the West until the late 1950s. Dantzig's contribution was independent, general, and came with an algorithm that machines could run, but "the father of linear programming" is a title with an asterisk.
- **The method can be beaten.** In 1972 Klee and Minty built a distorted cube on which the simplex method visits every one of the $2^n$ corners. So Dantzig's first instinct was right in the worst case and wrong in practice, and why it is wrong in practice took until the 2000s to explain. Methods that are guaranteed fast arrived in 1979 and 1984. The simplex method is still in daily use beside them.
- **It is a recollection.** The blackboard story rests on Dantzig's own telling, decades later. The papers are real and dated: the first appeared in the *Annals of Mathematical Statistics* in 1940, the second with Wald in 1951, and the thesis is titled after the two problems. The dialogue on the doorstep is as he remembered it.

## Connections

- The statistics of the two problems: [[Hypothesis Tests]], [[t-Tests]]; the quarrel Neyman was in the middle of: [[The Lady Tasting Tea]].
- Linear programming in two dimensions: [[Graphical Inequalities (Vocab)]]. The general idea of a best point under constraints: [[Optimisation]]. Why $70!$ is hopeless and $3m$ steps is not: [[Big-O Notation]].
- The man who said "Oh, that": [[Von Neumann machine]].
- Why practice, not confidence, was the cause: [[Learning with the Whole Body]], [[You Are a Reinforcement Learner]]. Why the sermon version spread and the true one did not: [[Humans Are Story Animals]].

## Receipts

1. D. J. Albers & C. Reid, "An Interview with George B. Dantzig: The Father of Linear Programming", *The College Mathematics Journal* 17(4), 1986, pp. 292–314. Every quotation above is from this interview, which was recorded in November 1984.
2. G. B. Dantzig, "On the Non-Existence of Tests of 'Student's' Hypothesis Having Power Functions Independent of σ", *Annals of Mathematical Statistics* 11(2), 1940, pp. 186–192.
3. G. B. Dantzig & A. Wald, "On the Fundamental Lemma of Neyman and Pearson", *Annals of Mathematical Statistics* 22(1), 1951, pp. 87–93.
4. R. W. Cottle, "George B. Dantzig: a legendary life in mathematical programming", *Mathematical Programming* 105, 2006; and R. W. Cottle (ed.), *The Basic George B. Dantzig*, 2003, for the thesis geometry and its role in the simplex method.
5. G. J. Stigler, "The Cost of Subsistence", *Journal of Farm Economics* 27(2), 1945; G. B. Dantzig, "The Diet Problem", *Interfaces* 20(4), 1990, for Laderman's nine clerks.
6. V. Klee & G. J. Minty, "How good is the simplex algorithm?", in *Inequalities III*, 1972.
7. The fact-checking site Snopes, "The Unsolvable Math Problem", for Schuller's printed version and its additions.
