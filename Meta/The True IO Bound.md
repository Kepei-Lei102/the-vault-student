---
chinese: 真正的 I/O 瓶颈 (zhēnzhèng de I/O píngjǐng) — 慢的从来不是计算，是搬运
prerequisites:
  - "[[RAM and the Memory Hierarchy]]"
  - "[[Parallel and External Sorting]]"
  - "[[Decouple and Recouple]]"
  - "[[Forward Reading and Problem Discovery]]"
leads_to:
  - "[[The Love of Wisdom]]"
  - "[[The Feynman Technique]]"
  - "[[Compression Is Intelligence]]"
tags:
  - subject/methodology
  - subject/philosophy
  - subject/computer-science
  - domain/cognition
  - domain/computer-architecture
  - domain/learning
  - level/life
  - type/methodology
  - type/meta
  - type/cross-domain
---

# The True I/O Bound 真正的 I/O 瓶颈

> *The slow step is almost never the thinking. It is moving the data — into the machine, into the head, and past the self.*

## What this card is for

Every computer scientist learns one lesson early and then keeps relearning it at every scale: **the processor is rarely the bottleneck.** Programs are slow because they wait — for memory, for the disk, for the network, for the user. This card takes that lesson seriously enough to climb it as a ladder. Each rung is a system whose limit is not how fast it *computes* but how fast data *gets through*, and the rungs go from silicon to you:

1. **The machine.** Disk, network and memory bandwidth dwarf the arithmetic — and this is still true at the frontier, where a chip that can do a quadrillion multiplications a second spends most of its life waiting for bytes.
2. **The human as hardware.** Your intuition is astonishingly fast, but your working memory holds about four things and your speech channel carries a few dozen bits a second. External memory — paper, notes, a vault like this one — is not a crutch. It is the architecture.
3. **The self as filter — the true bound.** Evolution shipped every one of us with a filter that admits input by one test: *does this fit who I think I am?* What it drops is precisely the highest-value traffic in the stream — the correction, the contradicting fact, the sentence you least want to hear.

The card ends with the only known way to widen that last pipe, and with a plain statement of why this vault exists.

### 中文锚点

电脑城的老板有一句万能话：**"加个固态。"** 一台卡得要死的旧笔记本，CPU 一点没换，换上固态硬盘之后开机从三分钟变成十秒，"跟新的一样"。这件事背后的道理，就是整张卡的主题：**慢的从来不是计算，是搬运。** CPU 做一次加法不到一纳秒，从机械硬盘取一块数据要十几毫秒，差了一千万倍；把内存的一次访问算作一秒，硬盘就是一天半。整个存储层级（[[RAM and the Memory Hierarchy]]）、外部排序（[[Parallel and External Sorting]]），乃至今天训练和运行大模型，瓶颈都在"数据搬得够不够快"，而不是"算得够不够快"——这是第一级。第二级是你自己：人的直觉快得惊人，但**工作记忆只有四格左右**，二十秒不复述就没了；说话这条信道，每秒只有 39 比特。所以草稿纸不是作弊，笔记不是偷懒，这个知识库也不是拐杖——**外部记忆本身就是设计**。第三级才是真正的瓶颈：**自我**。进化给每个人装了一台过滤器，它按"这跟我心里的自己合不合"来决定放不放行，于是被丢掉的恰恰是价值最高的那些包：别人指出你错了的那一句、你最不想听的那一句。这张卡从机器讲到人，再讲到过滤器，最后讲怎么把它松开——**星空即心空**：向外探索和向内探索，是同一条路。

| English | 中文 | 一句话 |
|---|---|---|
| I/O bound | I/O 瓶颈 / 输入输出受限 | 快慢由**搬数据**决定，不由算术决定 |
| Memory wall / von Neumann bottleneck | 内存墙 / 冯·诺依曼瓶颈 | 处理器和内存之间那条太窄的路 |
| Roofline | 屋顶线模型 | 一张图告诉你：这个任务在等字节，还是在等算术 |
| Working memory | 工作记忆 | 脑子里同时拿得住的那四格左右 |
| Chunk | 组块 | 工作记忆的单位：一个有意义的整体，不是一个字符 |
| The filter / projection | 过滤器 / 投射 | 自我按"合不合我"筛选输入，丢掉最有价值的那些 |
| Confabulation | 虚构 / 编造式解释 | 大脑为已做的选择现编一个理由，并且自己相信 |
| Echo chamber | 回音室 | 对信念的正反馈：喂你更多你已经相信的 |

