---
chinese: 蓝光二极管 (lánguāng èrjíguǎn)
prerequisites:
  - "[[Input and Output Devices]]"
leads_to:
  - "[[Semiconductors]]"
tags:
  - type/story
  - subject/physics
  - era/20c
  - era/21c
  - cast/nakamura
  - cast/ogawa
  - cast/akasaki
  - cast/amano
  - region/japan
---

# The Blue LED 蓝光二极管

> *For thirty years, humanity could make light-emitting diodes in red and in green — but not in blue. Without blue there is no white, and without white an LED is a glowing indicator, not a lamp. The whole industry knew which crystal would crack the problem, and bet accordingly. The man who actually cracked it worked for a phosphor company nobody had heard of, on an island most Japanese couldn't place on a map, using a reactor he re-welded himself every morning — on the one material everyone agreed was hopeless.*

![[blue-led-comic.png|640]]

## Cast of Characters

- **Shuji Nakamura 中村修二** (b. 1954) — engineer at Nichia Chemical, Tokushima. No PhD, no elite degree, no research budget — and, eventually, no patience left. His memoir is titled *Breakthrough with Anger*.
- **Nobuo Ogawa 小川信雄** (1912–2002) — founder and chairman of Nichia. At 76, listened to a mid-ranking engineer propose spending a few percent of the company's yearly sales on a "impossible" project — and said yes on the spot.
- **Isamu Akasaki 赤崎勇** (1929–2021) & **Hiroshi Amano 天野浩** (b. 1960) — professor and doctoral student at Nagoya University, the academics who kept gallium nitride alive when the field abandoned it — and got there first on the two hardest steps.
- *Cameos:* **Nick Holonyak** (the red LED, 1962), **Herbert Maruska & Jacques Pankove** (RCA's dim violet GaN glow, 1972 — the road not taken).

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| light-emitting diode (LED) | 发光二极管 | a semiconductor junction that turns current directly into light |
| band gap | 带隙 / 能隙 | the energy step an electron falls down — which sets the photon's colour |
| gallium nitride (GaN) | 氮化镓 | the "hopeless" crystal that blue actually came from |
| zinc selenide (ZnSe) | 硒化锌 | the beautiful crystal the whole industry bet on instead |
| p-type doping | p 型掺杂 | seeding a crystal with positive charge carriers — GaN's "impossible" half |
| phosphor | 荧光粉 | the glow-powder that turns blue light into white — Nichia's home turf |
| candela | 坎德拉 | roughly one candle's worth of light — the brightness that changed everything |

## Act I — The missing colour (1962–1988)

In 1962, Nick Holonyak at General Electric made a semiconductor junction glow **red**. The physics is beautifully direct: push an electron across a diode's junction and it falls down an energy step — the **band gap** — and the height of that fall *is* the photon: $E = hf$. Small step, red light. By the seventies there was green. And that is where the palette stopped.

Blue is a high-energy photon, so blue needs a **tall** step — a wide-band-gap crystal, grown nearly perfect, and doped both n-type *and* p-type so a junction can exist at all. For thirty years, blue was always "ten years away." The stakes were not decorative: red + green + **blue** is the full kit — screens that can show every colour, and above all *white light from a chip*, lighting that could retire the light bulb.

Two crystals could plausibly do it. **Zinc selenide** grew like a jewel — its atoms spaced almost perfectly to sit on cheap gallium-arsenide wafers, so laboratories could make gorgeous, low-defect crystals. **Gallium nitride** had no matching wafer at all: grown on sapphire, it came out riddled with defects — a billion dislocations per square centimetre — and nobody could make it p-type. RCA had coaxed a dim violet glimmer from GaN back in 1972, and the field had shrugged and moved on. By the late eighties the consensus was total: serious people did ZnSe. GaN was career suicide.

Almost everyone obeyed. In Nagoya, Isamu Akasaki and his student Hiroshi Amano did not — in 1986 they learned to grow mirror-smooth GaN by first laying down a thin low-temperature buffer layer, and in 1989 they cracked the "impossible" half: magnesium-doped GaN turned p-type under their electron-beam microscope. First real GaN junction, first real blue-violet glow — faint, but real. The door was ajar. The field, mesmerised by ZnSe, mostly declined to walk through it.

## Act II — The money-eater and the old man (1979–1988)

Shuji Nakamura grew up in a fishing village in Ehime, on Shikoku — the smallest of Japan's four main islands — a boy who made his own toys and liked physics because it felt like the instruction manual for everything else. Local university (Tokushima, not Tokyo), a master's degree, and in 1979 a job at **Nichia Chemical**: a family firm in rural Anan that made **phosphors** — the glow-powders inside fluorescent tubes and CRT televisions.

For ten years he developed exactly what he was told to: gallium metal, red and infrared LEDs — commodity products, years behind the giants, that barely sold. Colleagues had a nickname for him: **金食い虫** — *the money-eater*. He later said he came within a breath of quitting.

Instead, in 1988, he did the thing that makes this a story: he walked past the entire management chain into the office of the founder himself. Nobuo Ogawa was seventy-six. Nakamura asked for roughly **¥500 million** — a slice worth a few percent of everything Nichia sold in a year — plus a year in Florida to learn crystal-growth, to develop the blue LED that had defeated Matsushita, Toshiba, Sony, and every laboratory that had tried.

Ogawa said, in effect: *do it.* By most accounts the answer took less time than the question. An old founder who had built the company from a shed, choosing one more fight over a quiet balance sheet — the yes cost him nothing to say and everything to mean, and Nakamura never forgot it. (The sequel is harder: within a few years Ogawa had stepped back, and the company that inherited the bet did not love it — orders came down to stop the GaN "hobby". Nakamura ignored them and kept growing crystals. Insubordination is a load-bearing element of this story.)

Florida supplied the second fuel. At the university lab he was treated as a technician, not a scientist — no PhD, no publications, not invited to the meetings. He returned to Tokushima in 1989 carrying a private vow about papers, and a decision that looks insane until you hear his reasoning.

## Act III — Choosing the impossible on purpose (1989–1992)

Nakamura chose **gallium nitride** — *because* everyone else was on zinc selenide. His logic was the latecomer's logic, and it is worth teaching: in a crowded race, a small company arriving last loses to incumbents no matter how well it runs; in an empty race, stubbornness is a monopoly. If GaN worked, there would be nobody to share it with.

Then he out-worked the problem in the most literal sense. Commercial crystal reactors couldn't grow good GaN, so he rebuilt his: **mornings with a welding torch, modifying the machine; afternoons growing crystals; repeat.** Out of that daily cycle came the **two-flow MOCVD** reactor — a second gas stream pressing straight down, pinning the reactants onto the hot sapphire — and suddenly his GaN was the best in the world. (He also swapped Akasaki's buffer recipe for a low-temperature GaN buffer of his own. The welder and the crystal-grower were the same person; that was the whole advantage.)

