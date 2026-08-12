---
chinese: 图像编码 (túxiàng biānmǎ)
prerequisites:
  - "[[Number Bases]]"
  - "[[Text Encoding]]"
  - "[[Storage Units (Vocab)]]"
leads_to:
  - "[[Compression]]"
tags:
  - subject/computer-science
  - domain/data-representation
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/0478-1-2
  - syllabus/9618-1-2
  - type/deep
  - type/definition
  - notation/binary
  - notation/hexadecimal
  - misconception/zoom-and-enhance
  - misconception/vector-is-always-better
---

# Image Encoding 图像编码

> *A bitmap remembers what the world looked like; a vector remembers what the artist did. One stores samples, the other stores intentions — and everything about digital images follows from that split.*

Zoom into any photo, far enough, and it shatters into coloured squares. Now zoom into this sentence — crisp at 400%, crisp at 4000%. Same screen, same pinch gesture, two completely different fates. Why does a photograph run out of detail while a letterform never does? Because the two are *remembered differently* — and by the end of the ride you'll know exactly what each one wrote down.

## 中文锚点

**图像编码 (túxiàng biānmǎ)** = image encoding：把一幅图变成数字的两种哲学——

- **位图 (bitmap / 点阵图)** —— 把画面切成网格，每个**像素 (pixel)** 存成一个数字。**分辨率 (resolution)** = 宽 × 高（网格多细）；**色深 (colour depth / bit depth)** = 每个像素几位（颜色多准）。文件大小 = 宽 × 高 × 色深。照片就是位图：相机对现实**采样**。
- **矢量图 (vector graphic)** —— 不存像素，存**画图的指令**：绘图列表 (drawing list) 里一串绘图对象 (drawing object)，每个对象带属性 (property)（圆心、半径、颜色……）。缩放 = 重新执行指令，所以**永不模糊**——字体、logo、还有本库所有示意图（SVG）都是矢量。
- 关键对比：位图放大会**糊**（样本就那么多），矢量放大**重算**（指令与大小无关）。照片没有"配方"，只能位图；设计出来的形状有配方，矢量更优。

---

## The bitmap — a picture is a grid of numbers

Cut the picture into a grid. Each cell is a **pixel** (*picture element*) — the atom of the image, one flat colour. Store one number per pixel, and the picture *is* the list of numbers. Start at the smallest possible scale — **1 bit per pixel**, black or white:

![[image-encoding-bit-grid.svg|697]]

Read the left side and you have read a file; render it and you have seen a picture. There is no magic layer in between — **the numbers are the picture.** Everything else in this topic is just two questions about that grid:

1. **How fine is the grid?** — resolution.
2. **How many bits per cell?** — colour depth.

### Colour — why every pixel is three numbers

One bit gives black/white; $8$ bits give $256$ grey levels. For colour, the format was decided not by engineers but by **your retina**: human eyes sense colour through just **three** cone types (roughly red-, green- and blue-sensitive), so any colour *you can perceive* can be faked by mixing three primaries. The screen doesn't reproduce the light of the scene — it reproduces **your eye's three-number report** of that light.

Hence **RGB**: one byte each for red, green, blue — $3$ bytes $= 24$ bits per pixel, called **true colour**, $2^{24} = 16{,}777{,}216$ mixes (more than the eye can tell apart). And you have already met this format: a web colour like `#2563EB` is *literally the three bytes of one pixel* written in hex — `25` red, `63` green, `EB` blue ([[Number Bases]] cashing in). A fourth byte, **alpha** (transparency), gives the 32-bit pixel that screens and PNGs actually push around.

### Resolution and colour depth — the two quality dials

- **Image resolution** = the grid's size, width × height in pixels ($1920 \times 1080$; a "12-megapixel" photo is a grid of $\sim 12$ million cells). Distinct from **screen resolution** — the *display's* own grid; an image with more pixels than the screen can't show them all at once.
- **Colour depth (bit depth)** = bits per pixel: $1$ (line art), $8$ (greyscale or a 256-colour palette), $24$ (true colour), $32$ (+alpha).

