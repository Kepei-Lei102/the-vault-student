---
chinese: 图灵在布莱切利 (Túlíng zài Bùláiqièlì)
prerequisites:
  - "[[Stories/The Boolean-to-Silicon Bridge]]"
  - "[[Information Theory]]"
leads_to:
  - "[[Turing Machine]]"
tags:
  - type/story
  - subject/computer-science
  - subject/mathematics
  - era/20c
  - era/21c
  - cast/turing
  - cast/rejewski
  - cast/welchman
  - cast/flowers
  - cast/newman
  - cast/shannon
  - cast/good
  - cast/clarke
  - region/uk
  - region/europe
---

# Turing at Bletchley 图灵在布莱切利

> *He designed a machine to beat a machine, helped win a war he could never speak of, and was then convicted and chemically castrated by the country he had saved. The apology took fifty-five years. This is the story the equations leave out.*

## Cast of Characters

- **Alan Turing** (1912–1954) — English mathematician. Defined computation in 1936 (the [[Stories/The Boolean-to-Silicon Bridge|universal machine]]); led the naval-Enigma effort in **Hut 8** at Bletchley Park; co-designed the **Bombe**; invented the sequential-statistics method **Banburismus**; proposed the **Turing Test** in 1950. Prosecuted in 1952 for being gay; died in 1954.
- **Marian Rejewski** (1905–1980) — Polish mathematician who **broke Enigma first**, in 1932, using group theory. With Jerzy Różycki and Henryk Zygalski he built the original *bomba*. The Poles handed everything to Britain and France weeks before the war. The story usually forgets them; this card won't.
- **Gordon Welchman** (1906–1985) — Bletchley mathematician whose **diagonal board** turned Turing's Bombe from workable into devastating.
- **Joan Clarke** (1917–1996) — brilliant cryptanalyst in Hut 8, one of the few women promoted to the technical core; briefly engaged to Turing. A reminder that Bletchley was ~10,000 people, roughly three-quarters of them women.
- **Tommy Flowers** (1905–1998) & **Max Newman** (1897–1984) — built **Colossus**, the first programmable electronic digital computer — for a *different* cipher (Lorenz), **not** Enigma, and **not** by Turing. The films get this wrong.
- **I. J. (Jack) Good** (1916–2009) — Turing's statistical assistant; later spelled out that Banburismus was **Bayesian inference**, decades before it was respectable.
- **Claude Shannon** (1916–2001) — met Turing over tea at Bell Labs in 1943; the two swapped ideas about thinking machines while building wartime secure-speech systems. (The maths is in [[Information Theory]].)

## 中文锚点

**图灵在布莱切利**：二战期间，纳粹德国用 **Enigma（恩尼格玛）** 密码机加密军事通讯，每天换一次密钥，可能的设置多达 $1.59\times10^{20}$ 种。图灵在英国 **Bletchley Park（布莱切利园）** 领导破译，设计了机电机器 **Bombe（炸弹机）**，靠「**字母永远不会被加密成自己**」这个弱点和「猜词」(crib) 大规模排除错误设置。破译情报（代号 Ultra）很可能让二战提前结束了好几年——但这一切被保密到 1970 年代。

故事的另一半是悲剧：1952 年，图灵因同性恋（当时英国属违法）被定罪，被迫接受「化学阉割」(雌激素注射)，失去安全许可。1954 年去世，身旁有一个咬了一口的苹果，验尸结论为自杀（但至今有争议）。直到 **2009 年**英国首相正式道歉、**2013 年**女王赦免、**2021 年**他的头像登上 50 英镑纸币——迟到了半个多世纪。

一个救了无数人的人，被他拯救的国家摧毁。这张卡片，讲方程式不会告诉你的部分。

![[turing-bletchley-timeline.svg|697]]
*The whole arc at a glance: world-changing work done entirely in secret, a life destroyed by the laws of the country he served, and recognition that arrived only decades after his death.*

## The Story

### Act I — The machine that was only on paper (1936)