Then came the discovery that turned a recipe into science. Nagoya's p-type trick — electron-beam irradiation — was slow, shallow, and mysterious. In 1992 Nakamura's group showed that simple **thermal annealing** did the job completely, and *why*: hydrogen atoms from the growth gas had been quietly handcuffing the magnesium acceptors (Mg–H complexes). The electron beam had only ever been heating the crystal. Break the handcuffs with heat, and p-type GaN was not a miracle — it was a procedure. Any question that has an answer like that was never impossible; it was just unexplained.

## Act IV — One candela (1993–1996)

He still needed the light itself to be bright, which meant sandwiching a layer of **indium** gallium nitride — a notoriously fussy alloy — between the doped layers as the quantum well where electrons fall. He got InGaN to behave when nobody else could. In **November 1993**, Nichia announced a blue LED of **one candela** — a hundred times brighter than anything before it, bright enough to see across a sunlit room. A phosphor company from Tokushima, population: agriculture, had just lapped the global electronics industry.

The endgame was pure poetry. White light arrived in 1996 as **a blue Nichia chip shining through a yellow phosphor** — and phosphors were the one thing Nichia had been world-class at all along. The company's oldest product turned its newest one into the light bulb's replacement. And in 1995–96 the same crystals were persuaded to lase: a **405-nanometre violet laser diode** — the exact finer pen that [[Secondary Storage]]'s wavelength ladder ends on. Every Blu-ray player writes with the beam this act produced.

