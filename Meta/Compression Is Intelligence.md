---
chinese: 压缩即智能 (yāsuō jí zhìnéng) — 预测得越准，需要的比特越少
prerequisites:
  - "[[Information Theory]]"
  - "[[Compression]]"
  - "[[Forward Reading and Problem Discovery]]"
  - "[[The True IO Bound]]"
leads_to:
  - "[[The Feynman Technique]]"
  - "[[Chain of Thought]]"
tags:
  - subject/methodology
  - subject/philosophy
  - subject/computer-science
  - domain/cognition
  - domain/information-theory
  - domain/learning
  - level/life
  - type/methodology
  - type/meta
  - type/cross-domain
---

# Compression Is Intelligence 压缩即智能

> *To compress a thing you must predict it; to predict it you must understand it. Shannon proved the first half in 1948, a language model proved the second half by accident, and your own memory has been running the trick all along: you do not store the answer, you store the seed and grow it back.*

## What this card is for

[[Information Theory]] proves that a message costs as many bits as it is surprising, and [[Compression]] shows how a file is shrunk by charging less for what was expected. Put the two sentences together and something larger falls out: **a compressor is exactly as good as its predictor**, and a predictor is exactly as good as its model of the world. That equivalence is not a metaphor. It is an identity with a unit (bits per character), it can be measured on any text, and it has quietly become the most concrete definition of intelligence anyone has.

This card climbs it in five steps:

1. **Compression is prediction** — measured on this vault's own prose, from a letter-frequency table to a language model.
2. **Memory is a seed and a decompressor** — why the person who remembers the start and re-derives the rest beats the person who stored every bit.
3. **Perception is a predictive codec** — the brain transmits prediction *error*, exactly as a video coder does, and the science of what you cannot perceive is the most-replicated psychology there is.
4. **No free lunch** — no compressor shrinks everything and no intelligence solves everything; every predictor is a bet on the world it will meet.
5. **Encoding is search** — quality is bought with thinking time, once, so that decoding is cheap forever.

The card ends with what this makes the vault: a corpus compressed once, so that the predictive capacity of a teacher, a model or a student is spent on the student.

### 中文锚点

视频通话时，只要你猛地一挥手，画面就会糊成一团马赛克，半秒后才恢复——为什么平时那么清楚，一动就糊？因为视频编码器根本**不传画面，只传"变化"**：它先根据上一帧**预测**这一帧，然后只发送预测错的那部分。你坐着不动，每帧只有几个像素在变，几千比特就够；你一挥手，整块画面都"出乎意料"，要传的东西暴涨，带宽跟不上，就糊了。这就是这张卡的全部：**压缩就是预测，预测得越准，需要的比特越少**。这不是比喻，是一个有单位的等式——每个字符要几比特。这张卡用本知识库自己的英文文本测了一遍：什么都不知道的模型每个字母要 8 比特，记住字母频率要 4.6，记住前三个字母要 2.1，gzip 要 2.9，而一个大语言模型只要 0.66——它**预测**得最准，所以它**压缩**得最好，而要把维基百科预测准，你得懂维基百科在讲什么。把同一个道理倒过来用，就是你的**记忆**：好学生不背整套推导，只记开头，剩下的当场推出来——记忆是种子加一台"解压器"，而追溯因果的能力就是那台解压器。再倒一层，是你的**感觉**：大脑传的也是"预测误差"，所以 MP3 敢把人耳听不到的部分整个扔掉，魔术师敢把手法藏在你的预测里。最后是两条边界：**没有免费的午餐**——没有一种压缩能压小所有文件，也没有一种智能能解决所有问题，每个预测器都是在赌自己会遇到一个什么样的世界；以及**编码即搜索**——好的压缩靠慢慢想，想一次，所有人都能快速解开。这个知识库本身，就是把整门课先压缩好，让老师、模型和你的预测能力，都省下来花在你身上。

| English | 中文 | 一句话 |
|---|---|---|
| Compression = prediction | 压缩即预测 | 猜得准的符号几乎不花比特 |
| Bits per character | 每字符比特数 | 衡量一个模型懂不懂这段文本的尺子 |
| Seed + decompressor | 种子 + 解压器 | 记开头，推其余：记忆的真实结构 |
| Prediction error | 预测误差 | 编码器和大脑真正传输的东西 |
| Masking / just-noticeable difference | 掩蔽 / 最小可觉差 | 感官的分辨极限——MP3 和魔术都靠它 |
| No free lunch | 没有免费的午餐 | 没有通用的压缩，也没有通用的智能 |
| Encoding as search | 编码即搜索 | 想得越久压得越好；想一次，解无数次 |

