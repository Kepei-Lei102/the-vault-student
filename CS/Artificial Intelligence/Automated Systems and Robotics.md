---
chinese: 自动化系统与机器人 (zìdònghuà xìtǒng yǔ jīqìrén)
prerequisites:
  - "[[Sensors and Control Systems]]"
  - "[[Embedded Systems]]"
  - "[[Input and Output Devices]]"
leads_to:
  - "[[Artificial Intelligence]]"
  - "[[Ethics and Ownership]]"
tags:
  - subject/computer-science
  - domain/computer-architecture
  - domain/artificial-intelligence
  - level/IGCSE
  - curriculum/Cambridge-0478
  - syllabus/0478-6-1
  - syllabus/0478-6-2
  - type/deep
  - misconception/automated-means-computerised
  - misconception/robot-must-be-autonomous
  - misconception/sensor-decides
  - misconception/advantage-for-everyone
---

# Automated Systems and Robotics 自动化系统与机器人

> *In 1961 a one-armed machine called Unimate began lifting red-hot die castings out of a press at a General Motors plant in New Jersey and dropping them into a cooling bath, over and over, all shift, without a person near it. It had no eyes and no brain worth the name: a drum of instructions, a hydraulic arm, and switches that told it where the arm was. Every robot since is that machine with better senses and a longer program. And every question about robots, from the factory floor to the operating theatre, is the same question Unimate raised on its first day: what does the machine do better than the person it replaced, what does it do worse, and who, exactly, is better off?*

## Definition

### Formal

An **automated system** is a system in which **sensors**, a **microprocessor** and **actuators** work in collaboration so that actions are carried out **without human intervention**: the sensors provide repeated measurements, digitised through an ADC when their output is analogue, to the microprocessor, the microprocessor compares them with stored values and decides, and the actuators carry the decision out, changing the very quantities the sensors are measuring, so that the ring runs again.

**Robotics** is the branch of computer science that incorporates the **design, construction and operation of robots**. A **robot** is a machine with three characteristics: a **mechanical structure or framework**; **electrical components**, namely sensors, a microprocessor and actuators; and it is **programmable**, following instructions that can be changed. Most robots can also **move**, or move part of themselves. Examples: factory arms, domestic robots such as vacuum cleaners, drones.

### Intuitive

An automated system is a ring with no person in it. Something in the world is measured, a chip compares the measurement with what it wants, and a motor or valve or heater pushes the world toward it. Then the measurement is taken again. A thermostat is the smallest one; a self-driving tractor turning at the end of a field is the same ring with a bigger actuator.

A robot is an automated system that has been given a **body**. The syllabus's three characteristics are three layers: a framework to stand on (mechanical), senses, a brain and muscles wired through it (electrical), and instructions the brain follows (programmable). The layer people forget is the first: a smart speaker has a chip and a program, but no framework and nothing that moves, and so it is not a robot. The layer people over-demand is the third: "programmable" means it *follows* a program, not that it thinks, learns or steers itself. A surgical robot whose every movement is a surgeon's hand at a console is a robot; the autonomy is optional, the body is not.

### 中文锚点

把空调设到 26 度就去睡觉。一整夜没人按任何按钮，房间却一直在 26 度上下：传感器测出室温，一块小芯片把它和 26 度比较，室温高了就开压缩机；房间凉下来，传感器报出新的温度，芯片再比一次。测量、比较、执行、再测量——执行改变的恰好就是被测量的那个量，所以这个环自己就能一直转下去，里面不需要人。"自动化"就是这个意思：从测量到动作的这个环，自己合上了。机器人就是给这个环装上了身体。扫地机器人的碰撞板碰到椅子腿，芯片决定转向，轮子电机把它转过去，碰撞板再接着探。它之所以算机器人，是因为它有机械的骨架和能动的部件，有负责感知、判断、执行的电气部件，还有一套可以修改的程序；它并不需要会思考、会自己拿主意。智能音箱有芯片有程序，却没有任何能动的部件，所以不是机器人；而完全由外科医生的双手操控的手术机械臂，仍然是机器人。

---

## Part I — The collaboration: three roles, one ring

The sensor, the microprocessor and the actuator each do one thing, and the exam's favourite six marks are simply the three things in order, with the ring closed at the end.

![[automated-systems-loop.svg|760]]

