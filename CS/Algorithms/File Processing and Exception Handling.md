---
chinese: 文件处理与异常处理 (wénjiàn chǔlǐ yǔ yìcháng chǔlǐ)
prerequisites:
  - "[[File Handling]]"
  - "[[Hash Tables]]"
  - "[[User-Defined Data Types]]"
  - "[[Program Development Life Cycle and Testing]]"
leads_to:
  - "[[File Systems]]"
  - "[[Relational Databases]]"
tags:
  - subject/computer-science
  - domain/software-engineering
  - domain/data-structures
  - level/A-Level
  - curriculum/Cambridge-9618
  - syllabus/9618-20-2
  - type/deep
  - type/definition
  - notation/python
  - misconception/exception-handling-is-interrupt-handling
  - misconception/try-except-makes-the-error-go-away
  - misconception/close-the-file-after-the-except
  - misconception/a-random-file-is-in-random-order
  - misconception/serial-and-sequential-are-the-same
  - misconception/exceptions-are-for-bugs
---

# File Processing and Exception Handling 文件处理与异常处理

> *Everything a program does inside its own memory, it controls. The moment it reaches outside — for a file, a disk, a line typed by a person — it is dealing with a world that can say no: the file is not there, the disk is full, the "number" is the word ten. This card is about both halves of that reach. First, the three ways records can be shelved in a file and what each way costs to write and to find. Second, what a program should do when the world refuses — and why the answer the syllabus wants, the exception, is not an error message but a **message that travels**: raised where the trouble is detected, caught where a decision can be made. The two topics share one sentence in the syllabus because they share one fact: a file is the place a program's promises meet reality.*

## 中文锚点

写了半天文档，按下保存，才发现U盘已经拔掉了。字还在屏幕上，不等于已经存进文件：程序还得把它交给外面的存储设备，而这一步可能办不到。发现U盘不在的那段代码，可以把问题往上传，让负责保存流程的部分来决定：换个位置，还是请你插回去再试。异常处理的用处，就在于把“发现这里出了什么事”和“决定接下来怎么办”分开，再把问题交给能拿主意的地方，而不是没存成也假装保存成功。

## Key Vocabulary

| English | 中文 | one-line meaning |
|---|---|---|
| record | 记录 | one entity's fields stored together, the unit a file is processed in |
| serial file | 串行文件 | records in arrival order; append to write, scan to find |
| sequential file | 顺序文件 | records in key order; scan-and-stop to find, merge to update |
| random (direct-access) file | 随机（直接存取）文件 | record position computed from its key; one seek to find |
| fixed-length record | 定长记录 | every record the same number of bytes, so address = slot × size |
| file pointer | 文件指针 | the position the next read or write happens at |
| seek | 定位 | move the file pointer to a computed address without reading |
| hash / hashing algorithm | 哈希 / 散列算法 | key → slot number |
| collision | 冲突 | two keys hashing to the same slot |
| exception | 异常 | an event during execution that disrupts the normal flow |
| exception handling | 异常处理 | code that responds to the event so the program does not halt unexpectedly |
| raise / throw | 抛出 | report an exception from the point where it is detected |
| catch / handle | 捕获 / 处理 | receive the exception and decide what to do |
| call stack unwinding | 调用栈回退 | the exception leaving frame after frame until a handler takes it |
| run-time error | 运行时错误 | a fault that appears only while the program runs, for some inputs |

## Part I — A record goes out to the file and comes back

[[File Handling]] stopped at lines of text: `OPENFILE`, `READFILE`, `WRITEFILE`, `EOF`, `CLOSEFILE`, and the discovery that writing a structure down is easy and reading it back is the hard part. The A-Level step is to make the unit of work a **record** rather than a line — the user-defined `TYPE` from [[User-Defined Data Types]] — and to ask how a whole file of them should be *organised* so that the operations the program actually performs are cheap.

Start with one common file format: **one record per line, fields separated by a comma.**

```python
from dataclasses import dataclass

@dataclass
class ToyRecord:                 # the syllabus's TYPE ... ENDTYPE, in Python
    toy_name: str
    number_bricks: int
    difficulty: str
    category: str

def write_record(f, r: ToyRecord) -> None:       # WRITE a record TO a file
    f.write(f"{r.toy_name},{r.number_bricks},{r.difficulty},{r.category}\n")

def read_record(line: str) -> ToyRecord:         # READ a record FROM a file
    name, bricks, diff, cat = line.rstrip("\n").split(",")
    return ToyRecord(name, int(bricks), diff, cat)   # the int() is where the world can say no
```

