---
chinese: 响度战争 (xiǎngdù zhànzhēng)
prerequisites: []
leads_to:
  - "[[Sound Encoding]]"
tags:
  - type/story
  - subject/computer-science
  - era/20c
  - era/21c
  - cast/fletcher
  - cast/munson
  - cast/jensen
  - cast/lee
  - cast/bottrill
  - cast/katz
  - region/usa
  - region/europe
---

# The Loudness War 响度战争

> *For twenty-five years the record industry fought a war nobody wanted, nobody could stop, and nobody could win — each release a little louder than the last, until the music had no quiet left in it. It ended in the only way such wars ever end: not because anyone's taste improved, but because somebody agreed on how to measure the thing they were fighting over. And it is quietly still running, wherever nobody does.*

![[loudness-war-guitar-hero-comic.png|560]]

## Cast of Characters

- **Harvey Fletcher** (1884–1981) and **Wilden Munson** — Bell Labs researchers whose 1933 equal-loudness contours explain, sixty years early, why the loud version always wins the audition.
- **Ted Jensen** (b. 1954) — mastering engineer at Sterling Sound; mastered *Death Magnetic* and then publicly declined to own the result.
- **Geddy Lee** (b. 1953) and **Alex Lifeson** (b. 1953) — of Rush, who said out loud what almost no band did: *we overcooked it.*
- **David Bottrill** (b. 1962) — the producer handed an eleven-year-old album and told to mix it again, properly.
- **Bob Katz** (b. 1949) — mastering engineer and author, who campaigned against hyper-compression for a decade and then, in autumn 2013, stood up at an audio-engineering convention and declared the war over.
- **The unnamed party that actually won:** a committee at the International Telecommunication Union, and the algorithm it published in 2006.

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| loudness war | 响度战争 | the decades-long race to master records louder than the competition |
| dynamic range | 动态范围 | the distance between the quietest and loudest sounds a recording holds |
| dBFS | 满刻度分贝 | decibels relative to the loudest number the format can store — 0 is the ceiling |
| crest factor | 峰值因数 | how far the peaks stand above the average; the war's real casualty |
| brickwall limiter | 砖墙限制器 | a processor that lets nothing at all exceed a set ceiling |
| clipping | 削波 | pushing past the ceiling so the peaks are flattened into plateaus — audible distortion |
| makeup gain | 补偿增益 | the volume added back after the peaks have been held down |
| normalisation | 响度归一化 | the platform turning every track to one agreed loudness before you hear it |
| LUFS | 响度单位 | loudness units relative to full scale — one number for a whole track |
| mixing | 混音 | combining the multitrack into one balanced stereo file — the parts within the song |
| mastering | 母带处理 | preparing the finished mix for release — the song against everything else |
| object-based audio | 基于对象的音频 | placing sounds in a 3-D space and letting a renderer map them to your speakers |
| tragedy of the commons | 公地悲剧 | everyone acting rationally, and everyone ending up worse off |

## Act I — The referee was a needle (1948–1982)

The desire to be louder than the record before you is as old as records. Jukebox singles and radio promos were cut hot on purpose through the fifties and sixties, because a 45 that jumped out of the speaker got played again. What kept it from becoming a war was that vinyl had a referee, and the referee was made of metal and could not be argued with.

A vinyl master is *cut*: a lathe drives a heated stylus through a lacquer disc, carving one continuous spiral groove whose wiggles are the waveform. Louder music means wider wiggles. Wider wiggles take more radial space, so a loud record holds less music per side — and past a certain point the wiggles become so violent that the playback stylus cannot follow them and jumps out of the groove entirely. Every cutting engineer in the world therefore had a professional reason, backed by physics, to say *no, not that loud.*

That is the whole of Act I. There was an incentive to be loud, and there was a hard physical governor on it, and for thirty-odd years the governor held.

## Act II — A ceiling made of nothing (1982)

The compact disc arrives, and the governor is gone.

