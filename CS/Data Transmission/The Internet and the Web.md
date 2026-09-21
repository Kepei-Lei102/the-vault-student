---
chinese: 互联网与万维网 (hùliánwǎng yǔ wànwéiwǎng) — 网址、域名解析、Cookie、IP 地址与局域网拓扑
prerequisites:
  - "[[Networks]]"
  - "[[Encryption]]"
leads_to:
  - "[[Data Security]]"
  - "[[Digital Currency and Blockchain]]"
tags:
  - subject/computer-science
  - domain/networks
  - domain/data-transmission
  - level/IGCSE
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/0478-3-4
  - syllabus/0478-5-1
  - syllabus/9618-2-1
  - syllabus/IB-CS-A2-2
  - type/deep
  - misconception/the-internet-is-the-web
  - misconception/dns-is-one-server
  - misconception/a-cookie-is-a-program
  - misconception/https-means-the-site-is-honest
---

# The Internet and the Web 互联网与万维网

> *You typed a name. Computers deliver only to numbers. Between the name and the page there is a chain of servers that translate, a handshake that proves who you are talking to, a request in plain text, and a small file the site leaves behind so it will know you tomorrow. And the whole of it runs on something older and bigger than itself, which most people call by the wrong name.*

## Definition

### Formal

The **internet** is the global network of networks: the physical infrastructure (cables, fibre, radio links, satellites, routers, switches) together with the **TCP/IP** protocols that move packets between any two IP addresses on Earth. The **World Wide Web** is one *service* that runs on the internet: a collection of **web pages** written in **HTML**, identified by **URLs**, transferred by **HTTP** or its encrypted form **HTTPS**, stored on **web servers** and displayed by **web browsers**. Email, file transfer, video calls and online games are other services on the same internet that are not part of the web.

A **URL** (uniform resource locator) names a page by protocol, domain name and file path. The **domain name service (DNS)** is the distributed system of servers that translates a domain name into an **IP address**, without which no packet can be delivered. A **cookie** is a small text file a web server asks the browser to store and return on later requests; a **session** cookie is deleted when the browser closes, a **persistent** cookie has an expiry date.

Every device on a network has a **MAC address** (normally a 48-bit link-layer identifier; a factory address is assigned by the manufacturer of its **network interface card**) and, when connected, an **IP address** (**IPv4**: 32 bits; **IPv6**: 128 bits), which may be **static** or **dynamic**, **public** or **private**. A **router** forwards packets toward their destination, assigns IP addresses on its own network, and joins a **LAN** to the internet.

### Intuitive

The internet is the road system: tarmac, bridges, junctions, and the highway code that lets any vehicle reach any address. The web is the postal service that uses those roads — one very large customer among many. A URL is a postal address written for the web; DNS is the directory that turns "the bakery on the corner" into a street number; the router at your door is the postman who knows which room inside the house each letter is for, and which of the house's letters go out to the street. A cookie is the loyalty card the shop hands you, which you show on your next visit so they remember your order.

### 中文锚点

想想今天早上。醒来先看微信：用的是互联网，没有任何网页参与。打开浏览器上 B 站看了个视频：那是万维网，跑在互联网上。登录游戏：又是互联网，不是万维网——游戏用自己的一套话跟服务器聊，根本没有"页面"。跟国外的朋友视频通话：互联网，不是万维网。然后你在聊天里点了一个链接，微信内部打开了一个网页：那是万维网，套在一个 App 里，跑在互联网上。你一整天两样都在用，而它们**不是一回事**。**互联网**是路网：电缆、光纤、基站、路由器，加上把一个数据包从任何一个地址送到另一个地址的规则。**万维网**是路上跑的东西之一——用 HTML 写的页面，每个页面都有一个 URL，由浏览器取回——而且只是"之一"：邮件、游戏、通话、App 更新、付款，都走同一张路网，却从来不是一个页面。最好认的记号是**地址栏**：看得见地址栏，你就在万维网上；看不见，你多半还在互联网上，只是不在万维网上。

### 术语对照 (Terms)

