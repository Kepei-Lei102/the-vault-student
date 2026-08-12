---
chinese: 电流之战 (diànliú zhī zhàn)
prerequisites: []
leads_to:
  - "[[Lorentz Force]]"
  - "[[Maxwell's Equations]]"
tags:
  - type/story
  - subject/physics
  - era/19c
  - era/20c
  - cast/edison
  - cast/tesla
  - cast/westinghouse
  - region/usa
---

# The War of the Currents 电流之战

> *"The doctor will throw the switch."* — and on the other side of the campaign, an inventor who claimed to oppose the death penalty quietly made sure the chair ran on his rival's current.
>
> *It was sold as a fight about safety. It was really a fight about distance — and the loser had the better showmanship.*

## Cast of Characters

- **Thomas Edison** (1847–1931) — the incandescent-lamp magnate; his Pearl Street Station (1882) ran on **direct current** (DC), and his fortune was wired to it. Brilliant, relentless, and — when AC threatened him — willing to fight dirty.
- **Nikola Tesla** (1856–1943) — Serbian-American engineer; invented the **alternating-current** induction motor and the polyphase AC system. Worked for Edison briefly and miserably, quit, and sold his AC patents to Westinghouse.
- **George Westinghouse** (1846–1914) — industrialist and the actual *winner* of the war; bought Tesla's AC patents in 1888, paired them with the **transformer**, and out-engineered Edison's grid. The least mythologized and most decisive of the three.
- **Harold P. Brown** — the engineer who ran Edison's anti-AC publicity, staging public animal electrocutions to brand AC as the "executioner's current."
- **William Kemmler** (1860–1890) — convicted murderer; the first human ever executed by electric chair, made an unwilling exhibit in the currents war.

## 中文锚点

**电流之战**（diànliú zhī zhàn）：1880s–1890s 美国，三个人争夺哪一种电力制式统治世界——爱迪生（Edison）的**直流电**（zhíliú, DC）对特斯拉（Tesla）+ 威斯汀豪斯（Westinghouse）的**交流电**（jiāoliú, AC）。

表面上吵的是"安全"，**真正的胜负手是"距离"**。直流电压低，长距离输电时电流大、损耗 $P=I^2R$ 惊人——发电厂得每隔一英里建一座。交流配上**变压器**（biànyāqì, transformer）就能把电压**升高**再远距离输送（高压 → 小电流 → 损耗极小），到用户端再**降下来**。这就是交流取胜的物理原因。

故事的黑暗面：爱迪生为抹黑交流，公开电死动物、并推动用交流电做**电椅**（diànyǐ）。而广为流传的"爱迪生电死大象 Topsy"是**谣言**——见下文"诚实的边角"。

## Act I — Edison's direct-current empire (1882)

When Edison switched on the **Pearl Street Station** in lower Manhattan in 1882, he didn't just sell light bulbs — he sold an entire system, and that system ran on **direct current**. Money, patents, and reputation were all soldered to DC.

DC had one fatal flaw, and Edison knew it. At the safe, usable voltage of a household lamp (~110 V), pushing power over a wire means pushing a large *current*, and a wire's resistance turns current into wasted heat at a rate of $P_{\text{loss}} = I^2 R$. The losses pile up so fast that a DC station could only serve customers within about a mile before the lights browned out. Electrifying a city the DC way meant a power plant on nearly every block. It did not scale.

## Act II — Tesla, Westinghouse, and the alternating answer (1884–1888)

