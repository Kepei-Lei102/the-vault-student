---
chinese: 输入与输出设备 (shūrù yǔ shūchū shèbèi)
prerequisites:
  - "[[CPU Architecture and the Fetch-Execute Cycle]]"
  - "[[Secondary Storage]]"
leads_to:
  - "[[Sensors and Control Systems]]"
  - "[[Embedded Systems]]"
  - "[[Interrupt Handling]]"
  - "[[The Blue LED]]"
tags:
  - subject/computer-science
  - domain/computer-architecture
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/0478-3-2
  - syllabus/9618-3-1
  - syllabus/IB-CS-A1-1
  - type/deep
  - misconception/led-screen-is-oled
  - misconception/touchscreen-one-technology
  - misconception/cpu-waits-for-slow-devices
  - misconception/laser-printer-uses-ink
---

# Input and Output Devices 输入与输出设备

> *A processor cannot see a photograph, hear a voice, or feel a fingertip. It moves numbers between registers — that is the whole of what it does. So every device that connects a computer to a person is a **translator**: it turns some physical thing a human can produce (a keypress, a spoken word, a touch) into a number, or turns a number back into some physical thing a human can perceive (ink on paper, light on a screen, a pressure wave in the air). Learn the devices as **transducers**, not as a list — every one of them is the same idea in a different costume: **cross the boundary between the digital interior and the analog world outside.***

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| peripheral | 外围设备 / 外设 | any device attached to the computer that isn't the CPU or main memory |
| input device | 输入设备 | turns a physical action into data the CPU can read |
| output device | 输出设备 | turns data from the CPU into a form a human can perceive |
| transducer | 换能器 / 传感元件 | converts energy from one form to another (physical ↔ electrical) |
| touchscreen | 触摸屏 | an input and output device in one — displays *and* senses touch |
| resistive / capacitive / infra-red | 电阻式 / 电容式 / 红外式 | the three touchscreen technologies |
| pixel | 像素 | one addressable dot of a screen |
| buffer | 缓冲区 | a memory waiting-area that decouples a fast device from a slow one |
| polling | 轮询 | the CPU repeatedly asking a device "ready yet?" |
| interrupt | 中断 | a device signalling the CPU that it needs attention *now* |
| interrupt service routine (ISR) | 中断服务程序 | the code the CPU jumps to when an interrupt fires |
| DMA (direct memory access) | 直接内存访问 | hardware that moves a block device↔RAM without the CPU copying each byte |

## The one job: translate

A computer's inside is a sealed world of bits — voltages that the [[CPU Architecture and the Fetch-Execute Cycle|CPU]] pushes between registers and memory. Nothing a human does is a bit. A fingertip is pressure; a voice is a pressure wave; a printed page is ink. So a peripheral has exactly one job: **stand at the boundary and translate.**

- An **input device** turns a physical action into a number the CPU can read. *Physical → digital.*
- An **output device** turns a number from the CPU into something a person can perceive. *Digital → physical.*

The physics word for "converts one form of energy into another" is a **transducer**, and it is the single idea beneath every device on this page. A microphone is a transducer (pressure → voltage). A speaker is the same transducer run backwards (voltage → pressure). Once you see that, the syllabus's long device list collapses into one question asked over and over: *what physical thing is being turned into a number here, or a number turned back into?*

And notice what the translation costs: **computation**. The keyboard has a small processor of its own scanning the key grid; the optical mouse contains a camera *and* the chip that compares its photographs; a printer holds a full computer that turns a page description into millions of toner placements. Every peripheral is at least a little [[Embedded Systems|embedded system]] — a dedicated computer whose whole life is translating for the big one. Open any device on this page and you will find another, smaller computer inside.

![[io-transducer-frame.svg|697]]

## Input devices — the world coming in

**Keyboard and optical mouse — mechanical intent.** A key press closes a switch in a **grid** — one matrix of a couple of dozen wires serves a hundred keys, instead of one wire per key. The keyboard's own controller drives each row in turn, reads which column answers, and sends a **scan code**: a *number*, not a letter. The letter is assigned later, by the operating system's key map — which is why the same physical keyboard can type twenty languages ([[Text Encoding]] takes it from there). An optical mouse shines an LED (or laser) at the surface and photographs it hundreds of times a second; a tiny processor compares successive frames to see how far the pattern shifted, and reports that displacement as a pair of numbers. Both turn a hand's motion into integers.