- **The sensor measures.** It turns a physical quantity into a signal and provides readings repeatedly. Analogue sensor signals need an **ADC** before digital processing; a digital sensor can supply digitised readings directly. It does not decide anything; a sensor that "detects the bowl is empty" is a sensor plus a decision that belongs to the next box. The fourteen kinds, what each one actually transduces, and the analogue-to-digital step in between are in [[Sensors and Control Systems]]; here it is enough to pick the right one for the quantity in the scenario (a **level** or **moisture** sensor for a water bowl, a **proximity** or **infra-red** sensor for a fence three metres ahead, a **temperature** sensor for a 40 °C alert).
- **The microprocessor compares and decides.** It receives the reading, compares it with a **stored value** or range (10 cm, 3 m, 40 °C, "the bowl is below the line"), and, depending on whether the reading is inside or outside the range, either does nothing or **sends a signal**. That signal is the decision. The microprocessor is a single-chip CPU, the same one that runs the [[Embedded Systems]] in your washing machine.
- **The actuator acts.** A motor, a valve, a pump, a heater, a relay: the electrical signal becomes a **physical** change. Then, and this is the step that makes it a system rather than a chain, the change is felt by the sensor on the next reading, and **the process repeats until the system is switched off**.

Recall from [[Sensors and Control Systems]] that a ring whose action changes the measured quantity is a *control* system, and a chain that ends in a display or an alarm is *monitoring*. Both count as automated systems in the syllabus's sense; the weather station that sends an alert above 40 °C is automated (no human reads the thermometer) its output is information rather than a physical control action, so the message is not an actuator.

**What "automated" means, in one line.** A system (or a robot) is automated when it **performs actions without human intervention**. The point is not that a computer is involved, a calculator involves a computer; the point is that the loop from measurement to action closes by itself.

## Part II — What makes a robot a robot

![[automated-systems-robot-anatomy.svg|800]]

The three characteristics are a checklist, and the questions that catch students are the ones that ask you to run it on something that is *not obviously* a robot, or that *is* one for a reason other than you expected.

| Layer | What it means | The tell |
|---|---|---|
| **Mechanical structure** | a framework the parts are mounted on: an arm and its joints, a chassis and wheels, a drone's frame and rotors | something *shaped to act* on the world, not merely a case |
| **Electrical components** | sensors (to measure), a microprocessor (to decide), actuators (to move) | the automated-system ring from Part I, now on board |
| **Programmable** | it follows stored instructions, and the instructions can be changed | the same arm welds a car door today and a boot lid tomorrow after a re-program |

Two things are deliberately **not** on the list. **Autonomy**: a drone is a robot whether it flies itself or a person flies it with a controller, and the surgical robot in a hospital, whose movements are controlled by a surgeon at a console, is a robot. **Intelligence**: "programmable" means the program *can be changed*, not that the robot changes it. A robot that can adapt its own processes has been given [[Artificial Intelligence]] on top, and the syllabus keeps that as a separate idea, which is why so many exam questions end with "the robot is upgraded with machine learning; explain how it helps".

Run the checklist on a **smart speaker**: it is programmable and it has a microprocessor and a microphone, but it lacks the mechanical structure for robotic movement. Its loudspeaker does convert an electrical signal into physical vibration, so “no actuators” would be misleading. A speaker cone moving does not by itself make the device a robot. Run it on a **self-driving tractor**: wheels, engine and framework (mechanical), sensors, microprocessor and the actuators that steer and brake (electrical), a program that turns at each end of the field (programmable). Three for three.

Where do the words come from? **Robot** entered English in 1920 from Karel Čapek's play *R.U.R.*, from the Czech *robota*, forced labour, and the robots in the play are artificial workers who eventually rise. **Robotics** was coined by Isaac Asimov in a 1941 story; his Three Laws followed a year later, and they are fiction, not engineering: no real robot has ever been able to evaluate "harm to a human being" as a predicate. The real discipline is younger than both words. It began with Unimate in 1961, a hydraulic arm programmed by moving it through its motions once and recording the joint positions on a magnetic drum, and grew a proper research arm at Stanford in 1969, the first electric, computer-controlled six-jointed arm, whose descendants weld nearly every car body on Earth.

## Part III — The scenarios, and who is better off

