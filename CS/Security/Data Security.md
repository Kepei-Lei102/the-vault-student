---
chinese: 数据安全 (shùjù ānquán)
prerequisites:
  - "[[Operating Systems]]"
  - "[[SQL]]"
  - "[[Error Detection and Correction]]"
  - "[[Famous for the Wrong Thing]]"
  - "[[The Internet and the Web]]"
leads_to:
  - "[[Encryption]]"
tags:
  - subject/computer-science
  - domain/security
  - level/IGCSE
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/0478-5-3
  - syllabus/9618-6-1
  - syllabus/9618-6-2
  - type/deep
  - misconception/a-password-is-stored-somewhere
  - misconception/antivirus-makes-you-safe
  - misconception/validation-checks-truth
---

# Data Security 数据安全

> *Every rule in this card exists because someone lost something. The threats are not a list to memorise; they are the moves in a game that has been played, for real money, since a graduate student's worm took down a tenth of the internet in 1988. This card teaches the exam's list — and then shows the actual mechanism the exam stops at, because you asked how a hack works, and the honest answer is worth more than the vocabulary.*

## Definition

### Formal

**Data security** is the protection of data against unauthorised access, alteration and loss. It is examined as three related properties and the measures that defend them:

- **Security** — data (and the system holding it) is protected from unauthorised access.
- **Privacy** — the right to control who may see data about you, and for what purpose.
- **Integrity** — data is accurate and consistent: what is stored and transmitted is what was intended, unchanged by accident or attack.

Against these stand **threats** (malware, phishing, hacking, denial of service, interception) and, for each, one or more **countermeasures** (authentication, access control, firewalls, anti-malware, encryption, validation, verification). Cambridge splits the material two ways — IGCSE 0478 calls it **cyber security** (§5.3), A-Level 9618 calls it **data security** and **data integrity** (§6.1–6.2) — but the content is one subject, and this card carries both.

### Intuitive

Three questions, asked of every system that holds data worth holding: *can the wrong person get in?* (security), *should this person see this data at all?* (privacy), *is the data still what it should be?* (integrity). A bank cares about all three at once: a stranger must not read your balance (security), a teller must not browse celebrities' accounts (privacy), and a transfer of ¥100 must not arrive as ¥1000 (integrity). Every threat below attacks one of the three, and every defence protects one — knowing *which* is most of the exam.

### 中文锚点

你每天都会收到这样一条短信：**【某某】验证码 483920，5 分钟内有效，请勿泄露给任何人。**登录微信、支付宝付款、12306 买票，一天好几次。它存在的理由，就是这张卡的主题：**数据和钱越来越多地存在系统里，而攻击这些系统是一门能赚到真金白银的生意。**这条短信本身就是一道防线：密码是"你知道的东西"，验证码证明你手里拿着这部手机——这就是下面要讲的**两步验证**；而"请勿泄露给任何人"这半句，防的是骗子打电话来要它——**社会工程**，攻击的是人不是机器。考试把内容分成三个词：**安全**（security，别让不该进的人进来）、**隐私**（privacy，该看的人才能看）、**完整性**（integrity，数据没被改错、没在传输中损坏）。**威胁**你要会描述：**恶意软件**（malware：病毒 virus 会自我复制、蠕虫 worm 自己在网络里传、木马 Trojan 伪装成正常程序、勒索软件 ransomware 加密你的文件勒索赎金、间谍软件 spyware 偷记你的按键）、**钓鱼**（phishing，假邮件骗你点链接、交密码）、**域欺骗**（pharming，把你导到假网站，不用你上钩）、**黑客入侵**（hacking）、**暴力破解**（brute-force，把密码一个个试到对为止）、**拒绝服务攻击**（DDoS，用海量请求把服务器压垮）、**社会工程**（social engineering，骗的是人而不是机器——**杀猪盘**就是它的极端形态）。**防御**要能解释：**认证**（密码、生物识别、两步验证——光 Google 2019 年自己的数据就够说明问题：两步验证拦下了 100% 的自动攻击、96% 的批量钓鱼；**强密码**有个好记的做法——取一个只属于你的画面，比如**脚滑的狐狸**，写成英文再换几个形近字符：`$Iippery_F0x`，你记的是一幅画，机器得挨个试 94 的 12 次方个可能的字符串）、**访问权限**（access levels，谁只能读、谁能写）、**防火墙**（按规则过滤进出的网络流量）、**反恶意软件**、**自动更新**、**加密**（[[Encryption]]，就算被偷走也读不懂）。**完整性**靠两道关：**验证**（validation，机器检查数据"合不合理"——范围、格式、长度、存在性、校验位）和**核验**（verification，检查数据"跟原件一不一样"——双重录入、肉眼核对，传输时靠[[Error Detection and Correction|奇偶校验/校验和]]）。**注意一个关键区分：validation 查的是"合不合理"，不是"真不真实"**——生日填 05/07/2010，格式对、范围也对，但它可能根本不是你的生日；机器管得了形式，管不了真假。卡片最后的"Beyond"部分，回答的是你真正想问的问题：**一次入侵在内存里到底发生了什么？黑客的实验室为什么要把 ASLR（地址空间随机化）关掉？**——那属于操作系统级的攻防，超出任何中学考纲，但"hacking"这个词底下真正的东西，是它。