---

## Part I — The machine: the ladder of waiting

### One RAM access, one second

Take every delay a computer suffers and rescale it so that one access to main memory takes **one second** of human time. The ladder is the whole argument in one picture:

![[true-io-bound-ladder.svg|860]]

On that scale the arithmetic is a *few milliseconds* — a register read, an addition, a cache hit. Then the rungs open up: ten minutes for a solid-state disk, a day and a half for a spinning one, seventeen days for a packet to cross the Pacific and come back — and then the human rungs, on the *same* ladder, in **months and centuries**. The processor is the fastest thing in the building by a factor of a million or more, and it spends almost all of its life waiting for something slower. [[RAM and the Memory Hierarchy]] is the engineering answer to the top half of the ladder (small fast caches in front of big slow memory); [[Secondary Storage]] to the middle; [[Input and Output Devices]] and [[Interrupt Handling]] to the bottom — the CPU refusing to sit and poll a keyboard that answers once every few centuries of its time.

### Backus's bottleneck, and the sixty years since

The pattern has a name and a birthday. In his 1977 Turing Award lecture, **John Backus** — the man behind FORTRAN — called the single channel between processor and memory the **von Neumann bottleneck**, and complained that the whole discipline of programming had grown up as a way of pushing words one at a time through it ([[Von Neumann machine]]). Every decade since has confirmed him from a new direction:

- **Amdahl's law** (1967): a program is bounded by its serial part, however many processors you add — and the serial part is usually *moving the data to where the processors are*. [[Parallel and External Sorting]] measured this: eight cores did not give eight times the speed, because every chunk had to be copied into a fresh process and the results copied back.
- **External sort**: a terabyte on a machine with sixteen gigabytes of memory is sorted by counting *passes over the disk*, not comparisons. An algorithm that compares *more* but reads the file *once fewer* wins. It is, in that card's phrase, an I/O-cost problem wearing a sorting costume.
- **The memory wall** (Wulf and McKee, 1995): processor speed grew about fifty per cent a year for two decades while memory latency improved by single digits. The gap is the reason a modern chip is mostly cache by area — silicon spent not on computing but on *not waiting*.
- **Jim Gray's rule** (2003): computing is so cheap and moving bytes so expensive that the right design is to *send the program to the data*, never the data to the program. MapReduce, the database, the data warehouse of [[NoSQL and Distributed Data]] are that sentence made into systems.

### The frontier: a chip that is mostly waiting

The lesson has not weakened at the top of the market; it has sharpened. Consider one of the fastest chips of the current decade running a language model that answers one user. To produce *each token* the chip must read every weight of the model out of memory once and do about two arithmetic operations per weight:

| An 8-billion-parameter model on one H100 | per token |
|---|---|
| Bytes to move (16-bit weights) | 16 GB |
| Time to move them at the chip's memory bandwidth (3.35 TB/s) | **4.8 ms** |
| Arithmetic (16 GFLOP at ~990 TFLOP/s) | **0.016 ms** |
| Ratio | **~300 : 1** in favour of waiting |

The chip computes for sixteen microseconds and waits nearly five milliseconds. Its arithmetic units are idle more than 99% of the time, and no amount of extra arithmetic would help — the bound is *bandwidth*. This is why the industry's real currency is memory bandwidth and interconnect, why inference engines *batch* many users so that one read of the weights serves all of them, and why the training of the largest models is limited by how fast the network can average gradients across thousands of chips rather than by any chip's speed.

The tool the engineers use to see this is the **roofline model** (Williams, Waterman and Patterson, 2009), and it is worth knowing because it puts the whole of Part I on one graph:

![[true-io-bound-roofline.svg|820]]

