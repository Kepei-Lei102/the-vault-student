---
chinese: 海蒂·拉玛与会跳频的钢琴 (Hǎidì Lāmǎ yǔ huì tiàopín de gāngqín)
aliases:
  - Hedy Lamarr
  - George Antheil
prerequisites: []
leads_to: []
teach_together:
  - "[[Networks]]"
tags:
  - type/story
  - subject/computer-science
  - subject/physics
  - era/20c
  - cast/lamarr
  - cast/antheil
  - region/usa
---

# Hedy Lamarr and the Frequency-Hopping Piano 海蒂·拉玛与会跳频的钢琴

> *The film star brings a communication problem. The composer brings experience with machines that are supposed to play together. Neither has arrived with the job title you expected.*

## Cast of Characters

- **Hedy Lamarr (1914–2000)** — born Hedwig Kiesler in Vienna; Hollywood actor and co-inventor, named Hedy Kiesler Markey on the patent.
- **George Antheil (1900–1959)** — American composer, pianist and co-inventor; someone for whom keeping machines in time was already a practical problem.
- **The listener who should hear** — a receiver which must follow its transmitter.
- **The listener who should not interfere** — an adversary who would like to make the useful signal disappear under another one.

## 中文锚点

用对讲机聊天，碰上同一个频道里有人一直大声说话，光把自己的话讲得更清楚也没用。要是你和朋友事先约好，每隔一会儿就一起换到下一个频道，对方守着一个频道吵，就只能挡住你们的一部分交谈。难点在“一起”：你换了，朋友没跟上，你们自己也听不见彼此了。海蒂·拉玛和作曲家乔治·安泰尔想到用两卷按同一节奏转动的打孔纸卷，让两端的无线电同步换频；纸卷借的是自动钢琴的办法，当然不是把一架钢琴塞进鱼雷。一个常被人只盯着长相看的演员，一个琢磨过怎么让机器合奏的作曲家，把各自的经验接到了一起。今天蓝牙耳机也会通过跳频来减少干扰，但那已经是许多人接力改进后的技术，不是当年那套纸卷装置。

## Prologue — The wrong people for the job

There is a particular kind of surprise that says more about the audience than about the person on stage.

*A film star? An inventor?*

The surprise assumes that the first description should have used up the person.

Lamarr's collaboration with Antheil gives that assumption a wonderfully awkward object to explain: **US Patent 2,292,387**, granted on 11 August 1942, to both of them. Its title is the unglamorous **“Secret communication system.”** Behind the title is a proposal to change the tuning of two radios together. [The patent](https://patents.google.com/patent/US2292387A/en)

The glamorous part is not the claim of magic. It is the collision of experiences that made the proposal imaginable.

## Act I — Before Hollywood, a music box

