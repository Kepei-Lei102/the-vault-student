---
chinese: 计算机网络 (jìsuànjī wǎngluò) — 协议栈、分组交换与数据传输方式
prerequisites:
  - "[[Error Detection and Correction]]"
  - "[[Encryption]]"
  - "[[Operating Systems]]"
leads_to:
  - "[[The Internet and the Web]]"
  - "[[NoSQL and Distributed Data]]"
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
  - syllabus/0478-2-1
  - syllabus/9618-14-1
  - syllabus/9618-14-2
  - syllabus/IB-CS-A2-1
  - syllabus/IB-CS-A2-2
  - syllabus/IB-CS-A2-3
  - type/deep
  - misconception/bandwidth-is-speed
  - misconception/the-router-knows-the-whole-path
  - misconception/full-duplex-doubles-the-bandwidth
---

# Networks 计算机网络

> *No wire on Earth runs from your phone to the server. What runs is a chain of strangers, each holding a piece of your message for a few microseconds and handing it to the next, none of them knowing the whole route, all of them obeying the same rules. The rules are the network. This card is about the rules, the pieces, and the one number in the corner of the screen that tells you how the chain is doing.*

## Definition

### Formal

A **network** is two or more computers connected so that they can exchange data. A **protocol** is an agreed set of rules for that exchange — the format of the data, the order of the messages, what to do on error — without which two machines from different makers cannot communicate at all. Protocols are organised as a **stack** of layers, each with one job and an interface only to the layer above and below; the internet's stack is the **TCP/IP suite**: Application, Transport, Internet, Link.

