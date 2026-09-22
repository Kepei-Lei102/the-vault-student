---
chinese: 独立磁盘冗余阵列 (dúlì cípán rǒngyú zhènliè)
prerequisites:
  - "[[Secondary Storage]]"
  - "[[Bitwise Operations]]"
  - "[[Error Detection and Correction]]"
leads_to: []
tags:
  - subject/computer-science
  - domain/computer-architecture
  - level/university
  - type/deep
  - type/definition
  - type/proof
  - notation/binary
  - misconception/redundancy-is-backup
  - misconception/parity-is-a-copy
  - misconception/raid-levels-rank-quality
---

# RAID 独立磁盘冗余阵列

Your family photos live in a little box beside the router. One evening, a drive inside it dies. A red light comes on. The photos still open.

The box has not made the drive immortal. It arranged the information so that **one broken part does not take the only surviving evidence with it**.

## Definition

**RAID — Redundant Array of Independent Disks** — combines physical drives into a logical storage device, distributing blocks according to a layout. Some layouts duplicate data; others compute extra recovery blocks. Some seek only speed and capacity: confusingly, **RAID 0 contains no redundancy at all**.

“Independent” describes the drives, not a guarantee that their failures are statistically independent. They may share a power supply, controller, enclosure, flood or careless human.

The original expansion was *Inexpensive*: Patterson, Gibson and Katz proposed assembling smaller drives into an alternative to a single large expensive disk in their [1987 Berkeley report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1987/5853.html), followed by the 1988 paper. The enduring question is architectural: can several fallible components cooperate to provide a useful service?

### 中文锚点

你把全家的照片存进路由器旁边的小盒子。有一天，一块硬盘坏了，盒子亮起红灯，照片却还能打开。它不是让硬盘变得不会坏，而是提前给照片留了后路：可以在另一块盘上留一份相同的内容，也可以多存一份由原数据算出的校验信息，让缺失的部分有办法算回来。**坏掉的盘不再是那些信息的唯一的存身之处。** 但如果你自己点了“删除”，盒子也会认真地把这个操作执行到所有副本上——它能替你扛住硬盘损坏，却不会自动替你记住昨天你还想留着的照片。

## The three building blocks

A **block** is a fixed-sized unit of storage. A **chunk** is the consecutive amount assigned to one drive before moving to another; it can contain many blocks. A **stripe** is one such row across the participating drives. The diagrams use one block per chunk to make the placement visible.

| Technique | What is stored? | What it buys |
|---|---|---|
| **Striping** | Different parts on different drives | Several drives can work at once |
| **Mirroring** | Copies of the same part on different drives | A surviving copy after a member fails |
| **Parity coding** | Data plus a computed relation between parts | Reconstruction without duplicating every part |

A file system such as NTFS can sit above a logical RAID device: it sees block addresses; the array maps them to drives. A hardware controller can do that mapping, or operating-system software can. Some systems, including ZFS, integrate allocation, redundancy and integrity checking. The responsibilities remain distinguishable even when one implementation owns several of them.

![[raid-layouts.svg|1000]]

*Equal letters are equal data; P and Q are recovery information. These are illustrative layouts, not a specification of every controller's on-disk format. RAID 1 uses two drives here; RAID 10 stripes across two mirrored pairs.*

## RAID 0 — share the work, share the risk

Number four drives 0–3. Store successive chunks A, B, C, D across them, then E, F, G, H on the next row. A large read can use all four drives concurrently.

With $n$ equal drives of usable component capacity $C$, ideal data capacity is $nC$. No space was spent on extra information. If a drive fails, its chunks have **no surviving copy and no recovery equation**. The complete logical volume is lost, although some raw blocks remain on other drives.

For one-block chunks, logical block $j$ maps to:

$$\text{drive}=j\bmod n,\qquad \text{row}=\left\lfloor\frac{j}{n}\right\rfloor.$$

The remainder chooses a column; the quotient counts completed rows. Larger chunks group several consecutive blocks before advancing to the next drive.

**Striping increases possible throughput, not the speed of every operation.** A tiny read contained on one drive still depends on that drive. A large sequential read may approach the combined drive bandwidth until the controller, bus, CPU or network becomes the bottleneck. A 1 Gbit/s network cannot deliver more than 125 MB/s of raw bits, even if the disks behind it can supply much more; protocol overhead lowers useful throughput further.

## RAID 1 and RAID 10 — keep a second copy

A two-drive **RAID 1 mirror** stores the same logical blocks on both drives. Two drives of capacity $C$ provide $C$ of data space. Either drive can fail while the other continues serving data, assuming the surviving copy is readable and consistent.