| English | 中文 | 今天早上的哪一件事 |
|---|---|---|
| The internet | 互联网 | 微信、游戏、视频通话——全都是 |
| The World Wide Web | 万维网 | 浏览器里的 B 站、聊天里点开的那个网页 |
| URL · domain name · DNS | 网址 · 域名 · 域名解析 | 你敲的名字，和把它变成数字的那一步 |
| HTTP / HTTPS | 网页传输协议 / 加密版 | 地址栏里的那把锁 |
| Cookie (session / persistent) | Cookie（会话 / 持久） | 明天还在的购物车 |
| MAC address · IP address | MAC 地址 · IP 地址 | 本地链路上的地址 · IP 网络上的地址 |

---

## Part I — The internet is not the web

The confusion is understandable: for most people the browser *is* the internet. But the two have different birthdays, different inventors and different jobs, and both Cambridge boards ask for the difference in so many words.

![[internet-vs-web.svg|960]]

*The internet is the bottom layer: hardware plus the protocol stack from [[Networks]], moving packets between IP addresses without caring what they mean. The web is one of the services on top — the biggest, but one of many. Email, games, video calls and the API traffic behind every app use the internet and never fetch a web page.*

| | The internet | The World Wide Web |
|---|---|---|
| What it is | infrastructure: networks joined by routers, speaking TCP/IP | a service: pages of HTML linked by hyperlinks |
| Born | 1969 (ARPANET); TCP/IP adopted 1983 | 1990, Tim Berners-Lee at CERN; public 1991 |
| Addressed by | IP addresses | URLs |
| Its protocol | IP, TCP, UDP | HTTP, HTTPS (on top of TCP) |
| You use it through | anything with a network connection | a web browser |
| Without the other | works fine — email and games carry on | cannot exist |

The examined sentence, in one line: **the internet is the network; the web is a collection of pages that uses the network.** A student who writes "the internet is where you look at websites" has described the web.

---

## Part II — From URL to page

### The URL

![[internet-url-anatomy.svg|960]]

*The three parts the boards name — protocol, domain name, web-page (file) name — and two more a browser reads. The 0478 question gives a URL with brackets under it and asks for the three names; the 9618 question asks what each part is for.*

The **protocol** says how to talk to the server: `http://` in plain text, `https://` encrypted and authenticated. The **domain name** says which server, in a form humans can remember; it is hierarchical, read from the right — `.com` is the top-level domain, `bilibili` the organisation, `www` a particular machine or service. The **path** names the file or resource on that server; if it is missing, the server sends its default page, usually `index.html`.

### The browser

A **web browser** is the program that turns a URL into a page. The boards want its functions listed: it **renders HTML** (turns the mark-up into the layout you see), provides the **address bar**, **stores cookies**, keeps **bookmarks** and **history**, runs **multiple tabs**, offers **navigation** (back, forward, refresh), keeps a **cache** of recent pages, and runs the **JavaScript** that makes pages interactive. It also does the one thing this section is about: it asks for the page.

### DNS: the name becomes a number

A computer cannot deliver to `www.bilibili.com`; packets carry IP addresses, not names. So the browser first asks the **domain name service**. DNS is not one server but a **hierarchy** of them, each holding a table of names against addresses:

1. The browser sends the domain name to its **resolver** — the DNS server given by the ISP, the home router, or a public one such as 223.5.5.5 or 8.8.8.8.
2. If the resolver has seen the name recently it answers from its **cache**. If not, it asks a **root server**, which does not know the answer but knows who handles `.com`.
3. The **.com server** does not know either, but knows the **authoritative server** for `bilibili.com` — the organisation's own.
4. The authoritative server returns the IP address; the resolver caches it for the **TTL** (time to live) the record specifies, and passes it to the browser.

![[internet-url-to-page.mp4]]

*The chain, animated: the question climbs the hierarchy until a server that knows answers, the answer is cached on the way back, and only then can the browser connect. Then the TCP handshake, the TLS certificate, the request, the HTML, and the cookie — and the cookie going back on the next visit.*

The mark scheme's version, which is what to write: *the browser sends the URL (domain name) to the DNS; the DNS stores a table of domain names and matching IP addresses; it searches for the match; if it is not found the request is passed to a higher-level DNS until it is; the IP address is returned to the browser.* The script `internet-dns-by-hand.py` beside this card does the query with no library at all — a 29-byte packet over UDP — and reads the answer out of the bytes:

