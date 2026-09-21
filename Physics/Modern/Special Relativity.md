---
chinese: 狭义相对论 (xiáyì xiāngduìlùn)
prerequisites:
  - "[[Pythagoras Theorem]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Maxwell's Equations]]"
  - "[[Doppler Effect]]"
leads_to:
  - "[[General Relativity]]"
tags:
  - subject/physics
  - domain/relativity
  - domain/modern-physics
  - level/IB-HL
  - level/university
  - curriculum/IB-Physics
  - type/theory
  - type/derivation
  - type/visual-tool
  - notation/gamma
  - notation/beta
  - misconception/moving-clocks-are-faulty
  - misconception/time-dilation-is-an-illusion-of-light-delay
  - misconception/simultaneity-is-absolute
  - misconception/mass-increases-with-speed
  - misconception/proper-time-is-always-the-earth-time
---

# Special Relativity 狭义相对论

> You are in the back seat of a car doing 100 km/h, and you throw a ball forwards at 20 km/h. Someone at the roadside sees the ball doing 120. Nobody needs a physics course to know that.
>
> Now switch on the headlights. The light leaves the car at 300 000 km/s. The person at the roadside measures that light too, and gets 300 000 km/s. Not 300 000 plus the car. The same number.

## The problem

That second paragraph is an experimental fact, checked over and over since the 1880s, and it is absurd. Speeds add. They always have. If the light is doing $c$ relative to the car, and the car is moving, the road should see something else.

