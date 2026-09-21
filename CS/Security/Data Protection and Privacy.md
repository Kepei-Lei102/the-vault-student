---
chinese: 数据保护与隐私 (shùjù bǎohù yǔ yǐnsī)
prerequisites:
  - "[[Data Security]]"
  - "[[Ethics and Ownership]]"
  - "[[Relational Databases]]"
  - "[[Encryption]]"
  - "[[Artificial Intelligence]]"
  - "[[Digital Currency and Blockchain]]"
  - "[[Probability Basics]]"
leads_to:
  - "[[Privacy-Preserving Computation]]"
  - "[[Affective Computing]]"
tags:
  - subject/computer-science
  - domain/security
  - domain/privacy
  - level/IGCSE
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-9618
  - curriculum/Cambridge-0478
  - curriculum/IB-CS
  - curriculum/AP-CSA
  - syllabus/9618-6-1
  - syllabus/0478-5-3
  - syllabus/IB-CS-A4-4
  - type/deep
  - misconception/no-names-means-anonymous
  - misconception/hashing-is-anonymising
  - misconception/privacy-equals-secrecy
  - misconception/consent-fixes-everything
---

# Data Protection and Privacy 数据保护与隐私

> *In 1997 the state of Massachusetts released the hospital records of its employees to researchers, with every name, address and identity number removed. The governor, William Weld, assured the public that privacy was protected. A graduate student named Latanya Sweeney paid twenty dollars for the voter roll of Cambridge, the city where Weld lived, which listed every voter's name, postcode, date of birth and sex. Six people in Cambridge shared the governor's birth date. Three were men. One lived in his postcode. She posted his medical file to his office. Nothing had been hacked, no password guessed, no rule broken. Everything that follows, the law and the mathematics alike, is an answer to what she showed that day: personal data is not protected by deleting the column labelled "name".*

## Definition

### Formal

**Privacy of data** is ensuring that data about a person is accessed by, and disclosed to, only those authorised to see it, and used only for the purpose it was given for. **Personal data** is any information relating to an identified **or identifiable** living person: a name, but equally a phone number, a location trail, a face, or a combination of fields that singles one person out. **Data protection** is the body of law and engineering practice that binds whoever holds personal data. Its two largest statutes are the European Union's **General Data Protection Regulation** (GDPR, in force 25 May 2018) and China's **Personal Information Protection Law** (个人信息保护法, PIPL, in force 1 November 2021). Both rest on the same skeleton: a **lawful basis** for every act of processing; **principles** that limit what may be collected, for what, and for how long; **rights** held by the person the data is about; **duties** on the organisation that decides the purpose; and **penalties** scaled to turnover.

### Intuitive

Security asks *can an outsider get in?* Privacy asks a harder question: *of the people who can get in, who should see this, and what may they do with it?* A hospital with perfect firewalls can still breach your privacy if a clerk browses your file out of curiosity, or if the hospital sells "anonymised" records that are nothing of the kind. So privacy cannot be delivered by a lock alone. It needs a rule about **purpose**: data you hand over to get a parcel delivered is for delivering the parcel, and every later use has to be justified against that.

Two surprises give the subject its depth. The first is Sweeney's: **identity lives in combinations.** No single field in the released hospital file named anyone, and three harmless fields together named almost everyone. The second is its mirror image: **privacy can be measured and dialled.** A database can answer questions about five thousand salaries to within a tenth of a percent while mathematically refusing to reveal any one of them.

### 中文锚点

刚交了新房的首付，装修公司的电话就一个接一个打进来，开口就能叫出你的姓、说出你的楼盘和户型。你并没有把号码给过他们。你给的是售楼处，目的只有一个：办买房手续。号码本身算不上秘密，快递员、同事、外卖小哥都知道；让人不舒服的，是它**离开了当初交出去时的那个目的**，被带到了你从没答应过的地方。数据保护的核心就是这一条：**个人信息是为了某个说清楚的目的交出去的，拿到它的人只能为这个目的用它、只拿够干这件事的那么多、用完就删**；想挪作他用，得重新问你。这不是因为信息"见不得人"，而是因为一条条看似无害的信息——姓氏、楼盘、手机号——拼在一起，就足以在人群里把你单独指出来，而被指出来之后会发生什么，你已经控制不了了。

