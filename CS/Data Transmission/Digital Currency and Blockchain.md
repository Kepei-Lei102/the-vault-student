---
chinese: 数字货币与区块链 (shùzì huòbì yǔ qūkuàiliàn)
prerequisites:
  - "[[The Internet and the Web]]"
  - "[[Encryption]]"
  - "[[NoSQL and Distributed Data]]"
leads_to:
  - "[[Data Protection and Privacy]]"
tags:
  - subject/computer-science
  - domain/distributed-systems
  - domain/cryptography
  - level/IGCSE
  - level/IB
  - level/university
  - curriculum/Cambridge-0478
  - curriculum/IB-CS
  - syllabus/0478-5-2
  - syllabus/IB-CS-A2-1
  - syllabus/IB-CS-A2-2
  - type/deep
  - misconception/digital-money-requires-blockchain
  - misconception/hashing-is-encryption
  - misconception/blockchain-means-impossible-to-change
  - misconception/signatures-prevent-double-spending
---

# Digital Currency and Blockchain 数字货币与区块链

> *Copy a photograph and you have two photographs. Copy a payment and you must not have twice the money. Digital money begins with a surprisingly awkward question: who gets to say that something has already been spent?*

## Two pizzas, 10,000 bitcoins

On 18 May 2010, the Bitcoin forum user **laszlo** offered **10,000 BTC for two large pizzas**. He wanted enough for leftovers the next day. Three days later, with no deal yet, he wondered: *“Is the bitcoin amount I'm offering too low?”*