A CD stores sixteen bits per sample. Those sixteen bits buy about 96 decibels of range between the loudest representable sound and the quantisation noise floor — six decibels per bit, the arithmetic worked through in [[Sound Encoding]]. The largest number the format can hold is called **0 dBFS**, and it is a genuinely hard ceiling: there is no number above it, so a sample cannot be louder, ever.

Here is the trap, and it is worth reading twice, because the entire war lives in the gap between two words. **The format defends the peak. It says nothing whatever about the average.**

You cannot make the loudest instant of your record any louder than anyone else's — everybody's peak sits at the same ceiling. But you can raise the *average*, by taking the moments that stick up and pressing them down, and then turning the whole thing up until the peaks touch the ceiling again. Do that hard enough and the waveform stops looking like a landscape and starts looking like a brick. The technical name for what you have destroyed is **crest factor**: the distance from average to peak. The everyday name is *dynamics*, and it is the difference between a whisper and a shout — which is to say, most of what music expresses.

So the CD did not make anyone louder. It removed the only thing that had been stopping them.

## Act III — Why the loud one always wins the audition

None of this would matter if listeners preferred dynamics. The uncomfortable fact at the centre of the story is that, under the conditions in which records are actually judged, they don't — and they can't.

In 1933 Fletcher and Munson at Bell Labs mapped how loudness perception varies with frequency, producing the **equal-loudness contours**. The finding that matters here: the ear's frequency response is not flat, and it changes shape with level. Play something louder and the bass and the top end come up *disproportionately* — the sound doesn't merely get bigger, it gets fuller, warmer, more present, more finished.

Which means that in any comparison where the levels are not carefully matched, the louder version sounds **better** rather than merely louder. Not to fools — to everyone, including the engineer who knows exactly what is happening. Mastering studios level-match obsessively for precisely this reason. Nobody else does: not the A&R executive in the playback room, not the radio programmer, not the listener whose shuffle drops your track between two others.

So the loudness war was never a story about bad taste corrupting good art. It was a rational response to a rigged comparison, made independently by thousands of people who each had every reason to make it. Each individual choice is correct. The shared resource — the dynamic range that all music draws on to be expressive — gets consumed anyway. That is a **tragedy of the commons**, in an art form, playing out over twenty-five years.

## Act IV — The ratchet (1990s–2008)

The tool is the **brickwall limiter**: a processor with an effectively infinite ratio and a very fast attack, which simply refuses to let anything past a set ceiling. Feed it a signal, then add **makeup gain** to bring the whole flattened result back up to 0 dBFS. Repeat with the next release, harder, because the comparison set is everyone else's records and they are doing it too.

When limiting alone stops delivering, engineers reach past it into outright **clipping**: driving the signal beyond the ceiling and letting the peaks be sheared flat into little plateaus. Clipping is not a subtle loss. A flattened peak is a different waveform — squarer, harmonically richer in exactly the way a distortion pedal is — and on a rock mix it audibly grits and crunches.

The ratchet ran through the nineties and accelerated in the 2000s. Reissues became the clearest evidence, because they let you hear the same performance mastered three times across three decades, each louder and flatter than the last. The music was not being remastered. It was being pressed.

![[loudness-war-normalisation.svg|780]]

## Act V — The album whose best version was a video game (2008)

The next act turns on a distinction worth having straight, because it decides who is to blame.

> [!info] Two different jobs, and the difference is not a matter of degree
> **Mixing** takes the multitrack session — every microphone, every overdub, often hundreds of tracks — and turns it into one stereo file. The unit of work is *the track within the song*: relative levels, panning, per-instrument tone and dynamics, space, automation. The mixer works **inside** the song.
>
> **Mastering** takes those finished mixes, one stereo file per song, and prepares them to leave the building. The unit of work is *the song within the record, and the record within the world*: broad tonal correction rather than per-instrument surgery, overall level, consistency so that track three and track nine sound like the same album, running order and gaps, and the format-specific deliverables. The mastering engineer works **on** the song — deliberately a fresh, uninvested pair of ears in a room built for accuracy rather than for comfort.
>
> The one-line version: **mixing is about how the parts of a song relate to each other; mastering is about how the song relates to everything else.**
>
> The historical note explains the name. Mastering began as a *transfer* job — making the **master**, the lacquer from which discs are pressed — and the mastering engineer was originally the cutting engineer at the lathe from Act I, whose problems were physical rather than aesthetic: mono the deep bass so the stylus doesn't lift, tame the sibilance before it burns the lacquer, trade level against playing time. Taste was a by-product of keeping the disc playable.
>
> And the modern blur is what the next two acts are about. Mix engineers now routinely put a limiter across the mix bus, so mixes can arrive at mastering *already* crushed — at which point the mastering engineer's remaining options are all bad, and the name on the sleeve is theirs.