The horizontal axis is **arithmetic intensity** — how many operations a workload performs per byte it moves. The roof is the chip's ceiling: a sloping part where bandwidth limits you (every byte buys a few operations, so more bytes per second is the only way up) and a flat part where the arithmetic units limit you. The **ridge** where they meet is the chip's character in one number — for this chip, about three hundred operations per byte. Anything to the left of it is *I/O-bound*, and the whole history of Part I lives to the left: external sort, one user's decode, a database scan. Batching moves a workload rightward by reusing each byte for more users; that is the entire trick, and it is [[Decouple and Recouple]]'s buffer in a new costume — collect, then serve at the fast side's rate.

> [!tip] The honest edge of Part I
> Not everything is I/O-bound. A big matrix multiply, a physics simulation, a prefill pass over a long prompt sit to the *right* of the ridge and genuinely want faster arithmetic. The claim is not that compute never matters; it is that **the default guess is wrong**. When something is slow, an engineer's first question is not "how do I compute faster?" but "**what am I waiting for?**" — and nine times in ten the answer is a byte in transit. That question is the whole method of this card, and the next two parts ask it of a person.

---

## Part II — The human as hardware

### Fast compute, tiny cache

Human thinking is not slow. A chess master glances at a board and *sees* the good move before any conscious search begins; a doctor walks into a ward and knows which patient is in trouble; you recognise a friend's walk from a hundred metres. Whatever intuition is at the level of neurons, it behaves like a **massively parallel pattern search** — millions of stored patterns matched at once, the best few surfacing as a feeling. It is tempting to call it a quantum computer; the physics says otherwise (a warm, wet brain loses quantum coherence in something like $10^{-13}$ seconds, far too fast for any computation to ride on), so keep it as a metaphor for *parallelism*, which is real, rather than for quantum mechanics, which is not involved.

The compute is fast. The cache is the problem. **George Miller** (1956) put the capacity of immediate memory at seven items, plus or minus two; modern work — Nelson Cowan's 2001 review is the standard reference — finds the honest number closer to **four chunks**, and finds it *decays in about twenty seconds* unless you keep rehearsing it. Four slots, twenty seconds. That is the L1 cache of the human mind, and it is the reason a phone number is spoken in groups, a proof is remembered as three moves rather than thirty lines, and a student who reads a question once and looks away has already lost the second condition.

The one lever is **chunking**. Chase and Simon (1973) showed chess masters a real position for five seconds and they reconstructed most of the board; novices managed a handful of pieces. Then they showed *random* positions — same pieces, no chess sense — and the masters fell to the novices' level. The cache had not grown; the *unit* had. A master's slot holds "castled king's side with a fianchettoed bishop", a novice's holds "a knight on f3". Expertise is chunking: it is the compression of [[Information Theory]] applied to your own cache, so that four slots hold a whole position.

![[true-io-bound-chess.png|760]]

*Carnegie Mellon, 1973. Five seconds of a real game and the master rebuilds the board from memory; five seconds of the same pieces scattered at random and he places four, like anyone. The cache never grew. The unit did.*

### The channel

The pipe *between* people is narrower still. Reading runs at a few hundred words a minute; speech at about a hundred and fifty. A 2019 study across seventeen languages (Coupé and colleagues) found that whatever the language, spoken information arrives at roughly **39 bits per second** — fast-spoken languages carry less per syllable, slow ones more, and the product is nearly constant. Thirty-nine bits a second is a slower link than the first modems. Every lecture, every conversation, every explanation in this vault is being pushed through it. A teacher who talks faster does not transmit faster; they only raise the drop rate at the other end.

### External memory is the architecture

Put the two numbers together — four chunks, twenty seconds; thirty-nine bits a second — and one design conclusion follows, the same one the engineers reached: **you cannot compute your way out of a bandwidth limit; you build a hierarchy.** A machine wraps its tiny cache in RAM, its RAM in disk, its disk in the network. A mind wraps its four slots in notes, its notes in books, its books in a searchable vault, and the vault in the world. Every layer is slower and larger than the one inside it, and every layer exists because the one inside is too small.