---

## Part I — What counts as personal data

The legal definition turns on one word, *identifiable*, and the code beside this note measures what it means. In a synthetic city of 200 000 people, no one is unique by sex, by district, by year of birth, or by any two of those. Give an attacker district, **date** of birth and sex, and **90 %** of the city is the only person with their combination.

![[data-protection-uniqueness.svg|820]]

The figure can be checked by counting. There are $40 \times 32\,850 \times 2 \approx 2.6$ million possible combinations of district, birth date and sex, and 200 000 people to scatter among them. The chance that nobody else lands in your cell is about $e^{-N/\text{cells}} = e^{-0.076} = 93\,\%$ if the districts were equal; unequal districts pull it down to the simulated 90 %. Sweeney's measured figure for the real United States, using postcode, birth date and sex, was 87 %.

Fields like these are **quasi-identifiers**: not names, but name-equivalents once combined. The consequences:

- **The linkage attack.** Release the hospital's 20 000 records with names removed but district, birth date and sex left in. Take any public list that carries those three fields *with* names: a marathon's results, a club roster. Of 527 patients who appear on a 5 000-name list, the join re-identifies **519**, with their diagnosis. It also confidently pins 42 strangers' records on people who were never in hospital, which is its own kind of harm.
- **"We hashed the phone numbers."** A hash is deterministic and the space of phone numbers is small. SHA-256 of an eleven-digit mobile number, with the carrier prefix and city block known, falls in **2.8 milliseconds**; the whole national number space takes a laptop a few hours and a graphics card a few minutes. Replacing an identifier with a token that the holder of a key can reverse is **pseudonymisation**, and the law still treats the result as personal data. Only when re-identification is not reasonably possible for anyone is data **anonymous** and outside the law.
- **Sensitive data.** Both statutes fence off categories where exposure does disproportionate harm: health, biometrics, religion, precise location, financial accounts, and under PIPL anything about a child under fourteen. These need a stronger justification and, in China, **separate consent** asked on its own, not buried in a general agreement.

## Part II — The rules: one life of one piece of data

The law is easiest to hold as the life story of a single piece of personal data, because each principle bites at one stage of it.

![[data-protection-lifecycle.svg|900]]

**Collect: a lawful basis, and no more than needed.** Processing personal data is unlawful unless one of a short list of bases applies.

| Lawful basis | GDPR (Art. 6) | PIPL (Art. 13) | Example |
|---|---|---|---|
| The person's **consent** | yes: freely given, specific, informed, withdrawable | yes: same; *separate* consent for sensitive data, sharing, going abroad | a newsletter sign-up |
| Needed for a **contract** with them | yes | yes, and for human-resources management | an address, to deliver what you bought |
| A **legal duty** | yes | yes | tax records an employer must keep |
| To protect **life** | yes ("vital interests") | yes (emergencies, public health) | an unconscious patient's blood type |
| A **public task** | yes | partly (news reporting in the public interest) | a census |
| The holder's **legitimate interests**, balanced against the person's | yes | **no such basis** | fraud detection on your own customers |
| Information **already lawfully public** | no separate basis | yes, within a reasonable scope | a published court judgment |

The last two rows are the sharpest difference between the systems: European companies lean heavily on "legitimate interests", and PIPL does not offer it, which is why consent screens are so much more frequent in Chinese apps. Whatever the basis, **data minimisation** applies: a torch app has no purpose that needs your contacts.

