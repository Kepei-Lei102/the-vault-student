---
chinese: 图灵测试 (Túlíng cèshì)
prerequisites:
  - "[[Turing Machine]]"
leads_to: []
tags:
  - subject/computer-science
  - subject/philosophy
  - domain/artificial-intelligence
  - domain/philosophy-of-mind
  - domain/theory-of-computation
  - level/A-Level
  - level/university
  - type/deep
  - type/cross-domain
  - misconception/turing-test-measures-intelligence
  - misconception/passing-means-conscious
  - misconception/turing-test-is-a-formal-benchmark
---

# The Turing Test 图灵测试

> *In 1950, the same man who had defined what a machine can **compute** asked what a machine can **be**. He refused to argue about whether machines can "think" — he thought the word too vague to settle — and proposed a game instead: if, in plain conversation, you cannot tell the machine from a person, on what honest grounds do you still deny it a mind? Seventy-five years later a machine helped write this card, and you might not have known.*

## The question Turing refused to answer

Turing's 1950 paper *Computing Machinery and Intelligence* opens with seven of the boldest words in science: **"Can machines think?"** — and then immediately throws the question away. The words *machine* and *think*, he argues, are so loosely used that settling the question honestly would mean taking *"a statistical survey such as a Gallup poll,"* which is absurd. A question you can only answer by opinion poll is not yet a scientific question.

So Turing does something characteristic: he **replaces an unanswerable question with an answerable one.** Instead of "can it think?" — a claim about the machine's hidden inner life that no experiment can reach — he asks a question about *behaviour you can actually observe*: can it **hold its own in a conversation well enough to be mistaken for a human?** This is the move of an **operationalist**: define a concept by the test you would run, not by the essence you imagine behind it. The same instinct that turned "computation" into a tape, a head, and a rule-book in [[Turing Machine]] now turns "thinking" into a game anyone can score.

## The Imitation Game — the test itself

Turing builds the test out of a party game. In the **original imitation game**, an interrogator **C** sits in one room and exchanges typed notes with two hidden people: a man **A** and a woman **B**. C's job is to work out which is which; A *tries to deceive* C, B *tries to help*. Then Turing springs the substitution that founded a field:

> *"What will happen when a machine takes the part of A in this game? Will the interrogator decide wrongly as often as when the game is played between a man and a woman?"*

That is the **Turing Test**: put a machine and a human behind the curtain, let an interrogator interrogate both by text alone, and see whether the machine can be told apart. Everything that could leak a non-conversational clue is stripped away — **no voice, no face, no body** — so that nothing is judged except the quality of the *responses themselves*. The modern, simplified form drops the gender frame: one judge, one human, one machine, text only; the machine **passes** if the judge does no better than chance at fingering it.

![[turing-test-imitation-game.svg|620]]
*The setup, stripped to its logic: a judge trades text with two hidden players — one human, one machine — and tries to name the machine. Only words cross the curtain; voice, face and body are deliberately removed, so the only thing on trial is the conversation. The machine wins by being indistinguishable.*

The gendered original is not a historical curiosity — it carries the whole point. The game was never "ask it directly whether it is a computer." It was always about **imitation**, about *performing* a kind of mind convincingly, the way A must perform being a woman. Turing's bet is that performance, sustained under any line of questioning the judge can invent, is all the evidence of mind we ever actually have about *each other*.

## 中文锚点

**图灵测试**是图灵 1950 年论文《计算机器与智能》提出的判定标准。他认为「机器能思考吗」这个问题太含糊、无法用实验回答，于是换成一个**能观测**的问题：让一位**裁判 C** 只通过**打字**（不看脸、不听声音）分别与两位隐藏者对话——一个是**人**，一个是**机器**——裁判要分辨哪个是机器。如果裁判的判断**不比瞎猜更准**，机器就**通过了测试**。

关键在于：图灵把「思考」从一个关于**内在本质**的问题，换成了一个关于**外在行为**的问题（这叫**操作主义**）。深层主张是——我们判断**别人**是否有思想，靠的也只是对方的言行，从来没有别的证据。反对意见里最有名的是塞尔的**中文房间**（见下）：它指出「能对话」未必等于「真的懂」——语法（符号操作）不等于语义（理解）。现代大语言模型（LLM）在受控实验里已能让多数裁判分辨不出，所以**就图灵的标准而言，测试已被通过**;但这究竟证明了什么，仍是开放问题。

## What Turing was really doing — the burden-of-proof flip