Three things the exam marks separately are hiding in those ten lines. The **mode** at `open` — `"r"`, `"w"`, `"a"` — with `"w"` truncating and `"a"` starting the file pointer at the end. The **newline** — every `write` must add one, and every `read` must strip one, or the last field of each record silently grows a `\n`. And the **cast**: a file holds characters, so `3981` comes back as the string `"3981"` until `int()` is asked to convert it, and `int("expert")` is the first exception this card will meet.

## Part II — Three ways to shelve the records

A text file read from the top is one organisation among three, and the syllabus names all three. The question that separates them is not *what is in the file* but **what the program needs to do most often**: add records, process every record, or find one record now.

![[file-processing-organisations.svg|900]]

### Serial — arrival order

Records are appended as they arrive; the file has no order except time. **Writing** is one append at the end, the cheapest operation a file offers. **Finding** one record means reading from the first record until it turns up — and a key that is not there costs the *whole* file, because nothing tells you it is absent until the end. A serial file is a log: the transaction file of everything that happened today, the audit trail, the backup written to tape in one pass.

### Sequential — key order

Records are kept sorted on a key field. Finding one record is still a scan, but a scan that can **stop early**: once the keys pass the target it cannot be further on, so a missing key is rejected in a few reads rather than the whole file. The price is paid at write time — a new record belongs *between* two existing ones, and a file cannot open a gap. Sequential files are therefore updated in **batch**: the day's transactions are themselves sorted into a serial-turned-sequential transaction file, then master and transactions are read once each, in step, and a **new master** is written — unchanged records copied across, updated ones replaced, deleted ones simply not copied, new ones slotted in as the keys dictate. This merge is the oldest algorithm in commercial computing, and it is still how a payroll or a statement run works, because touching every record in order is exactly what those jobs do. **Direct access** to a sequential file is possible if an **index** of key fields and positions is kept beside it — the exam's phrase for it.

### Random (direct-access) — computed position

The record's position is **calculated from its key** by a hashing algorithm — the disk-resident cousin of [[Hash Tables]], and the reason §13.2 asked you to "use hashing algorithms to read and write data to a random file". Hash the key, get a slot number, move the file pointer to *slot × record size*, read one record. One seek, one read, whatever the size of the file. Two consequences follow, and both are examined:

- **Records must be fixed length**, or the address arithmetic has nothing to multiply. A `STRING` field is padded (or cut) to a fixed width; the file is pre-sized so that every slot exists, empty, before any record is written.
- **Collisions happen**, because keys outnumber slots. The record goes to the next free slot (linear probing), or to an overflow area, and every later search must follow the same rule until it meets the key or an *empty* slot — which is why deleting must leave a marker rather than a genuine hole.

"Random" describes how the positions look from outside, not how they were chosen: nothing about the file is left to chance. Booking systems, account lookups, an operating system's own file tables — anything that needs *this record, now* — is a random file underneath.

The four pseudocode commands the syllabus gives this organisation map onto four Python calls, and [[Cambridge Pseudocode]] carries the dialect; the meaning is what matters:

| 9618 pseudocode | Python | what it does |
|---|---|---|
| `OPENFILE F FOR RANDOM` | `f = open(F, "r+b")` | open for reading *and* writing, no truncation |
| `SEEK F, Address` | `f.seek(Address * RECORD_SIZE)` | move the file pointer by arithmetic, reading nothing |
| `GETRECORD F, Rec` | `Rec = unpack(f.read(RECORD_SIZE))` | read the record at the pointer into a variable |
| `PUTRECORD F, Rec` | `f.write(pack(Rec))` | write the variable's record at the pointer, replacing what was there |

The `pack` and `unpack` are the fixed-length serialisation — Python's `struct` module turns a record into exactly 37 bytes and back:

```python
import struct
FMT = "<Bi24sd"                      # flag, 4-byte int, 24 bytes of name, 8-byte float
RECORD_SIZE = struct.calcsize(FMT)   # 37 — every record, whatever the name's length

class RandomFile:
    def __init__(self, path, slots):
        with open(path, "wb") as f:             # pre-size: every slot exists, empty
            f.write(struct.pack(FMT, 0, 0, b"", 0.0) * slots)
        self.f, self.slots = open(path, "r+b"), slots
    def hash(self, key):      return key % self.slots
    def seek(self, slot):     self.f.seek(slot * RECORD_SIZE)
    def get_record(self):     return struct.unpack(FMT, self.f.read(RECORD_SIZE))
    def put_record(self, rec): self.f.write(struct.pack(FMT, 1, *rec))

    def find(self, key):                        # hash, then probe until key or empty
        slot = self.hash(key)
        for _ in range(self.slots):
            self.seek(slot)
            flag, k, name, balance = self.get_record()
            if flag == 0:  return None          # empty slot: it was never here
            if flag == 1 and k == key: return (k, name.rstrip(b"\0").decode(), balance)
            slot = (slot + 1) % self.slots      # collision: the next slot
```

