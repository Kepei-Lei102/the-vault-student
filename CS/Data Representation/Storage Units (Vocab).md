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

- **位 (bit)** = 1 个二进制位（0 或 1）；**半字节 (nibble)** = 4 位；**字节 (byte)** = 8 位——存储的基本单位。
- 两套阶梯：**十进制**（kilo/mega/giga/tera，每级 ×1000，硬盘厂商用）和**二进制**（kibi/mebi/gibi/tebi，每级 ×1024 = $2^{10}$，操作系统和考试用）。
- 考试写法：**KiB、MiB、GiB、TiB、PiB、EiB**，全部按 1024 进位。
- 文件大小 = 数据量的算术：图像 = 宽 × 高 × 色深；声音 = 采样率 × 位深 × 声道 × 时长。

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

**Why two ladders exist:** hardware addresses memory in powers of $2$, and by lucky coincidence $2^{10} = 1024 \approx 10^3$ — so engineers borrowed the metric prefix "kilo" for 1024 and the ambiguity was born. The *-bi-* prefixes (kibi = "kilo binary," 1998) exist to end it: **Cambridge requires the binary ladder, written KiB/MiB/GiB/…, stepping by 1024.**

> [!info] The case of the missing gigabytes
> Buy a "1 TB" drive and your computer reports **931 GB**. Nothing is missing: the manufacturer sold you $10^{12}$ bytes (decimal ladder — bigger-sounding numbers sell drives), and your OS divides by $2^{30}$ to display GiB: $10^{12} / 2^{30} = 931$ GiB — then labels it "GB" anyway. Same bytes, two treaties, one very common lawsuit. The kibi/kilo distinction is consumer protection in disguise.
>
> *"So my SSD loses gigabytes the same way?"* — the display story is identical (decimal sticker, binary OS), but the SSD hides a better twist. Flash chips are *manufactured* on the binary ladder — a "512 GB" SSD physically contains 512 **GiB** ≈ 550 decimal GB of raw flash. The ≈ 7% between the silicon and the sticker isn't lost either: the controller keeps it as **over-provisioning**, a private reserve of spare blocks it uses to keep the drive fast and alive — the story [[Secondary Storage]] tells. On an HDD the gap is bookkeeping; on an SSD it's a workshop.

## File-size arithmetic

A file's size is just multiplication — *count the numbers being stored*:

$$\textbf{image} = \text{width} \times \text{height} \times \text{colour depth} \qquad \textbf{sound} = \text{sample rate} \times \text{bit depth} \times \text{channels} \times \text{seconds}$$

**Worked — a 1080p photo, uncompressed.** $1920 \times 1080$ pixels $\times\ 24$ bits ($3$ B) per pixel $= 6{,}220{,}800$ B $= 6{,}220{,}800 / 2^{20} \approx \mathbf{5.93}$ **MiB**. (Why the terms mean what they mean: [[Image Encoding]].)

**Worked — a 3-minute CD-quality song.** $44{,}100$ samples/s $\times\ 16$ bits ($2$ B) $\times\ 2$ channels $\times\ 180$ s $= 31{,}752{,}000$ B $\approx \mathbf{30.3}$ **MiB**. (Why 44,100 of all numbers: [[Sound Encoding]].)

Your actual photos and songs are far smaller than these — that gap is [[Compression]] doing its work.

## Exam Notes

**0478 §1.3.1–1.3.2:** know the ladder bit → nibble → byte → KiB → MiB → GiB → TiB → PiB → EiB, **all steps ×1024**; calculate file sizes with the two formulas above and convert the answer into sensible units (divide by $1024$ per step). Show the multiplication *in bits or bytes first*, convert last — unit-mixing (bits vs bytes, ×1000 vs ×1024) is the classic dropped mark.

**9618 §1.1:** the syllabus asks explicitly for the **difference between binary and decimal prefixes** — kibi vs kilo, mebi vs mega, gibi vs giga, tebi vs tera — i.e. know *both* ladders and which is which, not just the binary one.

**IB CS:** not a named statement — A1.2's confirmed wording covers binary/hexadecimal conversion, not storage units or prefixes. The ladder still earns its keep the moment any IB scenario quotes a file size.

**AP CSA:** not examined.

## Connections

- **Prerequisite:** [[Number Bases]] — $2^{10}$, $2^{20}$, $2^{30}$ are just place value climbing in chunks of ten binary digits; one nibble = one hex digit.
- **Mathematics:** [[Logarithms]] — the whole kibi/kilo confusion exists because $\log_{10} 2 \approx 0.301$, so ten doublings land *almost* on three decades: $2^{10} = 1024 \approx 10^3$. A near-miss in logarithms became an industry's ambiguity.
- **Used by:** [[Sound Encoding]] and [[Image Encoding]] — the file-size formulas are those cards' parameters multiplied out; [[Text Encoding]] — one byte per ASCII character is the smallest sizing rule of all.
- **Sequel:** [[Compression]] — the reason real files undercut every calculation on this page.
- **The gap put to work:** [[Secondary Storage]] — on an SSD the binary-silicon-vs-decimal-sticker difference becomes **over-provisioning**, the controller's hidden workshop for wear levelling and block repair.
