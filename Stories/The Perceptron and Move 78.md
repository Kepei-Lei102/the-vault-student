---
chinese: 感知机与第78手 (gǎnzhījī yǔ dì qīshíbā shǒu)
prerequisites:
  - "[[Artificial Intelligence]]"
  - "[[Graphs]]"
  - "[[You Never Expect the Change of Needs]]"
leads_to:
  - "[[Compression Is Intelligence]]"
  - "[[The Turing Test]]"
  - "[[You Are a Reinforcement Learner]]"
tags:
  - type/story
  - subject/cs
  - domain/artificial-intelligence
  - era/20c
  - era/21c
  - cast/rosenblatt
  - cast/minsky
  - cast/hinton
  - cast/lee-sedol
  - cast/hassabis
  - region/usa
  - region/korea
---

# The Perceptron and Move 78 感知机与第78手

> *"The Navy revealed the embryo of an electronic computer today that it expects will be able to walk, talk, see, write, reproduce itself and be conscious of its existence."*
> — *The New York Times*, 8 July 1958, on a machine that could not learn XOR.

> *"I thought AlphaGo was based on probability calculation and that it was merely a machine. But when I saw this move, I changed my mind. Surely, AlphaGo is creative."*
> — Lee Sedol, on move 37, game two, 10 March 2016.

> *"It was the only move."*
> — Lee Sedol, on his own move 78, game four, three days later.

## Cast of Characters

- **Frank Rosenblatt** (1928–1971) — Cornell psychologist; built the perceptron, the first machine that learned from examples, and let the Navy oversell it; drowned on his forty-third birthday.
- **Marvin Minsky** (1927–2016) and **Seymour Papert** (1928–2016) — MIT; their 1969 book *Perceptrons* proved what Rosenblatt's machine could not do, and helped bury his lineage for fifteen years.
- **Geoffrey Hinton** (b. 1947) — kept the neural lineage alive through both winters; back propagation in 1986 with Rumelhart and Williams; AlexNet in 2012 with his students Krizhevsky and Sutskever.
- **Sir James Lighthill** (1924–1998) — the fluid dynamicist whose 1973 report to the British government declared AI had delivered nothing it promised, and cut it off.
- **Rémi Coulom** (b. 1974) — whose 2006 Go program *Crazy Stone* introduced Monte Carlo tree search, the symbolic lineage's last great trick.
- **Demis Hassabis** (b. 1976) and **David Silver** (b. 1976) — DeepMind; AlphaGo, the marriage of the two lineages.
- **Lee Sedol** (b. 1983) — eighteen world titles; the man who played move 78.
- **Aja Huang** — the DeepMind engineer who placed AlphaGo's stones on the board.

---

## 中文锚点

人工智能的历史不是一架梯子，而是两条各自奔流了五十年的血脉。**符号派**写规则、搜空间：专家系统、下棋程序、蒙特卡洛树搜索。**统计派**从数据里学规则：1958 年罗森布拉特的感知机——海军的发布会上，《纽约时报》说它将会"走路、说话、看、写、自我复制并意识到自己的存在"——但它连异或（XOR）都学不会，1969 年明斯基和帕珀特用一本书证明了这一点，经费随之枯竭，罗森布拉特两年后在四十三岁生日那天溺水身亡。1973 年英国的莱特希尔报告让整个领域进入第一个"冬天"；八十年代专家系统的热潮和崩盘带来第二个。反向传播算法 1986 年被重新发现（真正的发明更早：林纳因马 1970 年，韦伯斯 1974 年），却又被支持向量机和随机森林压了十年，直到 2012 年 AlexNet 用两块游戏显卡把图像识别的错误率从 26% 打到 15%。2016 年，两条血脉结婚了：AlphaGo 用深度网络判断局面、用树搜索向前推演、用自我对弈的强化学习训练自己。第二局的第 37 手，是人类认为出现的概率只有万分之一的一手棋；第四局，李世石回敬了第 78 手——同样万分之一，机器随即崩溃，这是人类赢下的唯一一局。2017 年的 Transformer 只是一种新的网络结构，大语言模型是"深度学习 + 预测下一个词 + 人类反馈的强化学习"；2024 年的推理模型，又是 AlphaGo 的配方：一个评估器、一次搜索、一份可验证的奖励。这张卡讲的是两条血脉、两个冬天、一场婚礼，以及那一步棋。

---

## Act I — The press conference (1958)

![[perceptron-press-conference-comic.png|560]]