A read can be served from either member. A write must update both copies; those physical writes can happen in parallel. Mirroring can improve aggregate read throughput, but does not promise to halve every read's latency or double write throughput.

**RAID 10**, conventionally written **1+0**, stripes over mirrored pairs. With four drives, pair 0–1 stores A, C, E…; pair 2–3 stores B, D, F… . With $n$ drives in two-way pairs, capacity is $nC/2$.

The failure rule is more useful than a slogan:

> **Every mirror pair must retain at least one readable member.**

Lose drives 0 and 2: both pairs retain a copy. Lose drives 0 and 1: the first pair loses both copies, so the full volume cannot be recovered from this array. Thus conventional RAID 10 guarantees survival of **any one** drive failure, and may survive as many as $n/2$ failures **if they fall in different pairs**.

RAID **0+1** reverses the nesting: mirror two striped groups. A failed drive compromises its entire striped group, leaving the other group to carry the load. The order of composition changes which later failures are survivable; “the same four drives” is not the same protection model.

## RAID 5 — store the equation instead of the copy

Recall the two identities from [[Bitwise Operations]]:

$$x\oplus x=0,\qquad x\oplus0=x.$$

XOR is performed separately at each bit position, with no carry. For three data blocks $A,B,C$, form a fourth block:

$$P=A\oplus B\oplus C.$$

If $B$ is missing, use what remains:

$$
\begin{aligned}
A\oplus C\oplus P
 &=A\oplus C\oplus(A\oplus B\oplus C)\\
 &=(A\oplus A)\oplus(C\oplus C)\oplus B\\
 &=0\oplus0\oplus B=B.
\end{aligned}
$$

**Why it works:** every known contribution appears twice and cancels. The missing contribution appears once and remains. The same calculation works at every byte offset in a large block. If parity itself is missing, recompute it from the data.

![[raid-xor-recovery.svg|960]]

**RAID 5 distributes parity across the drives.** Stripe 0 might place parity on drive 3, stripe 1 on drive 2, stripe 2 on drive 1, and so on. The array sacrifices *one drive's worth of capacity*, not one dedicated parity drive. A dedicated-parity design is RAID 4; rotating parity helps distribute the update workload.

With $n$ equal drives, each stripe contains $n-1$ data chunks and one parity chunk, so capacity is $(n-1)C$. Any one whole-drive failure is recoverable under the known-failure model.

### Missing is different from secretly wrong

If the controller knows which drive stopped responding, there is one unknown block in each stripe. This is an **erasure**: the missing location is known.

If all drives return bytes but one returns the wrong byte, a parity mismatch alone does not identify the culprit. Changing A, B, C or P can each restore the equation. **One XOR relation can reconstruct one known erasure; it cannot in general locate an arbitrary silent error.** Checksums and a recovery policy are additional parts of the system.

Nor can one relation determine two missing bytes. If all we know is $A\oplus B=\mathtt{99}$, both $(\mathtt{3C},\mathtt{A5})$ and $(\mathtt{00},\mathtt{99})$ fit. In fact, every choice of A has a matching B: 256 possible byte pairs. More confidence cannot remove that ambiguity. More independent information can.

![[raid-recovery.mp4]]

*Watch drive 1 disappear. Its first two missing blocks are data; its third is parity. The same XOR reconstruction restores all three. The ending contrasts a failed drive with an intentional deletion.*

## RAID 6 — two genuinely different relations

**RAID 6** spends two drives' worth of capacity on recovery information and tolerates **any two known drive failures**. Capacity is $(n-2)C$.

Copying the XOR parity twice would not do this. Once two data blocks are missing, the second copy would merely repeat the same equation. A second **independent** relation is needed.

An ordinary-number analogy makes the idea visible: if $a+b=11$, many pairs fit; adding $a+2b=18$ fixes $b=7$ and $a=4$. Actual RAID byte arithmetic is different: ordinary integer addition and multiplication would require carries and larger storage units.

