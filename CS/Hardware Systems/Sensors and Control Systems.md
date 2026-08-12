---
chinese: 传感器与控制系统 (chuángǎnqì yǔ kòngzhì xìtǒng)
prerequisites:
  - "[[Input and Output Devices]]"
leads_to:
  - "[[Embedded Systems]]"
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
  - syllabus/IB-CS-A1-3
  - type/deep
  - misconception/sensor-outputs-a-number
  - misconception/monitoring-equals-control
  - misconception/humidity-equals-moisture
  - misconception/control-loop-runs-once
---

# Sensors and Control Systems 传感器与控制系统

> *An input device waits for a human. A sensor waits for nothing — it watches the world itself: heat, light, acid, pressure, the invisible tilt of the ground. Give a computer sensors and it can **notice**; give it actuators and it can **act**; connect the two through a program and something genuinely new appears: a machine that measures the world, changes it, and then measures its own change — around and around, forever. That ring — **sense, decide, act, repeat** — is the quiet machine inside greenhouses, incubators, airliners and artificial hearts. And it was already running, in spinning brass, a century before the first computer arrived.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| sensor | 传感器 | a transducer pointed at the world — turns a physical quantity into an electrical signal |
| actuator | 执行器 | an output device that produces physical action — motor, valve, heater, pump |
| ADC (analogue-to-digital converter) | 模数转换器 | measures a smoothly varying voltage into a number, over and over |
| DAC (digital-to-analogue converter) | 数模转换器 | the reverse — a number back into a voltage |
| monitoring system | 监测系统 | measures and reports; never touches the process |
| control system | 控制系统 | measures, compares, and **acts** — its action changes the next measurement |
| feedback loop | 反馈回路 | the ring: output fed back to become part of the next input |
| negative feedback | 负反馈 | a response that *opposes* the deviation — the stabilising kind |
| setpoint | 设定值 | the stored target value the processor compares against |
| threshold | 阈值 | the boundary reading that triggers a decision |
| calibration | 校准 | mapping raw sensor numbers onto real physical units |
| relay | 继电器 | an electrically-thrown switch — a small signal commanding a big current |

## The seam: pointed at the world, not at a person

Every peripheral is a **transducer** — that is the whole thesis of [[Input and Output Devices]] — and the devices there share one quiet assumption: a *human* stands on the far end. A keyboard waits for fingers; a screen performs for eyes.

A sensor is the same translator with the assumption removed. A thermistor does not care whether anyone is watching; it reports the heat of the room to whatever is wired to it, at three in the morning, in a greenhouse nobody has visited for a week. And the **actuator** is the output half with the same assumption removed: a speaker plays *to someone*, but a valve performs for no audience — its job is to change the world so that the *sensor will notice the difference*.

That is the seam, and it is why this pair earns its own machinery. Once both ends of the translation face the world instead of a person, **the human can leave the room** — and the room keeps running.

One truth carries over unchanged: *nothing in nature is a number*. A thermistor's resistance slides smoothly as the room warms; a moisture probe's current drifts as soil dries. Every sensor chain is the same three-step translation, and it pays to name the steps:

**physical quantity → sensor (a smeary analogue voltage) → ADC (a number) → the program**

## The fourteen senses

Evolution gave you a handful of senses. The syllabus hands the machine **fourteen** — several of which no unaided human has. You cannot feel pH. You cannot feel a magnetic field (a robin can; you need a chip).

