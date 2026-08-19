---
chinese: 指向另一边的箭头 (zhǐxiàng lìng yībiān de jiàntóu) — 赋值符号的跨洋之争
prerequisites:
  - "[[Arrays]]"
  - "[[Cambridge Pseudocode]]"
leads_to: []
tags:
  - type/story
  - subject/computer-science
  - era/20c
  - era/21c
  - cast/zuse
  - cast/rutishauser
  - cast/bauer
  - cast/backus
  - cast/iverson
  - cast/falkoff
  - cast/thompson
  - cast/ritchie
  - cast/van-rossum
  - region/europe
  - region/usa
---

# The Arrow That Pointed the Other Way 指向另一边的箭头

> *`x = x + 1` is false. No number equals itself plus one. Every programmer alive has typed it anyway — and there was a fight, across an ocean and then across sixty years, about whether we should have to.*

## Cast of Characters

- **Konrad Zuse** (1910–1995) — a Berlin civil engineer who built programmable computers in his parents' living room, and in 1945 wrote the first high-level programming language for a machine that had just been bombed. He drew the assignment arrow pointing **right**.
- **Heinz Rutishauser** (1918–1970) — ETH Zurich; kept Zuse's direction in his *Superplan* (1951) and carried it to the negotiating table.
- **Friedrich L. Bauer** (1924–2015), **Klaus Samelson** (1918–1980), **Hermann Bottenbruch** — with Rutishauser, the European delegation at Zurich, 1958 — sent by the GAMM, the German-speaking Society for Applied Mathematics and Mechanics.
- **John Backus** (1924–2007) — leader of Fortran, whose `=` the Americans brought to Zurich; with **Alan Perlis**, **Charles Katz** and **Joseph Wegstein**, the American delegation — sent by the ACM, the Association for Computing Machinery.
- **Kenneth Iverson** (1920–2004) and **Adin Falkoff** (1921–2010) — APL; the arrow that pointed **left**, and needed its own typeface to be written at all.
- **Ken Thompson** (b. 1943) and **Dennis Ritchie** (1941–2011) — Bell Labs; B and C; the men who took a character away and gave the world its `=`.
- **Guido van Rossum** (b. 1956) — Python's "Benevolent Dictator For Life", who in 2018 accepted the 1958 compromise symbol into his language and resigned within days.

## 中文锚点

赋值符号——把一个值**放进**一个变量——用什么写？这个问题在计算机史上从来没有共识，而且真的吵过架。中文的"**赋值**"二字自带方向：赋予一个值，值流向变量。英文的 `=` 却借用了"等于"，于是 `x = x + 1` 成了每个初学者遇到的第一句"假话"。故事从楚泽（Zuse）1945 年的右指箭头 `Z + 1 ⇒ Z` 开始（先算、后存，机器的顺序），经过 1958 年苏黎世 ALGOL 会议上欧美两派的争执与妥协 `:=`，Fortran 的 `=`，艾佛森（Iverson）需要定制打字球才能打出的 `←`，贝尔实验室把 `:=` 削成 `=`（代价是 `if (x = 5)` 悄悄编译通过），最后到 2018 年：Python 之父吉多（Guido van Rossum）为"海象运算符" `:=` 力排众议之后宣布辞去终身仁慈独裁者——1958 年为结束一场争吵而选出的符号，六十年后又引发了另一场。剑桥考试的伪代码用 `←`，站在了当年输掉的那一边。

## The Story

### Prologue — the sentence that is false

The first lie a programmer is asked to swallow arrives on day one: `x = x + 1`. In arithmetic it is simply false, and every student who has just been taught to solve equations notices. The teacher waves it off — *it doesn't mean equals here, it means put the right side into the left* — and the class moves on, having learned that in this new subject the symbols do not mean what they mean.

But that is not a law of nature. Somebody *chose* to write "equals" when they meant "put". Somebody else thought that was a terrible idea and drew an arrow instead. They argued about it in a room in Zurich, and the argument is not over: the second bug most beginners write in Python (after the off-by-one) is `if x = 5:` — a slip that exists *only* because of the choice this story is about. And on the Cambridge exam paper the assignment is written `x ← 5`, an arrow — the losing side's symbol, still in service.

### Act I — Berlin, 1945: the arrow pointed the other way

Konrad Zuse built his first computers between 1936 and 1941 in the living room of his parents' flat in Berlin, out of relays salvaged from telephone exchanges. The Z3 of 1941 was the first working programmable, fully automatic digital computer in the world; it computed wing flutter for the Henschel aircraft works, which is to say it was paid for by the war and worked for it, and Zuse never pretended otherwise. In December 1943 an Allied raid destroyed the Z3. By 1945 he had fled Berlin with the successor machine, the Z4, and was hiding it in a barn in Hinterstein, a village in the Bavarian Alps, waiting to see who would arrive first.

