---
chinese: 文件处理 (wénjiàn chǔlǐ)
prerequisites:
  - "[[Arrays]]"
  - "[[Secondary Storage]]"
leads_to:
  - "[[File Systems]]"
tags:
  - subject/computer-science
  - domain/data-structures
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/0478-8-3
  - syllabus/9618-10-3
  - syllabus/IB-CS-B2-5
  - type/deep
  - notation/python
  - misconception/eof-is-a-character
  - misconception/write-mode-appends
  - misconception/written-means-saved
  - misconception/text-and-binary-are-different-things
  - misconception/a-comma-is-a-safe-separator
  - misconception/the-extension-is-the-file-type
  - misconception/close-is-how-you-save
---

# File Handling 文件处理

> *Every variable your program has ever created is gone. The array you filled, the record you assembled, the total you spent an hour getting right — all of it lived in RAM, and RAM forgets the moment the process ends. That is not a flaw to be worked around; it is the deal. A file is the **one** deliberate exception: the structure whose lifetime is longer than the program that made it. Everything else here — why `open` and `close` exist at all, why a file has no idea how many lines it has, why writing a record down is easy and reading it back is the hard part — follows from taking that exception seriously.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| file | 文件 | a named run of bytes that outlives the program |
| persistent / persistence | 持久化 | surviving after the process ends and the power goes off |
| open / close | 打开 / 关闭 | ask the system for access / hand it back and flush |
| file pointer | 文件指针 | the cursor marking how far through the file you are |
| EOF (end of file) | 文件结束 | the cursor has reached the end — a *condition*, not a character |
| read / write / append | 读 / 写 / 追加 | take data out / replace contents / add to the end |
| buffer | 缓冲区 | the waiting-area in RAM your writes sit in before the disk gets them |
| text file | 文本文件 | bytes agreed to mean characters |
| delimiter / separator | 分隔符 | the character that marks where one field ends |
| serialise | 序列化 | flatten a structure into a run of characters |
| metadata | 元数据 | the facts stored *about* a file — name, length, owner, dates |
| directory entry | 目录项 | the record that maps a name to its blocks and its length |
| magic number | 幻数 / 文件签名 | a signature in the first bytes by which a format names itself |
| atomic | 原子的 | happens completely or not at all — never half-done |

## The problem, before the tool

Run the class-average program from [[Arrays]] and it works perfectly. Run it again tomorrow and you type in all thirty scores again. Nothing was kept, because nothing *could* be: [[RAM and the Memory Hierarchy]] is volatile, and volatility is not a bug but the price of the speed that makes RAM worth having. Cut the power and every cell sags to zero.

So the hunter's question this time is not *what varies* but **what survives?** Three different needs push toward the same answer:

1. **Persistence** — data must outlive the process. The exam asks exactly this and it is the one-mark answer: *a file stores data permanently so it can be used again after the program has finished running*.
2. **Size** — some data is bigger than RAM. A file lets you work on a slice at a time.
3. **Sharing** — one program writes, another reads, possibly on another machine, possibly in ten years. A file is the oldest and most reliable interface between programs that will never meet.

## What a file actually is

Not an object on a disk. **A file is a name plus a promise.**

[[Secondary Storage]] gives the truth of the medium: a disk holds numbered blocks and knows nothing else. [[Operating Systems]] builds everything above that — the directory that maps a *name* to a *list of blocks*, the permissions, the timestamps. When you say `"scores.txt"` you are not naming a place; you are handing the operating system a lookup key and trusting it to find the pieces.

This is worth putting directly against the structure from the card before, because they are opposites, and the contrast explains both:

| | Array | File |
|---|---|---|
| lives in | RAM — gone when the process ends | secondary storage — outlives everything |
| layout | one **contiguous** block, no gaps | blocks anywhere, in any order |
| element $i$ found by | arithmetic: $\text{base} + (i-l)\times\text{size}$ | asking the operating system |
| can it grow? | no — the neighbours are not yours | yes — take any free block |
| cost of reaching item $i$ | one multiply and one add | a lookup, and possibly a disk seek |

An array buys constant-time access by demanding contiguity. A file gives contiguity up and buys growth and permanence with it. That is why a file can be appended to forever while an array cannot gain a single element, and it is why **defragmentation** exists at all — a file's blocks drift apart over its life, and [[Secondary Storage]]'s spinning platter pays for the scatter in arm movement.