---

## Part I — Compression is prediction

### The identity

[[Information Theory]] gives a symbol with probability $p$ a cost of $\log_2(1/p)$ bits. A perfect coder pays exactly that. So if you can predict the next character of a text with probability $p$, you pay $\log_2(1/p)$ for it — almost nothing if you were nearly sure, a lot if you were surprised. Sum over the text and you have its compressed size. **A compressor's output length is the sum of its surprises.** Improve the predictor and the file shrinks; there is no other way to shrink it.

This is why the field talks about "models". A compression program is a predictor plus an arithmetic coder that converts probabilities into bits; the coder is a solved problem, and every gain since the 1980s has come from the model. And it is why the identity runs backwards: **anything that compresses well predicts well, and anything that predicts well must contain a model of what it predicts.**

### Measured on this vault

The script beside this card takes a megabyte of the vault's own English and costs it with predictors of increasing memory: a model that knows only letter frequencies, then one that knows the previous character, the previous two, and so on. Beside them, what three standard compressors actually achieve on the same text, and two reference points.

![[compression-is-intelligence-ladder.svg|840]]

```
order-0 model (knows the previous 0 chars): 4.64 bits/char
order-1 model (knows the previous 1 chars): 3.69 bits/char
order-2 model (knows the previous 2 chars): 2.89 bits/char
order-3 model (knows the previous 3 chars): 2.14 bits/char
gzip -9   : 2.90 bits/char      bzip2 : 2.32 bits/char      xz : 2.43 bits/char
Shannon 1951, human guessers on English : about 1 bit/char
Chinchilla 70B on Wikipedia (2023)      : 0.66 bits/char
```

Read the ladder downward. Each rung is the same text, costed by a predictor that knows a little more about English. Letter frequencies alone save nearly half of the eight bits an ASCII character occupies. Knowing three previous characters — enough to guess that *th* is followed by *e*, that *q* is followed by *u* — brings it under 2.2. The general-purpose compressors sit around 2.5, because they must *learn* the model from the file as they go and pay for that learning. And at the bottom, two predictors that know English as a language rather than as a string: people, and a large language model.

### Shannon's parlour game, 1951

The first person to measure the bottom rung had no computer. Claude Shannon, three years after founding the subject, wanted the entropy of English itself — how unpredictable it *really* is to something that understands it — and reasoned that the best predictor of English available in 1951 was an English speaker. So he ran an experiment at home. His wife Betty was shown a passage of text one letter at a time and asked to guess the next letter; the count of guesses she needed was recorded. A letter she got first time cost almost nothing; a letter she needed eleven guesses for cost a lot. From the guess counts Shannon bounded the entropy of printed English at between 0.6 and 1.3 bits per letter — about **one bit**, against the 4.7 bits a letter-frequency table implies and the 8 bits a byte spends. The gap between 4.7 and 1 is the amount of English that lives *above* the letter: in words, grammar, and knowing what the sentence is about.

That number was a prediction about compression, and it took seventy years to cash. The Hutter Prize, founded in 2006 on the explicit thesis that compressing Wikipedia is an intelligence test, has driven the best entrants to under 0.9 bits per character on a gigabyte of it — Betty Shannon's territory, reached by programs that model text with neural networks. And in 2023 a group at DeepMind (Delétang and colleagues, *Language Modeling Is Compression*) simply used a large language model as the predictor inside an arithmetic coder, with no compression-specific engineering at all:

| Data | gzip | best classical | the language model (Chinchilla 70B) |
|---|---|---|---|
| Wikipedia text (enwik9) | 32.3 % of raw size | 23.0 % (xz) | **8.3 %** — 0.66 bits/char |
| ImageNet pictures | 70.7 % | 61.7 % (PNG) | **48.0 %** |
| LibriSpeech audio | 36.4 % | 43.0 % (FLAC) | **21.0 %** |

The model had been trained only on text. It compressed *pictures* better than PNG and *sound* better than FLAC, because whatever it had learned about predicting sequences was general enough to carry over. Nobody built it to be a compressor. It is one because it is a predictor, and the identity in the first section does not care what you meant to build.

> [!tip] The honest edge of Part I
> "Compression is intelligence" is a thesis, not a theorem. What is proven is that compression *equals prediction* and that prediction requires a model. Whether *understanding* is anything more than a very good model is exactly the open question, and the 2023 result sharpens it rather than settling it: a text-only model that compresses images has learned something general, but nobody can yet say what. Hold the identity firmly and the slogan loosely.