On 8 July 1958 the United States Navy held a press conference in Washington to show off a machine it had paid for, and let a thirty-year-old psychologist from Cornell describe it. Frank Rosenblatt's **perceptron** was, at that moment, a program on an IBM 704 that occupied a room; it took a grid of four hundred light-sensitive cells as an eye, multiplied each cell's reading by a weight, added them up, and said yes or no. What made it new was that nobody set the weights. Show it a triangle and say "triangle", show it a square and say "not triangle", and Rosenblatt's rule nudged every weight a little towards the right answer each time it was wrong. After enough examples it drew the line itself.

The *New York Times* went home and wrote that the Navy had revealed "the embryo of an electronic computer" that would "walk, talk, see, write, reproduce itself and be conscious of its existence". Rosenblatt was more careful in print than the reporters were, and less careful at the lectern than he should have been, and the sentence followed him for the rest of his life. [NYT 1958]

`perceptron-and-move-78.py` runs his rule. On AND it learns in six passes, on OR in four, and draws the line each time. On XOR, the function that says yes when exactly one input is on, it runs a thousand passes and learns nothing, because the two yes-cases sit on opposite corners of a square with the no-cases between them and no straight line separates them. Rosenblatt knew this. He also knew that a second layer of units would fix it, and he had no way to train a second layer, because his rule only knew how to correct the unit that gave the answer.

---

## Act II — The book, and the first winter (1969–1980)

Marvin Minsky had built a neural-network machine of his own in 1951 and moved on; by the 1960s he was the leader of the other lineage at MIT, the one that wrote the rules by hand and searched, and he had watched the perceptron money flow past him for a decade. In 1969 he and Seymour Papert published *Perceptrons: An Introduction to Computational Geometry*. It is a beautiful book of theorems about what a single-layer perceptron can and cannot compute, and XOR is its smallest example. It also carried, in its prose, the judgement that the multi-layer version was a "sterile" direction unlikely to lead anywhere, and the field read the judgement more carefully than the theorems. Funding for neural networks in the United States collapsed within three years. [Minsky & Papert 1969]

Rosenblatt did not live to argue. On 11 July 1971, his forty-third birthday, he drowned in a sailing accident on Chesapeake Bay. Minsky and Papert dedicated the 1988 edition of their book to him.

The other lineage got its own blow. In 1973 the British Science Research Council asked Sir James Lighthill, a fluid dynamicist with no stake in the field, to assess it. His report said that "in no part of the field have the discoveries made so far produced the major impact that was then promised", blamed the combinatorial explosion, and recommended that Britain stop paying for general AI. It did, and so, over the next few years, did most of the American agencies. Nobody called it a winter until it was over. [Lighthill 1973]

---

## Act III — The boom that was rules, and the second winter (1980–1993)

The symbolic lineage came back first, and it came back as a product. If a machine could not learn expertise, it could be *told* it: interview the expert, write the rules down, add an inference engine. DENDRAL had identified molecules this way since 1965; MYCIN diagnosed blood infections in 1972 and did it about as well as the specialists; and in 1980 Digital Equipment Corporation put **XCON** to work configuring its VAX computers, a rule base that grew to ten thousand rules and was said to save the company forty million dollars a year. Companies were founded to sell the machines the rules ran on, the Lisp machines, and Japan announced a Fifth Generation project to build them at national scale. [[Artificial Intelligence]] Part II is what they built; its honest edge, that a rule base cannot learn and must be maintained by hand, is what killed them. XCON's rules grew faster than anyone could keep them consistent; the Lisp-machine market vanished in 1987 when ordinary workstations became fast enough; the Fifth Generation project ended in 1992 having met none of its goals. Second winter.

Underneath, the statistical lineage was being quietly repaired. The trick Rosenblatt lacked, a way to train the *hidden* layer by passing the output's error backwards through the weights with the chain rule, had been written down by Seppo Linnainmaa in 1970 as a general method and by Paul Werbos in 1974 in exactly this setting, and nobody had noticed either. In 1986 David Rumelhart, Geoffrey Hinton and Ronald Williams published it in *Nature* under the name **back propagation**, showed multi-layer networks learning XOR and much more, and this time the field noticed. The script's second experiment is their result: three hidden units and back propagation, and XOR falls in a few thousand passes. [Rumelhart, Hinton & Williams 1986]

And then, having been repaired, neural networks lost anyway. They were slow, they needed more data than anyone had, and through the 1990s and 2000s cleaner statistical methods beat them on nearly every benchmark: Vapnik's support vector machines in 1995, Breiman's random forests in 2001. The "classical machine learning" that a textbook puts *before* neural networks in its chapter order actually came *after* the perceptron and defeated it. For twenty years, being a neural-network researcher was a mild professional embarrassment. Hinton kept at it in Toronto.

---

## Act IV — Dice, and two gaming cards (2006–2012)

Two things happened in the two lineages, six years apart, that nobody connected at the time.

