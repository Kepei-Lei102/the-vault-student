---
chinese: 语言的字母表 (yǔyán de zìmǔbiǎo) — C 语言名字之谜
prerequisites:
  - "[[Compilers and Interpreters]]"
  - "[[Space Travel]]"
leads_to:
  - "[[Two Family Trees]]"
tags:
  - type/story
  - subject/computer-science
  - era/20c
  - cast/strachey
  - cast/landin
  - cast/richards
  - cast/thompson
  - cast/ritchie
  - cast/mcilroy
  - cast/kernighan
  - cast/stroustrup
  - region/europe
  - region/usa
---

# A, B, C 语言的字母表

> *Every beginner asks why the world's most important programming language is called C. The man who named it knew both possible answers, wrote them down side by side, and refused — for the rest of his life — to choose.*

## Cast of Characters

- **Christopher Strachey** (1916–1975) — presided over CPL, the gloriously ambitious ancestor that was never fully built; coined *lvalue* and *rvalue*, two words your compiler still shouts at you; played piano duets during design meetings.
- **Peter Landin** (1930–2009) — Strachey's assistant, who connected programming languages to the λ-calculus; the other half of the duets.
- **Martin Richards** (b. 1940) — the Cambridge research student who cut CPL down to BCPL at MIT in 1966–67, and half a century later wrote the family's honest obituary.
- **Doug McIlroy** (b. 1932) — Bell Labs; his TMG compiler-compiler shamed Ken Thompson into writing a language of his own.
- **Ken Thompson** (b. 1943) — Bell Labs; squeezed BCPL into **B** on a machine with 8K words of memory; forty years later co-created Go, ending the alphabet game.
- **Dennis Ritchie** (1941–2011) — Bell Labs; turned B into **C** in 1971–73, and wrote the history this story leans on at every step.
- **Brian Kernighan** (b. 1942) — Bell Labs; wrote the tutorials, including the one where *hello, world* first said hello.
- **Bjarne Stroustrup** (b. 1950) — answered the succession question in C's own notation.
- **Bonnie Thompson** — possibly the only person with a major programming language named after her. Nobody is certain, which is the point.

## 中文锚点

C 语言为什么叫 C?这是每个初学者的第一问,而官方答案是:**命名者拒绝回答**。里奇(Dennis Ritchie)在他自己写的 C 语言史里说,他"沿用单字母的风格,把它叫做 C,并且不去说明这个名字究竟是沿字母表前进,还是沿 BCPL 的字母前进"——两种读法都成立,他故意留白了一辈子。家谱是真实的:**CPL**(1963,剑桥+伦敦,野心太大,编译器始终没有建成——设计会议的间隙,斯特雷奇和兰丁会四手联弹钢琴);**BCPL**(1967,理查兹在 MIT 把 CPL 砍到只剩"能编译的部分",整个语言只有一种数据类型:机器字);**B**(1969,汤普森在只有 8K 字内存的 PDP-7 上"把 BCPL 挤压进 8K 字节,再经过他自己大脑的过滤"——名字多半是 BCPL 的缩写,但另一种说法是来自他更早的语言 Bon,而 Bon 要么以他妻子 Bonnie 命名,要么以一个"仪式中喃喃念诵咒语的宗教"命名:一门可能以咒语命名的语言,出自给机器写咒语的人);**C**(1971–73,PDP-11 有了**字节**,无类型的"字"世界撑不住了,类型就此诞生——定名 C 之前,它曾短暂地叫作 **NB**,"new B" 的缩写)。没有 A——字母表是中途才加入这个故事的。后来 C++ 用 C 自己的自增运算符回答了继承之问,而汤普森的最后一门语言叫 **Go**:字母表游戏,由开局的人亲手结束。

## The Story

### Prologue — the question with two official answers

Ask why Python is called Python and you get an answer (Monty Python). Ask why Java is called Java and you get an answer (the coffee). Ask why C is called C and you get a shrug that has lasted fifty years, because the man who named it built the shrug into the record. Dennis Ritchie, writing the language's official history in 1993, put it this way: "I decided to follow the single-letter style and called it C, leaving open the question whether the name represented a progression through the alphabet or through the letters in BCPL."