The full engine — `put` with update-in-place and tombstone reuse, `delete`, the serial and sequential operations beside it, and a 6,000-operation fuzz against a Python `dict` in which the file never once disagreed — is `file-processing-records.py`, committed beside this card. Its run also shows the three costs on the same fifty records: the fortieth record written takes forty serial reads, nine sequential reads (its sorted position), and one seek; a missing key costs fifty serial reads and two sequential ones; fifty keys in 101 slots collide often enough that seven of them needed a second probe and the worst needed six.

### The cost, measured

![[file-processing-seek-vs-scan.svg|760]]

`file-processing-benchmark.py` builds files of 37-byte records from a thousand to three hundred thousand and times one lookup in each. The serial scan grows with the file — twenty milliseconds by the top — and the random-file lookup stays at seventeen microseconds regardless, because it never learns how big the file is. That flat green line is the whole argument for random organisation, and it is the same flat line [[Hash Tables]] drew in memory.

![[file-processing-manim.mp4]]

## Part III — When the world says no

Run the reader from Part I on a file whose second line is `Pear,ten,Easy,Play`, and the program stops:

```
Traceback (most recent call last):
  File "toys.py", line 21, in <module>      load(lines)
  File "toys.py", line 14, in load          return [parse_line(l) for l in lines]
  File "toys.py", line 9,  in parse_line    return name, int(qty)
ValueError: invalid literal for int() with base 10: 'ten'
```

Read that as a story rather than an error. `int()` was asked for something impossible and **raised** a `ValueError`. Nobody in `parse_line` had said what to do about that, so the function was abandoned and the exception moved up to `load`, which had said nothing either, so `load` was abandoned too — and so on to the main program, and past it, where the interpreter's default policy is to print exactly this list of abandoned frames and halt. Every frame is listed because every frame was unwound.

![[exception-stack-unwind.svg|900]]

### What an exception is

An **exception** is *an event during the execution of a program that disrupts the normal flow of instructions* — the mark scheme's own wording — and, left alone, causes the program to halt unexpectedly. The causes the examiners list, and expect you to list, fall into four families:

- **User errors** — a filename that does not exist, a word where a number was expected, an empty input.
- **Hardware and environment failures** — the disk is full, the network is down, the printer has gone.
- **Programming errors** that surface only for some inputs — an array index past the end, a division whose denominator happens to be zero, a `None` where an object was assumed.
- **Run-time errors** generally — the third kind of error in [[Program Development Life Cycle and Testing]], the kind the translator cannot catch because the program was perfectly grammatical.

Two of those four are things the program **could not have prevented**: the file *was* there when it was written, and the user *usually* types a number. That is the point of exception handling, and the answer to the syllabus's "know when it is appropriate": an exception is for the **expected but unpreventable** failure. A bug — the loop that runs one too far — should be found by testing and *fixed*; catching it and carrying on would hide the fault, not handle it.

### What exception *handling* is

Exception handling is *the process of responding to an unexpected event while the program is running, so that it does not halt unexpectedly* — one mark on Paper 3, verbatim. The mechanism has four parts in Python, and the same four in Java and VB.NET under the names `try` / `catch` / `finally` / `throw`:

```python
try:
    f = open(filename)                 # the code that might fail
    records = [parse_line(l) for l in f]
except FileNotFoundError:              # one policy for one cause ...
    print("File not found:", filename)
    records = []
except ValueError as e:                # ... another policy for another cause
    print("Bad line skipped:", e)
    records = []
else:                                  # runs only if nothing was raised
    print(len(records), "records loaded")
finally:                               # runs whatever happened — even after a return
    print("finished trying")
```

- **`try`** marks the region whose failure you are prepared for. It should hold *everything* that can fail for the reason you are handling — including, for files, the `open` itself.
- **`except <Class>`** is a *policy* for one *cause*. `FileNotFoundError` and `ValueError` are different events with different sensible responses, and naming them keeps the two apart. A bare `except:` catches everything, including a user pressing Ctrl-C and the program's own attempt to exit; it is accepted on the mark scheme, and it is what you must *not* do in code someone will run.
- **`finally`** is the tidy-up that must happen on both paths — closing a file, releasing a lock. `exception-handling-demo.py` shows it running after the `return` value has already been decided.
- **`raise`** reports an exception from *your* code. `raise InsufficientFunds(f"asked for {amount}, only {balance} available")` turns an impossible state into a message that travels to whoever can decide — and defining your own class (`class InsufficientFunds(Exception): pass`) lets the caller name it in `except`.