**Store: accurate and secure.** The holder must keep the data correct and protect its confidentiality and integrity, which is where every defence in [[Data Security]] and [[Encryption]] becomes a legal duty instead of good practice. When a breach happens anyway, GDPR gives the controller **72 hours** to tell the regulator.

**Use: purpose limitation.** Data collected for one stated purpose may not be quietly reused for an incompatible one. This is the principle the anchor's phone number broke.

**Share: controller and processor.** The law names the parties so that responsibility cannot leak.

![[data-protection-roles.svg|900]]

The **controller** (PIPL: 个人信息处理者, the *handler*) decides why and how data is processed. A **processor** (受托人, the *entrusted party*) acts only on the controller's written instructions. A school that puts its registers on a cloud platform is still the controller; the platform is its processor; and if the platform leaks, the parents' claim is against the school.

**Send abroad: protection must travel with the data.** GDPR allows transfers to countries the Commission has found *adequate*, or under standard contractual clauses. PIPL gives three routes, scaled by volume: a government **security assessment** for the largest exporters, **standard contracts** for the middle, and since 1 January 2026 a third-party **certification** route. The record GDPR fine, €1.2 billion against Meta in May 2023, was for sending Europeans' data to the United States without valid protection; TikTok's €530 million in May 2025 was for transfers to China.

**Delete: storage limitation and the right to erasure.** Keep data no longer than its purpose needs, and delete it when the person validly asks.

**The person's rights** run through every stage: to be **informed**; to **access** a copy; to **rectify** errors; to **erase**; to **restrict** or **object** to processing; to **portability** (take the data to a competitor in a usable format); and **not to be subject to a purely automated decision** with serious effects, such as a loan refusal, without a human to appeal to. PIPL adds a pointed one: automated decisions may not apply **unreasonable differential treatment in price**, the practice of charging loyal customers more that Chinese users call 大数据杀熟.

**Accountability and penalties.** The holder must be able to *demonstrate* compliance: records of processing, impact assessments before risky projects, a named responsible officer. Fines reach **€20 million or 4 % of worldwide annual turnover** under GDPR and **¥50 million or 5 % of the previous year's turnover** under PIPL, whichever is higher. Both reach beyond their borders: a company anywhere in the world that offers services to people in the EU, or in China, is bound.

## Part III — Engineering privacy: three tools, each measured

Law states the duty; these are the ways code discharges it. Every number below is printed by `data-protection-privacy-lab.py`.

**1. Generalise until everyone hides in a crowd: k-anonymity.** A table is *k-anonymous* if every combination of quasi-identifiers is shared by at least $k$ people. You reach it by blurring: exact birth date becomes year, then decade; district becomes region. In the synthetic city, exact date and district gives $k = 1$ (everyone exposed); birth year and district still leaves someone alone; birth year and region reaches $k = 75$; birth decade and region, $k = 984$. Each step protects more and says less. And $k$-anonymity has a known hole: if all 75 people in your group have the same diagnosis, hiding among them reveals it anyway (the *homogeneity attack*).

**2. Tokenise with a key, not a hash.** The repair for the phone-number failure is an **HMAC**: a hash that takes a secret key as well as the input.

```python
import hmac, hashlib, secrets
key = secrets.token_bytes(32)                      # held by the controller, never released
token = hmac.new(key, b"13881234567", hashlib.sha256).hexdigest()[:16]
```

The same number still gives the same token, so records link for analysis; an attacker without the key cannot test guesses at all; and destroying the key orphans every token at once. It remains pseudonymisation, because the key-holder can reverse it, but it moves the risk from "anyone with a laptop" to "whoever guards the key".

**3. Answer questions with calibrated noise: differential privacy.** A query interface that returns only totals looks safe and is not. Ask for the total payroll, then for the total excluding employee #7, and subtract: **3 500**, her salary exactly, and no individual record was ever opened. This *differencing attack* defeats any system that answers exactly.