*Death Magnetic* arrived on 12 September 2008 and was, by any measure, an event: Metallica's most anticipated record in years. Within days the conversation had stopped being about the songs.

The album was clipping. Not subtly, not arguably — visibly, on any waveform display, and audibly on ordinary speakers as a persistent grit under the loud passages. Fans who had waited years came away describing their new record as fatiguing.

And then came the detail that turns a complaint into a story. Activision had been supplied with the album's **stems** — the separate instrument tracks — to build the songs into *Guitar Hero III*, and those stems had been sent *before* the crushing. So the game contained a version of the album that had never been through the final master. Players noticed. They ripped the game audio, put the two side by side, and the plastic-guitar toy won: more space, more punch, more of the record still intact.

A petition asking Metallica to remix or remaster the album passed thirteen thousand signatures. And the mastering engineer, Ted Jensen, did something engineers essentially never do — he distanced himself from his own master in public, saying the mixes had arrived at his studio already brickwalled, before he had touched them.

That last point is the honest one, and it recurs: the people usually blamed for the loudness war were most often the people who had been handed something already ruined.

## Act VI — An apology in album form (2002 → 2013)

Rush's *Vapor Trails* came out in 2002 after the worst five years of the band's life, and it was mastered so hot that the distortion is audible on the first track. This is a band with an audience that reads liner notes; the reaction was immediate and it never faded.

What makes it a story is what they did about it. Not a remaster — a **remix**, from the multitracks, eleven years later, handed to producer David Bottrill and released on 27 September 2013 as *Vapor Trails Remixed*. A band paying real money to mix an old album again, and shipping it as an acknowledgement that the first attempt was wrong.

Geddy Lee's summary, to *Rolling Stone*, is as clean an admission as the era produced: **"We overcooked it. The mixes were really loud and brash. The mastering job was harsh and distorted."**

## Act VII — The treaty was a measurement (2006–2013)

Nobody's taste changed. What changed is that loudness stopped being an argument and became a number.

In 2006 the International Telecommunication Union published **ITU-R BS.1770**, an algorithm that takes an entire piece of audio and returns one figure for how loud a human will find it — frequency-weighted to match hearing, and gated so silence doesn't drag the answer down. The scale is **LUFS**: loudness units relative to full scale. In 2010 the European Broadcasting Union turned it into policy as **EBU R 128** — broadcast to a target of −23 LUFS, with peaks kept below −1 dBTP — and European television stopped shouting during the adverts.

Then streaming adopted the same machinery, and the incentive **inverted**.

The platform measures your track and turns it *down* to the house target — Spotify settled on about −14 LUFS in 2017, with Apple Music and YouTube in the same neighbourhood. Your crushed master does not arrive louder than anyone else's. It arrives at exactly the same loudness as everyone else's, having already spent everything it had to get there.

The figure above is that reversal, drawn, using a comparison *Sound on Sound* published: a hyper-compressed remaster measuring −7.8 LUFS beside its own dynamic original at −18.8 LUFS. Normalise both to one loudness and the dynamic version's peaks still reach −4.5 dBTP while the crushed version has nothing above −13.7. **Nine decibels of headroom, at identical perceived loudness.** The record that never fought arrives sounding open; the record that fought arrives sounding flat, small and tiring, and its twenty-five-year advantage has been deleted by a multiplication.