The word that matters most is *travels*. Detection and decision are usually in different places: the line that cannot convert `"ten"` has no idea whether the right response is to skip the record, ask the user again, or abort the run. Before exceptions, functions returned a special value — `-1`, `NULL` — and every caller had to remember to check it, and most did not. An exception cannot be ignored: it either meets a handler or it stops the program. That inescapability is the design.

### Files are where exceptions become unavoidable

Every file operation can fail for a reason the program cannot prevent, which is why the syllabus pairs the two topics and why every Paper 4 file question ends with the sentence *the function uses exception handling when opening and reading from the file*. The pattern that earns the mark, and survives contact with a missing file, is the one the June 2024 examiners had to spell out after watching candidates get it wrong:

```python
def read_data(filename):
    records = []
    try:
        f = open(filename)                 # the open is INSIDE the try ...
        for line in f:
            records.append(parse_line(line))
        f.close()                          # ... and so is the close
    except FileNotFoundError:
        print("Cannot open file", filename)
    return records
```

Put `f.close()` *after* the `except` and the handler runs, prints its message — and then the program crashes anyway, because `f` was never assigned and there is nothing to close. Demo 5 in `exception-handling-demo.py` reproduces exactly that second crash. The honest modern form makes the close impossible to forget:

```python
def read_data(filename):
    records = []
    try:
        with open(filename) as f:          # closed on exit — normal or by exception
            for line in f:
                try:
                    records.append(parse_line(line))
                except ValueError as e:    # one bad line does not sink the file
                    print("skipped:", line.strip(), "-", e)
    except OSError as e:                   # FileNotFoundError, PermissionError, disk gone
        print("Cannot read", filename, "-", e)
    return records
```

Two handlers at two depths, because two decisions live at two depths: a bad *line* is decided per line (skip it, keep the rest), a missing *file* is decided per file (nothing to read). That nesting is the "when it is appropriate" bullet made concrete.

### Check first, or try and recover?

There is always a temptation to test before acting — `if os.path.exists(filename): open(filename)` — and it feels safer. It is not airtight: between the check and the act, the file can be removed by another program, a sync client, a user. Demo 8 shows the check pass and the open fail in the same millisecond. Only `try` around the act itself covers the gap, which is why "ask forgiveness, not permission" is the working idiom for anything outside the program's own memory. Checking first is still right for what the program *does* control — its own array bounds, its own menu choices — because a check there is a *design* decision, not a race against the world.

## Where this is the working tool

- **Every database is a random file.** SQLite stores a whole database in one file of fixed-size pages (4,096 bytes by default); reading row 40,000 is *hash or B-tree → page number → seek to page × 4096 → read one page*, which is this card's `SEEK` and `GETRECORD` with a better address calculator. [[Relational Databases]] begin exactly where this card ends: when one file of records needs several keys, several users, and a guarantee about crashes.
- **Every log is a serial file.** Web-server logs, git's reflog, Kafka's topics, the write-ahead log a database appends to before it dares touch its pages — all append-only, all read from the top when something has to be reconstructed.
- **The nightly batch still runs.** Banks, payroll bureaux and tax authorities still process the day's transactions against a sorted master in a merge pass — much of it in COBOL, because the algorithm has not needed to change since the 1960s.
- **Your web server's last line of defence is a handler.** An unhandled exception in a request would kill the process; the framework's outermost `try` turns it into an HTTP 500 and a log entry, and the other thousand users never notice. The handler sitting *above* all the code is exception handling's most common shape.
- **Ariane 5, flight 501.** The unhandled-exception story in [[Program Development Life Cycle and Testing]] is also an exception-*handling* story: the conversion overflow raised an exception, and the handler's specified policy was to shut the inertial reference unit down — sensible for a hardware fault, fatal for a software one. Both units followed the policy; the rocket flew on diagnostic data. The lesson is the "when appropriate" bullet at scale: a handler is a *decision*, and the wrong decision handles the exception straight into the ground.
- **Languages still argue about it.** Java makes some exceptions *checked* — the compiler refuses code that does not declare or catch `IOException`. Go returns errors as ordinary values and makes you look at them. Rust's `Result` type makes an unchecked error a compile-time failure. All three are answers to the same complaint about the silent `-1` return, and all three agree with this card on the one thing that matters: a failure must not be ignorable.

## Hands-on

Three scripts sit beside this card and are the evidence for everything above:

- **`file-processing-records.py`** — the fixed-length record, the serial and sequential operations (including the master–transaction merge), and the random-file engine with probing and tombstones, fuzzed against a `dict`. Change `FMT` and watch every slot address move with it.
- **`file-processing-benchmark.py`** — the scan-versus-seek timings and the figure above. Try a key near the front of the file and watch the serial line drop; the seek line will not move.
- **`exception-handling-demo.py`** — eight claims about exceptions, each run and checked: the halt, the catch two frames up, `finally` after `return`, `with` closing on error, the examiner's close-outside-the-try crash, the bare `except:` swallowing Ctrl-C, a user-defined exception, and the check-then-act race.

## Worked examples — every one a real paper

### Example 1 (November 2023 Paper 31 Q8, 8 marks) — a record from a random file, and two definitions

> *A pseudocode algorithm finds a customer account record in a random file and outputs it. Records use `TAccount` (AccountNumber, LastName, FirstName, Address, ContactNumber). `Hash()` takes the account number and returns the hash value. Complete the pseudocode* [5]. *(b) Define the term exception handling* [1]. *(c) State two possible causes of an exception* [2].

*Tool: the random-file lifecycle — open for RANDOM, compute the address, SEEK, GETRECORD, close. Trigger: "random file" plus a `Hash()` function in the stem — the address is computed, not searched for.*

```
AccountFile ← "AccountRecords.dat"
OPENFILE AccountFile FOR RANDOM
OUTPUT "Please enter an account number"
INPUT Customer.AccountNumber
Location ← Hash(Customer.AccountNumber)
SEEK AccountFile, Location
GETRECORD AccountFile, Customer
OUTPUT Customer
CLOSEFILE AccountFile
```

Five blanks, five marks: the assignment of the filename, `FOR RANDOM`, the argument of `Hash` (the key field of the record just typed), the file in `SEEK`, and `GETRECORD` with the record variable. In Python the same nine lines are `rf = RandomFile("AccountRecords.dat", slots)`, `rf.seek(rf.hash(number))`, `rf.get_record()`.

**(b)** *Responding to an unexpected event while the program is running so that it does not halt unexpectedly.* **(c)** Any two of: programming errors, user errors, hardware failure, run-time errors.

### Example 2 (November 2023 Paper 32 Q12(b), 7 marks) — searching a random file by a non-key field

> *A pseudocode algorithm searches for a customer record in a random file `AccountRecord.dat` by the customer's **name**. `MaxSize` is 1000. If found, output the record; otherwise an error message.*

*Tool: a bounded linear search with a found-flag, driven by `SEEK` + `GETRECORD` at each location. Trigger: the search key is the name, and the file is hashed on the account number — the hash is useless here, so the only option is to visit every location.*

```
OPENFILE "AccountRecord.dat" FOR RANDOM
Location ← 1
FoundFlag ← FALSE
OUTPUT "Enter the customer's name"
INPUT SearchCustomer
WHILE NOT FoundFlag AND Location <= MaxSize
    SEEK "AccountRecord.dat", Location
    GETRECORD "AccountRecord.dat", Customer
    IF SearchCustomer = Customer.Name THEN
        OUTPUT "Customer found: "
        OUTPUT Customer
        FoundFlag ← TRUE
    ENDIF
    Location ← Location + 1
ENDWHILE
IF NOT FoundFlag THEN
    OUTPUT "Customer does not exist."
ENDIF
```

The question is quietly making Part II's point: a random file is only fast for the key it was hashed on. Search it by anything else and it is a serial file with extra steps — a thousand seeks and a thousand reads. A real system would keep a second index on the name, which is the moment a file becomes a database.

### Example 3 (June 2026 Paper 41 Q2(b)(i), 8 marks) — records from a text file with exception handling

> *`Toys.txt` stores 16 toys, one per line: `Fire Station,3981,Expert,Town`. `ReadData()` takes an array of `ToyRecord`, opens the file, creates a record for each line, stores each in the array and returns it. The function uses exception handling when opening and reading from the file.*

*Tool: the read-split-cast-append loop inside a `try`. Trigger: "uses exception handling when opening and reading" — so the `open` goes inside the `try`, and the scheme's own words are "all file handling inside try".*

```python
def ReadData(TheToys):
    try:
        with open("Toys.txt") as TheFile:                       # open + close inside the try
            for Line in TheFile:                                # until EOF — 16 lines
                Name, Bricks, Difficulty, Category = Line.strip().split(",")
                TheToys.append(ToyRecord(Name, int(Bricks), Difficulty, Category))
    except (OSError, ValueError) as e:
        print("Cannot read Toys.txt:", e)                       # suitable output
    return TheToys
```