> [!warning] One term, two industries
> A photographer's "10-bit colour" and a monitor's "8-bit panel" count bits **per channel** — multiply by $3$ for RGB ($30$ or $24$ bits per pixel). Computer science — and every exam board — counts bits **per pixel**. Same words, different bookkeeping: a Cambridge "24-bit" image *is* a photographer's "8-bit" one. When reading a spec sheet, check which treaty you're in.

> [!info] And the "8-bit style"? — the 8 that isn't a depth at all
> ![[image-encoding-8bit-style-cat.png|180]]
> The retro pixel-art look is named "8-bit" after the **CPUs of the 1980s consoles** — chips whose registers and data bus were one byte wide ([[CPU Architecture and the Fetch-Execute Cycle]]) — not after any image measurement. The irony is lovely: the NES, the era's icon, drew its sprites at **2 bits per pixel** (four values: three colours plus transparent, per palette) from a master palette of about $54$ colours. The chunky charm is the shadow of the *whole machine's* constraints — $8\times8$ tiles, a few tiny palettes, $256\times240$ pixels — and today it is an aesthetic worn by games running on 64-bit processors, usually breaking every rule the real hardware enforced. When "8-bit" *is* a literal image term, it means $256$ greyscale levels or a $256$-colour palette — the sense above, not the style.

Turn either dial down and the file shrinks — and the image degrades in its own characteristic way. Too few pixels: blockiness. Too few colours: smooth gradients collapse into visible stripes — **banding** (posterisation):

![[image-encoding-colour-depth.svg|680]]

And on a real photograph — the same sunset at **8, 4, and 2 bits per RGB channel** (that's $24$, $12$ and $6$ bits *per pixel*, in the exam's counting — the two bookkeepings from the warning above, side by side in one caption):

![[image-encoding-landscape-8bit.png|640]]
![[image-encoding-landscape-4bit.png|640]]
![[image-encoding-landscape-2bit.png|640]]

*At 4 bits per channel the sky begins to stripe; at 2 bits per channel ($4$ levels each, $64$ colours total) the sunset becomes a poster of itself — every smooth gradient snapped to the nearest of a handful of allowed colours.*

File size is the two dials multiplied ([[Storage Units (Vocab)]]):

$$\text{file size} \;=\; \text{width} \times \text{height} \times \text{colour depth} \;\; (+\ \text{a small header})$$

**Worked:** $1920 \times 1080$ at $24$-bit $= 6{,}220{,}800$ B $\approx 5.93$ MiB. Double *both* dimensions and triple the depth ($8 \to 24$): $4 \times 3 = 12\times$ the size — the dials multiply, which is why raw images balloon so fast.

> [!tip] "Wait — my phone's 4K photos are only about 4 MB?"
> Good catch. The formula says a $3840 \times 2160$ photo at $24$-bit must cost $3840 \times 2160 \times 3$ B $\approx 23.7$ MiB — yet your gallery reports a fifth of that. The formula is not wrong; **the saved file is not the raw grid.** The moment the camera writes the photo, the grid's massive redundancy — a blue sky is millions of near-identical pixels — gets squeezed out ([[Compression]]). Exam calculations always ask for the *uncompressed* size: the before picture, the honest cost of the grid itself. The gap between your answer and your gallery is an entire topic waiting.

> [!info] The file header — the treaty declaration
> The pixel bytes alone are a number soup: $6$ million bytes could be $1920\times1080$ at $24$-bit or $2560\times810$ at $24$-bit or $1920\times2160$ at $12$-bit. So every image file opens with a **file header**: a few dozen bytes stating the format, the width and height, the colour depth, and where the pixel data starts. It is the same lesson [[Text Encoding]] taught — *bytes do not announce their own meaning* — solved the same way: declare the treaty at the top of the file. And notice what makes the declaration *work*: every image reader on Earth honours it, every time, which is the only reason a photo from a stranger's camera opens instantly on your phone. A protocol is a promise kept — [[Credit Is the Currency]].

---

## Vector graphics — store the recipe, not the pixels

The bitmap stored the *result*. The other philosophy stores the *instructions*: a **vector graphic** is a **drawing list** — an ordered list of **drawing objects** (line, circle, rectangle, curve, text), each carrying **properties** (position, size, colour, stroke width). This is not exotic — every diagram in these notes is one, and you can open it in a text editor and *read* it:

```
<circle cx="60" cy="60" r="45" fill="none" stroke="#2563eb"/>
<text x="60" y="112">a circle, described — not sampled</text>
```

Fifty-ish bytes. The same circle as a $1080\times1080$ bitmap costs $3.3$ MB — *and still has jagged edges if you zoom.*

![[image-encoding-bitmap-vs-vector.svg|700]]

**Scaling is the killer difference.** Zoom a bitmap and the renderer can only stretch the samples it has — squares grow, edges staircase, detail *cannot* be recovered. Zoom a vector and the renderer **re-executes the recipe** at the new size: a circle of radius $45$ becomes a circle of radius $4500$, mathematically perfect at every scale. That is the answer to the opening riddle: **fonts are vector graphics** (each letterform is a little drawing list of curves), which is why text stays razor-sharp at any zoom while the photo beside it dissolves.

**When each wins** — the exam's "justify" skill, and it comes down to one question: *does a recipe exist?*

| | Bitmap 位图 | Vector 矢量 |
|---|---|---|
| Stores | samples (pixels) | instructions (drawing list) |
| Source | **measured** — cameras, scanners | **designed** — humans, software |
| Zoom | degrades (fixed samples) | perfect (recipe re-runs) |
| File size | fixed by resolution × depth, large | tiny for simple art; grows with *complexity*, not size |
| Editing | paint over pixels | change a property, re-render |
| Best for | photographs, scans | logos, fonts, diagrams, maps, UI icons |

A photograph *must* be a bitmap: the real world has no drawing list, so a camera can only **sample** it. A logo *should* be a vector: it was born as shapes, and storing the shapes keeps it perfect on a business card and on a billboard. (Trying to vectorise a photo means inventing millions of tiny objects — possible, enormous, and worse than the bitmap. "Vector is always better" is a mark-loser, not a fact.)

> [!info] A justification you are looking at right now
> Every schematic in these notes is a vector — open one in a text editor and you will find a drawing list you can read. That choice was made for exactly the two reasons this section teaches:
>
> 1. **Crisp on any device.** The same figure renders sharp on a phone, a projector, and a printed page — the recipe re-runs at whatever size the screen demands, so there is no "right resolution" to guess in advance.
> 2. **Exactness.** In a technical diagram, positions *are* claims: a curve must be the actual function, an angle the actual angle, a circuit junction exactly where the wires meet. A recipe **states** coordinates; a sampled image only approximates them. Where a picture must be *right*, vectors win — AI image generators have become astonishing painters, but they paint, they don't plot.
>
> And the comics in these notes? Raster, **on purpose**: warmth, texture, and molten lava have no drawing list. Choosing per figure — recipe where precision matters, paint where mood matters, both on one page when it earns it — is precisely the bitmap-vs-vector judgement this syllabus section asks you to make.

---

## Sampling in space — and the "enhance!" myth

Step back and the bitmap is something familiar: **sampling a continuous scene, in space**. The world has infinitely fine detail; the camera measures it at grid points and keeps only those measurements — exactly what sound recording does to a continuous wave *in time* ([[Sound Encoding]], where the idea gets its full theory). Resolution is a *spatial sampling rate*, and undersampling has visible symptoms: staircase **jaggies** on slanted edges, and the shimmering **moiré** patterns when you photograph a striped shirt or a screen — detail finer than the grid, misread as detail that isn't there.

> [!warning] "Zoom in and enhance"
> The crime-show move — zooming into a licence plate reflected in a sunglass lens and sharpening it to legibility — is a lie, and now you can say precisely why: **the information was never sampled.** A bitmap contains its measurements and nothing else; no algorithm can *recover* detail between the samples, because nothing was recorded there. (Modern AI "enhance" tools don't recover the missing pixels — they **invent** plausible ones. That's painting, not evidence, which is exactly why enhanced images are inadmissible in court.)

---

## Below the pixel — subpixels 亚像素

The pixel is the *image's* atom — but it is not the screen's, and not the simulation's. Two floors exist beneath it, and both are worth the visit:

**The screen's floor: a pixel is three lamps.** Physically, each pixel of an LCD or OLED panel is **three separate light strips** — red, green, blue, side by side. "White" is all three lit at once; you have never actually seen a white pixel, only three coloured strips too small to resolve. (Proof you can run tonight: put a tiny water droplet on a screen — it becomes a magnifying lens, and the strips appear.) And because the strips sit at *different horizontal positions*, text renderers exploit them: **subpixel rendering** (Microsoft's ClearType and its kin) lets a letter's edge land on a *third* of a pixel by lighting only the nearest strip — effectively tripling the horizontal resolution for text, a large part of why on-screen type looks so sharp. Two consequences you have already met without knowing: zoom deep into a screenshot of text and the letter edges show faint **red and blue fringes** — subpixel rendering caught in the act; and panels with *other* strip layouts (BGR monitors, PenTile OLEDs) need the renderer to know their physical arrangement, or text goes fuzzy — the treaty again, one floor further down.

![[image-encoding-subpixels.svg|720]]

**The simulation's floor: positions finer than the display.** Games compute physics at a resolution finer than the screen shows. *Super Mario Bros.* (1985) stores Mario's position as a whole pixel **plus one hidden byte of subpixels** — steps of $\tfrac{1}{256}$ of a pixel, plain fixed-point arithmetic (the frugal cousin from [[Floating-Point Representation]]'s opening). Every frame, velocity adds subpixels; the screen rounds to whole pixels, but the physics never does. Speedrunners live on this floor: whether a frame-perfect jump connects can hinge on invisible fractions of a pixel, and the world-record chase — now deep in the 4:54s — is won partly in **subpixel bookkeeping**. The display's grid is a treaty about *showing*; the world underneath is allowed to be finer than what it shows.

---

## Worked examples

**Example 1 — file size.** A $640 \times 480$ screenshot at $8$-bit depth: $640 \times 480 \times 1$ B $= 307{,}200$ B $= 300$ KiB exactly. The same screenshot at $24$-bit: $\times 3 = 900$ KiB. (Compute in bytes, convert last — ÷$1024$ per step.)

**Example 2 — the dials multiply.** A phone camera upgrade doubles photo width and height and moves from $24$-bit to $48$-bit "deep colour." File size factor: $2 \times 2 \times 2 = \mathbf{8\times}$. Resolution went up $4\times$, depth $2\times$ — the dials always multiply.

**Example 3 — read a bitmap.** With $1$-bit depth, the bytes `3C 42 A5 81 A5 99 42 3C` drawn as an $8\times8$ grid (each byte = one row, MSB on the left) render… a circular smiley face. Decode a row: `3C` $= 0011\,1100$ — two blanks, four filled, two blanks. Eight bytes *are* a picture.

**Example 4 — justify (exam style).** *A company needs its new logo on staff badges and on the side of a building. Bitmap or vector?* Vector: the logo is designed shapes (a drawing list exists); one file renders perfectly at both sizes, while a bitmap sized for the badge would pixelate on the building — and a bitmap sized for the building is megabytes wasted on the badge.

---

## Exam Notes

### Cambridge 0478 (IGCSE)

**§1.2.3 — image representation.** Expect to: explain that an image is stored as **pixels**, each encoded in binary; use **resolution** (pixels wide × high) and **colour depth** (bits per pixel); state the effect of increasing either on **quality and file size** (both increase — and file size = width × height × depth is the §1.3.2 calculation). Common ask: "why does increasing colour depth increase file size?" — more bits *per pixel*, same number of pixels.

### Cambridge 9618 (A-Level)

**§1.2 Multimedia — Graphics.** The 0478 material plus, by name: the **file header** (dimensions, depth, format — stored before the pixel data); **image resolution vs screen resolution** as distinct terms; file-size *estimation* (pixel data + header); the effects of changing resolution/depth on quality **and** size; and vector graphics via the exact triad — **drawing list** (the ordered list of objects), **drawing object** (line, circle, rectangle…), **property** (position, radius, fill…). Be ready to **justify bitmap vs vector for a given task** — argue from *source* (measured vs designed) and *use* (fixed size vs any size), not from a memorised "vector better."

**Common mark-losers:** mixing bits and bytes in the file-size calculation (depth may be given in bits *or* bytes — read the unit before multiplying); "resolution" used for screen when the question means image (or vice versa); claiming vector files are always smaller (false for photographic content); forgetting the header when asked to *estimate* a file size; "zooming reveals detail" (it cannot — the samples don't exist).

> [!tip] "Bit depth" vs "colour depth" — the mess, settled by the papers themselves
> Industry uses *bit depth* two ways (per pixel, or per RGB channel), and the exam wording wobbles between phrasings — so here is the actual pattern from the 2021–2025 papers, mark schemes and examiner reports, on **both** boards:
>
> 1. **The two terms are official synonyms.** Mark schemes write "colour depth **//** bit depth" as interchangeable answers, and the 9618 syllabus itself lists "colour depth / bit depth" as one term.
> 2. **Both always mean bits per *pixel* — never per channel.** Every file-size question multiplies width × height × depth directly, with depths stated as "16-bit", "24 bits per pixel", even "4 bytes" or "8 bytes" per pixel; a 9618 examiner report says it flat out: *"bit depth means bits per pixel."*
> 3. **Two stock definitions both earn the mark:** *"the number of bits used to represent each colour"* (the mark schemes' favourite sentence) and *"the number of bits per pixel."* Examiner reports list both among the most common correct answers — "each colour" here means *each pixel's colour value*, not each RGB channel.
> 4. **The bullet-proof sentence — write it every time:** ***"the number of bits used to represent the colour of each pixel."*** It contains both accepted phrasings in one clause and cannot be read the wrong way.
> 5. **What loses the mark:** "the number of pixels" or "pixels per bit" (reversed); "the number of bits used to represent *the image*" (whole image); and the vague "the number of colours the image uses" — an examiner report flagged it as lacking precision (if you reach for colours, say "determines the number of colours that *can* be represented", and put the bits first).
> 6. **The units trap is real:** papers have set depth in *bytes* ("a bit depth of 4 bytes", even "8 bytes"), and an examiner report records candidates reading "8 bytes" as 8 bits and losing the calculation. Read the unit, then work consistently.

---

### IB CS (2027)

Image representation is **not a named statement**: A1.2's published wording stops at binary/hexadecimal conversion and logic gates processing encoded data — pixels, bitmaps, vectors and colour depth are not listed. Treat this card as depth behind "encoded data", not examinable IB content.

## Connections

- **Prerequisite:** [[Number Bases]] — a pixel's colour *is* three bytes in hex; `#2563EB` is raw image data you've been reading all along.
- **Prerequisite:** [[Text Encoding]] — the treaty lesson repeats: pixel bytes don't announce their meaning, so the file header declares it; and text vs image is *convention* vs *measurement*.
- **Prerequisite:** [[Storage Units (Vocab)]] — the file-size formula and the unit ladder this topic's calculations run on.
- **Sibling:** [[Sound Encoding]] — the same sampling story in time instead of space: sampling rate ↔ resolution, bit depth ↔ colour depth, aliasing ↔ moiré. Two cards, one idea.
- **Sequel:** [[Compression]] — a bitmap is gloriously redundant (a blue sky is millions of near-identical pixels), which is exactly what run-length encoding and friends exploit; vectors are already compressed, in a sense — the recipe *is* the compact form.
- **Physics:** [[Optics]] — everything here stands on the eye and on light: the three-cone retina is *why* RGB works, the water droplet magnifies because it is a lens, and a camera's sensor is photons counted per cell before it is numbers per pixel.
- **Mathematics:** [[Matrix Transformations]] — "zoom a vector graphic" means multiplying every coordinate in the drawing list by a scale matrix; rotation and reflection of the recipe are the same one idea. The reason vectors re-render perfectly is that transformations act on *coordinates*, not samples.
- **Cross-domain:** the vault's own figures — every schematic in these notes is a vector drawing list you can open and read; the plots are rendered from [[Number Bases|numbers]] the same way a camera's samples are.

---

## Notation Reference

| Notation | Meaning |
|---|---|
| `#2563EB` | one pixel's colour as three hex bytes — R `25`, G `63`, B `EB` |
| $W \times H$ | image resolution — pixels wide × pixels high |
| bpp | bits per pixel — colour/bit depth |
| $W \times H \times d$ | bitmap pixel-data size in bits (÷8 for bytes; + header) |
| `<circle r="45"/>` | a drawing object with a property — vector graphics' unit of memory |
