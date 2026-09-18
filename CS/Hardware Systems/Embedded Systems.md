---
chinese: 嵌入式系统 (qiànrùshì xìtǒng)
prerequisites:
  - "[[CPU Architecture and the Fetch-Execute Cycle]]"
  - "[[Sensors and Control Systems]]"
  - "[[Input and Output Devices]]"
leads_to:
  - "[[Interrupt Handling]]"
  - "[[Operating Systems]]"
  - "[[Automated Systems and Robotics]]"
tags:
  - subject/computer-science
  - domain/computer-architecture
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/0478-3-1
  - syllabus/9618-3-1
  - type/deep
  - misconception/smartphone-is-embedded
  - misconception/embedded-means-weak
  - misconception/firmware-is-hardware
  - misconception/upgrade-like-a-pc
---

# Embedded Systems 嵌入式系统

> *Count the computers in your home. You will say two, maybe three — the laptop, the phone, perhaps a tablet. The real number is closer to fifty. The washing machine has one. The rice cooker has one. The air conditioner has one, and so does its remote. The car parked downstairs has somewhere between thirty and a hundred and fifty. Your bank card has one. The **charger** plugged into the wall has one — and it is faster than the computer that landed people on the Moon. You miscounted by an order of magnitude because these computers succeeded at the highest ambition a machine can have: they disappeared.*

![[embedded-census-comic.png|640]]

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| embedded system | 嵌入式系统 | a computer built *inside* a device, dedicated to one function |
| general-purpose computer | 通用计算机 | a computer that runs whatever program you install — laptop, desktop, server |
| dedicated function | 专用功能 | the specific role the system is designed to serve |
| microcontroller (MCU) | 微控制器 | an entire computer — CPU, RAM, flash, I/O — on a single chip |
| firmware | 固件 | the system's software, written into flash/ROM at the factory |
| real-time | 实时 | correctness includes a *deadline* — a late answer counts as wrong |
| RTOS (real-time operating system) | 实时操作系统 | an OS designed for predictable timing and scheduling; deadlines also depend on the application and hardware |
| ECU (electronic control unit) | 电子控制单元 | the car industry's name for one of its embedded computers |
| IoT (Internet of Things) | 物联网 | embedded systems that have been given a network connection |
| GPIO (general-purpose input/output) | 通用输入输出引脚 | the MCU's raw pins — where sensors and actuators physically attach |
| SoC (system-on-chip) | 片上系统 | a full computer's worth of silicon on one die — the phone-class big sibling of the MCU |

## The definition — classify the role

An **embedded system** is a computer system — processor, memory, and input/output — built **into a larger device** to perform a **dedicated function**. It executes instructions through the same [[CPU Architecture and the Fetch-Execute Cycle|fetch–decode–execute cycle]] as a laptop. The distinction is the role it was designed to serve.

> **What job does this computer serve inside the product?**
> A dedicated control or processing function points to an embedded system. A platform for a broad range of user-chosen tasks points to a general-purpose computer.

A washing-machine controller reads sensors and controls the wash cycle; selecting a temperature chooses an option within that role. A laptop supports spreadsheets, games, programming and many other jobs. Small size, a missing screen and a locked-down interface are clues, not definitions: a managed laptop is still general-purpose even if its user cannot install applications.

![[embedded-spectrum.svg|697]]

**Firmware updates do not stop a system being embedded.** A router can receive new networking software and remain a dedicated router. An embedded controller can run Linux on a powerful ARM system-on-chip; it need not be a tiny microcontroller running one unchangeable program. Replacing router firmware with OpenWrt does not, by itself, change the device's role.