Data is sent in **packets**: a slice of the message (the **payload**) wrapped in a **header** (destination address, originator's address, packet number) and a **trailer** (an error check). In **packet switching** each packet is forwarded independently by **routers**, may take a different route, may arrive out of order, and is reassembled by number at the destination; in **circuit switching** a dedicated path is set up first and held for the whole conversation.

At the wire, data travels **serial** (one bit at a time on one wire) or **parallel** (several bits at once on several), and a link is **simplex** (one way), **half-duplex** (both ways, one at a time) or **full-duplex** (both ways at once).

### Intuitive

A network is a postal system for a city with no maps. You cannot send a book, so you tear it into numbered pages and put each in an envelope with the address, your address and the page number. Each sorting office looks only at the address and hands the envelope to whichever neighbouring office is nearest and least busy right now; pages take different roads and arrive in any order; the recipient sorts them by number and writes back for any that are missing. The envelope's format, the numbering, the "write back for missing pages" rule — those are the protocol. The sorting offices are routers. The book never existed on any one road.

### 中文锚点

打《英雄联盟》或《无畏契约》时，屏幕角落有个数字：**ping，比如 45 ms 或 200 ms**。它是什么？是一个小数据包从你的电脑到游戏服务器**再回来**所用的时间——往返时间。它和你家"百兆宽带"没有关系：**带宽**是管子有多粗（一秒能过多少比特），**延迟**是管子有多长（一个比特要走多久）；管子再粗，成都到上海的光纤也得走几毫秒，到美国要走一百多毫秒，光速说了算。所以百兆宽带照样会"卡"，卡的是延迟和**抖动**（延迟忽大忽小），不是带宽。你按下技能键，这条消息是怎么过去的？它被切成一个个**数据包**——每个包带着**目的地址、源地址、包编号**（头部）、一小段数据（**载荷**）和一个校验（尾部）——交给你家路由器；路由器只看目的地址，把包转给它此刻认为最好的下一跳，再下一跳的路由器再决定下一步，**没有人知道全程**。各个包可能走不同的路、乱序到达，服务器按编号重排；坏了或丢了的包，请对方再发一次。这就是**分组交换**，整个互联网都这么工作，和老式电话的**电路交换**（先接通一条专线，通话期间独占）刚好相反。管这一切的规则叫**协议**，而协议是**分层**的：应用层（HTTP 网页、SMTP 发邮件、IMAP 收邮件、BitTorrent 下载）、传输层（TCP 保证送到且有序，UDP 快但不保证——游戏和视频通话用 UDP，因为迟到的一帧不如不要）、网际层（IP，地址和路由）、链路层（以太网、Wi-Fi、5G，一跳）。这张卡把这条链**真的摸了一遍**：用 Python 在本机跑一次 TCP 和 UDP 通信，手写一个 HTTP 请求看服务器回什么，从成都 ping 谷歌四十次画出延迟的分布，traceroute 数出中间的路由器。最后是 0478 要考的"线上的事"：**串行还是并行**（一根线还是八根线）、**单工 / 半双工 / 全双工**（单向、轮流、同时），以及 **USB** 为什么统一了所有接口。

| English | 中文 | 一句话 |
|---|---|---|
| Protocol | 协议 | 双方约定的通信规则；没有它，不同厂商的机器无法对话 |
| Protocol stack / TCP/IP | 协议栈 / TCP/IP 协议族 | 四层：应用、传输、网际、链路，各干一件事 |
| Packet: header · payload · trailer | 数据包：头部 · 载荷 · 尾部 | 地址和编号 · 数据本身 · 校验 |
| Packet switching · router | 分组交换 · 路由器 | 每个包独立转发；路由器只看目的地址决定下一跳 |
| Circuit switching | 电路交换 | 先建专线，通话期间独占，结束再拆 |
| Latency / round-trip time (ping) | 延迟 / 往返时间 | 管子有多长；游戏里那个 ms 数 |
| Bandwidth | 带宽 | 管子有多粗；每秒多少比特 |
| TCP / UDP | 传输控制协议 / 用户数据报协议 | 可靠有序 / 快而不保证 |
| Serial / parallel | 串行 / 并行 | 一根线逐位 / 多根线同时 |
| Simplex / half-duplex / full-duplex | 单工 / 半双工 / 全双工 | 单向 / 轮流双向 / 同时双向 |
| USB | 通用串行总线 | 串行、统一、可供电、热插拔 |

---

## Part I — Protocols, and why they come in layers

### Why a protocol at all

Two computers from different makers, running different software, on different continents, must agree on everything before a single byte means anything: which wire is which, how a bit is signalled, how long a message is, where the address goes, what "received" looks like, what to do when a piece is missing. A **protocol** is that agreement written down. Without one, the machines are not disagreeing; they are not communicating at all — the 9618 scheme's phrase is that protocols *set a standard for communication* and *enable compatibility between devices from different manufacturers*. Every network standard you have heard of — Ethernet, Wi-Fi, IP, TCP, HTTP — is a protocol, and the internet is the set of machines that agreed to the same ones.

### The stack

Nobody writes one protocol that does everything, for the same reason nobody writes one program that does everything ([[Decouple and Recouple]]). The job is cut into **layers**, each with a single responsibility, each talking only to the layer directly above and below it through a fixed interface. The internet's stack has four:

![[networks-tcpip-stack.svg|960]]

| Layer | Its one job | Protocols that live there |
|---|---|---|
| **Application** | what the message *means* to the programs at each end — a web page, an email, a file | HTTP (web pages), FTP (file transfer), SMTP (sending mail), POP3 and IMAP (collecting mail), BitTorrent (peer-to-peer sharing) |
| **Transport** | getting the message from *this program* to *that program*, complete and in order — or fast and best-effort | **TCP**: numbers the pieces, acknowledges them, re-sends losses, controls the flow. **UDP**: sends and forgets |
| **Internet** | getting each packet from *this machine* to *that machine* across many networks — addressing and routing | **IP**: the address on every packet, and the hop-by-hop forwarding decision |
| **Link** | moving a frame across *one* physical hop — a cable, a radio channel | Ethernet, Wi-Fi, 4G/5G; the MAC address and the frame check |

Going down the stack on the sending machine, each layer **wraps** what it is given in its own header: the transport layer adds ports and sequence numbers, the internet layer adds the two IP addresses, the link layer adds the two hardware addresses and a checksum. The script beside this card counts it: a 100-byte message leaves the wire as a 158-byte frame, so 37 % of what is transmitted is addressing and checking. Going up on the receiving machine, each layer strips the header meant for it and passes the rest up. **The two ends converse layer to layer** — the application layers exchange a web page, the transport layers exchange acknowledgements — while everything in between, every router on the route, opens only the Internet and Link headers, reads the destination address, and forwards. A router never sees the TCP header, never sees the page.

That is what the November 2024 question means by *how the layers interact*: each layer accepts input only from its neighbours; the only interaction is through the interface between adjacent layers; headers are added on the way down; the user touches the top layer and the hardware the bottom. It is also why the internet has survived fifty years of technology change underneath it: you can replace every cable and every router with something faster and the web page above never notices, because the layer boundaries are contracts.

### TCP or UDP — the only choice the application makes

Two transport protocols, two philosophies. **TCP** promises that every byte arrives, once, in order: it numbers segments, the receiver acknowledges, the sender re-transmits anything unacknowledged, and it slows down when the network is congested. That costs a handshake before the first byte and a stall whenever one piece is late, because the pieces behind it must wait. Web pages, email, file downloads and anything that would be wrong with a byte missing use TCP. **UDP** promises nothing: a datagram is sent and forgotten. Video calls and games use UDP, because a frame that arrives late is *worse* than one that never arrives — the moment has passed — so there is no point waiting for a re-send. The script runs both on your own machine:

```
== (1) TCP on the loopback: reliable, ordered, connection first ==
  server: got b'hello, network' from ('127.0.0.1', 59792)
  client: reply b'ACK: HELLO, NETWORK'
== (2) UDP: fire and forget ==
  datagram b'frame 1' — no connection was made, no acknowledgement will be sent
```

And it writes an HTTP request by hand, so the top layer is not a mystery either:

```
GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n
  first byte after 229 ms; 868 bytes back:   HTTP/1.1 200 OK   Content-Type: text/html   Server: cloudflare
```

Three lines of text, a blank line, and a web server on another continent answers. Every browser tab you have ever opened began with those three lines.

> [!tip] The named protocols the exam wants, in one line each
> **HTTP** carries web pages between browser and server (HTTPS is the same inside [[Encryption]]'s TLS). **FTP** transfers whole files to and from a server. **SMTP** *sends* email from your client to a mail server and between servers. **POP3** *collects* email by downloading it to one device and usually deleting it from the server; **IMAP** collects it by keeping it on the server and synchronising every device — which is why your phone and laptop show the same inbox. **BitTorrent** is peer-to-peer: a file is cut into pieces and every downloader also uploads the pieces it has, so a popular file gets *faster* to fetch as more people want it — the opposite of a single server, which gets slower.

---

## Part II — Packets, and packet switching

### The packet

![[networks-packet.svg|900]]

A message too big to send whole — and on the internet anything over about **1 500 bytes** is — is cut into packets. Each carries a **header** with the destination address, the originator's address and the packet's number in the sequence; a **payload**, the slice of data; and a **trailer** with an error check ([[Error Detection and Correction]]'s checksum or CRC) so that the receiver can tell a damaged packet from a good one. The addresses are for the routers; the number is for the receiver; the check is for both.

### Packet switching

![[networks-packet-switching.mp4]]

*The clip: a thirteen-character message becomes six numbered packets; each router forwards each one along whichever link is best right now, so they take different routes and arrive as 2, 1, 5, 3, 6, 4; one is damaged, fails its check, and is requested again; the receiver reassembles by number.*

The process, in the order the 0478 and 9618 schemes want it:

1. The data is **broken into packets** of (roughly) equal size, each with a header carrying the sender's and receiver's addresses and a sequence number.
2. Each packet is **sent independently**. A **router** reads the destination address, consults its table of where that address is reachable, and forwards the packet to the best next hop *available at that moment* — the least congested, or the shortest, or the only one still working. It does not know the whole route and does not need to.
3. Because "best right now" changes from packet to packet, packets of one message **take different routes** and may **arrive out of order**, or not at all.
4. The receiver checks each packet's trailer, **requests a re-send** of any that are damaged or missing, and once the last has arrived **reorders them by number** and reassembles the message.

Two consequences make this the design the whole internet runs on. **Efficiency:** the links are shared — while your packet waits, someone else's is on the wire — so no capacity sits idle the way a reserved circuit does. **Resilience:** a dead router or cut cable is simply routed around, packet by packet, with no set-up and no one in charge. That second property was the point: Paul Baran designed packet switching in the early 1960s for a communications network that would survive the loss of any of its parts, and the ARPANET switched its first packets in 1969. Vint Cerf and Bob Kahn published TCP in 1974; the ARPANET moved to TCP/IP on 1 January 1983; and the address in your packet's header today is still the one they defined.

### Watch it happen from Chengdu

Two real measurements, made while this card was written. `traceroute` sends packets with deliberately short lifetimes so that each router on the way reveals itself as it discards them:

```
traceroute to www.cam.ac.uk (23.185.0.2), 16 hops max
 1  198.18.192.1     310 ms        ← the first router: the home gateway
 2  103.136.184.1    211 ms
 3  209.177.154.224  189 ms
 4  66.208.232.1     191 ms
 5  96.110.32.250    184 ms        ← after this, routers that do not answer
```

Five machines showed themselves, each a stranger holding the packet for a moment; the rest of the chain is there but silent, because many routers are configured not to reply. And `ping` — forty small packets, one every quarter second, each one timed there and back to Google's public DNS server:

![[networks-ping.svg|960]]

*Median 210 ms, but no two the same: 188 ms at best, 315 ms at worst, a standard deviation of 32 ms. This spread is **jitter**, and it is what a video call or a game feels as stutter — not the average delay, which the brain adjusts to, but its unpredictability.*

---

## Part III — Circuit switching, and when it is still the right answer

![[networks-switching.svg|960]]

Before packets there was the telephone. To make a call, the exchanges **set up a dedicated path** from your handset to the other, end to end, before you said a word; the path was **held for the whole call** and carried your voice as a continuous stream in order and at a fixed rate; when you hung up it was **torn down** and its wires freed. That is **circuit switching**, and it has real merits, which is why the exam asks for both sides:

| | Circuit switching | Packet switching |
|---|---|---|
| Before sending | a path is set up end to end — takes time | nothing; the first packet just goes |
| During | the whole path's bandwidth is yours; fixed rate; data arrives in order; no waiting at switches; nothing lost | links shared with everyone; variable delay and jitter; packets reordered and occasionally lost, then re-sent |
| The path | fixed; if it breaks the call ends and must be re-established | none; each packet routed independently, so failures are routed around |
| Efficiency | poor — the circuit is reserved even in silence, and no one else may use it | high — capacity is used whenever anyone has something to send |
| Security | poor — all the data takes one predictable route | poor in a different way — pieces on many routes, but any one of them readable |
| Best for | long, continuous, real-time streams where a guaranteed rate matters: a live voice call, a private data link | almost everything else: web, email, file transfer, and — with UDP and a little buffering — voice and video too |

The June 2023 scheme's answer to *where circuit switching is appropriate* is exactly the left column: where a dedicated path must be sustained for the whole communication, where the whole bandwidth is required, where the communication is real-time — traditional voice calls, video streams, private networks. The honest modern footnote is that even voice now mostly travels as packets (every phone call over 4G or Wi-Fi is UDP with buffering), because packet switching's efficiency won; circuit switching survives in leased private lines and as the idea the exam contrasts against.

---

## Part IV — At the wire: serial, parallel, duplex, USB

The layers above describe *what* is sent. The IGCSE also asks *how the bits physically move* between two devices, and the vocabulary is two independent choices.

![[networks-serial-parallel-duplex.svg|960]]

**How many wires.** **Serial** transmission sends one bit after another down a single wire (or pair). It is cheap, it works over long distances, and the bits cannot get out of step with each other because there is only one stream — the scheme's "no skew, fewer errors". **Parallel** transmission sends several bits at once on several wires, a byte at a time on eight; it is faster per clock tick but only over centimetres, because over any distance the bits on different wires arrive at slightly different times (**skew**) and the wires interfere with each other (**crosstalk**). Parallel lives inside the computer, on the buses of [[CPU Architecture and the Fetch-Execute Cycle]]; everything that leaves the case — Ethernet, USB, HDMI, the fibre to your building — is serial, and modern serial links are so fast that the old parallel printer and disk cables are gone.

**Which directions.** **Simplex** is one way only, ever: a keyboard to its computer, a sensor to its controller, a broadcast. **Half-duplex** is both ways but one at a time, like a walkie-talkie or an old Wi-Fi channel — cheaper, and enough when the two ends take turns. **Full-duplex** is both ways at the same time: a phone call, a video call, every wired Ethernet link. The exam pairs one word from each choice and asks for the reason in the scenario — a kitchen order system thirty metres away that must send confirmations back wants *serial full-duplex*: serial for the distance and reliability, full-duplex because data flows both ways.

**USB**, the Universal Serial Bus, is the case study: a **serial** connection (one differential pair, so no skew), **universal** (one connector for keyboards, mice, cameras, storage and phones, replacing a decade of different ports), **hot-pluggable** (the operating system detects the device and loads its driver — [[Operating Systems]]' plug-and-play), able to **power** the device down the same cable, **backward compatible** across versions, and impossible to insert wrongly (at last, with USB-C). Its drawbacks are the ones the scheme lists: cable length is limited to a few metres, and its speed, though high, is below a dedicated link such as Thunderbolt or Ethernet for the heaviest loads. USB 2 was half-duplex; USB 3 added a second pair and became full-duplex — the two choices above, changed independently.

**The medium** (for IB's transmission-media row): copper cable (Ethernet, cheap, up to about 100 m per run), optical fibre (light in glass, kilometres without a repeater, immune to electrical interference, the whole long-distance internet), and wireless (Wi-Fi and cellular radio, shared and half-duplex by nature, convenient and the most lossy). A **LAN** is a network on one site, owned by whoever owns the site; a **WAN** joins LANs across cities and countries over links you rent; the internet is the WAN of WANs. In a **client–server** design one machine serves many (the web); in **peer-to-peer** every machine is both (BitTorrent); the **cloud** is client–server where the servers belong to someone else and are rented by the hour.

---

## Part V — Where this is the working tool: why the game lags

The one network quantity every student already watches is the **ping** in the corner of a game. It is the round-trip time of a small packet, and the physics of Part II says what it is made of: propagation (light in fibre covers about 200 km per millisecond, so Chengdu to Shanghai is 10 ms there and back at best, Chengdu to a US server over 150 ms — [[The True IO Bound]] puts that on its ladder), plus queueing at every router on the way, which is the part that varies. Three lessons the card's own measurements teach:

- **Bandwidth is not latency.** A 100 Mbit/s line and a 1 Gbit/s line have the same round-trip time to the same server; the wider pipe moves a file faster but does not move a single packet sooner. Upgrading the plan does not fix lag. Moving closer to the server, or the server to you — which is what a content-delivery network does — does.
- **Jitter is the enemy, not delay.** A steady 200 ms is playable, because the game predicts and the brain adjusts; a ping that swings from 188 to 315 ms, as in the measurement above, is what causes rubber-banding, because packets arrive in bursts and gaps. Wi-Fi's shared half-duplex channel is the commonest source of jitter in a home; a cable is the fix.
- **Games use UDP on purpose.** Under TCP a lost packet stalls everything behind it until the re-send arrives — a "head-of-line" freeze of a full round trip. A game would rather drop the frame and show the next one. Video calls make the same choice, and add a small buffer to smooth the jitter, which is why they have a fixed, slight delay.

Two more places the same machinery is the tool. When a messaging app shows *sent* and then *delivered*, the second tick is an application-layer acknowledgement riding on TCP's own acknowledgements: the packet-switched chain reported back. And when a large game update arrives quickly on launch day, it is often BitTorrent-style peer-to-peer distribution: every player who has a piece serves it, so the crowd that would crush one server instead becomes the network that delivers to itself.

---

## Worked examples — real Paper 3 and Paper 1 questions, every mark point named

### Cambridge 9618 June 2025 Paper 31 Q3 — the two upper layers, and packet switching [5 + 4]

*(a) Describe the purpose of the Application Layer and the purpose of the Transport Layer.* Up to three for each. Application: provides services and the **interface to the user's programs** — login, file transfer, email; **defines the protocols** the exchange uses; can provide security (encryption, authentication) and application-level error handling. Transport: provides **logical communication between applications on different hosts** — delivers to the right process; ensures **error-free, in-sequence, end-to-end delivery** with error detection and automatic repeat request; **breaks data into segments and reassembles** them; **flow control** to prevent loss. *(b) Describe packet switching across the internet.* Four of: data **broken into equal-sized packets**; headers with **sender's and receiver's IP addresses**; each packet **sent independently** and not necessarily by the same route; each by the **optimum path available**; packets **may arrive out of order and are reconstructed in order** at the destination; missing or damaged packets **re-sent**.

### Cambridge 9618 November 2024 Paper 31 Q3–4 — circuit switching, and how the layers interact [3 + 2 + 4]

*3(a) Describe circuit switching.* A **dedicated circuit** is required; it is **established before** transmission; it **lasts for the whole transmission** and is closed at the end; data travels as a **continuous stream along the same route**; usually bidirectional. *3(b) One benefit, one drawback.* Benefit: no reassembly needed / data arrives in order, or suits real-time, or the whole bandwidth is available. Drawback: nobody else can use the circuit while it is held; not secure (one predictable route); if the route fails the transmission ends; set-up time. *4 Describe how the TCP/IP layers interact.* Four of: each layer accepts input only from the **layer above or below**; there is an **interface between adjacent layers** and that is the only interaction; **headers are added** as data passes down; the interactions are carried out by software; the **user interacts at the Application layer**; **hardware is accessed at the Link layer**. Part I's stack figure is this answer drawn.

### Cambridge 9618 June 2023 Paper 31 Q5 — where circuit switching belongs [2 + 4]

*(a) State, with a reason, where circuit switching is appropriate.* Where a **dedicated path must be sustained** throughout — where the whole bandwidth is required, or the communication is real-time; standard voice calls, video streaming, private data networks. *(b) Two benefits, two drawbacks.* Benefits from: whole bandwidth available; dedicated channel raises quality; fixed data rate; no waiting at switches; suits long continuous communication; data in order; nothing lost. Drawbacks from: the dedicated connection blocks other data even when idle; wasted capacity during silence; set-up delay; a broken path ends the call.

### Cambridge 9618 November 2025 Paper 31 Q3 — protocols, two named ones, and complete delivery [2 + 4 + 4]

*(a) Why a protocol is essential.* Protocols **set a standard set of rules** for communication; they **enable compatibility** between devices from different manufacturers; without a shared protocol two devices cannot communicate at all. *(b) Name and describe two protocols.* One mark each for the name and the description — SMTP *sends* email between client and server and between servers; IMAP lets a user *read mail from any device* without removing it from the server, synchronising across devices; POP3, HTTP, FTP and BitTorrent are equally acceptable with their one-line purposes. *(c) Two ways packet switching ensures a complete message.* Two marks each: packets are **checked on arrival** and, if damaged or missing, **a re-send is requested**; packets are **numbered** so the receiver can **detect a gap and reorder** — or, routed individually, so that a failed route does not lose the message.

### Cambridge 0478 June 2025 Paper 11 Q4 — choosing the transmission method, and the packet header [2 + 1 + 1 + 2]

A restaurant's tablets send orders to the kitchen computer over its network. *(a)(i) Two reasons serial full-duplex suits this.* One mark for the serial half — the data may travel more than a few metres, bits arrive without skew, fewer errors, and the volume is small so serial is fast enough — and one for full-duplex: data must go **both ways**, order in and confirmation back. *(ii) One improvement if parallel were used.* Faster transmission. *(c)(i) Which item is not in a packet's header?* The **payload / the data** — the header carries destination address, originator's address and packet number. *(ii) Two reasons the packets may need reordering.* They **arrive in the wrong order**; each **may take a different route**; some take longer than others.

### Cambridge 0478 November 2024 Paper 11 Q4 — the structure of a packet, and parallel full-duplex [4 + 4 + 2]

*(a) Describe the structure of a packet.* Three sections: a **header** containing data such as the destination address; a **payload** containing the main data (the email); a **trailer** containing data such as the error-detection method. *(b)(i) Why the company chose parallel full-duplex for a single office.* Parallel sends **several bits at once on several wires**, so it is **fast**; the devices are **within one room**, so distance and skew are not a problem; full-duplex sends **both ways at the same time**, so users can exchange data with no delay. *(ii) Two drawbacks.* More **interference / crosstalk** from multiple wires; bits may be **skewed** and arrive out of order; more chance of **collisions** with data in both directions at once.

### Cambridge 0478 June 2024 Paper 13 Q7 — draw serial half-duplex [4 + 2 + 1]

*(a) Draw and annotate a diagram.* Four marks for: bits sent **one at a time**; over a **single wire**; data can go **to and from** the web server; but **not at the same time** — the figure in Part IV is the answer, with the two-way arrows marked "one direction at a time". *(b) Two benefits* — a single wire is cheap; no skew; data can travel a long distance; both ends can send. *(c) One drawback* — the two ends must take turns, so a busy link waits.

### Cambridge 0478 November 2025 Paper 12 Q5(c) — the USB connection [2 + 2 + 1]

*(i) How data is sent over USB.* **One bit at a time** (serial), down a **single wire** (pair). *(ii) Two benefits.* From: the device can be **powered** by the connection; it is a **universal** connection; **backward compatible**; less chance of **skew** or error; supports different transmission speeds, adequate for the device; the cable **cannot be inserted incorrectly**. *(iii) One drawback.* The cable **length is limited** (a few metres); the speed is below dedicated interfaces for the heaviest data.

---

## Misconceptions

1. **"Faster internet means a bigger number on the plan."** The plan sells bandwidth — how much per second. What a game or a call feels is latency and jitter — how long and how steadily. A fatter pipe does not make a single packet arrive sooner; distance and queueing do that, and only moving the ends closer changes it.
2. **"The router knows the route."** A router knows only its own next hop for each destination. No device on the internet holds the whole path; the route emerges hop by hop, which is exactly why a failure anywhere can be routed around.
3. **"Packets of one message travel together."** They are forwarded independently, may take different routes, and arrive in any order. The sequence number in the header exists because they do not travel together.
4. **"TCP is the internet."** TCP is one transport protocol; UDP is the other, and it carries most of your video calls and games because it refuses to wait for re-sends. IP, underneath both, is what makes it one internet.
5. **"Full-duplex is twice as fast."** It is two directions at once, not double the bandwidth in one direction. A download on a full-duplex link is not faster than on a half-duplex one; it can just be answered while it runs.
6. **"USB is parallel because it is fast."** USB is serial, and so is every fast modern link. Parallel lost at distance to skew and crosstalk; speed today comes from clocking one wire very fast, not from adding wires.
7. **"Circuit switching is obsolete."** It lost the internet, but the idea survives in leased lines and in the comparison the exam draws; and every packet-switched voice call re-creates its virtues — fixed rate, in-order delivery — with buffering, at the cost of a small fixed delay.

---

## Hands-on

Everything here runs on your own machine, with tools already installed.

1. **Run the card.** `python3 networks-demo.py` (beside this card) opens a TCP conversation and a UDP one on your loopback interface, writes an HTTP request by hand and prints the server's headers, and counts what each layer adds to a 100-byte message. Change the message; change the server (`Host:` and the connection) to a site you use.
2. **Time the chain.** `ping -c 40 8.8.8.8` in a terminal, then the same to a server in your own city (your school's, or `ping www.baidu.com`) — the difference is distance. Do it on Wi-Fi and then on a cable, and watch the *spread*, not the average: that is jitter, and it is the lag you feel.
3. **Count the strangers.** `traceroute -n www.cam.ac.uk` (`tracert` on Windows) lists the routers that answer along the way with their addresses and delays. Try a site on your continent and one across an ocean, and watch where the delay jumps: that hop is the undersea cable.
4. **Look up an address.** `dig +short www.cam.ac.uk` asks a DNS server to turn the name into the IP address your packets will carry — the step that happens before any of the above, and the subject of [[The Internet and the Web]].
5. **Read a plug.** Look at a USB-C cable, an old rectangular USB-A, and the Ethernet cable behind a desktop: two serial links and one serial full-duplex link on four pairs. If you can find a parallel ribbon cable in an old machine, that is the road not taken.

---

## Exam Notes

### Cambridge 9618 — Section 14 (A2 Paper 3)

- **§14.1 Protocols:** why a protocol is essential; protocol implementation as a **stack**, each layer with its own functionality; the **TCP/IP suite's four layers** (Application, Transport, Internet, Link), the purpose of each, and what happens when a message is sent from one host to another; the purposes of **HTTP, FTP, POP3, IMAP, SMTP, BitTorrent** (peer-to-peer).
- **§14.2 Circuit switching, packet switching:** each described, with benefits, drawbacks and where applicable; the **function of a router**; how packet switching passes messages across a network including the internet.
- **Question shapes:** define a protocol's purpose (2); describe a layer's purpose (2–3 each, often two layers for 5–6); how the layers interact (4); describe packet switching (4); describe circuit switching (3) plus benefit/drawback (2) or where appropriate (2); name-and-describe two protocols (4); a fill-in-the-gaps paragraph with a word list (BitTorrent, peer-to-peer, stack, layered…).

### Cambridge 0478 — §2.1 Types and methods of data transmission (Paper 1)

- **§2.1.1:** data is broken into **packets**; a packet's **header** (destination address, packet number, originator's address), **payload** and **trailer**; the **packet-switching process** — broken down, different routes, the **router controls the route**, may arrive out of order, reordered once the last has arrived.
- **§2.1.2:** **serial, parallel, simplex, half-duplex, full-duplex** — describe each and explain its suitability for a given scenario, with advantages and disadvantages.
- **§2.1.3:** the **USB** interface, how it transmits data, its benefits and drawbacks.
- **Question shapes:** describe a packet's structure (3–4); the role of a router (2); why packets need reordering (2); choose and justify a transmission method for a scenario (2–4); *draw and annotate* a transmission mode (4); USB how/benefits/drawback (2 + 2 + 1); tick the item not in a header (1).

### IB Computer Science — A2.1–A2.3

- **A2.1 Network fundamentals:** LAN and WAN, client–server and peer-to-peer, the role of routers and the idea of a protocol. **A2.2 Network architecture:** layered protocols and the cloud as rented client–server. **A2.3 Data transmission:** packets, protocols and transmission media (copper, fibre, wireless), with [[Compression]] for the lossy/lossless half. The register is descriptive; the depth is this card's Parts I–IV without the 9618 mark-point precision.

### Not examined on…

- **AP Computer Science A** — no networking in the course.
- **The maths and physics boards** — none; the nearest physics is the speed of light in fibre behind Part V's propagation delay.
- **9618 AS Paper 1** examines none of Section 14; the topic is A2 only. **0478's §5 (the internet and its uses — WWW, URLs, browsers, ISPs, cookies)** is [[The Internet and the Web]], not here.

---

## Quick reference

| Ask | Answer in one line |
|---|---|
| why a protocol | a shared set of rules; without it different makers' machines cannot communicate at all |
| the four layers | Application (meaning; HTTP, FTP, SMTP, POP3, IMAP, BitTorrent) · Transport (program to program; TCP reliable, UDP fast) · Internet (machine to machine; IP addressing and routing) · Link (one hop; Ethernet, Wi-Fi) |
| how layers interact | only with neighbours, through an interface; headers added going down, stripped going up; user at the top, hardware at the bottom |
| a packet | header (destination, originator, number) · payload · trailer (error check) |
| packet switching | split, send each independently, routers pick the next hop, different routes, reorder by number, re-send the damaged |
| the router's job | read the destination address, forward to the best available next hop; nothing more |
| circuit switching | set up a dedicated path, hold it for the call, tear it down: in order, fixed rate, whole bandwidth — but idle capacity is wasted and set-up takes time |
| serial vs parallel | one wire, one bit at a time, any distance · many wires at once, fast, centimetres only (skew, crosstalk) |
| simplex / half / full | one way · both ways in turn · both ways at once |
| USB | serial, universal, powered, hot-plug, backward compatible; limited cable length |
| latency vs bandwidth | how long a packet takes (ping) vs how many bits per second; jitter is the variation, and the lag you feel |

---

## Connections

- **Parents:** [[Error Detection and Correction]] — the packet's trailer and the re-send request are its parity, checksum and ARQ, deployed on every packet; [[Encryption]] — HTTPS is HTTP inside TLS at the top of this stack, and the padlock's handshake rides on TCP; [[Operating Systems]] — the TCP/IP stack is implemented in the OS, and USB's plug-and-play is its device management.
- **Children:** [[The Internet and the Web]] — DNS, URLs, browsers, the World Wide Web as the largest application on this stack; [[NoSQL and Distributed Data]] — what happens when the machines at both ends are a data centre: partitions, and the CAP theorem as packet loss made into a design constraint.
- **Cross-domain:** [[Decouple and Recouple]] — the layered stack as the vault's cleanest example of decoupling by interface, and why the internet could change everything underneath a web page; [[The True IO Bound]] — the network rungs of the latency ladder, and why the wait is never the arithmetic; [[Graphs]] — routing is shortest-path search on a graph whose edge weights change every second; [[Stacks and Queues]] — every router is a set of queues, and jitter is their length varying; [[Sensors and Control Systems]] — a simplex link from sensor to controller is the simplest network there is.
- **Misconception traps cleared:** bandwidth is speed; the router knows the path; packets travel together; TCP is the internet; full-duplex doubles bandwidth; USB is parallel; circuit switching is obsolete.

## Sources

- P. Baran, *On Distributed Communications*, RAND (1964). V. Cerf and R. Kahn, *A Protocol for Packet Network Intercommunication*, IEEE Trans. Communications (1974). RFC 791 (IP) and RFC 793 (TCP), 1981; the ARPANET flag day, 1 January 1983.
- J. Saltzer, D. Reed, D. Clark, *End-to-End Arguments in System Design* (1984) — why the intelligence sits at the ends and routers stay simple. B. Cohen, *Incentives Build Robustness in BitTorrent* (2003).
- Cambridge 9618 syllabus 2027–29 §14; Cambridge 0478 syllabus 2026–28 §2.1. Question papers and mark schemes: 9618/31 June 2025 Q3, November 2024 Q3–4, June 2023 Q5, November 2025 Q3; 0478/11 June 2025 Q4, 0478/11 November 2024 Q4, 0478/13 June 2024 Q7, 0478/12 November 2025 Q5.
- The measurements — the traceroute, the forty pings (`networks-ping-samples.txt`), the TCP/UDP/HTTP run — were made on 2026-09-09 from a home connection in Chengdu with `networks-demo.py`; header sizes in the encapsulation count are the standard TCP (20 B), IPv4 (20 B) and Ethernet (14 + 4 B) values.