The syllabus lists scenarios for automated systems (industry, transport, agriculture, weather, gaming, lighting, science) and roles for robots (industry, transport, agriculture, medicine, domestic, entertainment), and asks for advantages and disadvantages **for a given scenario**. The pattern that scores is not a memorised list but a habit: name the **sensor and actuator** the scenario uses, and then ask the advantage-and-disadvantage question **from a named person's point of view**, because the same fact is an advantage to one party and a disadvantage to another. A robot that plants seeds all night is a saving to the farmer and a lost job to the labourer. Mark schemes are written that way, "advantage to the employees", "disadvantage to the owner", "drawback to the elderly customers", and an answer written from the wrong seat scores nothing.

| Scenario | Sensor → output | Advantages (to whom) | Disadvantages (to whom) |
|---|---|---|---|
| **Industry**: a welding cell, a bottling line with a flow sensor | proximity, pressure, flow → arm, valve, conveyor motor | *workers*: no lifting, no danger, no monotony, time for skilled work; *owner*: 24/7, consistent quality, lower wage bill | *owner*: high purchase and set-up cost, maintenance needs experts, production stops if it fails; *workers*: jobs lost, deskilling |
| **Transport**: a self-driving tractor, an automated train, a delivery robot | infra-red, proximity, accelerometer, GPS → steering, brakes, motors | *operator*: no fatigue, runs at night, precise routes; *customer*: delivery to those who cannot travel | *everyone*: a malfunction is a moving hazard; *workers*: fewer drivers; *customers*: mistrust, less human contact |
| **Agriculture**: an automated water bowl, a seed-planting robot, a greenhouse | level, moisture, humidity, light → pump, valve, drill, heater | *farmer*: accurate placement, works 24/7, no boredom, frees the farmer for other tasks, safer round animals | *farmer*: expensive, needs training, if it breaks the job is done by hand again, cannot adapt to an unexpected event, a fault can damage the crop |
| **Weather**: a station logging and alerting | temperature, humidity, pressure, light, level → an alert, a logger | *staff*: no overnight or outdoor duty in bad weather, no mundane readings, maintenance jobs created | *staff*: deskilling, jobs replaced; a broken sensor logs nonsense for weeks |
| **Gaming**: motion-tracked controllers and VR headsets | accelerometer, gyroscope, infra-red camera → haptic motors, the display | *player*: natural control, immersion, physical play | *player*: cost, motion sickness, the room must be cleared; systems misread movement |
| **Lighting**: streetlights and room lights that switch themselves | light, motion (infra-red) → relay, dimmer | *owner*: energy saved, lights only when needed, no one walks the street at dusk | *owner*: set-up cost; *user*: lights go off while you sit still; false triggers |
| **Science**: a lab that titrates, samples or monitors a reactor by itself | pH, temperature, level, flow → pumps, valves | *scientist*: precise, repeatable, tireless, safe with hazardous material, records everything | *scientist*: expensive, needs calibration and experts, a wrong stored value ruins every run identically |

And the robot roles the syllabus adds, with the one advantage and the one disadvantage each keeps producing in questions:

- **Medicine**: a surgical robot controlled by a surgeon. Assess the described system: precise instrument control is a potential advantage; purchase cost, specialist training and technical failures are limitations. A **remote-operation** scenario additionally raises network delay and loss of connection. Remote operation is not a defining feature of every surgical robot, and a robot does not remove the need for a trained surgical team.
- **Domestic**: the robot vacuum cleaner. Advantages: it works while you are out, it never tires of a boring task. Disadvantages: it cannot handle the unexpected (a cable, a step, a sock), it costs more than a broom, it needs maintenance.
- **Entertainment**: a toy robot animal that walks and stops 10 cm from an object. Advantages: engaging, safe play. Disadvantages: limited, fragile, expensive to replace.
- **Transport and delivery**: grocery robots for elderly customers. Benefit *to the supermarket*: more customers, several orders a trip. Drawback *to the customers*: less exercise, mistrust of technology, stress at the handover, no human to talk to.

The eight ideas that generate almost every mark, so you can build an answer instead of recalling one:

> [!tip] The advantage engine
> A machine in the ring does not **tire**, get **bored**, need **breaks** or **wages**, and it does the same thing the same way every time (**accuracy**, **consistency**). It can go where people should not (**danger**: heat, radiation, animals, a reactor) and it frees the person for **other work**. Choose the three that fit the scenario and say them from the right seat.