This reverses a piece of school morality. Scratch paper is not weakness; it is L2. A formula sheet is not cheating; it is swapping to disk. Looking something up is not failure to learn; it is a cache miss served correctly. **Cognitive load theory** (John Sweller, from 1988) turned this into experiments: novices learn *more* from a worked example than from solving the problem themselves, because problem-solving fills the four slots with search and leaves none for the pattern being taught. That result is why every worked example in this vault names its tool before each step ([[Chain of Thought]]) — the name is a chunk, and a chunk is a slot saved — and why the whole thing is written down at all. This vault is your L3: too slow to think *in*, exactly the right size to think *from*.

> [!info] Recall that the exam is a cache-thrash
> The reason time pressure makes able students stupid is not that they think slower under stress; it is that stress **evicts**. Four slots, and the fifth item — "how many marks is this?", "she finished already" — pushes out the second condition of the question. The fix is the engineer's: write the invariants down *first* ([[Forward Reading and Problem Discovery]]), so that the page is the cache and your head is free to search.

---

## Part III — The true bound: the filter you did not build

### Where it came from

So far the bounds have been honest limits: small caches, narrow pipes. The last one is different in kind, because it is *selective* — it does not slow the stream, it chooses what to drop, and it chooses badly on purpose.

Evolution built minds for survival in groups, and in a group the self you *present* is a survival tool. Robert Trivers argued in the 1970s, and at book length in 2011, that self-deception evolved *because* it improves deception of others: the liar who believes the lie shows no tells. The self-serving bias that psychology measures in every population — successes are mine, failures are circumstance — is not a bug in an otherwise honest reader of the world. It is a working filter, installed for its owner's protection, and its test for admitting a packet is one question: **does this fit who I already think I am?**

![[true-io-bound-filter.svg|900]]

### What it drops

The trouble is the *selectivity*. A random filter would cost you a fraction of everything. This one preferentially drops one class of packet — **the ones that contradict the self-narrative** — and those are the packets with the highest information content in the stream. [[Information Theory]] says it exactly: the surprise of a message is $-\log_2 p$, so the packet you *expected* carries nearly nothing, and the packet you did not is the only one worth the bandwidth. The filter throws away the traffic in order of value, highest first.

Three demonstrations, none of them about anyone you know:

- **Wason's 2-4-6 task** (1960). Subjects were told that the triple 2, 4, 6 obeys a hidden rule and asked to discover it by proposing triples and hearing yes or no. Almost everyone proposed 8, 10, 12, then 20, 22, 24 — triples that *confirmed* their guess ("even numbers going up by two") — and announced the guess with confidence. The rule was *any increasing sequence*. The one triple that would have revealed it, something like 1, 2, 3 or 5, 4, 3, was the one they almost never sent, because a "no" would have been a packet against themselves. Confirmation bias is the filter caught on camera.
- **Semmelweis** (1847). In Vienna's maternity hospital the ward staffed by doctors killed mothers at several times the rate of the ward staffed by midwives. Ignaz Semmelweis noticed the doctors came to deliveries straight from the dissecting room, made them wash in chlorinated lime, and the death rate fell from around one in six to around one in fifty within months. The medical establishment rejected it for twenty years — not because the data was weak but because the packet said *you, the gentlemen, have been killing your patients with your own hands.* Nothing in the stream that decade was more valuable, and nothing was more thoroughly dropped. He died in an asylum in 1865, two years before Lister's antiseptic surgery began to vindicate him.
- **The returned paper.** A student reads a mark scheme and finds the line they lost: "*I knew that — silly mistake.*" Watch what the sentence does. It admits the packet's *existence* and drops its *content*: the mistake was not silly, it was a misconception with a shape, and "I knew that" is the filter stamping it as already-known so that it need not be stored. This vault's misconception callouts exist to defeat exactly this move — each one is a dropped packet pinned to the page where the filter cannot lose it.

![[true-io-bound-semmelweis.png|760]]

*Vienna, 1847. The basin of chlorinated lime, the falling death rate on the wall, and the gentlemen of the faculty declining to look — because the packet said the killing was done by their own hands. Twenty years of the most valuable message in medicine, dropped by the filter it insulted.*

### It filters at read time, too