## How the system tells one file from another

Nothing in the bytes says where a file begins or ends. The **directory entry** does: a record holding the name, where the blocks are, how long the data is, who may touch it and when it was last changed. Everything that delimits a file is stored *outside* it.

That is worth comparing with the thing it most resembles and is most unlike. A **network packet** carries its own header — length included — *inside* the transmission, because the wire remembers nothing: each packet arrives among strangers and must be able to say where it stops without help. A file is the opposite case. It sits in a system that keeps an index and can be asked, so its boundaries live in that index instead. Two names for the same choice:

- **in-band framing** — the boundaries travel with the data (a packet's header; a comma between fields)
- **out-of-band framing** — the boundaries live in a separate structure that describes the data (a directory entry; a database schema)

Hold on to that pair, because the serialisation section below is the same decision one level down, made *inside* one file's contents — and this time you have to make it yourself, because there is no index to consult.

**Then what is the `.txt` doing?** Not delimiting, and not identifying. An extension is part of the **name**, and the name is a string a human chose — so the extension is a *convention* about which application should open the file, not evidence about what is in it. Rename `holiday.jpg` to `holiday.txt` and not one byte changes; the operating system simply offers you the wrong program. Extensions lie freely, because nothing checks them.

What does not lie is a **magic number**: real formats put a signature in their first few bytes, so the file identifies itself from the inside. PNG opens with `89 50 4E 47`, PDF with the literal `%PDF`, ZIP with `PK` (Phil Katz's initials). Unix's `file` command reads those rather than the name, which is why it can tell you the truth about a mislabelled download.

The gap between the two is a real attack surface. `invoice.pdf.exe` is an executable whose *name* ends in something reassuring, and systems that hide "known" extensions show it to the user as `invoice.pdf` — a convention treated as a fact, which is how conventions hurt people.

## The lifecycle, and why `open` and `close` exist

Every language makes you open a file before using it and close it after. Students learn this as ritual. It is not ritual — each call does real work, and knowing what makes the rules obvious instead of arbitrary.

![[file-handling-lifecycle.svg|697]]

**`open` builds a live object.** It resolves the name to a location, checks that you are allowed the access you asked for, sets aside a **buffer** in RAM, and creates a **file pointer** set to the start. What you get back is not the file — it is a *connection* to the file, with a position of its own. Two programs can open the same file and each has its own pointer.

**The file pointer is why reading is sequential.** Each read hands you the next piece and advances the cursor past it. Nothing rewinds unless you ask. This single fact answers a question that otherwise looks arbitrary — *why can't I just read the last line?* — because in a text file, lines have no fixed length, so the only way to know where line 400 starts is to have walked past lines 1 to 399.

**`EOF` is a condition, not a character** — but then how does the pointer *know* the end is there? Not from anything inside the file. **The file's length is stored beside the file, not in it**: the directory entry that maps the name to its blocks also records how many bytes long it is. So `EOF()` is a comparison the operating system can answer without reading anything — *is the pointer now equal to the recorded size?* No sentinel byte is needed, which is exactly why a file may contain **any** byte at all, including one that looks like an ending.

That is worth dwelling on, because the misconception here is unusually respectable: **it used to be true.** CP/M allocated storage in fixed 128-byte records and recorded a file's length only in whole records, so it genuinely could not say where the data stopped inside the last one. The convention was to pad the tail with **Ctrl-Z (0x1A)** and have every program stop reading when it hit one — a real in-band end-of-file character, forced into existence by metadata too coarse to do the job. MS-DOS inherited it. The sentinel disappeared when filesystems started recording exact byte lengths, and the modern rule fell out of that one change.

The fossil is still visible, and it is on your disk right now. Every PNG file begins with the eight bytes `89 50 4E 47 0D 0A 1A 0A`, and the spec's own rationale explains each one: the high bit catches transfers that strip it, `PNG` names the format, the CR-LF pair catches newline mangling — and the **`1A` is there because Ctrl-Z stops file display under MS-DOS**, so typing a PNG at a DOS prompt halts politely instead of spraying binary at the terminal. A courtesy to a convention that stopped being how endings work, preserved in every PNG ever made.

**`close` flushes.** This is the one with teeth. Your writes do not go to the disk when you write them; they go to the buffer, because a disk answers in milliseconds and a CPU in nanoseconds ([[Secondary Storage]]'s speed-matching argument, met from the programmer's side). The buffer is emptied when it fills, and when you close. **Skip the close and the tail of your data was never written** — the program will have reported success on every line and produced a truncated file. It is the same mechanism as the "safely eject" button, and the same failure.

```python
f = open("scores.txt", "w")
f.write("74\n")
# program ends badly here — "74" may never reach the disk
```

Python's answer to *remember to close* is to make forgetting impossible:

```python
with open("scores.txt", "w") as f:      # the file is closed when the block ends —
    f.write("74\n")                     # including if an error is raised inside it
```

That is what `with` is for. It is a genuine case where real code is better than the exam's version rather than merely different: the dialect has no exception handling at AS level, so it can only ask you to remember.

## The three modes, and the trap in the middle

| Mode | What it does | The catch |
|---|---|---|
| **read** | open for input, pointer at the start | the file must already exist |
| **write** | open for output | **the existing contents are destroyed immediately** — before you write a single byte |
| **append** | open for output, pointer at the *end* | existing contents kept; new data goes on the end |

The middle row is why there are three modes and not two, and it is the most expensive beginner mistake in the topic: opening a data file "to add a record" in write mode empties it. There is no warning and no undo, because from the system's point of view you asked for exactly that.

```python
with open("log.txt", "w") as f:   # log.txt is now empty. The write hasn't happened yet.
    ...
with open("log.txt", "a") as f:   # log.txt is intact; new lines go at the end.
    f.write("another entry\n")
```

## But my editor saves instantly — how?

Nothing above describes how a real application behaves, and the mismatch is worth naming rather than leaving as a puzzle. A note-taking app appears to save on every keystroke. It plainly is not opening and closing a file a thousand times, and it is certainly not rewriting the whole document each time you press a key.

Start by tightening one sentence from earlier, because it is easy to over-read. **Flushing is what makes writing real; `close` is simply one thing that triggers a flush** — the last one, and the one you can forget. A program that intends to keep going just flushes when it wants durability and keeps the file open for hours. Open and close are not the unit of saving; they bracket a *connection*.

Three mechanisms do the actual work, and each answers a different part of the question.

**1. Write somewhere else, then swap the name.** The standard way to save a document is not to overwrite it. Write the new version to a **temporary file**, flush it all the way to the disk, then `rename` the temporary file over the original. Renaming is *atomic*: at every instant the name refers to one complete file or the other, never to a half-written one. This is what makes "save" survive a power cut — and it is the professional answer to the write-mode trap above, since the original is never opened for writing at all. (The subtlety, for the same reason: the rename itself has to be flushed, or a crash can leave the old name pointing at the old data.)

```python
import os, tempfile
def save_atomically(path, text):
    d = os.path.dirname(path) or "."
    fd, tmp = tempfile.mkstemp(dir=d)            # same filesystem, or rename won't be atomic
    with os.fdopen(fd, "w") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())                     # the bytes are on the disk, not just in a buffer
    os.replace(tmp, path)                        # atomic: old file or new file, never half of one
```

**2. Record the change, not the document.** Rewriting a novel because you typed one comma is absurd, so applications that save continuously **append** — a small record of *what changed* goes on the end of a log, which is cheap, and the full document is rebuilt from the last saved version plus the log. Append is the mode that makes this affordable, since adding to the end never touches what is already there.

**3. Let something else worry about it.** Most apps that appear to save instantly are not managing files at all — they are writing rows to an embedded database, overwhelmingly **SQLite**, which does the journalling, the atomic replace and the crash recovery internally. The application says *store this note*; the durability problem has been solved once, by people who specialise in it, rather than badly in every app.

And the honest tail: **"saved" in a user interface is a claim about the application's buffer, not about the disk.** The data may still be in the program's buffer, then the operating system's cache, then the drive's own cache. Only an explicit flush-to-disk makes it a fact — which is the same promise-versus-fact distinction the whole topic runs on.

## Text and binary are the same thing

A **text file** is not a different species from a binary file. Every file is bytes. A text file is a file whose bytes everyone has agreed to interpret as characters using a known encoding — which is exactly [[Text Encoding]]'s subject, and exactly why opening a file with the wrong encoding produces 乱码 rather than an error. The bytes were always fine; the agreement broke.

Two consequences worth carrying:

- **A "line" is a convention.** Lines are separated by a character, and the world never agreed which. Unix and macOS use one byte, `\n` (line feed); Windows uses two, `\r\n` (carriage return then line feed). Both names are instructions to a *typewriter carriage*: return the head to the left margin, then advance the paper one line. Nobody has owned that machine for decades, and every text file you make still carries its choreography.
- **Reading a line usually keeps its newline.** `readline()` in Python hands back `"74\n"`, not `"74"`, and comparing that to `"74"` fails. `.strip()` is the fix, and forgetting it is a rite of passage.

## Getting the structure back out

Writing is the easy half. Here is the hard half, and it is where the exam gets genuinely interesting.

A record has typed fields — a name, a flag, a weight. A text file has one long run of characters. **Flattening a structure into characters is called serialising, and the whole difficulty is that flattening throws away the boundaries.** `"Ali"`, `False`, `19.6` written one after another is `Ali False19.6`, and nothing in that string says where the name stopped.

![[file-handling-serialisation.svg|697]]

There are three answers, and each buys its safety with something:

**1. A delimiter.** Choose a character that separates fields — a comma, a tab, a `^`. Simple, readable, and it works right up until the data contains the delimiter. One address with a comma in it and every field after it shifts by one, silently, with no error anywhere. This is not a hypothetical: it is why CSV has quoting rules, and why those rules then need an escape for the quote character, and why "just split on commas" is the most confidently wrong line of code in data processing.

The exam poses this precisely. A scenario storing a website name and an encrypted password on one line states that *the encrypted password may contain any character from the character set* and that both fields vary in length — which is a way of saying **no delimiter is safe**, and then asking what you will do about it.

**2. Fixed width.** Give every field a known length and pad it. Nothing needs separating because you always know where to cut: characters 1–20 are the name, 21–28 the amount. Completely safe, and the exam asks for its cost by name — **wasted space**, since every short field carries its padding, and a hard ceiling, since a field longer than its slot cannot be stored at all.

**3. A length prefix.** Write the length of the field, then the field. `3Ali` says *take three characters*. Nothing is forbidden inside the data and nothing is padded — it is what real formats do, and it is the answer worth knowing even though the exam will accept the other two.

```python
# delimiter — fine until a name contains a comma
line = f"{name},{amount}\n"

# fixed width — safe, wasteful, and it truncates
line = f"{name:<20.20}{amount:>8.2f}\n"

# length-prefixed — safe and tight
line = f"{len(name)},{name}{amount}\n"
```

## Worked examples

### Example 1 — file into array, every tool named

*Read every line of a text file into an array of strings.*

**Tool: the read-until-EOF loop.** You cannot ask a text file how many lines it has — nothing stores that, and finding out means reading to the end anyway. So the loop is controlled by the *condition* EOF, not by a count.

**Tool: the array index as the write position.** [[Arrays]]' computable name does the work: one counter serves as both "how many so far" and "where the next one goes."

```python
lines = [""] * 1000
count = 0

with open("project.txt") as f:          # Tool: the context manager — closes on any exit
    for line in f:                      # Tool: iterating a file yields lines, in order
        if count == len(lines):         # Tool: the bound check — the array cannot grow
            break
        lines[count] = line.rstrip("\n")
        count += 1
```

Note the third tool. The array is fixed-length and the file is not, so one of them has to give — and a real exam question guarantees the array is the bigger of the two precisely so it doesn't have to be discussed. Outside the exam it does.

### Example 2 — the last three lines, and why it is awkward

*Output the last three lines of a text file.*

The instinct is to jump to the end. You cannot: lines vary in length, so the end is only reachable by walking. What you can do is walk once and **keep only what you might still need** — three slots, reused in a ring.

```python
BUFFER = 3
recent = [""] * BUFFER
n = 0

with open("log.txt") as f:
    for line in f:
        recent[n % BUFFER] = line.rstrip("\n")   # Tool: the MOD ring
        n += 1

start = max(0, n - BUFFER)
for i in range(start, n):
    print(recent[i % BUFFER])                    # Tool: read out in arrival order
```

That `% BUFFER` is [[Stacks and Queues]]' circular queue doing a second job: a fixed-size window sliding over an unbounded stream. This is a real Paper 2 question, and the marks are for spotting that a naive version prints the three lines *in the wrong order* — the ring's oldest slot is not slot 0 — and that it breaks when the file has fewer than three lines. Both bugs are the ring's, not the file's.

### Example 3 — writing records and reading them back

```python
from dataclasses import dataclass

@dataclass
class Entry:
    site: str
    secret: str

def save(entries, path):
    with open(path, "w") as f:                     # "w": the old file is gone from here on
        for e in entries:
            f.write(f"{len(e.site)},{e.site}{e.secret}\n")   # Tool: length prefix

def load(path):
    out = []
    with open(path) as f:
        for line in f:
            line = line.rstrip("\n")
            comma = line.index(",")                # Tool: the length is a known field
            n = int(line[:comma])
            site = line[comma + 1: comma + 1 + n]
            out.append(Entry(site, line[comma + 1 + n:]))
    return out
```

The secret may contain commas, quotes, anything at all, and this still works — because the only structural information is the length, and the length is read before the data it describes.

## Common misconceptions (teaching notes)

### 1. "EOF is a character at the end of the file"

Students write `WHILE ThisLine <> EOF` or look for a special byte.

**Fix:** ask the better question first — *how does the system know the end is there?* — and answer it: **the length is recorded beside the file, so EOF is a comparison, not a search.** Then give the misconception its due, because it was right for a decade: CP/M really did pad files with Ctrl-Z because it could not record an exact length. Ending on the PNG signature makes it stick — the `1A` in every PNG on earth is there to humour a convention that has been obsolete since before the students were born.

### 2. "Opening for write adds to the file"

They open a data file in write mode to add one record and lose everything.

**Fix:** run it once on a throwaway file with three lines in it and let them see the file empty *before* any write happens. The mode is a declaration of intent, and "write" means *this file's contents are now mine to replace.* Then append becomes memorable as the mode that exists because of this.

### 3. "Once I've written it, it's saved"

The program printed no errors, so the data must be on disk.

**Fix:** connect it to something they have already been told off about — the "safely eject" warning. Writes queue in a buffer for speed; `close` empties the queue. This is also why 0478 questions say *make sure both files are closed after use* and give a mark for it: closing is not tidiness, it is the step that makes the writing real.

### 4. "Text files and binary files are different kinds of thing"

Leads to the belief that a text file is somehow simpler or safer.

**Fix:** open a `.txt` in a hex viewer. It is bytes, like everything else. What makes it text is an *agreement* about how to read those bytes — and [[Text Encoding]]'s 乱码 gallery is what a broken agreement looks like.

### 5. "A comma is a safe separator"

The most consequential one, because it survives into professional work and fails silently.

**Fix:** hand them a file where one name is `"Smith, John"` and let the parse quietly shift every later field. Then present the three strategies as a *choice with costs* rather than a rule: delimiters are cheap and fragile, fixed width is safe and wasteful, length prefixes are safe and tight. Choosing is the skill.

## Exam Notes

### Cambridge 9618 (A Level)

**§10.3 Files**, AS content, examined on **Paper 2** — and reappearing constantly on **Paper 4**, since almost every practical scenario has to load or save something.

- Two learning objectives only: *show understanding of why files are needed*, and *write pseudocode to handle text files that consist of one or more lines*. The first is the persistence answer above; the second is where the marks are.
- The keywords are `OPENFILE … FOR READ / WRITE / APPEND`, `READFILE`, `WRITEFILE`, `EOF()`, `CLOSEFILE` — note the **two-word forms**, and that the file is named by a **string**, which is why the syllabus's `FILE` data type is never actually usable. [[Cambridge Pseudocode]] documents the dialect and that gap.
- **Serialisation questions are the discriminator.** Expect a scenario storing several variable-length fields on one line, with the stem quietly stating that the data may contain any character — that sentence is telling you a delimiter will not do. Say so, and give a length or fixed-width scheme.
- **Reading into an array is the standard pairing**, including as a stepwise-refinement question ("outline five steps") where you must describe the process without writing pseudocode at all.
- Expect **fault-finding on a file-reading algorithm** — the last-three-lines ring above is a real one, and the errors are ordering and the short-file case.
- Random and sequential *organisation*, record-level access and hashing are **not here** — they are A2 §13.2, which [[File Systems]] takes up. At AS every file is a text file read from the start.

### Cambridge 0478 (IGCSE)

**§8.3 File handling**, examined on **Paper 2**, and small but genuinely tested:

- Understand *the purpose of storing data in a file to be used by a program*; open, close and use a file for reading and writing — explicitly *including reading and writing a single item of data and a line of text*.
- Argument order is worth a mark on its own: a multiple-choice question has asked which of `WRITEFILE Hotels.txt, Name` and `WRITEFILE Name, Hotels.txt` is correct. **File first, then the data.**
- Write-out questions say so directly: one asks for statements to input a line, store it, lower-case it and store that, and instructs *make sure that any variables used are declared and that both text files are closed after they have been used.* Closing is on the mark scheme.
- Records do not exist at IGCSE, so the serialisation problem above does not appear in its full form — but the file-plus-array combination does.
- 0478 Paper 2 requires **pseudocode**; a correct Python answer earns nothing outside the scenario question. That hazard, and the fact that 0478 issues no insert, live in [[Cambridge Pseudocode]].

### IB Computer Science

**B2.5 File processing.** IB frames it around choosing and justifying a storage approach rather than around one dialect's keywords, so the three-strategy comparison and the array-versus-file table are the parts an IB answer wants.

### Where this is *not* examined

**AP Computer Science A has no file I/O at all** — input arrives only through `Scanner`, and no free-response question can require reading a file. Buffering, flushing, encodings and line-ending conventions are examined on none of the four boards; they are here because they explain the rules that are.

> [!info] Beyond syllabus — why "written" still doesn't mean "safe"
> `close` empties your program's buffer into the operating system. The operating system then has a buffer of its own, and the drive has one after that. A power cut in between can still lose data that every layer reported as written. Programs that genuinely cannot afford this — databases, above all — call `fsync`, which asks the whole chain to commit before returning, and pay for it in speed. It is the same trade the whole topic runs on: buffering is fast because it is a promise about the future, and a promise is not a fact. The database's answer to *how do I keep a promise across a crash* is the transaction log, which is why [[Databases]] exist as something other than a tidy file format.

> [!info] Beyond syllabus — the formats that solved this once
> Nobody hand-rolls serialisation any more, and the reason is that the three strategies above were argued to a conclusion decades ago. **CSV** is the delimiter approach with a quoting rule bolted on; **JSON** carries the structure explicitly, so nesting works and no field can be mistaken for a separator; **binary formats** like Parquet or protobuf use length prefixes for exactly the reason given above. Reading a modern format's specification is a good way to watch those three options being weighed by people who had to live with the answer.

## Connections

- **Built on:** [[Secondary Storage]] — the numbered blocks a file is assembled from, and the buffers that make `close` matter; [[RAM and the Memory Hierarchy]] — the volatility that makes files necessary in the first place.
- **Contrast:** [[Arrays]] — contiguity and constant-time access, traded away here for growth and permanence; the two are each other's complement, and moving data between them is most of what file code does.
- **Uses:** [[Stacks and Queues]] — the MOD ring, reused as a sliding window over a stream too long to hold; [[Text Encoding]] — the agreement that makes bytes into text.
- **Managed by:** [[Operating Systems]] — the directory entry that turns a name into blocks *and records the length EOF is measured against*, the permissions checked at `open`, and the atomic `rename` that makes a real save survive a crash.
- **The idea underneath:** in-band versus out-of-band framing. A file's boundaries live outside it in the directory; a network packet's live inside it in a header, because the wire keeps no index. The same choice reappears inside a single file as delimiter-versus-length-prefix — and reappears again as the difference between a self-describing format and one that needs a schema.
- **Extends into:** [[File Systems]] — how those blocks are organised and found, and the serial / sequential / random access methods; [[Databases]] — what you reach for when files stop being enough.
- **Exam dialect:** [[Cambridge Pseudocode]] — `OPENFILE`, `READFILE`, `WRITEFILE`, `EOF`, `CLOSEFILE`, and the undefined `FILE` type.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $n \bmod k$ | `n \bmod k` | the ring index for a fixed-size sliding window |
| $O(n)$ | `O(n)` | cost of reaching line $n$ of a text file — you must walk |
| $\text{base} + (i-l)\times\text{size}$ | `\text{base} + (i-l)\times\text{size}` | the array's constant-time alternative, given up here |