> [!warning] The disadvantage engine
> It **costs** a great deal to buy, install and **maintain**, and the people who can fix it are rare. When it **malfunctions** everything it was doing stops, or goes wrong identically until someone notices. It **cannot adapt** to an event its program did not anticipate. And it changes people: **jobs** go, skills fade (**deskilling**), and the ones who keep their jobs need **retraining**.

## Where it is the working tool

- **The car body.** A modern body shop runs several hundred six-axis arms that spot-weld, seal and paint with no person on the line; the arms' descendants of the Stanford Arm place each weld within a fraction of a millimetre, every shift, which no human welder can do for eight hours. This is the syllabus's *industry* row made of steel, and its economics are why the syllabus lists "expensive to purchase" as the disadvantage and "consistent, 24/7" as the advantage in the same breath: a welding cell installed at about $200 000 that replaces two and a half shifts of labour pays for itself in roughly two and a half years at a $40 000 wage, and in six at half that wage. The break-even calculation is in the hands-on, with every assumption written down, because the answer moves with the wage, which is why automation arrives in rich countries first.
- **The warehouse.** Amazon's fulfilment centres run more than three quarters of a million mobile robots descended from the Kiva system it bought in 2012: instead of a picker walking to a shelf, the shelf drives to the picker, guided by a camera reading a grid of stickers on the floor and a proximity ring to stop before anything living. The person is still in the loop, but the walking, twelve miles a shift, is gone.
- **The operating theatre.** The da Vinci system, approved in 2000, is the exam's surgical robot: the surgeon sits at a console, the robot's wrists move inside the patient through keyhole ports, and tremor is filtered out in software. Over twelve million procedures have been done on it. It is not autonomous; it is a robot because it has the three layers.
- **The sky.** Zipline's fixed-wing drones have carried blood and vaccines to rural clinics in Rwanda since 2016, launched by catapult, flown by GPS and an inertial sensor, and landed by a hook; a delivery that took a four-hour drive takes fifteen minutes. The Rwandan government's decision was the syllabus's *medicine* row and *transport* row at once.
- **The living room and the street.** The Roomba (2002) is Part I's ring with a bump sensor, a cliff sensor and two wheel motors, and its floor-covering policy is the random-angle bounce of the hands-on, chosen because it needs no map. Adaptive traffic signals (the SCOOT system, in use since the 1980s) count vehicles with inductive loops in the road and re-time the lights every cycle; nobody stands at a junction with a stopwatch.

## Hands-on

The script `automated-systems-sim.py` beside this note runs three experiments, and each one is a sentence above made checkable.

**1. The exam's robot in a room.** A robot moves forward until its proximity sensor reads 10 cm or less, then turns: sensor, compare with a stored value, actuator. In a 4 m by 3 m room with a table, a bookcase and a bench, the syllabus's own rule, *turn right 90°*, sends the robot along the wall into a **closed loop of 12.5 m that it repeats forever**, having seen 14.5 % of the floor. Change one line, turn by a random angle between 90° and 270°, and after 300 m of travel it has covered about 90 % of the floor (47 % after 50 m, 96 % after 300 m in a second run, 99.9 % after a kilometre). Same sensor, same microprocessor, same actuator; this is what **programmable** buys, and it is why a real floor robot bounces instead of turning square.

![[automated-systems-coverage.svg|880]]

**2. One sensor versus a vote.** A proximity sensor reading a 50 cm gap at a hundred readings a second, with a glitch (a reflection, dust, a loose wire) that reads 5 cm once in every thousand readings, will stop the machine **360 times an hour** for nothing. Two sensors that must both agree glitch together only $p^2$ of the time: **0.4 false stops an hour** (0.5 simulated). Three that vote two-out-of-three: about one an hour, and, unlike the pair, they still stop for a *real* object when one sensor has died and reads 50 cm forever. This is the arithmetic behind "if it malfunctions", and behind the worst automated-system failure of the century, below.

![[automated-systems-voting.svg|720]]

**3. Break-even.** With the assumptions stated in the script (robot $150 000, integration $50 000, maintenance and energy $18 000 a year, replacing two and a half workers at $40 000), the cell pays for itself in **29 months**; at half the wage, **75 months**. Change any number and watch the verdict move; that sensitivity is the honest content of "expensive to purchase".

![[automated-systems-manim.mp4]]

*The two films: the exam's robot under the two rules, sensor reading and decision shown at every turn; then three sensor traces, and the count of false stops with and without the vote.*