Marks, one each: the header with the parameter and the return; exception handling with suitable output *and all file handling inside the try*; opening the file; closing it in an appropriate place (the `with` does it); looping until EOF or 16 times; splitting on the comma and removing the newline; creating the record; appending it. The published Python uses a bare `except:` and an explicit `TheFile.close()` inside the `try`; both earn the marks, and both are the exam's convenience rather than the real world's habit — name the classes and let `with` close.

### Example 4 (June 2025 Paper 41 Q2(c), 5 marks) — appending to a file with exception handling

> *`StoreData()` takes a 1D array and a filename, opens the file, appends each item on a new line, and uses exception handling when opening and writing.*

*Tool: append mode plus the write-then-newline pair, inside a `try`. Trigger: "appends" — mode `"a"`, never `"w"`, or the file is wiped every call.*

```python
def StoreData(DataToStore, FileName):
    try:
        with open(FileName, "a") as File:          # APPEND: pointer starts at the end
            for Item in DataToStore:
                File.write(str(Item) + "\n")       # the newline is a mark on its own
    except OSError as e:
        print("Cannot create or write to file:", e)
```

The five marks are the header with both parameters plus open-for-append and close, the loop, the write, the newline between lines, and try/except with suitable output. The VB.NET model answer in the scheme opens the file *before* the `Try` — which the June 2024 report had warned against a year earlier; the Python one does it right.

### Example 5 (Paper 3 theory — June 2022 Paper 32 Q9, 4 marks; November 2025 Paper 33 Q12, 5 marks)

> *State the reasons for including exception handling routines when writing a program. Include an example of an exception.* [4]

Three reasons and an example: **to trap run-time errors**; **to prevent the program halting unexpectedly**; **to produce a meaningful error message** instead of a traceback; example — *division by zero, end of file, file not found*. The examiners' report for this paper records that the common wrong answer was a description of **interrupt handling** — a hardware signal to the processor, handled by the operating system, from [[Interrupt Handling]]. An exception is a *software* event inside one program, handled by that program's own code.

> *(a) Explain what is meant by an exception.* [3] *(b) Identify one example and give one reason why it may cause a problem.* [2]

**(a)** An exception is an unplanned event that occurs while a program is running; it arises from an error — in programming or logic, or in the data or environment — that was not detected during construction or compilation; its effect, if unhandled, is that the program halts unexpectedly. **(b)** *Division by zero — the processor cannot produce a value for it, so without a handler the program crashes at that line.*

### Example 6 (June 2024 Paper 41 Q2(b), 7 marks) — "raises an exception if the file is not found"

> *`ReadData()` creates an array of type `Tree`, reads the data from `Trees.txt`, **raises an exception if the file is not found**, creates an object per line, appends and returns.*

*Trigger: the wording says "raises", but the mark point is "appropriate use of exception handling, with catch and output".* The `open` already raises `FileNotFoundError` on its own; what the mark wants is that your code **catches** it and says so. The pattern is Example 3's with a `Tree(...)` constructor and three `int()` casts. If a question genuinely wanted you to raise, the line is `raise FileNotFoundError(f"{filename} is missing")` — and something further up must catch it, or the program halts exactly as before.

## Common misconceptions (teaching notes)

### 1. "Exception handling is interrupt handling"
The examiners named this as *the* common wrong answer. An interrupt is a hardware signal that makes the *processor* suspend the current program so the *operating system* can service a device. An exception is a *software* event inside one program, raised and caught by that program's own code. The word "handling" is the only thing they share.

### 2. "try/except makes the error go away"
It moves the *decision*. The file is still missing; the line is still `ten`. A handler that prints nothing and carries on has not handled anything — it has hidden a failure that will surface later, further from its cause. Every `except` must do one of: report, recover, retry, or re-raise.

### 3. "Close the file after the except, to be tidy"
If `open` failed, there is no file object to close, and the tidy-up line crashes the program the handler just saved. Open *and* close inside the `try` — or use `with`, which closes on every exit path.

### 4. "A random file stores records in random order"
Every position is computed from the key; nothing is left to chance. The order looks scrambled only because a good hash scatters. The examiners' guidance explicitly refuses "random" as the *description* of random organisation — say *computed from the key by a hashing algorithm*.

### 5. "Serial and sequential are the same thing"
Both are read from the top. Only a sequential file is in **key order** — which is what lets a search stop early and lets an index give direct access. A serial file has *arrival* order and nothing else.

### 6. "Exceptions are for bugs"
A bug is fixed, not caught. Exception handling is for the failure the program could not prevent — the world's input, the world's hardware. Catching an `IndexError` from your own off-by-one loop hides a fault that testing should have exposed.

## Beyond syllabus