In the symbolic lineage, the game of Go had defeated every rule-writer. Chess had fallen to Deep Blue in 1997 by brute search with a hand-written evaluation function; Go's board is larger, its games longer, and nobody could write down what a good position looked like. In 2006 Rémi Coulom's program *Crazy Stone*, and Levente Kocsis and Csaba Szepesvári's UCT algorithm, took a different route: **Monte Carlo tree search**. To judge a move, play the game out from it *at random*, thousands of times, and count how often you win; spend more play-outs on the moves that look good so far. No knowledge of Go is needed beyond the rules. The script's second half does it for noughts and crosses: with two thousand random play-outs per move, and no strategy programmed at all, it wins ninety-seven games in a hundred against a random opponent and loses none. Within a few years Monte Carlo programs reached strong amateur level at Go. They could not get further, because random play-outs are a poor judge of a subtle position. What they needed was a better judge. [Coulom 2006]

In the statistical lineage, the judge was being built for another purpose. Fei-Fei Li's ImageNet, fourteen million labelled photographs, had given the data problem an answer in 2009, and the annual contest to classify them had been won for three years by careful hand-designed features and support vector machines, at about twenty-six per cent error. In 2012 Hinton's students Alex Krizhevsky and Ilya Sutskever trained a deep convolutional network on the whole thing. It had sixty million weights and needed more arithmetic than any research machine could supply, so Krizhevsky trained it on two NVIDIA GTX 580 graphics cards in his bedroom, cards built to draw triangles for games, whose thousands of small cores turned out to be exactly what multiplying weight matrices needs. **AlexNet** scored fifteen per cent, and the field changed direction in a season. The chain from gaming cards to neural networks to the most valuable company on Earth is told in [[Stories/You Never Expect the Change of Needs]]; this story only needs the fact that the judge now existed. [Krizhevsky, Sutskever & Hinton 2012]

---

## Act V — The marriage (2016)

DeepMind's AlphaGo was the two lineages in one program, and its architecture is worth stating exactly, because the syllabus's four ideas are all in it. A **policy network**, deep, trained first by supervised learning on thirty million positions from expert games, suggested which moves were worth considering. A **value network**, deep, trained by reinforcement learning on games AlphaGo played against copies of itself, judged who was winning from any position: the judge the Monte Carlo programs had lacked. And **Monte Carlo tree search** used both, exploring the suggested moves and scoring them with the value network instead of random dice. Symbolic search, statistical judgement, reward as the training signal. [Silver et al. 2016]

In March 2016 it played Lee Sedol, holder of eighteen world titles, in Seoul, for a million dollars and, as it turned out, for the history of the game.

**Move 37.** In game two, AlphaGo played a shoulder hit on the fifth line, a move no professional would consider; the commentators assumed the operator had misplaced the stone. DeepMind later said its policy network had rated the move at one chance in ten thousand of being played by a human. Lee left the room for fifteen minutes. He lost the game, and afterwards said the sentence at the top of this card: he had thought the machine was calculating probabilities, and now he thought it was creative. The move is studied by professionals today; it was good. [Wikipedia, AlphaGo versus Lee Sedol]

**Move 78.** Three games down, in game four, Lee found the answer nobody had found: a wedge into the centre of the board that the network had rated at the same one in ten thousand, a move so unexpected that AlphaGo's evaluation, confident of victory a moment before, collapsed, and the program spent the next dozen moves playing nonsense, as a search does when its judge has been told something it cannot believe. Lee won. Asked about it, he said it was the only move he could see. It is the only game a human has won against a top program since, and Lee Sedol retired from professional Go in 2019, saying that with AI in the game, the top was no longer a place a human could hold.

![[move-78-comic.png|620]]

A year later **AlphaZero** dropped the thirty million human games. Given the rules alone, it learned Go, chess and shogi from self-play in days and beat every previous program, including AlphaGo. The supervised half of the marriage had been a scaffold; reinforcement and search were the building. [Silver et al. 2017]

---

## Act VI — Attention, and the recipe again (2017–2025)

What came next is often told as a new era, and it is better told as the same two lineages, still married.

In 2017 a paper from Google titled *Attention Is All You Need* proposed the **transformer**, a network whose layers let every word in a sentence attend to every other. It is an architecture: a better way to wire a deep network, trained by back propagation like every network since 1986. Trained to predict the next word over most of the written internet, transformers turned out to learn grammar, facts and something like reasoning as side effects of prediction, which [[Compression Is Intelligence]] argues is not an accident. Then, to make them useful rather than merely fluent, they were shaped by **reinforcement learning from human feedback**: people rank the model's answers, a reward model learns the ranking, and the language model is trained against it. Supervised learning, deep learning, reinforcement learning, in that order, on the largest data set there is. [Vaswani et al. 2017]

