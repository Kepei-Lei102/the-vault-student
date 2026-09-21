---
chinese: 伦理与所有权 (lúnlǐ yǔ suǒyǒuquán)
prerequisites:
  - "[[Data Security]]"
  - "[[Program Development Life Cycle and Testing]]"
  - "[[Learning as Verification]]"
  - "[[Stats Lies Hall of Fame]]"
  - "[[Automated Systems and Robotics]]"
leads_to:
  - "[[Data Protection and Privacy]]"
  - "[[Artificial Intelligence]]"
  - "[[A Rich Neighbor Named Xerox]]"
tags:
  - subject/computer-science
  - domain/ethics
  - domain/security
  - level/A-Level
  - curriculum/Cambridge-9618
  - curriculum/AP-CSA
  - curriculum/IB-CS
  - syllabus/9618-7-1
  - syllabus/AP-CSA-3-2
  - syllabus/AP-CSA-4-1
  - type/deep
  - type/definition
  - misconception/copyright-stops-copying
  - misconception/freeware-is-free-software
  - misconception/shareware-shares-the-source
  - misconception/legal-means-ethical
  - misconception/removing-the-column-removes-the-bias
  - misconception/the-computer-is-never-wrong
---

# Ethics and Ownership 伦理与所有权

> *Every other card in this bank teaches you how to make a machine do something. This one is about the moment after: the machine works, it is deployed, and it is now deciding who gets the loan, who is prosecuted for theft, how fast a delivery rider must ride, whose face is recognised and whose is not. The people on the receiving end did not write the code and cannot read it. They have exactly one protection, and it is not the law, which arrives years late, and not the company, whose incentives point the other way. It is the person who wrote it. This card is about being that person — in an era in which the code increasingly writes itself, which makes the person more necessary, not less.*

## Definition

### Formal

**Professional ethics** in computing is the set of obligations a person takes on by building systems other people depend on: to the public, to clients and employers, to colleagues, and to the profession itself. The obligations are written down by **professional bodies** — the **BCS** (British Computer Society, The Chartered Institute for IT), the **IEEE** (Institute of Electrical and Electronics Engineers) and the **ACM** (Association for Computing Machinery) — in **codes of conduct**, which members agree to and can be expelled for breaking.

**Ownership** is the legal side: **copyright** gives the author of a program (or an image, a text, a recording) the exclusive right to copy, distribute and adapt it, automatically and without registration, for decades. A **licence** is the permission an owner attaches to a copy — the terms under which someone else may use it. The syllabus names four families: **free software** (the Free Software Foundation's four freedoms), **open source** (the Open Source Initiative's definition), **shareware** (try, then pay) and **commercial** (pay, and never see the source).

**Artificial intelligence** enters the same section because it is where all of the above now collides: systems that learn their behaviour from data inherit the biases of that data; models trained on copyrighted work and producing new work strain the definition of ownership; and the social, economic and environmental impact of AI is the largest ethical question the profession has faced.

### Intuitive

A doctor takes an oath because a patient cannot check the diagnosis. A structural engineer signs the drawings because the people in the building cannot check the beam. A programmer is in the same position and, historically, has not been asked to sign anything — which is why the codes exist, and why the cases in this card happened. Ethics is not the part of the job where you feel good; it is the part where **you are the only check** on something that will act on people who cannot see it.

### 中文锚点

2020 年有一篇刷屏的文章，叫《外卖骑手，困在系统里》。它讲的是平台的算法把每一单的送餐时限一压再压，骑手为了赶时间只好闯红灯、逆行；出事的是人，做"决定"的却是代码。可是代码没法被追责，能负责的只有写代码的人。计算机行业讲的职业伦理，全部意思就在这里：你做的系统，会落到那些看不见它、也改不了它的人身上；法律通常要好几年才追得上来，公司的利益又常常指向另一边；所以能在伤害发生之前把它拦住的关口只有一个，就是写这个系统的人。正因为如此，专业组织才把这些责任一条条写成行为准则：先是对公众的责任，然后是对雇主、对同事、对这个行业的责任。"所有权"也是同一个思路：你写的程序，一落笔就是你的；你给它附上的许可证，就是你提前定好：别人可以拿它做什么；而使用别人的作品，就意味着尊重对方做出的这个决定。