| English | 中文 | 一句话 |
|---|---|---|
| Security / Privacy / Integrity | 安全 / 隐私 / 完整性 | 别让人进 / 该看才看 / 数据没被改错 |
| Malware | 恶意软件 | virus 复制 · worm 自传 · Trojan 伪装 · ransomware 勒索 · spyware 偷窥 |
| Phishing / Pharming | 钓鱼 / 域欺骗 | 骗你点假链接 / 把你导到假网站（不用你上钩） |
| Brute-force / DDoS | 暴力破解 / 拒绝服务 | 密码逐个试 / 海量请求压垮服务器 |
| Social engineering | 社会工程 | 攻击的是人不是机器（杀猪盘） |
| Authentication | 认证 | 密码 / 生物识别 / 两步验证 |
| Firewall | 防火墙 | 按规则过滤进出的网络流量 |
| Validation vs Verification | 验证 vs 核验 | 检查"合理" vs 检查"和原件一样" |
| Encryption | 加密 | 就算被偷走也读不懂——[[Encryption]] |

---

## Part I — The three properties, and why they differ

Students collapse the three into "keeping data safe", and the exam separates them because the *defences* differ. Security is a wall against outsiders; privacy is a rule about insiders; integrity is a check on the data itself.

- **Security is broken** when someone who should have no access gets some: a stolen password, an unpatched server, a hacked account. The defences are authentication and access control.
- **Privacy is broken** when someone with legitimate access uses it beyond its purpose: the hospital clerk who looks up a neighbour's records, the app that sells your location. The defences are access *levels* (each role sees only what it needs) and law — China's *Personal Information Protection Law* (2021), Europe's GDPR.
- **Integrity is broken** when data changes when it should not: a corrupted transfer, a mistyped date of birth, a bit flipped in transmission. The defences are validation, verification, and the [[Error Detection and Correction|parity and checksum]] machinery of transmission.

A system can have any one without the others. An encrypted database with one shared password has security without privacy. A carefully validated form on an open network has integrity without security. The exam's favourite trap is a scenario that names one and asks for the defence of another.

## Part II — Threats

The 0478 list is the fuller one; 9618 uses the same names. Learn each as *mechanism → aim → the property it attacks*, because the exam asks you to *describe the process*, not just name it.