The defence is to add random noise to every answer, drawn from a Laplace distribution whose width is the most one person could change the answer (the **sensitivity**, here the salary cap of 60 000) divided by a chosen **privacy budget** $\varepsilon$.

![[data-protection-dp.svg|720]]

At $\varepsilon = 1$ the attacker's estimate of the salary is off by about ±90 000, twenty-five times the salary itself, while the honest analyst's total for 5 000 staff is off by **0.11 %**. The noise that blinds the question about one person barely touches the question about everyone: that asymmetry is the whole idea, and it is why privacy here is a dial and not a switch. Formally, a mechanism is $\varepsilon$-differentially private if adding or removing any one person changes the probability of any output by a factor of at most $e^{\varepsilon}$; the guarantee holds whatever else the attacker knows, which is exactly what defeated name-removal.

![[data-protection-privacy-manim.mp4]]

*Two films. A hospital release with no names meets a public list with names, and rows join on three ordinary columns. Then two harmless payroll totals whose difference is one person's salary, asked again of a database that adds calibrated noise.*

**Privacy by design** is the habit these tools serve, and GDPR Article 25 makes it a duty: decide at the schema stage which fields you need, who may read each (the `GRANT` of [[SQL]]), how long each lives, and which can be stored as tokens, because retrofitting privacy into a system that already hoards everything is the expensive direction.

## Where it is the working tool

- **The 2020 United States census** published every table through a differential-privacy mechanism, after the Census Bureau's own test reconstructed and re-identified tens of millions of records from the 2010 tables, which had used only swapping and rounding. The privacy budget was debated in public like a tax rate.
- **Your phone's keyboard.** Apple (since 2016) and Google learn which new words and emoji are popular by having each phone add noise to its report *before* sending it, so the company sees the trend and never your typing. This is *local* differential privacy: the noise is added on your side of the wire.
- **The parcel label.** China's couriers moved to privacy waybills (隐私面单) that mask the middle digits of the phone number and most of the name; the full details live in the courier's handheld, fetched per delivery. It is data minimisation applied to a sticker: the bin no longer needs to know who you are.
- **The cookie banner**, for honesty's sake. It exists because European law requires consent before non-essential tracking, and it is also the law's most visible failure: a consent nobody reads is not informed, and regulators now fine designs that make "reject" harder to find than "accept".
- **When it fails.** In July 2022 China's regulator fined the ride-hailing firm Didi **¥8.026 billion** for sixteen categories of violation, including collecting nearly twelve million screenshots from users' photo albums and over a hundred million facial-recognition records without a valid basis. In 2006 AOL published twenty million "anonymised" search queries for research; reporters identified user 4417749 as a 62-year-old widow in Georgia from her searches within days. Netflix's anonymised prize dataset was re-identified in 2008 by linking its ratings to public IMDb reviews.

## Hands-on

Run `data-protection-privacy-lab.py` (numpy only, about two seconds). It builds the synthetic city and prints all five experiments: uniqueness by field combination, the linkage attack, k-anonymity by generalisation, the hashed phone number and its keyed repair, and the differencing attack against exact and noisy answers. Then break it on purpose. Shrink the city to 20 000 and watch uniqueness rise; give the attacker only *year* of birth and watch the join collapse; set $\varepsilon$ to 50 and watch Alice's salary reappear. Finally do an audit you can finish in ten minutes: open your phone's permission settings and, for each app with access to location, contacts or photos, write down the purpose that would justify it. The ones where you cannot are the data-minimisation principle, failed.

## Worked examples — every tool named

### Example 1 — security against privacy, in one mark (Cambridge 9618, June 2022 Paper 11, Q3(a))

*A teacher writes examination papers on a laptop connected to the internet and is concerned about their security and privacy. State the difference between the security of data and the privacy of data.* [1]

*Tool: the two questions.* **Security** protects data against loss, damage or theft: keeping it safe. **Privacy** prevents unauthorised access or disclosure: keeping it to those who should see it. The scheme's wording is "security prevents against loss while privacy prevents unauthorised access". The mark needs both halves and a contrast; defining one term scores nothing.