> [!info] Beyond syllabus — the file that outgrows one key
> Hashing gives one fast key. Real records are looked up by several — account number *and* name *and* postcode — and a hashed file answers only the first. The classic fix was **indexed sequential** organisation: a sorted master with a separate index per key. Its modern form is the **B-tree**, a [[Balanced Trees]] structure with nodes the size of a disk page, so that any key reaches its record in three or four page reads whatever the file's size — and *in order*, which hashing can never give. Every relational database's index is one.

> [!info] Beyond syllabus — `with`, and what a context manager guarantees
> `with open(f) as h:` is a `try/finally` written for you: whatever happens in the block, `h.close()` runs on the way out. The same shape guards database transactions (`with conn:` commits or rolls back), locks (`with lock:` always releases), and temporary directories. C++ calls the idea RAII — resource acquisition is initialisation — and enforces it with destructors; Java's `try-with-resources` is the same promise. The principle: **a resource's release should be impossible to forget**, which no amount of remembering to call `close()` achieves.

> [!info] Beyond syllabus — what an exception costs
> In Python, entering a `try` block costs almost nothing and raising an exception costs a few microseconds — cheap enough to use for control flow (`for` loops stop on a `StopIteration` exception). C++ made the opposite trade: a `try` is free, a `throw` is expensive, so exceptions are reserved for the exceptional. Java's checked exceptions and Rust's `Result` push the question to the compiler. There is no consensus, only the shared conviction that the *silent* failure — the ignored return code — is the one design everybody has agreed to abandon.

## Exam Notes

### Cambridge 9618 (A Level)

**§20.2 File Processing and Exception Handling**, A2 content, examined on **Paper 3** (theory, with pseudocode fill-in questions) and on **Paper 4** (where almost every practical scenario opens a file and every recent one asks for exception handling around it). §13.2 file organisation — serial, sequential, random, hashing — is examined alongside it on Paper 3, and [[Hash Tables]] carries that half.