## Worked examples — every tool named

### Example 1 — the six-mark skeleton (Cambridge 0478, June 2023 Paper 11, Q5)

*A farm has an automated drinking system: when the water bowl is empty it is automatically refilled. The system uses a sensor and a microprocessor. (a) Identify the most appropriate sensor. [1] (b) Describe how the sensor and the microprocessor are used to automatically refill the bowl. [6]*

*Tool: match the sensor to the quantity.* The quantity is how much water is in the bowl: a **level** sensor (pressure or moisture also accepted). **(a)** Level sensor.

*Tool: the Part I ring, in order, with the ring closed.* **(b)** The sensor **continually sends digitised data** to the microprocessor (1). The microprocessor **compares** the data with a **stored value** for the empty level (1). If the reading is below the stored value / outside the range, the microprocessor **sends a signal** to release water (1), using an **actuator** to open the valve (1). The bowl is filled by a set amount or for a set time, or until the reading matches the full value (1). **The process repeats** until the system is switched off (1). Six points, six marks; the scheme's list is exactly these. Students who write "the sensor detects that the bowl is empty and refills it" have given the sensor two jobs it does not have and left out the microprocessor's comparison, the actuator and the repeat.

### Example 2 — the definition, the checklist, the fence and both engines (Cambridge 0478, June 2024 Paper 11, Q8)

*A farmer uses an automated robot to plant seeds. (a) State what is meant by the robot being automated. [1] (b) Give three characteristics of a robot. [3] (c) The robot stops when it reaches a fence, turns and continues. Explain how the robot uses sensors and a microprocessor to know it has reached a fence. [6] (d) Give two advantages of the farmer using an automated robot to plant seeds. [2] (e) Give two disadvantages. [2] (f) The robot is adapted to have machine-learning capabilities. Explain how this helps. [2]*

**(a)** *Tool: the definition.* It can perform actions **without human intervention**.

**(b)** *Tool: the three layers.* Mechanical structure or framework; electrical components; programmable (the scheme also accepts "it can move").

**(c)** *Tool: the ring, with the right sensor and the trigger stated.* A **proximity** sensor is used (1); it continuously sends digitised data to the microprocessor (1); the microprocessor compares the data with a stored value or range for the fence distance (1); if the value is within the range the robot continues planting (1); if outside, the microprocessor sends a signal to stop or turn the robot (1), using an **actuator** (1); the process repeats until switched off (1). Any six.

**(d)** *Tool: the advantage engine, from the farmer's seat.* More accurate planting; works 24/7 without breaks; does not get bored of a repetitive task; frees the farmer to do other work; faster; no wages to pay.

**(e)** *Tool: the disadvantage engine, same seat.* Expensive to buy; costly maintenance; the farmer may need training; if it breaks the farmer plants by hand; it cannot adapt to an unexpected event (the scheme also accepts deskilling and lost jobs, which are disadvantages to the workers rather than to the farmer, so the safer choices are the ones the farmer feels directly).

**(f)** *Tool: machine learning is a program adapting its own data and rules.* The robot can adapt its own rules and processes from experience (1), so it becomes more efficient, for instance by remembering where the fence and the obstacles are, or the best route across the field (1). This is the [[Artificial Intelligence]] card's definition, and "it learns" alone scores nothing; the mark is for *what* it changes about itself.

### Example 3 — three components, a named distance, and the drawbacks explained (Cambridge 0478, March 2024 Paper 12, Q6)

*A self-driving tractor sows seeds and harvests crops, moving through the field, turning at each end. (a) One reason it is a robot is its mechanical structure. Give one other reason. [1] (b)(i) If a person is detected within 3 metres while moving, the tractor must stop. Explain how an infra-red sensor, microprocessor and actuator can be used to stop the tractor. [5] (b)(ii) Identify one other sensor the tractor might use and how. [2] (c) Explain the drawbacks of a farmer using a self-driving tractor. [3]*

**(a)** Electrical components, or programmable.

**(b)(i)** *Tool: the ring with three named boxes and the numbers from the question.* The infra-red sensor continuously sends the digitised reading to the microprocessor (1); the microprocessor compares it with the stored data for a person and the 3 m distance (1); if a person is within 3 m (1), a signal is sent to the **actuator** to apply the brakes (1); if not, no action is taken, and once the person is more than 3 m away a signal restarts the tractor (1); the process repeats until switched off (1). Any five. The question handed you the three boxes and the threshold; the marks are for wiring them in order.

