---
chinese: "阿基米德与那个士兵 (Ājīmǐdé yǔ nàge shìbīng) — 别碰我的圆"
prerequisites:
  - "[[Density and Pressure]]"
  - "[[Surface Area and Volume (Vocab)]]"
  - "[[Integration]]"
leads_to:
  - "[[The Calculus Priority Dispute]]"
  - "[[Centres of Mass by Integration]]"
tags:
  - type/story
  - subject/mathematics
  - subject/physics
  - domain/geometry
  - domain/fluids
  - domain/calculus
  - era/3bc
  - era/1bc
  - era/20c
  - cast/archimedes
  - cast/hiero
  - cast/marcellus
  - cast/cicero
  - cast/galileo
  - cast/heiberg
  - region/sicily
  - region/rome
---

# Archimedes and the Soldier 阿基米德与那个士兵

> *He had asked for one thing to be carved on his grave: not his name, not the machines that had held off a Roman army for two years, but a sphere inside a cylinder, and the fraction two-thirds. A hundred and thirty-seven years later a young Roman tax official found the stone under brambles, because the city that had been saved by him had forgotten where he was.*

## Cast of Characters

- **Archimedes** (c. 287–212 BC) — of Syracuse, the Greek city on Sicily's east coast; probably studied at Alexandria; the greatest mathematician of antiquity and, reluctantly, its greatest engineer.
- **Hiero II** (c. 308–215 BC) — king of Syracuse for fifty-four years, Archimedes' kinsman or friend, who commissioned the crown, the great ship *Syracusia*, and the war machines, and kept the peace with Rome.
- **Marcus Claudius Marcellus** (c. 268–208 BC) — the Roman general who besieged Syracuse for two years, took it, and wept for the man his soldier killed.
- **The soldier** — unnamed in every source. Livy says he did not know whom he was killing.
- **Marcus Tullius Cicero** (106–43 BC) — as quaestor of Sicily in 75 BC, found the tomb.
- **Vitruvius** (1st c. BC) and **Plutarch** (c. 46–120) — the Roman architect who told the bath story and the Greek biographer who told the death; neither had met him, and both are all we have.
- **Galileo Galilei** (1564–1642) — at twenty-two, worked out how the crown must really have been tested.
- **Johan Ludvig Heiberg** (1854–1928) — the Danish philologist who, in a Constantinople library in 1906, read the *Method* through a prayer book.

## 中文锚点

**阿基米德**（Archimedes，约公元前 287–212）是叙拉古人——叙拉古是西西里岛东岸的一座希腊城邦。人人都知道他从澡盆里跳出来喊"**我找到了**"的故事：国王希伦怀疑金匠在王冠里掺了银，阿基米德在澡盆里发现身体排开的水和自己的体积一样多。这张卡先把这个故事**算了一遍**：一顶一罗马磅重的王冠，把其中一成黄金换成了银，比同重的纯金王冠只多排开 1.4 立方厘米的水，在一个脸盆里水面只升高**十分之一毫米**——公元前 250 年根本量不出来。伽利略二十二岁时指出了这一点：阿基米德真正用的一定是**天平**——王冠和等重的金块在空气里平衡，一起浸入水里，天平就会倾斜，那是 1.4 克的差别，一眼就能看见。这正是阿基米德自己在《论浮体》里写下的原理，也是[[Density and Pressure|密度与压强]]那张卡的定理。他真正的骄傲不是王冠：是用 96 边形把 π 夹在 $3\tfrac{10}{71}$ 和 $3\tfrac17$ 之间（这张卡照他的办法重算了一遍）；是**球的体积和表面积都恰好是其外切圆柱的三分之二**——他要求把这个图刻在自己墓上；是《数沙者》里为了数清填满宇宙要多少粒沙子而造出的一套能写到 $10^{8\times10^{16}}$ 的记数法；是《方法》里用杠杆**称**面积的办法——微积分的雏形，失传两千年，1906 年才在一本被刮掉重写的祈祷书底下被读出来。公元前 214 年罗马人围城，他的抛石机和"铁爪"把罗马舰队挡了两年；公元前 212 年城破，一个士兵在他画图时把他杀了——普鲁塔克记了三个版本，最出名的那句"**别碰我的圆**"其实出自更晚的罗马作家。罗马统帅马塞卢斯为此难过。一百三十七年后，年轻的西塞罗在叙拉古当财务官，在荆棘丛里找到了那块刻着球和圆柱的墓碑——连叙拉古当地人都已经不知道它在哪儿了。

