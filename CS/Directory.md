# The Vault — Computer Science Directory

> **61 cards across 10 bays.** Last landed: [[Program Development Life Cycle and Testing]] (2026-09-14) — cooking for six on Saturday: five stages, three models, three kinds of error, nine testing methods, four kinds of data, the trace table filled live; nine real Paper 2 questions from both boards.
> One line per card: what it teaches and, where settled, which syllabus rows it closes. Open the card for everything else — its frontmatter and Connections section carry the graph of what to read first.

**Reading the bays.** A bay is a run of cards built in order. *Closed* bays cover their syllabus stretch end to end; *open* bays are still growing, and the italic line under each names what comes next (a link that leads nowhere yet is a card still to be written). 💎 marks enrichment beyond every syllabus. Board codes: 0478 = Cambridge IGCSE, 9618 = Cambridge A Level, AP CSA = AP Computer Science A.

See also: [[Mathematics/Directory|Mathematics]] · [[Physics/Directory|Physics]] · [[Stories/Directory|Stories]] · [[Meta/Directory|Meta]].

---

## Foundations (6)

*The floor everything else stands on: the gates, recursion, information, and the three hard edges of the discipline — Turing, P vs NP, Gödel.*

1. **[[Logic Gates]]** — AND/OR/NOT/NAND/NOR/XOR as circuits that compute with voltage; truth tables and symbols; NAND universality; De Morgan as the licence to swap gates. *0478 §10 · 9618 §3.2*
2. **[[Recursion]]** — base case + recursive case; tracing the call stack; factorial, Fibonacci, list reversal; when recursion is the natural shape and when it costs. *9618 §19.2 · AP CSA §4.16*
3. **[[Information Theory]]** — Shannon's entropy $H=-\sum p\log_2 p$ as surprise measured in bits, and the floor under every lossless compressor. 💎
4. **[[The Turing Test]]** — the Imitation Game as a burden-of-proof flip; Turing's nine pre-answered objections; ELIZA and over-attribution; Searle's Chinese Room. 💎
5. **[[P vs NP]]** — if an answer can be *checked* fast, can it be *found* fast? P, NP, NP-complete, reductions, and why one crack would collapse the whole class. 💎
6. **[[Gödel's Incompleteness Theorems]]** — Gödel numbering makes provability arithmetic, and one self-referential sentence ends Hilbert's program; code-is-data in logical dress. 💎

## Logic Circuits (4 — closed)

*What you do with gates: transform, minimise, wire into arithmetic, bend into memory. 9618 §15.2 end to end.*

1. **[[Boolean Algebra]]** — the identities proved by law-chain, the duality principle, De Morgan, and simplifying an expression without moving a single truth-table row.
2. **[[Karnaugh Maps]]** — the truth table redrawn on a Gray-code grid so minimisation becomes "loop the biggest rectangles of 1s"; the map is a torus.
3. **[[Half-Adder and Full-Adder]]** — a computer does arithmetic by doing logic: Sum = XOR, Carry = the majority function; the ripple-carry chain.
4. **[[Flip-Flops]]** — memory bought with feedback: why one inverter in a loop oscillates and two remember; the SR and JK flip-flops; the SRAM cell.

## Algorithms (8 — core arc closed, plus enrichment, the paradigms and the life cycle)

*Concrete first, analysis after: searching → sorting → Big-O, with program design and the exam dialect alongside.*

1. **[[Program Design]]** — a flowchart is a causality trace someone already drew for you; the five design notations as five questions about one program; top-down design and the identifier table.
2. **[[Cambridge Pseudocode]]** — the one card that speaks the exam dialect — every keyword, declaration form and the `←` convention — so every other card can write real Python and point here.
3. **[[Searching]]** — linear vs binary search; why halving means a million items fall in twenty looks; the sorted precondition that sorting pays for.
4. **[[Sorting]]** — bubble, selection, insertion, merge and quicksort on one shared list, with the $n^2$-vs-$n\log n$ gap made tangible. *0478 §7.16 · 9618 §9.2 · AP CSA §4.15, §4.17*
5. **[[Big-O Notation]]** — how cost grows with $n$: the class ladder from $O(1)$ to $O(n!)$, the $c, n_0$ definition, reading Big-O off code. *9618 §19.1 · AP CSA §2.12*
6. **[[Parallel and External Sorting]]** — what sorting becomes with many cores or data too big for RAM: fork–join merge sort, Amdahl's law, the measured overhead crossover. 💎
7. **[[Object-Oriented Programming]]** — the nine syllabus terms built in real Python: data and behaviour bundled, encapsulation as invariants living next to the data, inheritance as is-a, polymorphism as the loop that never asks, containment as has-a; the June 2025 Animal/Parrot/Wolf and Nov 2025 Station/Train Paper 4 questions worked against their schemes; ECS in Beyond as OOP's deliberate inverse — and the vault's own architecture. *9618 §20.1 · AP CSA Unit 3 · IB CS B3*
8. **[[Program Development Life Cycle and Testing]]** — the cycle from coding onward and the three models (waterfall, iterative, RAD); syntax, run-time and logic errors by who finds them; nine testing methods, the strategy and the plan; normal / abnormal / extreme / boundary data and the six validation checks; trace tables done by hand and by machine; three kinds of maintenance. *0478 §7.1, §7.5–7.8 · 9618 §12.1, §12.3*

## Data Representation (12 — closed)

*How numbers, text, images and sound become bits. 0478 §1 and 9618 §1 complete, plus 9618 §13.1 and §13.3.*

1. **[[Number Bases]]** — place value as the one rule behind binary, denary and hex; conversions both ways; why base 2 and why base 16. *0478 §1.1.1–2 · 9618 §1.1*
2. **[[Two's Complement]]** — signed integers as wraparound turned into a feature: a register is arithmetic mod $2^n$, so subtraction becomes addition on one adder. *0478 §1.1.6*
3. **[[Overflow and Underflow]]** — the same wraparound as the villain: detection by carry bits, and the famous bugs (Pac-Man 256, Gangnam Style, Y2038, Ariane 5). *0478 §1.1.4*
4. **[[Bitwise Operations]]** — AND/OR/XOR/NOT applied bit-parallel; masking to test, set, clear and toggle; logical vs arithmetic shifts. *0478 §1.1.5*
5. **[[Gray Code]]** — the same $n$ bits re-ordered so neighbours differ in one bit, because physical bits don't flip together; the rotary encoder; a walk on the $n$-cube. 💎
6. **[[Floating-Point Representation]]** — binary scientific notation: mantissa for precision, exponent for range, normalisation as the most-tested skill, and the errors that follow. *9618 §13.3*
7. **[[Text Encoding]]** — character set vs encoding as two layers: ASCII's designed tricks, Unicode code points, UTF-8 worked on 你, and the 乱码 gallery read forensically.
8. **[[Image Encoding]]** — bitmaps store samples (pixels, RGB, resolution × colour depth = file size); vectors store intentions (a drawing list).
9. **[[Sound Encoding]]** — sample rate and resolution as the two dials in time; Nyquist–Shannon, aliasing, and why 44,100 Hz.
10. **[[Compression]]** — can you get the original back? RLE with its honest edge, Huffman on MISSISSIPPI, dictionary methods; lossy as a deal with your senses.
11. **[[User-Defined Data Types]]** — a type as allowed values + operations; non-composite (enumerated, pointer) vs composite (set, record, class), each in real Python. *9618 §13.1*
12. **[[Storage Units (Vocab)]]** — kilo/mega/giga vs KiB/MiB/GiB, why $2^{10}\approx10^3$ bred the confusion, and file-size arithmetic for images and sound. *0478 §1.3.1–2*

## Hardware Systems (13 — closed)

*The whole machine below the software line: Turing → von Neumann → the fetch–execute CPU → pipelining, then memory, storage, I/O, sensors, embedded systems, interrupts, assembly, CISC vs RISC. 0478 §3 (bar network hardware) and 9618 §3.1 + §4.*

1. **[[Turing Machine]]** — tape, head, states and a rule-book as the minimal model of computing; the universal machine; the halting problem proved by diagonal. 💎
2. **[[Von Neumann machine]]** — program and data in one memory, instructions as numbers: reprogram by loading, not rewiring; the bottleneck and the Harvard rival.
3. **[[CPU Architecture and the Fetch-Execute Cycle]]** — CU, ALU, the five exam registers and three buses; the cycle traced register by register on a three-instruction program.
4. **[[Pipelining and Simultaneous Multithreading]]** — overlap the stages so one instruction finishes per cycle; hazards, branch prediction, SMT, and the GPU's SIMD bet.
5. **[[RAM and the Memory Hierarchy]]** — DRAM as leaking charge, SRAM as a flip-flop; the cache ladder and why locality pays.
6. **[[Clock Domains and Metastability]]** — one crystal, many clocks: PLLs multiply by dividing, and a signal crossing clock domains can sit undecided. 💎
7. **[[Secondary Storage]]** — nothing in nature is a bit: magnetic, optical and solid-state media each hand you an analogue smear and a decision boundary.
8. **[[Input and Output Devices]]** — every peripheral is a transducer: keyboards, mice, the three touchscreen technologies, screens and printers.
9. **[[Sensors and Control Systems]]** — a sensor is a transducer pointed at the world; the fourteen 0478 sensors, the sensing chain, and the feedback loop with an actuator.
10. **[[Embedded Systems]]** — dedication, not power, is the boundary: the one-question test (can the user change what it does?) and the blurring hardware line.
11. **[[Interrupt Handling]]** — the doorbell and the bookmark: cause families, the service routine, priorities, and why one machine seems to care about everything at once.
12. **[[Assembly Language]]** — machine code with names on; the Cambridge instruction set, addressing modes as hop-counting, traced programs.
13. **[[CISC vs RISC]]** — the ISA is a contract, not a blueprint: why pipelines love RISC, how x86 decodes to micro-ops, and why the ecosystem still decides.

## Systems Software (2 — open)

*The software that runs the machine itself. 0478 §4, 9618 §5 and §16 complete.*

1. **[[Operating Systems]]** — part government, part illusionist: process states and scheduling, paging vs segmentation, files, drivers, utilities, and virtual machines. *0478 §4.1 · 9618 §5.1, §15.1, §16.1*
2. **[[Compilers and Interpreters]]** — translate the book once or interpret live: the three translators, the four compilation stages, BNF, and RPN on a stack. *0478 §4.2 · 9618 §5.2, §16.2*

*Next in the bay: [[The Call Stack]] · [[File Systems]].*

## Data Structures (8 — closed)

*From the array to the graph, each structure bought by restricting who may connect to whom. 9618 §10 and §19 complete, with §13.2 and the graph half of §18.1.*

1. **[[Arrays]]** — a name made computable: fixed length, one type and consecutive indices all forced by address = base + index × size; 1D and 2D.
2. **[[Stacks and Queues]]** — a stack is an array and one integer; a queue is an array and two; push/pop/enqueue/dequeue with their edge cases. *9618 §10.4, §19.1*
3. **[[Linked List]]** — order separated from location: nodes and pointers, insert in two writes, the free list, and the price paid in access time.
4. **[[File Handling]]** — what survives the process: open/read/write/close, text vs binary, serial, sequential and random-access files. *9618 §13.2*
5. **[[Binary Trees]]** — binary search frozen into pointers: the whole-subtree promise, insert and search, and the three traversals.
6. **[[Balanced Trees]]** — the hope converted into a contract: deletion built properly, the measured price of imbalance, and the rotations that keep $O(\log n)$. 💎
7. **[[Hash Tables]]** — don't store where things are, calculate where they must be; collisions as certainty (the birthday paradox), chaining and probing.
8. **[[Graphs]]** — delete every rule and the graph remains: adjacency matrix vs list, BFS and DFS, Dijkstra and A* worked on real papers. *9618 §18.1*

*Enrichment shelf: [[Heaps and Priority Queues]].*

## Databases (3 — closed)

*One fact, one place — then what happens when the place is a thousand machines. 0478 §9, 9618 §8 and IB A3 end to end, every worked question a real Paper 1 or Paper 2 against its scheme.*

1. **[[Relational Databases]]** — why files fail, Codd's tables linked by values, keys and E-R diagrams, normalisation to 3NF walked on a real order sheet and on real papers, the DBMS's features, ACID and the trillion SQLite instances in every pocket. *0478 §9.1 · 9618 §8.1–8.2 · IB A3.1–A3.2*
2. **[[SQL]]** — DDL and DML with every paper statement run for real in SQLite (script beside the card); the FROM-first execution order that explains WHERE vs HAVING; joins, GROUP BY, nested queries; the injection attack and the parameterised query. *0478 §9.2 · 9618 §8.3 · IB A3.3*
3. **[[NoSQL and Distributed Data]]** — the four families, sharding and replication, the CAP theorem proved in one paragraph, ACID vs BASE, 12306 and OceanBase, data warehouses and OLAP, and the NewSQL swing back. *IB A3.4 (HL) · 💎 for Cambridge*

## Security (2 — open)

*The threat/defence game, and the mechanism under the word "hacking". 0478 §5.3, 9618 §6, IB A2.4 — one real Paper 1 each against its scheme.*

1. **[[Data Security]]** — security/privacy/integrity; every threat as mechanism → aim → property (malware, phishing vs pharming, brute-force, DDoS, social engineering); the defences with the *how*; validation vs verification (valid ≠ true); a crack-time chart; and Beyond, the buffer overflow with the three walls — canary, NX, ASLR — and why a hack-lab turns ASLR off. *0478 §5.3 · 9618 §6.1–6.2 · IB A2.4*
2. **[[Encryption]]** — symmetric (Caesar → one-time pad → AES, Kerckhoffs) and asymmetric (Diffie–Hellman, RSA with $p=61,\ q=53$ walked and run, Euler's theorem, the factoring trapdoor); the two key directions and the who-holds-which-key table across HTTPS, mail, Signal, SSH, passkeys, updates, U 盾, wallets; hash-then-sign, certificates and CAs, TLS in five lines; key sizes, factoring records, QKD vs Shor and post-quantum; six real 9618 P3 / 0478 P1 questions. *9618 §17.1 · 0478 §2.3 · IB A2.4*

*Next in the bay: [[Encryption]] (0478 §2.3 · 9618 §17 · IB A2.4) and the ethics/privacy law card.*

## Data Transmission (3 — open)

*0478 Section 2, and 9618 Section 14. Two of the three subsections are written; §2.3 encryption lives in the Security bay.*

1. **[[Error Detection and Correction]]** — validation, verification and correction at three prices: parity and its honest limit, the parity block, checksums, check digits, the echo check. *0478 §2.2*
2. **[[Networks]]** — why a protocol, the four-layer TCP/IP stack with encapsulation counted, packets and packet switching animated, circuit switching weighed, serial/parallel/duplex and USB, latency measured from Chengdu. *9618 §14 closed · 0478 §2.1 · IB A2.1–A2.3*

3. **[[The Internet and the Web]]** — the internet is not the web: URL anatomy, the DNS chain sent by hand and animated, HTTP vs HTTPS with a certificate read live, session and persistent cookies fetched from a real site, MAC/IPv4/IPv6, the router, LAN topologies with a packet's path, client-server vs P2P, cloud, bit streaming. *0478 §3.4 + §5.1 · 9618 §2.1 · IB A2.2*

## Planned bays

Each closes rows across 0478, 9618 and AP CSA at once.

- **Programming foundations** — variables, selection, iteration, procedures and functions, scope. *0478 §8 · 9618 §11 · AP CSA U2*
- **[[Object-Oriented Programming]]** — classes, objects, encapsulation, inheritance, polymorphism. *9618 · AP CSA U1/U3*
- **Networks and the internet** — protocol stack, packets, addressing, the web. *0478 §2/§5 · 9618 §2/§14*
- **Ethics and encryption** — professional ethics, ownership, and the encryption depth ([[Encryption]]). *0478 §7 · 9618 §7/§17*
- **Artificial intelligence** — the 9618 §18 unit; cross-links [[Information Theory]].
- **Hardware enrichment** 💎 — [[Arithmetic Logic Unit]], [[How a Chip Is Made]], the modern CPU vs the textbook model, the GPU from triangles to tensors.

---

## How this directory stays honest

- **One line per card.** The hook says what the card teaches; the card carries everything else. If a line wants a second sentence, the second sentence belongs in the card.
- **Counts match the disk.** Each bay's number is the `.md` count in its folder and the total at the top is their sum; the linter checks both, and flags any line that has grown past a paragraph.
- **The landing story lives elsewhere.** What each card closed, and why it was built when it was, is recorded in the maintainer trackers at close-out — never here.