| Threat | The mechanism, in one line | Attacks |
|---|---|---|
| **Virus** | malicious code that attaches to a file and *replicates* when run, filling storage or corrupting data | integrity, availability |
| **Worm** | like a virus but *self-propagating* across a network with no host file and no user action | availability |
| **Trojan** | malware *disguised* as a legitimate program the user installs willingly | security |
| **Spyware** | records what you do — keystrokes, screens — and sends it to the attacker | privacy, security |
| **Ransomware** | encrypts your files and demands payment for the key | availability |
| **Phishing** | a *legitimate-looking message* lures the user to a fake site to hand over credentials | security (via the human) |
| **Pharming** | redirects the user to a fake site *without their action* — poisoned DNS or a hosts file | security (via the machine) |
| **Brute-force** | tries passwords one after another until one works | security |
| **DDoS** | floods a server with requests from many machines so real users cannot get through | availability |
| **Social engineering** | manipulates a *person* into breaking security — the con, not the code | all three |

Two distinctions the schemes reward. **Phishing needs the user to act** (click, reply); **pharming does not** — it is automatic, so "you were careful" does not protect you. And **a worm self-propagates while a virus needs a host and a trigger** — the Nov 2023 paper's "one difference and one similarity" question is exactly this kind.

> [!warning] The threat is usually the human
> Every technical defence below can be defeated by one person clicking one link. Social engineering — and its industrial-scale form, the **杀猪盘 "pig-butchering" scam** that grooms a victim for weeks before the fake investment — is the reason China stood up the National Anti-Fraud Centre and passed the *Anti-Telecom-and-Online-Fraud Law* (in force 1 December 2022). The most cost-effective security measure ever measured is not a firewall; it is teaching people to distrust a message that creates urgency.

## Part III — Defences

For each threat, a countermeasure — and the exam wants the *how*, not the name.

- **Authentication** proves you are who you claim. Passwords (something you know), biometrics (something you are — fingerprint, face), and **two-step / two-factor verification** (something you have — a code on your phone). 2FA is the single highest-value control: Google's 2019 study found an on-device prompt blocked **100% of automated attacks, 99% of bulk phishing, and 90% of targeted attacks**. A password alone blocks far less.
- **Access control / access levels** decide, once you are in, what you may see and change. This is the *privacy* defence: the database's `GRANT` from [[SQL]], the file permissions of [[Operating Systems]]. Least privilege — give every account the minimum it needs — is the principle behind it.
- **Firewall** monitors traffic in and out and rejects anything not matching its rules (a blacklist or whitelist of addresses; closing ports known to be used by attackers). It is the network wall, not a scanner of content.
- **Anti-malware** scans files against a database of known-malware signatures (and, increasingly, behaviour) and quarantines or deletes matches. It must be *kept updated*, because the signature database is only as good as its last update — which is why **automatic software updates** are a control in their own right: most breaches exploit a hole that was patched months earlier.
- **Encryption** scrambles data so that intercepting it yields nothing without the key. It is the last-line defence: it does not stop the theft, it makes the theft worthless. The mechanism — symmetric vs asymmetric keys, public and private — is [[Encryption]].

![[data-security-crack-time.svg|700]]

The chart is why "use a long password" and "the site must hash properly" are two different, both-necessary rules. It plots the expected time to brute-force a password by its shape, under two assumptions about how the site *stored* it. A six-letter lowercase password stored as a fast MD5 hash falls in under a hundredth of a second; the same password stored with a deliberately slow hash (bcrypt) takes twenty-five minutes. Length helps the user; a slow, salted hash is the site's job — and the gap between the two bars is the site keeping its promise. Four random words beat a short "complex" password, which is why the advice changed.

### Making a password that is strong — and that you can remember

The chart speaks the machine's language: length and character classes. Your memory speaks another: *one thing I can picture*. A good password is where the two meet, and there is a recipe. Take an image that is yours and vivid — 脚滑的狐狸, the slippery fox — write it in English, join the words, then swap a few letters for the symbols and digits that look like them:

```
Slippery Fox  →  Slippery_Fox  →  $Iippery_F0x
                                   S→$    l→I    o→0
```