In that village, with no computer to run it on, he wrote a programming language.

The **Plankalkül** — the "plan calculus" — was the first high-level language ever designed: variables, conditionals, loops, subroutines, even data structures, on paper, in 1945. And its assignment was written like this:

$$Z + 1 \;\Rightarrow\; Z$$

Zuse called the double arrow the *Ergibt-Zeichen*, the **yields sign**. Read it aloud and it is a sentence: *Z plus one yields Z*. The expression sits on the **left**, the destination on the **right** — because that is the order in which the machine does it. First compute, then store. The data flows left to right, and the arrow points where the data goes.

Nobody ran the Plankalkül for a very long time. Zuse published fragments in 1948 and the whole in 1972; the first implementation was a doctoral dissertation in 1975. It was a language for a machine that had been bombed, written by a man walking away from a war, and it sat unexecuted for thirty years. But the arrow had been drawn, and it had been drawn pointing right.

Heinz Rutishauser at ETH Zurich picked the direction up in his *Superplan* of 1951 — a system for having the machine write its own computing plans, one of the earliest compilers in all but name — and through him the right-pointing arrow became the European habit. It was, everyone on that side of the Atlantic agreed, simply the natural way to write down what happens.

### Act II — Zurich, 27 May to 2 June 1958: eight men and one arrow

By 1958 there were programming languages on both continents, none of them shared, and two learned societies decided to fix it. On the American side, the **ACM** — the *Association for Computing Machinery*, founded in 1947 and still the profession's main society (its Turing Award is computing's Nobel). On the European side, the **GAMM** — the *Gesellschaft für Angewandte Mathematik und Mechanik*, the German-speaking Society for Applied Mathematics and Mechanics, founded in 1922, whose members were the mathematicians and engineers actually building Europe's early machines. Note the asymmetry in the names: one society is *for computing*, the other *for applied mathematics* — which is a fair summary of who arrived thinking about machines and who arrived thinking about notation. The two would meet and design a *universal* algorithmic language. Four men from each side sat down at ETH Zurich for a week — Bauer, Bottenbruch, Rutishauser and Samelson for Europe; Backus, Katz, Perlis and Wegstein for America. What came out was ALGOL 58, the ancestor of Pascal, Ada, and the exam pseudocode you write, and of the whole idea that a language should be designed rather than grown.

And they fought about the arrow.

The Europeans wanted assignment written the Zuse–Rutishauser way — Peter Naur's later account of the European side puts the case as it was argued: the natural flow of computation is a notation of the form *b + 7 → z*. Compute, then store; arrow pointing at the destination. The Americans wanted it the other way round. They arrived, Naur wrote, with preconceptions formed by their experience of Fortran — where the destination came first and the sign between was `=`.

![[assignment-arrow-zurich-comic.png|720]]

The compromise was `:=` — read *becomes* — with the destination on the left, as the Americans wanted, and a symbol that at least was not the equals sign, as the Europeans insisted. It has been suggested since, politely, that the Europeans were simply out-pressured. ALGOL 60 kept it; Pascal, Modula, Ada, and later Go inherited it. **Every `:=` and every `=` you will ever type has the destination on the left, which is the way the losing side didn't want it.**

One more thing about ALGOL is worth carrying away, because it explains something on your own exam paper. ALGOL was designed with a **publication language** — a form of the notation meant to be *printed*, in journals and textbooks, with real subscripts and real arrows, separate from whatever a given machine could actually read. The idea that a program can be a piece of writing before it is a piece of software is ALGOL's; and [[Cambridge Pseudocode]] is a publication language in exactly that sense — a notation designed to be read by an examiner, not run by a computer.

### Act III — Fortran's `=`, and the lie sold as a resemblance

Why did the Americans want the destination first with an equals sign between? Because of what Fortran was for. **FOR**mula **TRAN**slation, 1957, John Backus's team at IBM: a language whose entire pitch to sceptical engineers was that a program would look like the formulas they already wrote. `AREA = 3.14159 * R ** 2` looks like a formula, and that resemblance sold the language.

The resemblance was a lie about one line in every program: `X = X + 1`. As arithmetic it is false; as an instruction it is fine; and Fortran had chosen a symbol that means the first thing to write the second. Inside Fortran itself the choice was safe enough — the early language had no equality test at all (a comparison was done by an "arithmetic IF" that jumped on the sign of a number; the relational `.EQ.` only came years later), so `=` had the sign to itself. The confusion was never the machine's. It was reserved for humans, and it has been paid by every beginner since.

### Act IV — Iverson's arrow, and the typeface that came before the language