---

## Part II — Memory is a seed and a decompressor

Turn the identity on yourself. What does it cost to *remember* something?

A student who memorises a derivation as a sequence of lines is storing it uncompressed: every line a separate fact, every fact a separate cost, and nothing to fall back on when one line is lost — the whole chain breaks at the missing link. A student who remembers *where the derivation starts* and *how such derivations go* stores a seed and a decompressor: the first line, and a general method for growing the rest back on demand. The second student's storage is tiny and their recall is robust, because a forgotten line is regenerated rather than retrieved. Their memory is compressed, which is to say it is *predictive*: given what came before, they can say what comes next.

This is not a metaphor for good study habits; it is what memory is. [[The True IO Bound]] shows, through Bartlett and Loftus, that recall is a *reconstruction* run each time from fragments — the brain stores seeds and regenerates, whether you want it to or not. The choice is not between compressed and uncompressed memory but between a good decompressor and a bad one. And the decompressor has a name in this vault: [[Forward Reading and Problem Discovery]] calls it *tracing causality* — the habit of asking, at every line, what forces the next one. A hunter who can trace causality can regenerate a proof from its first move. A student who cannot has no decompressor, and must store everything, and it does not fit.

Three consequences for how to learn anything:

- **Store the starts, not the middles.** The first line of a derivation and the *reason* it is the first line are worth ten of its middle lines; the middle regenerates from the start if you have the method. [[Chain of Thought]]'s rule that a worked example names its *trigger* is this: the trigger is the seed.
- **Chunking is compression.** The chess masters of [[The True IO Bound]] hold whole positions in four slots because a "castled king's side" is one chunk regenerated from a name. Expertise is a better codec for the domain.
- **Understanding is the test of the decompressor.** [[The Feynman Technique]] asks you to rebuild an idea from scratch and teach it; that is a decompression test. What you cannot regenerate, you did not have — you had a stored copy, which is fragile and expensive and not knowledge.

---

## Part III — Perception is a predictive codec

### What a video coder sends

A video is thirty pictures a second, and almost all of each picture is the previous picture. So a video coder does not send pictures. It **predicts** each frame from the last (shifting blocks along their motion), sends only the **difference** between prediction and reality — the prediction error — and the decoder adds it to its own copy of the prediction. When nothing moves, the difference is nearly zero and the bitrate collapses; when everything changes at once, the difference is the whole frame and the bitrate explodes, which is why a video call turns to blocks the moment you wave.

![[compression-is-intelligence-frames.svg|620]]

*Two synthetic frames of a scene with one moving object, and their difference. Sent whole, each frame costs about 58 kilobits; the difference costs 3.5 — sixteen times less — because only 2.6 % of its pixels are anything but zero. Everything the coder transmits is surprise.*

### What a brain sends

The **predictive-processing** account of perception (Rao and Ballard 1999 for the visual cortex; Friston, Clark and others for the whole brain) says the cortex works the same way. Each level predicts the activity of the level below it and passes *upward* only the error — the part of the input the prediction did not account for. Perception is the settling of predictions until the error is small; attention is the raising of the gain on some errors; surprise, literally, is what you feel when a large error arrives. The experimental signatures are the ones a codec would show: neurons that fall silent when a stimulus becomes predictable, and fire when it deviates.

Whether the brain is *only* a predictive codec is contested. What is not contested is that it discards most of what reaches it, and that engineers have built an entire industry on knowing exactly what.

### The science of what you cannot notice

**Psychophysics** is the branch of psychology that measures perception with numbers, and it is two centuries old. Ernst Weber (1834) found that the smallest detectable change in a stimulus — the **just-noticeable difference** — is a fixed *fraction* of the stimulus: you can tell 100 g from 102 g and 1 kg from 1.02 kg, but not 1 kg from 1.002 kg. Gustav Fechner (1860) integrated that into a law: sensation grows as the *logarithm* of the stimulus, which is why sound is measured in decibels, why star magnitudes and earthquake scales are logarithmic, and why doubling the light in a room looks like one notch brighter. These are among the most replicated results in all of psychology, replicated in every hearing test and every display calibration ever done, and they are the compression-shaped answer to the tired question of whether psychology is a science: it is, wherever it measures what a perceiver *cannot distinguish*, because that is a quantity a codec can cash.

