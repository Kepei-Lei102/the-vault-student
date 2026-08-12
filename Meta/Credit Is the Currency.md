---
chinese: 信用即货币 (xìnyòng jí huòbì)
prerequisites:
  - "[[Text Encoding]]"
leads_to: []
tags:
  - subject/methodology
  - subject/computer-science
  - domain/game-theory
  - domain/economics
  - domain/protocols
  - domain/character
  - level/A-Level
  - level/life
  - type/methodology
  - type/meta
  - type/cross-domain
  - misconception/strategy-means-concealment
  - misconception/money-has-intrinsic-value
---

# Credit Is the Currency 信用即货币

> 「好的兵法是让别人知道你下一步是什么，更好的兵法是让别人知道你的下两步是什么，最好的兵法是让别人知道你的下三步是什么。」
> *"Good strategy lets others know your next move. Better strategy lets them know your next two. The best strategy lets them know your next three."*
> — 庞统, in 陈某's manhua **《火凤燎原》** (*The Ravages of Time*)

## What this card is for

The line above should feel wrong. Everything we absorb about strategy — from playground games to war films — says *conceal*: hide your plans, keep them guessing, strike where they least expect. And here is a strategist ranking plans by how far ahead he *reveals* them, and calling the most transparent one the strongest.

The paradox dissolves into one idea, and the idea turns out to run computers, economies, friendships, and classrooms alike: **announced moves that always come true become a currency.** When your word reliably becomes fact, other people stop treating it as talk and start treating it as *terrain* — something they can build on before it even happens. That convertibility — word into accepted fact — is what the word **credit** literally means, and minting it is one of the most powerful things a person, an institution, or a machine can do.

The etymology is the thesis. **Credit** comes from Latin ***credere*** — *to believe*. And Chinese says it even more precisely: **信用 = 信 (trust) + 用 (use)** — *trust you can spend*. Both languages caught the same secret: belief, accumulated, becomes purchasing power.

## 中文锚点

**信用即货币 (xìnyòng jí huòbì)** — 核心论点：**说出的话每次都兑现，话就变成了货币。**

- **悖论**：庞统说最好的兵法是让敌人知道你的**下三步**。为什么最强的策略反而是最透明的？
- **解**：宣布并兑现的行动会铸造**信用**——别人开始把你的"下一步"当作**已成的事实**来规划。你的未来变成了他们脚下的地形。这就是**阳谋**：摆在明处也无法破解的计策。
- **词源即论点**：credit ← 拉丁语 *credere*（相信）；**信用 = 信 + 用** ——可以**花**的信任。
- **计算机是信用之塔**：时钟（"我每 0.3 纳秒滴答一次"——一颗芯片一生兑现约 $10^{18}$ 次）；ASCII（"65 就是 A"，一诺六十年）；IEEE 754（连**出错的方式**都全球统一）；文件头（每一个阅读器都遵守条约）；向后兼容（GBK 背着 GB2312 的每一个旧文件前行）。计算机里**没有任何东西靠强制运转**——全是被遵守的承诺。
- **经济学**：货币即制度化的信用（货币即信用）；钞票 = 发行者宣布的下几步 + 它的兑现记录；通胀 = 承诺的磨损；比特币 = 用**协议信用**替换**机构信用**。
- **博弈论的边界（诚实的边角）**：一次性零和博弈（扑克、点球）奖励**隐藏**；**重复正和博弈**奖励**可预测**（Axelrod 锦标赛：以牙还牙胜出，靠的是清晰）。分清你在玩哪种游戏。
- **学生版**：写出步骤 = 宣布你的行动，让阅卷人能给你**部分信用**——partial credit 字面意思就是"部分信用"；声誉 = 兑现记录；守住的截止日期是会**复利**的资本。

## The paradox, resolved — the three-move ladder

Read the quote as a ladder, one rung per announced move.