### 术语对照 (Terms)

| English | 中文 | one-line meaning |
|---|---|---|
| professional ethics | 职业伦理 | the obligations that come with building what others depend on |
| code of conduct | 行为准则 | a professional body's written rules; members can be expelled for breaking them |
| BCS · IEEE · ACM | 英国计算机学会 · 电气电子工程师学会 · 计算机协会 | the three bodies whose codes the exam expects you to know |
| copyright | 版权 / 著作权 | the author's exclusive right to copy, distribute and adapt a work |
| intellectual property | 知识产权 | copyright, patents, trademarks — ownership of ideas and their expression |
| licence | 许可证 | the owner's permission, with conditions, to use a copy |
| free software (FSF) | 自由软件 | the four freedoms: run, study, change, share |
| open source (OSI) | 开源软件 | source available; modification and redistribution allowed by the licence |
| copyleft | 著佐权 | a licence that requires derived works to carry the same licence (GPL) |
| shareware | 共享软件 | free to try for a period or with limits, then a fee |
| commercial / proprietary | 商业软件 / 专有软件 | bought for a fee, no source, no right to alter or share |
| freeware | 免费软件 | free of charge but closed — *not* free software |
| algorithmic bias | 算法偏见 | systematic unfairness to a group, learned from data or built into rules |
| proxy variable | 代理变量 | a feature that stands in for a protected one (postcode for race) |
| accountability | 问责 | someone answerable for what the system does |

## Part I — Why a profession needs a code

Three layers of obligation sit on anyone who writes software that others use, and they are enforced by three different things.

![[ethics-three-layers.svg|1000]]

**The law** is the floor. Copyright, data-protection statutes (the EU's GDPR from 2018, China's 个人信息保护法 PIPL from 2021), product-safety and fraud law all bind a programmer whether or not they have ever thought about ethics. But the law is slow, national, and written for the last problem: no statute anticipated a hiring model, a delivery algorithm or a chatbot, and the courts arrive after the harm. "Legal" and "right" are different words, and the gap between them is where most of this card lives.

**The profession's code** is the middle layer, and the one the syllabus examines. Doctors, lawyers and engineers have had codes for a century; computing's are younger, but they do the same job: they say, in advance and in writing, what a member will and will not do, so that a person under pressure from an employer *does not have to decide alone*. That is the practical reason the exam wants for joining a professional body, and the mark schemes list it directly: written standards that clients and colleagues can rely on; recognition of competence; help, support and legal advice; training that keeps skills current; and a body that can discipline members, which is what gives the code its teeth.

**Your own judgement** is the top layer, and the only one present in the room when the decision is made. Every case in Part III below was a case in which the law existed, a code existed, and a person still had to choose.

## Part II — The codes themselves

The **BCS Code of Conduct** organises everything under four duties, and the exam's "towards colleagues" and "towards the public" questions map straight onto them:

1. **Public interest** — have regard to the health, privacy, security and wellbeing of others and the environment; respect the rights of third parties; do not discriminate on any grounds.
2. **Professional competence and integrity** — undertake only work you are competent to do; keep your skills current; do not claim competence you lack; accept and offer honest criticism; reject bribery; do not misrepresent.
3. **Duty to the relevant authority** (your employer or client) — carry out the work with due care; avoid conflicts of interest; do not misuse information; accept responsibility for your work.
4. **Duty to the profession** — uphold its reputation; support and encourage colleagues; act with integrity towards members of other professions.

The **IEEE Code of Ethics** opens with the sentence the whole subject turns on: to *hold paramount the safety, health, and welfare of the public*, and continues through honesty about data and claims, rejecting bribery, fair treatment of all persons, avoiding harm to others and their property, and *assisting colleagues and co-workers in their professional development*. The **ACM Code of Ethics** (rewritten in 2018) adds explicit principles on avoiding harm, honesty, privacy, and a duty to *design and implement systems that are robustly and usably secure*.