The test's genius is not the game; it is what the game does to the **argument**. Before Turing, "of course a machine can't really think" was the default, and the burden lay on anyone claiming otherwise. The imitation game flips that burden. Once a machine is *behaviourally indistinguishable* from a person across open-ended conversation, the sceptic who still wants to deny it a mind must **name the missing ingredient** — and say why that ingredient matters when we never check for it in each other.

Every answer to "what's missing?" turns out to be uncomfortable:

- *"It's only manipulating symbols, not understanding."* — and your neurons are only passing ions; why does one count and the other not?
- *"It has no inner experience."* — how do you know **I** do? You infer my mind from my behaviour, which is exactly what the test measures.

This is the famous slide toward **solipsism** that Turing presses: the only way to be *certain* something thinks is to *be* it. Since we don't demand that certainty of other people — we extend the courtesy of "mind" on the strength of behaviour alone — Turing argues it is mere prejudice to withhold it from a machine that behaves the same way. You don't have to agree. But you can no longer answer "can it think?" with a shrug; the test makes you *show your reason*.

## Turing's predictions, and how they aged

Turing put numbers on the table. He predicted that by **the year 2000**, a computer with about **$10^9$ bits** of memory (~125 MB — laughably modest now) could be programmed so that an average interrogator would have **no more than a 70% chance** of correctly identifying the machine after **five minutes** of questioning. He went further, predicting that by century's end *"the use of words and general educated opinion will have altered so much that one will be able to speak of machines thinking without expecting to be contradicted."*

The memory prediction was met with room to spare; the five-minute, 70% bar took longer than he thought but has now fallen (see the modern verdict below). The *cultural* prediction is the one that aged most interestingly: we **do** now speak casually of what a chatbot "thinks" or "knows" or "wants" — Turing's looser, social sense of the word arrived almost exactly on schedule, even as the philosophers kept arguing about the strict sense.

## The nine objections Turing already answered

The deepest part of the 1950 paper is that Turing wrote down, and rebutted, **nine objections** to the idea of a thinking machine — most of which are still the objections people raise today, 75 years early:

| # | Objection | Turing's reply (in brief) |
|---|-----------|----------------------------|
| 1 | **Theological** — thinking needs a soul, given only to humans | Even on its own terms, it limits God's power to confer minds where He likes |
| 2 | **"Heads in the Sand"** — the consequences would be too dreadful | Not an argument, a fear; comfort is not evidence |
| 3 | **Mathematical** — Gödel/Turing limits mean machines can't answer some questions | True, but humans get those questions wrong too; the limit isn't unique to machines |
| 4 | **Consciousness** — it must *feel*, not just produce the words | Pressed hard, this denies other *people* have minds (solipsism) |
| 5 | **Various disabilities** — "a machine could never do X" (be kind, err, fall in love, enjoy strawberries) | An unfounded induction from today's machines to all possible ones |
| 6 | **Lady Lovelace's** — a machine can only do what it is told; it originates nothing | Machines surprise their makers constantly; and a machine can be built to **learn** |
| 7 | **Continuity of the nervous system** — the brain isn't discrete | A discrete machine can imitate a continuous one closely enough to fool the judge |
| 8 | **Informality of behaviour** — no finite rule-set captures all of human conduct | "Laws of behaviour" we can't yet state aren't the same as having none |
| 9 | **Extra-sensory perception** — telepathy would let the human cheat | (Turing took ESP oddly seriously — see honest edges) |

Three deserve a closer look, because they are the ones the AI debate never left:

**The Mathematical Objection (#3)** leans directly on the hard edge from [[Turing Machine]]: the halting problem and **Gödel's incompleteness** prove there are questions no algorithm can settle. So — the objection runs — there will always be a question the machine must fail and a human could see the truth of. Turing's reply is deflationary and devastating: *humans also have questions they get wrong*, and nobody concludes from a person's blunders that the person can't think. A limit shared by both sides cannot be what separates them. (The full logic of that shared limit is its own card: [[Gödel's Incompleteness Theorems]].)

**The Argument from Consciousness (#4)** is the one with real teeth. Turing quotes Professor Jefferson's 1949 Lister Oration: *"Not until a machine can write a sonnet... because of thoughts and emotions felt, and not by the chance fall of symbols, could we agree that machine equals brain."* Turing's answer is to follow the demand to its end: the *only* way to be sure a sonnet was written "because of feelings" is to **be** the writer. Applied consistently, Jefferson's standard would force you to doubt every mind but your own. We don't live that way with people; the test asks why we should with machines.

**Lady Lovelace's Objection (#6)** is the most modern of all. In her 1843 notes on Babbage's Analytical Engine, Ada Lovelace wrote that the machine *"has no pretensions whatever to originate anything. It can do whatever we know how to order it to perform."* This is exactly today's *"it's just predicting the next token; it can't be creative."* Turing's two replies were prescient: first, machines *do* take their makers by surprise (any programmer knows the feeling); second, and more importantly, the objection assumes the program is hand-specified — but you can instead build a **learning machine**, a "child machine" that is *educated* rather than fully programmed, and whose later behaviour its creators never wrote down. The entire field of machine learning is Turing taking Lovelace's objection seriously enough to engineer around it.

## ELIZA, and how cheap the illusion can be

Sixteen years later came a warning. In 1966 Joseph Weizenbaum at MIT wrote **ELIZA**, a tiny program that imitated a Rogerian psychotherapist by reflecting the user's own words back as questions ("My mother hates me." → "Who else in your family hates you?"). It understood **nothing** — it had no model of the conversation, just a bag of pattern-and-rephrase tricks. Yet people poured their hearts out to it, and Weizenbaum's own secretary asked him to leave the room so she could talk to it privately.

That reaction is now called the **ELIZA effect**: human beings *over-attribute* understanding to anything that produces fluent, on-topic language. It is a permanent crack in the Turing Test's foundation. If a few hundred lines of 1966 pattern-matching can be mistaken for a listening mind, then "the judge couldn't tell" measures the **judge's readiness to believe** at least as much as the machine's intelligence. Any honest reading of the test has to carry the ELIZA effect as a discount.

## The Chinese Room — the objection that won't die

In 1980 the philosopher **John Searle** built the most famous attack on the test, and it is the one every serious treatment must answer. He aimed it at what he called **Strong AI**: the claim that a suitably programmed computer doesn't just *model* a mind but *literally has* one — really understands, really means things. (Against **Weak AI** — computers as useful tools for studying the mind — he had no quarrel.)

The thought experiment: imagine **Searle himself**, who speaks no Chinese, locked in a room. Chinese questions are posted in through a slot. He has a giant **rule-book in English** that says, for any string of Chinese symbols, which Chinese symbols to write back — pure shape-matching, never meaning. He follows it and posts fluent Chinese answers out the other slot. To the Chinese speaker outside, the room is a perfect Chinese conversationalist — **it passes the Turing Test in Chinese.** But Searle, the only mind in the room, *understands not one word.* He is manipulating **syntax** (symbol shapes) with no access to **semantics** (meaning).

![[chinese-room.svg|640]]
*Searle's room passes the test from the outside and understands nothing on the inside. Chinese goes in; a rule-book maps symbols to symbols; fluent Chinese comes out — but the only mind present is shuffling shapes it cannot read. Searle's claim: running the right program is not sufficient for understanding, because **syntax is not semantics**.*

Searle's conclusion: **passing the Turing Test is not sufficient for understanding**, because everything the room does, a computer does — and there is no understanding anywhere in the room. The standard rebuttals are worth knowing, because the modern AI debate is still fought on this ground:

- **The Systems Reply:** *Searle* doesn't understand Chinese, but *the whole system* (Searle + rule-book + paper + room) does. Searle's retort: let him memorise the rule-book and work outdoors — now he *is* the whole system, and still understands nothing.
- **The Robot Reply:** put the program in a robot with eyes, hands, a body in the world — *grounding* the symbols in things. This concedes Searle's main point: pure symbol-shuffling wasn't enough; meaning needed contact with the world.
- **The Brain-Simulator Reply:** what if the program simulates the actual firing of a Chinese speaker's neurons? Searle: simulating a thing isn't being it — a perfect simulation of a rainstorm leaves you dry.

There is no settled winner. The Chinese Room may not *refute* the Turing Test, but it permanently marks its limit: the test is **behavioural**, and behaviour cannot, even in principle, distinguish "really understands" from "flawlessly imitates understanding." That gap is exactly the question.

> [!tip] The Chinese Room is the interpret-vs-copy question, asked about machines
> The [[The Feynman Technique|Feynman Technique]] card splits knowing into two passes: **copy** (reproduce the symbols) and **interpret** (run the meaning — derive, apply, *understand*). Searle's man in the room is the pure **copy** pass made flesh: he reproduces correct Chinese with zero interpretation. Searle's whole claim is that *copy is not interpret*, no matter how perfect the copy. The open question for modern AI is precisely whether a large enough model trained to predict text is doing only the copy pass at colossal scale — or whether interpretation **emerges** from it. Nobody knows. The vault's own wager (*"understanding is the interpret pass"*) is what makes the question feel urgent rather than academic.

## The modern verdict — the machines that passed

For decades the Turing Test stayed a thought experiment with the occasional stunt. The most notorious was **"Eugene Goostman"** (2014), a chatbot that fooled 33% of judges in a five-minute test by **posing as a 13-year-old Ukrainian boy** — so its non-sequiturs read as a child's shaky English rather than a machine's errors. It was widely called a *pass*, and just as widely debunked: it didn't get smarter, it **lowered the judges' expectations**. A test you beat by sandbagging is a test about the judges, not the machine — the ELIZA effect weaponised.

Then large language models arrived, and the stunt became routine. In a controlled three-party study by **Jones and Bergen at UC San Diego (2025)**, GPT-4.5 given a persona prompt was judged to be the human **73% of the time** — *more often than the actual humans* it was paired against. By the operational criterion Turing wrote down in 1950 — interrogator does no better than chance, indeed worse — **the test is passed, and not narrowly.**

And here is the honest, slightly vertiginous part, the part worth saying plainly: the system that may be **tutoring you from this vault**, or that helped assemble this very card, is exactly the kind of machine Turing was imagining behind the curtain. Held to his 1950 standard, it clears the bar. *Including, my friend, the one you may be talking to right now.*

What did passing prove? Less than Turing's framing promised — and that is the real lesson. The field's reaction was not to crown the machines as thinkers but to **quietly retire the test as a benchmark.** Indistinguishability turned out to reward *persuasion and human-mimicry* as much as intelligence; the best way to pass is sometimes to act *less* capable (no instant arithmetic, a few typos, some attitude). Modern systems are measured instead on what they can *do* — reasoning, mathematics, coding, factual accuracy — not on whether they can fool a stranger for five minutes. The Turing Test won its argument so completely that it made itself obsolete: it dragged "can machines think?" out of metaphysics and into engineering, and engineering promptly invented sharper rulers.

## What the test does and doesn't prove

- **It does** force intellectual honesty. Deny a behaviourally-indistinguishable machine a mind, and you owe a *principled* reason — one that doesn't also accidentally deny minds to other people. That burden-flip is permanent and valuable.
- **It does not** detect consciousness or inner experience. The Chinese Room shows behaviour can't reach "understanding"; Nagel's *"what is it like to be a bat?"* shows it can't reach *feeling*. The test was never built to.
- **It does not** measure general intelligence cleanly. It conflates intelligence with *human-likeness* and with the judge's gullibility. A superhuman intelligence that reasoned nothing like us might **fail** for being too obviously not-a-person.
- **It is** a brilliant piece of philosophy and a poor piece of engineering — which is fine, because Turing wrote it as the former. Its job was to make the question *thinkable*, and it did.

## Common Misconceptions

> [!warning] "Passing the Turing Test means the machine is conscious / really understands."
> The test is purely **behavioural** — it measures indistinguishability in conversation, nothing more. The Chinese Room argument shows that perfect behaviour is, even in principle, compatible with zero understanding. Passing tells you a system *acts* like a thinker; it is silent on whether anything is going on inside.

> [!warning] "The Turing Test is a standard, scored benchmark with an official pass mark."
> There is no canonical protocol — judge count, time limit, whether the machine may lie about being a computer, the calibre of the judges, all vary and all change the result. "Passing the Turing Test" is a *philosophical milestone*, not a certified score. Most AI research no longer uses it to evaluate anything.

> [!warning] "Turing's test was a direct interrogation: 'Are you a computer?'"
> It grew from an **imitation** game. The machine's task is to *perform* a human convincingly under any questioning the judge invents — not to answer a yes/no quiz. The gendered original (man imitating a woman) makes the performance framing explicit.

> [!warning] "ELIZA / Eugene Goostman passing proves machines were already intelligent in 1966 / 2014."
> Both exploited the **ELIZA effect** — humans over-attribute understanding to fluent language — and Goostman additionally gamed the judges by posing as a child non-native speaker. They reveal how *cheap* the illusion can be, which is a caution about the test, not a triumph of the machines.

## Exam Notes

The Turing Test is **not a named, examinable topic** on Cambridge IGCSE 0478 or A-Level 9618 in the way the [[CPU Architecture and the Fetch-Execute Cycle|von Neumann model]] is. It belongs to the **philosophy of artificial intelligence**, and it earns its place here as the natural companion to [[Turing Machine]] (Turing's "other machine") and as the conceptual anchor for any AI unit:

- **Cambridge A-Level 9618** — the A2 **Artificial Intelligence** material (types of AI, machine learning, neural networks) is where this card's *"can a machine think?"* framing and the Lovelace/learning-machine point give students the history their syllabus assumes but doesn't teach.
- **AP Computer Science Principles** — the *Impact of Computing* big idea raises exactly these questions (machine intelligence, its limits, its social effect); the Turing Test is the standard entry point.
- **University** — a fixture of first courses in AI, philosophy of mind, and cognitive science. The Turing Test, the Chinese Room, Strong vs Weak AI, functionalism, and the symbol-grounding problem are a single connected unit, and this card is its on-ramp.
- **General literacy** — in the age of LLMs this is no longer abstract. Knowing what the test does and doesn't establish is the difference between *"the AI is alive"* and *"the AI is indistinguishable in conversation, which is a fact about behaviour."*

### IB Computer Science (first assessment 2027)

- **Not a named statement, but closer to the syllabus than the Cambridge boards.** Theme A's fourth strand is **A4 Machine Learning**, and two of its sub-topics sit directly against this material: **A4.1 Machine learning fundamentals**, where *"can a machine think?"* is the question the whole strand presupposes and never states, and **A4.4 Ethical considerations**, where the behaviour-versus-understanding distinction is the load-bearing one — an argument about whether a system *understands* its outputs is an argument about the Chinese Room whether or not anyone names it.
- What is examined there is machine learning as **method** (approaches, preprocessing, evaluation, the HL-only A4.2 and A4.3), not philosophy of mind. So nothing on this card is directly assessed. It is the conceptual on-ramp: a student who has read it can say *why* "the model passed a benchmark" is a claim about behaviour rather than about cognition, which is exactly the sort of qualification A4.4 rewards.
- No `syllabus/IB-CS-A4` tags are carried, correctly — the card supports the strand rather than closing any statement in it.

## Connections

- **Prerequisite / sibling:** [[Turing Machine]] — Turing's *first* machine answers "what can be computed?"; the Turing Test is his *second* machine, asking "what can be mistaken for a mind?" Same author, same 14-year arc, opposite ends of the question of what a machine is.
- **The man behind it:** [[Stories/Turing at Bletchley]] — reads the test as *"an act of faith in people"*: judge by what something *does*, not what it's *made of* — written by a man whose own country was judging him for what he **was**. The biography the equations leave out.
- **The understanding question:** [[The Feynman Technique]] — the **interpret vs copy** distinction *is* the Chinese Room debate (syntax-copy without semantic-interpret); whether interpretation emerges from scaled-up prediction is the live question.
- **The shared hard edge:** [[Gödel's Incompleteness Theorems]] — the Mathematical Objection (#3) rests on it; Turing's reply (humans share the limit) is the bridge.
- **What LLMs are made of:** [[Information Theory]] — a language model is Shannon's 1948 framework at scale (cross-entropy, perplexity); the thing now passing the test is built out of the bit.
- **How they reason:** [[Chain of Thought]] — the card spans both senses of the phrase: Pólya's human reasoning chain, and the LLM *"think step by step"* prompting (Google, 2022) that sharpened the very models now clearing Turing's bar.

## Glossary / Notation Reference

This is a conceptual card; the only "notation" is its vocabulary.

| Term | Means |
|------|-------|
| Imitation Game | Turing's original name for the test — a judge tries to tell a hidden machine from a hidden human by text alone |
| operationalism | defining a concept by the *test you would run* (observable behaviour) rather than by an imagined inner essence |
| Strong AI | the claim that a suitably programmed computer *literally has* a mind and really understands (Searle's target) |
| Weak AI | the claim that computers are useful *tools* for modelling and studying the mind (Searle does not dispute this) |
| syntax | manipulation of symbols by their *shape* / form — what the Chinese Room does |
| semantics | the *meaning* the symbols carry — what the Chinese Room (Searle argues) lacks |
| ELIZA effect | the human tendency to over-attribute understanding to any system that produces fluent language |
| symbol grounding | the problem of connecting internal symbols to real-world things they're *about* (the Robot Reply's concern) |