Kenneth Iverson taught at Harvard from 1957 to 1960 and grew impatient with mathematical notation for describing procedures. He invented his own, published it as *A Programming Language* in 1962, and wrote assignment as an arrow pointing **left**:

$$z \leftarrow b + 7$$

Destination first, as the Americans had wanted — but an *arrow*, so that the sentence says what it does: the value flows into the box, and the arrow points at the box. This is the arrow on your exam paper. Zuse's arrow reversed, and made honest.

Now the best physical detail in this story. When Iverson and Adin Falkoff took the notation to IBM, they wanted programmers to type it as written — every arrow, every Greek letter, every rho and iota. The IBM Selectric typewriter carried its characters on a swappable golf ball; Falkoff and Iverson had two custom APL typeballs, numbers 987 and 988, designed in **late 1964** — before any computer existed that could run APL. The typeface was manufactured before the language ran, which it first did in 1966. And a Selectric ball holds only 88 characters, so the notation overflowed it: several APL symbols could only be produced by typing one character, backspacing, and striking a second over the top of it. A notation so committed to being right that it needed custom hardware to be written down.

The arrow then lost a seat it had briefly held. The 1963 edition of ASCII — the character treaty in [[Text Encoding]] — included a left arrow at code 95 and an up arrow at code 94. The 1967 revision evicted both, replacing them with the underscore `_` and the caret `^`. Every keyboard since has had `_` and `^` where two arrows used to be, which is why Smalltalk-80, a language that wanted Iverson's arrow, typed an underscore and drew it as `←` in its own fonts, and why the honest symbol was, from that year on, one you could not type on an ordinary terminal.

### Act V — Bell Labs, 1969: Thompson takes a character away

The lineage that produced C is a story of cutting things out. CPL (1963) was so ambitious it was never fully built; Martin Richards cut it down to BCPL (1967), which used `:=` for assignment; and in 1969, on a cast-off PDP-7 at Bell Labs, Ken Thompson cut BCPL down further into **B** — and while he was at it, cut the colon. Assignment became `=`. Equality, which now needed a symbol, became `==`. The reasoning, as it has come down: assignment is about twice as frequent as equality testing in ordinary programs, so its operator should be half as long.

Dennis Ritchie kept the choice when B became C in 1972, and in his own history of the language, written twenty years later, listed it among the fiddles made "as a matter of taste" and admitted, mildly, that some of them "remain controversial" — this one first. In the same paper he records another consequence of squeezing symbols together: B and early C wrote `x =+ 1` for *add one to x*, and `x=-1` was then ambiguous between *x becomes minus one* and *subtract one from x*, so the operators were flipped to `+=` and `-=`.

The price of the missing colon was a bug that compiles. `if (x = 5)` in C does not compare; it *assigns* 5 to x and then tests the 5, which is true, forever. It is silent, it is legal, and it is common enough to have folk remedies: programmers taught each other to write `if (5 == x)` — constant first — so that a slipped `=` becomes `5 = x`, which no compiler will accept, because you cannot assign to the number five. The habit is called **Yoda conditions**, because it reads the way Yoda talks: not *if x equals five* but *if five, equal to x, it is*. Ugly, backwards, and safe — like most folk remedies — and every modern compiler now carries a warning for the original slip, so the little green grammarian is slowly being retired. C's descendants — C++, Java, JavaScript, and Python — all inherited the `=`, and with it the bug's cousin, `if x = 5:`, which Python refuses to compile precisely because Guido van Rossum had seen where the C version leads.

### Act VI — 12 July 2018: the compromise comes home and costs a man his job

Python's assignment had always been a *statement*, not an expression — you could not assign in the middle of a condition, and that was deliberate: it made the C bug impossible. In 2018 a proposal, PEP 572, asked for **assignment expressions**: a way to bind a name inside an expression, for the cases where writing it any other way meant computing something twice. It needed a symbol that could not be mistaken for `=`. The proposal chose `:=`.

The ALGOL sign. Zurich's compromise, sixty years on, chosen for exactly Zurich's reason — it is not the equals sign — and immediately nicknamed the **walrus**, because sideways it has eyes and tusks — tilt your head to the left and the colon is the two eyes, the equals sign the two tusks.

![[assignment-arrow-walrus-comic.png|520]]

The argument that followed was the worst in the language's history — months of it, hundreds of messages, and unusually personal. Van Rossum, who had guided Python by consensus-and-final-say for twenty-seven years, accepted the PEP in early July. On 12 July 2018 he posted a message titled *Transfer of power* to the core developers. He did not want, he wrote, to have to fight that hard for a proposal again and find that "so many people despise my decisions"; he was removing himself from the decision process entirely; he named no successor and left the community to decide whether it wanted a democracy, an anarchy, a dictatorship or a federation. He ended: "I'm tired, and need a very long break."