**One move announced and kept** buys tactical trust: allies coordinate with you this turn, opponents brace where you said you'd strike — and it lands anyway. **Two moves** buy planning: others now schedule *their* second move around your second move; your future has entered their calculations as a fixed point. **Three moves** and something qualitative happens: your declared intentions have become part of the *landscape*. Nobody wastes effort hedging against your word being false, any more than they hedge against the sun failing to rise. Friends invest in your trajectory. Rivals are reduced to reacting to a future you authored in public. You have stopped making *claims* and started issuing *currency* — and everyone has chosen to hold it.

Chinese strategy has a dedicated name for the summit of this ladder: **阳谋** — the *open* scheme, as opposed to 阴谋, the hidden one. An 阳谋 is a plan that works **even when the opponent sees it completely**, because the incentives are arranged so that every visible countermove costs more than compliance. Announcing it is not a leak; announcing it is the *mechanism*. The three-moves line is a definition of 阳谋 disguised as a boast — and the rest of the argument is about discovering that our most reliable machines, and our most reliable people, are built out of exactly this material.

![[credit-is-the-currency-three-moves-comic.png|697]]

## Exhibit A — a computer is a tower of kept promises

Here is the strangest fact in computer engineering, hiding in plain sight: **nothing inside a computer works by force.** No component can *compel* another to do anything. Every single interaction is one party honouring a declaration another party once made. The machine on your desk is not a mechanism in the clockwork sense — it is a **treaty stack**, billions of promises deep, and it works only because essentially all of them are kept, essentially all of the time.

Climb the tower:

- **The clock.** The oscillator announces one move, forever: *"I will tick again in 0.3 nanoseconds."* Every flip-flop in the chip ([[Flip-Flops]]) times its entire existence around that promise; whole clock domains negotiate their treaties around it ([[Clock Domains and Metastability]]). At 3 GHz over a ten-year life, that single promise is kept on the order of $10^{18}$ times. No human institution has ever approached this record — and the machine's whole architecture *assumes* it without checking, which is precisely what perfect credit lets you do.
- **Character sets.** *"65 means A."* ASCII announced that move in 1963, and it has come true every time anyone, anywhere, has decoded a byte since ([[Text Encoding]]). Your ability to read this sentence is that promise, being kept right now, several thousand times per line.
- **File headers.** A PNG's header declares its width, height, and depth, and **every image reader on Earth honours the declaration, every time** — which is the only reason a photo from a stranger's camera opens instantly on your phone ([[Image Encoding]]; the same treaty logic runs [[Sound Encoding]]'s headers). Bytes do not announce their own meaning, so the ecosystem runs entirely on announced meanings, kept.
- **IEEE 754.** The floating-point standard did something subtler than standardise arithmetic: it standardised the **errors**. Every machine rounds $0.1 + 0.2$ to the *same* wrong answer ([[Floating-Point Representation]]). Machines agree even on how to be wrong — because a predictable error is spendable (you can reason about it, compensate for it, reproduce it), while an unpredictable truth is not.
- **The handshake.** TCP opens every connection with announced moves — *I want to talk; I heard you; let us begin* — and the internet is two machines extending each other credit by the packet, retransmitting precisely when a promise slips.
- **Backward compatibility — the oath that cannot be broken.** GBK (1995) carried every GB2312 (1980) file forward unchanged; GB18030 (2000) still carries them today ([[Text Encoding]]'s 国标 story). A modern x86 chip will still run code written for a processor from 1978. Once billions of parties have built on your announced moves, *you no longer have the option of changing them* — the credit you minted has become a debt you service forever. That is not a design flaw. That is what it means for a promise to have been fully spent by its holders.

The generalisation writes itself upward, too. A **law of nature** is, in this vocabulary, the universe's own credit rating: *announced* in every experiment, *kept* without exception since the beginning of time — the one issuer that has never defaulted ([[Laws and Theorems]] — and the reason physics can deduce at all is that nature's word is good). Engineering is the practice of building on credit; science is the audit.

## The economics rung — money *is* institutionalised credit

Turn the thesis around and point it at money, and money confesses: **货币即信用** — currency is credit that grew up and got an institution.

A banknote is nothing but an issuer's announced next moves plus its track record of keeping them. The note in your pocket has no intrinsic value; it is a *promise that it will be accepted* — by shops, by banks, by the tax office — and its worth is exactly the market's confidence in that promise. When the promise erodes gradually, we call it **inflation**: same announcements, weakening conviction that they'll be honoured at yesterday's rate. When it collapses, we call it **hyperinflation**, and the wheelbarrows of Weimar banknotes are what a fully invalidated promise looks like as a physical object.

**Bitcoin** is the thesis's cleanest modern exhibit, because it is an explicit *swap of credit types*: distrusting institutional promise-keepers, it replaces them with **protocol credit** — moves announced *in code*, kept by consensus mathematics rather than by anyone's good behaviour. The 21-million-coin cap is an announced move number infinity; every amount is an exact integer count of satoshis precisely so that no floating-point ambiguity can smudge the ledger's promises ([[Floating-Point Representation]]'s exact-arithmetic lesson, deployed as monetary policy). Whether one *trusts* that swap is a live debate; that it **is** a swap of credit systems, not an escape from credit, is the point — there is no escape from credit. Every currency ever tried is a claim about someone's future moves.