One honest wrinkle the textbooks still enjoy: by every rule of semiconductor physics, InGaN's defect-riddled crystals should barely emit at all — a billion dislocations should murder the light. They don't, and *precisely why* GaN forgives what kills other materials was argued about for decades. The blue LED shipped before it was fully understood. Engineering sometimes runs ahead of the science that explains it.

## Act V — Two envelopes of ¥10,000 (1997–2005)

For the patent on the two-flow reactor — the machine underneath a business worth billions — Nichia paid its inventor the standard rate: **¥10,000 on filing, ¥10,000 on grant.** About $180, in two envelopes.

In 1999 Nakamura left for a professorship at UC Santa Barbara. Nichia sued *him* (via a trade-secrets action aimed at a US rival he advised). He counter-sued in Tokyo in 2001 under Article 35 of Japan's patent law, which promises employees "reasonable remuneration" for inventions — a clause everyone had treated as decorative. In January 2004 the Tokyo District Court did the arithmetic out loud: it put the patent's contribution to Nichia's profits in the tens of billions of yen, credited Nakamura with half, and awarded him the full **¥20 billion** he had claimed — the largest inventor award in Japanese history. The appeal court then squeezed the parties into settling for about **¥840 million** in 2005. Nakamura walked out of the settlement press conference and said, in English and in fury, that Japan's justice system was rotten.

He had, characteristically, both lost and won. The settlement was a fraction of the judgment — and yet it was still the largest inventor payout Japan had seen, and the case detonated inside every Japanese corporation: invention-reward rules were rewritten across the economy, and Article 35 itself was amended. The two envelopes became a national cautionary tale. (Nichia's side of the ledger deserves its honest line too: it had paid a decade of salaries for products that didn't sell, funded the ¥500-million bet, and its LED teams — not one man alone — built it into the world's largest LED maker, which it still is. "Lone genius" is the story's shape, not its full truth.)

## Act VI — The prize the dynamite always wanted (2014)

Alfred Nobel's will asks that the prizes go to those who confer "the greatest benefit to mankind," and physics committees have spent a century stretching that phrase over quarks and cosmology. In October 2014 — Akasaki, Amano, Nakamura, three ways, the credit kept fair — it fit literally. Roughly a fifth of the world's electricity was going into lighting; the white LED collapses that. An incandescent bulb squeezes out about 16 lumens per watt, a fluorescent about 70; LEDs were passing 300 in the lab. And a chip that sips current can run on a small solar panel and a battery — light after sunset for the billion and a half people no grid had ever reached. The committee wrote the epigraph themselves: *the 20th century was lit by incandescent bulbs; the 21st will be lit by LED lamps.*

Ogawa had died in 2002; he saw the blue light and the white light, but not the medal his yes had purchased. Nakamura, accepting it, pointed the credit back at the old man — the entire miracle had hinged on one unhedged decision by a 76-year-old who could have said "be sensible."

And the driver underneath it all, by the laureate's own account, was never serenity. The memoir's title is *Breakthrough with Anger*: anger at the nickname, at Florida's seating chart, at the consensus, at the envelopes. He turned every slight into crystal growth. The boy from the fishing village who made his own toys ended up making his own light — and then, because the world had priced his light at ¥20,000, he made his own justice too, at market rates.

![[blue-led-timeline.svg|697]]

## Honest edges