You might hope the damage is done only once, at the moment of hearing. It is worse. Memory is not a recording that the filter guards the entrance to; it is a **reconstruction** performed every time you remember, and the filter runs on the reconstruction. Frederic Bartlett (1932) had English students read a Native American folk tale, *The War of the Ghosts*, and retell it over weeks and months; with every retelling the unfamiliar details drifted toward the tellers' own world — canoes became boats, spirits became ordinary enemies, the story straightened itself into one they would have told. Loftus and Palmer (1974) showed film of a car accident and asked how fast the cars were going when they "hit" or when they "smashed"; the "smashed" group estimated higher speeds and, a week later, *remembered broken glass that was never in the film.* The ego is not a doorman. It is an editor with access to the archive, and it revises old entries to fit the current story. That is why an honest account of one's own past is genuinely difficult and not merely embarrassing: the source has already been rewritten.

### Worked example — a four-hour talk, inverted

In the summer of 2026 a transcript circulated of a four-hour conversation between the founder of a leading Chinese AI laboratory and a group of investors. Read in full, its spine is two words: *restraint* — do the narrow thing extremely well, refuse the fashionable expansions — and *you cannot predict* — the field's own leaders do not know which direction wins, so do not bet as if you did. Commercial aerospace is not mentioned. Embodied AI is explicitly named as *not* a priority.

A reader summarised it for their friends in one confident line: *three sectors to bet on — AI, aerospace, embodied robots; bet the era; every bubble is cheap in hindsight.*

Trace the packets. The talk's thesis was *humility about prediction*; the summary was *a prediction*. The talk deprioritised embodied AI; the summary promoted it. The talk never mentioned aerospace; the summary added it. The filter did not merely drop the message — it **inverted** it, because the reader's self-narrative was *I am someone who sees the next big thing*, and a four-hour argument for restraint does not fit that person, while a three-item betting slip fits perfectly. Nothing was misheard. Every sentence passed through the four-slot cache and the 39-bit channel just fine. The loss happened at the filter, and it happened in the direction that flattered the reader.

> [!warning] The tell
> When a summary is *more* certain than its source, the filter has been at work. Real knowledge usually arrives hedged, because the people who have it know its edges. A takeaway that is cleaner, bolder and more flattering to the taker than the original is not a distillation; it is a projection.

### Positive feedback: the echo chamber

Recall from [[Sensors and Control Systems]] the microphone held to its own loudspeaker: positive feedback, where the output amplifies the input that caused it. A recommendation feed that shows you more of whatever you already react to is that circuit built at planetary scale, and what it amplifies is *exactly the filter's own selection*. The ego drops the contradicting packet; the feed notices you did not dwell on it and stops sending; the ego now receives a stream with the contradictions already removed and concludes, reasonably, that it was right all along. Two filters in series, each confirming the other. The engineering name for this is a loop with no negative feedback, and every engineer knows what such a loop does: it saturates.

---

## Part IV — Hallucination as a mirror

### The interpreter

In the 1970s Michael Gazzaniga studied patients whose two brain hemispheres had been surgically separated. He could show a picture to the right hemisphere alone (which cannot speak) and ask the left hemisphere (which can) to explain the patient's response. In the famous trial the left eye saw a snow scene and the right eye a chicken claw; the patient's left hand chose a shovel and the right hand a chicken. Asked why the shovel, the speaking hemisphere — which had never seen the snow — answered instantly and with total confidence: *to clean out the chicken shed.* No hesitation, no "I don't know." A reason was manufactured on the spot to fit the action, and believed. Gazzaniga called this module **the interpreter**, and argued it runs in everyone: we act, and a narrator explains, and the narrator does not have access to the real causes and does not know that it doesn't.

![[true-io-bound-chicken-shed.png|760]]

*The speaking half of the brain never saw the snow. Asked why the hand it does not control chose a shovel, it answers at once, fluently, and believes itself. Everyone has this narrator; the surgery only let us catch it working.*

It is not confined to surgery. In 2005 Johansson and colleagues asked people to choose the more attractive of two faces, then handed them — by sleight of hand — the *other* photograph and asked why they had chosen it. Most did not notice the swap, and explained fluently why they preferred the face they had rejected seconds earlier. **Confabulation** is the technical word: a confident, fluent, sincere account with no connection to the truth.