The community wrote itself a constitution — PEP 8016 — and in early 2019 elected a five-person steering council to do what one man had done; he sat on the first one and then stepped back. Python 3.8 shipped in October 2019 with `:=` inside it. The two characters chosen at a table in Zurich to end one fight had, on their return, ended a reign.

### Epilogue — what the arrow was for

It is tempting to file all this under taste. It is not. Notation decides **what a reader can be fooled about**, and the two symbols fool you about different things.

`=` invites you to read an assignment as a statement of fact — and it hides a question. Write `b = a` for two arrays and it looks like a claim that they are equal, which quietly stops you asking the only thing that matters. The arrow cannot hide it. `b ← a` reads as *put what is in `a` into `b`*, and the honest reader is forced to ask: **what actually is in `a`?** The answer, for an array, is its address, not its contents — copy the address and both names now point at one block of memory. That aliasing insight in [[Arrays]] is not helped by `=`; it is *asked for* by `←`.

Chinese has had the direction all along. 赋值 — *bestow a value* — is a verb with a recipient; nobody reading it thinks it means *equals*. English computing had to fight for sixty years to say something a two-character word already said.

And the exam board sided with the losers. Every algorithm you write in the Cambridge papers uses `←`: Iverson's arrow, Zuse's direction reversed, the symbol that lost the room in 1958 and lost its seat in ASCII in 1967. It survived because it is *right* — it points where the value goes — and being right, it turns out, is a slow way to win, but not a hopeless one.

## Cultural ripples

- **The exam arrow.** [[Cambridge Pseudocode]] writes `Total ← 0`, and its one non-negotiable rule — `←` for assignment, `=` for comparison only — is this story compressed to a table row.
- **`:=` lives on** in Pascal, Ada, and Go, where `x := 5` declares-and-assigns; and in Python's walrus.
- **`<-` in R**, inherited from S at Bell Labs, which took it from APL — the left arrow surviving as two ASCII characters because the real one had been evicted.
- **Yoda conditions**, `if (5 == x)` — *if five, equal to x, it is* — and the compiler warning for assignment-in-a-condition: engineering scar tissue from Thompson's missing colon.
- **The word "becomes"** — how ALGOL programmers pronounced `:=`, and still the best way to read `=` aloud to a beginner: *x becomes x plus one* is true.
- **The steering council** that governs Python today exists because of a fight about two characters.

## Where this surfaces in the vault

- [[Arrays]] — the aliasing section, where `b ← a` forces the question `=` hides.
- [[Cambridge Pseudocode]] — the exam's publication language, using Iverson's arrow.
- [[Text Encoding]] — ASCII 1963 and its 1967 revision, where the arrows lost their seats to `_` and `^`.
- [[Compilers and Interpreters]] — the translators whose lineage (BCPL → B → C) is Act V.

## Receipts

- Zuse, K., *Der Plankalkül* (written 1945; published in full 1972) — the *Ergibt-Zeichen* and `Z + 1 ⇒ Z`. Knuth, D. E. and Pardo, L. T., "The Early Development of Programming Languages" (Stanford, 1976) — Plankalkül, Superplan, and the pre-ALGOL notations side by side.
- Naur, P., "The European Side of the Last Phase of the Development of ALGOL 60", in *History of Programming Languages* (ACM, 1978) — the Zurich meeting, the American contingent's Fortran preconceptions, and the *b + 7 → z* argument. Meeting dates and delegates per the ALGOL 58 record (ACM–GAMM, ETH Zurich, 27 May–2 June 1958).
- Backus, J. W. et al., *The Fortran Automatic Coding System for the IBM 704 EDPM* (IBM, 1956).
- Iverson, K. E., *A Programming Language* (Wiley, 1962). Falkoff, A. D. and Iverson, K. E., "The Evolution of APL", in *History of Programming Languages* (ACM, 1978) — typeballs 987 and 988 designed late 1964, before any APL system existed. Computer History Museum, APL typewriter ball (catalogue 102696484).
- ASA X3.4-1963 and USAS X3.4-1967 — the ASCII editions with and without `←` (95) and `↑` (94).
- Ritchie, D. M., "The Development of the C Language", *History of Programming Languages II* (ACM, 1993) — the `=` for `:=` "fiddle", and the `=+` / `x=-1` ambiguity. Thompson, K., *Users' Reference to B* (Bell Labs, 1972); Kernighan, B. W., *A Tutorial Introduction to the Language B* (Bell Labs).
- PEP 572, *Assignment Expressions* (Angelico, Peters, van Rossum, 2018). Van Rossum, G., "Transfer of power", python-committers mailing list, 12 July 2018. PEP 8016, *The Steering Council Model* (2018).