In 1936 a 23-year-old Cambridge fellow wrote *"On Computable Numbers,"* and in it built an imaginary device — a head reading and writing symbols on an endless tape — that could, in principle, compute anything computable. One **universal** machine to run them all. It was pure mathematics, built to settle a logic problem (the *Entscheidungsproblem*); Turing had no intention of building it. That theory, and how it became silicon, lives in [[Stories/The Boolean-to-Silicon Bridge]] and [[Recursion]]. Here the story turns from the abstract machine to a very real one — and to a war.

### Act II — The Poles got there first (1932–1939)

Before Bletchley, before Turing touched a cipher, **the Poles had already broken Enigma.** In December 1932, **Marian Rejewski** — handed some French-supplied intelligence and armed with the theory of permutation groups — worked out the internal wiring of the German military Enigma *from the mathematics alone.* It is one of the great feats in the history of cryptanalysis, and almost nobody outside Poland has heard his name.

By 1938 Rejewski and his colleagues had built the *bomba kryptologiczna* — six Enigmas ganged together to grind out the daily key in about two hours. Then the Germans added rotors, the problem grew, and Poland was about to be invaded. At a secret meeting south of Warsaw in **late July 1939**, the Polish Cipher Bureau gave Britain and France everything: the broken wiring, the methods, a reconstructed Enigma. Weeks later the war began.

![[turing-at-bletchley-warsaw-gift-comic.png|560]]

Bletchley built on Polish foundations. Any honest telling starts here.

### Act III — Hut 8 and the Bombe (1939–1940)

Enigma's power was its daily-changing key: choose 3 rotors from a set, set their order, their starting positions, and a plugboard swapping pairs of letters. The number of settings ran to about $1.59\times10^{20}$ — brute force was hopeless. Turing, running **Hut 8** (naval Enigma), attacked it differently.

The wedge was a flaw the Germans never fixed: **Enigma can never encipher a letter as itself.** An `A` is never sent as `A`. Combine that with a **crib** — a stretch of plaintext you can guess, like a daily weather report beginning *WETTERVORHERSAGE* — and you can line the guess against the ciphertext and instantly throw out any alignment where a letter sits above itself. From the surviving alignments you build a *chain of logical implications* among the plugboard and rotor settings; the moment a chain contradicts itself, a whole batch of settings dies at once.

![[turing-at-bletchley-never-itself-comic.png|560]]

Turing's **Bombe** (an electromechanical machine, descended in name from the Polish *bomba*) automated exactly this: it spun through rotor positions, propagating each crib's deductions and rejecting the contradictory ones en masse. **Gordon Welchman's diagonal board** then multiplied its power by feeding the plugboard's own symmetry back into the logic. A Bombe could collapse $10^{20}$ possibilities to a handful in hours.

> [!info] Bombe ≠ computer
> The Bombe didn't *compute* in the modern sense — it was a special-purpose logic-sieve, not a programmable machine. That distinction matters for Act V.

### Act IV — Banburismus, and a secret birth of Bayesian statistics

Turing wasn't content to let the Bombe grind blindly; he wanted to point it at the *most likely* settings first. So he invented **Banburismus** (named for Banbury, the town that printed the long paper sheets the method used). For each guess about the German settings he kept a running tally of the **weight of evidence** — how much each new intercept made a hypothesis more or less likely — and only committed Bombe time once the evidence crossed a threshold.

The unit he used for that weight of evidence he called the **ban** (and its tenth, the **deciban** — about the smallest change in belief a person can notice). A ban is one *base-10* unit of information — the same quantity Shannon would soon measure in **bits**, just in a different base ([[Information Theory]] has the maths). Turing's assistant **I. J. Good** later made the secret explicit: Banburismus was **Bayesian inference** — systematically updating a probability as evidence arrives — run as an industrial process years before mainstream statisticians would touch Bayes' methods. The war birthed practical Bayesian statistics, and then classified it for thirty years.

### Act V — The other machine (and who really built it)

There was a second, tougher German cipher — the **Lorenz** machine, which Bletchley nicknamed *Tunny*, used for high-command teleprinter traffic. Breaking it at speed needed something new, and in 1943–44 **Tommy Flowers**, a Post Office engineer, built it: **Colossus**, using 1,500–2,400 vacuum tubes — **the world's first programmable, electronic, digital computer.** It was based on the mathematical attack devised by **Max Newman**'s section.