![[io-keyboard-matrix.svg|697]]

**Touchscreen — three different physics, one job.** A touchscreen is the rare device that is *both* input and output: it displays a picture and senses where you touch it. There are three ways to sense the touch, and the exam wants you to tell them apart:

![[io-touchscreen-three.svg|697]]

- **Resistive** — two transparent conductive layers held a hair apart. Pressing pushes them together at one spot, completing a circuit; a voltage gradient across the layers reads off the coordinates. *Cheap, works with any object (gloved finger, stylus, fingernail), but the extra layers dim the screen, it registers one touch at a time, and it wears out.* Older ATMs and industrial panels — and history's most expensive resistive screens: Nokia's flagship **5800 XpressMusic** (2008) and **N97** (2009) shipped press-hard screens and a plastic stylus into a world the capacitive iPhone had already changed. The mis-chosen touchscreen technology became a symbol of the giant's fall.
- **Capacitive** — one glass layer coated with a transparent conductor holding a faint, even electrostatic field. A finger is itself a conductor, so touching it **draws charge away** at that point; the controller senses the dip at the screen's corners and computes where. *Sharp, bright, durable, and **multi-touch** (it can track several charge-draws at once — this is how pinch-to-zoom works), but it needs a **conductive** touch — a bare fingertip or a special stylus, not a woolly glove.* Every smartphone.
- **Infra-red** — a grid of infra-red LEDs down two edges and photodetectors down the other two, casting an invisible lattice of beams just above the glass. A touch **breaks** one horizontal and one vertical beam; the broken row and column are the coordinates. *Works with anything and scales to huge sizes, but the frame is bulky and dust or bright sun can fool it.* Large kiosks and interactive whiteboards.

Watch the three mechanisms in motion — pressure, charge, shadow:

![[io-touchscreen.mp4]]

**Scanners — a pattern becomes a number.** A **barcode scanner** sweeps a laser across the stripes and times the reflections: wide bright, narrow dark, and so on, decoded into the product number. A **QR code scanner** is really a camera plus software — it photographs the 2-D pattern and decodes the grid (with error-correction built in, so a torn code still reads). A **2-D scanner** (a flatbed) photographs a flat page into a bitmap ([[Image Encoding]]); a **3-D scanner** sweeps a laser or projects a pattern over an object and measures the distortion to capture its shape as a point cloud.

**Camera and microphone — the sampling bridge.** A digital camera's sensor is a grid of light-wells, each measuring how many photons of red, green, or blue arrived — the raw pixel grid of [[Image Encoding]]. A microphone's diaphragm rides the air-pressure wave and produces a continuously varying voltage, which an **analogue-to-digital converter (ADC)** measures at a fixed rate — the sampling of [[Sound Encoding]]. Both are transducers whose analog output must be *measured* into numbers, exactly the decision-boundary move that runs through [[Secondary Storage]].

## Output devices — the number going out

**Printers — two mechanisms, plus a third dimension.**

- **Inkjet.** Liquid ink is fired through microscopic nozzles, one droplet at a time, as the print head sweeps across the paper. Two ways to fire it: **thermal** (a pulse of heat boils a tiny bubble that ejects the drop) or **piezoelectric** (a crystal flexes when charged, squeezing the drop out). *Cheap printer, expensive ink; excellent photos; slow; ink can smear until dry.*
- **Laser.** The star of the section, and a beautiful reuse of the "charge is the medium" idea from [[Secondary Storage]]. A **laser** draws the whole page as a pattern of electric charge on a rotating photosensitive **drum**; charged **toner** (a fine plastic powder, *not* liquid ink) sticks only to the charged pattern; the drum rolls the toner onto the paper; and a hot **fuser** melts the toner so it bonds permanently. *Fast, razor-sharp text, cheap per page, expensive printer.* The whole machine is electrostatics — the same physics that stores your files, now drawing your homework.
- **3-D printer.** Instead of laying ink on a surface, it builds a solid object **layer by layer** from a 3-D model sliced into thin horizontal slices. The common kind (FDM) extrudes molten plastic filament and lets each layer cool and fuse to the last; others cure liquid resin with a laser (SLA) or fuse powder with a laser (SLS). *Additive manufacturing — you add material where you want it, rather than carving it away.*