**MP3** is Weber and Fechner, engineered. A loud tone makes nearby quieter tones inaudible for a few milliseconds — **masking** — so a coder that models the ear's masking thresholds can throw away everything under them and lose nothing you can hear. Tuning those thresholds took years of listening. Karlheinz Brandenburg, leading the work at Fraunhofer in Erlangen around 1990, tested every version against Suzanne Vega's a cappella *Tom's Diner*, a bare voice with nowhere for artefacts to hide, until the codec passed it; he is said to have heard the song thousands of times, and Vega has been called the mother of MP3.

![[compression-is-intelligence-mp3-comic.png|760]]

*Erlangen, about 1990. The tally sheet is the number of times he has listened to the same three minutes. The masking curve is on the whiteboard; the ear is the codec's specification, and the song is the unit test.*

The same knowledge in other hands is called something else. A magician's **misdirection** is a masking threshold applied to attention: a large motion masks a small one, a question masks a move, and the spectator's predictive codec fills in a frame that was never there. Codec engineers and conjurers are in the same trade — both have measured, precisely, what the perceiver will discard, and both build their work in the gap.

---

## Part IV — No free lunch: every predictor is a bet

### The pigeonhole, and its twin

[[Compression]] proves, by counting, that no lossless scheme shrinks every file: there are $2^n$ files of $n$ bits and only $2^n - 1$ shorter ones to map them to, so any scheme that shrinks some files must *lengthen* others.

![[compression-is-intelligence-pigeonhole.svg|880]]

Run the identity across it and the theorem grows a twin. A compressor shrinks the files it predicts well and lengthens the rest; a predictor is right about the world it modelled and wrong about the others. So **no predictor is good everywhere** — Wolpert and Macready proved the formal version for learning algorithms in 1997 and called it the *no free lunch* theorem — and therefore no intelligence solves everything. Every intelligence, natural or built, is a **bet on which world it will meet**: a bundle of expectations that pay off in the environments that produced them and cost in the ones that did not. Human vision is a superb codec for a savannah and a poor one for a magic show. A language model is a superb predictor of text written by people and a mediocre predictor of a random number table, which is exactly as it should be.

This is why instruction sets keep growing. Every opcode a chip adds — a fused multiply-add, a vector permute, an AES round in silicon — is a bet that a particular pattern of work is common enough to deserve its own short code, and the bet keeps being placed decade after decade because the world the chip meets keeps changing. A compressor's dictionary, a brain's shortcuts, a CPU's instructions and a curriculum's chapters are all the same object: a list of what the designer expected, made cheap.

### What this makes the vault

State the identity's consequence for teaching plainly. Every explanation costs the explainer prediction: the teacher predicts what the student knows and does not, the good textbook predicts what the reader will misunderstand, the tutor model predicts the next thing to say. That capacity is finite, and it is spent every time the content is re-derived from scratch for a new listener. So the vault is a *compression* of the courses it covers — every derivation done once, every misconception pinned once, every worked example with its trigger named — so that the predictive capacity of teacher, model and student is spent not on regenerating the content but **on the student**: on what this reader, today, is about to get wrong. The corpus is externalised losslessly so that intelligence can be spent where it is scarce. And because no compressor shrinks everything, the vault is an infinite game: every new student is a file it has not yet met.

---

## Part V — Encoding is search

The identity has one more consequence, and it is the practical one. If compression is prediction, then *better* compression is *harder* prediction, and prediction is search: the encoder tries many descriptions and keeps the shortest. That is why compression is **asymmetric**. Encoding a video with x265 at its slowest setting takes many times longer than at its fastest and produces a smaller, better file, because the slow setting searches more of the space of possible predictions; a hardware encoder in a graphics card is fast because it searches almost nothing. But *decoding* costs the same either way. The search is done once; the result is used forever.

- **Think hard once, decode everywhere.** John Napier spent twenty years computing his logarithm tables so that every navigator afterwards could multiply by adding. A chess engine's opening book is search precomputed. A theorem is a proof compressed to its statement, decoded by anyone who trusts it.
- **Reasoning is encoding.** A model that "thinks" before answering is running search at encoding time: trying continuations and keeping the one under which the answer is least surprising. The tokens it spends are the slow-preset cost, paid so that the answer decodes cleanly.
- **Learning is the slow preset.** The hours spent understanding a derivation once, so that it regenerates from its seed for the rest of your life, are the encoder's search. The student who skips them gets the fast preset: a big, fragile file.

---

## How to use this card