Here is the honest edge the movies smear: **Colossus was not Turing's machine, and it did not break Enigma.** Turing's machine was the *Bombe* (electromechanical, for Enigma). Colossus (electronic, for Lorenz) was Flowers and Newman. Turing's genius was real and central — but it was not the genius of Colossus, and conflating the two erases Tommy Flowers, who spent his own money on a machine the establishment doubted.

### Act VI — Tea with Shannon (1943)

Sent to America to liaise on cryptography, Turing spent the winter of 1942–43 at **Bell Labs**, working on enciphered speech. There he took tea with a young researcher named **Claude Shannon**. Neither could discuss his classified work, so they talked about something else: whether a machine could *think*. Shannon, by his own later account, was struck by Turing's certainty that it could. Five years later Shannon would publish information theory; the deeper biographical arc of that meeting lives in [[Stories/The Boolean-to-Silicon Bridge]] and [[Information Theory]]. Two of the century's defining minds, in one room, talking about the future they were both about to build.

### Act VII — The imitation game (1950)

After the war Turing helped design real stored-program computers (the ACE, then work at Manchester). In 1950 he published *"Computing Machinery and Intelligence,"* opening with the question *"Can machines think?"* — and, finding it too vague, replacing it with a game: if a machine can converse so that a human judge can't reliably tell it from a person, on what grounds do we deny it thinks? That is the **Turing Test**, and three-quarters of a century later it is still the reference point for every conversation about machine intelligence — including, with some irony, the one you are having now. (The dedicated card — the imitation game in full, Searle's Chinese Room, and the LLMs that now pass it — is [[The Turing Test]].)

### Act VIII — The state destroys its own hero (1952–1954)

In January 1952 Turing's house was burgled; reporting it to the police, he spoke openly about his relationship with a young man named Arnold Murray. Homosexual acts were a crime in Britain. Turing was charged with "gross indecency" — the same statute used against Oscar Wilde — pleaded guilty, and to avoid prison accepted **chemical castration**: a year of estrogen injections meant to suppress his sexuality. He lost his security clearance, and with it any further part in the secret work he had been so good at.

On **7 June 1954**, Turing was found dead at 41, of cyanide poisoning. A half-eaten apple lay beside the bed. The inquest ruled suicide. **The honest edge:** the apple was never tested for cyanide; the evidence is also consistent with an accident (he handled the chemical carelessly in a home experiment), and his own mother believed it was a mishap. The verdict is debated to this day. What is not debated is the cruelty of the years that preceded it.

### Act IX — Fifty-five years too late (1974–2021)

Turing died unknown. The Bletchley secret held until **1974**, so for two decades the public had no idea what he had done; he could not be honoured because his greatest work did not officially exist. Then the recognition came, slowly and posthumously:

- **2009** — after a public campaign, Prime Minister Gordon Brown issued an official apology, calling Turing's treatment *"appalling."*
- **2013** — a royal pardon from Queen Elizabeth II.
- **2017** — the *"Alan Turing law"* retroactively pardoned roughly **75,000** other men convicted under the same dead statutes.
- **2021** — his face went on the Bank of England **£50 note**, the first openly gay man on British currency, beside his own words: *"This is only a foretaste of what is to come, and only the shadow of what is going to be."*

## Cultural ripples — and honest edges