```
question: www.bilibili.com  (35 bytes on the wire)  ->  resolver 223.5.5.5:53 over UDP
answer:   99 bytes back in 38 ms; flags 0x8180 (bit 15 set = this is a response)
  A     119.84.174.66    TTL 41 s  (cache it for that long, then ask again)
  A     117.23.60.14     TTL 41 s
  A     222.210.39.59    TTL 41 s
  A     119.84.174.67    TTL 41 s
```

Four addresses for one name, and a TTL of forty-one seconds: a large site answers with several servers near you and changes the list often, which is how it spreads the load and survives a server failing.

### HTTP, HTTPS, and the page

With the address in hand the browser opens a **TCP connection** to the web server ([[Networks]]) and sends an **HTTP request** — a few lines of plain text asking for the path. The server replies with a status line (`200 OK`), headers, and the **HTML** of the page; the browser renders it and issues more requests for every image, style sheet and script the HTML names.

**HTTPS** is HTTP inside a **TLS** tunnel. Before any request is sent, the server presents a **certificate** signed by an authority the browser trusts, proving that whoever holds the private key really is `bilibili.com`; the two sides then agree a session key and encrypt everything ([[Encryption]] has the padlock's full mechanism). The exam contrast: **HTTP sends data in plain text that anyone on the path can read or alter; HTTPS encrypts it and authenticates the server.** The padlock in the address bar means exactly that and nothing more — it does not mean the site is honest, only that you are talking to the site the name claims, privately.

```
HTTPS to example.com: TLSv1.3 with cipher TLS_AES_256_GCM_SHA384
  certificate for: example.com  issued by: SSL Corporation  valid until: Oct 27 22:17:21 2026 GMT
```

*From `internet-url-and-cookies.py`: the handshake made, the certificate's subject, issuer and expiry read off it.*

---

## Part III — Cookies: how a site remembers you

HTTP has no memory: every request arrives as if from a stranger. A **cookie** fixes that. In its reply the server adds a header, `Set-Cookie: name=value`, and the browser stores that small text file and sends it back, unasked, with every later request to the same site. The site reads it and knows which basket, which login, which preferences belong to this visitor.

| | Session cookie | Persistent cookie |
|---|---|---|
| Lifetime | until the browser is closed | until its expiry date (`Expires` or `Max-Age`) |
| Typical use | shopping basket during one visit; progress through a multi-page form; "you are logged in" for this session | staying logged in across visits; remembered language and preferences; targeted advertising; items kept in the basket for days |
| Where it lives | in the browser's memory | in a file on the device |

The script fetches a site's front page and sorts what it sets:

```
GET / from github.com -> HTTP 200; the server set these cookies:
  _gh_sess             session (no expiry: dies with the browser)
  _octo                persistent (has Expires/Max-Age)
  logged_in            persistent (has Expires/Max-Age)
```

One of each kind on the first visit. The 0478 scheme's list of uses — *saving personal details, tracking preferences, holding items in a shopping cart, storing login details, targeted advertising* — is exactly what those three do. The privacy side belongs to [[Data Security]]: a cookie is only text, it cannot run, but a persistent cookie set by an advertising network appears on every site that carries its adverts, and that is how one company can follow one browser across the web.

---

## Part IV — Addresses, and the box that hands them out

![[internet-addresses.svg|960]]

*Three addresses on one laptop. A factory MAC address identifies a network interface; software can use a different local address. An IP address identifies an interface on an IP network. The script `internet-addresses.py` counts the address spaces and splits a subnet.*

**The NIC and the MAC address.** A computer joins a network through a **network interface card** (wired or wireless). Each NIC is given a **MAC address** at manufacture: 48 bits, written as six pairs of hexadecimal digits, the first three pairs identifying the **manufacturer** and the last three a **serial number** — the conventional manufacturer-assigned format is intended to provide unique addresses. The MAC address is used on the local link: an Ethernet frame is delivered to a MAC address, an IP packet to an IP address ([[Networks]] Part I, the link layer and the internet layer).

**IPv4 and IPv6.** An IP address identifies a device on the internet so packets can be routed to it. **IPv4** uses 32 bits, written as four denary numbers from 0 to 255 separated by dots: about 4.3 billion addresses, and the world ran out of unallocated ones between 2011 and 2019. **IPv6** uses 128 bits, written as eight groups of four hexadecimal digits separated by colons, with one run of zero groups allowed to collapse to `::` — $3.4 \times 10^{38}$ addresses, enough that every device can have a permanent public one. China has the largest IPv6 deployment in the world: over half of its internet traffic has run on IPv6 since 2023.

**The real-world qualification:** software can use a **locally administered MAC address**, including a randomised private Wi-Fi address. It can vary by network or rotate, so a MAC is not an unchangeable identity or proof of who is connecting. [Apple documents private Wi-Fi addresses](https://support.apple.com/en-ie/102509) as a protection against tracking.

**Static or dynamic; public or private.** A **static** address is fixed; a **dynamic** one is lent by the network for a while (through **DHCP**) and may change on the next connection. A **public** address is globally routable, though firewalls and routing policy may prevent access; a **private** address (ranges such as `192.168.x.x`, `10.x.x.x`, `172.16–31.x.x`) is valid only inside one LAN and is never routed on the internet. Your laptop almost certainly has a private, dynamic IPv4 address; your **router** holds the household's single public one and rewrites the addresses in every packet going out and coming back (**NAT**). This is also why a device with a private address cannot be reached directly from outside, which is a security feature as much as an inconvenience. **Subnetting** splits one network into smaller ones by reserving the leading bits of the address for the sub-network: `192.168.1.0/24` is 256 addresses; four `/26` subnets of 64 each keep a school's staff, students, printers and servers apart, reduce broadcast traffic and collisions, contain faults, and make the whole easier to manage.

**The router.** Three roles the boards list: it **forwards packets** toward their destination by reading the destination IP address and choosing the next hop; a home router commonly **assigns IP addresses through a DHCP service** to devices on its own network; and it **connects the LAN to the internet**, holding the public address on one side and the private ones on the other. The other LAN hardware 9618 names: a **switch** (delivers frames to the right MAC address within the LAN), a **wireless access point** (the LAN's radio), a **bridge** (joins two LAN segments), a **repeater** (regenerates a fading signal), and the cables themselves. On the internet side: **modems** (which turn digital data into a form a telephone line, cable or fibre can carry), the **PSTN**, **dedicated leased lines**, and the **cell-phone network**.

---

## Part V — The shapes of a network

**LAN and WAN.** A **local area network** covers one site — a house, a school, an office — with hardware the owner controls; a **wide area network** joins sites across a city or the world, usually over infrastructure leased from a telecoms company. The internet is the largest WAN.

### Topologies

![[internet-topologies.svg|960]]

*Bus, star, mesh and hybrid, with the path of one packet from A to D. The 9618 question gives a scenario and asks for the topology, a drawing of it, the packet's route, and a justification.*

- **Bus:** one shared cable with terminators at the ends. Cheap and simple, but every transmission is broadcast to every node, only one can transmit at a time, a cable fault stops everything, and it scales badly. On a bus, **Ethernet** uses **CSMA/CD** — *carrier sense multiple access with collision detection*: a node listens until the line is free, sends, and if two send at once and their signals collide, both stop, wait a random time, and try again.
- **Star:** every node connected to a central **switch**. A failed cable isolates one node only; traffic goes only where it is addressed, so no collisions and better privacy; adding a node is one more cable — but the switch is a single point of failure and the cabling costs more.
- **Mesh:** every node connected to every other (full mesh) or to several (partial). Multiple routes, so any link can fail without loss and traffic can be spread — at the price of $n(n-1)/2$ cables for $n$ nodes. The internet's backbone and wireless home systems are partial meshes.
- **Hybrid:** any combination; almost every real LAN is one, typically stars joined by a backbone.

### Client-server and peer-to-peer

In the **client-server** model some machines are **servers** that hold the data and do the processing, and the rest are **clients** that send requests and display responses: a bank's app, an online game with a virtual world, a school's file server. It centralises control, backup and security, and it scales by adding servers — but the server is a bottleneck and a single point of failure, and it costs money to run. In the **peer-to-peer** model every machine is both client and server, sharing files or processing directly: BitTorrent, some games, blockchains. No central cost or failure point, easy to set up, but no central control over what is shared, and performance depends on the peers.

A **thin client** does little itself — it needs the server for processing and storage (a browser-based app, a school terminal, a cloud-gaming stream) — so it is cheap, easy to manage centrally and useless offline. A **thick client** has its own storage and processing (a laptop running installed software), works without the network, and demands more of each machine.

### The cloud, the media, and streaming

**Cloud computing** is the client-server model rented by the hour: storage and processing on someone else's servers, reached over the internet. A **public cloud** is shared infrastructure (the big providers); a **private cloud** is the same idea run for one organisation on its own hardware. Benefits: no hardware to buy or maintain, capacity on demand, access from anywhere, automatic backup; drawbacks: dependence on the connection and the provider, ongoing cost, and data held by a third party under its jurisdiction. The IB syllabus adds the service tiers — infrastructure, platform and software as a service — which are the same rental at three levels.

**Wired or wireless.** Copper cable is cheap and short-range and picks up interference; fibre carries far more, farther, immune to interference, but costs more to install; radio (Wi-Fi) is convenient and mobile but slower, shared, and open to anyone in range; microwave links need line of sight; satellites reach anywhere and add a delay of hundreds of milliseconds ([[Networks]] Part V).

**Bit streaming** is sending a media file as a continuous stream that plays as it arrives, rather than downloading it whole first; a **buffer** in the player absorbs the jitter. **On-demand** streaming plays a file already stored on a server — it can be paused, rewound and re-watched, and the player can read ahead. **Real-time** (live) streaming sends an event as it happens — nothing exists to read ahead into, it cannot be rewound at the source, and a slow connection means dropped frames rather than a longer wait. Both need a **bit rate** — the bits per second the connection can sustain — at least equal to the stream's, which is why a 4K video stalls on a 5 Mbit/s link and plays on a 50 Mbit/s one.

---

## Part VI — Where this is the working tool

- **The four addresses for one name.** The DNS answer above is a **content delivery network** at work: the same page served from machines near you, chosen by DNS, with a short TTL so a failed machine drops out of the list within a minute. Every large site — video, shopping, games — is delivered this way, and it is the reason the script gets different answers from different cities.
- **The padlock everywhere.** In 2013 most of the web was HTTP; by 2020 over 90 % of pages loaded in Chrome were HTTPS, driven by free certificates (Let's Encrypt, 2015) and browsers marking plain HTTP "not secure". The exam's HTTP-versus-HTTPS contrast describes a change that happened within the lifetime of the students taking it.
- **NAT is why your IP address is not yours.** A household shares one public IPv4 address; a mobile network shares one among thousands (carrier-grade NAT). This is what made IPv4 last a decade past exhaustion, and why hosting a game server at home needs "port forwarding" on the router.
- **The cookie economy.** The consent banner on every site is the law (the EU's GDPR, China's PIPL) catching up with the persistent cookie: the same mechanism that keeps you logged in is the one that lets an advertising network follow you across every site that carries its adverts.
- **China's IPv6.** A national plan in 2017 set a target of 500 million active IPv6 users by 2020; by 2024 the count was over 800 million and the majority of mobile traffic ran on IPv6 — the largest deployment anywhere. The 128-bit address in the figure is what the phone in your pocket is using.

---

## Worked examples — Paper 1 questions from both boards, every mark named

### Cambridge 0478 June 2025 Paper 13 Q5 — DNS, cookies, the browser [2 + 1 + 3 + 2]

*(a) The user types a URL, which is sent to a DNS. Describe the role of the DNS.* **Tool: the DNS chain in scheme language** — any two of: *stores a database of URLs and matching IP addresses; searches it for the match; sends the URL to another DNS if not found; returns the IP address to the browser* [2]. *(d)(i) Items stay in the cart after the browser is closed — which cookie?* **Trigger: survives the browser closing → persistent** [B1]. *(ii) Three other uses of cookies:* login details, payment details, preferences, targeted advertising [3]. *(iii) Two other functions of a web browser:* bookmarks, history, multiple tabs, rendering HTML, navigation [2].

### Cambridge 0478 November 2025 Paper 12 Q6 — the URL, the table, the cookie statements [3 + 5 + 4]

*(a) Name parts a, b, c of `https://www.cieclothes.com/index.html`.* **Tool: the URL anatomy** — protocol, domain name, web-page (file) name [3]. *(c) Complete the table.* HTML: *the language used to write web pages*; DNS: *stores domain names and their matching IP addresses / provides the IP address for a web page to the browser*; the description "numerical address used to locate the web server" is the **IP address**; "secure protocol to transmit data to and from a web server" is **HTTPS (SSL/TLS)** [5]. *(d) Cookies are stored and managed by the… created when a user visits a web page.* **web browser**; the cookie that dies when the browser closes is the **session** cookie; the one that stays is **persistent** [4]. The distractor words (asymmetric, symmetric, static, dynamic, utility software) belong to other topics — read the definition, not the list.

### Cambridge 0478 March 2026 Paper 12 Q2 — from URL to IP address [3 + 1 + 3 + 1 + 2]

*(b)(i) Purpose of an IP address:* **to uniquely identify a device on a network** [1]. *(ii) Explain how a URL is converted to an IP address.* **Tool: the chain, in order** — the browser sends the domain name to the DNS; the DNS holds a table of domain names against IP addresses and searches it; if not found, the request goes to a higher-level DNS until it is; the IP address is returned to the browser [3]. *(c)(i) A cookie is* **a text file storing data about the user or their browsing, kept on the computer by the browser** [1]; *(ii) one session use and one persistent use, different:* basket contents during a visit; staying logged in across visits [2]. Writing "stores the shopping basket" for both scores one — the scheme wants the lifetimes to differ.

### Cambridge 0478 November 2025 Paper 11 — IPv6 and the MAC address [3 + 1]

*(c) Three characteristics of the IPv6 format:* **128 bits; hexadecimal; eight groups separated by colons; each group four digits; consecutive zero groups written as `::` once** [3]. *(d) A MAC address is assigned by* **the manufacturer** [B1] — the question is about the factory-assigned address. Locally administered addresses are the qualification explained above.

### Cambridge 9618 June 2026 Paper 11 Q7 — a bus with Ethernet, a static private IP, subnetting [4 + 2 + 1 + 3]

*(b)(i) Explain how data is transmitted between two nodes in a bus topology using Ethernet.* **Tool: bus = broadcast; Ethernet = frames + CSMA/CD** — both nodes are on the one cable; data is broadcast on it and accepted only by the addressed node; Ethernet sends **frames** carrying the two MAC addresses; it uses **CSMA/CD**: the sender listens and sends only when the line is free, and on a collision waits a random time and retries [4]. *(ii) Two drawbacks of a bus:* only one transmission at a time, so inefficient with many nodes; a cable fault takes the network down; broadcasting to all nodes is a confidentiality risk; hard to scale [2]. *(c)(i) A static private IP address:* **does not change, and is visible only within the LAN** — both halves for the mark [1]. *(ii) Three benefits of subnetting:* splits the network into manageable parts; less congestion and fewer collisions; better security and fault isolation; easier to scale [3].

### Cambridge 9618 June 2024 Paper 11 — client-server roles, the topology table, IPv6 [4 + 5 + 1 + 2]

*Q5(a) A bank's app: describe the roles of the devices in the client-server model.* **Tool: name the server and the client in the scenario, then their jobs** — the bank's server receives and processes requests and holds the accounts; the customer's phone is the client, which sends requests, waits, and displays the response [4]. *Q8(a) Tick the topology each statement describes:* all devices to one central device → star; all to a central cable → bus; multiple paths for packets → mesh; robust if any line fails → mesh; most likely to lose data through collisions → bus [5]. *(b)(i) Why does the router have a public IP address?* **So it can be reached from, and route to, the internet** [1]. *(ii) Two more differences between IPv4 and IPv6 beyond dots and colons:* 4 groups against 8; denary against hexadecimal; 0–255 against 0–FFFF per group; 32 bits against 128 [2].

### Cambridge 9618 June 2025 Paper 12 — the address description, and a star to draw [6 + 4]

*(c) Fill the description.* IPv4: four groups of 8-bit numbers separated by **full stops**; IPv6: eight groups of 4 **hexadecimal** numbers; consecutive groups of **zeros** collapse to `::`; each IPv6 address is **128** bits; a **dynamic** address can change on each connection; a **private** address is reachable only within the LAN and assigned by its router [6]. *(d) Draw the star for four computers, a server, two printers, a central switch and the internet access device.* **Tool: everything to the switch, once** — eight labelled devices each on its own line to the switch, the router (or modem) among them as the point of internet access; nothing connected to anything but the switch [4].

### Cambridge 9618 June 2024 Paper 11 Q(e) — bit streaming [1 + 2]

*(i) Bit streaming is* **sending a continuous stream of data (bits) that is played as it arrives, without waiting for the whole file** [1]. *(ii) Two differences between real-time and on-demand:* real-time comes direct from the source as it happens, on-demand from a file recorded earlier; on-demand can be paused, rewound and re-watched, real-time cannot; on-demand can be read ahead in blocks, real-time plays continuously [2].

---

## Misconceptions

- **"The internet and the web are the same thing."** The internet is the network (1969); the web is one service on it (1990). Email, games and video calls are internet, not web. Both boards ask for this distinction directly.
- **"DNS is a server."** It is a hierarchy of servers with caches at every level; the one your machine talks to usually does not know the answer and asks upward. Write "higher-level DNS" and the mark is there.
- **"The IP address identifies the person, or the computer permanently."** It identifies a device *on a network, for now*. Most devices have private, dynamic addresses; a household shares one public address through NAT; the MAC address is used for delivery on the local link, but can be locally administered or randomised. Routers do not preserve the original Ethernet header across links.
- **"A cookie is a program, or a virus."** It is a text file, written by the browser at the server's request, that cannot execute anything. Its risk is tracking, not infection.
- **"HTTPS means the site is safe."** It means the connection is encrypted and the server is who its certificate says. A fraudulent site can have a perfect certificate for its own fraudulent name. Check the domain name, not the padlock.
- **"A MAC address is assigned by the router."** The factory MAC address is manufacturer-assigned; private Wi-Fi addresses are a separate software-controlled case. A home router commonly supplies IP addresses through its DHCP service.
- **"Mesh means wireless."** Mesh is a topology — every node to several others — and can be cabled; the home "mesh Wi-Fi" is a partial mesh of access points.

---

## Hands-on

- **Do a DNS lookup by hand.** `python3 internet-dns-by-hand.py www.bilibili.com` builds the query packet byte by byte, sends it over UDP to a public resolver, and decodes the answer: the addresses and their TTL. Run it from two networks and compare the addresses; wait longer than the TTL and run it again.
- **Read a certificate and a cookie.** `python3 internet-url-and-cookies.py` splits a URL into its parts, makes a TLS connection and prints who signed the server's certificate and when it expires, then fetches a front page and sorts the cookies it sets into session and persistent.
- **Count addresses and cut a subnet.** `python3 internet-addresses.py` counts the IPv4 and IPv6 spaces, marks which addresses are private, and splits a `/24` into four `/26` subnets with their host ranges.
- **Look at your own three addresses.** On a Mac, `ifconfig en0` shows the MAC (`ether`) and the private IPv4 (`inet`) and IPv6 (`inet6`) addresses; any "what is my IP" page shows the public address the router presents. They are different numbers, and now you know why.

---

## Exam Notes

### Cambridge 0478 — §3.4 and §5.1 (Paper 1)

- **§3.4 Network hardware:** the NIC as the way onto a network; the MAC address — purpose and structure (manufacturer code + serial number, hexadecimal, set at manufacture); IP addresses — purpose, static vs dynamic, IPv4 vs IPv6 characteristics and differences; the router's three roles. Short-answer and tick-box questions; the IPv6 "three characteristics" and the IPv4/IPv6 "two differences" are set almost every year.
- **§5.1 The internet and the WWW:** the internet-vs-web difference; ISPs; the three parts of a URL; HTTP vs HTTPS; the functions of a web browser; the full **URL → DNS → IP → web server → HTML → browser** sequence (the five-mark describe question, June 2025 Q5, March 2026 Q2); cookies, session vs persistent, and their uses. The §5.3 security items that share these questions (proxy servers, DDoS, two-step verification) live in [[Data Security]].

### Cambridge 9618 — §2.1 Networks including the internet (AS, Paper 1)

- Everything in Part IV and Part V: LAN vs WAN; client-server vs peer-to-peer with justification for a scenario; thin vs thick clients; bus, star, mesh, hybrid — how packets travel in each, and which to choose; cloud, public and private; wired vs wireless media; LAN hardware (switch, server, NIC, WNIC, WAP, cables, bridge, repeater) and the router; **Ethernet with CSMA/CD**; bit streaming, real-time vs on-demand, the importance of bit rate; the WWW vs the internet; internet hardware (modems, PSTN, dedicated lines, cell network); IP addresses — IPv4/IPv6 format, subnetting, how an address is associated with a device, public vs private and the security implication, static vs dynamic; URLs and the role of DNS.
- The descriptions are marked in bullet points: name the thing, say what it does, and where a scenario is given, refer to it ("the bank's server…"). A drawing question wants every device labelled and every connection correct.

### IB Computer Science — A2.1, A2.2

- A2.1 (network fundamentals) and A2.2 (architecture, including cloud) are the same content as 9618 §2.1 with the cloud tiers named — IaaS, PaaS, SaaS — and the layered model from [[Networks]].

### Not examined on…

- **AP Computer Science A** — no networking content at all; the course is Java and object-oriented design.
- **Cambridge 0625 / 9702** — none; the physics boards examine the transmission hardware only as electromagnetic waves and optical fibre.

---

## Quick reference

| Term | One line |
|---|---|
| Internet | network of networks, TCP/IP, 1969; carries every service |
| World Wide Web | HTML pages, URLs, HTTP(S), browsers, 1990; one service on the internet |
| URL | protocol :// domain name / file path (+ query, fragment) |
| DNS | hierarchy of servers mapping names to IP addresses; caches with a TTL; asks upward if unknown |
| HTTP / HTTPS | request–response for pages; HTTPS = HTTP inside TLS: encrypted, server authenticated |
| Cookie | text file stored by the browser at the server's request; session dies with the browser, persistent has an expiry |
| MAC address | 48 bits hex, manufacturer + serial, set at manufacture, used on the local link |
| IPv4 / IPv6 | 32 bits, four denary 0–255 with dots / 128 bits, eight hex groups with colons, `::` once |
| Static / dynamic · public / private | fixed vs lent by DHCP · globally routable vs LAN-only (NAT at the router) |
| Router | forwards by destination IP; assigns addresses; joins LAN to internet |
| Topologies | bus (shared cable, CSMA/CD), star (switch), mesh (many paths), hybrid |
| Client-server / P2P | central servers and requesting clients / every node both |
| Thin / thick client | needs the server for processing and storage / does its own |
| Bit streaming | play as it arrives; on-demand (stored, seekable) vs real-time (live, not seekable); needs bit rate ≥ stream rate |

---

## Connections

- **Prerequisites:** [[Networks]] — the stack, packets and routing this card sits on: DNS rides UDP, HTTP rides TCP, the MAC address is the link layer's and the IP address the internet layer's; [[Encryption]] — what HTTPS actually does: certificates, the handshake, the session key.
- **Leads to:** [[Data Security]] — cookies and tracking, DDoS and the proxy server, phishing by look-alike domain; [[Digital Currency and Blockchain]] — the peer-to-peer model with money on it.
- **Related:** [[Error Detection and Correction]] — the frame check the Ethernet frame carries; [[Operating Systems]] — the network stack is the OS's; [[Number Bases]] — why MAC and IPv6 addresses are written in hexadecimal.

## Sources

- Cambridge IGCSE Computer Science 0478 syllabus 2026–28, §3.4, §5.1; Cambridge International AS & A Level Computer Science 9618 syllabus 2027–29, §2.1; IB Computer Science guide (first assessment 2027), A2.
- Cambridge 0478 June 2025 Paper 13 Q5, November 2025 Paper 12 Q6, November 2025 Paper 11 Q2, March 2026 Paper 12 Q2; 9618 June 2024 Paper 11 Q5 and Q8, June 2025 Paper 12 Q(c)–(d), June 2026 Paper 11 Q7 — with their published mark schemes.
- The scripts beside this card: `internet-dns-by-hand.py` (RFC 1035 message format), `internet-url-and-cookies.py`, `internet-addresses.py`; the Manim source `internet-url-to-page.py`.
- Tim Berners-Lee, *Information Management: A Proposal* (CERN, March 1989); the first website, info.cern.ch (1991). RFC 1034/1035 (DNS, 1987); RFC 6265 (HTTP cookies, 2011); RFC 1918 (private address space, 1996); RFC 8200 (IPv6, 2017).
- Google Transparency Report, HTTPS encryption on the web (share of page loads over HTTPS in Chrome). China Academy of Information and Communications Technology, IPv6 deployment reports (2023–24).