1. **Measure your understanding in bits.** If you can predict the next line of a derivation, you have compressed it; if you must look, you are storing it. Read a proof with the next line covered, and guess.
2. **Store seeds.** For every technique, know the first move and the reason it is first. Let the middle regenerate.
3. **Run the decompression test.** Rebuild the idea from the seed on blank paper ([[The Feynman Technique]]). Where regeneration fails, that is where the model is missing, and no amount of re-reading stores it.
4. **Know what you are betting on.** Every method you learn is a predictor tuned to a family of problems; when it fails, ask which world it was built for, not whether you applied it correctly.
5. **Spend search where it pays.** Think slowly once, on the things you will decode many times; do not re-derive what should have been compressed.

---

## Misconceptions

1. **"Compression is a clever trick for saving disk space."** It is prediction with a unit. The trick is the arithmetic coder, which was solved decades ago; everything since is modelling, and the size of the file is a measurement of how well the world was modelled.
2. **"A language model compresses text because it was built to."** It was built to predict the next token. It compresses because prediction and compression are the same operation; it compresses images and sound it never trained on for the same reason.
3. **"Good memory means storing more."** Good memory means a better decompressor. The person who can regenerate a page from its first line remembers more than the person who stored the page.
4. **"Lossy compression cheats."** It models the receiver. MP3 and JPEG discard what a measured human ear or eye cannot distinguish — the loss is real and the science of where to put it is two centuries old.
5. **"A general intelligence would be right about everything."** No predictor is; the pigeonhole forbids it and the no-free-lunch theorem formalises it. Generality is a wider bet, not the absence of one.
6. **"Compression is understanding."** It is prediction, provably; whether prediction exhausts understanding is the open question, and the card's title is a thesis to be argued with, not a result.

---

## Connections

- **Parents:**
   - [[Information Theory]] — $\log_2(1/p)$ bits per symbol, the source-coding theorem; this card is that theorem read as a claim about minds.
   - [[Compression]] — RLE, Huffman, lossy coding, the pigeonhole proof, and the "compression is prediction" section this card grows from.
   - [[Forward Reading and Problem Discovery]] — tracing causality is the decompressor of Part II.
   - [[The True IO Bound]] — the sibling: that card is about what the filter *drops*, this one about how the codec *predicts*; reconstructive memory, chunking and the four-slot cache are shared ground.

- **Children:**
   - [[The Feynman Technique]] — the decompression test as the definition of understanding.
   - [[Chain of Thought]] — naming the trigger is storing the seed.

- **Cross-domain:** [[Hash Tables]] and [[Graphs]] — nothing directly, except that the compression distance in the script clusters this vault's cards by subject with no notion of subject in the code; [[Sensors and Control Systems]] — prediction error as the signal in a control loop; [[Fun Is the Brachistochrone]] — the slow preset that makes every later metre cheaper is the cycloid's early plunge; [[Credit Is the Currency]] — a theorem as a proof compressed to a promise.

- **Misconception traps cleared:** compression is a disk-space trick; the model compresses because it was told to; good memory is more storage; lossy compression cheats; general intelligence is right everywhere; compression is understanding.

## Sources

- C. E. Shannon, *A Mathematical Theory of Communication* (1948); *Prediction and Entropy of Printed English*, Bell System Technical Journal 30 (1951) — the guessing experiment and the 0.6–1.3 bits/letter bounds.
- G. Delétang et al., *Language Modeling Is Compression*, arXiv 2309.10668 (2023; ICLR 2024) — the Chinchilla compression table. M. Hutter, the Hutter Prize (2006–), and M. Mahoney, *Data Compression Explained* (2010–13), for the compression-as-intelligence thesis; S. Legg and M. Hutter, *Universal Intelligence* (2007).
- R. P. N. Rao and D. H. Ballard, *Predictive coding in the visual cortex*, Nature Neuroscience 1999. A. Clark, *Whatever next? Predictive brains, situated agents, and the future of cognitive science*, Behavioral and Brain Sciences 2013. K. Friston, *The free-energy principle*, Nature Reviews Neuroscience 2010.
- E. H. Weber, *De Tactu* (1834); G. T. Fechner, *Elemente der Psychophysik* (1860). K. Brandenburg, *MP3 and AAC explained*, AES 17th International Conference (1999); the *Tom's Diner* account is Brandenburg's own, widely reported (e.g. *Business 2.0*, 2000).
- D. H. Wolpert and W. G. Macready, *No Free Lunch Theorems for Optimization*, IEEE Trans. Evolutionary Computation 1997. R. Cilibrasi and P. Vitányi, *Clustering by compression*, IEEE Trans. Information Theory 2005 — the normalised compression distance in the script.
- The entropy ladder and the compression-distance table were computed on 2026-09-09 by `compression-is-intelligence-entropy.py` on a megabyte of this vault's English (105 cards); the frame figure by `compression-is-intelligence-frames.py`.