## The game-theory rung — and the honest boundary

The twentieth century made 庞统's insight rigorous, twice.

**Thomas Schelling** (*The Strategy of Conflict*, 1960) showed that in bargaining and deterrence, power flows from **visibly binding yourself** — from *destroying your own options in public*. The general who burns his ships wins concessions no flexible general can extract, because his threat to stand and fight has stopped being talk and become terrain. And the commitment must be *announced* to work at all: *Dr. Strangelove*'s doomsday machine — wired to fire automatically, the perfect deterrent — fails and ends the world **because the Soviets kept it secret**. As the film's Strangelove wails: the whole point of the device is *lost* if you don't tell anyone. An unannounced move mints no credit. (In this card's language: a commitment is an announced move with the retraction physically removed — credit with collateral.)

**Robert Axelrod** (1980) ran the famous computer tournaments of the iterated prisoner's dilemma, and the winner — **tit-for-tat** — won not by cleverness but by *legibility*: it was **nice** (never defects first), **retaliatory** (answers defection at once), **forgiving** (returns to cooperation immediately), and above all **clear** — an opponent learns its next three moves after one round of play, and precisely *because* its future is transparent, cooperation with it becomes the opponent's best strategy. Predictability, not cunning, compounded into victory.

> [!warning] The honest edge — know which game you are in
> The theory also marks exactly where the thesis **stops**. In a **one-shot, zero-sum** game — a poker hand, a penalty kick, a single sealed-bid auction — concealment is not merely permitted, it is *mathematically prescribed*: the optimal mixed strategy is deliberately unpredictable, because there my gain is your loss and information given is advantage handed over. Nobody announces their next three penalty kicks.
>
> The 庞统 doctrine belongs to **iterated, positive-sum** games — the games where the players will meet again and can *build* something between them. That is where announced-and-kept moves compound; that is where credit is the currency. The boundary itself is the deepest lesson here: **most of life — collaboration, teaching, friendship, science, trade, family — is iterated and positive-sum, and most people play it with instincts trained on poker.** They conceal by default, hedge by default, keep options open by default — and are quietly out-competed by the people whose word is spendable. The rare true zero-sum moments deserve game faces. Everything else rewards being legible.

## The student rung — credit in the classroom

The thesis lands on schoolwork with almost embarrassing precision.

