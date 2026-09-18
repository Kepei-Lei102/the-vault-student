---
chinese: 文件系统 (wénjiàn xìtǒng)
prerequisites:
  - "[[Secondary Storage]]"
  - "[[Operating Systems]]"
  - "[[File Handling]]"
  - "[[File Processing and Exception Handling]]"
leads_to: []
tags:
  - subject/computer-science
  - domain/systems-software
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/0478-4-1
  - syllabus/9618-5-1
  - syllabus/IB-CS-A1-3
  - type/deep
  - notation/python
  - misconception/deleting-means-erasing
  - misconception/filename-is-the-file
  - misconception/formatting-means-sanitising
  - misconception/snapshot-is-a-backup
---

# File Systems 文件系统

> You delete a holiday photo. It disappears instantly, even if it was a gigantic video. You rename another: that is instant too. Copying it to a different drive takes minutes. **What changed in each case?** The answer begins with a separation: the name, the record describing the file, and the bytes themselves are different things. The recycle bin is only the lobby. The interesting machinery is underneath.

## Definition

### Formal

A **file system** is the set of data structures and rules that organises files and directories, records their metadata, maps their contents to storage, and tracks available space. The operating system's file-system implementation uses those structures to resolve names, read and write data, and enforce access rules.

A **regular file** presents a finite sequence of bytes to a program. Its **metadata** describes it: length, ownership, permissions, timestamps, and where its contents can be found. A **directory** associates names with file-system objects. The exact representation differs between FAT, NTFS, ext4 and APFS; an inode is one implementation, not a universal file-system requirement.

### Intuitive

The storage device offers numbered locations. You want `Photos/holiday.jpg`. The file system is the translator between those worlds—and the bookkeeper that stops two unrelated writes from being assigned the same live space.

**A filename is an address-book entry, not the thing it names.** Crossing out the entry, releasing the storage and physically erasing the contents are separate events.

### 中文锚点

一个很大的视频，改名只要一瞬间，复制到另一块硬盘却得等一会儿。因为文件名不是文件内容：文件系统一边记着“它叫什么、内容在哪里”，一边管理真正存放内容的空间。改名通常只改记录，复制则要搬动数据。删除也因此没那么简单：名字消失了，不等于内容立刻被擦净；能不能找回，还要看空间是否被重用、设备怎样处理删除。文件系统让我们用名字找东西，也决定了“找不到”究竟意味着什么。

## Notation and vocabulary

| Term | Meaning | Keep separate from |
|---|---|---|
| path | a route through directories, such as `/home/lee/photo.jpg` | the file's stored contents |
| directory entry | a name-to-object association | the object's metadata |
| inode | Unix-style metadata record identified within one file system | filename; a file may have several names |
| file descriptor / handle | a process's reference to an opened object | a path that must be looked up again |
| sector / logical block address (LBA) | a unit/address exposed by the storage device | the file system's allocation unit |
| block / cluster | unit in which a file system allocates space | a NAND erase block, usually much larger |
| extent | a run of consecutive blocks represented by start and length | a requirement that an entire file be contiguous |
| volume / mount point | a storage space with a file system / where it joins the namespace | necessarily one whole physical drive |

A **partition** divides a device's address space. A volume may occupy a partition, or be built by a volume manager from more complicated storage. **Formatting** creates file-system structures on a volume. **Mounting** makes an existing file system accessible: under a directory on Unix-like systems, or often through a drive letter on Windows. None of these words means “open an individual file”.

## Key Facts / Properties

### 1. Follow the name before following the bytes

For a Unix-style example, opening `/home/lee/photo.jpg` conceptually does this:

1. Start at the root directory `/` and find its `home` entry.
2. In that directory find `lee`, then in Lee's directory find `photo.jpg`.
3. Resolve the final entry to its metadata record; check relevant access permissions.
4. Create an open-file reference. Later reads use that reference and a current byte offset.
5. Translate the requested byte range into file-system blocks, then storage requests. Cached data may satisfy the read without accessing the device.