## The Story

### Act I — The bath, and what he cannot have done in it

The story everyone knows is told by Vitruvius, a Roman architect writing two centuries after the event, in a book about buildings. Hiero had given a goldsmith a weight of gold for a votive crown; the crown came back weighing the same, and a rumour said silver had been mixed in. The king asked Archimedes to find out without damaging it. Archimedes, worrying at the problem, went to the public baths, noticed as he sat down that the water rose and ran over in proportion to how much of him went under, and saw the answer: *volume*, which he could not measure on a crown of twisted leaves, could be measured as displaced water. He ran home naked through the streets shouting *heurēka* — I have found it — and, Vitruvius says, filled a vessel to the brim three times, lowering in the crown, then an equal weight of gold, then of silver, and compared the overflow.

![[archimedes-eureka-comic.png|720]]

*Syracuse, c. 250 BC, as Vitruvius tells it. The crown waits by the door. Whether any of it happened is the subject of Act II, but the shout is the one Greek word most people know, and it is the right word: not "I have thought of it" but "I have* found *it".*

Here is the trouble, and it took the vault's own script to make it vivid. `archimedes-crown.py` takes a crown of one Roman pound, $327$ g, with a tenth of its gold replaced by silver. Its volume exceeds the pure gold's by $1.4\ \text{cm}^3$. In a basin twenty centimetres across, that is a rise of **five hundredths of a millimetre** — less than the meniscus, less than the splash, less than anything a Greek could measure. Vitruvius's method cannot have worked.

### Act II — What he must have done instead, and the book that says so

In 1586 a twenty-two-year-old Galileo, not yet famous for anything, wrote a short essay called *La Bilancetta*, the little balance, arguing exactly this. Archimedes had written a whole treatise on the physics of floating; he would not have needed a bowl. Hang the crown on one arm of a balance and an equal weight of pure gold on the other, so they balance in air. Lower the whole balance into water. Each side now loses weight equal to the water it displaces — the upthrust of *On Floating Bodies*, Proposition 7, in the author's own words: *a solid heavier than a fluid will, if placed in it, descend to the bottom, and the solid will, when weighed in the fluid, be lighter than its true weight by the weight of the fluid displaced.* The crown, being bigger, displaces more and loses more, and the beam tips. The script does that too: the difference is $14$ mN, a gram and a half on a scale, visible from across the room. And from the crown's weight in air and in water alone, its density comes out as $17\,800\ \text{kg m}^{-3}$ against gold's $19\,300$: the goldsmith is found out with no basin at all.

That principle, upthrust equals the weight of fluid displaced, is what [[Density and Pressure]] derives from the pressure on an object's top and bottom. Archimedes derived it differently — from a postulate about fluid pressing on fluid, and a set of propositions on what floats, how deep, and how it rights itself — and then, in Book II, did something no one would do again for eighteen centuries: he worked out the stable floating positions of a paraboloid of revolution, which is the theory of why a ship of a given shape and loading does or does not capsize. Naval architects still use the word he needed: *metacentre* is later, but the problem is his.

### Act III — What he was actually proud of

He thought the crown was a parlour trick. What he wanted remembered was geometry, and three results in particular.

**The circle.** No one could say what the ratio of a circle's circumference to its diameter was; he showed how to trap it. Inscribe a regular hexagon in the circle and circumscribe one about it: the circumference lies between the two perimeters. Double the sides — twelve, twenty-four, forty-eight, ninety-six — and the trap closes. At each doubling he needed a square root, and he bounded every one by hand with fractions, rounding the inner perimeter down and the outer one up so the bounds stayed honest. The result, *Measurement of the Circle*, Proposition 3:

$$3\tfrac{10}{71} < \pi < 3\tfrac{1}{7}.$$

![[archimedes-pi-polygons.svg|1000]]

*`archimedes-pi.py` repeats the four doublings with exact arithmetic and lands on $3.14103 < \pi < 3.14272$; his hand-rounded fractions sit just outside, $3.14085$ and $3.14286$, exactly as honest rounding must leave them. The upper bound is the $22/7$ that schools taught for two thousand years.*

**The sphere.** *On the Sphere and Cylinder* proved that a sphere's volume is two-thirds of the volume of the cylinder that just contains it, and its surface two-thirds of that cylinder's total surface — the formula $V = \tfrac43\pi r^3$ that [[Surface Area and Volume (Vocab)]] states, and the hat-box theorem that [[Centres of Mass by Integration]] uses to skip an integral. He said this was the finest thing he had done, and asked that the figure be carved on his tomb.

![[archimedes-sphere-cylinder.svg|760]]

**The sand.** Greek numbers stopped at a myriad myriads, $10^8$, and the word for anything larger was "innumerable". *The Sand Reckoner*, addressed to Hiero's son, set out to count the grains of sand that would fill not the Earth but the whole universe — and, to make the universe as large as anyone had dared, he took Aristarchus's model with the Sun at the centre and the fixed stars enormously far away, the first surviving mention of heliocentrism. Then he built a number system to hold the answer: orders of $10^8$, periods of $10^8$ orders, up to $10^{8 \times 10^{16}}$. The sand came to fewer than $10^{63}$ grains. `archimedes-sand.py` follows his chain of overestimates — a poppy seed of ten thousand grains, forty seeds to a finger-breadth, ten thousand finger-breadths to a stadion, a universe $10^{14}$ stadia across — and gets his $10^{63}$ exactly. He had built a tower to $10^{80\,000\,000\,000\,000\,000}$ to house a number on its eighth floor, to show that "innumerable" was a failure of notation, not of the world.

### Act IV — The Method, and the prayer book

There was a fourth thing, and for two thousand years nobody knew it existed. In a letter to Eratosthenes at Alexandria — *The Method of Mechanical Theorems* — Archimedes explained how he actually *found* his results before proving them. He imagined a figure cut into infinitely thin slices, hung the slices on a lever, and balanced them against the slices of a figure whose volume he knew: an area weighed against an area. It is integration by another name, eighteen centuries before Cavalieri and nineteen before [[The Calculus Priority Dispute]], and he was careful to say it was a method of discovery, not of proof; the proofs he then supplied by exhaustion, the rigorous double-bounding of Act III.

The letter was copied in Constantinople in the tenth century, and in the thirteenth a monk scraped the ink off the parchment, cut the leaves in half, and wrote a prayer book over them. In 1906 Heiberg, following a catalogue note, read the ghost of the older text under the prayers with a magnifying glass and published the *Method*. The book then vanished for most of the twentieth century, reappeared at Christie's in 1998 with forged illuminations painted over some pages, sold to an anonymous buyer for two million dollars, and spent a decade at the Walters Art Museum in Baltimore under ultraviolet, X-ray fluorescence and a particle accelerator. What came out included a passage nobody had read: Archimedes counting the ways a puzzle called the *Stomachion* could be assembled — combinatorics — and, in the *Method*, treating his infinitely many slices as an actual infinite collection and comparing two such collections one to one. Cantor's move ([[Cantor vs Kronecker]]), on a lever, in 250 BC.

### Act V — The siege

Hiero died in 215, in the middle of the Second Punic War, and his teenage grandson took Syracuse over to Carthage. Rome sent Marcellus. In 214 the fleet came under the sea walls with sambucae — scaling ladders mounted on lashed-together ships — and Polybius, Livy and Plutarch all describe what happened next in the same astonished tone. Catapults of graded ranges, so that a ship was under fire from the moment it was in sight to the moment it touched the wall. Loopholes through the wall at the waterline, with scorpions behind them. And the **claw**: a beam swung out over the wall on a pivot, with a grapple on a chain that took a ship by the bow, hauled it up until it stood on its stern, and dropped it. Plutarch says the Romans came to believe they were fighting the gods, and that Marcellus, half-laughing, called Archimedes "this geometrical Briareus" — the hundred-handed giant — and gave up the assault for a blockade. Hiero had commissioned the machines years before, and Archimedes, Plutarch insists, had regarded the whole business as beneath the dignity of geometry and left no writing on it.