**(b)(ii)** *Tool: a sensor and a matching use, one mark each.* An **accelerometer** to detect uneven ground or a crash; a **proximity** sensor to detect the end of the field or an obstacle; a **light** sensor to switch the headlights on. A sensor without its use is one mark of two.

**(c)** *Tool: the disadvantage engine, and "explain" means point plus consequence.* High set-up and maintenance cost, needing skilled experts to fix (1); the farmer needs re-skilling and may need fewer employees, leading to unemployment (1); it can malfunction, and a tractor that fails to recognise a person does not stop (1). Three points with their consequences.

### Example 4 — running the checklist backwards (Cambridge 0478, November 2025 Paper 12, Q7(a))

*A house has a smart speaker that takes voice commands. The smart speaker cannot be described as a robot. Explain why. [3]*

*Tool: the three layers, applied to something that fails them.* It does not have a mechanical structure or framework (1); it has no actuators (1), so it cannot move itself or act on anything (1). A speaker cone technically moves, but for an audience of eardrums, not to change the physical world; that is why it does not count as an actuator (the distinction is drawn in [[Sensors and Control Systems]]). Note what the answer does *not* say: "it is not intelligent" is irrelevant, because intelligence is not a characteristic of a robot.

### Example 5 — the seat matters (Cambridge 0478, November 2023 Paper 12, Q11(b),(c))

*A manufacturing company uses an automated system. (b) Explain one advantage to employees of using an automated system in manufacturing. [2] (c) Explain one disadvantage to the company owner. [2]*

*Tool: pick the engine, then the seat, then give point plus explanation.* **(b)** *To employees*: safety increases (1) because workers no longer go into dangerous areas to take readings or do dangerous tasks (1). Or: no repetitive tasks, so their time goes to more skilled work. **(c)** *To the owner*: high installation cost (1), so a large sum is needed up front and staff need training (1). Or: maintenance and utility costs rise, and skilled staff must be employed to keep it running. Writing "workers lose their jobs" under (c) is a true sentence in the wrong seat.

### Example 6 — the surgical robot (Cambridge 0478, June 2025 Paper 12, Q5(b))

*A hospital has a robot used to perform surgery; a doctor controls the robot from a different location. (i) One feature of the robot is that it has electrical components. Give two examples. [2] (ii) Explain the advantages of using the robot to perform surgery. [4] (iii) Explain one disadvantage. [2]*

**(i)** Sensors, microprocessor, actuators; any two.

**(ii)** *Tool: think through the ring.* The surgeon need not travel (1), so any specialist in the world can operate, at once, rested, and without travel costs (1). The robot is more precise (1), so incisions are smaller, recovery is shorter, and the instruments entering the body can be smaller than a human hand (1). It is safer and more hygienic, since the surgeon need not be near an infectious patient. Any four, in point-and-consequence pairs.

**(iii)** *Tool: the ring has a network in it now.* The internet connection could be lost or delayed (1), so the surgery may not be able to continue (1). Or: the robot could be hacked, endangering the patient; data corrupted in transmission changes the instruction; the hardware could malfunction mid-operation; the cost could have gone to other care. Notice that the exam's *teleoperated* robot, with a person controlling every move, is still called a robot: autonomy is not on the list.

### Example 7 — a benefit and a drawback, each from a different seat (Cambridge 0478, November 2025 Paper 11, Q5(a)–(c))

*A supermarket wants to deliver groceries to elderly people using robots. (a) Describe the characteristics of a robot. [3] (b) Explain one benefit to the supermarket. [2] (c) Explain one drawback to the elderly customers. [2]*

**(a)** A mechanical structure or framework; electrical components such as sensors, a microprocessor and actuators; programmable; and it can move.

**(b)** *Seat: the business.* It may gain customers (1), because elderly people who could not get to the store can now shop there, raising sales (1). Or: several orders delivered in one trip, so customers are served more efficiently.

**(c)** *Seat: the customer.* They get less exercise (1), since they no longer walk to and round the store, which may harm their health (1). Or: they may struggle with or mistrust the technology, causing stress at the handover, or they would rather see a person. The drawback to the *customers* is not "the robots are expensive"; that is the supermarket's problem.

## Common Misconceptions (Teaching Notes)

### 1. "Automated means it has a computer in it"