**Nikola Tesla** arrived in America in 1884 with the solution already in his head: **alternating current** and the **induction motor**. He worked for Edison just long enough to be disillusioned (a famously unpaid bonus, by Tesla's account), quit, and in 1888 sold his AC patents to **George Westinghouse**.

AC's superpower is the **transformer**. Because an alternating current's changing magnetic field can induce a voltage in a second coil (Faraday's law of induction), AC voltage can be *stepped up* and *stepped down* almost losslessly. Generate power, **transform it up to very high voltage** for the journey — high voltage means *low current* for the same power $P = VI$, and low current means almost no $I^2 R$ loss — then **transform it back down** to a safe voltage at the customer's wall. Suddenly one power station could serve a whole region. Distance was solved.

![[war-of-currents-one-per-mile-comic.png|620]]

## Act III — The campaign to make AC mean death (1888–1890)

Edison could not match the physics, so he fought the politics. Threatened by a rival current that was simply better at distance, he launched a campaign to convince the public that **AC was lethal**. His associate **Harold P. Brown** staged public demonstrations electrocuting stray dogs, then larger animals, with alternating current — theatre dressed as science. Edison's camp pushed the verb *"to be Westinghoused"* as a synonym for electrocution.

Then came the grimmest move of all. When New York sought a "humane" replacement for hanging, Edison — who said he personally opposed capital punishment — recommended **alternating current** as the surest way to kill, precisely so the public would forever associate AC with death. The state built an electric chair, and wired it for AC.

## Act IV — William Kemmler (6 August 1890)

On 6 August 1890, at Auburn State Prison, **William Kemmler** became the first person executed by electric chair. The first jolt — about 1,000 volts for 17 seconds — did not kill him. Witnesses watched him struggle; a second, longer charge of around 2,000 volts was applied, and reports describe the body smoking and catching fire before he was declared dead. It took several minutes. Westinghouse, who had quietly funded Kemmler's appeal to keep AC off the chair, said afterward: *"They would have done better using an axe."*

It was a botched, horrifying death made into a public-relations weapon. Kemmler's name belongs in this story because he was, in a real sense, collateral in a marketing war between two companies.

## Act V — AC wins (1893–1896)

The campaign lost anyway, because distance always wins. In **1893**, Westinghouse beat Edison's old company (by then merged into General Electric) for the contract to light the **World's Columbian Exposition in Chicago** — and the fair blazed with nearly 100,000 AC lamps, a dazzling public proof that AC was safe and magnificent at scale.

Then the decisive blow: the **Niagara Falls** hydroelectric project chose Westinghouse and Tesla's AC. In **1895–96** the Adams Power Plant began sending power from the falls all the way to **Buffalo, 26 miles away** — a distance DC could never have reached. That transmission is the unofficial end of the war. Within a generation, the entire planet was wired for alternating current.

![[war-of-currents-niagara-comic.png|560]]

## The physics — why AC really won

![[war-of-currents-transmission.svg|697]]

Strip away the showmanship and the war was decided by one equation, $P_{\text{loss}} = I^2 R$. To send a fixed amount of power $P = VI$ down a line, you can use high voltage and low current, or low voltage and high current. The line's heat loss depends on the **square of the current**, so halving the current quarters the loss. AC's transformer let engineers crank the transmission voltage sky-high (and the current correspondingly low), ship power hundreds of miles with trivial loss, then drop it back to a safe level at the destination. DC, with no easy way to change voltage in that era, was stuck at low voltage and high current — and so stuck close to its power plant. The "safety" argument was noise; the transformer was the whole game.

## Honest edges

**The Topsy myth — the most-repeated falsehood in this story.** You will very often read that Edison electrocuted **Topsy the elephant** in 1903 to discredit AC. This is **wrong on every count that matters.** Topsy, a circus elephant deemed dangerous after killing handlers, was put down at Coney Island's Luna Park on 4 January 1903 (by a combination of cyanide, electrocution, and strangulation). But the War of the Currents had been **over for roughly a decade** by then — AC had already won at Niagara. Edison **never visited** Luna Park, is **not mentioned in any contemporary news account** of Topsy's death, and there's no evidence he was consulted. His film company shot footage titled *Electrocuting an Elephant*, which is how his name later got fused to the event — but the popular "Edison killed Topsy to smear AC" narrative is a retrofit, debunked by the Rutgers Edison Papers. The real story is sad enough without the myth: a captive animal killed by her owners, filmed for spectacle.

**The electric chair.** It belongs in the record without sensationalizing it. Kemmler's execution was genuinely gruesome, and it was made worse by being staged inside a corporate rivalry. The vault states that plainly rather than treating it as a fun bit of trivia.

**Hero, villain, and the man who actually won.** Modern retellings flatten this into Saint Tesla versus Edison the villain. The honest version is messier: **Tesla** was a genuine visionary (the AC motor is his) who was also, later, mythologized far beyond the record; **Edison** fought ruthlessly and dishonestly here, but was not a cartoon — he was protecting a real investment and had real (if exaggerated) safety points; and **Westinghouse**, the businessman who bought the right patents and out-engineered everyone, is the one who actually delivered the AC world and is the one everybody forgets. (The vault keeps difficult figures difficult — same practice as [[Stories/Newton vs Hooke]] and [[Stories/The Calculus Priority Dispute]].)

## Cultural ripples

**The grid you are plugged into right now** is the direct descendant of this fight — AC, stepped up for transmission and down for your wall socket, at 50 or 60 Hz. Every transformer humming on a utility pole is a relic of Niagara.

**Why your travel adapter exists — and why the US is 120 V.** The *voltage* at the socket is a fossil too. Edison settled on about **110 V** because it suited his carbon-filament bulb, and when AC took over, American utilities kept that number to stay compatible with every Edison-era lamp already installed. The United States is, to this day, frozen at Edison's voltage. Most of the world electrified *later* — after higher-voltage metal-filament lamps arrived (Berlin jumped to 220 V in 1899) — and chose the higher figure for the *same reason AC beat DC*: double the voltage and the current halves, so household wiring needs less copper and wastes less to $I^2R$. The lasting split — **~120 V** (safer shock, more copper) versus **~230 V** (more efficient, more dangerous) — is the War of the Currents still humming inside your walls, and the reason a hairdryer bought in London can't go straight into a New York outlet. (The same 1890s moment also froze the US at **60 Hz** and Europe at **50 Hz**.)

And here is the joke that finishes it: **America never actually escaped the efficiency argument** — it just hid it behind the wall. US homes are fed **split-phase 240 V** (two 120 V legs, opposite in phase), and the power-hungry appliances — the electric range, oven, dryer, water heater, EV charger — quietly run on the **full 240 V**. The reason is, once again, $I^2R$: a 5 kW stove burner at 120 V would draw a fire-risk **42 A**, but at 240 V it draws **21 A** — half the current, a quarter the loss, a thinner cord. So an American kitchen runs its outlets at 120 V *for safety* and its stove at 240 V *for efficiency*, conceding Europe's whole point in the one room where the watts actually matter.

**DC's quiet revenge — the grid went hybrid.** The verdict wasn't permanent (a law, not a theorem — see [[Laws and Theorems]]). Once modern **power electronics** delivered the cheap, controllable voltage conversion Edison's era couldn't, DC came back for exactly the jobs it is best at, and the grid quietly became a *hybrid*. The everyday network is still an AC backbone — but **high-voltage DC (HVDC)** now owns three things AC can't do well: the *longest hauls* (China's 1,100 kV, ~3,300 km Zhundong–South Anhui line carries 12 GW across the country with less loss than AC could), the *undersea links* (in a long submarine cable AC drowns in its own charging current, so the cross-Channel and offshore-wind connections are all DC), and the *ties between incompatible grids* (an HVDC link can splice a 50 Hz network to a 60 Hz one, or join two unsynchronised AC grids — it is how the US's Eastern and Western interconnections shake hands). And at the *other* end of the scale, DC quietly owns the edges: solar panels, batteries, EVs, LEDs, and every phone and laptop are natively DC. The war never really ended — it settled into a division of labour: **AC where you transform voltage and spin motors, DC where you cross oceans, tie strangers together, or run a chip.** Edison is winning the matches he lost, a century late.

**Tesla as folk hero.** The late-20th-century rehabilitation of Tesla — and a certain car company taking his name — is itself a cultural artifact worth noticing: we love a misunderstood genius, and we rewrite history to give him the clean win the messy record won't quite support.

**And the band that refused to choose.** The rock band **AC/DC** got its name when Angus and Malcolm Young's sister spotted "AC/DC" on the back of a sewing machine — the label for a device that runs on *either* alternating or direct current. Edison and Tesla spent a decade insisting the world had to pick one; the Youngs just plugged in "High Voltage" and took both. Given that the modern grid ended up a hybrid, that may be the most physically accurate position anyone took in the entire war.

## Where this surfaces in the vault

- **Foreshadows the Electricity & Fields bay.** Everything here — transformers, induction, transmission — is the human prologue to the vault's electricity-and-fields physics: [[Lorentz Force]], [[Maxwell's Equations]], and the 9702 / IB / AP electricity-and-fields cards. The transformer *is* Faraday's law of induction in commercial form.
- **Sibling technology-history Stories:** [[Stories/The Boolean-to-Silicon Bridge]] — the other "an idea becomes the infrastructure we live inside" arc; and [[Stories/One Take, Many Tracks]] — the same Edison opens both, misjudging his own phonograph as thoroughly as he misjudged AC.
- **Methodology tie-in:** [[Laws and Theorems]] — the AC verdict was a *law* (a robustly-observed engineering fact), and HVDC is the experiment that partly *demoted* it; exactly the "held until conditions change" pattern.

