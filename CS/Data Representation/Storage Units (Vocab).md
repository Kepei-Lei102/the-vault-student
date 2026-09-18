---
chinese: 存储单位 (cúnchǔ dānwèi)
prerequisites:
  - "[[Number Bases]]"
leads_to:
  - "[[Sound Encoding]]"
  - "[[Image Encoding]]"
tags:
  - subject/computer-science
  - domain/data-representation
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/0478-1-3
  - syllabus/9618-1-1
  - type/vocab
  - type/definition
  - notation/binary
  - misconception/kilo-is-always-1000
---

# Storage Units (Vocab) 存储单位

> *Two ladders climb from the byte: the shopkeeper's (×1000) and the engineer's (×1024). They look alike, they're both called "kilo-something," and the gap between them is where your missing gigabytes went.*

## 中文锚点


买来的硬盘标着 1 TB，有的软件却显示约 931 GiB，乍看像少了一块。先想想同一批鸡蛋：每盒装得多一点，盒数就会少一点，鸡蛋并没有少。TB 和 GiB 也是在用不同大小的“盒子”数字节；同样一万亿字节，换个单位，数字就变了。光是换算单位不会吃掉容量，系统文件实际占用空间则是另一回事。

## The units

| Unit | Size | |
|---|---|---|
| **bit** (b) | one binary digit, $0$ or $1$ | the atom |
| **nibble** | $4$ bits | one hex digit ([[Number Bases]]) |
| **byte** (B) | $8$ bits | one ASCII character ([[Text Encoding]]) |

Above the byte, **two ladders** — same prefixes-sound, different step size:

| Binary (×1024) | Value | Decimal (×1000) | Value |
|---|---|---|---|
| **KiB** kibibyte | $2^{10}$ B $= 1024$ B | kB kilobyte | $10^3$ B |
| **MiB** mebibyte | $2^{20}$ B | MB megabyte | $10^6$ B |
| **GiB** gibibyte | $2^{30}$ B | GB gigabyte | $10^9$ B |
| **TiB** tebibyte | $2^{40}$ B | TB terabyte | $10^{12}$ B |
| **PiB** pebibyte | $2^{50}$ B | PB petabyte | $10^{15}$ B |
| **EiB** exbibyte | $2^{60}$ B | EB exabyte | $10^{18}$ B |

**Why two ladders exist:** hardware addresses memory in powers of $2$, and by lucky coincidence $2^{10} = 1024 \approx 10^3$ — so engineers borrowed the metric prefix "kilo" for 1024 and the ambiguity was born. The *-bi-* prefixes (kibi = "kilo binary," 1998) exist to end it: **0478 requires the binary ladder, written KiB/MiB/GiB/…, stepping by 1024; 9618 explicitly distinguishes this from the decimal ladder.**

> [!info] The case of the missing gigabytes
> A drive advertised as **1 TB** contains $10^{12}$ advertised bytes. Express that same quantity in binary units and you get $10^{12}/2^{30}\approx931.3$ **GiB**. Some software labels this binary number “GB”; other software uses decimal units. **The display convention depends on the system and tool**, not a universal rule that all operating systems count in binary. The unit conversion itself removes no bytes. Formatting, partitions and installed software affect available space separately. [Apple's explanation of capacity units](https://support.apple.com/en-gb/102119)
>
> An SSD may also reserve physical capacity for controller work such as garbage collection and wear management: **over-provisioning**. Its amount depends on the drive and configuration; a “512 GB” label alone does not prove exactly 512 GiB of raw flash or a universal 7% reserve. Unit conversion and reserved capacity are distinct explanations. [[Secondary Storage]] develops the controller's job. [Samsung's over-provisioning explanation](https://semiconductor.samsung.com/resources/others/Samsung_SSD_845DC_04_Over-provisioning.pdf)

## File-size arithmetic

A file's size is just multiplication — *count the numbers being stored*:

$$\textbf{image} = \text{width} \times \text{height} \times \text{colour depth} \qquad \textbf{sound} = \text{sample rate} \times \text{bit depth} \times \text{channels} \times \text{seconds}$$

**Worked — a 1080p photo, uncompressed.** $1920 \times 1080$ pixels $\times\ 24$ bits ($3$ B) per pixel $= 6{,}220{,}800$ B $= 6{,}220{,}800 / 2^{20} \approx \mathbf{5.93}$ **MiB**. (Why the terms mean what they mean: [[Image Encoding]].)

**Worked — a 3-minute CD-quality song.** $44{,}100$ samples/s $\times\ 16$ bits ($2$ B) $\times\ 2$ channels $\times\ 180$ s $= 31{,}752{,}000$ B $\approx \mathbf{30.3}$ **MiB**. (Why 44,100 of all numbers: [[Sound Encoding]].)

These formulas count uncompressed pixel or sample data, excluding headers and metadata. Compressed files may be much smaller; actual size depends on the format and content. [[Compression]] explains the trade.

## Exam Notes

**0478 Paper 1, §1.3.1–1.3.2:** know the ladder bit → nibble → byte → KiB → MiB → GiB → TiB → PiB → EiB, **1 nibble = 4 bits; 1 byte = 8 bits; each prefix step from byte upwards is ×1024**; calculate file sizes with the two formulas above and convert the answer into the units requested by the question (divide by $1024$ per step). Show the multiplication *in bits or bytes first*, convert last — unit-mixing (bits vs bytes, ×1000 vs ×1024) is the classic dropped mark.

**9618 AS Paper 1, §1.1:** the syllabus asks explicitly for the **difference between binary and decimal prefixes** — kibi vs kilo, mebi vs mega, gibi vs giga, tebi vs tera — i.e. know *both* ladders and which is which, not just the binary one.

**IB CS (first assessment 2027):** A1.2.1 names integer representations and conversions; A1.2.2 explicitly includes binary storage of integers, strings, characters, images, audio and video. The full guide does **not explicitly prescribe the KiB–EiB prefix ladder**. Distinguish that narrow absence from claiming data storage itself is absent; units remain useful supporting knowledge.

**AP CSA (2025–26 CED):** binary/decimal storage-prefix conversions and image/audio file-size calculations are not named required outcomes. Java numeric limits are relevant elsewhere; do not interpret this as “memory sizes never matter.”

## Connections

- **Prerequisite:** [[Number Bases]] — $2^{10}$, $2^{20}$, $2^{30}$ are just place value climbing in chunks of ten binary digits; one nibble = one hex digit.
- **Mathematics:** [[Logarithms]] — the whole kibi/kilo confusion exists because $\log_{10} 2 \approx 0.301$, so ten doublings land *almost* on three decades: $2^{10} = 1024 \approx 10^3$. A near-miss in logarithms became an industry's ambiguity.
- **Used by:** [[Sound Encoding]] and [[Image Encoding]] — the file-size formulas are those cards' parameters multiplied out; [[Text Encoding]] — one byte per ASCII character is the smallest sizing rule of all.
- **Sequel:** [[Compression]] — the reason real files undercut every calculation on this page.
- **The gap put to work:** [[Secondary Storage]] — reserved capacity helps the controller with wear management and block maintenance; distinguish it from merely expressing the same byte count in different units.