The National Women's History Museum recounts a childhood in which Lamarr's father explained machines during walks and she took apart a music box to discover its workings. Treat the music-box episode as a reported biographical anecdote, not a preserved childhood experiment. Her mother was a pianist; music and mechanism were not strangers in the same house. [NWHM biography](https://www.womenshistory.org/education-resources/biographies/hedy-lamarr)

A music box contains a useful provocation. You can enjoy the tune, or ask what makes the next note happen. These are compatible pleasures. Nothing requires you to choose between having an artistic life and wanting to see behind a mechanism.

Lamarr became an actor, married the Austrian arms manufacturer Fritz Mandl in 1933, and left him in 1937. The museum describes the marriage as controlling. She reached London, met MGM's Louis B. Mayer, and built a Hollywood career. The outline is sufficiently dramatic without treating every colourful escape story as established fact. [NWHM biography](https://www.womenshistory.org/education-resources/biographies/hedy-lamarr)

On screen, audiences could see an image carefully lit and framed. An interest in how machinery worked did not necessarily fit inside that frame.

The childhood thread matters here: the questions a person asks in private need not resemble the role other people recognise in public.

## Act II — A composer with a synchronisation problem

Antheil was an avant-garde composer whose *Ballet Mécanique* involved player pianos. He had attempted—and failed—to synchronise sixteen of them in early performances. The Smithsonian's account also records his 1924 French patent for a device that recorded keyboard activity onto a moving paper roll. This was musical experience with an engineering underside. [Smithsonian finding aid, Historical](https://sova.si.edu/record/nmah.ac.1590)

A player piano is a machine reading instructions from a moving strip. The perforations determine which notes are played; the strip's movement determines when.

Now imagine several machines reading the right instructions at slightly different times. Each can be locally correct and the ensemble can still be a disaster.

That is a useful failure to have met before someone asks you how two radios might change their tuning together.

Lamarr and Antheil met in 1940 at the home of Janet Gaynor and Gilbert Adrian. Their subsequent work concerned radio control and resistance to jamming. The Smithsonian preserves a notebook of sketches and correspondence with patent attorneys and the National Inventors Council. There is paperwork behind this collaboration, not merely a later celebrity legend. [Smithsonian collection](https://sova.si.edu/record/nmah.ac.1590)

The meeting of disciplines is easy to romanticise. The documents point to something more demanding: explaining an idea well enough that another person can turn it into mechanisms, drawings and claims.

## Act III — Move the conversation, together

A radio receiver is selective. It listens around a chosen carrier frequency rather than treating every radio signal as the same conversation. If interference occupies that channel, a useful signal can become difficult to recover.

Here is an everyday analogy, with the machinery temporarily removed. You and a friend agree on a sequence of rooms. Every minute, both move to the next room. Someone who stays in one room shouting can disrupt only the visits to that room.

But if your friend follows the same list **one minute late**, the shouting is no longer your only problem. You may never meet.

The problem has two halves:

1. **Spread the exposure:** avoid spending the whole conversation in one vulnerable place.
2. **Preserve coordination:** make sure the intended listener follows.

![[lamarr-hopping-schedule.svg|850]]

*An invented four-channel teaching schedule, not a reconstruction of the patent's electronics. Green marks successful slots in an idealised model; red marks interference or mismatched tuning. Real reception depends on signal strength, bandwidth, timing and receiver design.*

The patent proposed synchronised perforated records, borrowing a familiar player-piano mechanism. It discusses 88 possible frequencies by analogy with 88 paper-roll tracks. Its illustrated example is smaller and includes dummy transmissions that the intended receiver ignores. **Eighty-eight is an example of capacity, not a magical radio number.** [Patent description and drawings](https://patents.google.com/patent/US2292387A/en)

The roll is a schedule. It is not a source of musical sound travelling through the sea.

![[lamarr-piano-comic.png|950]]

*An imagined 1940s-style editorial joke. The dialogue and George's piano-sized misunderstanding are invented, not quotations or a documented meeting. The real proposal borrows a paper-roll control mechanism.*

The patent also addresses starting the two records together and maintaining their timing. That detail deserves as much attention as hopping itself. Saying “both devices change” describes the desired result; synchronisation is the machinery that makes *both* mean *together*. [Patent, synchronisation and starting arrangement](https://patents.google.com/patent/US2292387A/en)

### Try losing the beat

Use the same eight-slot schedule as the figure:

```python
schedule = [1, 4, 2, 3, 1, 2, 4, 3]
jammed = {2}

def received(tx, rx, blocked):
    if len(tx) != len(rx):
        raise ValueError("Compare equal-length time windows")
    return sum(a == b and a not in blocked for a, b in zip(tx, rx))

fixed = [2] * len(schedule)
late = schedule[-1:] + schedule[:-1]  # steady repeating cycle, one slot late
print(received(fixed, fixed, jammed))       # 0 of 8
print(received(schedule, schedule, jammed)) # 6 of 8
print(received(schedule, late, jammed))     # 0 of 8
```

This is a counting model, not a radio simulator. It assumes a blocked channel always fails and a matched clear channel always succeeds. Change the blocked channel to `{1, 2}`: the aligned hopping link now succeeds in four slots. Remove interference entirely: aligned radios succeed in all eight, while this particular one-slot-late schedule still fails throughout.

The lesson is not that hopping guarantees safety. A jammer covering every available channel defeats this model; a predictable sequence can be followed; timing errors can defeat your own receiver. Nor does changing carrier frequency automatically encrypt the message or authenticate the sender. **Resistance to one kind of interference is one property, not every property called “security.”** [[Encryption]] and [[Data Security]] concern additional problems.

## Act IV — A patent is not a deployment

The Navy did not adopt the wartime proposal. Lamarr instead contributed to the war effort through her celebrity, including war-bond work. The National Women's History Museum records both the rejection and the much later recognition of her invention. [NWHM biography](https://www.womenshistory.org/education-resources/biographies/hedy-lamarr)

A familiar retelling says officials imagined fitting an entire piano inside a torpedo. Naval historian accounts attribute that explanation to Antheil. It is an account of the rejection, not a verbatim engineering-board transcript—and it is not enough to establish every reason the proposal failed to proceed. [US Naval Institute, historical account](https://www.usni.org/magazines/naval-history-magazine/2019/april/naval-warfare-and-most-beautiful-woman-world)

The distinction matters. A good joke can preserve an experience of being misunderstood. It can also become so satisfying that it replaces the harder question of what actually happened.

We do not need an imaginary room full of fools to recognise a frustrating outcome: two people did substantial inventive work, secured a patent, and did not see the wartime system they proposed put into service.

Nor should we turn invention into a harmless parlour game. Their intended application was military: controlling a weapon. The later friendliness of a wireless headset does not erase the purpose of the original proposal.

## Act V — Recognition arrives on a different clock

In 1997, the Electronic Frontier Foundation honoured Lamarr and Antheil with a special Pioneer Award. Antheil had died in 1959; Lamarr lived until 2000. Both entered the National Inventors Hall of Fame in 2014. Recognition did not arrive in time for both collaborators to receive it. [EFF award archive](https://w2.eff.org/awards/98pioneer.html), [NIHF: Antheil](https://www.invent.org/inductees/george-antheil), [NIHF: Lamarr](https://www.invent.org/inductees/hedy-lamarr)

The temptation now is to repair neglect with an equally simple overcorrection: *she invented all the wireless technology in your pocket*.

That gives her a larger monument and a less accurate achievement.

Lamarr and Antheil deserve credit for their documented collaboration and particular system. Bluetooth, Wi-Fi and satellite navigation have different technical histories and many contributors. Showing that two systems use related ideas is not, by itself, evidence that one was directly built from the other. The interesting historical question is transmission of knowledge, not resemblance alone.

## Cultural ripples — The music is finally in your ears

Bluetooth provides a concrete modern comparison. Its adaptive frequency hopping changes channels and can avoid channels suffering persistent interference. That helps devices coexist in a crowded radio band. The shared schedule is now electronic; there is no paper roll in an earbud. [Bluetooth SIG: adaptive frequency hopping](https://www.bluetooth.com/blog/how-bluetooth-technology-uses-adaptive-frequency-hopping-to-overcome-packet-interference/)

When your headphones keep playing amid other wireless devices, one part of the explanation is coordination in a noisy shared environment. Hopping is not the whole explanation, and it does not make dropouts impossible.

That is close enough to daily life to make the older problem tangible, without claiming your earbuds are a miniature version of the 1942 apparatus.

The most durable human connection may be simpler still. Lamarr's acting career did not exhaust her curiosity. Antheil's musical work had left him with an unusually relevant technical problem. Their collaboration gave those experiences a place to meet.

The piano did not have to go into the torpedo.

Something learned from trying to make pianos cooperate did.

## Connections

- **[[Networks]]** — shared media, interference and the agreements that let devices communicate.
- **[[Electromagnetic Spectrum]]** — carrier frequency belongs to the physical signal; changing it is not making the wave travel faster.
- **[[Decouple and Recouple]]** — a mechanism useful in one setting becomes a component in another.
- **[[Grace Hopper and the Nanosecond]]** — the gap between a memorable legend and an achievement worth describing accurately.
- **[[Encryption]] / [[Data Security]]** — confidentiality, authentication and availability are different requirements.

## Receipts

- [US Patent 2,292,387, *Secret communication system*](https://patents.google.com/patent/US2292387A/en) — filed 10 June 1941; granted 11 August 1942. The primary technical document; a patent is evidence of a disclosed design, not proof of operational success.
- [Smithsonian: Hedy Lamarr and George Antheil Invention Papers](https://sova.si.edu/record/nmah.ac.1590) — catalogue and historical account, including the notebook and correspondence. The catalogue was consulted; the entire archival collection was not independently examined.
- [National Women's History Museum: Hedy Lamarr](https://www.womenshistory.org/education-resources/biographies/hedy-lamarr) — biographical context. Childhood anecdotes are identified as reported; broad wireless-credit slogans are not adopted.
- [US Naval Institute: *Naval Warfare and the Most Beautiful Woman in the World*](https://www.usni.org/magazines/naval-history-magazine/2019/april/naval-warfare-and-most-beautiful-woman-world) — the piano misunderstanding attributed to Antheil, rather than staged as an established transcript.
- [EFF's 1998 award announcement](https://w2.eff.org/awards/98pioneer.html) — lists Lamarr and Antheil among the preceding year's honorees.
- [NIHF: Lamarr](https://www.invent.org/inductees/hedy-lamarr) and [Antheil](https://www.invent.org/inductees/george-antheil) — recognition and biographical dates.
- [Bluetooth SIG: *How Bluetooth technology uses adaptive frequency hopping to overcome packet interference*](https://www.bluetooth.com/blog/how-bluetooth-technology-uses-adaptive-frequency-hopping-to-overcome-packet-interference/) — modern mechanism, not evidence of a simple patent-to-product lineage.