Both readings were live. C's parent really was called B. B's parent really was called BCPL. Read one way, the letters march A, B, C; read the other, they spell out B-C-P-L one at a time, and the next language should be called P. The folklore version — that there was once a language called A, which begat B, which begat C — is wrong in the most instructive way: **there was no A.** The family starts with a four-letter name, and the alphabet joined the story in the middle, by accident, through an act of compression.

What actually connects the four names is not the alphabet. It is that every language in the chain is the previous one **cut down** — to fit a smaller machine, a smaller team, or a harder deadline. This is a story about subtraction, and about how the leftovers of each cut fossilised into the language you can still run today.

![[abc-language-lineage.svg|700]]

### Act I — Bedford Gardens, 1963: piano duets and a language too good to build

In 1962 the University of Cambridge and the University of London set out to design a common successor to ALGOL 60, and the name tracked the politics: the **Cambridge Programming Language** became the **Combined Programming Language** when London joined, and was known unofficially as *Christopher's Programming Language*, after the man at the head of the table. Christopher Strachey ran the design committee — Peter Landin, David Hartley, David Park and David Barron from Cambridge; John Buxton, Eric Nixon and George Coulouris from London — and the meetings happened either in Cambridge or at Strachey's own house in Bedford Gardens, London. Martin Richards, then a junior research student, attended most of them, and recorded the detail that sets the tone of the whole era: during breaks in the arguments, Strachey and Landin would entertain the committee with piano duets.

![[abc-piano-duet-comic.png|640]]

CPL deserved the salon. It extended ALGOL 60 with integers, reals, complex numbers, bit patterns; it had `if`, `unless`, `while`, `until`, `repeat`; and Strachey kept proposing ideas faster than anyone could implement them. Among them was a distinction he cared about deeply: an expression on the *left* of an assignment names a **place**, an expression on the *right* names a **value**, and the two deserve different names — the **L-value** and the **R-value**. Remember those two words; they outlive everything else in this act.

Because the language itself died of ambition. The compiler was being written for EDSAC 2 when, mid-project, Cambridge switched machines to Titan — a cut-down Ferranti Atlas that arrived late and had no operating system — and the work had to start over. London got a usable subset running on its Atlas; Cambridge never finished. Richards, who was there, delivered the verdict without anaesthetic in his memoir of Strachey: the project "cannot be regarded as being successful since it did not result in a usable CPL compiler." The language was too large, the implementers too few, the machines a moving target. What survived was a 1963 paper, a set of ideas, and a generation of students who had watched a beautiful thing fail to compile.

One of those ideas is still talking. Type `x + 1 = 5;` into a modern compiler and it answers: *lvalue required as left operand of assignment*. That word is Strachey's, coined for a language that never ran, delivered to you by a compiler for its great-grandchild.

### Act II — Cambridge, Massachusetts, December 1966: keep only what compiles

Martin Richards arrived at MIT in December 1966 and did the thing the committee could not: he cut. **BCPL** — *Basic CPL* — kept CPL's syntax, its control words, its feel, and deleted everything that had made the compiler impossible. Above all it deleted the types. BCPL has exactly one kind of data: the machine **word** — a fixed-length bit pattern, called a "cell", whose meaning depends entirely on what you do to it. Add two cells and the machine adds integers; apply one as an address and the machine fetches. The language does not know or care which you meant. Richards later stated the philosophy in a sentence that programmers have quoted for fifty years: BCPL's philosophy "is not one of the tyrant who thinks he knows best"; the language "acts more as a servant", assuming the programmer knows what they are doing — even, the manual adds, when confronted with apparent nonsense.

It worked immediately. Richards had a compiler running on MIT's CTSS time-sharing system within weeks and wrote the reference manual by July 1967. BCPL went on to build the OS6 operating system at Oxford and parts of the seminal Alto work at Xerox PARC, and Richards later made it portable by compiling to *O-code* — instructions for an imaginary machine, translated to each real one — the trick every virtual machine in [[Compilers and Interpreters]] still plays. Along the way BCPL quietly invented something you used today: the `//` comment, running to the end of the line.

And it travelled to one place that matters for this story. Ported to the GE mainframes at Bell Labs, BCPL became — in Ritchie's words — "the language of choice among the group of people who would later become involved with Unix."

### Act III — Murray Hill, 1969: eight thousand words, one brain