| sensor | measures | the physics, in one line | classic context |
|---|---|---|---|
| acoustic 声学 | sound level | a microphone — pressure waves flex a diaphragm into voltage | glass-break alarm; machinery health |
| accelerometer 加速度计 | acceleration, tilt | a microscopic silicon mass on springs; motion shifts it, changing a capacitance | phone screen rotation; airbag trigger — a crash is a huge deceleration |
| flow 流量 | liquid/gas movement | a tiny turbine in the stream; each spin sends a pulse | water meter; drip-irrigation line |
| gas 气体 | a specific gas | the target gas reacts on a sensitive surface, changing its resistance | carbon-monoxide alarm; air-quality station |
| humidity 湿度 | water vapour **in the air** | a capacitor whose insulator absorbs vapour, shifting its capacitance | greenhouse air; server room |
| infra-red 红外 | a broken beam, or body heat | active: an invisible beam interrupted; passive (PIR): moving warmth against the background | intruder alarm; automatic door |
| level 液位 | liquid height | a float on a switch — or pressure at the tank floor, or an ultrasonic echo off the surface | washing-machine fill; fuel gauge |
| light 光 | brightness | an LDR whose resistance falls as light rises | streetlights at dusk; greenhouse shading |
| magnetic field 磁场 | a magnet near, or field strength | a reed switch snaps shut; or a Hall-effect voltage appears | door/window alarm contact; laptop-lid sleep |
| moisture 水分 | water **in soil or a surface** | two probes — wet material conducts between them | irrigation: water only when the soil is dry |
| pH 酸碱度 | acidity | a glass electrode develops a voltage tracking hydrogen-ion concentration | river-pollution monitoring; aquarium |
| pressure 压力 | force, weight, squeeze | a crystal or strain gauge yields a voltage when squeezed | burglar mat under the carpet; tyre monitor |
| proximity 接近 | something nearby, without contact | emits infra-red or ultrasound and watches for the reflection | phone-by-your-ear screen-off; parking assist |
| temperature 温度 | hot and cold | a thermistor whose resistance falls as it warms | greenhouse, oven, CPU, incubator — everything |

Three flags worth pinning to the table:

- **Humidity is not moisture.** Humidity is water vapour *in the air*; moisture is water *in the soil or on a surface*. An irrigation system wants a **moisture** sensor — a humid evening can hang over bone-dry soil. This near-synonym is the single most reliable trap in the topic.
- **Sensors hunt in packs.** A greenhouse runs temperature *and* humidity *and* light *and* moisture; a phone carries an accelerometer, proximity, light and magnetic sensor without you ever noticing. Exam questions rarely want one sensor — they want the *right set*, each justified.
- **The pressure sensor closes an old loop:** it is the working heart of the resistive touchscreen from [[Input and Output Devices]] — the same physics, promoted from sensing a finger to sensing the world.
- **How an accelerometer knows *tilt*:** it cannot tell gravity from acceleration — and that is the trick. At rest, the proof mass sags under gravity's steady 1 g; tilt the chip and that 1 g redistributes across its three axes (a component $g\sin\theta$ appears along the tilted axis), so reading the axes reads *the direction of down*. Fine print: in a turning car the same confusion fools it — extra acceleration masquerades as tilt — which is why real devices get their orientation from sensor fusion (see Beyond).

## From smear to number — the ADC

The sensor's raw output is analogue: a voltage that slides. The **ADC** measures it into a number, and does so *repeatedly* — a control system's ADC is never done, because the world never holds still.

Two ideas ride along. **Resolution:** an 8-bit ADC splits the voltage range into 256 steps, a 10-bit one into 1024 — finer steps, finer distinctions (the same staircase as [[Sound Encoding]]'s sample depth; an acoustic sensor *is* that card's microphone-and-ADC chain wearing work clothes). **Calibration:** the ADC's output is just a count — 743 of 1024. Somebody must map counts onto reality ("743 means 21.3 °C"), by checking the sensor against known references. An uncalibrated sensor is confidently meaningless.

## The actuator — the hand

An **actuator** turns an electrical signal back into physical action: a **motor** (rotation — open the window, spin the drum), a **pump**, a **valve**, a **heater**, a **solenoid**. The signal path runs down through a **DAC** or a simple on/off line, usually via a **relay** — an electrically-thrown switch that lets a tiny processor signal command a mains-powered machine. A milliwatt whisper throwing a kilowatt punch.

0478 files the actuator under *output devices*, and that is technically true — but it hides the point. Screens and speakers aim their output at people. An actuator aims its output at *the measured quantity itself*. It exists to be noticed by a sensor.

> [!tip] The two questions that draw the boundary
> Boundary cases ("is this an actuator?" — "is this a control system?") settle with two questions. **One: does it push on the physical world — move it, heat it, pump it — rather than present something to a person's senses?** That separates the actuator from the screen and the speaker (whose cone technically moves, but for an audience of eardrums, not sensors). **Two: is the thing it changes the very quantity a sensor is watching?** That separates a closed control loop from a mere output — the monitoring-vs-control question in miniature. Ask them in order: the first classifies the *device*, the second classifies the *system*.