- **"Show your working" is a credit application.** A bare final answer asks the marker for total trust; worked steps *announce your moves* so the marker can verify each one and extend you **partial credit — which is literally partial *credit***, the word in its exact monetary sense. The mark scheme is a promise the examiner announced first; showing your working is you announcing back. The transaction is credit in both directions.
- **Reputation is a track record of announced moves.** The student who says "I'll have it by Friday" and does — every time — discovers that teachers, teammates, and eventually employers begin building on their word *before the work exists*. That is 信用 being spent. And the compounding is real: each kept deadline makes the next announcement worth more.
- **Trust is cached verification.** The first hundred times, your working is checked line by line. Then something changes: your announced results start being *accepted unverified* — your word has been promoted from claim to fact. In computing terms, credit is a **cache**: expensively verified once, cheaply trusted thereafter. And it inherits the cache's brutal failure mode — **one broken promise invalidates the whole cache**, and rebuilding it costs the full original price plus suspicion. This asymmetry (slow to mint, instant to destroy) is not unfair; it is what makes the currency worth holding.
- **The strongest study partnership is an 阳谋.** "I will know this chapter by Tuesday; test me" — announced, checkable, kept — outperforms every private resolution, for Schelling's exact reason: the public announcement burns the ships. ([[Inertia and Bootstrapping]] holds the mechanics of actually starting; [[The Feynman Technique]] holds the test of whether the chapter is truly known.)

## Honest edges

**The quote is fiction — and better for being read as fiction.** The three-moves line belongs to Chan Mou's *drawn* 庞统 in 火凤燎原, not to the historical strategist of the Three Kingdoms, and the manhua's whole universe runs on schemes nested inside schemes — announced moves that are themselves feints around deeper announced moves. Take it as a distilled aphorism from a great work of strategy fiction, in the same spirit the vault takes physics thought experiments: true as a *shape*, not as a biography.

**Credit can be weaponised, because it is real.** Every confidence trick is a credit operation — the word *con* is short for *confidence*. A Ponzi scheme mints genuine credit by keeping small promises punctually (early investors really are paid) precisely to steal on the strength of the accumulated trust. This does not weaken the thesis; it confirms it — counterfeiting only pays in a currency that has value. The defence is the auditor's habit: track *announced moves versus outcomes* over time, and weight the record above the announcement. Forward-read the causality, not the charisma ([[Forward Reading and Problem Discovery]]).

**Transparency is not an unconditional virtue.** Beyond the zero-sum boundary above: some things — privacy, others' secrets, options genuinely worth preserving — should not be announced, and a *commitment* in Schelling's sense is a weapon you point at your own future self, to be drawn rarely. The claim is not "reveal everything"; it is "in repeated positive-sum games, **let your kept word do the compounding** — and be the kind of player whose announcements are worth building on."

## Connections

- **Prerequisite:** [[Text Encoding]] — the treaty thesis in its original habitat: text works because "65 means A" was announced once and kept forever. The whole multimedia arc ([[Image Encoding]], [[Sound Encoding]]) runs on the same declared-and-honoured headers.
- **The silicon exhibits:** [[Flip-Flops]] + [[Clock Domains and Metastability]] — the clock's $10^{18}$ kept ticks, and what the seams between promise-domains cost; [[Floating-Point Representation]] — IEEE 754 standardising even the errors, and the exact-integer discipline Bitcoin borrows.
- **Epistemology sibling:** [[Laws and Theorems]] — a law of nature as the universe's perfect credit record; physics as deduction built on the one word that has never been broken.
- **Methodology siblings:** [[Forward Reading and Problem Discovery]] — auditing credit *is* forward reading applied to people and institutions (trace announced moves to outcomes); [[The Feynman Technique]] — teaching as the announced move that proves the understanding exists; [[Inertia and Bootstrapping]] — the public announcement as activation-energy hack.
- **The founder:** [[Stories/von Neumann the Martian]] — game theory itself (1928/1944) is his mathematics; Schelling and Axelrod built the commitment-and-cooperation wing on his foundation.
- **Philosophy floor:** [[The Love of Wisdom]] — that card asks why we reach; the reaching becomes *shared* the moment we announce it and keep our word about it. Credit is how incomplete beings compose into something larger than any of them.