### Example 2 — privacy and integrity, defined (Cambridge 9618, November 2023 Paper 12, Q5(a),(b))

*(a) State the meaning of privacy of data. (b) State the meaning of integrity of data.* [1 + 1]

*Tool: each property answers a different question about the same data.* **(a)** Ensuring data can be accessed by, or disclosed to, only authorised persons. **(b)** Ensuring the data is accurate, consistent and up to date. *Trigger for keeping them apart:* a nurse reading a neighbour's file breaches privacy and leaves integrity untouched; a mistyped dosage breaches integrity though every reader was authorised.

### Example 3 — privacy as a social impact (Cambridge 9618, November 2022 Paper 12, Q9)

*One use of AI is facial recognition software. Describe the social impact of using facial recognition software to identify individuals in an airport.* [2]

*Trigger: "social impact" wants consequences for people, in both directions.* People may feel safer, and crime may fall or criminals be caught (1); boarding is faster (1); incorrect recognition leads to mistakes such as wrongly denied access (1); **privacy issues: people do not like their data being stored** (1). Any two. *Tool: Part II's categories sharpen the privacy point.* A face is biometric data, a sensitive category; an airport-wide system collects it from everyone, including the overwhelming majority who are not suspects, which is a data-minimisation question; and under PIPL Article 26 image collection in public places must be for public security, with prominent signs.

### Example 4 — privacy is not intellectual property (AP Computer Science A, Course and Exam Description sample question 10)

*A programmer wants other programmers to use a method in their own programs without raising intellectual-property concerns. Which action best supports this? (A) designate it public (B) designate it static (C) publish the code as open source (D) remove all personal information from the data used by the method.*

*Tool: sort the concern before choosing the fix.* **C.** (A) and (B) are language features with no legal meaning. (D) is a real and good practice, and it answers a *different* concern: personal information in the data is a **privacy** risk to the people described (learning objective 4.1.A), while reuse of the code is a question of **ownership and licence**, which is [[Ethics and Ownership]]. The distractor works on students who file both under "legal stuff".

### Example 5 — a design review (constructed, not from a paper)

*A school wants an attendance app. Students tap a card; the app, hosted by a cloud company, records name, class, time, and the phone's GPS position, keeps records indefinitely, and sends parents a weekly summary.*

*Tool: walk the life cycle.* **Roles:** the school decides the purpose, so it is the controller; the cloud company is its processor and needs a written contract. **Basis:** a legal or public duty to record attendance, not consent (a student cannot freely refuse). **Minimisation:** the card tap already proves presence; GPS position serves no attendance purpose and, as location data about minors, is sensitive twice over. Remove it. **Storage limitation:** "indefinitely" has no purpose; keep records for the period the law requires, then delete. **Security:** access levels so a teacher sees their own classes only. **Rights:** a parent's request for a copy must be answerable, which means knowing where every copy lives. Four of the six stages needed a change, and none of the changes was a firewall.

### Example 6 — how unique are you? (the estimate behind Part I)

*A city of $N = 200\,000$; an attacker knows district (40), date of birth (about 32 850 days in 90 years) and sex (2). Estimate the fraction of people who are unique.*

*Tool: count the cells; then the Poisson approximation from [[Probability Basics]].* Cells $= 40 \times 32\,850 \times 2 = 2\,628\,000$. With people scattered roughly evenly, the number of *other* people in your cell is approximately Poisson with mean $\lambda = N/\text{cells} = 0.076$, so $P(\text{nobody else}) = e^{-\lambda} = e^{-0.076} \approx 0.93$. The simulation's 90 % is lower because real districts are unequal and the crowded ones have more collisions. *The trigger worth carrying away:* whenever cells greatly outnumber people, nearly everyone is alone in theirs, and it takes remarkably few fields to get there.