And in 2024 the reasoning models arrived, trained to think in steps before answering and to try many chains of thought and keep the ones that check out, with reinforcement learning on problems whose answers can be verified. Read the description again: a deep model as the judge, search over its own candidates at inference time, and a verifiable reward as the training signal. It is AlphaGo's recipe, played on language instead of Go.

![[perceptron-and-move-78-timeline.svg|900]]

---

## Honest edges

- **Rosenblatt did not say it.** The "walk, talk, see, write" sentence is the newspaper's, and the field paid for it as if it were his. His own book is careful about what the perceptron could not do. The hype cycle that followed, and the two winters, are a pattern, not a scandal: a promise made by a press office, a theorem that punctures it, funding that overreacts in both directions.
- **Minsky was right and wrong.** The theorems in *Perceptrons* are correct and still taught; the prose judgement that multi-layer networks were sterile was wrong, and it cost the field fifteen years. He was also, by every account, a generous and brilliant man whose own lineage produced most of what AI *was* until 2012.
- **Back propagation has four inventors.** Linnainmaa (1970) and Werbos (1974) had it first; Rumelhart, Hinton and Williams (1986) made it work and made it known. Credit went, as [[Stories/Stigler's Law of Eponymy]] predicts, to the people who made the field notice.
- **Move 78 was not magic.** Later analysis suggests it worked because AlphaGo's networks had a blind spot in that kind of position, and that a correct reply existed; the machine's collapse was the search trusting a judge who was briefly wrong. That does not make it less of a move.
- **The lineages are two, not ten.** Event-driven, functional, evolutionary and Bayesian approaches all have histories of their own; this card follows the two that married.

---

## Cultural ripples

- **"AI winter"** entered the language from these two collapses, and every funding cycle since has been read against them.
- **Move 37** became shorthand for a machine doing something creative that its makers did not put in, and **move 78** for the human answer; both phrases are used far outside Go.
- **The GPU** went from a gaming part to the most important computer chip in the world because of Act IV, which is why a generation of gamers accidentally funded the training of every model you have used.
- **Lee Sedol's retirement** is the first case of a world champion leaving a game because a machine had made the summit unreachable, and the Go world's response, studying the machine's moves as a new teacher, is the more interesting half of the story.

---

## Where this surfaces in the vault

- [[Artificial Intelligence]] — the mechanics: the perceptron that fails XOR, back propagation checked to the tenth decimal place, Q-learning, the expert system. This card is why those things exist in the order they do.
- [[Graphs]] — the tree search under AlphaGo, from BFS to A*.
- [[Compression Is Intelligence]] — why predicting the next word teaches a model more than the next word.
- [[You Are a Reinforcement Learner]] — the self-play loop, read as a life.
- [[The Turing Test]] — whether move 37 counts as thinking.
- [[Stories/You Never Expect the Change of Needs]] — the two gaming cards, and what they became.
- [[Stories/Stigler's Law of Eponymy]] — back propagation's four inventors.

---

## Receipts

- *The New York Times*, "New Navy Device Learns by Doing", 8 July 1958; F. Rosenblatt, *Principles of Neurodynamics* (1962).
- Cornell University Faculty Memorial Statement, Frank Rosenblatt, 1971 — the sailing accident on his forty-third birthday.
- M. Minsky and S. Papert, *Perceptrons* (1969; expanded edition 1988, dedicated to Rosenblatt).
- J. Lighthill, "Artificial Intelligence: A General Survey" (Science Research Council, 1973).
- S. Linnainmaa, master's thesis, University of Helsinki (1970); P. Werbos, PhD thesis, Harvard (1974); D. Rumelhart, G. Hinton and R. Williams, "Learning representations by back-propagating errors", *Nature* 323 (1986).
- R. Coulom, "Efficient selectivity and backup operators in Monte-Carlo tree search" (2006); L. Kocsis and C. Szepesvári, "Bandit based Monte-Carlo planning" (2006).
- A. Krizhevsky, I. Sutskever and G. Hinton, "ImageNet classification with deep convolutional neural networks", NIPS (2012).
- D. Silver et al., "Mastering the game of Go with deep neural networks and tree search", *Nature* 529 (2016); "Mastering the game of Go without human knowledge", *Nature* 550 (2017).
- A. Vaswani et al., "Attention is all you need", NeurIPS (2017).
- DeepMind and press coverage of the March 2016 match, including Lee Sedol's post-game remarks on moves 37 and 78.
- `perceptron-and-move-78.py`, `perceptron-and-move-78-timeline.py` — the perceptron and the tree search, run.