- **Paper 3 definitions come from the schemes' own words.** *Exception*: an event during execution that disrupts the normal flow / an unplanned event that causes the program to halt unexpectedly. *Exception handling*: responding to an unexpected event while the program is running so that it does not halt unexpectedly. *Causes* (two marks, any two): programming errors, user errors, hardware failure, run-time errors — with examples such as divide by zero, out-of-bounds index, file not found, wrong data type. *Avoiding termination*: use an exception-handling routine — `try … except` / `catch` — and generate an error message. Questions have been set in November 2023 (31 and 33 Q8, 32 Q12), June 2022 (32 Q9) and November 2025 (31 Q10, 32 Q10, 33 Q12).
- **Paper 3 pseudocode fill-ins use the random-file dialect**: `OPENFILE F FOR RANDOM`, `SEEK F, Address`, `GETRECORD F, Rec`, `PUTRECORD F, Rec`, `CLOSEFILE F` — June 2025 Paper 31 Q12 (a stock file of 500 locations) and both November 2023 questions above. The address is usually `Hash(key)`; the pseudocode guide says explaining *how* addresses are computed is good practice.
- **Random organisation as prose**: June 2026 Paper 31 Q2 asked for a use (booking systems, an operating system's file management, video games — *not* a database management system, which the stem had already given), how records are organised (no particular order; position determined from the key by a hash; new records placed in an empty location), and the find process (direct access; hash the key; retrieve if found, else follow the collision policy). June 2024 Paper 32 Q7 contrasted direct access to a **sequential** file (an index of key fields is kept and searched) with a **random** file (the hash is applied).
- **Paper 4's standing sentence** — *the function uses exception handling when opening and reading from the file* — carries one mark of the question, and the scheme's guidance is explicit: **all file handling inside the `try`**, with suitable output in the handler. Opening and closing the file, looping to EOF, splitting and casting, building the record or object, and appending to the array are the other marks. Set in June 2026 (41, 42, 43), June 2025 (41 Q2(c), appending), November 2025 (42 Q3(d), writing), November 2024 (42), June 2024 (41 — phrased as "raises an exception"), June 2023 (41).
- **The examiners' recurring complaints**: closing the file *outside* the `try` (impossible if the open failed — June 2024); not closing the file at all (June 2021–2024, every report); reading in ways that ignore EOF. The June 2023 report praised candidates who used exception handling to *detect data type* — trying `int()` on a field to tell a manager's bonus from an employee's blank — as the stronger approach.
- **Paper 4 accepts a bare `except:`** and prints its model answers with one. It also accepts `except Exception`. Write the named class when you know the cause; nothing is lost and the code is honest.
- **Paper 4 has never asked for a random file** — every practical file has been a text file, one record per line — and Java, VB.NET and Python are all allowed. The random-file commands are Paper 3 pseudocode only.

### Cambridge 0478 (IGCSE)

**Not examined.** §8.3 covers opening, reading, writing and closing a text file, and [[File Handling]] carries it. The syllabus contains no exception handling and no file organisation.

### Where this is *not* examined

**AP Computer Science A** names specific exceptions — `ArrayIndexOutOfBoundsException`, `NullPointerException`, `ArithmeticException`, `InputMismatchException` — as run-time errors a student should recognise, along with `StringIndexOutOfBoundsException`, `IndexOutOfBoundsException` and `ConcurrentModificationException`. It has **no `try`/`catch`**: a method that reads a file declares `throws IOException` and handles nothing. It does examine **reading a text file** with `File` and `Scanner` (topic 4.6 of the course effective Fall 2025), which [[File Handling]] carries; writing files is outside it. **IB Computer Science** credits B2.5 File processing to [[File Handling]], and **names exception handling as its own statement, B2.1.3**: the points where a program can fail (unexpected input, an unavailable resource, a logic error) and the `try`/`except`/`finally` construct, which is Part III of this card. Serial, sequential and random *organisation* is examined nowhere but 9618.

## Connections

- **Built on:** [[File Handling]] — the lifecycle, modes, EOF and the serialisation problem this card takes from lines to records; [[Hash Tables]] — the hashing, probing and tombstones that a random file lifts onto disk, and §13.2's organisation-and-access theory; [[User-Defined Data Types]] — the `TYPE … ENDTYPE` record that is the unit of every file operation here; [[Program Development Life Cycle and Testing]] — the run-time error as the third kind of error, and the testing that catches the errors exceptions must not hide.
- **Contrast:** [[Interrupt Handling]] — the hardware signal handled by the operating system, which is what an exception is *not*; [[Balanced Trees]] — the B-tree as the ordered alternative to the hashed file.
- **Same shape elsewhere:** [[Stacks and Queues]] — the call stack an exception unwinds is a stack, and the frames it discards are pops; [[Recursion]] — the same stack, growing in the other direction.
- **Extends into:** [[Relational Databases]] — one file of records that has grown several keys, several users and a crash guarantee; [[File Systems]] — how the operating system turns a filename into the blocks these seeks land on; [[Operating Systems]] — the directory entry, the open-file table, and the kernel's own handling of a faulting process.
- **Exam dialect:** [[Cambridge Pseudocode]] — `OPENFILE … FOR RANDOM`, `SEEK`, `GETRECORD`, `PUTRECORD`, alongside the text-file commands.

## Quick reference

| Organisation | write | find one by key | find one by another field | best for |
|---|---|---|---|---|
| Serial | append, $O(1)$ | scan, $O(n)$; missing key = whole file | scan | logs, transaction files, backups |
| Sequential | merge master + sorted transactions into a new file | scan, stops when keys pass; index gives direct access | scan | batch processing of every record |
| Random | hash → seek → write, $O(1)$ | hash → seek → read, $O(1)$ (plus probes) | scan of every slot | one record, now |

| Python | meaning |
|---|---|
| `try:` | the region whose failure is expected |
| `except ValueError as e:` | one policy for one cause; `e` carries the message |
| `except (OSError, ValueError):` | several causes, one policy |
| `else:` | only if nothing was raised |
| `finally:` | on every path, even after `return` |
| `raise SomeError("why")` | report from the detection point |
| `with open(f) as h:` | `try/finally` with `h.close()` built in |

## Sources

- Cambridge International AS & A Level Computer Science 9618, syllabus for 2027–2029, §20.2 (p. 38); Pseudocode Guide for Teachers 2027–2029, §9.1 text files and §9.2 random files.
- 9618 Paper 3: June 2022/32 Q9; November 2023/31 and /33 Q8, /32 Q12; June 2024/32 Q7; June 2025/31 Q12; November 2025/31 Q10, /32 Q10, /33 Q12; June 2026/31 Q2 — with their published mark schemes and the examiners' reports for June 2022 and November 2023.
- 9618 Paper 4: June 2023/41 Q3(b)(iii); June 2024/41 Q2(b); November 2024/42 Q3(b); June 2025/41 Q2(c); November 2025/42 Q3(d); June 2026/41 Q2(b)(i), /42 and /43 — with their mark schemes and the examiners' reports for June 2021–2024.
- The three scripts beside this card: `file-processing-records.py`, `file-processing-benchmark.py`, `exception-handling-demo.py`; the figures `file-processing-organisations.svg`, `file-processing-seek-vs-scan.svg`, `exception-stack-unwind.svg`; the animation `file-processing-manim.py`.
- J. L. Lions et al., *Ariane 5 Flight 501 Failure — Report by the Inquiry Board* (1996), for the exception-handler policy that shut down both inertial reference units.