On **22 May**, he reported success and thanked **jercos**, the forum member who arranged the pizza. The exchange was between people; it did not mean the pizza restaurant itself accepted Bitcoin. You can still read [the original offer, the wait and the successful trade in the forum thread](https://bitcointalk.org/index.php?topic=137.0).

The interesting part is not a hindsight calculation of how rich he could have been. He was trying to turn an experimental digital asset into **something another person would provide in exchange**. A network can verify a payment; it cannot make somebody accept it, or make a pizza arrive. The cryptographic machinery and the human agreement solve different parts of the problem.

## Definition

**Digital currency** exists electronically rather than as physical notes or coins. It can be transferred electronically and used for payment where accepted. **Cryptocurrency** uses cryptographic mechanisms to control spending and maintain its records; Bitcoin is one example. Digital currency does not necessarily require a blockchain or lack a central issuer.

A **ledger** is a record of transactions. A **blockchain** organises records into blocks, cryptographically links each block to its predecessor, and uses rules for validating and agreeing on additions across participating computers. It produces a shared, ordered history whose alteration is detectable and, under the system's security assumptions, difficult to get accepted.

**Intuition:** the chain makes earlier pages answerable to later pages; consensus decides which version of the book counts. A chain of hashes on one laptop supplies the first property, not the second.

### 中文锚点

用比特币买完披萨，买家为什么不能拿同一笔钱再付一次？纸钞交出去，手里就没了；数字记录却可以复制。银行靠统一记账解决这个问题，区块链系统则要让许多参与者按共同规则认可一份交易历史。把记录串起来还不够，关键是大家怎样判断哪些付款有效、哪份记录算数。它努力守住的是“这笔钱已经花过了”，至于披萨有没有送到，还得靠账本之外的证据。

## Three things that are easy to confuse

| Term | What it describes | What it does not imply |
|---|---|---|
| Digital money | Money represented and transferred electronically | A blockchain; a new currency unit |
| Cryptocurrency | A cryptographically controlled digital asset/currency | Guaranteed purchasing power; complete anonymity |
| Blockchain | A way to maintain an ordered shared record | Money at all; public access; truthful input data |
| Wallet | Software/hardware that manages spending keys and constructs transactions | Coins stored inside the device as little files |
| Exchange | A service that trades assets and may hold them for customers | The blockchain itself |

A bank-app balance is digital money denominated in an ordinary currency. Paying by QR code changes the **interface**; it does not tell you whether the underlying ledger is a bank database or a blockchain. A **central bank digital currency (CBDC)** is a digital liability of a central bank; a **stablecoin** aims to track another asset's value, often through reserves. The issuer, claim, redemption rules and technical ledger are separate questions. [The Bank of England distinguishes these forms of money](https://www.bankofengland.co.uk/paper/2024/responses-to-the-digital-pound-consultation-paper).

Do not infer “decentralised cryptocurrency” merely from “electronic payment”. Nor does a stablecoin's name guarantee that its peg will hold.

## 1. Start with the invariant: money cannot be spent twice

Alice has 10 units. She sends Bob an instruction to transfer 7 and simultaneously sends Cara another instruction to transfer the **same** 7. Both instructions can be genuine: Alice herself signed both.

If Bob's computer sees only his payment, it finds enough money. Cara's computer, seeing only hers, finds enough too. Together the payments require 14 units. The failure is not arithmetic or forgery; the computers disagree about the state against which they checked the payments.

**The invariant:** a valid history must never spend more than is available, and must never consume the same spendable output twice. Authorisation and ordering are distinct requirements.

### The centralised solution already works

A bank maintains an authoritative ledger and serialises conflicting updates. After paying Bob, Alice has 3, so the second payment fails. [[Relational Databases]] supplies transactions and integrity rules; replication can protect availability without giving up one institution's authority.

A distributed system now asks: can several parties agree on the order **without appointing one of them the permanent owner of the ledger**? That is the problem a blockchain attempts to solve. It does not abolish trust: participants trust software, cryptography, rules and assumptions about who can overpower the protocol.

### Two models of spendable state

| Model | What is recorded | How a repeated spend is rejected |
|---|---|---|
| Accounts | Balances plus transaction sequence/state | Check available balance and the expected sender sequence number |
| Unspent transaction outputs (**UTXOs**) | Individually identified outputs from earlier transactions | An input must refer to an output that has not already been consumed |

Bitcoin uses UTXOs. Imagine Alice controls one output worth 10. A payment can consume that whole output and create 7 for Bob, 2 for Alice as change, and leave 1 as the fee:

$$\text{input value}=\text{recipient outputs}+\text{change}+\text{fee},\qquad 10=7+2+1.$$

A second payment referencing the same original output conflicts with the first. Copying its bytes does not create a new spendable output. A wallet's displayed balance aggregates what its keys can spend. The [Bitcoin transaction guide](https://developer.bitcoin.org/devguide/transactions.html) describes the input/output machinery. The small Python experiment below uses accounts instead, to make changing state easy to see.

## 2. Hashing: make changes visible

A **cryptographic hash** maps bytes to a fixed-length digest. SHA-256 produces 256 bits, normally displayed as 64 hexadecimal digits. It is deterministic: the same bytes give the same digest. A small change normally produces a very different digest.

A useful cryptographic hash makes it computationally infeasible to find an input for a chosen digest (**preimage resistance**) or two distinct inputs with the same digest (**collision resistance**). Collisions must mathematically exist—there are more possible messages than 256-bit outputs—but finding a useful one should be infeasible.

**Hashing is not encryption.** There is no decryption key. It is also not authentication: an attacker can edit a message and calculate its new hash. The expected digest needs a trusted source or must be protected by a larger construction.

```python
import hashlib

original = b"Alice pays Bob 7"
edited = b"Alice pays Bob 6"
print(hashlib.sha256(original).hexdigest())
print(hashlib.sha256(edited).hexdigest())
```

A [[Hash Tables|hash table]] wants fast, well-distributed indexing. A blockchain additionally needs resistance to an adversary deliberately searching for misleading matches. Python's built-in `hash()` is not a substitute for SHA-256.

### Link the records

![[blockchain-see-it-break.mp4]]

Watch one altered payment change a block hash and break the next link. This simplified SHA-256 chain demonstrates tamper evidence; signatures and consensus do separate jobs.

For a simplified block, let $T_i$ be its transaction data, $t_i$ its timestamp, and $n_i$ a nonce—a value varied during proof-of-work search:

$$h_i=H\bigl(\operatorname{encode}(h_{i-1},T_i,t_i,n_i)\bigr).$$

`encode` must specify exact bytes and boundaries. Otherwise “1 then 23” could look like “12 then 3”. The experiment uses a fixed JSON representation; real protocols prescribe their own formats. A timestamp records a time claim, not an infallible global clock.

![[blockchain-links.svg|700]]

**Follow the dependency, one move at a time:**

1. Change a transaction in block 1. Recomputing its digest no longer gives the stored $h_1$.
2. Replace the stored digest too. Block 2 still contains the old $h_1$, so its previous-block link fails.
3. Repair block 2. Its digest changes, so block 3 must change too.
4. Continue to the tip. You can repair a local chain; you have not made other participants accept it.

In Bitcoin the header commits to transactions through a **Merkle root**, rather than hashing every transaction directly with every mining attempt. The [Bitcoin block-chain guide](https://developer.bitcoin.org/devguide/block_chain.html) describes that extra layer.

## 3. Signatures: who authorised this payment?

The spender uses a **private key** to sign the transaction. Other participants use the corresponding **public key** to verify the signature against the exact transaction data. Changing the recipient or amount makes verification fail. [[Encryption]] develops public/private key cryptography; here its job is authorisation, not secrecy.

A signature does not mean “the whole transaction is encrypted”. Public blockchains often expose transaction data so participants can validate it. A signature also proves control of a key, not the holder's real-world name or whether they were tricked into signing.

**Why a signature alone cannot prevent double spending:** Alice can sign two conflicting payments. Both signatures verify. Deciding which payment consumes the available money requires the ledger's state and ordering rules.

**Replay** is another distinction: a copied signature may still verify for the same message. Rejecting an already-spent UTXO or an already-used account sequence number supplies freshness. Cryptographic authenticity is not permission to apply the same update twice.

A self-custody wallet holds or derives the keys. Losing the only usable key can mean losing access even though the ledger still records the funds. A custodial exchange controls keys on a customer's behalf; that introduces an institution the customer must trust.

## 4. Consensus: which valid history counts?

**Validation** asks, “Does this transaction/block obey the rules?” **Consensus** concerns agreement on one history among participants who may receive messages in different orders or behave maliciously.

A payment's journey is therefore:

1. The wallet constructs and signs a transaction.
2. It broadcasts it to peers; receiving nodes check authorisation and spending rules.
3. A block producer proposes a batch linked to an earlier block.
4. Nodes check the proposed block for themselves; invalid payments remain invalid even inside an expensive block.
5. The protocol's consensus rules determine the accepted history, and participating nodes update their ledger state.

![[blockchain-payment.svg|700]]

Copies propagate with delay. “Shared ledger” does not mean every phone stores the whole chain, all computers update simultaneously, or every participant votes on every payment.

### Why not simply count computers?

If one computer gets one vote, an attacker can invent thousands of identities: a **Sybil attack**. A permissionless system needs a scarce resource or another admission mechanism. Copying software must not buy unlimited authority.

### Proof of work: expensive to propose, cheap to check

In a simplified proof-of-work (**PoW**) puzzle, vary a block's nonce until its hash begins with $d$ zero hexadecimal digits. Each digit has 16 possibilities. Modelling successive hashes as uniform independent trials gives:

$$p=16^{-d},\qquad \mathbb E[N]=\frac1p=16^d.$$

Why $1/p$? Let $E$ be the expected number of attempts. You always make one attempt; with probability $1-p$ it fails and the same problem starts again. Thus $E=1+(1-p)E$, so $pE=1$ and $E=1/p$.

Two zeroes cost **256 attempts on average**, not exactly 256; three cost 4096. Checking a found answer takes one hash. The work is searching, not solving each transaction's arithmetic. The real Bitcoin rule compares a header hash with a numerical target, and mining includes a protocol-defined reward/fees.

Two valid blocks can arrive almost together, producing a temporary **fork**. Bitcoin's rule prefers the valid history with the **most accumulated proof of work**, not a vote by machine count and not simply the largest number of blocks when difficulty differs. More confirmations make replacing an earlier payment harder under the honest-hashpower assumption; finality is probabilistic. [Nakamoto's original paper](https://bitcoin.org/bitcoin.pdf) explains the double-spending race.

A majority-hashpower attacker can censor or reorganise history and attempt to reverse their own payments. That does **not** let them forge somebody else's signature or make an invalid spend acceptable to validating nodes. PoW also consumes energy: the cost is part of its defence, not useful calculation accidentally being done for free.

### Proof of stake and permissioned ledgers

**Proof of stake (PoS)** uses locked stake and protocol penalties to make dishonest participation costly. Ethereum's validators propose and attest to blocks; its rules include finality and punish certain conflicting votes. It does not run Bitcoin's mining race. Exact thresholds and attack assumptions belong to the chosen protocol, not to the word “blockchain”. [Ethereum's PoS documentation](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/) explains that design.

A **permissioned** ledger instead restricts who may participate in consensus, often to known organisations. Admission and governance help resist fake identities. Neither design means “trustless” in the literal sense: ask who may join, what resource or authority they control, and what happens when they collude or go offline.

## 5. What “immutable” can honestly mean

**Tamper-evident** means a change can be detected. **Tamper-resistant** means making an accepted change is difficult under stated assumptions. Neither means bits physically cannot be rewritten.

A correction is normally a **new transaction** that preserves the earlier record. Consensus failures, reorganisations, compromised keys, software bugs and governance changes are separate ways the practical guarantee can fail or change. A private database with hashes but one administrator remains under that administrator's control.

**The oracle problem:** an on-chain statement about the world still needs a source. If a sensor falsely reports “medicine stayed refrigerated”, a perfect ledger can preserve that false report perfectly. [[Sensors and Control Systems]] handles measurement; cryptography cannot establish a temperature it never measured. This distinction is central to [NIST's blockchain overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/NIST.IR.8202.pdf).

## Worked Examples — real questions, tools and triggers

### 1. Name the idea — Cambridge 0478/11/M/J/25 Q9(c) [1 + 1]

The scenario describes a company paying for a car electronically, then describes a ledger of timestamped records protected against alteration. The question asks for a definition and a process name.

**Tool and trigger:** “what is meant by” → the defining property, not a list of advantages. **A digital currency exists only electronically**, rather than as physical notes/coins. That earns the first mark; “used online” alone does not distinguish it from other payment arrangements.

**Tool and trigger:** timestamped transaction ledger → **blockchain**. That earns the second mark. Do not answer “Bitcoin”: that is one currency using the process.

### 2. Draw the causal path — Cambridge 0478/11/O/N/24 Q8 [4]

The task asks for an annotated diagram showing a digital-currency payment using blockchain. Use the payment diagram above, reducing it to four labelled features:

1. **Tool: a directed flow.** A customer's device sends payment data to a **digital ledger**.
2. **Tool: a record.** The ledger records the payment, with a **digital signature/date or timestamp**.
3. **Tool: grouping and identification.** Transactions are stored in a **block with a block hash**.
4. **Tool: replication.** The accepted block is linked into the blockchain copies held by participating devices.

The published scheme offers more than four creditworthy points; these select four explicit ones. Boxes labelled only “customer → internet → shop” omit the mechanism. Arrows must say what moves or changes.

**Technical precision:** the scheme also accepts a device “encrypting data”. That is not a universal requirement of a public blockchain: signing proves authorisation, while encryption hides contents. The four points above avoid that confusion. Likewise, blocks need not wait until completely full before being proposed.

### 3. Read the nouns carefully — Cambridge 0478/12/F/M/24 Q5 [4]

The supplied paragraph has four blanks describing electronic existence, the ledger name, a time record and traceability.

**Tool and trigger:** fit each blank's role rather than choosing a familiar technical word. The scheme's ordered answers are **physically; blockchains; time-stamp; traced**. “Encryption” cannot name the ledger, and a physical address cannot supply a transaction time.

The paragraph uses “cannot be altered” as its ledger abstraction. Explain the protection through linked hashes and agreement; do not turn that school-level shorthand into a promise of perfect security.

### 4. A genuine signature, an impossible second payment

Alice starts with 10. First accept Alice → Bob, 7; then consider Alice → Cara, 7. Assume each has valid authorisation and an otherwise acceptable sequence number.

**Tool: state invariant. Trigger: two updates draw on the same funds.** After the first, Alice has $10-7=3$. The second requires $7>3$, so reject it. A valid signature cannot increase the balance.

**Tool: conservation. Trigger: check that implementation did not create money.** Without fees or issuance, the total over all accounts remains 10. A payment of $a$ changes one balance by $-a$ and another by $+a$, so the net change is zero. If the sender and receiver are the same account, it still changes the total by zero.

## Where it is the working tool

### A payment recipient needs evidence, not a screenshot

In a cryptocurrency payment, the recipient needs to check the intended address, amount and accepted transaction history. A screenshot of “payment sent” is not evidence that the network accepted it. A wallet or service checks the ledger; confirmation policy accounts for the risk of replacement. Fees, congestion, custody and exchange into local money all affect the practical experience. The [Bitcoin payment-processing guide](https://developer.bitcoin.org/devguide/payment_processing.html) explains the acceptance problem.

### Coordinating food assistance across organisations

The World Food Programme's **Building Blocks** uses a privately managed blockchain network to coordinate assistance from multiple humanitarian organisations. Participating organisations can direct support to the same account and identify unintended overlaps. This is a concrete shared-record problem: several organisations need a coordinated view of assistance without one owning the entire arrangement. It is not a scheme requiring recipients to speculate on a coin. [WFP describes the deployed system](https://www.wfp.org/building-blocks).

The general lesson is **shared governance**, not “put every database on a blockchain”. If one school owns its lunch-card system and everyone accepts its authority, a conventional database can enforce balances more simply. A blockchain must earn the extra replication, consensus and operational complexity.

### Programmable escrow—and the boundary of code

A **smart contract** is a program whose execution changes blockchain state according to agreed rules. For example, funds may be released only when specified on-chain conditions hold. It is not necessarily a legal contract and it is only as correct as its code and inputs. A rule depending on delivery of a physical parcel still needs a trustworthy report of delivery. [Ethereum's smart-contract introduction](https://ethereum.org/en/developers/docs/smart-contracts/) describes the execution model.

## Hands-on — break the ledger, then repair it

Run the accompanying [Python source](digital-currency-blockchain.py) from its folder:

```bash
python3 digital-currency-blockchain.py
python3 digital-currency-blockchain.py --signatures
```

The first command uses only Python's standard library. It runs a **local account-ledger model**, real SHA-256, a tiny PoW search, balance checks and sender sequence checks. It does not connect to any network or move money. It assumes payment authorisation has already been checked; its transactions are unsigned.

The optional second command needs `cryptography` (`python3 -m pip install cryptography`) and adds a **separate real Ed25519 signature experiment**. Keys are generated temporarily in memory. Ed25519 is chosen for the library demonstration; this is not a claim that Bitcoin uses that signature scheme. The [library documentation](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ed25519/) gives the API.

**Predict each result before running:**

| Experiment | What to look for | Why it matters |
|---|---|---|
| Alice pays Bob 7; Bob pays Cara 3 | Alice 3, Bob 4, Cara 3 | Running state and conservation |
| Edit the first payment from 7 to 6 | The stored hash fails | Detectable tampering |
| Recompute the edited suffix and its tiny PoW | Alice 4, Bob 3, Cara 3; locally valid | Hash links alone cannot establish which history to trust |
| Build separate Alice → Bob 7 / Alice → Cara 7 branches | Both individually pass | Local validity does not settle conflicts |
| Try to include both with the same sender sequence | Reject replay/wrong sequence | The second update is not fresh |
| Add a longer branch containing an overspend | It loses to a shorter valid chain | Work never excuses an invalid transaction |
| Sign 7, then verify against 6 | Signature verification fails | A block hash can be recomputed; the spender's signature cannot simply be repaired |
| Verify the original signature again | It still verifies | Signature checking alone does not prevent replay |

**Scope of the model:** the fixed initial balances and genesis are trusted, timestamps are lesson-step labels, and all blocks use the same tiny difficulty. There are no peers, message delays, fees, rewards or real consensus. `choose()` compares supplied **valid** candidates by length only because their work target is identical. The exercise exposes the missing network problem rather than pretending to solve it.

The built-in checks cover 54 account/amount combinations, conservation, invalid amounts, replay, overspending, broken links, a changed genesis and valid-chain selection. To explore further, change `DIFFICULTY` from 2 to 3 and compare the nonce counts; individual searches vary, so one run does not establish the average.

## Common Misconceptions

- **“Digital currency means Bitcoin.”** Classify the money, its issuer and its ledger separately. A QR code tells you none of them by itself.
- **“A hash is encrypted data.”** Ask for the decryption key. There is none; the digest is a fingerprint, not a locked copy.
- **“A valid signature means accept the payment.”** Offer the two 7-unit payments from a 10-unit balance; authenticity does not settle ordering or availability.
- **“Changing a block is impossible.”** Repair the local hashes in the experiment; then ask what would make other participants accept the rewrite.
- **“Most computers win.”** Let one student invent 1000 identities; explain why permissionless consensus needs a scarce resource or admission rule.
- **“Everyone stores everything immediately.”** Distinguish full nodes, light clients and wallets; allow for propagation delay and temporary forks.
- **“A public address is anonymous.”** Addresses are usually pseudonyms. Linking one to a person can expose a history; privacy requires more than omitting a name.
- **“An accepted record proves the event happened.”** Feed a false sensor reading into a valid ledger. Integrity of the record is not truth of the claim.

## Beyond the syllabus — a short proof instead of a whole block

Recall that a block can commit to its transactions with a **Merkle root**. Hash pairs of transaction hashes, then pairs of those hashes, until one root remains. With eight leaves, a proof for one leaf needs only **three sibling hashes** to recompute the root: one per level.

For a balanced binary tree with $n=2^k$ leaves, $k=\log_2 n$. A membership proof therefore needs $O(\log n)$ hashes instead of the whole $O(n)$ list. A successful proof establishes inclusion under a particular root; it does not by itself prove that the transaction was valid or that the containing block belongs to the accepted chain.

This is a useful bridge to [[Binary Trees]]: a tree can be an instrument for **checking** a large dataset, not just finding an item in it. [[NoSQL and Distributed Data]] supplies the wider problem of keeping distributed state coherent.

## Exam Notes

### Cambridge 0478 IGCSE — §5.2.1–2, Paper 1

The 2026–28 syllabus requires the meaning and uses of digital currency, plus blockchain's process for tracking transactions. Its notes describe electronic-only currency and a timestamped ledger protected against alteration. Know payments/transfers as uses, and be able to **name, define, explain or draw and annotate** the process.

The real questions above range from a one-mark definition/name to four-mark completion and annotated-diagram tasks. For a process answer, connect **payment data → ledger record → block/hash → linked, replicated history**. “Secure and decentralised” without mechanisms is not an explanation.

SHA-256 internals, signature mathematics, UTXO scripting, mining-target calculations, PoS thresholds, smart-contract coding and Merkle proofs are enrichment; the syllabus does not require their implementation. No formula sheet is needed for §5.2.

### IB Computer Science — first assessment 2027, SL and HL

The February 2025 guide, **p.31**, names cryptocurrency blockchains as examples for **A2.1.2** (modern digital infrastructure) and blockchain for **A2.2.3** (client–server versus peer-to-peer models). These are **Theme A / Paper 1** applications at both levels. Explain benefits and limitations in context: distributed participation and resilience versus coordination, replication and security assumptions. A server-based wallet interface can sit on top of a peer network; compare the layer actually asked about.

These example references do not prescribe Bitcoin internals, mining calculations or contract programming. The [IB-authored guide, publicly mirrored](https://faq.computersciencewiki.org/images/uploads/computer-science-guide-en.pdf), is the scope source; the Cambridge questions above are not presented as IB papers.

### Where it is not a named topic

**Cambridge 9618 (2027–29)** does not prescribe digital currency/blockchain; its networking, hashing and §17.1 cryptography are supporting knowledge, not a blockchain syllabus row. **AP Computer Science A** does not examine cryptocurrency, blockchain consensus or SHA-256 implementation; this is an application of programming and data structures beyond its assessed content. Those absences were checked against the full syllabus/course descriptions. Do not confuse AP CSA with AP Computer Science Principles, or the outgoing IB course and its year-specific case studies with the 2027 guide.

## Connections

- **Parents:** [[The Internet and the Web]] — peer-to-peer communication; [[Encryption]] — public/private keys, signatures and cryptographic hashing; [[NoSQL and Distributed Data]] — replicated state and distributed coordination.
- **Components:** [[Hash Tables]] — hashing with a different threat model; [[Binary Trees]] — Merkle proof structure; [[Probability Basics]] — repeated hash trials and expected search effort.
- **Applications:** [[Relational Databases]] — the centralised alternative; [[Sensors and Control Systems]] — why trustworthy input matters; [[Ethics and Ownership]] — who governs rules and bears a failure's costs.
- **Extension:** [[Data Protection and Privacy]] — public transaction trails and identity linkage.
- **History:** [[Turing at Bletchley]] — cryptography's older adversarial setting; protecting a payment now needs public verification as well as secrets.

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $h_i$ | `h_i` | Digest committing to block $i$ |
| $H(x)$ | `H(x)` | Cryptographic hash of encoded bytes |
| $\operatorname{encode}$ | `\operatorname{encode}` | Agreed conversion into exact bytes |
| $p=16^{-d}$ | `p=16^{-d}` | Toy search success probability for $d$ leading hex zeroes |
| $\mathbb E[N]=1/p$ | `\mathbb E[N]=1/p` | Expected number of independent trials |
| $O(\log n)$ | `O(\log n)` | Merkle proof size for a balanced tree |