The laser printer's five electrostatic stages, animated — charge, write, dust, transfer, fuse:

![[io-laser-printer.mp4]]

And the 3-D printer as the pulps would have covered it — the cosmic promise, the fourteen-hour boat:

![[io-3d-printer-comic.png|500]]

**Screens — emit, or shutter?** The key distinction the syllabus hides:

- An **LCD** (liquid-crystal display) does **not** make its own light. Behind the glass is a **backlight**; in front of it, a layer of **liquid crystals** that twist under voltage to either block or pass that light, pixel by pixel, through red/green/blue colour filters. The crystal is a *shutter*, not a lamp. When a screen is sold as an **"LED screen,"** it almost always means an LCD whose backlight is made of LEDs — the LEDs light the panel, they are not the pixels.
- A true **LED / OLED** display makes each pixel emit its own light, with no backlight at all — so a black pixel is genuinely *off* (perfect blacks, thinner panels). Knowing that "LED-backlit LCD" and "OLED" are different answers this: *why do OLED phones have inkier blacks than LCD ones?*

**Projectors.** A **DLP** projector holds a chip of **millions of microscopic mirrors — one per pixel** — each tilting thousands of times a second to bounce light either toward the lens (bright) or away (dark), while a spinning colour wheel paints in the colour. An **LCD projector** shines a bright lamp through three small LCD panels (one each for red, green, blue) and recombines them through a prism.

**Speaker — the microphone in reverse.** A **digital-to-analogue converter (DAC)** turns the stream of sound numbers back into a smoothly varying voltage; that voltage drives an electromagnet (the voice coil) that pushes and pulls a paper cone; the cone shoves the air; the air-pressure wave is sound. Every transducer on this page has a partner running the other way, and the microphone/speaker pair is the clearest: *measure the wave into numbers, then push the numbers back into a wave.*

**VR headset — everything at once.** A virtual-reality headset is the whole card in one object: **two** small, very high refresh-rate displays (one per eye) showing slightly offset images so your brain fuses them into 3-D depth (**stereoscopy**); **lenses** to focus those centimetre-close screens; and — crucially — **head-tracking sensors** (an accelerometer and gyroscope, sometimes helped by external cameras) that report which way you're looking so the rendered view updates as you turn. The output (two displays) and the input (motion sensors) must stay in a tight loop with tiny **latency**, because if the picture lags your head by even a few tens of milliseconds, your inner ear disagrees with your eyes and you feel sick. Those motion sensors are the doorway to [[Sensors and Control Systems]].

## How I/O is actually done — the speed problem and its fixes

Naming the devices is half the topic; the other half is *how the CPU talks to them*, and it starts from one brutal fact: **the CPU and its peripherals live on wildly different clocks.** The CPU acts in nanoseconds; a disk answers in milliseconds; a printer takes seconds per page; a human types a few characters a second. If the CPU simply waited for each device, a machine would spend nearly all its time doing nothing. Three ideas fix this.

**Buffers — decouple fast from slow.** A **buffer** is a small waiting-area in memory between the CPU and a device (the same buffer met in [[Secondary Storage]]). The fast side drops its data into the buffer and walks away; the slow side drains it at its own pace. Send a document to print and it lands in a print buffer in milliseconds — the CPU is then free while the printer chews through it for minutes. The buffer *decouples the producer from the consumer* so neither waits on the other's bad moments.

![[io-buffer.svg|697]]

**Polling vs interrupts — how the CPU knows a device is ready.** A buffer solves *where* the data waits, but not *how the CPU learns* a device needs attention. Two answers, and the difference is one of the most important ideas in the whole architecture:

![[io-polling-vs-interrupt.svg|660]]