The burning mirrors are not in Polybius, Livy or Plutarch. They first appear four centuries later, and every modern attempt to set a ship alight with bronze mirrors from a city wall has failed; the honest edges below say why.

### Act VI — 212 BC

The city fell in 212 through a gate left unguarded during a festival. Marcellus gave orders that Archimedes was to be taken alive. Plutarch gives three versions of what happened instead, and says he cannot choose between them. In the first, Archimedes is bent over a diagram when a soldier orders him to come to Marcellus; he refuses to leave the problem unfinished, and the soldier, enraged, kills him. In the second, the soldier comes to kill him from the start, and Archimedes asks only for a moment to complete the proof. In the third, he is carrying a box of instruments — sundials, spheres, angle-measures — to Marcellus, and soldiers who think it is gold kill him for it. Livy's version is a single sentence: in the confusion of the sack, a soldier who did not know who he was.

![[archimedes-soldier-comic.png|720]]

*The courtyard, in the version the Romans themselves preferred. The famous last words are not in Plutarch: "Do not disturb my circles" —* noli turbare circulos meos *— comes from Valerius Maximus, a century and a half later, and reaches us in Latin, not Greek. What all the sources agree on is that Marcellus was distressed, turned away from the soldier as from a polluted man, and sought out the family to honour them.*

### Act VII — 75 BC

Cicero, at thirty-one, was sent to Sicily as quaestor — a junior treasury post — and, being Cicero, wanted to see the tomb of the most famous Syracusan. The Syracusans told him there was no such tomb. He remembered the sphere and the cylinder, went outside the Agrigentine gate to the old burial ground, and had the brambles cut back until a small column showed a sphere and a cylinder on its top. Verses carved beneath had half worn away. He wrote it up in the *Tusculan Disputations*, twenty-five years later, with the sting intact: one of the noblest cities of Greece, once the most learned, would have remained ignorant of the tomb of its most ingenious citizen, had a man from Arpinum not pointed it out.

![[archimedes-cicero-tomb-comic.png|720]]

*Outside the walls, 75 BC. The stone remembered what the city forgot. The tomb has not been seen since; the "Tomb of Archimedes" shown to tourists in Syracuse today is a Roman columbarium.*

![[archimedes-timeline.svg|1000]]

*The life on the left, the afterlife on the right, from `archimedes-timeline.py`. Every date in the left panel except the siege and the death is approximate; the right panel's are exact, which is its own comment on how history keeps things.*

## Honest edges