In the autumn of 2013, at an Audio Engineering Society convention, Bob Katz — who had spent a decade arguing against hyper-compression on aesthetic grounds and losing — stood up and said the loudness wars were over. He was not describing a change of heart in the industry. He was describing a change in the arithmetic.

## Act VIII — The treaty holds where it is enforced (2021–now)

Two things have happened since, and between them they say what kind of peace this actually is.

**The first tightened it.** Immersive formats — Dolby Atmos, sold to listeners as *spatial audio* — are **object-based**: instead of mixing to a fixed speaker layout, you place sounds as objects in a three-dimensional space with metadata, and a renderer maps them onto whatever the listener actually owns, from a 7.1.4 room to a pair of earbuds. That is a story about *space*, not about dynamics; the two are different axes, and nothing about a third dimension obliges anyone to stop crushing.

Except that the format arrived with a **stricter loudness discipline built in**. Dolby's specification for Atmos music targets −18 LUFS integrated with true peak no higher than −1 dBTP — *quieter* than the stereo streaming targets — and the renderer enforces it. You cannot deliver a brickwalled immersive master and have it play as intended. And there is a second, subtler pressure: in a crushed stereo mix everything competes for the same narrow window, whereas a three-dimensional field lets you separate elements **spatially instead of by loudness**, which hands a mixer back a reason to leave the dynamics alone.

The reason the catalogue converted as fast as it did is, once again, not virtue. Apple pays a higher share of sound-recording royalties — up to about ten per cent more — for tracks available in spatial audio. Same mechanism as the LUFS treaty, one floor up: change what pays, and the behaviour follows within a year.

**The second reopened it.** Short-form video is a genuine counter-current, and it is instructive precisely because it removes every condition that made the treaty work.

- **The playback device is a phone speaker** in a noisy room. Dynamics there are not merely wasted, they are *harmful* — quiet passages do not read as restraint, they read as silence, because the ambient noise floor swallows them.
- **The comparison is instantaneous and in-feed.** You have well under a second to stop a thumb, against whatever preceded you. That is Act III's rigged A/B restored and intensified — the radio programmer's problem, now running a billion times a day.
- **The referee does not call fouls.** Normalisation on these platforms is inconsistent, and the "track" is frequently a re-upload of a re-upload, stacking generation loss on re-encoding.

The result is visible in the writing, not just the mastering: hooks moved to the very top, intros deleted, sped-up versions released as official variants. The loudness war's underlying logic — *win the first instant of the comparison* — never died. It relocated to a venue that does not measure.

Which gives the story its real moral, sharper than "the war ended." **The treaty holds exactly where the platform enforces a measurement, and lapses exactly where it doesn't.** Nothing was learned. Something was merely counted, in some places and not others.

## Honest edges

- **It is not over everywhere, and "loud" is not a synonym for "bad."** Plenty of hip-hop, punk, industrial and electronic music is *deliberately* dense — the flat, relentless wall is the aesthetic, and "restoring" its dynamics would wreck it. The war was about loudness applied as competitive strategy, not loudness as a choice.
- **Normalisation can be switched off,** and often is — Spotify lets users disable it, and club systems, broadcast playout and car radio are separate worlds with separate rules.
- **The measurement became its own fetish.** Crowd-sourced dynamic-range databases turned a production judgement into a leaderboard, and a record can score badly and still sound wonderful. Replacing taste with a number solved the incentive problem and created a smaller one.
- **The blame was usually misplaced.** Mastering engineers took the public criticism, and were frequently the last people in the chain still arguing for restraint — *Death Magnetic* is the documented case, not the exception.
- **And the ending is less noble than it sounds.** Records did not get quieter because anyone repented. They got quieter because it stopped paying to be loud. A measurement changed an incentive, and the behaviour followed. That is the actual mechanism by which the commons was saved, and it is worth being clear-eyed that no virtue was involved.

## Cultural ripples