## Monitoring — measure and tell

A **monitoring system** is sensors + ADC + processor, ending in a record, a display, or an alarm: an ICU patient monitor that pages a nurse, a river station logging pH and temperature above a factory outflow, a weather station, the data logger in a science lesson.

The defining property: **the system never touches the process.** It watches; it tells; it cannot act. The loop is left open, and a *human* closes it — the nurse adjusts the drip, the environment agency phones the factory. If the readings misbehave at 3 a.m. and nobody comes, nothing changes. That is not a flaw; it is the definition.

## Control — closing the ring

Now add an actuator, and give the processor a **setpoint** — a stored target. Everything changes:

![[sensors-control-loop.svg|697]]

The system measures, **compares the reading with the setpoint**, and acts — and here is the beautiful part — *the action changes the very quantity being measured*, so the next reading already contains the system's own fingerprints. Output feeds back into input. The chain has become a ring: **feedback**.

Watch one lap in a greenhouse holding 20–25 °C: the temperature sensor reads continuously; the ADC hands the processor a number; below 20 °C the processor throws the relay — heater on; the room warms; the *same sensor* reports the warmth; above 25 °C the heater goes off; the room slowly cools; repeat, all night, forever.

![[sensors-thermostat-cycle.svg|697]]

**Why a band and not a single perfect target?** Hold the heater to one threshold — "on below 22.5, off above" — and the reading, trembling with noise around that line, would machine-gun the relay on and off every few seconds. Two thresholds give the loop a calm breathing rhythm: the temperature *surfs* between them. (The trick has a name — see Beyond.)

**Negative feedback** is what makes this settle instead of explode: the response always *opposes* the deviation. Too cold → add heat; too hot → stop. The evil twin is **positive feedback**, where the response amplifies the deviation — put a microphone near its own loudspeaker and a whisper becomes a screech in half a second: an acoustic sensor and an actuator wired into the *wrong* kind of ring. Society has since built that circuit at scale: a feed that shows you more of whatever you already react to is a microphone held to its own loudspeaker — the **echo chamber** is positive feedback running on beliefs instead of sound. Your own body is a federation of negative-feedback loops holding you at 37 °C — shivering is your heater, sweating is your fan, and the insulin–glucose loop is the same diagram with different transducers.

**And the ring is older than the computer.** James Watt's flyball governor (1788): the steam engine spins a pair of brass balls; spin too fast and they fly outward, and their rising linkage *narrows the steam valve* — the engine throttles itself. Sense, compare, act — with the setpoint built into the geometry. When Victorian governors began to misbehave — oscillating around their targets, "hunting" — it was Maxwell, the same Maxwell of the equations, whose paper *On Governors* (1868) founded control theory to explain why. The computer did not invent the loop. It made the **decide** step programmable: to change the rules, you now edit a number instead of re-machining a linkage.

## Worked example — the greenhouse, exam-grade

**Part (a) — describe how sensors and a microprocessor keep a greenhouse between 20 °C and 25 °C.**

*Tool: walk the ring once, stage by stage, and say "continuously".*

1. A **temperature sensor** continuously measures the air (an analogue reading).
2. The **ADC** converts each reading to a digital value for the microprocessor.
3. The processor **compares** the value with the **stored range** (the setpoint, 20–25 °C).
4. Below 20 °C → the processor signals the **actuator**: heater **on** (windows stay shut).
5. Above 25 °C → heater **off**; a window-motor actuator opens the vents.
6. **The process repeats continuously** — each action changes the temperature that the next reading reports.

Marker's note: the two most-dropped marks in this classic are "**compares with a stored value**" (not just "checks the temperature") and "**continuously / repeatedly**" (a loop described once is not a loop). And name the actuator doing the work — "the computer makes it warmer" earns nothing.

**Part (b) — a system must water a garden only when the soil is dry and it is night. Choose two sensors, and explain why a humidity sensor is the wrong third choice.**