Read the three side by side and the same skeleton shows through: **the public before the client, the client before yourself, honesty about what you know and what your software does, and colleagues treated as people whose work you credit and whose criticism you accept.** An exam answer that names two distinct duties and says *why* each matters — "credit colleagues' contributions, so that they feel valued and the team keeps working" — is the full-marks shape.

## Part III — Acting ethically in a situation: the cases that made the rules

The syllabus asks for *the impact of acting ethically or unethically for a given situation*, and the exam's situations are small: a developer unfamiliar with the IDE, a tester who finds a bug in code already signed off, a manager and her team. The right answers are small too — say so, ask for training, report the fault — and the reason they matter is that the same choice, scaled up, produced the following.

![[ethics-horizon-comic.png|640]]

**The Post Office Horizon scandal (UK, 1999–2024).** Horizon was the accounting system installed in every British sub-post office. It contained bugs that created phantom shortfalls in branch accounts. Rather than doubt the software, the Post Office prosecuted the sub-postmasters — more than **900** of them between 1999 and 2015 — for theft and false accounting; people were bankrupted, imprisoned, and several took their own lives. Engineers at the supplier knew of the bugs; internal knowledge of remote access to branch accounts was not disclosed in court. The convictions began to be overturned in 2021 after a group of sub-postmasters won a civil case in 2019, and in 2024 Parliament passed an Act quashing them wholesale. Every layer failed: the law took two decades, the company's incentive was to defend its system, and the people who knew the software was unreliable did not say so where it counted. *Duty to the public interest; honesty about what the software does.*

**Volkswagen's defeat device (2015).** Engine-control software detected when a car was on an emissions test rig — steering wheel not moving, specific speed profile — and switched to a clean mode; on the road the cars emitted up to forty times the permitted nitrogen oxides. Eleven million vehicles. The engineer who led the software work, James Liang, pleaded guilty in 2016 and was sentenced to forty months in prison in 2017; his managers ordered it, and he wrote it. *Following an instruction is not a defence the code recognises; duty to the relevant authority sits below duty to the public.*

**Boeing 737 MAX (2018–2019).** A flight-control routine, MCAS, pushed the nose down on the reading of a single sensor, without redundancy and without being described to pilots, because describing it would have required expensive retraining. Two crashes, 346 deaths. *Honesty about what the system does; competence — a single-sensor safety-critical input is a design an engineer is obliged to refuse.*

**Therac-25 (1985–87)**, in [[Program Development Life Cycle and Testing]], belongs here too: software interlocks replaced hardware ones, a race condition delivered lethal radiation doses, and the manufacturer's first response to reports was that the machine could not have done it.

The pattern across all four is the one the small exam scenario is teaching: **a fault was known, reporting it was uncomfortable, and the discomfort won.** The November 2021 question — a developer finds an error in already-tested code and says nothing "because he is worried about the consequences" — is Horizon in miniature, and the mark scheme's answer is the BCS code's: he failed the product, the client and the profession.

## Part IV — Copyright: why the law exists, and what it actually does

A program is a *work*, like a novel or a photograph, and **copyright** arises the moment it is written: the author has the exclusive right to copy it, distribute it, adapt it and license it, for the author's life plus seventy years in most jurisdictions. No registration is needed and no © symbol is required, although stating ownership makes enforcement easier — which is the exam's *reasons to copyright your program*: it identifies you as the owner, it makes copying by others a legal wrong with consequences, and it restricts competitors from taking the work.

The examiners' report for June 2025 draws the line that students most often cross: **copyright does not *prevent* a program being copied or altered; it makes doing so *illegal***. Copyright is a right, not a lock. Locks are [[Data Security]]'s business; copyright is what you go to court with afterwards.

Why does the legislation exist at all? Because a program costs years to write and seconds to copy. Without an exclusive right, the second copy is free and the first is never paid for, so the work is not done — the same argument that justifies patents for drugs. The law's bargain is a temporary monopoly in exchange for the work existing. The bargain has edges: **ideas are not copyrightable, only their expression**, so an algorithm cannot be copyrighted (though it may be patented), and *Oracle v. Google* (2021) held that reimplementing an API's structure was fair use. [[A Rich Neighbor Named Xerox]] tells the earlier version of the same fight — the desktop metaphor Apple took from PARC and then sued Microsoft over, and the 1994 ruling that a look and feel is not a work.