In 1969 Bell Labs walked out of the Multics project, and its programmers lost the big machine they had been building on. What Ken Thompson had instead was a cast-off DEC PDP-7 — in Ritchie's description, an environment "cramped and spartan even for the time": **8K words of memory, 18 bits each, and no software useful to him.** How that machine was found, the game that was running on it, and the month in which an operating system appeared on it are their own story — [[Space Travel]] — but one working detail belongs here, because it explains everything about what happened to the languages. At first there was no way to program the PDP-7 *on* the PDP-7: Thompson wrote code on a GE mainframe in another room, and a postprocessor punched it onto **paper tape**, which was then carried by hand to the smaller machine and fed in. Every program was a corridor walk. (One fossil of this era is still on your computer: the assembler's output file had a fixed name, `a.out` — *assembler output* — and compilers that contain no assembler still emit it, fifty years later.)

![[abc-paper-tape-comic.png|640]]

The corridor era ended when the PDP-7 could assemble its own programs, and then the language itch started. Doug McIlroy had brought up TMG — a language for writing compilers — *on* the tiny machine, and Ritchie records what that did to Thompson: "Challenged by McIlroy's feat in reproducing TMG, Thompson decided that Unix — possibly it had not even been named yet — needed a system programming language. After a rapidly scuttled attempt at Fortran, he created instead a language of his own, which he called B."

Ritchie's one-sentence description of B has never been improved on: "B can be thought of as C without types; more accurately, it is BCPL squeezed into 8K bytes of memory and filtered through Thompson's brain."

The squeeze had consequences, and each one is a scar you can still touch:

- BCPL's assignment `:=` lost its colon and became `=` — one character saved, and a sixty-year argument joined; that fight has its own story in [[The Arrow That Pointed the Other Way]].
- Thompson invented `++` and `--`. The legend says he was exploiting the PDP-11's auto-increment addressing — and Ritchie kills the legend with a date: "This is historically impossible, since there was no PDP-11 when B was developed." The real reason was poverty: the translation of `++x` was *smaller* than the translation of `x = x + 1`, and on 8K words, smaller won.
- BCPL's `//` comments were dropped in favour of PL/I's `/* */`. Hold that thought; the family returns to it.
- BCPL's strings carried their length in front. B dropped the count and instead ended every string with a special terminating character, which B spelled `*e`. The **null-terminated string** — arguably the most consequential data-structure decision ever made — entered the world as a space-saving fiddle on a machine with eight kilowords.

And the name? Ritchie preserves both theories with visible delight: B "most probably represents a contraction of BCPL, though an alternate theory holds that it derives from Bon" — an earlier language of Thompson's, which "was named either after his wife Bonnie, or (according to an encyclopedia quotation in its manual), after a religion whose rituals involve the murmuring of magic formulas." The religion is Bön, of Tibet; the encyclopedia quotation really is in the Bon manual; and so the ancestor of C is a language possibly named after incantation, by men writing spells for a machine.

One more thing about B, and it is the hinge of the whole story: **B was interpreted.** The compiler emitted *threaded code* — a chain of addresses fed to an interpreter loop, a scheme [[Compilers and Interpreters]] will show you — and the result ran so much slower than assembly that writing the operating system in B was, in Ritchie's words, a possibility they "discounted". A calculator, `dc`, was written in B and survives to this day. The kernel stayed in assembly. The language wasn't good enough yet, and everyone knew it.

### Act IV — 1970–72: the machine with bytes

By 1970 the Unix project had shown enough promise to earn a new machine, and the machine changed everything. The DEC PDP-11 was among the first of its line delivered — so early that **three months passed before its disk arrived**, during which, Ritchie notes, "the machine marked time by enumerating closed knight's tours on chess boards of various sizes." A brand-new computer, waiting for its own storage, counting the ways a knight can visit every square.

When real work started, B began to creak, because the PDP-11 was **byte-addressed**. B and BCPL knew only the word; on a machine whose natural unit was the byte, Ritchie found their character handling "awkward, even silly". Floating-point numbers would not fit a 16-bit word, so BCPL's trick for them was dead on arrival. Worst of all, B defined a pointer as an index into an array of *words*, so every single pointer reference paid a run-time conversion from word-index to the byte address the hardware actually wanted. The conclusion was forced: "it seemed that a typing scheme was necessary to cope with characters and byte addressing, and to prepare for the coming floating-point hardware." The machine's shape demanded that the language finally know what things *are*.