## Receipts

- *War of the Currents* and *Electrocuting an Elephant*, Wikipedia — accessed 2026-06-04 for the chronology and the film record.
- History.com, "How Edison, Tesla and Westinghouse Battled to Electrify America" — overview of the rivalry, the propaganda campaign, the 1893 Fair, and Niagara.
- The Rutgers **Thomas A. Edison Papers**, "Myth Buster: Topsy the Elephant" — the primary debunking: Edison absent, the war already over, his name absent from contemporary accounts.
- Smithsonian Magazine, "Topsy the Elephant Was a Victim of Her Captors, Not Thomas Edison" (2014) — the corrected account.
- History.com / *History Today*, on the 6 August 1890 Kemmler execution at Auburn and Westinghouse's "an axe" remark.
- U.S. Department of Energy, "The War of the Currents: AC vs. DC Power"; and on the Adams Power Plant, Niagara → Buffalo transmission (1895–96).
- On the 110 V / 230 V legacy: Electronics360, "How the U.S. Came to Adopt 120 V While Others Use 230 V"; Wikipedia, "Mains electricity" — Edison's lamp-driven ~110 V, the US installed-base lock-in, and Berlin's 1899 switch to 220 V.
- On the hybrid modern grid: Wikipedia, "High-voltage direct current" — HVDC for long-haul, submarine cables, and asynchronous (50/60 Hz) interconnection; China's 1,100 kV Zhundong–South Anhui UHVDC line as the long-haul exemplar.