The equations of electromagnetism had hinted at it first. [[Maxwell's Equations]] give the speed of light as $1/\sqrt{\mu_0 \varepsilon_0}$, built from two constants measured on a laboratory bench, and the equations do not say *relative to what*. In 1905 Einstein took the formula at its word: the speed of light is a law of physics, laws of physics are the same for everyone moving steadily, so the speed of light is the same for everyone moving steadily.

If that is kept, something else has to go. Speed is distance divided by time. If two observers in relative motion agree on the speed of the same beam of light, they cannot also agree on distances and times. **Special relativity is the working-out of exactly how much they disagree**, and it needs no mathematics beyond Pythagoras.

## Definition

### Formal

An **inertial reference frame** is a system of rulers and synchronised clocks that is not accelerating. An **event** is something that happens at one place and one time: a flash, a collision, a clock striking. It has coordinates $(x, t)$ in one frame and $(x', t')$ in another.

Special relativity rests on two **postulates**:

1. **The principle of relativity.** The laws of physics are the same in every inertial frame. No experiment done inside a closed, steadily moving laboratory can tell you that it is moving.
2. **The constancy of the speed of light.** The speed of light in a vacuum has the same value $c$ in every inertial frame, whatever the motion of the source or the observer.

Everything else follows from these two, through the **Lorentz factor**

$$\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}, \qquad \beta = \frac{v}{c}.$$

### Intuitive

Postulate 1 is old. Galileo noticed that below deck on a smoothly sailing ship, butterflies fly and water drips exactly as they do in harbour. Postulate 2 is the new one, and it is simply postulate 1 applied to electromagnetism: if the speed of light were different in a moving laboratory, measuring it would tell you that you were moving.

The price is that **time and space are not shared**. Each inertial frame has its own time and its own lengths, and $\gamma$ is the exchange rate between them. At every speed you have travelled at, $\gamma$ is $1$ to ten decimal places, which is why nobody noticed for three hundred years.

![[special-relativity-gamma.svg|820]]
*The Lorentz factor. It is indistinguishable from 1 up to about a tenth of the speed of light, reaches 2 at 87 % of it, and grows without limit as $v$ approaches $c$.*

### 中文锚点 (Chinese Anchor)

你坐在时速一百公里的车上，往前扔一个球，路边的人看到球的速度是车速加上你扔的速度，这谁都知道。可是你打开车灯，路边的人去量那束光的速度，量出来的却和你在车上量的一模一样，一点也没有多出车速来。这不是仪器的毛病，而是一百多年来被反复验证过的事实。速度是“走过的距离”除以“花掉的时间”，既然两个人对同一束光量出了同一个速度，那他们量出来的距离和时间就不可能还一样：在路边的人看来，车上的钟走得慢一点，车身也短一点。所以被放弃的是“全世界共用同一个时间”这个想法：每个匀速运动的人都有自己的时间，运动得越快，和别人的时间差得越多。平时感觉不到，只是因为我们的速度和光速相比实在太小。导航卫星上的钟每天都要按这个道理修正，否则手机上的定位一天之内就会偏出十公里。

## Notation

| Symbol | Meaning |
|---|---|
| $S$, $S'$ | two inertial frames; $S'$ moves at velocity $v$ along the $x$-axis of $S$ |
| $c$ | the speed of light in vacuum, $2.998 \times 10^8\ \text{m s}^{-1}$ |
| $\beta = v/c$ | speed as a fraction of the speed of light |
| $\gamma = 1/\sqrt{1 - \beta^2}$ | the Lorentz factor, always $\ge 1$ |
| $\Delta t_0$ (also $\Delta\tau$) | **proper time**: the time between two events measured by a clock that is present at both |
| $L_0$ | **proper length**: the length of an object measured in the frame where it is at rest |
| $\Delta s$ | the space-time interval between two events |

## Galilean relativity — the rule that fails

Let frame $S'$ move at speed $v$ along the $x$-axis of $S$, with the origins together at $t = 0$. Common sense gives the **Galilean transformation**:

$$x' = x - vt, \qquad t' = t,$$

and, from it, the everyday rule for adding velocities: an object moving at $u$ in $S$ moves at $u' = u - v$ in $S'$. Newton's laws keep their form under this change, which is what Galilean relativity means.

The second equation, $t' = t$, is so obvious that for centuries nobody wrote it down. It says there is one universal time. Apply the velocity rule to light and it predicts $c' = c - v$, which is not what is measured. One of the two equations is wrong, and it is the obvious one.

## Time dilation — the light clock

Build the simplest clock there could be: two mirrors a distance $L$ apart with a pulse of light bouncing between them. One tick is one round trip.

![[special-relativity-light-clock.svg|820]]
*Left: the clock in its own rest frame. Right: the same clock seen by someone it moves past. The light must reach a mirror that has moved on, so it travels along a diagonal.*

**In the clock's own frame** the light covers $2L$ at speed $c$, so one tick lasts $\Delta t_0 = 2L/c$.

**In a frame the clock moves through at speed $v$**, let one tick last $\Delta t$. During half a tick the clock moves sideways by $v\,\Delta t/2$, and the light travels along the hypotenuse. By the second postulate it does so **at speed $c$**, so the hypotenuse has length $c\,\Delta t/2$. [[Pythagoras Theorem]] gives

$$\left(\frac{c\,\Delta t}{2}\right)^2 = L^2 + \left(\frac{v\,\Delta t}{2}\right)^2 .$$

Solve for $\Delta t$: $\ (c^2 - v^2)\,\Delta t^2 = 4L^2$, so $\Delta t = \dfrac{2L}{c}\cdot\dfrac{1}{\sqrt{1 - v^2/c^2}}$, which is

$$\boxed{\Delta t = \gamma\,\Delta t_0}$$

A moving clock takes longer between ticks. In Newton's physics the light on the diagonal would simply travel faster, at $\sqrt{c^2 + v^2}$, and the two tick times would agree. The second postulate forbids that, so the time has to give.

![[special-relativity-light-clock.mp4]]
*Two identical light clocks, one at rest and one moving at $0.6c$, for which $\gamma = 1.25$. The light moves at the same speed on both paths. While the clock at rest completes five ticks, the moving one completes four.*

**It is not only light clocks.** Put a wristwatch, a beating heart and a radioactive sample next to the moving light clock. If they drifted out of step with it, the passengers could measure their own speed from the drift, with no window. The first postulate forbids that. So every process in the moving frame slows by the same factor: it is time that runs differently, not one kind of mechanism.

**And it is symmetric.** The passengers see the *ground's* clocks running slow by the same $\gamma$. That sounds like a contradiction and is not, for a reason the section on simultaneity explains: comparing two clocks that are apart needs a judgement about "at the same time", and the two frames make that judgement differently.

## Length contraction

The **proper length** $L_0$ of an object is its length in the frame where it is at rest. Measured from a frame in which it moves at speed $v$ along its length, it is shorter:

$$\boxed{L = \frac{L_0}{\gamma}}$$

**Why, from time dilation.** A rod of proper length $L_0$ lies at rest in $S$, and a traveller flies along it at speed $v$. In $S$ the trip takes $\Delta t = L_0/v$. The traveller's own clock is present at both ends of the trip, so it records the proper time, $\Delta t_0 = \Delta t/\gamma$. To the traveller the rod is what moves, at the same speed $v$, and it takes $\Delta t_0$ to pass. So the traveller measures its length as $L = v\,\Delta t_0 = v\,\Delta t/\gamma = L_0/\gamma$.

Only lengths **along the direction of motion** contract. The light clock's mirror separation $L$ was perpendicular to the motion, which is why the derivation above could use the same $L$ in both frames.

## The relativity of simultaneity

This is the idea that makes the rest consistent, and the one people skip.

A flash goes off at the exact middle of a railway carriage. **In the carriage's frame** the light travels equal distances at equal speeds and reaches the two end walls at the same moment. **On the platform**, the carriage moves at $v$ while the light is in flight. The light still moves at $c$ in both directions, because it always does. The rear wall moves *towards* the flash and the front wall moves *away* from it, so the light reaches the rear wall first.

![[special-relativity-simultaneity.mp4]]
*The same flash in the same carriage, moving at $0.6c$. Above, in the carriage's frame, both walls are reached together. Below, on the platform, drawn to scale with the carriage contracted, the rear wall is reached first and the front wall four times later.*

"The light reaches the rear wall" and "the light reaches the front wall" are two events. They are simultaneous in one frame and not in the other, and neither frame is mistaken. **Two events at different places that are simultaneous in one frame are not simultaneous in a frame moving relative to it.**

This removes the paradox of symmetric time dilation. To say "your clock runs slow" I must compare your one clock against *two* of mine, at two places, which I have synchronised. You do not accept that my two clocks are synchronised. Each of us finds the other's clocks slow, and each of us can explain the other's finding.

## The Lorentz transformation

The Galilean equations are replaced by the **Lorentz transformation**:

$$\boxed{x' = \gamma\,(x - vt), \qquad t' = \gamma\left(t - \frac{vx}{c^2}\right)}$$

Each piece is something already met. The factor $\gamma$ in front carries time dilation and length contraction. The new term $-vx/c^2$ is the relativity of simultaneity: events with the same $t$ and different $x$ get different $t'$. Set $v \ll c$ and $\gamma \to 1$, $vx/c^2 \to 0$, and the Galilean equations come back. Nothing in everyday life is contradicted; it is contained.

**Adding velocities.** An object moves at $u$ in $S$. Dividing $\Delta x'$ by $\Delta t'$ from the two equations gives its velocity in $S'$:

$$\boxed{u' = \frac{u - v}{1 - uv/c^2}}$$

Try $u = c$: $\ u' = \dfrac{c - v}{1 - v/c} = c$. Light moves at $c$ in the new frame too, whatever $v$ is, as the second postulate demanded. Try two rockets approaching each other at $0.6c$ each, so $u = 0.6c$, $v = -0.6c$: $\ u' = 1.2c / 1.36 = 0.882c$, not $1.2c$. No combination of speeds below $c$ ever reaches $c$. [[Hyperbolic Functions]] shows why: there is a quantity, the rapidity, that *does* add, and speed is its $\tanh$.

## What everyone agrees on — the interval

Observers disagree about $\Delta t$ and about $\Delta x$. There is a combination they agree on:

$$\boxed{(\Delta s)^2 = (c\,\Delta t)^2 - (\Delta x)^2}$$

This is the **space-time interval**, and it is **invariant**: substitute the Lorentz transformation into $(c\,\Delta t')^2 - (\Delta x')^2$, and every $v$ cancels.

It is Pythagoras with a minus sign, and that is the right way to think of it. Rotate a sheet of paper and the $x$- and $y$-separations of two dots both change, while $x^2 + y^2$ stays put, because both describe one distance. Change velocity and $\Delta t$ and $\Delta x$ both change, while $(c\Delta t)^2 - (\Delta x)^2$ stays put, because both describe one separation in space-time.

If a clock can be present at both events, then in its frame $\Delta x = 0$, and the interval is $c$ times the proper time: $\Delta s = c\,\Delta t_0$. That is the quickest route to a proper time, and Example 3 uses it.

## Space-time diagrams

Plot $ct$ upwards and $x$ across. Light then travels along lines at $45°$. The path of an object through the diagram is its **world line**. A world line at angle $\theta$ to the $ct$-axis belongs to an object moving at

$$\tan\theta = \frac{v}{c},$$

so nothing material can tilt as far as $45°$.

![[special-relativity-spacetime.svg|820]]
*A traveller moves at $0.6c$. Blue: the traveller's world line, which is the $ct'$ axis. Purple: the $x'$ axis, the set of events the traveller calls simultaneous with O. Both axes tilt towards the light line by the same angle. Events P and Q (teal squares) are simultaneous in the frame at rest; the dash-dot lines, parallel to $x'$, read off the traveller's times for them, and Q comes out $3.6$ s before P. The green curve is $(ct)^2 - x^2 = 16$: it marks 4 s of proper time on every world line through O, so event A, at $ct = 5$ for the frame at rest, is at $ct' = 4$ for the traveller.*

The scales on the tilted axes are not the scale of the paper. The green hyperbola, a line of constant interval, is what carries the scale from one set of axes to the other. The diagram puts the three effects in one picture: the hyperbola shows time dilation, the tilted $x'$ axis shows the relativity of simultaneity, and the two together give length contraction.

## The evidence — muons

Cosmic rays striking the upper atmosphere create **muons**, heavy cousins of the electron, which decay with a mean lifetime of $2.2$ microseconds. Even at the speed of light a muon should cover only about $660$ m in one lifetime.

In 1963 David Frisch and James Smith counted muons of a selected speed, $0.995c$, on top of Mount Washington and again near sea level, $1907$ m lower. At the top they counted $565$ per hour. The descent takes $6.4$ microseconds on the ground's clocks, which is $2.9$ lifetimes, so without relativity only $5\,\%$ would survive: about $31$ per hour. **They counted $409$.**

![[special-relativity-muons.svg|820]]
*Red: the survival expected if a moving muon aged at the ordinary rate. Green: with its clock slowed by $\gamma = 10$. Amber: what was measured.*

At $0.995c$, $\gamma = 10$. In the ground's frame the muon's internal clock runs ten times slow, so it ages $0.64$ microseconds during the descent and $75\,\%$ should survive. The measured $72\,\%$ corresponds to a slowing by a factor of about $9$.

**Now ride with the muon.** In its own frame the muon's clock is perfectly ordinary and it lives $2.2$ microseconds. But the mountain is rushing upwards past it at $0.995c$, and the mountain is length-contracted to $1907/10 = 190$ m, which passes in $0.64$ microseconds. **Both frames predict that the same fraction arrives.** One calls the reason time dilation, the other calls it length contraction, and that is what it means for them to be two views of one thing.

## Where this is the working tool

**Satellite navigation.** Your phone finds its position from the arrival times of signals from satellite clocks, and a nanosecond of clock error is 30 cm of position error. A GPS satellite moves at $3.87\ \text{km s}^{-1}$, so special relativity slows its clock by $7.2$ microseconds a day. It also sits high in the Earth's gravity, which by [[General Relativity]] speeds its clock up by $45.7$ microseconds a day. The net $+38.5$ microseconds a day, left uncorrected, would be $11.5$ km of ranging error per day. The satellites' clocks are built to tick slow by exactly that amount before launch.

**Particle accelerators.** A proton in the Large Hadron Collider at $6.8$ TeV has $\gamma \approx 7250$ and moves $2.9\ \text{m s}^{-1}$ slower than light. The magnets that steer it are designed for a particle with 7250 times the momentum Newton would predict, and the machine would not work otherwise. Unstable particles reach detectors metres away for the muon's reason.

**Magnetism.** The force between two current-carrying wires is what the electric force between their charges looks like after length contraction changes the charge densities, at drift speeds of a fraction of a millimetre per second. [[Lorentz Force]] works through the argument. Special relativity is not only about fast things.

**Atomic clocks in aeroplanes.** In 1971 Joseph Hafele and Richard Keating flew caesium clocks round the world on commercial airliners, once eastward and once westward. Relative to clocks that stayed at home, the eastward clocks lost $59 \pm 10$ nanoseconds and the westward clocks gained $273 \pm 7$, against predictions (special and general relativity combined) of $-40 \pm 23$ and $+275 \pm 21$.

**Light from moving sources.** The formula for the Doppler shift of light differs from the one for sound because time dilation enters it; [[Doppler Effect]] derives it.

**Hands-on.** `special-relativity-model.py`, in the same folder, computes every number quoted here. Change the muon speed from $0.995c$ to $0.9c$ and predict, before running it, whether more or fewer reach sea level, and by roughly what factor.

## Worked examples

### Example 1: whose time is the proper time?

> A spacecraft passes Earth at $0.8c$ on its way to a star $4.0$ light-years away, as measured from Earth. How long does the journey take (a) according to Earth, (b) according to the crew? (c) How far away is the star, according to the crew?

**Tool: $\Delta t = \gamma \Delta t_0$, after deciding which clock is present at both events.** Trigger: two events (passing Earth, reaching the star) and two sets of observers. The ship's clock is at both events, so the *crew* measure the proper time. Earth needs two clocks, one at each end.

(a) $\Delta t = 4.0 / 0.8 = 5.0$ years. (b) $\gamma = 1/\sqrt{1 - 0.64} = 5/3$, so $\Delta t_0 = 5.0 / (5/3) = 3.0$ years. (c) To the crew it is the star that approaches, across a contracted distance $L = 4.0 / (5/3) = 2.4$ light-years. Check: $2.4$ light-years at $0.8c$ takes $3.0$ years, which agrees with (b).

### Example 2: a Lorentz transformation

> In frame $S$ an event occurs at $x = 5.0$ light-seconds, $t = 4.0$ s. Find its coordinates in a frame $S'$ moving at $0.6c$ along $+x$.

**Tool: the Lorentz transformation, in units where distances are in light-seconds so that $c = 1$.** Trigger: one event, coordinates wanted in another frame. There is no single clock or rod to reason about, so the full transformation is needed.

$\gamma = 1.25$. $x' = 1.25\,(5.0 - 0.6 \times 4.0) = 3.25$ light-seconds. $t' = 1.25\,(4.0 - 0.6 \times 5.0) = 1.25$ s.

Check with the interval: $4.0^2 - 5.0^2 = -9$ and $1.25^2 - 3.25^2 = -9$. It is negative, meaning the two events (this one and the origin) are too far apart in space for light to connect them, and no clock could be present at both.

### Example 3: proper time from the interval

> Event A is at $x = 3.0$ light-seconds, $t = 5.0$ s in frame $S$. A probe travels at constant velocity from the origin event to A. How much time passes on the probe?

**Tool: the invariant interval, $(c\Delta t_0)^2 = (c\Delta t)^2 - (\Delta x)^2$.** Trigger: "time on the traveller's own clock" between two events whose coordinates are known in some other frame. The interval gives it without ever finding $v$.

$(c\Delta t_0)^2 = 5.0^2 - 3.0^2 = 16$, so $\Delta t_0 = 4.0$ s. (The probe's speed is $3/5 = 0.6c$ and $\gamma = 1.25$, and $5.0/1.25 = 4.0$ s agrees.) This is event A on the space-time diagram above.

### Example 4: simultaneity on a train

> A train of proper length $300$ m passes a platform at $0.6c$. Lightning strikes both ends of the train at the same instant according to the platform. According to the passengers, which strike came first, and by how much?

**Tool: $t' = \gamma(t - vx/c^2)$ applied to two events with the same $t$.** Trigger: "at the same instant according to…" names a frame, and the question asks about another.

On the platform the train is $300/1.25 = 240$ m long. Put the rear strike at $x = 0$ and the front at $x = 240$ m, both at $t = 0$. Then $t'_{\text{rear}} = 0$ and $t'_{\text{front}} = 1.25 \times (0 - 0.6 \times 240 / c) = -6.0 \times 10^{-7}$ s. **The front strike came first, by $0.60$ microseconds.** In general the gap is $vL_0/c^2$: it grows with the separation, which is why simultaneity is only a problem for events that are apart.

### Example 5: the muon, both ways

> Muons are created $15$ km up, moving at $0.999c$. What fraction reach the ground? Answer in the ground's frame, then in the muon's.

**Tool: time dilation in one frame, length contraction in the other, and $N = N_0 e^{-t/\tau}$ with the muon's own elapsed time.** Trigger: a decaying particle. Decay runs on the particle's own clock, so whichever frame is used, find the *proper* time of the trip.

$\gamma = 22.4$. **Ground's frame:** the trip takes $15\,000 / (0.999c) = 50.1$ microseconds; the muon ages $50.1 / 22.4 = 2.24$ microseconds. **Muon's frame:** the atmosphere is $15\,000/22.4 = 671$ m thick and passes in $671/(0.999c) = 2.24$ microseconds. Both give $e^{-2.24/2.197} = 0.36$. Without relativity the answer would be $e^{-50.1/2.197} \approx 10^{-10}$: one muon in ten billion, where a third actually arrive.

## Common Misconceptions (Teaching Notes)

### 1. "The moving clock is affected by its motion; it is a mechanical effect"

Nothing happens *to* the clock. In its own frame it ticks normally, and it is the other frame's clocks that run slow. **Fix:** ask what the passengers see. If the answer is "everything normal", the effect is in the relation between frames, not in the mechanism.

### 2. "It is an illusion caused by the time light takes to reach you"

Light-travel delay is a separate effect, and it is removed before any of these statements are made. "The moving clock runs slow" describes what an observer concludes *after* correcting for signal delays. **Fix:** the muons. They physically arrive at the detector, in numbers no illusion could supply.

### 3. "Simultaneous is simultaneous"

For events at the same place, yes. For events apart, it depends on the frame, by $vx/c^2$. **Fix:** in any problem that feels paradoxical, find the step that compares two separated clocks, and ask who says they are synchronised.

### 4. "Proper time is Earth's time" or "the time in the rest frame of whoever is at rest"

Proper time belongs to the clock that is **present at both events**. In Example 1 that is the ship's clock, although the ship is "the moving one". **Fix:** name the two events first. Then ask which single clock was at both.

### 5. "Mass increases with speed"

Older books define a "relativistic mass" $\gamma m$. Modern usage keeps **mass** as one invariant number per particle, and puts the $\gamma$ into momentum and energy, $p = \gamma m v$ and $E = \gamma m c^2$. The physics is identical; the older wording invites the wrong picture of a particle getting fatter. **Fix:** mass is what everyone agrees on; energy and momentum are what depend on the frame.

### 6. "So everything is relative"

The opposite. The theory identifies what is *not* relative: the speed of light, the interval, the laws of physics, proper time, rest mass. Einstein is said to have wished he had called it the theory of invariants.

## Exam Notes

### IB Physics (2025 guide) — A.5 Galilean and special relativity, higher level only

Eight hours of additional higher-level content. Of the school syllabuses named in these notes, it is the only one that examines the topic.

- **Required:** reference frames; Galilean relativity with $x' = x - vt$, $t' = t$ and $u' = u - v$; the two postulates; the Lorentz transformation $x' = \gamma(x - vt)$, $t' = \gamma(t - vx/c^2)$; velocity addition $u' = (u - v)/(1 - uv/c^2)$; the invariant interval $(\Delta s)^2 = (c\Delta t)^2 - (\Delta x)^2$; proper time and proper length; $\Delta t = \gamma\Delta t_0$ and $L = L_0/\gamma$; the relativity of simultaneity; space-time diagrams with the time axis labelled $ct$, world lines at constant velocity only, and $\tan\theta = v/c$; muon decay as evidence for both time dilation and length contraction.
- **Not required, by the guide's own guidance:** the *derivations* of the Lorentz transformation, of velocity addition, and of the time-dilation and length-contraction formulae. They are given above because they are what makes the formulae believable.
- **The guide states** that the scales on the primed and unprimed axes of a space-time diagram differ and are fixed by lines of constant interval, which is the green hyperbola above.
- **Not in A.5:** relativistic momentum and energy. $E = mc^2$ is used elsewhere in the course, for mass defect and binding energy.
- **Where marks go:** identifying which observer measures the proper time or proper length; sign errors in $u' = (u - v)/(1 - uv/c^2)$ when the two objects move in opposite directions (Example in the Lorentz section: $v = -0.6c$); and explaining the muon result in *both* frames.

### Where this is *not* examined

Cambridge 9702 and 0625 contain no special relativity: a text search of both syllabuses for time dilation, Lorentz, length contraction and space-time finds nothing. 9702 does use $E = mc^2$ for mass defect and binding energy, which [[Nuclear Physics]] covers. AP Physics 1, AP Physics C: Mechanics and AP Physics C: Electricity and Magnetism do not include it, and the same search finds nothing in AP Physics 2.

## Beyond the syllabus

> [!info] Energy and momentum
> Recall that the interval combines time and space into one invariant. Energy and momentum combine the same way. For a particle of mass $m$ moving at $v$,
> $$p = \gamma m v, \qquad E = \gamma m c^2, \qquad E^2 = (pc)^2 + (mc^2)^2 .$$
> At rest $p = 0$ and $E = mc^2$: mass is a form of energy, at an exchange rate of $9 \times 10^{16}$ joules per kilogram. One gram is $21$ kilotonnes of TNT. The Sun pays for its light with $4.3$ billion kilograms of mass every second, and the mass defect of a nucleus in [[Nuclear Physics]] is the same accounting.
>
> The kinetic energy is what is left after the rest energy is subtracted: $E_k = (\gamma - 1)mc^2$. Expand $\gamma$ for small $v/c$ with the [[Binomial Series]]: $\gamma \approx 1 + \tfrac12 v^2/c^2$, so $E_k \approx \tfrac12 mv^2$. Newton's formula is the first term. At $0.1c$ the two differ by $0.8\,\%$; at $0.9c$ the true value is $3.2$ times larger; and as $v \to c$ it grows without limit, which is the real reason nothing with mass reaches the speed of light.
>
> ![[special-relativity-energy.svg|820]]

> [!info] The twins
> Recall Example 1. Let the ship turn round at the star and come home at $0.8c$. Earth's clocks record $10$ years and the ship's record $6$, and when the twins stand side by side one really is four years younger. The situation is not symmetric, because the travelling twin changed inertial frames at the turn-round and the stay-at-home twin did not. On a space-time diagram the traveller's world line is bent, the other is straight, and in this geometry the straight line between two events is the *longest* in proper time. Acceleration is what marks the difference; it is not what causes the ageing.

> [!info] What comes next
> Special relativity is "special" because it is restricted to inertial frames and leaves out gravity. Einstein spent the next ten years removing the restriction. The starting observation is as simple as the light clock: inside a freely falling lift, you cannot tell that gravity exists. [[General Relativity]] takes it from there, and [[The 1919 Eclipse]] tells how it was tested.

## Connections

- **Where the problem comes from:** [[Maxwell's Equations]] — a speed with no "relative to what" attached.
- **Tools used:** [[Pythagoras Theorem]] (the light clock, and the interval as Pythagoras with a minus sign), [[Binomial Series]] (recovering $\tfrac12 mv^2$), [[Hyperbolic Functions]] (rapidity, and the Lorentz transformation as a hyperbolic rotation).
- **The mechanics it contains as a limit:** [[Newton's Laws of Motion]], [[Linear Momentum]], [[Work, Energy and Power]].
- **Where it is already at work:** [[Doppler Effect]] (light), [[Lorentz Force]] (magnetism as relativity), [[Nuclear Physics]] ($E = mc^2$ as mass defect), [[Hubble's Law and the Expanding Universe]].
- **Extension:** [[General Relativity]]. **Story:** [[The 1919 Eclipse]].

## Sources

- Einstein, A. (1905). Zur Elektrodynamik bewegter Körper. *Annalen der Physik*, 17, 891–921.
- Frisch, D. H., & Smith, J. H. (1963). Measurement of the relativistic time dilation using μ-mesons. *American Journal of Physics*, 31, 342–355. Counts: $565 \pm 10$ per hour on Mount Washington, $409 \pm 9$ at sea level.
- Hafele, J. C., & Keating, R. E. (1972). Around-the-world atomic clocks. *Science*, 177, 166–170.
- The GPS and accelerator figures are computed in `special-relativity-model.py` from the orbital radius, the Earth's mass and radius, and the proton's rest energy.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\gamma = \dfrac{1}{\sqrt{1 - v^2/c^2}}$ | `\gamma = \dfrac{1}{\sqrt{1 - v^2/c^2}}` | The Lorentz factor |
| $\Delta t = \gamma\,\Delta t_0$ | `\Delta t = \gamma\,\Delta t_0` | Time dilation; $\Delta t_0$ is the proper time |
| $L = L_0/\gamma$ | `L = L_0/\gamma` | Length contraction; $L_0$ is the proper length |
| $x' = \gamma(x - vt)$ | `x' = \gamma(x - vt)` | Lorentz transformation, position |
| $t' = \gamma\left(t - \dfrac{vx}{c^2}\right)$ | `t' = \gamma\left(t - \dfrac{vx}{c^2}\right)` | Lorentz transformation, time |
| $(\Delta s)^2 = (c\Delta t)^2 - (\Delta x)^2$ | `(\Delta s)^2 = (c\Delta t)^2 - (\Delta x)^2` | The invariant interval |
| $\tan\theta = v/c$ | `\tan\theta = v/c` | Angle of a world line from the $ct$ axis |