So in 1971 Ritchie added a character type to B and — the other half of the hinge — **rewrote its compiler to generate real PDP-11 instructions instead of threaded code**. Compiled, not interpreted; fast enough, for the first time, to look assembly in the eye. He called the extension **NB**, "new B", and the name lasted about as long as the language, which existed so briefly no full description was ever written. Then came structures — Ritchie wanted a type that could describe an actual object, the bits of a directory entry as they lay on disk — and solving how arrays and pointers should behave inside them produced what he calls "the crucial jump in the evolutionary chain": an array's name, mentioned in an expression, simply *becomes* a pointer to its first element. Nothing stored, everything conjured at the point of use. Every C programmer since has lived inside that rule.

With a type system, new syntax, and a real compiler, the language had outgrown its name: "I felt that it deserved a new name; NB seemed insufficiently distinctive. I decided to follow the single-letter style and called it C, leaving open the question whether the name represented a progression through the alphabet or through the letters in BCPL."

That is the whole naming, in the namer's own words, ambiguity included on purpose. The year that followed — 1972 — Ritchie calls the most creative period of the language's development. By early 1973 the essentials of modern C were complete, and that summer the Unix kernel itself was rewritten in C: an operating system in a high-level language, the step that would later let Unix walk off its birth machine and onto everything else — the ledger of what an OS owes its language is in [[Operating Systems]].

### Act V — the succession, answered three ways

An ambiguous name leaves an ambiguous inheritance. By the alphabet reading, C's successor is D. By the BCPL reading, the letters spell B, C… and the next language should be called **P**. Both doors stood open, and what walked through them is a study in temperament.

**Bjarne Stroustrup refused both doors.** His extension of C needed a name in 1983, and the one that stuck — coined by Rick Mascitti — was **C++**: not a new letter but C's own increment operator applied to C itself, a name that says *the same language, one more*. Stroustrup then footnoted his own joke twice. First: "Connoisseurs of C semantics find C++ inferior to ++C" — because `C++` is a *post*-increment, it hands back the **old** value of C. Second, deadpan, in his own book: "The language is not called D, because it is an extension of C" — and readers seeking "yet another interpretation" of the name are referred to the appendix of *Nineteen Eighty-Four*, where Newspeak grades its praise *plusgood* and *doubleplusgood*.

**The alphabet door opened anyway.** In 1999 Walter Bright began a from-scratch successor he called Mars; his friends, seeing exactly what it was, kept calling it D until he gave in, and D shipped under the letter the folklore had always predicted. The BCPL door — P — has never been claimed by anyone in the family.