### Why the machine's version is easier to patch

A large language model that states a false citation in perfect academic prose is doing something structurally similar: producing the most plausible continuation with no internal signal that distinguishes *recalled* from *invented*. Part of the reason is technical — the training objective rewards plausibility, not truth, and the model has no ground to check against. But part of it is that the model learned to write from **us**, and the corpus is the output of billions of interpreters explaining choices they did not make. In that sense the model's hallucination is a mirror: the same fluent confidence, learned from the species that invented it.

The difference is in the fix. The machine's confabulation is being patched — retrieval that grounds answers in a source, calibration training that rewards "I don't know", tools that check. The human version is harder, not because the mind is cleverer but because **the filter defends itself**: the patch arrives as a packet, the packet contradicts the self, and the filter drops the patch. That asymmetry is the deepest fact in this card. A system whose error-correction is blocked by the error is not a system that improves with more input. It needs the filter *opened from the inside* — which is the subject of the last part.

---

## Part V — Widening the pipe: 星空即心空

### Feynman's first principle

Richard Feynman, in the 1974 address that named cargo-cult science, gave the rule in one sentence: *the first principle is that you must not fool yourself — and you are the easiest person to fool.* Everything scientific method adds to ordinary looking — controls, blinding, pre-registration, the *show your working* of a mark scheme — is a mechanism for routing packets *around* the filter. The double-blind trial is not there because doctors are dishonest; it is there because an honest doctor's filter will drop the patient who got worse. Science is the engineering of an anti-filter, and it works because it puts the check *outside* the self, where the ego cannot edit it.

### The cave

The oldest popular telling of this card's last thesis is a swamp. In *The Empire Strikes Back* the apprentice stands at the mouth of a cave on Dagobah and asks his teacher what is inside, and the answer is the whole of Part III in six words: only what you take with you. He goes in armed. A masked figure comes at him out of the dark; he strikes first, and the mask splits open on his own face.

![[true-io-bound-cave.png|760]]

*He brought the enemy in with him. The cave held nothing; it returned the input. What came at him was his own filter, and the mask it wore was the only thing in the swamp that was not his.*

Read the scene as engineering rather than mysticism and it says something exact. The threat the apprentice perceived was a projection — the ego's classification of the input, not the input — and the moment he attacked it he lost the information the cave was offering, which was the shape of his own fear. The lesson of the swamp is not that the dark side is out there. It is that the packet you flinch from is usually addressed to you. A second telling in the same story, years later, puts the apprentice in a mirror cave and lets her ask to see her parents; the mirror shows her only herself, endlessly. Same lesson from the other side: the ego wants an external answer, and the honest cave returns the questioner.

That is what the Chinese phrase in the heading means. **星空即心空** — the starry sky is the empty mind. Exploring outward and exploring inward are one motion, because the thing that limits how much of the world reaches you is the same thing that limits how much of yourself you can see. 悟空 and 悟爱 are one awakening: to see clearly and to love clearly are the same clearing. The more of yourself you can feel, the more of the world can get in — and the more you can do in it.

### Three practices

The same design can be applied to one person, and the practices that do it are old, ordinary, and all of them work by *moving the check outside*:

1. **Write it down honestly, then read it as a stranger.** A written sentence is a packet stored where the read-time editor cannot silently revise it. The discipline is to write what happened before writing what it meant — [[The Feynman Technique]]'s *interpret* pass is this in another key: what you cannot rebuild on paper from scratch, you did not have, however strongly you feel you did. The felt certainty is the interpreter's output, not the archive's.
2. **When feedback is offered, take it without hesitation.** [[Sensors and Control Systems]] ends on the observation that RLHF — human judgment closing the loop on a model — is the most expensive feedback signal ever purchased. The scarcest input your own control loop can receive is someone else's honest reading of you, and the filter's first reflex is to explain why it does not apply. The practice is mechanical: *store first, argue later.* Write the packet down before your interpreter starts.
3. **Sit and watch the filter run.** Every contemplative tradition that survived converges on one exercise: be still, and observe thoughts arriving without acting on them. Stripped of doctrine, it is a debugger attached to the interpreter — you watch the narrator generate its explanations in real time, and the watching is itself the loosening, because a filter you can *see* is no longer transparent. It is the apprentice's cave without the swamp: sit long enough and the masked thing walks up on its own, and this time you do not strike.