- **The credit is genuinely three-way.** Akasaki and Amano solved crystal quality (the 1986 buffer layer) and p-type GaN (1989) *first*; Nakamura solved brightness (InGaN), the annealing mechanism, and the industrial reality. The Nobel's three-way split is the fair reading, and this card keeps it — the "one angry genius" version erases Nagoya.
- **Prehistory:** RCA's Maruska and Pankove had a working (dim, violet, magnesium-doped) GaN emitter in 1972 — GaN's first glow predates the story's hero by two decades; RCA simply stopped.
- **Nichia's ledger:** the company funded a decade of unprofitable work and the ¥500M bet, and its teams industrialised the result; it remains the world's largest LED maker. The envelopes were indefensible; the investment was real. Both facts stay.
- **The insubordination is not varnish:** Nakamura kept working on GaN after being ordered to stop. The story's moral is not "persistence is rewarded" but the sharper "the bet was made by a founder, resented by his successors, and vindicated over their objection."
- **The physics kept a secret:** why InGaN emits brilliantly despite defect densities that kill every comparable semiconductor was debated for decades after the products shipped — a rare, humbling case of the recipe outrunning the explanation.
- **The numbers are court numbers:** the ¥20B award was capped by what Nakamura claimed (the court's own arithmetic implied roughly triple); the ¥840M settlement included interest. Precision matters because the case rewrote the law.

## Cultural ripples

- **Article 35 and after:** the 2004 judgment terrified Japanese HR departments into writing real inventor-compensation schedules, and the patent law itself was amended — the two envelopes arguably did more for Japanese inventors than any prize.
- **Blue as the bottleneck colour:** "waiting for the blue LED" became engineering shorthand for a system stuck on its last, hardest component — the other two primaries were worthless as a trio until the third arrived (a pure complements story: red and green had almost no lamp-value without blue).
- **The screens in your pocket:** every white-backlit LCD — which [[Input and Output Devices]] taught you is really an "LED screen" — and every true LED/OLED-era display descends from this act; so do Blu-ray's 405 nm pens, LED streetlights, and the solar lantern replacing kerosene across the off-grid world.
- **Hunt the cause, not the result.** The crowd bet on ZnSe because it *already glowed prettiest* — chasing the best current result. The winners hunted causes: *why* won't GaN dope? (hydrogen handcuffs) — *why* won't it grow? (gas flow) — and causes, once found, compound into procedures while results just sit there. It is [[Forward Reading and Problem Discovery]]'s thesis in laboratory form, and the inversion of how momentum-chasing works in any market: the field's consensus was, in effect, a price chart of laboratory results, and it pointed everyone at the dead end.

## Where this surfaces in the vault

- [[Input and Output Devices]] — the "LED screen" misconception (LED-backlit LCD vs OLED): the backlight that makes the modern screen possible is this story's white light.
- [[Secondary Storage]] — the CD→DVD→Blu-ray wavelength ladder (780→650→**405 nm**): the ladder's final rung is Nakamura's violet laser.
- [[Semiconductors]] — the band gap, doping, and the p-n junction, told properly.
- [[Stories/The War of the Currents]] — the electricity shelf's other bet-the-company story; Ogawa's yes belongs on the same shelf as Westinghouse's.

## Receipts

- 1962 — Holonyak, first practical visible (red) LED, GE. · 1972 — Maruska/Pankove (RCA), first dim violet GaN emitter.
- 1986 — Akasaki & Amano: low-temperature AlN buffer → device-grade GaN. · 1989 — first p-type GaN (Mg + electron-beam), first GaN p-n junction LED.
- 1988 — Nakamura's direct appeal; Ogawa approves ≈¥500M. 1988–89 Florida year. · 1990–91 — two-flow MOCVD; low-temp GaN buffer.
- 1992 — thermal-annealing p-type + the Mg–H hydrogen-passivation explanation. · Nov 1993 — 1-candela InGaN blue LED announced (≈100× prior brightness); on sale 1994.
- 1996 — white LED (blue + YAG:Ce phosphor); CW 405 nm violet laser diode (→ Blu-ray). · Patent JP 2,628,404 ("the 404"): bonus ¥10,000 + ¥10,000.
- 1999 — Nakamura to UCSB. 2001 — Article 35 suit. Jan 2004 — Tokyo District Court awards ¥20B (claim-capped). Jan 2005 — settles ≈¥843M incl. interest.
- Oct 2014 — Nobel Prize in Physics: Akasaki, Amano, Nakamura. Committee epigraph: the 21st century lit by LEDs. Lighting ≈ one-fifth of world electricity at the time; incandescent ≈ 16 lm/W, fluorescent ≈ 70, lab LEDs > 300.