## Common Misconceptions (Teaching Notes)

### 1. "We removed the names, so it's anonymous"

**Fix:** run the linkage experiment, then ask what *other* list carries the same fields with names attached. The test for anonymity is not "is there a name column?" but "could anyone, with any other data, single a person out?"

### 2. "Hashing anonymises"

**Fix:** have the student time the brute-force loop. A hash hides inputs only when the input space is too large to enumerate; phone numbers, identity numbers, birth dates and postcodes never are. Keyed tokens, or random identifiers with the lookup table held elsewhere, are the honest alternatives, and both are still pseudonymous.

### 3. "Privacy means secrecy, and I have nothing to hide"

**Fix:** the anchor. The phone number was never secret. Privacy is control over where information flows, relative to the purpose it was shared for; people who "have nothing to hide" still close the bathroom door and still mind when their salary is read out.

### 4. "They got consent, so it's fine"

**Fix:** consent is one basis of six, and the weakest when the person cannot realistically refuse (an employee, a student, the only hospital in town). Even valid consent does not switch off minimisation, purpose limitation, security or deletion.

### 5. "Security and privacy are the same thing"

**Fix:** Example 1. A system can be perfectly secure and violate privacy (the curious clerk, the sold dataset); privacy *needs* security and is not delivered by it.

### 6. "Aggregate statistics can't leak individuals"

**Fix:** the differencing attack, on the board, with two subtraction lines. Then the census.

## Exam Notes

### Cambridge 9618 (A Level) — §6.1 Data Security, §7.1 Ethics and Ownership (Paper 1)

§6.1 requires the difference between the **security, privacy and integrity** of data; the one- and two-mark definitions of Examples 1 and 2 recur (June 2022 Paper 11 Q3, November 2023 Paper 12 Q5), usually opening a longer security question whose body is [[Data Security]]. §7.1's AI outcome ("the impact of AI including social, economic and environmental issues") draws privacy as a creditworthy social impact (Example 3). Questions that open "a company stores personal data…" go on to ask about threats, encryption, validation or database design, not about law.

### Cambridge 0478 (IGCSE) — §5.3 Cyber security (Paper 1)

**Privacy settings** are one of the listed solutions to keep data safe: restricting who can see a profile or personal information. The depth is a sentence; [[Data Security]] carries it with the other solutions.

### IB Computer Science (first assessment 2027) — A4.4 Ethical considerations

A4.4.1 asks students to *discuss* the ethical implications of machine learning, naming **consent, privacy, security, transparency, accountability** and, for online communication, **anonymity**; A4.4.2 extends to "individual rights, privacy and equity" as technology spreads. Parts I and III supply what a discussion needs to be more than opinion: why training data is personal data, why "anonymised" training sets are not, and what differential privacy offers.

### AP Computer Science A — Topic 4.1 Ethical and Social Issues Around Data Collection

Learning objective 4.1.A: *explain the risks to privacy from collecting and storing personal data on computer systems*; the essential knowledge is that programmers should attempt to safeguard the personal privacy of the user. Assessed by multiple choice (Example 4 shows the style and the usual distractor).

### Where it is *not* examined

- **No board served here examines a named statute.** The 9618, 0478, IB 2027 and AP CSA documents were each searched: none contains "GDPR", "Data Protection Act" or PIPL. The principles, rights and roles of Part II are professional knowledge, not examinable recall, on these boards.
- **9618 Papers 2–4 and 0478 Paper 2** (programming and problem-solving) carry no privacy content.
- **k-anonymity and differential privacy** are beyond every school syllabus.

---

## Connections