*Tool: name the exact physical quantity each candidate measures, then match it to the quantity the context actually cares about.*

A **moisture** sensor — the question is about water *in the soil*, and that is precisely what it measures. A **light** sensor — falling light level identifies night. The humidity sensor fails because it measures water vapour *in the air*: a muggy evening over parched soil would report "wet" and the garden would die of good weather reports.

## Misconceptions

> [!warning] "The sensor sends the computer a temperature."
> It sends a smeary analogue voltage. The **ADC** turns that into a number, and **calibration** is what makes the number *mean* 21.3 °C. Three steps, and exam answers earn credit for naming the middle one — "the sensor's analogue value is converted by an ADC" is a marking point in its own right.

> [!warning] "Monitoring and control are basically the same thing."
> One question separates them: **does the system's own output change the quantity it measures?** A patient monitor pages a nurse — a *human* closes the loop: monitoring. A greenhouse throws its own heater: control. No actuator acting on the process → monitoring, always.

> [!warning] "Humidity and moisture are synonyms."
> Air versus soil. Humidity = water vapour in the **air**; moisture = water in the **soil or a surface**. The irrigation question is set precisely to catch this — and in Chinese the trap half-vanishes (湿度 vs 水分), which is a hint: the confusion is an accident of English, not of physics.

> [!warning] "The loop runs once."
> "…and the process **repeats continuously**" is the sentence exam answers forget. Without repetition there is no control — just one lucky adjustment and a long blind night. The ring, not any single lap, is the machine.

> [!info] Beyond syllabus — the loop, grown up
> - **Hysteresis 滞回.** The two-threshold trick has a name: the gap is a *dead band*, and it exists to stop noise near a single threshold from machine-gunning the actuator. Watch it work below — one threshold and every noisy crossing throws the relay; a dead band and the loop breathes. Electronics plays the same trick on any trembling analogue signal with a **Schmitt trigger** — two switching levels, one calm digital output.
>
> ![[sensors-hysteresis.svg|660]]
>
> - **PID control.** On/off ("bang-bang") is the syllabus loop. Serious loops read the error **three ways** and push with the weighted sum: **P**roportional — how far off *now*; **I**ntegral — how long you have *been* off (the accumulated area); **D**erivative — how fast it is *changing* (the slope, which says "ease up, you're arriving"). That third term is what kills the eternal sawtooth: the 3-D printer of [[Input and Output Devices]] holds its nozzle at 200 ± 1 °C with PID, and a hovering drone re-runs its PID loops hundreds of times per second.
>
> ![[sensors-pid.svg|660]]
>
> - **Sensor fusion.** No single sense is trustworthy — accelerometers are noisy (and read hard cornering as tilt), gyroscopes drift. Combining them (the classic recipe is the *Kalman filter*) beats either alone: that is how a VR headset, a phone, and a rocket all know which way is up. Recall that the VR headset's tracking loop lives under a hard latency deadline — fusion has to be not just right but *fast*.
> - **Feedback as a worldview.** Body temperature, blood glucose, predator–prey populations, a market groping toward a price — once you can see closed loops, they are everywhere. Feedback is deliberate **re-coupling**: wiring an output back into an input *on purpose* — the constructive half of [[Decouple and Recouple]]. The newest member of the family is **reinforcement learning**: an agent acts, the environment scores the action, and the score reshapes the next action — this card's ring, taught to software. **RLHF**, the technique that aligns large language models, closes that loop through *human judgment* — arguably the most expensive feedback signal ever purchased. Which hides a lesson worth keeping: feedback about yourself is the scarcest input your own control loop can get. When someone offers it, never hesitate.

## Exam Notes

### Cambridge 0478 (IGCSE) — §3.2.3 Sensors