## Part V — Licences: the owner's permission, and choosing one

Copyright makes every licence enforceable; the licence is the permission the owner attaches to a copy. The choices form a spectrum, and the exam's four names sit on it.

![[ethics-licence-spectrum.svg|1000]]

- **Free software (Free Software Foundation).** Richard Stallman's 1985 definition is four **freedoms**: to *run* the program for any purpose, to *study* and change it (which requires the source), to *redistribute* copies, and to *distribute modified versions*. The GPL adds **copyleft**: anyone who redistributes must pass on the same freedoms, so a GPL library cannot be absorbed into a closed product. "Free" is about liberty, not price — the FSF's own line is *free as in speech, not as in beer*.
- **Open source (Open Source Initiative).** Defined in 1998 by ten criteria — free redistribution, source available, modifications allowed, no discrimination against persons or fields of use — chosen to make the idea acceptable to business. Most open-source licences (MIT, BSD, Apache) are **permissive**: keep the copyright notice, otherwise do as you like, closed products included. The FSF and OSI lists overlap almost entirely; the difference is philosophy, and the exam treats the two as one answer.
- **Shareware.** Closed source, distributed free for a **trial** — a time limit, or missing features — after which a fee is due. The programmer's benefits (an exam question in its own right): users try before buying, so distribution is cheap and wide; the developer keeps the source and the copyright. The examiners note the standing confusion: **shareware does not mean the source is shared.**
- **Commercial software.** Developed as a business activity. Cambridge commonly contrasts a paid proprietary package with free/open-source alternatives: its licence may restrict modification, redistribution and installations, with support sold alongside it. But **commercial and proprietary are not synonyms**: free/open-source software can also be sold, while proprietary software can be supplied at no charge. [The GNU classification](https://www.gnu.org/philosophy/categories.en.html) makes this distinction explicit. Choose by the permissions and support actually offered, not the price alone.

**Freeware** — free of charge, closed source, no right to modify — is none of the four, and the examiners' reports name freeware-versus-free-software as the confusion they see most.

**Choosing for a situation** is the examined skill, and the reasoning is the same every time: *who needs to see or change the code, and who needs to be paid?* A business that will modify the program itself and pays the developer for maintenance wants an open-source or free-software licence (the November 2024 answer — source visible so the business can adapt it, developer paid for updates). A supermarket product-reader whose wrong output could send an allergic customer to hospital should *not* be open source (June 2025 — the source could be altered and the altered program could give wrong answers with serious consequences). A hobbyist who wants adoption chooses permissive; a project that wants to stay free forever chooses the GPL; a studio that needs revenue chooses commercial.

`ethics-licence-audit.py` reads the licence of every package installed on the machine it runs on: on this one, 154 packages, of which 146 permissive, 5 weak copyleft, none strong copyleft, and 3 whose licence a real audit would have to read by hand — one of them dual-licensed *AGPL or commercial*, exactly the kind of line that decides whether a product can ship.

## Part VI — Artificial intelligence: applications, impact, and the bias you cannot delete

The syllabus asks for the *applications* of AI and its *social, economic and environmental impact*. The exam's applications are concrete — a program that photographs a label, recognises the characters, translates them and reads them aloud; a chess program that stores rules and past games, looks ahead, and chooses the move most likely to succeed — and the social benefits it wants are concrete too: a visually impaired shopper can identify products; a person who does not read the language can. The costs are just as concrete, and they are the part of this section that will matter most in your working life.

### Bias: the model learns the decisions, not the truth

A model trained on historical decisions learns to reproduce them, including the unfairness in them. In 2018 Reuters reported that Amazon had abandoned a recruiting model that had taught itself to downgrade CVs containing the word "women's" — it had been trained on ten years of hiring in which men had been preferred. The usual first fix — delete the protected attribute — does not work, and `ethics-bias-demo.py` shows why on data whose ground truth is known:

![[ethics-bias-proxy.svg|900]]

Twenty thousand synthetic applicants, two groups with the *same* ability distribution, historical hiring that favoured group A, and a postcode feature correlated with group but not with ability. A logistic regression trained on the historical decisions with every column present hires 71% of group A and 8% of group B *at equal ability*. Delete the group column and the gap falls to 21 points — the model has found the postcode and reads group through it, as American lenders once read race through redlined maps. Delete the postcode too and the gap closes; keep every column but train on *fair* decisions and it closes just as well. **The bias was in the data, and only the data can remove it.** Applied to people, the same mechanism was documented in COMPAS, the risk score used in US courts, which ProPublica showed in 2016 flagged Black defendants who did not reoffend at nearly twice the rate of white defendants.

![[ethics-manim.mp4]]

The professional obligations follow directly: know how the data was collected; audit outcomes by group, not just overall accuracy; be able to explain a decision (**transparency**) and name who answers for it (**accountability**). The GDPR gives a person the right not to be subject to a decision made solely by automated processing; PIPL Article 24 forbids using automated decisions to set unreasonably different prices for different people — the practice Chinese users call 大数据杀熟 — and requires an explanation and an opt-out on demand.

### Economic and environmental impact

- **Economic.** AI automates cognitive work the way machinery automated manual work. Goldman Sachs estimated in 2023 that around 300 million full-time jobs worldwide are exposed to automation by generative AI; the same report expected productivity gains. Which jobs, who captures the gain, and who retrains whom are questions the profession's codes place under *public interest*. The delivery-platform algorithm is the local case: a system that shortens the allowed delivery time because riders keep meeting it, until the only way to meet it is to break traffic law — reported in 人物 in 2020, and answered by regulation in 2021 requiring platforms to relax the algorithms. The engineers who tuned the timer were optimising a metric; the riders were the externality.
- **Environmental.** Training GPT-3 was estimated at about 1,287 MWh of electricity and 552 tonnes of CO₂-equivalent (Patterson et al., 2021); data centres used roughly 460 TWh in 2022, close to 2% of global electricity, and the IEA expects that to double by 2026 with AI the fastest-growing share. Water for cooling and rare-earth mining for hardware are the other two lines. The BCS code's *wellbeing of others and the environment* is not decoration.

### Ownership in the age of models

Two questions the law has not settled. **Training data:** models are trained on text and images under copyright, and whether that is fair use is being litigated (*The New York Times v. OpenAI*, filed 2023; the Getty and author suits alongside). **Outputs:** the US Copyright Office has held that work generated by AI without human authorship cannot be copyrighted (the *Zarya of the Dawn* decision, 2023, and *Thaler v. Perlmutter*), so a program or image produced by prompting alone may belong to no one. For a student: the code a model wrote for you is not yours in the sense that the code you wrote is, and a licence attached to the training data may travel with it.

### The student's own case

You will use these tools for your work; the question is how. [[Learning as Verification]] makes the argument in full: when a machine produces the answer, the skill you keep is *checking* it, and a student who submits generated work unchecked has surrendered the one skill the era still needs. The professional version is identical. A developer who ships model-generated code they cannot verify has broken the competence duty exactly as if they had copied it from a stranger, and the Horizon engineers' failure — trusting the system's output over the person in front of them — is the failure mode.

## Worked examples — the real Paper 1 shapes

### Example 1 — the professional body and the unreported bug (Cambridge 9618, November 2021 Paper 11, Q4)

> Francis starts his first job as a software developer. (a) Describe the benefits to Francis of joining a professional ethical body [3]. (b)(i) He is unfamiliar with the IDE he must use; describe the ways he can act ethically [2]. (c) He finds an error in code already tested and decides not to tell anyone because he is worried about the consequences; explain why he acted unethically [2].

*Tool: the codes, quoted as duties. Trigger: every part names a person and a situation — the answer is always which duty, and what follows from it.* **(a)** He has written guidelines to follow, so he does not have to decide alone and clients know the standards applied; membership signals competence to clients and colleagues; the body provides support, including legal advice; and it runs training that keeps his skills current. Any three. **(b)(i)** Tell the manager he has not used it and how he will get up to speed; ask for training or a mentor; research and practise it himself — the competence duty is *do not claim what you cannot do*, and the ethical act is the honest sentence. **(c)** He did not act in the best interest of the product, which may fail; nor of the client, who is let down when it does; nor of the profession, whose reputation he has risked. The examiners' report notes that answers saying only what he *should* have done scored nothing: the question asks why what he did was wrong.

### Example 2 — colleagues, the public, a licence and a copyright (Cambridge 9618, November 2024 Paper 12, Q5)

> (a) Explain why a programmer needs to act ethically towards colleagues and the public [4]. (b) A business will modify the program's source code itself and pays the programmer for maintenance and security updates. (i) Identify a suitable licence and give reasons [3]. (ii) Explain why the programmer should copyright the program [2].

**(a)** Two for colleagues — treat them fairly without discrimination; credit their contributions so they feel valued; accept and offer critique so the work improves — and two for the public — maintain their health, safety and welfare; be honest in claims about the software so trust is kept; keep their data secure. **(b)(i)** Open source (or free software): the source is visible, so the business can adapt the program to its needs, and the programmer is still paid for the updates and maintenance — the licence does not forbid charging for service. **(b)(ii)** To be formally recognised as the owner, and to have legal consequences available if anyone copies or steals it.

### Example 3 — commercial, and why not open source (Cambridge 9618, June 2025 Paper 12, Q3(c))

> A program photographs a product label, recognises the words, translates them and reads them aloud; it is released under a commercial licence. (i) Describe the features of a commercial software licence [3]. (ii) Explain why an open-source licence might not be appropriate for this program [3].

**(i)** Sold for a fee; no access to the source code; users cannot legally alter or share it; limits on installations or users; support and updates provided; the developer's intellectual property protected. **(ii)** Open source would expose the code, so it could be changed; a changed program could output an incorrect translation; a shopper could then buy the wrong item — with serious consequences for someone with an allergy. The examiners' report: listing open source's *features* is not an answer; each feature must be tied to *why it is unsuitable here*.

### Example 4 — name the licence from its description (Cambridge 9618, June 2026 Paper 11, Q(d))

> Released on a trial period, after which a fee may be required → **shareware**. Purchased for a fee, no access to the source → **commercial** (proprietary). Released with the source; may be changed and distributed under the same licence restrictions → **open source** (the scheme also accepts free software; it explicitly rejects *freeware*).

## Where this is the working tool

- **Every software release goes through a licence audit** — the script above, industrialised: companies scan dependencies for copyleft obligations before shipping, because one GPL library in a closed product is a lawsuit.
- **Model cards and fairness audits** are now standard deliverables for deployed machine-learning systems: documented training data, measured performance by subgroup, known failure modes. The bias demo is the smallest possible one.
- **Data-protection impact assessments** are legally required under the GDPR before high-risk processing — a written answer to "what could this do to the people in the data?"
- **Responsible-disclosure and whistleblowing channels** exist because the November 2021 scenario is real: the developer who finds the fault needs somewhere to report it that does not end their career.

## Hands-on

- **`ethics-bias-demo.py`** — the synthetic hiring world with the bias built in on purpose; a logistic regression from scratch; the four audits. Change the correlation between postcode and group and watch how much of the bias survives deletion.
- **`ethics-licence-audit.py`** — every installed package's licence, classified and tallied, with the obligation each class carries. Run it on the school machines.
- **`ethics-manim.py`** — the two scenes: the proxy bias as moving bars, and copyleft as a flow that runs back upstream.
- **Read one code.** The BCS Code of Conduct is two pages. Read it, then re-read the four cases in Part III and mark which clause each broke.

## Common Misconceptions (Teaching Notes)

### 1. "Copyright stops people copying my program"
It makes copying unlawful; it stops nothing. The June 2025 examiners' report says exactly this. Prevention is encryption, licensing servers and obfuscation; copyright is the remedy afterwards.

### 2. "Freeware is free software" and "shareware shares the source"
Freeware is free of charge and closed. Free software is about the four freedoms and may be sold. Shareware is closed source with a trial; nothing is shared but the trial copy. Three sittings' reports name these confusions.

### 3. "It was legal, so it was fine" — and "I was told to"
The law is the floor and arrives late; the codes exist for what the law has not yet reached. Volkswagen's engineer was told to; he went to prison. Duty to the employer sits below duty to the public in every code.

### 4. "Delete the sensitive column and the model is fair"
The demo is the refutation: a correlated proxy carries the bias through. Fairness is a property of outcomes, audited by group, not of the input list.

### 5. "The computer is never wrong" — the Horizon fallacy
Software output was treated as evidence stronger than the sworn word of hundreds of people. A system's output is a claim, and claims are checked. This is [[Learning as Verification]]'s thesis applied to a courtroom.

### 6. "Ethics questions are opinion questions"
They are answered from the codes. "Explain why he acted unethically" wants *which duty* was breached and *what the consequence* was, not a feeling.

## Exam Notes

### Cambridge 9618 (§7.1 Ethics and Ownership — Paper 1)

- **Five learning outcomes:** the need for and purpose of ethics as a computing professional, *including the importance of joining a professional ethical body — BCS and IEEE are named*; the need to act ethically and the impact of acting ethically or unethically *in a given situation*; the need for copyright legislation; the types of software licence — *Free Software Foundation, Open Source Initiative, shareware, commercial* — and justifying one for a situation; and AI — its social, economic and environmental impact, and its applications.
- **The recurring questions, with their schemes' shapes:** *benefits of joining a professional body* (written guidelines to follow, so standards are known and you need not decide alone; recognition of competence to clients; help and legal support; training to keep skills current — November 2021, November 2023, June 2025); *why act ethically towards colleagues / the public* (colleagues: fairness, credit, accept and offer critique, help and train; public: health, safety and welfare, honest claims about the software, security of their data — June 2021, November 2024); *why did X act unethically* (name the duty breached: product, client, profession — November 2021); *identify and justify a licence for a scenario* (November 2024's modifiable, paid-maintenance program → open source; June 2025's safety-critical reader → commercial, and *why open source would be unsuitable*, with the consequence spelled out); *complete the licence table* (June 2026: shareware, commercial, open source from one-line descriptions); *reasons to copyright* (ownership recognised, legal consequences for copying, competition restricted); *how AI is used* and *social benefits* in a described program (June 2025).
- **Examiners' recurring notes:** freeware confused with free software (2022, 2023); shareware taken to mean shared source (2023); copyright described as "using without permission" (2021) or as preventing copying (2025); benefits of a licence given when its *features* were asked (2025); professional bodies confused with employers (2021); two answers that are the same point reworded (2021); "not in a professional body therefore malicious code" (2025).
- The AI *application* and *impact* outcomes are new to the 2027–29 syllabus as §7.1 content; the graph-search and machine-learning mechanics of AI are §18.1, in [[Graphs]] and [[Artificial Intelligence]].

### AP Computer Science A (Units 3.2 and 4.1)

- **3.2 Impact of Program Design** — system reliability; programs' beneficial and harmful impacts on society, economy and culture; legal and intellectual-property issues when reusing others' code (attribution, licences). **4.1 Ethical and Social Issues Around Data Collection** — privacy risks of collecting and storing personal data; **algorithmic bias** as *systemic and repeated errors that create unfair outcomes for a specific group*; awareness of how a data set was collected and its potential for bias; incomplete or inaccurate data. Both are examined through the Free Response questions' context and the multiple choice, not as essays.

### IB Computer Science

- **A4.4 Ethical considerations** sits inside the machine-learning topic: bias, transparency, accountability and data provenance in trained systems — Part VI here; the ML mechanics themselves await [[Artificial Intelligence]].

### Where it is *not* examined

**Cambridge 0478** has no ethics, copyright or licensing content; its security material is §5, in [[Data Security]]. **9618 Papers 2, 3 and 4** never examine §7 — it is Paper 1 only. AP Computer Science *Principles* has a large "impact of computing" unit, but that course is not tracked here.

## Connections

- **Built on:** [[Data Security]] — the technical half of privacy, and the difference between preventing copying and forbidding it; [[Program Development Life Cycle and Testing]] — Therac-25, Ariane and CrowdStrike as what skipping a stage costs, and the testing that the Horizon engineers' duty required; [[Learning as Verification]] — the machine's output as a claim to be checked, the proof-kernel argument applied to people; [[Stats Lies Hall of Fame]] — Simpson's paradox and the missing data are the same audit this card runs on a model.
- **Same idea elsewhere:** [[Credit Is the Currency]] — a profession's code as a standing promise that makes its members trustworthy; [[Courage]] — the company that tells the truth about breakage; [[Compression]] — lossy is a licensing question too (patents on codecs).
- **Extends into:** [[Data Protection and Privacy]] — GDPR and PIPL in full; [[Artificial Intelligence]] — the mechanics of the systems whose ethics this card audits; [[A Rich Neighbor Named Xerox]] — ownership of an idea versus its expression, litigated.
- **Builds on:** [[Automated Systems and Robotics]] — the jobs, deskilling and accountability questions arrive with the machines that sense, decide and act without a person in the ring.

## Beyond Syllabus

### Whistleblowing, and what the codes say about it
The ACM code's principle 1.2 (*avoid harm*) says that when harm is caused by a system, those responsible are obliged to report it, and that reporting may require going outside the organisation. UK law (the Public Interest Disclosure Act 1998) protects an employee who does. The Horizon inquiry's central finding is that the people who knew did not have, or did not use, such a channel.

### The four freedoms, numbered from zero
Stallman numbered the freedoms 0 to 3 — freedom 0 is to run the program — because freedom 0 was added after the other three were written, and he would not renumber. It is the most on-brand fact in the history of licensing.

### Patents versus copyright, for software
Copyright protects expression; a patent protects an invention, for twenty years, after examination. Whether algorithms are patentable differs by country: the US allows software patents broadly, Europe only where there is a "technical effect". The RSA algorithm was patented in 1983 and the patent's expiry in 2000 is part of why [[Encryption]] is free to use today.

### Alignment, and the ethics of systems that set their own goals
A classifier that learns a proxy is the smallest instance of a general problem: an optimiser pursues the objective it was given, not the one you meant. The delivery timer, the recruiting model and the emissions controller are all cases of a system doing exactly what it was told. The research field that studies this for powerful models is called *alignment*, and its founding observation is this card's Part VI at scale.

## Sources

- Cambridge International AS & A Level Computer Science 9618, syllabus for 2027–2029, §7.1 (p. 24); 9618 Paper 1 questions and mark schemes: June 2021/12 Q2, November 2021/11 Q4, November 2023/13 Q6, November 2024/12 Q5, June 2025/12 Q3, June 2026/11; examiners' reports 2021–2025.
- BCS Code of Conduct (2022 revision); IEEE Code of Ethics (2020); ACM Code of Ethics and Professional Conduct (2018); Free Software Foundation, *What is Free Software?*; Open Source Initiative, *The Open Source Definition*.
- Post Office Horizon IT Inquiry (2021–); *Bates v Post Office Ltd* [2019] EWHC 3408; Post Office (Horizon System) Offences Act 2024. US Department of Justice, *United States v. James Liang* (2017). US House Committee on Transportation, *Final Report on the Boeing 737 MAX* (2020).
- J. Dastin, "Amazon scraps secret AI recruiting tool that showed bias against women", Reuters (2018); J. Angwin et al., "Machine Bias", ProPublica (2016). 人物, 《外卖骑手，困在系统里》(2020). 中华人民共和国个人信息保护法 (2021), 第二十四条.
- D. Patterson et al., "Carbon emissions and large neural network training" (2021); IEA, *Electricity 2024*. Goldman Sachs, *The Potentially Large Effects of Artificial Intelligence on Economic Growth* (2023).
- *Google LLC v. Oracle America, Inc.*, 593 U.S. (2021); US Copyright Office, *Zarya of the Dawn* letter (2023); *Thaler v. Perlmutter* (D.D.C. 2023).
- The scripts beside this card: `ethics-bias-demo.py`, `ethics-licence-audit.py`, `ethics-manim.py`.