- **Builds on:** [[Data Security]] — the security/privacy/integrity split, access levels and privacy settings, which are the technical floor the law stands on; [[Ethics and Ownership]] — law as the lowest of three layers of obligation, and the automated-decision and impact-assessment duties seen from the professional's side; [[Encryption]] — hashing and keys, the machinery behind pseudonymisation; [[Relational Databases]] and [[SQL]] — the join that performs a linkage attack is an ordinary `JOIN`, and `GRANT` is where privacy by design is written down; [[Probability Basics]] — the counting behind uniqueness.
- **Also builds on:** [[Artificial Intelligence]] — training data is personal data, and a model can memorise and leak it; [[Digital Currency and Blockchain]] — a ledger that cannot delete meets a right to erasure.
- **Sibling:** [[NoSQL and Distributed Data]] — data replicated across regions meets the cross-border rules; [[The Internet and the Web]] — cookies, the mechanism behind the banner.
- **Maths bridge:** [[Exponential Function]] — the $e^{-\lambda}$ of the uniqueness estimate and the $e^{\varepsilon}$ of the privacy guarantee; [[Continuous Random Variables]] — the Laplace distribution.
- **Story:** [[Turing at Bletchley]] — a life in which the state's knowledge of one private fact was the catastrophe.
- **The other half:** [[Privacy-Preserving Computation]] — this card protects what comes *out* of a computation; that one hides what goes *in*: secret sharing, homomorphic encryption, federated learning, enclaves and zero-knowledge proofs.

---

## Beyond Syllabus

### Why "identifiable" had to be in the definition
Recall that three quasi-identifiers singled out 90 % of the city. A law that protected only data *with names attached* would have allowed everything Sweeney did. So both statutes define personal data by identifiability, and the hard cases live at that edge: is an IP address personal data (European courts: usually yes)? A car's number plate? A model trained on your messages? The EU's 2025–26 "Digital Omnibus" proposals tried to narrow the definition so that data would not be personal *for a holder* who lacked the means to identify; the data-protection authorities objected that this would shrink the law's reach, and the member states' working text dropped the change. The definition is where the politics happens because it is where the scope is set.

### Contextual integrity
The philosopher Helen Nissenbaum's account explains why the anchor's phone call feels wrong when no secret was exposed: every flow of information carries the norms of the context it happened in. Your diagnosis flows properly to your doctor and improperly to your employer, though it is the same fact. Purpose limitation is this idea written as law.

### Composition: privacy budgets run out
Differential privacy's guarantees add: answer two queries at $\varepsilon = 1$ each and the combined guarantee is $\varepsilon = 2$. An attacker who may ask the same question a thousand times can average the noise away, so a real system tracks a total budget and stops answering when it is spent. This is why the census had to choose, in public, how to split one budget between accuracy for small towns and accuracy for ethnic minorities.

### The transatlantic transfers saga
European courts twice struck down the legal arrangement for sending personal data to the United States (*Schrems I*, 2015; *Schrems II*, 2020), on the ground that American surveillance law gave Europeans no real remedy. The third arrangement, the 2023 Data Privacy Framework, was upheld by the EU's General Court in September 2025, and an appeal to the Court of Justice was pending in 2026. A good share of the internet's plumbing rests on the outcome.

### The right to be forgotten meets the append-only log
Erasure is simple in a relational table and awkward everywhere else: in backups, in replicated caches, in a machine-learning model's weights, and in a blockchain, which is designed so that nothing can be deleted. The engineering answers (crypto-shredding: encrypt each person's data under its own key and destroy the key; "machine unlearning") are active research, and the reason [[Digital Currency and Blockchain]] designs keep personal data off the chain.

---

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $e^{-N/\text{cells}}$ | `e^{-N/\text{cells}}` | chance of being alone in your combination of fields |
| $k$ | `k` | smallest group sharing a combination of quasi-identifiers |
| $\varepsilon$ | `\varepsilon` | privacy budget: smaller is more private |
| $\Delta f / \varepsilon$ | `\Delta f / \varepsilon` | scale of the Laplace noise for a query of sensitivity $\Delta f$ |
| $e^{\varepsilon}$ | `e^{\varepsilon}` | the most one person can change any output's probability |