- **The sensor list is closed ("limited to"):** acoustic, accelerometer, flow, gas, humidity, infra-red, level, light, magnetic field, moisture, pH, pressure, proximity, temperature. Know each sensor's *quantity measured* and one context; the exam's favourite verb is **match** — sensors to a described scenario, with justification.
- **The answer skeleton** for any monitoring/control description: sensor (continuously) → ADC → processor compares with stored value → actuator acts *(control)* or data is recorded/alarm raised *(monitoring)* → repeats. The ADC step and the word "continuously" are each explicit marking points.
- **The actuator lives in §3.2.2** (output devices): "an output device that produces movement in response to a signal" — but every question that *uses* one is a §3.2.3 control question.
- **Monitoring vs control** must be distinguishable in one sentence: control systems act on the process; monitoring systems only report it.
- The **moisture ≠ humidity** distinction is examined deliberately.

### Cambridge 9618 (A-Level) — §3.1 monitoring and control

- §3.1's hardware bundle ends with **monitoring and control systems**: know sensors and actuators as the boundary devices and describe the **feedback** idea explicitly — *the system's output influences its next input*. Writing the word "feedback" and meaning it is the A-Level upgrade over IGCSE's step-list.
- Answer in mechanism stages (sensor → ADC → comparison with setpoint → actuator → repeat), and be ready to apply it to an unseen scenario (chemical plant, patient monitor, greenhouse — the scenery changes, the ring does not).
- The rest of §3.1's device operations (printers, VR, storage media, buffers) sit in [[Input and Output Devices]] and [[Secondary Storage]].

### IB Computer Science — A1.3 control systems

- A1.3 pairs **operating systems and control systems**; this card is the control half: the components of a control system (sensor → processor → actuator), open vs closed loop (monitoring vs control in Cambridge's language), and feedback. The OS half is its own machinery.
- IB scenarios lean real-world (traffic lights, climate control, elevators) — lead with the loop diagram and name each stage.

### AP Computer Science A

Not examined — AP CSA is a programming course; hardware control is out of scope.

## Connections

- **Parent:** [[Input and Output Devices]] — the transducer thesis, now pointed at the world instead of a person; the pressure sensor is the resistive touchscreen's heart promoted; the VR headset's motion sensors properly live here, in the loop.
- **Uses:** [[Sound Encoding]] — the acoustic sensor is that card's microphone + ADC chain; [[Secondary Storage]] — "nothing in nature is a number": the sensor chain is the decision-boundary move performed on the whole physical world.
- **Leads to:** [[Embedded Systems]] — seal the loop and its processor into one box and it disappears into a washing machine, a thermostat, a pacemaker: a computer whose entire life is one ring; [[Interrupt Handling]] — the loop's *measure* step is implemented either as a polling loop or as a sensor raising an interrupt.
- **Physics bridge:** the sensor's electrical half is the potential divider of A-Level physics — a thermistor or LDR as the variable leg, read out as a voltage; the magnetic-field row's Hall probe is [[Lorentz Force]] machinery (carriers shoved sideways until a steady voltage reports the field); and **negative feedback** is the same idea biology calls homeostasis.
- **Meta:** [[Decouple and Recouple]] — feedback is engineering's great *deliberate coupling*: output wired back to input on purpose, because here the coupling *is* the product.

## Glossary

| term | 中文 | one-liner |
|---|---|---|
| setpoint | 设定值 | the stored target the processor compares readings against |
| threshold | 阈值 | a boundary value that triggers a decision |
| feedback loop | 反馈回路 | output routed back to become part of the next input |
| negative feedback | 负反馈 | response opposes the deviation — stabilises |
| positive feedback | 正反馈 | response amplifies the deviation — runs away (the microphone screech) |
| calibration | 校准 | mapping raw sensor counts onto physical units |
| relay | 继电器 | a small signal throwing a big switch |
| data logger | 数据记录仪 | a monitoring system that records readings over time |
| hysteresis / dead band | 滞回 / 死区 | two thresholds with a gap, so noise cannot machine-gun the actuator |
| PID control | PID 控制（比例-积分-微分） | respond to the error's size, history, and trend — the grown-up loop |

## LaTeX Reference

| Symbol        | Meaning                                 | Notes                                            |
| ------------- | --------------------------------------- | ------------------------------------------------ |
| $g$           | gravitational acceleration              | the steady 1 g an accelerometer feels at rest    |
| $g\sin\theta$ | gravity's component along a tilted axis | how reading the axes reads the direction of down |

*(Otherwise readings and setpoints use plain units: °C, %, pH, lux.)*