> [!info] Beyond syllabus — a little linear algebra over bytes
> Recall that XOR is addition modulo 2 on each bit. A common RAID-6 construction treats whole bytes as elements of a **finite field**, $\mathrm{GF}(2^8)$: addition is XOR, and multiplication is a special operation that keeps every result a byte. Every nonzero field element has an inverse.
>
> Store $P=\bigoplus D_i$ and $Q=\bigoplus \alpha_iD_i$, with distinct nonzero field coefficients $\alpha_i$. After removing known contributions, two missing symbols $x,y$ satisfy $x\oplus y=s$ and $\alpha x\oplus\beta y=t$.
>
> Substitute $y=s\oplus x$: $(\alpha\oplus\beta)x=t\oplus\beta s$. Because $\alpha\ne\beta$, the coefficient is nonzero and invertible, so $x=(t\oplus\beta s)/(\alpha\oplus\beta)$; then $y=s\oplus x$. Products and division here are **field** operations, not Python's ordinary `*` and `/`. This is a byte-sized simultaneous-equations problem. The runnable lab implements the operations; H. Peter Anvin's [RAID-6 mathematics](https://www.kernel.org/pub/linux/kernel/people/hpa/raid6.pdf) gives the construction.

This also explains why Reed–Solomon coding belongs nearby: recovery is constrained algebra, not a guess about what the missing photo “probably looked like”.

## Capacity and failure tolerance at a glance

Assume equal-sized drives, readable consistent survivors, and standard layouts. $C$ is one drive's component capacity; metadata and file-system overhead are omitted. “Failures” means members unavailable **before repair restores redundancy**.

| Layout | Conventional minimum | Data capacity | Guaranteed known drive failures tolerated |
|---|---:|---:|---|
| RAID 0 | 2 | $nC$ | 0 |
| RAID 1, two-way mirror | 2 | $C$ for that pair | 1 |
| RAID 5 | 3 | $(n-1)C$ | 1 |
| RAID 6 | 4 | $(n-2)C$ | 2 |
| RAID 10, two-way pairs | 4, even $n$ | $nC/2$ | 1; more if each pair retains a member |

These are the conventional configurations used here ([IBM level summary](https://cloud.ibm.com/docs/bare-metal?topic=bare-metal-bm-raid-levels)). Some implementations permit special layouts or different replica counts. Mixing drive sizes usually means treating members as the smallest component size in a conventional fixed-width array; pooling systems may arrange the leftover space differently. Check the layout, not just the logo.

The numbers are not a league table. RAID 6 is not “six times safer”, and RAID 10 is not a later software version of RAID 5. Each layout chooses a different trade between usable space, I/O work and survivable failures.

## Writes — the bill for keeping the equation true

Suppose one RAID-5 data block changes from $A_{old}$ to $A_{new}$. Re-reading every unchanged data block is unnecessary:

$$P_{new}=P_{old}\oplus A_{old}\oplus A_{new}.$$

The old A cancels out of the parity; the new A takes its place. This **read–modify–write** path normally reads old data and old parity, then writes new data and new parity: **two reads plus two writes** for one small logical write. That counts physical operations, not four necessarily serial time delays. Caches, batching and implementation choices change actual performance.

A **full-stripe write** already supplies every new data block, so parity can be calculated directly without those old-data reads. This is why a large sequential video write and many tiny database updates can behave very differently on the same array. RAID 5 spreads parity updates across drives, but a single stripe's parity still has to stay consistent.

### A power cut can split a promise in half

If new data reaches a drive but its new parity does not, the stripe is inconsistent. Later recovery may combine different generations of information. This is the **write hole**.

The issue is atomicity: several physical writes are meant to act as one logical change. A durable journal or correctly protected write cache can preserve enough information to finish or recover an interrupted update. Linux's [RAID write-journal documentation](https://www.kernel.org/doc/html/latest/driver-api/md/raid5-cache.html) describes one implementation. A generic file-system journal above the array does **not automatically** make the array's parity writes atomic.

## Rebuilding — the dangerous interval

A degraded array has already spent some of its protection. A **hot spare** is an available replacement target; it does not add a second parity relation to RAID 5. It can shorten the delay before rebuilding begins.

To replace a missing RAID-5 member, surviving drives supply the other blocks of each stripe and the controller writes the reconstructed result. Until enough reconstruction has completed, another failure can exceed the remaining protection. Rebuild traffic also competes with ordinary requests.

Three qualifications matter:

- **Unreadable sectors:** a surviving drive may reveal a sector it cannot read. With another block already missing in that stripe, RAID 5 can lack enough information to recover that stripe. Whether software aborts a rebuild or continues with damaged regions is implementation-dependent; one unreadable sector is not a universal theorem that every byte vanishes.
- **Correlated failures:** drives share heat, vibration, age, firmware and power. A probability model assuming independent failures may miss precisely the event that matters.
- **Integrity checks:** periodic scrubbing reads stored information and checks consistency so faults can be discovered while recovery information is still available. Plain parity does not always identify which readable block is wrong; checksums plus trustworthy redundancy can support repair in systems designed for it.

The honest question is not just “can one drive fail?” It is **“what remains recoverable during the time it takes to repair that failure?”**

## Worked examples

### 1. Four drives for a photo archive

Four 8 TB drives are available. Compare layouts for 12 TB of existing photos, with a separate backup already planned. Use decimal TB and ignore overhead for this first calculation.

1. **Trigger: fixed drive count and size → tool: count data slots per stripe.** RAID 0 gives 32 TB; RAID 5 gives 24 TB; RAID 6 and two-way RAID 10 give 16 TB. The photos fit all four today, but growth and operational free space still need a budget.
2. **Trigger: requirement to survive any two drive failures → tool: test the failure pattern.** RAID 6 meets it. RAID 10 does not: both members of one pair may fail. Merely counting “two remaining drives” loses the location information.
3. **Trigger: a capacity fit is not a workload result → tool: separate capacity, availability and I/O.** RAID 10 may suit a workload with frequent small writes; RAID 6 spends computation and update work for its stronger two-failure guarantee. This scenario has not supplied enough workload evidence for a universal speed verdict.
4. **Trigger: irreplaceable photos → tool: enumerate failures outside the array model.** Theft, a fire or an authorised deletion can affect the whole box. The separate backup must be recoverable independently, and a restore should be tried.

### 2. Recover a byte for real

A stripe contains A = `3C`, B = `A5`, C = `66` and P = `FF`, all hexadecimal.

**Trigger: B's location is known and exactly one block is absent → tool: XOR cancellation.** `3C XOR 66 = 5A`; `5A XOR FF = A5`. The missing byte is reconstructed exactly.

```python
from functools import reduce
from operator import xor

def xor_blocks(*blocks):
    if not blocks or len({len(b) for b in blocks}) != 1:
        raise ValueError("Supply one or more equally sized blocks")
    return bytes(reduce(xor, column, 0) for column in zip(*blocks))

A, B, C = bytes.fromhex("3c"), bytes.fromhex("a5"), bytes.fromhex("66")
P = xor_blocks(A, B, C)
recovered = xor_blocks(A, C, P)
assert recovered == B
print(P.hex(), recovered.hex())  # ff a5
```

Try changing all three data bytes and recomputing P. Recovery still works. Now remove two data bytes: the formula no longer has enough inputs. That is an information shortage, not a Python bug.

**Hands-on:** download [raid-lab.py](raid-lab.py) and run `python3 raid-lab.py`. It uses only in-memory bytes. It builds rotating-parity RAID-5 stripes, erases each drive in turn, reconstructs it, and exercises one- and two-erasure recovery in a RAID-6 stripe using actual finite-field arithmetic. The lab tests the recovery model; it is not a disk-management utility or a performance benchmark.

### 3. Why “I'll rebuild it tonight” needs arithmetic

An 8 TB replacement drive can sustain an effective reconstruction write rate of 150 MB/s. Estimate an optimistic rebuild time, assuming all 8 TB must be reconstructed.

**Trigger: amount divided by sustained rate → tool: $t=C/v$.** Use the same decimal units:

$$t=\frac{8\times10^{12}}{150\times10^6}=53\,333\text{ s}\approx14.8\text{ hours}.$$

This is a **lower-bound model under the stated assumptions**, not a promise. Competing I/O, surviving-drive read speed, retries, throttling and controller limits can make it slower. Some systems rebuild only allocated regions, changing the amount of work. The missing specification matters as much as the division.

## Where it earns its keep — the box beside the router

A **NAS** is network-attached storage: a service reachable over a network. **RAID is a way of arranging drives.** A NAS may use RAID; NAS and RAID are not synonyms, and a NAS with one drive has no extra drive to fall back on.

In the photo-box example, redundancy lets a failed member be replaced while the household can still read the album. The same availability problem appears in a school's file server or a workstation holding a large video project. The benefit is continuity while hardware is repaired.

A deletion is different. From the storage system's point of view, “remove this file” is a perfectly legitimate update. A mirror copies the resulting writes faithfully. Parity is updated faithfully too. Neither contains an automatic instruction to remember yesterday's version.

- **RAID** preserves service against specified member failures.
- **Snapshots/version history** can preserve earlier logical states, subject to their retention and storage failure domain.
- **Backups** provide recoverable copies with independence from the failure being defended against; a copy destroyed with the same box does not defend against losing the box.

These are complementary jobs. Choosing one does not discharge the other two. See [[File Systems]] for the distinction between file operations, snapshots and recoverable copies.

### Beyond the box — erasure coding across machines

Recall that RAID-5 parity is already an **erasure code**: extra information recovers data whose location is known to be missing. A general $(k+m,k)$ erasure code stores $k$ data fragments plus $m$ recovery fragments. With an appropriate maximum-distance-separable code, any $k$ of the $k+m$ fragments suffice, giving ideal storage efficiency $k/(k+m)$.

The fragments can live on separate drives, servers or sites. The algebra only helps if placement matches the failure: putting two nominally separate fragments behind the same failing power supply does not make them independent survivors.

Recovery also has a network bill. Reading many fragments across machines to rebuild one may consume substantial bandwidth. **Locally repairable codes** add structure to reduce the amount fetched for common repairs, trading recovery locality against other costs. Microsoft's [Storage Spaces discussion](https://learn.microsoft.com/en-us/windows-server/storage/storage-spaces/fault-tolerance) shows how storage efficiency, failure domains and reconstruction interact. The general problem is larger than picking a RAID number.

## Common misconceptions

### “Parity is a compressed copy of the missing drive.”

P alone cannot reproduce B. It needs A and C as well. **Fix:** keep P fixed and exhibit two different data triples with that parity; then restore the surviving inputs and watch the answer become unique.

### “RAID 10 survives two failures.”

Sometimes. **Fix:** draw the mirror pairs and cross out both members of one pair, then one member of each pair. The arrangement of failures is the deciding fact.

### “If the array says healthy, my photos are backed up.”

Healthy means the array meets its current operational checks. It does not mean yesterday's deleted folder exists anywhere. **Fix:** describe a mistaken deletion and ask which stored version could undo it.

### “A second parity block means a second copy of the first.”

That buys two copies of the same relation. **Fix:** try solving two unknowns with the same equation written twice. RAID 6 needs genuinely different information.

## Exam Notes

### Cambridge IGCSE 0478 and A-Level 9618

**RAID layouts and RAID capacity/rebuild calculations are enrichment**, not named requirements in 0478 (2026–28) or 9618 (2027–29). The examined foundations are storage technology (0478 §3.3; 9618 §3.1) and integrity checking (0478 §2.2; 9618 §6.2). Use [[Secondary Storage]] and [[Error Detection and Correction]] for those learning outcomes. A parity question is not automatically asking for a disk-array explanation.

### IB Computer Science — first assessment 2027

A1.1.7 requires secondary-storage types, including NAS, and their uses. It does **not prescribe RAID levels, parity-array layouts or reconstruction arithmetic**. RAID provides an explanation for one possible implementation of reliable network storage; NAS itself neither implies nor requires RAID.

### AP Computer Science A

The 2025 course framework is organised around Java programming, classes and data collections. RAID and storage-controller design are not prescribed topics. The Python experiment develops transferable reasoning but is not AP CSA language practice.

### Other UK A-Level specifications

[AQA 7517](https://filestore.aqa.org.uk/resources/computing/specifications/AQA-7516-7517-SP-2015.PDF) and [OCR H446](https://www.ocr.org.uk/images/170844-specification-accredited-a-level-gce-computer-science-h446.pdf) prescribe storage foundations but do not name RAID levels or reconstruction algorithms. Treat these as enrichment there too.

**Where it is not examined as a named topic:** RAID itself is not prescribed by any of these four CS courses. The connections above identify useful foundations, not additional RAID syllabus requirements.

## Connections

- **Parents:** [[Secondary Storage]] — the physical drives; [[Bitwise Operations]] — XOR and its cancellation identities; [[Error Detection and Correction]] — redundancy and the distinction between detection and correction.
- **Above the array:** [[File Systems]] — turning logical blocks into files, with separate consistency and version-history concerns.
- **Across machines:** [[NoSQL and Distributed Data]] — replication and distributed-system choices; a replicated database has additional consistency questions beyond a disk array.
- **Mathematical neighbour:** [[Simultaneous Equations (Vocab)|Simultaneous Equations]] — enough independent constraints to determine missing values; [[Symmetric Functions of Roots]] — a further connection to error-correcting codes.
- **Human story:** [[Stories/A Fight With the Inevitable Errors]] — the demand that machines repair errors instead of merely reporting them.

## LaTeX Reference

| Symbol | LaTeX | Meaning here |
|---|---|---|
| $A\oplus B$ | `A\oplus B` | Bitwise XOR |
| $n,C$ | `n,C` | Drive count and component capacity |
| $\lfloor j/n\rfloor$ | `\lfloor j/n\rfloor` | Completed rows in one-block striping |
| $\mathrm{GF}(2^8)$ | `\mathrm{GF}(2^8)` | Finite field containing 256 elements |
| $k/(k+m)$ | `k/(k+m)` | Ideal data fraction with $m$ recovery fragments |