- **Polling** — the CPU asks, over and over, *"ready yet? ready yet? ready yet?"*, checking a status flag in a loop. Simple to build, but it is **busy-waiting**: every "not yet" is a wasted cycle the CPU could have spent computing. Polling a keyboard would burn a billion checks between two keystrokes.
- **Interrupts** — instead, the device stays quiet until it actually needs the CPU, then raises the **interrupt line** on the control bus (the very line named in the [[CPU Architecture and the Fetch-Execute Cycle|fetch–execute]] card's bus table). The CPU finishes its current instruction, **saves its state** (registers, program counter), jumps to a small piece of code called the **interrupt service routine (ISR)** that handles the device, then **restores its state** and resumes exactly where it was — as if nothing happened. Now the CPU does useful work and is tapped on the shoulder only when a device genuinely has something to say.

Interrupts are why a computer can do many things "at once": the keyboard, the mouse, the disk, the network card, and the system clock all interrupt the CPU as they need it, and the operating system juggles them. Without interrupts there is no multitasking — just one device polled to the exclusion of all else.

**DMA — don't make the CPU carry the boxes.** Even with interrupts, copying a whole disk block into memory byte-by-byte would still tie up the CPU for the entire transfer. **Direct memory access (DMA)** hands that job to a dedicated **DMA controller**: the CPU says "move these 4 KB from the disk into memory at this address," then goes back to computing; the DMA controller shuttles the block across the bus on its own and raises **one** interrupt at the very end to say "done." The CPU is bothered once, not thousands of times. Bulk transfers — disk, network, sound — all lean on DMA.

The arc is one of steadily removing the CPU from the drudgery: the **buffer** stops it waiting for *where* the data sits, the **interrupt** stops it asking *whether* a device is ready, and **DMA** stops it carrying the data itself.

## Worked example — describe and choose (exam style)

**Part (a) — describe the operation of a laser printer.**

*Tool: name the mechanism in stages, using the electrostatic keywords the mark scheme rewards.*

1. A rotating **drum** is given a uniform electric **charge**.
2. A **laser** is scanned across the drum, discharging the dots that will *not* hold toner — drawing the page as a charge pattern.
3. **Toner** (charged powder) is attracted to the charged areas of the drum only.
4. The paper is fed past the drum and the toner **transfers** onto it.
5. A heated **fuser** melts the toner so it **bonds permanently** to the paper.

Answering "it sprays ink" scores zero — that is an inkjet. The examinable distinction is *toner + drum + laser + fuser* (dry, electrostatic) versus *liquid ink through nozzles* (inkjet).

**Part (b) — a factory needs a touchscreen that operators use while wearing thick gloves. Which technology, and why?**

*Tool: match the device's limitation to the context's demand.*

A **capacitive** screen won't work — it needs a conductive bare-finger touch, and a glove is an insulator. Choose **resistive** (responds to *pressure* from any object, glove included) or **infra-red** (a gloved finger still breaks the beams). Name the deciding property — *the touch is not conductive* — not just the winner. The habit the exam rewards is: **state which axis the context stresses, then pick the technology that wins that axis.**

## Misconceptions

> [!warning] "An 'LED screen' has one LED per pixel."
> Almost never. A screen sold as "LED" is nearly always an **LCD** panel with an **LED backlight** — the LEDs light the whole panel from behind, and liquid-crystal shutters plus colour filters make the pixels. Only **OLED** (and micro-LED) screens truly emit light per pixel, which is why their blacks are perfectly dark: a black pixel is switched *off*, not shuttered over a lit backlight.

> [!warning] "A laser printer uses ink."
> It uses **toner** — a dry plastic powder — fused to the paper by heat, and the "laser" only *draws the charge pattern* on the drum; it never touches the paper. Liquid ink through nozzles is the **inkjet**. Mixing these up is the single most common lost mark in this topic.

> [!warning] "A touchscreen is one kind of thing."
> Three different physics wear the same name. If an exam says "explain why this touchscreen works with a gloved hand" or "…supports pinch-to-zoom," it is testing whether you know *which* technology — infra-red/resistive for the glove, capacitive for multi-touch.

> [!warning] "The CPU waits while a slow device works."
> Only under naive **polling**. With **interrupts**, the CPU does other work and the device signals when it's ready; with **DMA**, a separate controller moves bulk data while the CPU computes. "The CPU sits idle waiting for the printer" describes a machine nobody would build.

> [!info] Beyond syllabus — the I/O frontier
> - **Human interface devices as sensors.** The line between "input device" and "sensor" is really about *who's on the other end.* A touchscreen and a keyboard sense a **human**; a thermostat's thermistor senses the **environment**. Same transducer idea, different partner — which is exactly the seam into [[Sensors and Control Systems]].
> - **Memory-mapped I/O.** Many systems don't have separate "talk to a device" instructions at all — each device's control and data registers are wired to appear at ordinary **memory addresses**, so reading a keyboard is literally reading a memory location. The peripheral hides inside the address space.
> - **The interrupt vector table.** When an interrupt fires, how does the CPU know *which* ISR to run? A table in memory maps each interrupt number to the address of its handler — the CPU looks up the number and jumps. Priorities decide what happens when two interrupts arrive at once (a disk finishing vs a clock tick). The full machinery — vectors, priorities, nesting — is [[Interrupt Handling]].
> - **The polling hidden inside your gaming mouse.** At the wire level, USB is *pure polling* — but done by the **host controller chip**, not the CPU. The controller asks each device on a fixed schedule; a device with nothing to report answers with a single tiny "nothing" packet (a NAK), and the exchange dies right there in silicon. Only a poll that returns real data gets copied to memory and raises an interrupt. So both answers are true at once — *the bus polls, the CPU is interrupted* — and the busy-waiting has been exiled to a dedicated chip that is built to do nothing else.
> - **How 8000 Hz mice happen.** Full-speed USB delivers data in 1 ms frames, capping a mouse at 1000 reports per second. USB 2.0's high-speed mode (standardised in 2000) split each frame into eight 125 µs **microframes** — headroom that sat unused for two decades until e-sports came asking. A 4000 or 8000 Hz mouse simply enumerates at high speed and requests a poll every microframe; no exotic bus needed. The catch is on the receiving end: 8000 interrupts a second is real CPU load, which is why the drivers warn you.
> - **Where the DMA controller lives now.** The single central DMA chip of early PCs is gone. Every fast peripheral — graphics card, NVMe SSD, network card — now carries its **own** DMA engine and, as a *bus master*, reads and writes memory directly across PCIe; the memory controller it talks to sits on the CPU die itself, and an **IOMMU** stands guard over which addresses each device may touch. The old central design survives where peripherals are too simple to master a bus: inside microcontrollers — the little embedded systems this page keeps finding.
> - **Latency is the VR killer.** The reason VR needs 90+ Hz displays and sub-20 ms motion-to-photon latency is physiological: your vestibular system reports head motion instantly, and if the rendered view lags, the sensory conflict induces nausea. It's an I/O-loop deadline enforced by biology.

## Exam Notes

### Cambridge 0478 (IGCSE) — §3.2.1–2 Input and output devices

- **Define both, with the *why* (3.2.1–2 openers):** an input device turns a physical action into data the computer can process; an output device turns processed data into a form the user can use/perceive. Give the *reason* (computers need a way to receive and to present data), not just an example.
- **Know the device lists by name.** Input: barcode scanner, digital camera, keyboard, microphone, optical mouse, QR scanner, **touch screen (resistive, capacitive, infra-red)**, 2-D/3-D scanners. Output: **actuator**, DLP projector, inkjet printer, laser printer, LED screen, LCD projector, LCD screen, speaker, 3-D printer.
- **The three touchscreen technologies are examined explicitly** — be able to describe each mechanism *and* give an advantage/disadvantage and a suitable context. This is the highest-value part of the topic.
- **Printer confusion is the classic trap** — keep inkjet (liquid ink, nozzles) and laser (toner, charged drum, fuser) cleanly apart.
- **Note on the actuator.** 0478 files the **actuator** under *output devices* (§3.2.2), but it makes sense only inside the sensor→process→actuator control loop — its operation is treated with sensors in [[Sensors and Control Systems]]. For 0478 you need only that an actuator is an output device that produces movement (a motor, valve, or relay) in response to a signal.

### Cambridge 9618 (A-Level) — §3.1 principal operations of hardware devices

- The §3.1 LO "**describe the principal operations of hardware devices**" names a specific list; the human-facing half sits here: **laser printer, 3-D printer, microphone, speakers, touchscreen, virtual reality headset** (the magnetic hard disk, solid-state flash, and optical disc reader/writer are covered in [[Secondary Storage]]).
- Answer in **mechanism language, in stages** — for the laser printer, the drum/charge/laser/toner/fuser sequence; for VR, the two displays + lenses + head-tracking-sensors + low-latency loop.
- **Buffers (§3.1)** — an I/O buffer is a memory area that compensates for the **speed difference** between the CPU and a slower device; state one concrete use (printing, streaming) with the speed-mismatch reason. (Buffers are introduced in [[Secondary Storage]].)
- **Interrupts** appear across 9618 (§4.1 control bus, §16.1 OS scheduling) — the polling-vs-interrupt distinction and the save-state → ISR → restore-state sequence are reusable everywhere the syllabus discusses how a processor handles events.

### IB Computer Science — A1.1 Computer hardware and operation

Input/output devices and peripherals sit inside A1.1 (computer fundamentals): the transducer framing and the device families are the working vocabulary for A1.1 hardware questions, and the polling/interrupt/DMA material reappears in A1.3's operating-systems content as *how the OS manages devices and events*.

### AP Computer Science A

Not examined — AP CSA is a programming course; I/O hardware is out of scope.

## Connections

- **Parent:** [[CPU Architecture and the Fetch-Execute Cycle]] — the bits these devices translate to and from, and the control-bus **interrupt line** the ISR mechanism uses. Peripherals are what hang off the ends of those buses.
- **Uses:** [[Secondary Storage]] — the **buffer** that decouples fast CPU from slow device (and the "charge is the medium" electrostatics reused by the laser printer); [[Text Encoding]] — the scan-code-to-character step of a keypress; [[Image Encoding]] / [[Sound Encoding]] — cameras and microphones as the ADC front-ends whose sampling these cards derive.
- **Leads to:** [[Sensors and Control Systems]] — the *world*-facing twin of this *human*-facing card: sensors and actuators in the monitoring/control loop (where the 0478 actuator and the VR headset's motion sensors properly live); [[Embedded Systems]] — a whole computer built around that sense-decide-act loop; [[Interrupt Handling]] — the ISR / vector-table / priority machinery in full.
- **Physics bridge:** the microphone/speaker and camera/screen pairs are transducers in the [[Damped Oscillations|oscillation]] and wave sense — a voice coil pushing a cone is a driven mechanical system.
- **Story:** [[Stories/The Blue LED]] — the "LED screen" rows have a human story: thirty years of red-and-green, a phosphor company from Tokushima, and the Nobel that Alfred Nobel's will was actually written for.

## Glossary

| term | 中文 | one-liner |
|---|---|---|
| scan code | 扫描码 | the number a keyboard sends for a pressed key, before it becomes a character |
| electrostatic (printing) | 静电（打印） | using electric charge to place toner — the laser-printer principle |
| toner | 碳粉 | dry charged powder fused to paper by a laser printer (not liquid ink) |
| stereoscopy | 立体视觉 | two offset images, one per eye, fused into 3-D depth |
| latency | 延迟 | the delay between an action and its effect — critical in a VR I/O loop |
| busy-waiting | 忙等待 | a CPU looping to check a status flag, wasting cycles — the cost of polling |
| interrupt service routine | 中断服务程序 | the handler code an interrupt makes the CPU jump to |
| memory-mapped I/O | 内存映射输入输出 | wiring a device's registers to appear as ordinary memory addresses |

## LaTeX Reference

*(No mathematical notation is needed here — the content is mechanism and vocabulary. Device data rates and latencies, when named, use plain units: ns, µs, ms, Hz.)*
