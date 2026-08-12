---
chinese: 玻尔兹曼的墓碑 (bō'ěrzīmàn de mùbēi)
prerequisites: []
leads_to:
  - "[[Information Theory]]"
tags:
  - type/story
  - subject/physics
  - subject/computer-science
  - era/19c
  - era/20c
  - cast/boltzmann
  - cast/planck
  - cast/mach
  - cast/ostwald
  - cast/einstein
  - cast/perrin
  - region/europe
---

# Boltzmann's Tombstone 玻尔兹曼的墓碑

> *Above the bust, carved into the white marble: $S = k \log W$.*
>
> *He spent his life arguing that atoms are real and that the second law of thermodynamics is only a matter of overwhelming odds. He died in 1906, two years before the experiment that proved him right. And the equation on his grave — the one that made him immortal — he never actually wrote. The man who did was the one who introduced the constant $k$ and named it after him.*

![[boltzmann-tombstone-entropy.svg|697]]

## Cast of Characters

- **Ludwig Boltzmann** (1844–1906) — Austrian physicist; the architect of **statistical mechanics**. Bet his career on two then-radical ideas: that matter is made of real **atoms**, and that **entropy is a counting problem** — the second law of thermodynamics is not an iron law of nature but a statement about probability.
- **Max Planck** (1858–1947) — initially a skeptic of Boltzmann's statistical view, then the man who, in his 1900 work on blackbody radiation, **introduced the constant $k$** and **wrote the equation in the form $S = k \log W$**. The formula on Boltzmann's grave is, strictly, Planck's handwriting on Boltzmann's idea.
- **Ernst Mach** (1838–1916) — physicist-philosopher; the most famous voice of the **anti-atomists**. *"Have you ever seen one?"* If you can't observe atoms directly, he held, science has no business assuming them.
- **Wilhelm Ostwald** (1853–1932) — chemist and leader of the **Energeticists**, who wanted to build all of physics on energy alone and treat atoms as an unnecessary fiction. Boltzmann's great public sparring partner. (He later recanted — see Act V.)
- **Josef Loschmidt** (1821–1895) — Boltzmann's older friend and colleague, and the author of the sharpest objection to the H-theorem: the **reversibility paradox** (1876).
- **Ernst Zermelo** (1871–1953) — then Planck's assistant in Berlin; raised the **recurrence paradox** (1896) built on Poincaré's recurrence theorem. (Later famous for the axioms of set theory — the Z in ZFC.)
- **Albert Einstein** & **Jean Perrin** — the men who, in **1905** (theory) and **1908** (experiment), finally made atoms undeniable.

## 中文锚点

**玻尔兹曼的墓碑**（bō'ěrzīmàn de mùbēi）：路德维希·玻尔兹曼（Ludwig Boltzmann, 1844–1906）是**统计力学**的奠基人。他坚持两个当时被视为激进的观点：**原子是真实存在的**，以及**熵其实是一个"数微观态"的问题**——热力学第二定律不是绝对的自然律，而是一个关于**概率**的陈述。

他的核心公式是 $S = k \log W$：宏观的熵 $S$，等于玻尔兹曼常数 $k$ 乘以与该宏观态相容的**微观态数目** $W$ 的对数。混乱（高熵）之所以"自发"出现，仅仅因为对应的微观态数目压倒性地多。

故事的悲剧与讽刺：玻尔兹曼一生为原子论辩护，却在原子被实验证实（爱因斯坦 1905 理论 + 佩兰 1908 实验）的前夕，于 1906 年自杀离世。而刻在他墓碑上、让他不朽的那个公式，**其实是普朗克写下的形式**——普朗克引入了常数 $k$，并以玻尔兹曼之名命名它。这又是一则[[Stories/Stigler's Law of Eponymy|斯蒂格勒命名律]]的例子。详细的数学（以及它如何在 1948 年变成香农的信息熵）见 [[Information Theory]]。

> **A note on what follows:** this is a story that ends in a death by suicide, told as history. It is handled plainly and without detail, the way the vault handles [[Stories/The War of the Currents|the electric chair]] — as part of the record, not as spectacle.

## The Story

### Act I — Entropy is a counting problem (1872–1877)

For most of the nineteenth century, **entropy** was a bookkeeping quantity. Clausius had defined its *changes* through heat and temperature ($dS = dQ_{\text{rev}}/T$) and stated the second law as a brute fact of nature: heat flows from hot to cold, entropy never decreases, full stop. It worked beautifully and explained nothing about *why*.

Boltzmann's leap — the one carved on his grave — was to say that entropy is **a measure of how many ways the invisible pieces can be arranged to look the same from the outside.** A gas in a box has one *macrostate* (its pressure, volume, temperature) but an astronomical number of *microstates* (the exact position and velocity of every molecule). Call that number $W$ — for *Wahrscheinlichkeit*, German for "probability," though here it really counts **ways**. Then

$$S = k \log W.$$

Entropy is just the logarithm of the number of microstates, scaled by a constant. (Why the **logarithm**? Because if you put two independent systems side by side, their *numbers of arrangements multiply* — $W_{\text{total}} = W_1 W_2$ — but we want their *entropies to add*, $S_{\text{total}} = S_1 + S_2$. The one function that turns multiplication into addition is the log. The logarithm isn't a cosmetic choice; it is forced by the demand that entropy be additive — the same reason logs run through [[Information Theory|information]] and [[Logarithms|so much else]].)

This reframing detonates the mystery of the second law. A shuffled deck doesn't "want" to be disordered; it's just that there is exactly **one** ordered arrangement and about $8 \times 10^{67}$ shuffled ones, so a random shuffle lands you in the messy pile essentially every time. Heat spreads out, gases mix, ice melts in warm water — not because a law forbids the reverse, but because the reverse corresponds to so vanishingly few microstates that you would wait many times the age of the universe to see it. **The second law is not a commandment. It is a bet at overwhelming odds.** Boltzmann's **H-theorem** (1872) tried to prove this approach to equilibrium mechanically, tracking a quantity $H$ (essentially negative entropy) that he showed could only decrease.

### Act II — Two beautiful objections (1876, 1896)

The trouble with deriving "entropy always increases" from mechanics is that **mechanics doesn't know which way time runs.** Newton's laws, and the molecular collisions they govern, are perfectly **time-reversible**: film a collision and play it backward, and the reversed film also obeys the laws. So how can a one-way street (entropy up) be paved out of two-way bricks?

This is exactly what Boltzmann's friend **Josef Loschmidt** pressed in **1876** — the **reversibility paradox** (*Umkehreinwand*). If the molecules in your gas evolve from low entropy to high, then the state you'd get by **reversing every velocity** would have to evolve from high entropy *back down* to low — and that reversed state is just as legal under Newton's laws. So the H-theorem can't be a universal mechanical theorem; something extra must have been smuggled in. (It had: the assumption of **molecular chaos**, the *Stosszahlansatz*, that incoming molecules are uncorrelated. That assumption quietly inserts the arrow of time by hand.)

Twenty years later, in **1896**, **Ernst Zermelo** — then Planck's young assistant — landed the second blow: the **recurrence paradox** (*Wiederkehreinwand*). Henri Poincaré had proved that any bounded mechanical system, left alone long enough, returns **arbitrarily close to its starting configuration**. So $H$ can't decrease forever; it must eventually come back up. Irreversibility, Zermelo argued, is therefore impossible in principle.

Boltzmann's reply was the deep one, and it took the rest of his life to articulate cleanly: **both objections are correct, and neither matters.** Yes, a velocity-reversed state would un-mix the gas — but such states are so absurdly rare that you'll never prepare one by accident. Yes, Poincaré recurrence is real — but for a mole of gas the recurrence time is something like $10^{10^{23}}$ years, a number next to which the age of the universe is indistinguishable from zero. The second law isn't violated by these scenarios; it's **statistical**, and the statistics are so lopsided that "overwhelmingly probable" and "certain" are, for any practical purpose, the same word. This is the modern view. Boltzmann was right. But in 1896 it sounded like special pleading.

![[boltzmann-tombstone-reversed-film-comic.png|620]]

### Act III — The war over whether atoms are real

Underneath the technical fight was a bigger one, and it was philosophical. Boltzmann's whole edifice **assumed atoms** — real, countable, mechanical molecules. And in the German-speaking physics of the 1890s, that assumption was under serious attack.

**Ernst Mach**, the towering physicist-philosopher — yes, *that* Mach: supersonic speed is measured in **Mach numbers** (Mach 1, Mach 2…) after his pioneering photographs of the shock waves around fast bullets — was a **positivist**: science should speak only of what can be observed. Atoms had never been seen. To Mach they were at best a convenient calculating fiction and at worst a metaphysical embarrassment. The story goes that he would deflate atomic talk with a flat *"Haben Sie eines gesehen?"* — *"Have you ever seen one?"*

![[boltzmann-tombstone-seen-one-comic.png|560]]

**Wilhelm Ostwald** went further and tried to build a rival physics — **Energetics** — in which **energy**, not matter, was the single fundamental substance, and atoms were dispensable. Ostwald and Boltzmann clashed publicly and repeatedly; at one famous 1895 meeting in Lübeck the debate was likened to a bull (Boltzmann, defending atoms with mechanical detail) against a nimble matador (Ostwald, philosophical and quick). Boltzmann reportedly called himself *"the last pillar"* holding up the atomic theory against the energeticist tide.

He was being too gloomy — atoms had plenty of working physicists on their side, and kinetic theory was used productively throughout the period (this is one of the **honest edges** below). But Boltzmann *felt* besieged, and the feeling fed a darkening mood.

### Act IV — Duino (5 September 1906)

Boltzmann's later years were genuinely hard, and not only because of the science. He suffered from severe swings of mood — what we would today recognize as **bipolar disorder** — along with worsening asthma, angina, and failing eyesight that made it hard for him to read the journals where the fight was being waged. He had attempted suicide before. In 1906 he had to cancel his summer lectures on account of his "nervous condition."

On **5 September 1906**, while on holiday with his wife and youngest daughter at **Duino**, on the Adriatic near Trieste, Boltzmann **took his own life** while the two of them were out swimming. He was 62.

The neat literary version — *the positivists hounded him to his death* — is too neat, and the vault doesn't tell it that way (see the honest edges). His illness was real and largely independent of the atom wars. But it is true, and unbearably so, that he died **on the eve of his vindication**, with the fight still feeling, to him, unwon.

### Act V — The atoms appear (1905–1909)

Here is the cruel timing. In **1905** — Boltzmann still alive — a 26-year-old patent clerk named **Albert Einstein** published a theory of **Brownian motion**: the jittering dance of pollen grains in water, he showed, is the visible drumming of *invisible* water molecules, and the statistics of that dance let you **count the molecules** — to extract **Avogadro's number** from a microscope. It was a quantitative prediction that only made sense if atoms were real and Boltzmann's statistical mechanics was correct.

In **1908**, two years *after* Boltzmann's death, **Jean Perrin** at the Sorbonne did the experiment. He tracked Brownian particles under an ultramicroscope, measured exactly what Einstein predicted, and pulled out Avogadro's number. The decisive part: the value he got **agreed with values obtained from a dozen utterly unrelated methods** — radioactivity, blackbody radiation, electrochemistry. When that many independent roads converge on the same number, the thing being counted is real. (Perrin won the 1926 Nobel Prize for it.)

The skeptics folded. **Ostwald** — the arch-energeticist — publicly conceded, writing that Einstein's and Perrin's work had *"convinced even the most cautious"* that matter is atomic. **Mach** went to his grave in 1916 still refusing, but he was, by then, almost alone. Within a few years of Boltzmann's death the question he had staked everything on was simply **settled, in his favour.**

### The formula he never wrote — a tribute, not a theft

And now the detail that makes the tombstone a story rather than a monument. Boltzmann established the *physics* of $S \propto \log W$, but he never wrote the equation in the crisp form carved on his grave, and he never introduced the constant. **It was Max Planck**, in his 1900 blackbody work, who wrote it as $S = k \log W$ and who introduced $k$ — the **Boltzmann constant**, $k \approx 1.38 \times 10^{-23}\,\text{J/K}$ — *and named it after Boltzmann.* (Planck, who had started out a skeptic of the statistical view, ended up its great formalizer.)

It's tempting to file this under **[[Stories/Stigler's Law of Eponymy|Stigler's Law]]** — *no scientific discovery is named after its original discoverer.* But look closer and it is the **opposite**, and that's the lovely part. Stigler's Law is about *misattribution*: a name lands on the wrong person because their textbook won, or their country won, or they explained it loudest. Here the credit is **exactly right** — the physics of entropy-as-counting is unambiguously Boltzmann's, and Planck *knew* it. Planck didn't take the idea; he gave it its final, teachable form, and then deliberately attached his late rival's name to the constant *out of respect*. This is eponymy working as it should: a tribute from the formalizer to the discoverer. (There's even a quiet joke in it — Planck, who already had his own constant $h$ waiting in the same 1900 papers, made sure the *other* new constant of that revolutionary year would carry **Boltzmann's** name, not a second one of his own.) The grave is honest about the idea and generous about the authorship — the rare case where the name is *more* deserved than usual, not less. Mathematics keeps one twin to this on file: **"abelian,"** named for [[Stories/Abel the Other Boy Who Died Young|Niels Henrik Abel]] — another honest eponym, carved so deep it went lowercase. When credit is given rather than misplaced, it tends to be given *completely*.

### The bridge to information (1948)

The story doesn't end at the cemetery. Forty-two years later, **Claude Shannon** went looking for a measure of *information* — how much uncertainty a message resolves — and arrived at

$$H = -\sum_i p_i \log p_i.$$

It is the *same mathematical object* as Boltzmann's entropy. If a system's $W$ microstates are equally likely, each has probability $p = 1/W$, and Shannon's formula collapses straight back to $S = k \log W$. When Shannon asked **John von Neumann** what to call his quantity, von Neumann (the story goes) told him to call it **entropy** — *"for two reasons. First, the same expression already appears in statistical mechanics. Second, nobody really knows what entropy is, so in a debate you'll always have the advantage."*

This is not a metaphor or a pun. **Boltzmann's thermodynamic entropy and Shannon's information entropy are one quantity in two unit systems** — physics measures it in joules-per-kelvin with a natural log, information measures it in bits with a base-2 log, and **Landauer's principle** ($k_B T \ln 2$ of heat to erase one bit) is the exchange rate between them. The full development — the von Neumann story, the Shannon formula, Landauer — lives in **[[Information Theory]]**. Boltzmann counted the microstates of a gas; Turing's codebreakers at Bletchley counted them in messages and called the unit the *ban* (see [[Stories/Turing at Bletchley]]); your phone counts them every time it compresses a photo. The equation on the gravestone turned out to be about *everything that can be uncertain.*

## Honest edges

**Boltzmann did not write $S = k \log W$, and the constant isn't his either — but this is *not* a Stigler misattribution.** Planck wrote the equation in that form and introduced $k$ (naming it after Boltzmann) in 1900. Boltzmann's contribution is the physics — entropy as the log of the microstate count — not the specific notation or the constant. It would be easy, and wrong, to file this under [[Stories/Stigler's Law of Eponymy|Stigler's Law]]: that law is about credit landing on the *wrong* person, and here the credit is exactly right. The discovery is Boltzmann's; Planck, the formalizer, deliberately put his rival's name on the constant out of respect. It is the *inverse* of the usual eponymy story — a tribute, not a theft — and the vault flags it as the instructive counter-case in the Stigler card.

**"The positivists drove him to suicide" is a romantic oversimplification.** It is the version you'll most often hear, and it is too clean. Boltzmann had documented, severe mental illness — almost certainly bipolar disorder — together with declining physical health, and had attempted suicide before. The scientific opposition unquestionably weighed on him and darkened an already vulnerable mind, but historians are clear that his death is not reducible to the atom wars. Treating a man's suicide as a tidy plot device about scientific martyrdom does him a disservice; the vault states the illness and the timing without collapsing one into the other.

**Boltzmann was not as alone as the legend says.** The image of a single embattled defender holding off a unified anti-atomic establishment is dramatized. Kinetic theory was widely and successfully used; atomism had many adherents (Maxwell, Gibbs, and a generation of working physicists). Mach and Ostwald were prominent and loud, but they were a vocal faction, not a consensus. Boltzmann *felt* like "the last pillar"; the historical record is less lopsided.

**Ostwald and Mach were *wrong about atoms* — but their instinct was not worthless, and that distinction matters.** It is too easy to write them as the villains who lost. On the narrow empirical question — *are there real, countable atoms?* — they were simply wrong, and Ostwald had the grace to say so. But the deeper instincts underneath were serious physics, not obstinacy. **Mach's** demand that science speak only of the observable directly shaped the young **Einstein** (who credited Mach's critique of absolute space when building special relativity) and runs straight into the **Copenhagen interpretation** of quantum mechanics a generation later — Heisenberg's "we should talk only about what we can measure" is pure Mach. **Ostwald's** energy-first picture, that energy might be more fundamental than little billiard-ball particles, looks less foolish once quantum field theory recasts "particles" as *excitations of fields*: the naive classical atom — a tiny solid sphere — really is the wrong picture, just not in the way Ostwald meant. So the honest verdict is layered: Boltzmann won the fact, decisively; but the question of *what is ultimately real — matter, energy, or fields* — is one of the deepest in physics, and the people he was arguing with were asking it, not dodging it. (This is the kind of "law vs deeper truth" distinction [[Laws and Theorems]] is about.)

**"He died never knowing he was right" is *almost* exact, not exact.** Einstein's Brownian-motion paper appeared in **1905**, while Boltzmann was alive, so the theoretical case was already on the table. What came *after* his 1906 death was the **decisive experimental confirmation** — Perrin's 1908 measurements and the convergence of Avogadro's number across methods. So the honest phrasing is: he died with the verdict in but not yet delivered; the experiment that ended the argument came two years too late for him to see.

**$\log$ vs $\ln$, and what $W$ is.** The grave reads "$\log$," but in physics the base is $e$ (natural log); Shannon's information version uses base 2. And $W$ (*Wahrscheinlichkeit*) is usually translated "probability," but in this formula it is really a **count of microstates** (sometimes written $\Omega$ in modern texts). The translation "probability" is a historical artifact of the German word, not a claim that $W$ is a number between 0 and 1.

## Cultural ripples

**The arrow of time.** Boltzmann's statistical reading of entropy is still our best account of *why the future is different from the past* in a universe whose microscopic laws don't care about direction. The reason you remember yesterday and not tomorrow, the reason the cup shatters but never reassembles, traces back to the universe having started in an extraordinarily low-entropy state and the overwhelming microstate-counting odds doing the rest. The deepest open questions in cosmology about the early universe are, in part, questions about Boltzmann's $W$.

**The word that ate the culture.** "Entropy" escaped physics and became one of the most borrowed words of the twentieth century — a shorthand for decay, disorder, the tendency of everything to fall apart, invoked in everything from Pynchon novels to thermodynamics-flavoured despair. Most of those usages are loose, but they all descend from the gravestone.

**He was the midwife of quantum mechanics — without quite meaning to be.** Here is the connection most people miss. When **Planck** cornered the blackbody problem in 1900, the tool he reached for was *Boltzmann's* statistical counting — and to make the counting come out right he had to chop energy into discrete lumps, $E = h\nu$, as a bookkeeping trick he never fully believed. That trick *was* the birth of the quantum. So Planck didn't just write Boltzmann's equation on the grave; he used Boltzmann's method to crack open the quantum world. The line runs straight on: **Einstein** (1905) turned Planck's lumps into real light quanta; **Bose–Einstein** and **Fermi–Dirac** statistics are simply Boltzmann's "count the ways" redone with quantum rules about which arrangements count as distinct; and **Mach's** observables-only insistence became, through Einstein and then Heisenberg, part of the philosophical spine of quantum theory. In a real sense Boltzmann, Planck, Einstein — and even Mach — are the generation whose arguments *became* quantum physics. (Shannon comes *after* — information theory is 1948, two decades past the quantum revolution — but the entropy thread loops back in through **von Neumann's** quantum entropy, which actually predates Shannon's and is the bridge to today's quantum information theory.)

**The most consequential equation on any headstone.** Carving an equation on a grave is rare; carving one that turned out to underwrite *information theory, machine learning, and the physics of computation* is unique. Every time a model reports **cross-entropy loss**, every time a file is **compressed** to its Shannon limit, every time a physicist computes the **entropy of a black hole** (which is, astonishingly, also a count of microstates — the Bekenstein–Hawking formula is $S = k_B A / 4\ell_P^2$, the same idea applied to a horizon), Boltzmann's counting argument is doing the work. The tombstone in Vienna's Zentralfriedhof is, in a real sense, a pilgrimage site for two sciences that didn't exist when he died.

**A teaching gift.** The single best cure for the mystique of the second law is Boltzmann's deck of cards: disorder isn't a force, it's just arithmetic. Once a student sees that "spontaneous" only ever means "overwhelmingly more ways," the whole of thermodynamics stops being a list of decrees and becomes a consequence of counting — which is the spirit of [[Stories/The Naming of Normal|how a distribution gets its shape from counting, too]].

## Where this surfaces in the vault

- **The physics pedagogy lives in [[Entropy and the Second Law]].** That card carries the three statements of the second law, Clausius's measurable $\Delta S = Q/T$, heat engines and the Carnot ceiling, the arrow of time, and $S=k\ln W$ worked as physics — while this Story keeps Boltzmann's life, the reversibility/recurrence paradoxes, and *why* the logarithm. Dual residency.
- **The load-bearing information math lives in [[Information Theory]].** That card carries $S = k_B \ln W$, the von Neumann naming story, the Shannon-equals-Boltzmann identity, and Landauer's principle as working content. This Story is its human prologue; they cross-link both ways (dual residency).
- **[[Stories/Stigler's Law of Eponymy]]** — the formula-and-constant authorship (Planck wrote it, named the constant after Boltzmann) is the *inverse* of a Stigler case: not a misattribution but a tribute, the credit landing exactly where it belongs. It's the instructive counter-example in that meta-card.
- **[[Kinetic Theory and the Ideal Gas]]** — where the constant $k$ does concrete physics. That card derives $pV=NkT$ and $\tfrac{1}{2}m\langle c^2\rangle=\tfrac{3}{2}kT$ from molecules in a box; the same $k$ then reappears here counting microstates. The pedagogical companion to this Story.
- **[[Stories/Turing at Bletchley]]** & **[[Stories/The Boolean-to-Silicon Bridge]]** — the other two legs of the entropy-becomes-information arc. Bletchley measured information in *bans*; Shannon married Boolean logic to circuits. Read all three for the full thread from a gas in a box to a language model.
- **[[Stories/Wolfgang Pauli and the Number 137]]** — **Mach**, the anti-atomist who hounded Boltzmann here, was **godfather to Wolfgang Pauli**, who grew up on Mach's observables-only creed, turned it into "not even wrong," and then helped build the quantum theory of the very atoms Mach denied to his grave. The positivist thread runs straight from this card into Pauli's.
- **[[Normal Distribution]]** — the **Maxwell–Boltzmann** velocity distribution is where this same statistical-mechanics machinery produces a bell-shaped law for molecular speeds.
- **[[Why Probability and Statistics]]** — Maxwell–Boltzmann (and Bose–Einstein, Fermi–Dirac) statistics are *literally combinatorial counting under different rules*, exactly the "count the ways" move at the heart of $S = k \log W$.
- **[[Logarithms]]** — why entropy uses a log at all: to turn multiplying microstate counts into adding entropies.
- **[[Laws and Theorems]]** — the second law is the vault's cleanest example of a *statistical* law: not a theorem proved from axioms, not an absolute decree, but a statement true at odds so long it is indistinguishable from certainty. Boltzmann is the case study for "what kind of truth a physical law is."

## Receipts

- *Ludwig Boltzmann*, Wikipedia, and the MacTutor History of Mathematics biography (St Andrews) — accessed 2026-06-16 for the life, the 5 September 1906 death at Duino, the mental-health history, and the Lübeck 1895 debate with Ostwald.
- *Boltzmann's Work in Statistical Physics*, Stanford Encyclopedia of Philosophy — the H-theorem, the *Stosszahlansatz*, and Boltzmann's evolving replies to Loschmidt and Zermelo.
- *Loschmidt's paradox*, Wikipedia — the 1876 reversibility objection and the molecular-chaos assumption it exposed; Zermelo's 1896 recurrence objection from Poincaré recurrence.
- On the constant and the formula's authorship: standard history-of-physics accounts that Planck introduced $k$ and wrote $S = k \log W$ in his 1900 blackbody work, naming $k$ after Boltzmann (the "$W$ = *Wahrscheinlichkeit*" point and the Planck attribution are widely documented, e.g. the *Boltzmann tombstone* entries and history-of-thermodynamics references).
- R. Newburgh et al., "Einstein, Perrin, and the reality of atoms: 1905 revisited," *Am. J. Phys.* 74 (2006) — Einstein's 1905 Brownian-motion theory, Perrin's 1908 experiments, the convergence of Avogadro's number, and Ostwald's concession.
- For the information-theory bridge, the von Neumann naming anecdote, and Landauer's principle: **[[Information Theory]]** (vault card) and its receipts.
- *S = k log W* tombstone, Vienna Zentralfriedhof Section 14C — photographs and the BSHS Vienna travel guide / Atlas Obscura "Boltzmann's Grave."

> **Sensitive-topic note.** This card recounts a historical death by suicide. It is included as biography, told without detail. If this subject touches you personally, it's worth reaching out to someone you trust or a local support line.