### Faraday's request, and what this vault is

In 1857 Michael Faraday, over seventy and never taught mathematics, wrote to the young Maxwell, who had just turned his hand-drawn lines of force into equations. He asked whether the mathematics could not be translated back *into common language* for people like him ([[The Bookbinder's Apprentice]]). It is one of the most important requests in the history of teaching, and it is an I/O request: the knowledge existed, the channel to a whole class of minds did not.

This vault is an answer to that request, and now its design can be stated in the language of this card. It is **external memory** — the L3 for a four-slot cache, written so that a student with no teacher can think *from* it. It is **a translator** — rigour carried back across the formalism barrier into stories, pictures, and a Chinese anchor, so that the packet can get through a 39-bit channel at all. And above both, it is an **anti-filter**: every misconception callout is a packet the ego would drop, pinned to the page; every honest edge in a Story is a contradiction kept in the record; every *why* is a check placed outside the reader's interpreter, where it cannot be edited into "I knew that." An ordinary textbook is a cache. This is meant to be something more — a cache that argues back.

### "We accept" — where every trace ends

One last honesty, so the card does not overclaim. [[Hypothesis Tests]] teaches that in the probabilistic world causality is never traced to the end; it is *accepted*, when the evidence makes disbelief the crazier position, at a price set by which mistake you can afford. The filter is not the only thing that stops a trace. Every reader, every scientist, every hunter stops somewhere and says *enough — we accept.* The difference between the filter and the scientist is not that one stops and the other does not. It is that the scientist **prices the stop** — names the error they are risking and what it costs — while the filter stops silently, exactly where the self is comfortable, and calls the place knowledge. Widening the pipe does not mean never stopping. It means knowing where you stopped, and why, and that you could be wrong there.

---

## How to use this card

1. **When something is slow — a program, a project, your own learning — ask "what am I waiting for?" before "how do I go faster?"** The answer is a transfer nine times in ten: a byte, a reply, a fact not yet looked up, a decision not yet made.
2. **Design for the four slots.** Write the invariants down before you think. Read a question twice. Chunk deliberately: name the tool, and the name is a slot saved.
3. **Treat "I knew that" as an alarm.** It is the sound of a packet being dropped. Store the packet — write the misconception in your own words — *before* deciding whether it applies to you.
4. **When a summary is cleaner than its source, distrust the summary,** especially if it flatters the summariser, and most of all if the summariser is you.
5. **Take feedback mechanically: store first, argue later.** The argument can wait; the packet cannot.
6. **Watch the narrator.** Once a day, notice one explanation you gave for something you did, and ask whether you had the data for it. Most of the time you will find the chicken shed.

---

## Misconceptions

1. **"A faster processor makes the computer faster."** Only if the workload is compute-bound, and most are not. The SSD upgrade that revives an old laptop leaves the CPU untouched; it shortens the wait.
2. **"Working memory can be trained to hold more."** The number of chunks is stubborn; what training changes is the *size* of a chunk. Masters do not have bigger caches. They have better compression.
3. **"Notes and formula sheets are a crutch."** They are the memory hierarchy. A mind that refuses external memory is a processor that refuses to use RAM.
4. **"Confirmation bias is a flaw in careless people."** It is the standard filter, running in everyone, and it drops packets in order of value. Care does not remove it; only an external check does.
5. **"Memory is a recording."** It is a reconstruction, re-edited at each read by the same filter that guards the write. Sincerity is not evidence of accuracy.
6. **"AI hallucination is a machine-specific defect."** Its structure — fluent, confident, ungrounded explanation — is confabulation, and it was learned from a corpus of human confabulation. The machine's version is the one being patched.

---

## Connections

- **Parents:**
   - [[RAM and the Memory Hierarchy]] — the engineers' answer to the top half of the ladder; this card climbs the same ladder past the disk and into the reader.
   - [[Parallel and External Sorting]] — the two measured instances: cross-process copying as Amdahl's serial tail, and disk passes as the true cost of an external sort.
   - [[Decouple and Recouple]] — the buffer that lets a fast side and a slow side coexist; batching on the roofline is the same buffer.
   - [[Forward Reading and Problem Discovery]] — the hunter traces causality; this card names the three places the trace is throttled and the one place it is censored.

- **Children:**
   - [[The Love of Wisdom]] — philosophy as knowing that one lacks; the filter is precisely the part of us that pretends it does not.
   - [[The Feynman Technique]] — the *interpret* pass as the everyday anti-filter: what cannot be rebuilt on paper was never received.
   - [[Compression Is Intelligence]] — the sibling card: that one is about the codec, this one is about the dropped packets. Prediction compresses; projection deletes.

- **Cross-domain:** [[Von Neumann machine]] — Backus's bottleneck, where the machine half of this card begins; [[Information Theory]] — surprise as $-\log_2 p$, the measure by which the filter's discards are the most valuable traffic; [[Sensors and Control Systems]] — negative feedback as the only stable loop, the echo chamber as the positive-feedback failure, and the RLHF corollary; [[Hypothesis Tests]] — "we accept" as the priced stop that distinguishes a scientist's end-of-trace from the filter's; [[The Bookbinder's Apprentice]] — Faraday's request for a translation back into common language; [[Chain of Thought]] — naming the tool as chunking; [[Fun Is the Brachistochrone]] — the same vault philosophy from the motivation side: that card is why a student *wants* to hunt, this one is what stops the prey from arriving.

- **Misconception traps cleared:** faster CPU means faster computer; working memory is trainable in size; notes are a crutch; confirmation bias is carelessness; memory is a recording; hallucination is a machine-only defect.

## Sources

- J. Backus, *Can Programming Be Liberated from the von Neumann Style?*, Turing Award lecture (1977), CACM 21(8), 1978 — the "von Neumann bottleneck".
- G. Amdahl, *Validity of the single processor approach*, AFIPS 1967. W. Wulf and S. McKee, *Hitting the Memory Wall*, ACM SIGARCH 1995. J. Gray, *Distributed Computing Economics*, MSR-TR-2003-24.
- S. Williams, A. Waterman, D. Patterson, *Roofline: An Insightful Visual Performance Model for Multicore Architectures*, CACM 52(4), 2009. H100 figures: NVIDIA H100 SXM datasheet (≈989 TFLOP/s dense FP16, 3.35 TB/s HBM3); the decode arithmetic is two operations per weight per token.
- G. A. Miller, *The Magical Number Seven, Plus or Minus Two*, Psych. Review 1956. N. Cowan, *The magical number 4 in short-term memory*, Behavioral and Brain Sciences 2001. L. and M. Peterson, *Short-term retention of individual verbal items*, 1959 (the ~20-second decay). W. Chase and H. Simon, *Perception in chess*, Cognitive Psychology 1973.
- C. Coupé, Y. M. Oh, D. Dediu, F. Pellegrino, *Different languages, similar encoding efficiency*, Science Advances 2019 (≈39 bits/s). J. Sweller, *Cognitive load during problem solving*, Cognitive Science 1988; Sweller and Cooper 1985 on the worked-example effect. M. Tegmark, *Importance of quantum decoherence in brain processes*, Phys. Rev. E 2000.
- R. Trivers, *The Folly of Fools* (2011). P. Wason, *On the failure to eliminate hypotheses in a conceptual task*, QJEP 1960. I. Semmelweis, *Die Aetiologie… des Kindbettfiebers* (1861); the First Clinic mortality figures for 1847–48. F. Bartlett, *Remembering* (1932). E. Loftus and J. Palmer, *Reconstruction of automobile destruction*, 1974.
- M. Gazzaniga, *The Interpreter* (in *The Mind's Past*, 1998; the 1978 chicken-claw trial). P. Johansson et al., *Failure to detect mismatches between intention and outcome in a simple decision task*, Science 2005. R. Feynman, *Cargo Cult Science*, Caltech commencement 1974.
- The four-hour investor conversation of summer 2026 is cited as it circulated; the worked example depends only on the contrast between its stated theses and a reader's summary, not on any detail beyond those.