Twelve characters, all four classes — upper, lower, digit, symbol. To you it is a fox on ice. To an attacker who knows nothing about it, it is one string among $94^{12} \approx 5 \times 10^{23}$, and the chart's two `$Iippery_F0x` rows show what that costs:

| The attacker's strategy | Guesses needed | Stored as MD5 | Stored as bcrypt |
|---|---|---|---|
| Blind brute force over every 12-character string | $\approx 2 \times 10^{23}$ | 75,000 years | longer than the universe |
| Guesses the whole recipe: two English words, a separator, the usual substitutions, a capital | $\approx 10^{13}$ | about a minute | about a year and a half |
| `Password1!` and its thousand cousins | $< 10^{6}$ | 10 microseconds | 10 seconds |

Read the middle row honestly. Crackers *know* the substitutions — `S→$`, `o→0`, `l→1` and `l→I` are in every rule list — so the swaps alone add little. What makes the password strong is that the phrase is **private** (not a lyric, not a proverb, not in the million-entry breach lists where `Password1!` lives) and **long**: twelve characters push even the recipe-guessing attacker to ten trillion tries — a million *million*, not a million — and with a properly slow hash on the site's side, to years. The principle underneath: **you remember meaning; the machine must search characters.** Pick an image nobody else would, make it twelve or more, and never reuse it — one password per site, or a password manager holding all of them behind a single fox like this one, with two-factor on anything that matters.

## Part IV — Integrity: validation and verification

Integrity is the 9618 §6.2 half, and it turns on a distinction students routinely miss.

- **Validation** is the computer checking that entered data is *reasonable* — that it *could* be right. The named checks: **range** (a month is 1–12), **format** (a date matches dd/mm/yyyy), **length** (a phone number has the right count of digits), **presence** (a required field is not blank), **type/character**, **limit** (one-sided range), and **check digit** (an extra digit computed from the rest — the ISBN and bank-card mechanism worked in full in [[Error Detection and Correction]]).
- **Verification** is checking that data is *unchanged* — that it matches its source. On entry: **double entry** (type it twice, the computer compares) or a **visual check** (compare against the original by eye). On transfer: **parity**, **checksum**, **check digit** — the [[Error Detection and Correction]] machinery.

> [!warning] Validation checks *reasonable*, never *true*
> A date of birth of 05/07/2010 can pass every validation check — right format, right range, present — and still be a lie. Validation catches the *impossible* and the *malformed*; it cannot catch the *false*. This is the single most examined misunderstanding in §6.2, and it is also the door to the attack in Part VI: a field that is merely "valid" is not safe, because *valid* and *safe* are different questions.

## Worked examples — the real papers

### June 2026 Paper 12 Q2 (9618) — verification, validation, and a virus [4 + 3 + 3 + 3]

*(a) Two methods of data verification during entry.* *Tool: verification = compare against the source.* **Visual check** (a person compares the entered data with the original) and **double entry** (enter twice, the computer compares). The scheme's note is the trap: the question says *verification*, and a candidate who lists validation checks scores nothing. *(b) Two validation methods for a date of birth 05/07/2010, and how each applies.* **Presence check** (the field cannot be blank) and **range check** (must fall between two dates); the mark is for *applying* it to the date, not naming it — and "range" and "limit" cannot both be given as they are the same idea one-sided. *(c) Describe a virus, and one method to restrict it.* "Malicious software that replicates and can delete or corrupt data" plus **anti-virus software** — "scans files against a database of known viruses and quarantines or deletes a match." Each threat-and-defence pair is description + method + matching description, three marks, and the method's description must *match the method chosen*.

### November 2023 Paper 13 (9618) — the security-measures triple, and pharming vs phishing [3 + 2 + 2 + 3]