A calculator has a microprocessor and is not automated; a Victorian steam governor has no computer and is. **Fix:** the test is *does the loop close by itself?* Measurement to action with no human reading, deciding or pressing. Say "without human intervention" in every definition.

### 2. "A robot has to be autonomous, or intelligent, or look like a person"

Students deny that the surgical robot or a remote-controlled drone is a robot, and grant the title to a chatbot. **Fix:** run the three-layer checklist out loud, and note what is *not* on it. Then run it on the smart speaker (fails two layers) and the tractor (passes three). Programmable means the program can be changed, not that the machine changes it.

### 3. "The sensor detects the fence and stops the robot"

The sensor has been given three jobs: measuring, deciding and acting. **Fix:** three boxes, three verbs. The sensor *sends data*; the microprocessor *compares with a stored value and sends a signal*; the actuator *moves*. An answer that names all three, in that order, and ends with "repeats until switched off" is the six-mark answer; one that lets the sensor decide is worth one.

### 4. "An advantage is an advantage"

"It saves money on wages" written as an advantage *to the employees*. **Fix:** before writing, name the seat: employee, owner, farmer, patient, customer. Then ask what *that person* gains or loses. The same fact flips sign between seats, and the mark scheme is written from the seat the question names.

### 5. "Explain" answered as "give"

"Expensive" for two marks. **Fix:** point, then consequence, joined by "so" or "because": "expensive to install, *so* the company needs a large sum up front". Every two-mark explain in this topic is a point and its consequence.

### 6. "Machine learning helps because it makes the robot better"

**Fix:** say what it adapts: its own data, rules or processes, from the readings it collects. Then a consequence in the scenario: it remembers the fence, maps the field, learns the route, makes fewer errors. The general sentence scores the first mark; the scenario-specific consequence scores the second.

## Exam Notes

### Cambridge 0478 (§6.1 Automated systems, §6.2 Robotics — Paper 1)

Five learning outcomes across the two subsections. **6.1.1**: describe how sensors, microprocessors and actuators are used in collaboration to create automated systems. **6.1.2**: describe the advantages and disadvantages of an automated system for a given scenario, from industry, transport, agriculture, weather, gaming, lighting and science. **6.2.1**: understand what robotics is (the branch of computer science incorporating the design, construction and operation of robots; examples include factory equipment, domestic robots and drones). **6.2.2**: describe the characteristics of a robot (mechanical structure or framework; electrical components such as sensors, microprocessors and actuators; programmable). **6.2.3**: understand the roles robots perform (industry, transport, agriculture, medicine, domestic settings, entertainment) and describe the advantages and disadvantages of their use.