**And the man who started the single-letter style ended it.** In 2009 Ken Thompson, with Rob Pike and Robert Griesemer, released his last major language, and it is called **Go** — a word, not a letter, chosen forty years after B, by which time the joke had run its course. (The same Thompson-and-Pike pair had already spent a 1992 diner evening redesigning the world's text encoding — the placemat is in [[Text Encoding]].)

As for **A**: the letter a student goes looking for was never in this family. The famous A in programming is Kenneth Iverson's 1962 book *A Programming Language*, whose initials became APL — a different dynasty, whose war over a single arrow is told in [[The Arrow That Pointed the Other Way]]. The alphabet's first letter belongs to someone else's story.

### Epilogue — subtraction as a way of making things

Read the family tree as a set of verdicts. CPL died of ambition: too beautiful, too big, never compiled. BCPL lived by cutting CPL to what one man could implement in weeks. B lived by cutting BCPL to what 8K words could hold. C exists because the machine changed shape underneath B, and this time the answer was not another cut but the one addition the whole lineage had been resisting: types. Four languages, three named by subtraction, and the last one named with a shrug the namer never resolved.

Ritchie wrote the family's epitaph himself, and it is the least sentimental sentence in the whole literature: "C is quirky, flawed, and an enormous success." It displaced assembly language because it was efficient enough to; everything from your operating system to Python's own interpreter is still written in it or in its children.

And the names are the sediment. *lvalue* is Strachey's seminar still talking through your compiler's error messages. `a.out` names an assembler that no longer exists. `//` is BCPL's comment, dropped by B, resurrected by C++, and finally readmitted into C itself in 1999 — a thirty-year round trip back into the language of the man who deleted it. Ritchie himself, describing an old declaration form C still accepts, reached for the right word: "a living fossil." Every language is a fossil record of the machines and the arguments that made it — and the strangest bed of fossils of all, the one every computer still boots on top of, is [[The Ghost of Drive A]].

## Cultural ripples

- **`lvalue required as left operand of assignment`** — a word coined by Christopher Strachey for a language that never ran, in every C, C++, and Rust compiler's error vocabulary today.
- **hello, world was born in B, not C.** Its first known appearance is Brian Kernighan's Bell Labs tutorial for B, before C existed; K&R's C book made it a rite of passage.
- **The null-terminated string** — B's space-saving `*e` terminator — became C's string convention and, through unchecked buffer copies, the mother of decades of security holes; Poul-Henning Kamp's 2011 ACM Queue essay prices it as "the most expensive one-byte mistake."
- **`++` became a brand.** One operator invented to save words on a PDP-7 now names C++ (and, if you squint at four plus signs stacked two by two, C#).
- **"I'd spell creat with an e."** Thompson's answer, years later, to what he would change about Unix — the terse-name culture of B's era, regretted one vowel at a time.
- **Bonnie Thompson** may be the only person to have a foundational programming language named after her, and the record was left unclear on purpose — the manual preferred the religion.

## Where this surfaces in the vault

- [[Compilers and Interpreters]] — the pedagogy this story dramatises: B was *interpreted* (threaded code) and too slow to write an OS in; C was *compiled* to native PDP-11 instructions and rewrote the kernel within two years. The compiled/interpreted trade-off, with dates and a body count — plus self-hosting: the C compiler has been written in C since 1973, and the dark side of that bootstrap chain is Thompson's own "Trusting Trust".
- [[The Arrow That Pointed the Other Way]] — the sibling story: one single character of B's squeeze (`:=` to `=`), unfolded into its own sixty-year war.
- [[Text Encoding]] — the byte-addressed PDP-11 forced C's `char` into existence; the same Thompson later redesigned the world's text on a placemat.
- [[Operating Systems]] — the 1973 kernel rewrite in C is where this lineage pays its rent.
- [[Assembly Language]] — the language C was built to displace, and the source of the `a.out` fossil.

## Receipts

- Ritchie, D. M., "The Development of the C Language," *History of Programming Languages II* (ACM, 1993) — the source of nearly every quotation above: the naming sentence, "squeezed into 8K bytes… filtered through Thompson's brain," the Bon/Bonnie/religion passage, the TMG challenge, the `++` legend debunked, the knight's tours, the Problems of B, NB, the "crucial jump," the 1973 kernel rewrite, "quirky, flawed, and an enormous success," and "a living fossil."
- Richards, M., "Christopher Strachey and the Development of CPL" (Cambridge, 2016) — Bedford Gardens, the piano duets, the committee roster, the EDSAC 2 → Titan disaster, L-values and R-values, and the verdict that no usable CPL compiler ever resulted.
- Barron, D. W., Buxton, J. N., Hartley, D. F., Nixon, E., and Strachey, C., "The Main Features of CPL," *The Computer Journal* 6(2), 1963.
- Richards, M., "The BCPL Reference Manual," MIT Project MAC Memorandum M-352, July 1967; Richards, M. and Whitby-Strevens, C., *BCPL: The Language and its Compiler* (Cambridge University Press, 1979) — the tyrant/servant philosophy.
- Thompson, K., *Users' Reference to B* (Bell Labs, 1972); Kernighan, B. W., "A Tutorial Introduction to the Language B" (Bell Labs, c. 1973) — the first *hello, world*.
- Stroustrup, B., *The C++ Programming Language* (3rd ed., 1997) §1.4 and *The Design and Evolution of C++* (1994) — Rick Mascitti, "Connoisseurs of C semantics find C++ inferior to ++C," "not called D," and the *Nineteen Eighty-Four* appendix.
- Bright, W., D language FAQ — Mars, and the friends who kept saying D.
- Kamp, P.-H., "The Most Expensive One-Byte Mistake," *ACM Queue* 9(7), 2011.