*State how each protects a system: firewall, encryption, passwords.* One mark each, in mechanism language: firewall *"monitors incoming and outgoing traffic and rejects any that does not meet the set rules"*; encryption *"ensures intercepted data cannot be understood without the decryption key"*; passwords *"prevent unauthorised access."* Then *one difference and one similarity between pharming and phishing*: the difference is that **pharming redirects automatically to a fake site while phishing uses a message to prompt the user to act**; the similarity is that **both impersonate a legitimate organisation to obtain personal or financial data**. And *how to restrict malware*: download only from reputable sources, keep backups, run updated anti-malware, use a firewall to block unused ports, deny admin rights to everyday users — each with its *because*.

### June 2024 Paper 11 Q9 (0478) — the firewall, in five marks [5 + 2]

*Explain how a firewall operates to help protect the network.* The IGCSE scheme wants the mechanism spelled out: criteria can be set (a blacklist or whitelist of IP addresses); it examines traffic entering the network; it checks the traffic against the criteria and rejects what does not meet them; ports used by hackers can be blocked. Five marks is five distinct mechanism statements — the commonest loss is writing "it blocks hackers" three ways. *(ii) Two examples of malware a firewall helps against:* any two of virus, worm, Trojan, spyware, adware, ransomware.

### June 2025 Paper 11 Q9 (0478) — a brute-force attack, and three defences [1 + 3]

*Describe how a hacker performs a brute-force attack:* "tries to guess a password by repeatedly entering different combinations." *Three cyber-security solutions to prevent it:* **strong passwords** (long, mixed characters), **two-step verification / biometrics**, and **limiting the number of login attempts** — the last is the one specific to brute force, and the chart in Part III is the argument for the first.

### November 2025 Paper 11 (0478) — identify phishing [and describe the process]

*Describe the process of phishing:* a legitimate-looking email is sent; the user clicks a link (or replies); the user is directed to a fake website that harvests their details. *Two ways to identify it:* check the sender's email address, check the tone and spelling, check the URL the link actually points to — the same three habits the 0478 §5.3 solution list names, and the ones the Anti-Fraud app tries to build.

## Where this is the working tool