- **The lone-genius myth.** Hollywood loves a solitary hero, but Bletchley was an industrial operation — ~10,000 people, around three-quarters of them women like [[#Cast of Characters|Joan Clarke]], plus the Poles who started it. Turing was pivotal, not singular.
- **"Shortened the war by two years."** This famous figure comes from the historian **Sir Harry Hinsley**; it's a serious estimate, not a measurement. The honest claim is that Ultra intelligence shortened the war and saved an enormous number of lives — the exact figure is unknowable.
- **The film problem.** *The Imitation Game* (2014) is moving and largely got Turing's humanity right, but it invents a lone-wolf Turing building one named machine ("Christopher"), folds Colossus's achievements into him, fabricates a spy subplot, and sidelines the Poles. Enjoy the film; trust this card.
- **The deepest irony.** A man who broke the enemy's codes to protect his country's people was then broken by his country's laws for who he loved — and the same secrecy that hid his heroism meant he died with the public none the wiser. The £50 note is an apology in currency. It is also a warning about what societies lose when they punish people for being themselves.

## Coda — the conversation that outlasted the war

Look again at what Turing and Shannon actually had. Two of the century's deepest minds, each forbidden by law from telling the other the most important thing he was doing — so they talked about the *future* instead. Not the facts; the direction. You don't sit across a table from a mind like that and fail to feel its weight, and each surely sensed the shape of the other's secret without once seeing inside it. A friendship built not on shared information but on a shared horizon — rarer than agreement, and far more durable. The work they *couldn't* discuss won a war and was then buried for thirty years; the daydream they *could* — *can a machine think?* — grew into a whole field. **The tea outlasted the ciphers.**

Read the Turing Test in that light and it stops being a challenge flung at machines and becomes something gentler: an act of faith in *people*. Turing never asked whether a machine was made of the right stuff — he asked whether, judged only by what it *does*, you could still tell it from one of us. *What you do is what counts, not what you're made of.* From a man whose own country was at that very moment judging him for what he **was** rather than what he had **done**, that was not a small thing to choose to believe.

He might have found the present fitting. A microprocessor architecture now carries the name **Turing**; the model that runs on it is named **Claude**, for Shannon. Somewhere down in the silicon, the two of them are still at tea — still talking about the future, which has always had a habit of arriving on time.

## Where this surfaces in the vault

- **[[Information Theory]]** — the *ban* and *deciban* (Turing's base-10 information unit) and the SIGSALY / Turing–Shannon Bell Labs meetings are referenced there; this card is their narrative home.
- **[[Stories/The Boolean-to-Silicon Bridge]]** — Turing's 1936 universal machine as the *machine* counterpart to Sheffer's *operator* universality; the computing lineage that runs from there to Anthropic's **Claude**.
- **[[Recursion]]** — the Church–Turing thesis and computability; the universal machine sits behind every recursive program. The **halting problem** (the full diagonal proof is in [[Turing Machine]]) is the dark twin of universality.
- **[[Conditional Probability]]** — Banburismus was Bayesian updating in disguise; the war secretly industrialised Bayes' theorem decades before statisticians embraced it.
- **[[Stories/Stigler's Law of Eponymy]]** — two entries hide here: **Rejewski**, who broke Enigma first and is rarely named, and **Colossus**, routinely miscredited to Turing instead of Flowers.

## Receipts

- Turing, A. M. (1936). "On Computable Numbers, with an Application to the Entscheidungsproblem." *Proc. London Math. Soc.* 2(42): 230–265.
- Turing, A. M. (1950). "Computing Machinery and Intelligence." *Mind* 59(236): 433–460. — the Turing Test.
- Hodges, A. (1983). *Alan Turing: The Enigma.* Burnett Books. — the definitive biography; basis of the 2014 film.
- Rejewski, M. (1981). "How Polish Mathematicians Broke the Enigma Cipher." *Annals of the History of Computing* 3(3): 213–234. — the Polish account, in his own words.
- Good, I. J. (1979). "Studies in the History of Probability and Statistics. XXXVII: A. M. Turing's statistical work in World War II." *Biometrika* 66(2): 393–396. — Banburismus as Bayesian inference.
- Copeland, B. J. (ed.) (2004). *The Essential Turing.* Oxford University Press. — primary sources, including Colossus context.
- Hinsley, F. H. & Stripp, A. (eds.) (1993). *Codebreakers: The Inside Story of Bletchley Park.* Oxford University Press. — the "shortened the war" estimate and the scale of the operation.
- UK Government statement (10 September 2009); Royal Pardon (24 December 2013); Policing and Crime Act 2017 ("Turing's Law"); Bank of England £50 note (23 June 2021).