- **The word "compression" does two unrelated jobs** in this story, and confusing them is the single most common misunderstanding in digital audio. *Data* compression makes a file smaller by removing redundancy ([[Compression]]'s territory — MP3, ZIP, JPEG). *Dynamic-range* compression makes loud parts quieter so the whole can be turned up, and changes the file's size not at all. A brickwalled master and an MP3 are two entirely different injuries; a track can suffer both, neither, or either alone.
- **A tragedy of the commons that actually got solved — in the rooms that agreed to measure** — is rare enough to be worth teaching for its own sake. The solution was not education, not appeals to artistry, and not regulation of behaviour: it was a standardised *measurement* everyone agreed to honour, which then made the destructive strategy pointless. The same shape appears in standardised time zones, the shipping container and the metre — and, as Act VIII shows, the same shape in reverse wherever the measurement is absent.
- **The recording that best represents a 2008 metal album is a plastic-guitar video game.** Preservation is not always where you'd file it.
- **Vinyl's revival gets credited with better sound,** and the physical governor of Act I is real. But a vinyl record cut from a crushed digital master inherits the crush — the format cannot give back what the master already threw away.

## Where this surfaces in the vault

- **[[Sound Encoding]]** — dual residency, and the machinery underneath every act. Sixteen bits, six decibels per bit, ninety-six decibels of range, quantisation, and the 0 dBFS ceiling: the loudness war is that budget being spent down to single digits by choice.
- **[[Logarithms]]** — decibels and LUFS are log scales, and the log-compression of human hearing is *why* louder wins the audition. That card carries the pedagogy; this one carries the consequences.
- **[[Compression]]** — the other compression, and the disambiguation above. Also the source of the deeper irony: lossy codecs throw away what you cannot hear, while brickwall limiting throws away what you can.
- **[[Stories/One Take, Many Tracks]]** — the direct prequel, and the same boundary seen from the other side. That story ends by watching the mix *become* the composition — Kingston's dub plates, Eno's studio-as-instrument — so the mixing/mastering distinction defined in Act V above is one this card needs and that one watches dissolve.
- **[[Information Theory]]** — dynamic range is channel capacity by another name. A master that uses eight decibels of a ninety-six-decibel channel is discarding bits that were already paid for and stored.
- **[[Credit Is the Currency]]** — the same structural lesson from the other side: what a field chooses to *measure* determines what its members do, far more reliably than what it claims to value.

## Receipts

- Greg Milner, *Perfecting Sound Forever: An Aural History of Recorded Music* (2009) — the standard narrative history, with the loudness war as its closing act.
- Bob Katz, *Mastering Audio: The Art and the Science* — the K-System proposal and the decade-long argument against hyper-compression; his "the loudness wars are over" declaration was made at an AES convention in autumn 2013.
- Harvey Fletcher and Wilden A. Munson, "Loudness, Its Definition, Measurement and Calculation," *Journal of the Acoustical Society of America* 5 (1933) — the equal-loudness contours, later standardised and revised as ISO 226.
- ITU-R BS.1770, "Algorithms to measure audio programme loudness and true-peak audio level" (2006, revised since); EBU R 128, "Loudness normalisation and permitted maximum level of audio signals" (2010) — the −23 LUFS target and the −1 dBTP ceiling.
- Hugh Robjohns, "The End Of The Loudness War?", *Sound on Sound* — the worked before-and-after comparison used in the figure above (−7.8 LUFS vs −18.8 LUFS as released; −13.7 dBTP vs −4.5 dBTP after normalisation to a common target).
- Spotify's own loudness-normalisation documentation for the −14 LUFS target adopted in 2017.
- On *Death Magnetic*: contemporary coverage of the clipping controversy and the *Guitar Hero III* stem comparison (September 2008); the "Re-Mix or Remaster Death Magnetic!" petition, which passed thirteen thousand signatures; Ted Jensen's statement that the mixes arrived brickwalled before mastering, reported by *Rolling Stone* and *MusicRadar*.
- On *Vapor Trails*: Geddy Lee's "we overcooked it" to *Rolling Stone*; *Vapor Trails Remixed*, mixed by David Bottrill, released by Atlantic/Rhino on 27 September 2013.