**Every login you have.** When you set a password, a good site never stores it — it stores a **salted hash**: a one-way fingerprint ([[Hash Tables]]' cryptographic cousin) with a random salt so that two people with the same password get different fingerprints, run through a deliberately slow function so that a stolen database cannot be brute-forced. When the 2013 Adobe breach exposed 150 million passwords stored the *wrong* way, "123456" was instantly readable for millions of accounts. The hands-on below builds the right version in three lines.

**Every https.** The padlock is [[Encryption]] and the SSL/TLS handshake of 9618 §17: your browser and the server agree on a key no eavesdropper can compute, so the café wifi carries your bank login as noise. The card that dropped from HTTP to HTTPS is the same threat — interception — answered by encryption.

**Every patch Tuesday.** The largest breaches of the last decade were not clever: **WannaCry** (May 2017) shut down hospitals across the UK's NHS and 200,000 machines in 150 countries using a Windows hole Microsoft had patched *two months earlier*; **Equifax** (2017) leaked 147 million people's records through an Apache Struts hole patched *six months earlier*. "Keep software updated" is the least glamorous line on the syllabus and the one that would have stopped both.

## Misconceptions

1. **"My password is stored on the server."** A competent server stores a *salted hash*, not the password; it checks your login by hashing what you typed and comparing. If a site can email you your *actual* password, it stored it wrongly, and you should assume it is already compromised.
2. **"Antivirus makes me safe."** Anti-malware catches *known* malware and nothing else; it is one layer. The 2017 breaches above walked past every antivirus because they exploited unpatched software, not a known virus.
3. **"Validation checks that data is true."** It checks that data is *possible*. A valid date of birth can still be wrong; a valid input can still be an attack (Part VI). Validation is a sieve for the malformed, not a lie detector.
4. **"Encryption stops hackers getting in."** Encryption does not stop entry; it makes what they take unreadable. It is the last line, not the wall — you still need authentication and patching.
5. **"A firewall scans for viruses."** A firewall filters *traffic* by rule; it does not inspect files for malware — that is anti-malware's job. They are different layers against different threats.
6. **"Hacking is a lone genius typing fast."** Overwhelmingly it is a phishing email, a reused password, or an unpatched server — the boring three. The clever memory-corruption attack of the Beyond section is real and worth understanding, but it is not how most breaches happen.

## Beyond syllabus — how a hack actually works, and the wall the lab turns off

No school board explains what "hacking" means at the level of the machine. Here is the honest version — and with it the answer to a question that comes up the moment anyone tries a hands-on hacking lab: why the lab has to switch a protection *off* before its first exercise will work. The lab meant throughout this section is a specific one: the **Attack Lab** of **CMU 18-213 / 15-213, *Introduction to Computer Systems*** — the course behind the textbook *Computer Systems: A Programmer's Perspective* — in which students are handed two small programs and must make them run code they were never meant to run, by overflowing a buffer. It is the best-known teaching hack-lab in the world, copied by universities everywhere, and it is what "the lab" means below.

>[!important] A promise, before you read on
> What follows is real offensive knowledge — how an intrusion actually works. It is here for one reason: **you cannot defend what you do not understand, and you cannot fix what you cannot see.** Every technique below is taught in every university security course and used every day by the people who *protect* systems. So make the promise every ethical hacker makes, and mean it: **I will use this only to understand, to defend, and to test systems I own or have written permission to test — never to harm a person, steal, or break into what is not mine.** The difference between a security engineer and a criminal is not knowledge; it is consent and intent. The law agrees: unauthorised access is a crime in every country here, with or without damage. Learn the mechanism; keep the promise.

### The buffer overflow — data becoming code

[[Arrays]] and [[Von Neumann machine]] both flagged this: a computer keeps code and data in the *same* memory, and a **buffer overflow** exploits it. A function stores its local variables on the **stack**, and just above them sits the **return address** — where the CPU will jump when the function finishes. If the program copies input into a fixed buffer *without checking the length* (the notorious C function `gets()` does exactly this), a long enough input runs off the end of the buffer and overwrites the return address. Overwrite it with an address the attacker chose, and when the function returns, the CPU jumps *there* — into code the attacker smuggled in as "data".

![[data-security-stack-smash.svg|880]]

This is not theory. The **Morris worm** (1988), the first internet worm, spread through exactly this hole in the `fingerd` service and took down an estimated tenth of the internet; the technique was written up for everyone in Aleph One's 1996 *Phrack* article "Smashing the Stack for Fun and Profit"; and buffer overflows drove a large fraction of every serious exploit for the next twenty years, up to and including WannaCry.

### Three walls — and the one the lab removes

The industry answered with three defences, layered, each stopping one move of the attack:

1. **Stack canary** (StackGuard, 1998): a secret value placed just below the return address. The function checks it before returning; if an overflow changed it, the program aborts. Detects the overwrite.
2. **NX / DEP / W^X** (hardware from ~2003, Windows XP SP2 2004): memory is marked *writable* or *executable*, never both. The bytes the attacker wrote into the buffer are data, so the CPU refuses to run them. Stops the smuggled code.
3. **ASLR — Address Space Layout Randomization** (PaX 2001; Linux 2005; Windows Vista 2007; macOS): the stack, the heap and the libraries are loaded at a *different random address every run*. So the attacker cannot know what address to overwrite the return address *with* — the target moved.

**This is the setting the 18-213 Attack Lab turns off.** To *demonstrate* a buffer overflow — to have students compute an address on paper and see the program jump there — the addresses must be stable between runs. So the lab's first target, `ctarget`, runs with ASLR disabled and an executable stack, compiled without the canary: all three walls down, so that the first three phases can be solved with pen, paper and a hex editor. On a Linux machine of your own the same switch is `echo 0 > /proc/sys/kernel/randomize_va_space`, with `-fno-stack-protector -z execstack` at compile time to drop the other two walls. Its second target, `rtarget`, puts randomisation and the non-executable stack back — and the last two phases can then only be passed by return-oriented programming, the technique of the next subsection. The lab teaches the walls by first removing them and then rebuilding them one at a time. It is exactly analogous to a chemistry lab removing a safety interlock to demonstrate the reaction the interlock prevents: correct in the sandbox, never on a real machine. And the question this raises has a clear answer: is a memory-protection feature really *cyber security*? Yes — it sits under **cyber security** (specifically *systems* or *software* security), one level below the network-and-human threats the syllabus lists. The split is worth stating: the school boards teach the *outer* game (malware, phishing, firewalls, the human); this section is the *inner* game (memory corruption and the OS mitigations), which is [[Operating Systems]]' memory protection turned into an attack surface.

### The modern shape

The walls raised the cost, so attacks got cleverer: **return-oriented programming** stitches an exploit out of fragments of the program's *own* code (defeating NX, since it runs no new code), and info-leak bugs first *read* memory to defeat ASLR before overwriting anything. The arms race is why memory-safe languages — Rust above all, and the reason Android and Windows are being partly rewritten in it — are the real long-term answer: they make the overflow impossible at the source rather than surviving it at run time. That is [[Decouple and Recouple]]'s lesson in another key: the safest coupling between input length and buffer size is one the language enforces, not one the programmer remembers.

## Hands-on

Everything here runs on the student's own machine, with tools already installed.

1. **Watch ASLR move the ground.** On Linux or macOS, run this twice:

   ```bash
   python3 -c "import ctypes; x=ctypes.c_int(); print(hex(ctypes.addressof(x)))"
   ```

   The address is different every run — that is ASLR. On Linux you can then turn it off (as root) with `echo 0 | sudo tee /proc/sys/kernel/randomize_va_space` and watch the address freeze; set it back to `2` immediately after. That freeze is precisely what a buffer-overflow lab depends on — and it is only ever done on a machine you own, for the promise above.

2. **Store a password the right way.** Never `sha256(password)` alone — salt it and slow it down:

   ```python
   import hashlib, os
   salt = os.urandom(16)
   stored = hashlib.pbkdf2_hmac("sha256", b"correct horse battery staple", salt, 600_000)
   # keep (salt, stored); to check a login, recompute with the same salt and compare
   ```

   The 600,000 iterations are what turns the red bar into the green bar in the chart.

3. **Feel a brute force.** Time how long Python takes to try every 4-digit PIN (`for p in range(10000)`) — instant — then every 6-character lowercase password (`itertools.product`), and watch it become minutes. The exponent in the length is the whole defence.

4. **Read the real advice.** Your phone's built-in password manager will flag reused and breached passwords; the site *haveibeenpwned.com* tells you which of your accounts are in a known breach. Both are this card, applied to your own life.

## Exam Notes

### Cambridge 0478 (§5.3 — Paper 1, Computer Systems)

- **§5.3.1 — describe the process and aim of each threat:** brute-force, data interception, DDoS, hacking, malware (virus, worm, Trojan, spyware, adware, ransomware), pharming, phishing, social engineering. "Describe the process" means the mechanism, not just the name.
- **§5.3.2 — explain the solutions:** access levels, anti-malware, authentication (username/password, biometrics, two-step verification), automatic software updates, checking spelling/tone of communications, checking the URL of a link, firewalls, privacy settings, proxy servers, SSL. Match a solution to the threat it counters — the papers pair them.
- Question shapes: describe a threat's process (2–3); firewall mechanism (up to 5); brute-force + three preventions (1 + 3); phishing process + how to spot it; complete-the-paragraph on encryption (§5.3 overlaps the encryption row).

### Cambridge 9618 (§6.1–6.2 — AS Paper 1)

- **§6.1 Data Security:** the security/privacy/integrity distinction; the need to protect *both* data and the system; security measures from a stand-alone PC to a network (user accounts, passwords, authentication incl. digital signatures and biometrics, firewall, anti-virus, anti-spyware, encryption); the network/internet threats (malware, hackers, phishing, pharming); methods to restrict each; and access rights + encryption as data-protection measures.
- **§6.2 Data Integrity:** validation vs verification; the named validation checks (range, format, length, presence, existence, limit, check digit); verification on entry (visual check, double entry) and on transfer (parity — byte and block — and checksum). The validation checks and the transfer verification are [[Error Detection and Correction]].
- **§17.1 Encryption** (symmetric/asymmetric keys, SSL/TLS, digital certificates and signatures, quantum cryptography) is [[Encryption]] — the A2 depth pass on the encryption line named here.
- Question shapes: state-how-each-protects (firewall/encryption/passwords, 1 each); validation-and-use table (identify + apply); threat description + restriction method + matching description (3 each); one-difference-one-similarity (pharming/phishing).

### IB Computer Science (A2.4 Network security)

- Network security sits in A2.4 with authentication, encryption and the threat/countermeasure pairing; the encryption depth is [[Encryption]]. This card carries the threat-and-defence framing; the network specifics are the networks bay.

### Not examined on…

- **AP Computer Science A** — no security content; it is a Java programming course. The buffer-overflow and ASLR material in Beyond is university systems-security, beyond every school board here, and is included as enrichment because it is the real mechanism under the word "hacking".

## Quick reference

| Ask | Answer in one line |
|---|---|
| Security vs privacy vs integrity | keep intruders out / control who among the allowed may see / keep data unchanged |
| Virus vs worm | virus needs a host file and a trigger; worm self-propagates across a network |
| Phishing vs pharming | phishing needs the user to act; pharming redirects automatically |
| Validation vs verification | reasonable / unchanged (validation ≠ true) |
| Named validation checks | range, format, length, presence, existence, limit, check digit |
| Verification methods | entry: visual check, double entry; transfer: parity, checksum |
| Highest-value single control | two-factor authentication (Google: 96–100% of phishing/automated blocked) |
| The password rule | length (user) + salted slow hash (site); never store the password itself |
| A strong password you can remember | a private image, substituted — `$Iippery_F0x` (脚滑的狐狸): one picture for you, 94¹² strings for the machine |
| The three memory walls | stack canary (detect) · NX/DEP (no run) · ASLR (moving target) |
| Why the 18-213 Attack Lab disables ASLR | to make addresses stable so the overflow is demonstrable (then `rtarget` turns it back on) |

## Connections

- **Parents:**
   - [[Operating Systems]] — access rights, user accounts and memory protection are the OS's job; this card is the threat model those features answer, and Beyond is that memory protection seen from the attacker's side.
   - [[SQL]] — SQL injection is the database face of "valid is not safe"; the parameterised query is that card's fix, and the same lesson as validation here.
   - [[Error Detection and Correction]] — the integrity half: parity, checksum and the check digit are §6.2's transfer-verification, worked in full there.
- **Child:** [[Encryption]] — the last-line defence, the mechanism (symmetric/asymmetric, public/private keys, SSL/TLS, digital certificates) that this card names and 9618 §17 examines.
- **Uses:** [[Hash Tables]] — the cryptographic hash behind salted password storage, the resisting-an-opponent cousin of the table hash; [[Arrays]] and [[Von Neumann machine]] — the buffer overflow is their code-is-data shadow made into an attack; [[Decouple and Recouple]] — memory safety as a coupling the language enforces so the programmer cannot forget it.
- **Related:** [[Networks]] — firewalls, proxies and interception are network-layer; [[Data Protection and Privacy]] — the legal side (PIPL, GDPR) of the privacy property; [[File Systems]] — the other face of data security: *deleting* a file only unlinks it, formatting only rewrites the metadata, an SSD's TRIM erases lazily, and the only real erase is key destruction — data remanence is the privacy leak nobody sees.
- **Misconception traps cleared:** a password is stored somewhere; antivirus makes you safe; validation checks truth; encryption stops entry; a firewall scans for viruses; hacking is a lone genius.