- **The bath is probably a story.** Vitruvius is the only ancient source, he wrote two centuries later, and his method does not work (Act I's numbers). Galileo's reconstruction is a reconstruction. What is certain is *On Floating Bodies* and the principle in it; the running through the streets is what a good story needed.
- **The war machines are real; the mirrors are not.** Polybius wrote within living memory of the siege and describes the catapults, loopholes and the claw in engineering detail; the claw has been rebuilt and works. The mirrors enter with Lucian and Galen in the second century AD, as a joke and an aside, and Anthemius in the sixth; MIT's 2005 trial and two television attempts charred wood and set nothing alight at ship distances. He may have used mirrors to dazzle; he did not burn the fleet.
- **"Do not disturb my circles" is Roman.** Plutarch, our fullest source, does not have it and gives three incompatible deaths; Livy has no last words. The line is Valerius Maximus's, and is best read as what Rome wanted the scene to mean: the philosopher who does not look up.
- **Marcellus's grief is in every source and may still be spin.** A conqueror who mourns the enemy's sage is a flattering figure, and Plutarch's *Life* is of Marcellus, not of Archimedes. The soldier's anonymity, at least, is honest: nobody thought him worth a name.
- **The heliocentric mention is second-hand.** Archimedes cites Aristarchus in the *Sand Reckoner* only to make his universe as big as possible, and does not endorse the model; but without that sentence we would barely know Aristarchus had proposed it.
- **Heiberg read it; the imaging finished it.** The 1906 transcription missed the *Stomachion* and the infinity passage; the 1999–2008 project at the Walters recovered them and the forged paintings' damage remains. The buyer is still anonymous.

## Cultural ripples

- **Eureka** became the English word for the moment of discovery, the motto of California, and a genre of story — Newton's apple, Kekulé's snake — in which the answer arrives unbidden in a bath, an orchard, a dream. Every one of them is told to make the years of work before it disappear.
- **The Fields Medal** carries his head and, on the reverse, the sphere in the cylinder, with the Latin *transire suum pectus mundoque potiri*: to rise above oneself and grasp the world.
- **"Give me a place to stand and I will move the Earth"** — the lever line, from Pappus — is the archetype of the engineer's boast, and the screw named for him still lifts water in the Nile delta and grain in every elevator.
- **The Palimpsest** made "palimpsest" a common metaphor and its imaging the model for reading every damaged manuscript since, from Dead Sea fragments to the carbonised Herculaneum scrolls.
- The death scene — the absorbed thinker and the uncomprehending sword — is the oldest version of a story Europe has told about itself ever since: Hypatia, Lavoisier, the burning of libraries; the claim that knowledge and force are strangers.

## Where this surfaces in the vault

- **[[Density and Pressure]]** — the principle he wrote down, derived there from pressure; Act II is why the balance, not the basin, is the instrument that uses it.
- **[[Surface Area and Volume (Vocab)]]** — the sphere's volume as *Archimedes' theorem*; the tomb marker is that card's formula carved in stone.
- **[[Centres of Mass by Integration]]** and **[[Arc Length and Surfaces of Revolution]]** — the hat-box theorem, the equal-area bands of a sphere, used there to skip an integral; it is the surface half of *Sphere and Cylinder*.
- **[[Integration]]** and **[[The Calculus Priority Dispute]]** — the *Method* is the slicing-and-summing of calculus done on a lever, found before proved, and lost before Newton and Leibniz could have read it.
- **[[Cantor vs Kronecker]]** — the Palimpsest's infinity passage: two infinite collections compared one to one, twenty-one centuries early.
- **[[Laws of Indices]]** — the *Sand Reckoner* noticed that multiplying powers of ten adds their exponents, the first law of indices, on its way to $10^{63}$.

## Receipts

- Plutarch, *Life of Marcellus* 14–19 — the siege engines, "geometrical Briareus", the three deaths, Marcellus's grief. Polybius, *Histories* VIII.5–7 — the claw and the catapults, written within a lifetime. Livy, *Ab Urbe Condita* XXV.31 — the one-sentence death.
- Vitruvius, *De architectura* IX, preface — the crown and the bath. Valerius Maximus, *Facta et dicta memorabilia* VIII.7 ext. 7 — *noli turbare circulos meos*.
- Cicero, *Tusculan Disputations* V.64–66 — the tomb, and the man from Arpinum.
- Archimedes, *Measurement of the Circle*; *On the Sphere and Cylinder*; *The Sand Reckoner*; *On Floating Bodies*; *The Method* — in T. L. Heath, *The Works of Archimedes* (1897; *Method* supplement 1912). The circle bounds are rerun in `archimedes-pi.py`, the sand in `archimedes-sand.py`.
- Galileo Galilei, *La Bilancetta* (1586) — the hydrostatic balance; the numbers in `archimedes-crown.py`.
- J. L. Heiberg, *Eine neue Archimedeshandschrift*, Hermes 42 (1907). R. Netz and W. Noel, *The Archimedes Codex* (2007) — the 1998 sale, the imaging, the *Stomachion* and the infinity passage. The Walters Art Museum, *The Archimedes Palimpsest* (2011).
- On the mirrors: D. L. Simms, *Archimedes and the burning mirrors of Syracuse*, Technology and Culture 18 (1977); the MIT 2.009 trial of October 2005.