What the papers do with it, checked across every sitting from June 2023 to June 2026: one question a paper, six to fourteen marks, always in a scenario (a water bowl, a seed robot, a tractor, a weather station, a surgical robot, a delivery robot, a toy animal, a drone, a smart speaker). The parts are stable: *state what automated means* (1, "without human intervention"); *give n characteristics* (2–3, the three layers plus "can move"); *explain how the sensor, microprocessor and actuator…* (4–6, the Part I skeleton with the scenario's sensor and threshold); *advantages and disadvantages to a named party* (2 each, point plus consequence when the verb is "explain"); and a closing part that hands the robot machine learning or an expert system, which is §6.3's territory and is answered with [[Artificial Intelligence]]'s definitions. The sensor-choice mark uses the [[Sensors and Control Systems]] table; the microprocessor definition ("an integrated circuit that performs all the functions of a CPU on a single chip") appears as a one-mark aside. Movement is accepted as a characteristic; autonomy and intelligence are not.

### Where it is *not* examined

- **Cambridge 9618 (A-Level)** has no automated-systems or robotics section; §3.1 examines *monitoring and control systems*, sensors, actuators and feedback, which is [[Sensors and Control Systems]], and §18.1 examines the learning, which is [[Artificial Intelligence]]. A 9618 answer about a robot is an answer about feedback and, if asked, about machine learning.
- **IB Computer Science** examines control systems under A1.3 (components, open and closed loop, feedback), again [[Sensors and Control Systems]]; there is no robotics topic.
- **OxfordAQA International GCSE (9210)** and **AQA A-level (7517)** have no automated-systems or robotics content; **AP Computer Science A** has none.

---

## Connections

- **Builds on:** [[Sensors and Control Systems]] — the sensor table, the ADC, monitoring against control, feedback, hysteresis and PID, all assumed here and not retold; [[Embedded Systems]] — the microprocessor in the ring is an embedded computer, with the same "single function, dedicated hardware" test the exam runs on the smart speaker; [[Input and Output Devices]] — the boundary between a sensor and an input device, and between an actuator and an output device.
- **Extends into:** [[Artificial Intelligence]] — the closing part of nearly every robotics question: what changes when the program can change itself; [[Ethics and Ownership]] — jobs, deskilling and who is accountable when the automated system fails.
- **Sibling:** [[Interrupt Handling]] — the factory robot's interrupts (a hardware fault, an emergency stop, a low battery) in the June 2025 question; [[Networks]] and [[Error Detection and Correction]] — the surgical robot's disadvantage is a network's disadvantage, and the March 2024 tractor's data went home under an echo check.
- **Physics bridge:** the actuator is a motor, and the motor is [[Lorentz Force]] machinery; the drone's hover is the PID loop of [[Sensors and Control Systems]] run on the accelerometer's report of [[Newton's Laws of Motion]].
- **Meta:** [[You Are a Reinforcement Learner]] — the environment scores the action and the score reshapes the next; an automated system is the same ring with the rules fixed, a learning robot is the ring with the rules adjustable.

---

## Beyond Syllabus

### The failure not to skip: one sensor, 346 people
Recall that an automated system acts on what its sensor tells it without a human in the ring. The Boeing 737 MAX carried an automated system, MCAS, that pushed the nose down when an angle-of-attack sensor reported the aircraft near a stall. It read **one** sensor. On Lion Air 610 (October 2018) and Ethiopian 302 (March 2019) that sensor gave a false reading, the system pushed the nose down repeatedly, and the pilots, who had not been told the system existed, could not out-pull it. 346 people died and the type was grounded worldwide for twenty months. The hands-on's second experiment is this accident's arithmetic: a glitch believed by one sensor happens $np$ times, by two only $np^2$. The fix that returned the aircraft to service reads both sensors and disengages when they disagree. Every "if it malfunctions" mark in the syllabus is a small version of this paragraph.

### The ironies of automation
Lisanne Bainbridge's 1983 paper observed that automating the routine parts of a job leaves the human with only the hardest parts, the ones the machine could not do, and at the same time takes away the practice that kept the human able to do them. The nuclear-plant operator who has watched an automatic system for a year is the person least ready to take over when it fails, at the moment it matters most. This is what the syllabus's word **deskilling** actually costs, and why Fukushima in 2011 is on the timeline: the robots sent into the reactor buildings failed on stairs and in the radiation, and the people had to go in.

![[automated-systems-timeline.svg|960]]

### Why a robot vacuum bounces, and what a map costs
The random-angle bounce covers a floor without knowing where it is, and pays for that ignorance in distance: 300 m to cover 90 % of a 12 m² room. A robot that builds a map as it moves, called SLAM (simultaneous localisation and mapping), fuses odometry from its wheels with a laser rangefinder or a camera, keeps an estimate of its own position that it corrects every time it re-sees a landmark, and then cleans in straight lanes. The same ring, with a memory added between the sensor and the decision; the cost is a laser, a faster processor and software that took the field twenty years to get right.

### Degrees of freedom, and why arms have six
A rigid tool in space needs three numbers to say where it is and three to say which way it points: six degrees of freedom, so a general-purpose arm has six joints. The Stanford Arm of 1969 had them; a welding robot has them; your own arm has seven, the redundancy being why you can hold a cup still while moving your elbow. Fewer joints and there are places the tool cannot reach or angles it cannot take; more, and the program has choices to make.

### Moravec's paradox
Chess fell to computers in 1997 and folding laundry has not. The tasks that feel hard to people (arithmetic, search, planning) are cheap for a machine, and the ones that feel effortless (seeing, walking on stairs, picking up an unknown object) are the expensive ones, because evolution spent a billion years on them and left no notes. It is why the factory arm arrived in 1961 and the household robot that clears a table has not, and why every syllabus "cannot adapt to an unexpected event" bullet is, underneath, a statement about how far robotics still has to go.

---

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $np$ | `np` | expected false triggers from one sensor over $n$ readings |
| $np^2$ | `np^2` | from two sensors that must agree |
| $3np^2$ | `3np^2` | from three sensors voting two of three |