The level of description matters. A smartphone is a general-purpose device, yet it contains dedicated embedded controllers. “Is the whole device general-purpose?” and “does it contain an embedded system?” are different questions. [Arm's definition](https://www.arm.com/glossary/embedded-system-design) likewise centres on dedicated functions within a larger system.

## The chip: a computer shrunk to a grain of rice

Most embedded systems are built around a **microcontroller** (MCU): a complete von Neumann computer manufactured as **one chip**, a few millimetres across, costing a few yuan.

![[embedded-anatomy.svg|697]]

Everything the big computer spreads across a motherboard is here, in miniature:

| Inside the MCU | The big computer's version | Typical MCU scale |
|---|---|---|
| CPU core | multi-core CPU at 3–5 GHz | one core, 16–200 MHz |
| SRAM | 16 GB of DRAM sticks | **4–256 KB** |
| Flash (holds the firmware) | a 1 TB SSD | 32 KB – 2 MB |
| timers, ADC | expansion cards, sound card | built in |
| GPIO pins | USB, HDMI, DisplayPort | bare metal pins |

Read the RAM row again: **kilobytes**. A single photo from your phone would not fit in this computer's entire memory — and it does not care, because its one program needs four kilobytes and will never be asked to do anything else. This is the deep economy of dedication: a general-purpose machine must carry capacity for *anything*; a dedicated machine carries exactly what its function needs, and nothing more. That is why it can cost ¥2 and sip so little power that it runs for years on a watch battery.

The program itself is called **firmware** (固件) — "firm" because it sits between hard and soft: it *is* software (instructions, fetched and executed), but it is written into **flash or EEPROM** at the factory and typically never changes again. This is exactly the ROM-family territory mapped in [[Secondary Storage]] — PROM, EPROM and EEPROM exist largely *because* embedded systems needed a way to put one permanent program into a cheap chip.

## The sealed ring

What does that one program usually *do*? In most embedded systems, it is the **decide** step of a control loop. [[Sensors and Control Systems]] built the ring — *sense → decide → act → the action returns in the next reading* — and noted that once both ends face the world, the human can leave the room. An embedded system is the next step: **seal the ring, processor and all, inside the appliance**, and the *computer* leaves the room too. What remains visible is just a machine that seems to know what it is doing.

![[embedded-washing-machine.svg|697]]

Walk the washing machine's ring once, slowly:

1. **Lock** the door (actuator: latch solenoid) and *confirm* it is locked (sensor: switch) — act, then sense the act.
2. **Fill** — open the valve, watch the **level sensor**, close the valve at the setpoint.
3. **Heat** — heater on, watch the **temperature sensor**, hold the wash temperature inside a band (the two-threshold trick from the thermostat, unchanged).
4. **Wash** — motor tumbles the drum on a timer pattern.
5. **Drain, rinse, repeat** — pump out, refill, tumble again.
6. **Spin** — but only after the level sensor confirms the drum is empty and the door is still locked (a safety *interlock*: one sensor's reading gates another actuator).
7. **Beep.** The one output aimed at a human, and the only moment the human is needed at all.

Every stage is the same grammar — compare a sensor reading with a stored value, throw an actuator, wait for the world to answer — run by a chip that has no idea it is Tuesday.

## The five habitats

The IGCSE names five domains where embedded systems live; they make a tidy tour because each stresses a different virtue.

| Habitat | It senses | It decides | It actuates | The virtue on display |
|---|---|---|---|---|
| **Household appliances** — washing machine, microwave, dishwasher, rice cooker | level, temperature, door state | cycle state machine | valves, heaters, motors | cheapness — a ¥2 chip replaces a drum of cams and timers |
| **Motor vehicles** — engine management, ABS, airbags | crank angle, wheel slip, sudden deceleration | fuel/spark maps, brake pulsing, fire/don't-fire | injectors, brake valves, igniter | **real-time** — the airbag must fire ~20–30 ms after impact |
| **Security systems** — alarms, smart locks | motion (infra-red), door contacts, glass-break (acoustic) | armed/disarmed state, entry delay | siren, autodialler, lock bolt | reliability — it must work on the one night that matters |
| **Lighting systems** — street lights, motion-triggered stairwells | ambient light, motion, time | thresholds and schedules | lamps, dimmers | low power — the controller must cost less energy than it saves |
| **Vending machines** | coin/note validator, stock sensors, keypad | credit ≥ price? item in stock? | dispensing spiral motor, change hopper | unattended service — no operator, no downtime |

A modern car deserves its own sentence: it carries **dozens to over a hundred ECUs**, networked together — engine, gearbox, brakes, airbags, windows, seats, mirrors, infotainment. A car is not a machine with some computers in it; it is closer to a rolling network of computers that happens to have wheels.

## Benefits and drawbacks — both sides, on demand

The A-Level asks for a *balanced* judgement: why build a device around an embedded system rather than a general-purpose computer — and what does it cost you?

**Benefits:**

- **Cheap** — a microcontroller costs a few yuan; the device's price barely notices the computer inside it.
- **Small and low-power** — one chip, no fans, no screen; runs on a battery for months or years.
- **Predictable at its job** — hardware and software can be selected for the required response time, with fewer unrelated workloads competing. Some designs run without an OS; others use an RTOS or a general OS.
- **Easier to test for a restricted role** — fewer supported functions and configurations can simplify verification. Reliability must still be engineered: bugs, faulty updates and hardware failures remain possible.
- **Easy to mass-produce and easy to use** — millions of identical units, controlled by three buttons instead of a keyboard, needing no training and near-zero maintenance.

**Drawbacks:**

- **Restricted function** — the hardware and interfaces are tailored to a role, making repurposing or expansion difficult.
- **Hard to update** — firmware updates range from awkward to impossible; a discovered bug (or security hole) may live in the field forever.
- **Expert-only repair** — no screen, no error dialogue; diagnosing a fault needs specialist equipment, so a faulty unit is usually **replaced, not repaired** — a real electronic-waste cost.
- **A security risk once networked** — an internet-connected embedded system has all the exposure of a computer with none of the update discipline (see the Mirai story below).

Notice the symmetry: every drawback is a benefit read backwards. *Fixed function* is exactly where the cheapness, speed and reliability come from. The exam loves this observation because it shows you understand the design trade rather than reciting two memorised lists.

## Real time: the deadline is part of the answer

One habitat virtue deserves promotion to a concept. In a **real-time system**, an answer that arrives late is not an inconvenience — it is *wrong*. The airbag controller that decides "fire" 200 ms after the crash has produced the correct output and failed absolutely. Anti-lock brakes release and re-apply pressure many times per second; an engine controller times each spark to fractions of a millisecond, hundreds of times a second, for years.

Your laptop misses deadlines constantly — a stutter here, a spinning cursor there — and nobody is hurt, because a general-purpose OS promises *fairness on average*, not punctuality. An embedded controller makes the opposite promise. That is why most run **no operating system at all** — one program, one loop, nothing to get in the way — and why the ones that need to juggle several tasks run an **RTOS**, a minimal operating system whose one obsession is guaranteeing the deadline of the most urgent task. How a sleeping chip is woken by the world *the instant* something happens — rather than burning power asking "anything yet?" forever — is the [[Interrupt Handling]] story, and it is the natural idiom of every system on this page.

## Worked example 1 — the classifier

> *(a) State what is meant by an **embedded system**. [2]*
> *(b) A washing machine is controlled by an embedded system. Give **two benefits** of this compared with using a general-purpose computer. [2]*
> *(c) Give **one drawback**. [1]*

**(a)** *Tool: the definition — three parts plus dedication.* A computer system (processor, memory and I/O) built **into a larger device** ✓, performing a **dedicated function**, such as controlling the wash cycle ✓.

**(b)** *Tool: the benefits table — pick two, tie them to the machine.* It is small and cheap, so it adds almost nothing to the cost and size of the washing machine ✓; its hardware and software can be tailored to the wash-control deadlines, with fewer unrelated workloads to interfere ✓. (Low power, instant start-up, and no-training-needed are equally creditable.)

**(c)** *Tool: the drawbacks list.* If the firmware has a fault, it is difficult or impossible for the user to update or repair — the controller usually has to be replaced ✓.

## Worked example 2 — the vending machine, traced as input–process–output

> *A vending machine is controlled by an embedded system. Describe how the embedded system uses **input, processing and output** to dispense a can. [6]*

*Tool: the sealed ring — sensors in, comparison in the middle, actuators out. Name a device and its data at every step.*

**Input:** the coin validator senses each inserted coin (weight/size/magnetic signature) and sends its value ✓; the keypad sends the selected item's code ✓.

**Processing:** the processor keeps a running **credit total**, compares it with the selected item's **stored price** ✓ (the setpoint-comparison of every control system), and checks the item's stock count ✓.

**Output:** if credit ≥ price and the item is in stock, the processor drives the **dispensing motor** to rotate that item's spiral ✓, triggers the change hopper to return the difference, and updates the display and the stock count ✓ — storage written by the loop, ready for the *next* customer's comparison.

Six marks, and every one of them is a sensor reading, a comparison, or an actuator — the ring, worn as an exam answer.

## Misconceptions

> [!warning] "Embedded means small and weak."
> Dedication, not power, is the boundary. A car's infotainment ECU outguns a 2005 desktop; a jet engine's controller is a serious computer. They are embedded because their **function is fixed**, not because they are feeble. (The converse trap too: a Raspberry Pi is tiny, yet general-purpose — it runs whatever you install.)

> [!warning] "A smartphone is an embedded system."
> A smartphone as a whole supports many user-chosen tasks, so classify the whole device as **general-purpose**. It can still contain embedded controllers; identify which system the question is asking about.

> [!warning] "There's no software in a washing machine — it's just circuits."
> There is a program in there — fetched, decoded and executed instruction by instruction, like any other. It is called **firmware** because it is closely tied to the hardware and usually stored in non-volatile memory; it can sometimes be updated, but *firm* ware is still soft ware. Without it the chip does nothing at all.

> [!warning] "You can upgrade it like a PC."
> Usually you cannot, and that is a *design choice*, not an oversight. The fixed function is what buys the cheapness and the reliability; the price is that an obsolete or buggy unit is replaced, not upgraded. Firmware updates can fix bugs or improve the dedicated function without making the product general-purpose.

## Exam Notes

| Board | Where it appears | What they want |
|---|---|---|
| **Cambridge 0478 IGCSE** (§3.1.5) | Paper 1 | The **purpose** of an embedded system + **examples** from the five habitats (household appliances, cars, security systems, lighting, vending machines). Typical asks: define (2 marks), identify which devices contain one, give the purpose of the embedded system *in a named device* ("controls the wash cycle by reading sensors and switching the motor/valves/heater"). Anchor every answer in *dedicated function inside a larger device*. |
| **Cambridge 9618 A-Level** (§3.1) | Paper 1 | **Identify** a device as embedded or non-embedded (classify its designed role), and give **benefits and drawbacks** — the mark scheme rewards both sides, so rehearse the symmetric pairs (cheap/fixed, reliable/un-updatable, simple/expert-only-repair). Often folded into a monitoring-and-control scenario — answer with the [[Sensors and Control Systems]] loop vocabulary. |
| **IB CS** | — | Not separately named in any statement. Control-system scenarios (A1.3) may *feature* an embedded controller, and the loop language above answers them, but "embedded system" as a term carries no IB marks of its own. |
| **AP CSA / CSP** | — | Not examined (CSA is Java-only; CSP's computing-systems strand stays at the internet/devices level). |

**The trap to rehearse:** "give an example of a device that **does not** contain an embedded system." A laptop is general-purpose as a whole but may **contain** embedded controllers. Read whether the question asks what the device **is** or what it **contains**; use the described system and its dedicated function, rather than treating a device label as proof about every component.

## Beyond the syllabus

**The first famous embedded computer saved the first Moon landing.** Recall that a real-time system promises deadlines, not fairness. The Apollo Guidance Computer (1969) ran the lunar module's descent with about 4 KB of RAM and a program *woven* into core-rope memory by textile workers — firmware in the most literal sense in history. Three minutes before touchdown, a misconfigured radar began flooding it with spurious work, and the computer did something remarkable for its era: it **shed every task below the deadline-critical ones**, rebooted the rest, kept the engine burning, and raised the famous **1202 alarm** rather than crashing. Mission control read the alarm correctly — *the computer is overloaded but doing exactly what it should* — and called "go". Priority scheduling, graceful degradation, real-time guarantees: the whole RTOS creed, working, a quarter-century before the term existed.

**Your peripherals were the preview.** [[Input and Output Devices]] noticed that every keyboard, mouse and printer hides a small dedicated computer — "open any device on this page and you will find another, smaller computer inside." This card is that observation grown to full size: the peripheral's little translator chip *is* an embedded system, and the world turns out to be peripherals all the way down. Even the USB-C charger contains an MCU — it *negotiates* with your laptop (in an actual protocol) about how many watts to deliver, and that negotiator is quicker than the Apollo computer above.

**When the boxes got network cards.** Give millions of sealed, never-updated computers an internet connection and you get the IoT — and its security bill. In 2016 the **Mirai** botnet logged into hundreds of thousands of webcams and home routers *using their factory default passwords*, conscripted them, and pointed the flood at core internet infrastructure, knocking major websites offline for a day. Nobody's laptop was hacked; the attack came from devices their owners did not think of as computers at all. The security community's grim proverb — "the S in IoT stands for Security" — lands because there is no S. Every drawback in the table above compounds at internet scale: fixed function, no updates, invisible to their owners.

**The cartridge that out-computed the console.** Embedded thinking runs through gaming: your controller is an embedded system (its gyroscope-plus-accelerometer tilt sensing is the sensor-fusion story from [[Sensors and Control Systems]]), and in 1993 *Star Fox* shipped with the **Super FX chip** — a coprocessor *inside the game cartridge* that computed 3-D polygons the console itself could not. Players upgraded their machine by plugging in a game: a dedicated computer, embedded in a plastic box, doing one thing beautifully.

## Connections

- **Builds on:** [[CPU Architecture and the Fetch-Execute Cycle]] — the microcontroller is the same stored-program machine, shrunk to one chip and one program; [[Sensors and Control Systems]] — the ring this box seals in (sense → decide → act, forever); [[Input and Output Devices]] — where the "every peripheral hides a computer" observation first surfaced; [[Secondary Storage]] — flash and EEPROM are where firmware lives, and why the ROM family exists.
- **Leads to:** [[Interrupt Handling]] — how a sleeping chip is woken by the world the instant something happens, the working idiom of every controller on this page; [[Operating Systems]] — what changes when one computer must juggle many tasks, and what an *embedded* OS keeps and throws away.
- **Kindred:** [[Von Neumann machine]] — the MCU is the smallest, cheapest, most numerous von Neumann machine ever built; [[Clock Domains and Metastability]] — what really happens at the GPIO pin when the asynchronous world meets the clocked chip.
- **Leads to:** [[Automated Systems and Robotics]] — the microprocessor in the ring is this card's embedded computer; the smart-speaker question is answered from both cards at once (embedded: yes; robot: no).