The metadata record need not contain the name: several directory entries can name the same object. ext4 explicitly separates these structures. Its [directory documentation](https://docs.kernel.org/filesystems/ext4/directory.html) is a concrete implementation to inspect.

A directory hierarchy is a **general tree**, not necessarily a [[Binary Trees|binary tree]]: one folder may have hundreds of children. Hard links and symbolic links complicate the tree picture; the namespace can contain several routes to an object. Internally, large directories may use hashing or tree indexes so lookup need not scan every name.

**Permissions and encryption answer different questions.** Permissions tell a cooperating OS which user may perform an operation; [[Encryption]] protects the representation of the bytes using a key. A read-only permission bit is not a cryptographic lock on a removed drive.

### 2. Allocation: how a long file fits into small blocks

Assume ordinary, uncompressed files, with no sparse holes or inline data. If file length is $S$ bytes and block size is $B$ bytes, the smallest number of whole data blocks that fits it is

$$n=\left\lceil\frac{S}{B}\right\rceil,\qquad \text{allocated data space}=nB.$$

**Why round upward?** $n$ blocks must satisfy $nB\geq S$. Dividing by positive $B$ gives $n\geq S/B$; the ceiling is the smallest integer allowed. The unused tail is **internal fragmentation**, or slack: $nB-S$, between $0$ and $B-1$ bytes. Metadata consumes additional space.

How do we remember which blocks belong to the file?

| Scheme | Record stored | Why choose it? | Cost or complication |
|---|---|---|---|
| contiguous allocation | start block + length | simple addressing; sequential reads stay together | growing the file may require relocation or another run |
| linked allocation | first block, then a next-block link | growth can use scattered free space | reaching block $k$ needs following links |
| FAT-style allocation | next-cluster links in a file allocation table | follows a chain without reading each data block for its pointer | the table still needs space and the chain still needs traversal unless indexed/cached |
| indexed allocation | a collection/tree of block addresses | jump to the address for a requested part | index space and extra lookups |
| extents | several start-and-length runs, often indexed by a tree | compress a large contiguous mapping | heavily fragmented files require more extents |

This is [[Arrays]] versus [[Linked List]] appearing inside your laptop. Modern implementations mix techniques; ext4's [extent mapping](https://docs.kernel.org/filesystems/ext4/ifork.html), for example, stores runs in a tree rather than keeping one address per data block.

A **free-space bitmap** spends one bit per allocation unit: conventionally, say, 0 = free and 1 = allocated. Allocation changes both the file's mapping and the free-space accounting. The critical invariant is **no unrelated live owners of the same writable block**. Deliberate sharing by clones/snapshots needs additional ownership tracking and copy-on-write.

### 3. Fragmentation is a map problem with a hardware price

Suppose a file occupies blocks `2, 3, 19, 20, 45`. Its bytes are logically consecutive, but its allocation is fragmented. A **defragmenter** relocates data into fewer contiguous runs and updates the mapping; the file's contents should not change.

On an HDD, scattered reads can require repeated head movement and rotational waits. Fewer runs can therefore reduce access time. An SSD has no moving head, so that particular benefit disappears; generic HDD-style defragmentation also adds writes. File-system fragmentation can still impose metadata overhead on SSDs. Let the OS use its device-aware maintenance rather than treating “defrag” and “TRIM” as synonyms.

Larger blocks reduce the number of mapping entries for large files but waste more tail space for small ones. There is no single best block size independent of the workload.

### 4. Deletion: three lifetimes, not one

In the Unix/POSIX model, a **hard link** is another directory entry for the same file object. Renaming an entry within a file system usually changes namespace metadata without copying the whole file. A move across file systems generally needs copying followed by deletion; some same-volume copies can instead use clones.

A **symbolic link** stores a path to follow. Deleting its target can leave a dangling link. A hard link names the object itself; removing one name does not remove the other.

For an ordinary local file without snapshots or other retained copies:

1. **Unlink a name.** Remove that directory entry and decrease the hard-link count.
2. **Wait for remaining references.** Other hard links still expose the file. An already-open file can remain usable even after the last name disappears.
3. **Reclaim the object.** Once no links or open references keep it alive, its storage becomes eligible for reuse.
4. **Reuse or discard storage.** Old bytes may persist for a while, be overwritten, or become inaccessible through device discard. Reclamation alone is not a promise about those bytes.

This is why an administrator can delete a huge log yet see little free space until the process holding it open closes it. The [Linux `unlink` contract](https://man7.org/linux/man-pages/man2/unlink.2.html) makes the open-reference rule explicit. Windows sharing and deletion rules differ; do not assume this experiment behaves identically there.

The **Trash / Recycle Bin** usually adds a reversible layer by retaining the file and recording its original location. Emptying it removes that protection; it does not certify physical erasure. Cloud “Recently deleted” folders and version histories have their own retention rules.

![[file-systems-deletion.mp4]]

*Watch the name disappear before the data: one timeline follows reuse on a simplified HDD; the other adds SSD discard and later flash reclamation. Blocks are schematic; the clip makes no recovery-time promise.*

### 5. The SSD's second map

Recall from [[Secondary Storage]] that NAND flash is programmed in pages but erased in larger erase blocks. Updating a page normally means writing elsewhere, changing a mapping, and treating the old page as invalid. The **flash translation layer (FTL)** maps the host's logical addresses to physical flash locations.

There are therefore two maps:

- **File system:** file byte offset → logical storage address.
- **SSD controller:** logical storage address → physical flash page.

The controller sees storage requests, not your folder names. **TRIM / discard** lets the OS tell it that specified logical ranges are no longer needed. Notification may be immediate, batched, unsupported, or blocked by an intermediate device. **Garbage collection** moves still-valid pages out of a victim erase block, then erases that block for reuse. Knowing which pages are unwanted avoids copying dead data. [Kingston's controller explanation](https://www.kingston.com/en/blog/pc-performance/ssd-garbage-collection-trim-explained) separates these jobs.

Crucially, a discarded logical address may stop returning the old contents **before** the underlying cells have been physically erased. Exact read-after-discard behaviour depends on the device and protocol. “Nobody has written a new file yet” is therefore insufficient evidence that an SSD's deleted file is recoverable. Conversely, TRIM is not a certified sanitisation operation.

### 6. Formatting and sanitising solve different problems

| Operation | Main purpose | What it does **not** establish by itself |
|---|---|---|
| delete / unlink | remove a name and eventually release allocation | that all copies of the content are erased |
| quick format | construct fresh file-system metadata without an exhaustive data-area overwrite | recoverability; the operation may issue discard |
| full format | tool-specific preparation, potentially including checks and overwriting | a universal erasure guarantee across devices |
| overwrite a file | replace the bytes reachable through that file | removal of snapshots, old copy-on-write versions or remapped flash pages |
| device sanitisation | make target data infeasible to recover under a stated assurance level | removal of copies on other devices or cloud backups |

**“Full” is a user-interface label, not a physical law.** As one precise example, Microsoft's Windows `format` documentation says `/Q` performs quick formatting, while `/P:0` zeroes each sector in the volume; `/Q` overrides `/P`. It also documents a switch to suppress TRIM, showing why a quick format cannot be treated as “metadata only, old bytes guaranteed intact”. These are descriptions, not commands to try on your drive. [Windows command reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/format).

A validated device erase/sanitise procedure can address storage that normal file writes cannot reach. **Cryptographic erase** instead destroys the keys needed to decrypt stored ciphertext. It depends on strong encryption already protecting all target data, sound key management, and eliminating all effective key copies—not merely deleting a password or enabling encryption after the sensitive data was written. Verification and the device's documented coverage matter. NIST distinguishes **clear** (resists simple recovery through ordinary interfaces), **purge** (resists state-of-the-art laboratory recovery while potentially permitting reuse), and **destroy** (makes the medium unusable as well as the target data infeasible to recover). [NIST SP 800-88 Rev. 2](https://csrc.nist.gov/pubs/sp/800/88/r2/final).

## Special Cases — surviving a crash

Creating a file changes several things: directory entry, metadata, block map and free-space map. Power loss can interrupt the sequence. Mark a block used but fail to link the file and space may leak; link it before its contents are ready and a reader may find incomplete data.

**Journalling** records a transaction in a log, with ordering and a commit marker, so recovery can replay committed changes rather than guessing which half-finished updates belonged together. Metadata-only journalling protects structure; it does not promise every recent byte of user data survived. ext4 offers different [journalling modes](https://cdn.kernel.org/doc/html/latest/admin-guide/ext4.html).

**Copy-on-write (CoW)** writes changed structures elsewhere, then publishes a new reference once the required writes are safe. Old referenced versions remain intact. This supports snapshots and cheap clones: initially share unchanged blocks, copy only the parts that diverge. APFS uses CoW metadata and supports clones and snapshots. [Apple's APFS guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/FAQ/FAQ.html).

A **snapshot** preserves a point-in-time view. Deleting a live file may release little space while a snapshot still references its blocks. A local snapshot can rescue yesterday's essay but dies with the same failed device. A separate, recoverable **backup** addresses that failure; [[RAID]] redundancy addresses a different one.

**Atomic is not durable.** Atomic replacement means observers see one complete version or another; durable means acknowledged changes survive the relevant failure. A program's buffered `write()` or `close()` does not alone prove power-loss durability. Robust saving involves flushing, appropriate file/directory synchronisation, a supported atomic replacement protocol, and a storage stack that honours the ordering. [[File Handling]] introduces the buffering distinction; the [Linux fsync contract](https://man7.org/linux/man-pages/man2/fsync.2.html) explicitly distinguishes file and directory synchronisation.

## Worked Examples

### Example 1 — the “size on disk” surprise

A game saves 1,000 separate files, each 600 bytes. Assume 4,096-byte blocks, no compression, no sharing and no inline data. Ignore metadata overhead.

**Tool and trigger: ceiling allocation — every tiny file still needs a whole block.**

$$n=\left\lceil\frac{600}{4096}\right\rceil=1.$$

Logical total: $1000\times600=600{,}000$ bytes. Allocated data total: $1000\times4096=4{,}096{,}000$ bytes. Tail waste: $3{,}496{,}000$ bytes.

**Tool and trigger: change the representation — most of the loss is per-file rounding.** If the payloads were packed into one 600,000-byte archive without compression or headers, they would require $\lceil600000/4096\rceil=147$ blocks, or 602,112 bytes. Real archives add headers and may compress; the saving here comes purely from packing. One large file also changes the ease of updating individual saves.

### Example 2 — find byte 9,000 without reading the beginning

Block size is 4,096 bytes. A file's first extent maps logical file blocks 0–2 to volume blocks 80–82. Offsets start at zero.

**Tool and trigger: quotient and remainder — split a byte offset into block number and position within it.**

$$9000=2\times4096+808.$$

The byte is in file block 2, offset 808. **Tool: extent translation.** The extent starts at file block 0 and volume block 80, so the answer is volume block $80+(2-0)=82$, byte offset 808 within that block. On an SSD, the FTL still has another mapping to perform. “Random access” does not mean random guessing; it means locating the required part without reading every previous record.

### Example 3 — delete both names, keep reading

This Python experiment creates and removes only its own temporary files. Run it on macOS/Linux on a local file system supporting hard links. It demonstrates normal open-file semantics, **not forensic recovery**.

```python
import os
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory(prefix="file-systems-") as folder:
    original = Path(folder) / "photo.txt"
    second_name = Path(folder) / "holiday.txt"
    original.write_text("sunset over Chengdu", encoding="utf-8")
    os.link(original, second_name)
    assert os.path.samefile(original, second_name)
    print("names:", original.stat().st_nlink)

    with original.open(encoding="utf-8") as reader:
        original.unlink()
        print("other name:", second_name.read_text(encoding="utf-8"))
        second_name.unlink()
        print("directory:", list(Path(folder).iterdir()))
        print("open reader:", reader.read())
    # reader is now closed; this experiment makes no raw-storage claim.
```

Expected output:

```text
names: 2
other name: sunset over Chengdu
directory: []
open reader: sunset over Chengdu
```

**Tool and trigger: track ownership separately from reachability — two names share one object.** Removing the first name leaves a hard link. Removing the second leaves the already-open reader. Closing it removes the final open reference. An empty directory listing tells you about names, not every live kernel reference or every physical copy.

### Example 4 — the recovery decision

You accidentally delete photos from an external HDD. There is no Trash copy. A second person loses a file from an SSD with discard enabled.

**Tool and trigger: trace what can still name or reconstruct the content.** First check independent backups or retained versions. For the HDD, surviving metadata may locate old data; otherwise recovery software may search for file signatures and reconstruct content, often losing names or fragmented pieces. Reusing the source space damages those possibilities, so don't install recovery tools or save recovered files onto it. A read-only image preserves a stable working copy when recovery matters.

For the SSD, “I stopped saving files” is no guarantee: discard and controller reclamation may already have removed host access. Neither case justifies promising recovery. The invariant is **preserve the evidence that remains**; the useful plan depends on the storage stack and what happened after deletion.

## Where this earns its keep

- **Lost phone photos:** a “Recently deleted” album or cloud version can retain a normal file that raw recovery cannot reconstruct. Recovery through retained references is a different mechanism from carving leftover bytes.
- **A USB drive that works on one machine but not another:** both may understand the USB hardware while supporting different file systems. Compatibility, maximum file size and permissions are properties of the format and implementation, not just the connector.
- **An essay saved over yesterday's version:** snapshots/versioned backups can retain the earlier data even though the current name points to the new version. Synchronisation alone may faithfully propagate the mistake.
- **Selling a laptop:** a clean-looking folder listing is not evidence of sanitisation. The relevant mechanism is the device's validated erase or cryptographic-erase path, with backup copies considered separately.
- **Game loading:** packing assets and arranging reads reduces tiny-file overhead and, on HDDs, seeks. Faster hardware does not abolish the cost of a poor access pattern.

## Common Misconceptions (Teaching Notes)

### “Delete means all the bits become zero.”

**Fix:** track three columns—names, live references, storage state. Ask which column each action changes. A fast unlink need not visit every byte; SSD discard may remove access without an immediate physical erase.

### “A folder contains the actual bytes like a box.”

**Fix:** create two hard links and ask which folder owns the single shared file. Directories hold associations. A symbolic link is different again: it stores a route, not a second hard link to the target.

### “If I overwrite the file enough times, every copy must disappear.”

**Fix:** draw both the file-system and controller maps, then add a snapshot. A write through one name cannot reach every old version, remapped location or backup. GNU's [`shred` limitations](https://www.gnu.org/software/coreutils/manual/html_node/shred-invocation.html) explain why in-place overwriting cannot be assumed.

### “Journalling or RAID means I no longer need backups.”

**Fix:** choose the failure first. Journalling repairs interrupted structural updates; RAID can tolerate specified hardware failures; backups preserve recoverable copies. Neither a consistent file system nor a mirror reverses a valid but unwanted deletion.

## Exam Notes

### Cambridge 0478 — §4.1.2

The 2026–28 syllabus includes **managing files** among OS functions. Explain organising files/directories, locating stored data, and supporting operations such as creation, copying and deletion. The internal inode/extent/FTL mechanisms are enrichment, not a required 0478 implementation specification. §8.3's opening, reading, writing and closing of program files belongs to [[File Handling]]; use [[Programming Fundamentals]] for the paired Python/exam notation.

### Cambridge 9618 — §5.1

The 2027–29 syllabus names file management and utilities including disk formatting, defragmentation, disk analysis/repair and backup. State **purpose → mechanism → benefit**: a defragmenter reorganises a fragmented file into fewer runs, reducing HDD seeks. Do not say it compresses the file. Formatting prepares file-system structures; it is not synonymous with validated sanitisation.

§13.2's **serial, sequential and random file organisation** concerns records and access methods, developed in [[File Processing and Exception Handling]]. It is a different layer from contiguous, linked or indexed allocation of storage blocks. Inodes, journalling internals and sanitisation commands are not named requirements. Worked examples above are original mechanism exercises, not attributed past-paper questions.

### IB Computer Science — first assessment 2027, A1.3.1–A1.3.2

The guide explicitly includes the **file system** among operating-system functions and OS abstraction of hardware. Use the path-to-storage explanation to explain that function. Inode layouts, TRIM and extent arithmetic are enrichment; this treatment does not complete all A1.3 scheduling, control-system and HL resource-management outcomes.

### AP Computer Science A — effective Fall 2025

**File-system internals are not examined.** Topic 4.6 does include text-file input using Java `File` and `Scanner`; that is an application-level operation, not a requirement to explain allocation, journalling or sanitisation. Do not turn “not examined” into “AP never uses files”. AP Computer Science Principles is a separate course and is not covered by this CSA scope claim.

## Beyond Syllabus — four answers to “what should storage make easy?”

Recall that a file system translates names into stored data while maintaining rules about ownership, free space and updates. **Choosing a format chooses which promises that translation layer can make.** A USB stick passed between devices and a laptop running several users’ applications face different problems.

The questions below are a way of interpreting the engineering choices, not quotations from the designers or a ranking from primitive to advanced.

| Format | A useful way to read its priorities | The trade-off to notice |
|---|---|---|
| **FAT32** | “Keep the shared map simple enough for many devices to understand.” | compatibility and simplicity; limited file size and few built-in protection mechanisms |
| **exFAT** | “Keep the portable map simple, but let the files grow.” | large-file interchange without the full machinery of a system volume |
| **NTFS** | “Make storage governable for a working, multi-user computer.” | richer access rules and recovery machinery require richer implementations |
| **APFS** | “Make sharing blocks and preserving versions fundamental operations.” | cheap clones, snapshots and flexible space allocation; more complex accounting and ecosystem dependence |

### FAT32 — a common language with a small vocabulary

FAT32’s central idea is familiar: directory records lead into chains in a file allocation table. A relatively small set of structures makes the format practical for devices with modest software. The attraction is often **how many readers can understand the map**, not how many features the map contains. Compatibility still depends on the particular camera, console or computer; “widely supported” never means every device.

The trade-off is visible when a USB drive has plenty of free space but rejects one large video: FAT32’s per-file size ceiling is just under 4 GiB. Free space and representable file size are different constraints. Standard FAT32 also lacks a metadata journal and native per-file access-control lists. A second FAT copy is redundancy for a table, not a journal recording a transaction’s progress. [Microsoft’s format comparison](https://learn.microsoft.com/en-us/windows/win32/fileio/filesystem-functionality-comparison).

### exFAT — modernise the suitcase, not the whole house

Microsoft’s stated goals are simplicity, large files/devices and extensibility. exFAT widens the file-size field to 64 bits. It also separates **which clusters are allocated** into a bitmap; a contiguous file can be described without maintaining a FAT chain for every cluster. That is a concrete way to reduce bookkeeping, not merely a bigger number in a specification. [exFAT specification](https://learn.microsoft.com/en-us/windows/win32/fileio/exfat-specification).

The philosophy is useful for a drive carrying large videos between compatible devices: move the payload without requiring a shared model of user identities and permissions. Standard exFAT does not provide NTFS-style access-control lists or metadata journalling; the separate **TexFAT** extension should not be silently assumed. A successful copy to exFAT therefore need not preserve the source system’s permission semantics. Simple interchange and rich system-volume behaviour are different jobs.

### NTFS — the filing cabinet has rules and a recovery ledger

NTFS is the default file system for modern Windows system storage. Think of a school’s shared computer: different accounts, private folders, applications updating files, storage quotas, and the possibility of power loss. **Who may change this, and can the structure recover if an update is interrupted?** These concerns justify machinery beyond “where are the bytes?”

NTFS supplies access-control lists, metadata journalling, quotas and other services. These make permissions and administration part of the file system’s job. They do not guarantee the last unsynchronised document edit survives, and permissions do not encrypt a removed drive. The OS, driver and enabled features still determine the actual behaviour. [Microsoft’s NTFS overview](https://learn.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview).

### APFS — a copy can be a new relationship, not new bytes

Recall that copy-on-write preserves shared data by writing changed parts elsewhere. APFS makes **clones**, **snapshots** and **space sharing** central features, alongside encryption support and a design optimised for flash/SSD storage. Its volumes can share the free space of an APFS container instead of each needing a permanently fixed allocation. [Apple’s APFS introduction](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/Introduction/Introduction.html).

Imagine duplicating a large video within the same APFS volume using a clone-capable operation. Initially the two files share content blocks, with additional metadata; changing one requires separate storage for the changed regions. The “copy” can appear almost immediately because its first act is to create a new relationship. A snapshot similarly retains a view of existing data. These are supported operations, not promises that every application’s copy command will use them. [Apple’s APFS guide](https://developer.apple.com/documentation/foundation/about-apple-file-system).

The accounting consequence is subtle: deleting one apparent copy may free little space while another file or snapshot still references its blocks. **What a user sees as separate files need not be separate physical allocations.** This flexibility also makes APFS a richer format for another device to implement; an Apple-native working volume and a widely exchanged USB drive need not want the same format.

### The deeper distinction: which layer owns the promise?

A file system is not the whole storage stack. An encrypted container can protect files stored on a format without native file encryption; an application can keep version history without native snapshots. Conversely, a file system supporting encryption does not mean a particular volume has it enabled. Ask **which layer supplies the feature, whether it is enabled, and which failure it covers**.

Nor must a network client understand the server’s on-disk format. A machine can request a file over SMB while the server translates that request into its own file-system operations. This is [[Operating Systems]]’ abstraction idea again: agree on the interface and the implementation can differ underneath.

**The question to carry away:** what must this storage make easy, and what must it preserve when something goes wrong? Compatibility, large files, access rules, structural recovery and version retention are separate axes. The letters on the format menu are different bundles of answers.

## Connections

- **Parents:** [[Secondary Storage]] — magnetic/flash mechanisms; [[Operating Systems]] — the manager and abstraction layer; [[File Handling]] — the program's open/read/write interface.
- **Implementation tools:** [[Linked List]], [[Hash Tables]] and [[Balanced Trees]] — chains and indexes beneath the names. [[Binary Trees]] supplies tree vocabulary; directories need not be binary.
- **Different layer:** [[File Processing and Exception Handling]] — record organisation and application failures, rather than physical allocation.
- **Protection:** [[Encryption]] and [[Data Security]] — protecting access, content and recoverable copies; [[RAID]] — hardware redundancy with a different failure model.
- **Meta bridge:** [[Decouple and Recouple]] — names, objects and storage can change independently because the mappings separate them.

---

## LaTeX Reference

| Symbol | LaTeX | Use |
|---|---|---|
| $\lceil S/B\rceil$ | `\lceil S/B\rceil` | whole blocks needed for an ordinary file |
| $nB-S$ | `nB-S` | unused tail space under the stated allocation assumptions |
