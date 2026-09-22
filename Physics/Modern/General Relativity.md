---
chinese: 广义相对论 (guǎngyì xiāngduìlùn)
prerequisites:
  - "[[Special Relativity]]"
  - "[[Gravitational Fields]]"
  - "[[Stellar Evolution]]"
  - "[[Newton's Laws of Motion]]"
leads_to:
  - "[[Emmy Noether]]"
tags:
  - subject/physics
  - domain/relativity
  - domain/modern-physics
  - domain/gravitation
  - level/IB-HL
  - level/university
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - type/theory
  - type/derivation
  - type/visual-tool
  - notation/schwarzschild-radius
  - misconception/astronauts-float-because-there-is-no-gravity
  - misconception/light-bends-because-photons-have-mass
  - misconception/the-rubber-sheet-is-the-explanation
  - misconception/black-holes-suck-things-in
  - misconception/general-relativity-replaces-newton
---

# General Relativity 广义相对论

> You are in a lift and the cable snaps. For the seconds of the fall everything in the lift floats: your keys, the phone you dropped, you. Gravity has not switched off. Everything is simply falling together, and gravity is the one force that makes everything fall at exactly the same rate, so nothing in the lift can pull ahead of anything else.
>
> Einstein said the thought came to him at his desk in the Bern patent office in 1907: *a person in free fall does not feel their own weight.* He called it the happiest thought of his life. The whole of general relativity is what happens when you take that sentence seriously.

## The problem

[[Special Relativity]] left gravity out. It had to. Newton's law of gravitation, $F = GMm/r^2$, says the force on the Earth depends on where the Sun is *now*, and special relativity forbids any influence travelling faster than light. If the Sun vanished, Newton's Earth would fly off at once; Einstein's could not know for eight minutes. Something in the law of gravity had to give.

There was a second oddity, older and stranger. In $F = ma$ the mass $m$ measures how hard a body is to accelerate. In $F = GMm/r^2$ the same $m$ measures how strongly gravity pulls it. There is no reason those two numbers should be the same, yet every experiment since Galileo says they are, to better than one part in $10^{13}$. That is why a hammer and a feather fall together on the Moon, and why everything in the falling lift floats: gravity gives every body the same acceleration, whatever it is made of. No other force does that. A charged pith ball and an uncharged one in an electric field go different ways.

Einstein's answer to both was the same idea. Gravity is not a force acting across space. It is the shape of space and time near a mass, and things fall because falling is the straightest path available.

## Definition

### Formal

**General relativity** is Einstein's theory of gravitation (1915). Its foundation is the **equivalence principle**: in a small enough region, and for a short enough time, no experiment can distinguish a uniform gravitational field from an accelerating reference frame, and free fall is indistinguishable from the absence of gravity. Its content is that mass and energy curve space-time, and that free bodies and light follow **geodesics**, the straightest possible paths, in that curved geometry. In the weak fields of the solar system it reduces to Newton's law plus small corrections: clocks deeper in a potential well by $\Delta\Phi$ run slow by a fraction $\Delta\Phi/c^2$, and light passing a mass $M$ at distance $b$ is deflected by $4GM/(bc^2)$.

### Intuitive

Stand in a lift. When it starts upward you feel heavier; when it starts downward you feel lighter; if the cable snapped you would feel nothing at all. What you feel as weight was never gravity pulling down. It was the floor pushing up. Einstein's move is to trust that feeling completely: a freely falling lift is the true "no gravity" state, and what we call gravity on the ground is the floor accelerating us away from the path we would naturally follow.

Once you accept that, gravity has to do to light and to clocks whatever acceleration does to them. In an accelerating lift a light beam bends and a clock on the floor runs slow compared with one on the ceiling, so near the Earth light bends and low clocks run slow. Both have been measured. And a lift can only be *small*: two balls in a lift the size of a continent drift together as they fall, because each heads for the centre of the Earth. That drift is what "curved space-time" means. It is the part of gravity no acceleration can imitate.

### 中文锚点 (Chinese Anchor)

想象你在电梯里，缆绳突然断了。下坠的那几秒钟，电梯里的一切都飘了起来：钥匙、掉在地上的手机，还有你自己。不是重力消失了，而是所有东西在一起下落，而重力恰好是那种让一切都以完全相同的加速度下落的力。你平时感到的"重量"从来不是重力在拉你，而是地板在向上推你的脚，现在地板不推了。空间站里的宇航员飘着，也是同一个道理：他们正在绕着地球下落，空间站和他们一起下落。爱因斯坦把这件事变成了整个理论。如果自由下落跟完全没有重力毫无区别，那么重力就不是一种力，而是物体自然运动路径的形状，地球的质量把这些路径掰弯了，连光走的路、钟表走的快慢，也跟着变了。你手机上的导航靠的就是这个：GPS 卫星上的钟远离地球的引力，每天要快四十五微秒，不做修正的话，地图每天会偏出十公里。

## Notation

| Symbol | Meaning | Notes |
|---|---|---|
| $\Phi$ | gravitational potential, energy per unit mass | $\Phi = -GM/r$ outside a sphere; from [[Gravitational Fields]] |
| $\Delta\Phi / c^2$ | fractional rate difference between two clocks | the clock deeper in the well runs slow |
| $r_s = 2GM/c^2$ | the Schwarzschild radius of a mass $M$ | $2.95$ km for the Sun, $8.9$ mm for the Earth |
| $\sqrt{1 - r_s/r}$ | rate of a clock at distance $r$ from $M$, against a clock far away | the exact factor; $1 - GM/(rc^2)$ when $r \gg r_s$ |
| $b$ | impact parameter: closest approach of a light ray to a mass | measured from the centre of $M$ |
| $\theta = 4GM/(bc^2)$ | deflection of light passing a mass | Newton's particle picture gives half of this |

> [!warning] Notation trap
> The 2025 IB guide and the AP course descriptions use no general-relativity notation at all; the only line they examine is the equivalence principle in words. The symbols above are the standard ones in university texts, and $r_s$ is sometimes written $R_S$ or $r_g$.

## The equivalence principle

Take a lift far from any planet, pulled by a rocket so that it accelerates upward at $a = 9.8\ \text{m s}^{-2}$. Inside, a dropped ball "falls" to the floor at $9.8\ \text{m s}^{-2}$, you weigh what you weigh at home, and a thrown ball follows a parabola. Nothing you can do inside the lift tells you whether you are on the Earth or in the rocket. Einstein raised this from an observation to a principle: **the two situations are the same physics.**

The principle has teeth because it tells you what gravity must do to things Newton's law never mentioned. Light, for one.

![[general-relativity-elevator.svg|820]]

Send a pulse of light across the accelerating lift, entering horizontally at the left wall. Seen from outside, the pulse travels in a straight line while the lift accelerates upward, so by the time the pulse reaches the far wall the lift has risen and the pulse hits the wall lower than where it entered. Seen from inside, the pulse followed a curve. If the lift crosses its own width $w$ in time $w/c$, the lift has risen $\tfrac12 a (w/c)^2$ in that time, so the pulse arrives that much lower: a parabola, exactly the path of a thrown ball, only very flat because $c$ is so large.

Now the principle applies. A lift standing on the Earth is the same physics. So light falls in a gravitational field, at the same $g$ as everything else. Newton could have said this too, if light were made of fast particles, and in 1801 the Bavarian astronomer Johann Soldner did. Einstein's 1911 paper reached the same number by this route: a ray grazing the Sun bends by $0.87''$. It was too small by exactly half, and finding out why took him four more years.

![[general-relativity-equivalence.mp4]]

## Gravity slows clocks

The lift argument gives a second prediction, one Newton could not have made, and it is the one your phone uses every day.

Put a clock on the floor of the accelerating lift and another on the ceiling, height $h$ above it. The floor clock flashes once a second. Each flash takes time $h/c$ to reach the ceiling, and in that time the lift's speed has grown by $\Delta v = a h / c$. So the ceiling receives the flashes while moving away from where they were sent, at speed $\Delta v$ relative to the sender: by the [[Doppler Effect]] the flashes arrive spread out, at a rate lower by the fraction

$$\frac{\Delta f}{f} = \frac{\Delta v}{c} = \frac{a h}{c^2}.$$

The ceiling sees the floor clock run slow. By the equivalence principle a lift standing on the Earth must show the same thing, with $a$ replaced by $g$: **a clock lower in a gravitational field runs slow, by the fraction $gh/c^2$.** Nothing is wrong with the clock. A clock is anything that repeats, and every process on the floor, atoms vibrating, people ageing, runs slow by the same fraction compared with the ceiling.

Write $gh$ as the difference in gravitational potential, $\Delta\Phi$, and the result no longer needs the field to be uniform:

$$\frac{\Delta\tau_{\text{low}}}{\Delta\tau_{\text{high}}} = 1 - \frac{\Delta\Phi}{c^2}, \qquad \Delta\Phi = \Phi_{\text{high}} - \Phi_{\text{low}} > 0 .$$

**The measurement.** In 1959 Robert Pound and Glen Rebka sent gamma rays from the top of a $22.5$ m tower at Harvard to the bottom and back. Going down, the gamma rays gain energy, and their frequency rises by the fraction $gh/c^2 = 2.46 \times 10^{-15}$. That is a shift of one part in four hundred million million, and they could see it because the Mössbauer effect gives iron-57 a spectral line sharp enough to resolve it, provided the source is moved at a few millimetres per hour to tune the Doppler shift against gravity's. Their 1960 result agreed with the prediction to $10\,\%$; Pound and Snider repeated it in 1965 to $1\,\%$.

**The scale.** Your head is about a metre higher than your feet. Over a lifetime of eighty years it ages about $270$ nanoseconds more. On the surface of the Sun clocks run slow by two parts in a million; on a white dwarf by one part in four thousand; on the surface of a neutron star they run at $81\,\%$ of the rate of clocks far away, which a light-beam argument cannot deliver and only the full theory can (the exact factor is $\sqrt{1 - r_s/r}$, below).

## Where the equivalence principle stops: tides

The lift argument has a hidden assumption: the lift is small. Take a lift the width of a country and drop it. Two balls at its two ends fall toward the centre of the Earth, not "straight down", and their paths converge. An observer inside, floating and feeling no gravity, watches the balls drift together. Below the lift the field is stronger than above, so a ball at the floor pulls away from a ball at the ceiling. These are tidal effects, the same effects that raise the oceans twice a day, and **no acceleration of a lift can imitate them**, because an accelerating lift has one acceleration and the Earth's field has a different one at every point.

![[general-relativity-tidal.svg|820]]

So free fall removes gravity only locally, in a region small enough that the field is uniform across it. What remains when you have removed everything removable is the *relative* acceleration of nearby free bodies, and Einstein identified that with the **curvature of space-time**. The picture on the right of the figure is the honest one: two paths that start out parallel on a sphere, two lines of longitude leaving the equator, meet at the pole. Neither path bends; each is as straight as the surface allows. They meet because the surface is curved. Two freely falling bodies near the Earth are in the same situation, with time as one of the directions: they follow the straightest paths available, **geodesics**, and the paths converge because the Earth's mass has curved the space-time they move through.

This is why the theory is "general". Special relativity is the geometry of flat space-time, where the interval $(c\Delta t)^2 - (\Delta x)^2$ is the same for everyone. General relativity lets the interval vary from place to place, with mass and energy deciding how, through the **Einstein field equations**. In words: *matter and energy tell space-time how to curve; curved space-time tells matter and light how to move.* Solving them is university work. Two of their consequences are not, and they close the two loose ends above.

**The Schwarzschild solution (1916).** Outside a spherical mass $M$, a clock at distance $r$ runs, compared with a clock far away, at the rate

$$\frac{\text{d}\tau}{\text{d}t} = \sqrt{1 - \frac{2GM}{rc^2}} = \sqrt{1 - \frac{r_s}{r}}, \qquad r_s = \frac{2GM}{c^2}.$$

Expand with the [[Binomial Series]] for $r \gg r_s$: $\sqrt{1 - r_s/r} \approx 1 - GM/(rc^2) = 1 + \Phi/c^2$. The lift's answer, recovered. At $r = r_s$ the rate is zero: a clock at the **Schwarzschild radius** would appear, to a distant observer, to stop. For the Sun $r_s = 2.95$ km; for the Earth $8.9$ mm. Neither is anywhere near its own $r_s$, which is why Newton works so well for both.

**Light, taken twice.** The lift argument gave the deflection of light from the curvature of *time*: clocks run slow near the Sun, so the part of a wavefront nearer the Sun travels a little slower, and the front turns, exactly as light turns entering glass. The full theory adds an equal contribution from the curvature of *space* around the Sun, which no lift can show because a lift is flat. The total is

$$\theta = \frac{4GM}{bc^2} = 1.75'' \text{ at the Sun's edge.}$$

Twice Soldner and twice Einstein's 1911 value. This is the number Eddington's expeditions measured in 1919, and [[The 1919 Eclipse]] tells that story. Radio interferometry has since confirmed it to two parts in ten thousand.

![[general-relativity-deflection.svg|860]]

## The three classical tests, and two modern ones

| Test | Prediction | Measurement |
|---|---|---|
| Mercury's perihelion | the ellipse's long axis turns by $43''$ a century more than the planets' pulls explain | Le Verrier's unexplained residual since 1859; Einstein computed it in November 1915 and wrote that for days he was beside himself with joy |
| Deflection of starlight by the Sun | $1.75''$ at the limb | $1.98 \pm 0.12''$ and $1.61 \pm 0.30''$ in 1919; $1.7499 \pm 0.0003''$ by radio (2004) |
| Gravitational redshift | $gh/c^2 = 2.46 \times 10^{-15}$ over $22.5$ m | Pound–Rebka 1960 to $10\,\%$, Pound–Snider 1965 to $1\,\%$ |
| Gravitational waves | ripples of curvature travelling at $c$, radiated by accelerating masses | LIGO, 14 September 2015: two black holes of $36$ and $29$ solar masses merging; the $4$ km arms changed length by $10^{-18}$ m |
| The shadow of a black hole | a dark disc about $2.6\,r_s$ across against the glowing gas | the Event Horizon Telescope image of M87*, 2019 |

The perihelion advance per orbit is $\Delta\varphi = 6\pi GM/\big(a(1 - e^2)c^2\big)$, with $a$ the semi-major axis and $e$ the eccentricity; Mercury's $0.10''$ per orbit adds up to $43.0''$ a century over its $415$ orbits. The formula is a result of the full theory and this card does not derive it; `general-relativity-model.py` evaluates it.

**Black holes.** The Schwarzschild factor reaches zero at $r = r_s$. A star whose collapsed remnant is heavier than a neutron star can support, about three solar masses in [[Stellar Evolution]], has nothing left to hold it up, and its surface falls inside its own $r_s$. From outside, that sphere is an **event horizon**: light from inside cannot get out, and clocks approaching it appear to run ever slower. A ten-solar-mass black hole has $r_s = 30$ km; the one at the centre of our galaxy, $4.3$ million solar masses, has $r_s = 13$ million km, a fifth of the distance from the Sun to Mercury. Far from the horizon its gravity is entirely ordinary. If the Sun were replaced by a black hole of the same mass, the planets would keep their orbits and notice only the dark.

**Gravitational waves.** Shake a mass and the curvature around it changes; the change cannot spread faster than light, so it travels outward as a wave in the geometry itself, stretching space in one direction while squeezing it in the other. Two black holes spiralling together are the loudest source there is. When their wave crossed the Earth in 2015 it changed the length of LIGO's $4$ km arms by a thousandth of the width of a proton, and the instrument, an interferometer with $1\,100$ km of folded light path comparing the two arms by the interference that [[Superposition and Interference]] explains, heard it.

## Where this is the working tool

**Satellite navigation.** A GPS receiver finds its position from the arrival times of signals from satellite clocks, and a clock error of one nanosecond is $30$ cm of position error. A GPS satellite orbits at $26\,562$ km from the Earth's centre, where the potential is higher than at the surface: by the clock formula its clock runs fast by $\Delta\Phi/c^2 = 5.3 \times 10^{-10}$, which is $45.7$ microseconds a day. Its orbital speed of $3.87\ \text{km s}^{-1}$ slows the clock, by [[Special Relativity]], by $7.2$ microseconds a day. The net is $+38.5$ microseconds a day, and left uncorrected it would put your position $11.5$ km wrong by tomorrow. The satellite clocks are therefore set to tick slow before launch, at $10.229\,999\,995\,43$ MHz instead of $10.23$ MHz, so that they run at the ground rate once in orbit. The two effects cancel exactly for a circular orbit at $1.5$ Earth radii, $3\,190$ km up; the ISS is below that line, so its clocks run slow overall and astronauts return a few milliseconds younger, while GPS is well above it.

![[general-relativity-clock-rate.svg|860]]

**Atomic clocks on aeroplanes.** Hafele and Keating's 1971 flights, which [[Special Relativity]] describes, had to include gravity to match. Their published predictions split each flight into two parts: the aircraft's altitude, about $9$ km, made the clocks *gain* $144 \pm 14$ ns eastward and $179 \pm 18$ ns westward, while their speed, added to or subtracted from the Earth's rotation, made them lose $184 \pm 18$ ns eastward and gain $96 \pm 10$ ns westward. The sums, $-40$ and $+275$ ns, are what the clocks showed.

**Measuring height with a clock.** Since the rate of a clock depends on its height, a good enough clock is an altimeter. In 2010 a NIST team compared two aluminium-ion optical clocks and saw the rate change when one was raised by $33$ cm. Today's best clocks resolve a centimetre, and geodesists are beginning to use them to compare the heights of points on different continents, where a spirit level cannot reach.

**Seeing with gravity.** Every mass bends light, so galaxies act as lenses: a distant galaxy behind a nearer cluster appears as arcs, multiple images, or an Einstein ring, and the shapes of the arcs measure the lens's mass, including the dark matter that emits nothing. Microlensing, the brief brightening of a background star when a planet-sized mass crosses in front of it, has found planets no telescope could see directly.

**Hands-on.** `general-relativity-model.py`, in the same folder, computes every number quoted here from $G$, $c$ and the masses, and also integrates a speed-$c$ particle past the Sun under Newton's law to check the impulse argument in Example 4. Change the GPS orbit to the ISS's $420$ km altitude and predict the sign of the net drift before running it.

## Worked examples

### Example 1: the Pound–Rebka shift

*Gamma rays fall $22.5$ m in the Earth's field. By what fraction does their frequency change?*

**Trigger:** two clocks (here, the emitter and the absorber) at different heights in a uniform field. **Tool: the lift formula, $\Delta f/f = gh/c^2$.**

$$\frac{\Delta f}{f} = \frac{9.81 \times 22.5}{(3.00 \times 10^8)^2} = 2.46 \times 10^{-15}.$$

Falling light gains energy, so the frequency at the bottom is *higher*. The absorber at the bottom has to be moved away from the source at the speed $v = c\,\Delta f/f = 0.74\ \mu\text{m s}^{-1}$, a few millimetres an hour, to Doppler-shift the line back into resonance. That speed is what Pound and Rebka measured.

### Example 2: a GPS clock

*How much does a GPS satellite's clock gain per day from gravity alone?*

**Trigger:** two clocks at different distances from a spherical mass, not in a uniform field. **Tool: the potential form, $\Delta\tau/\tau = \Delta\Phi/c^2$ with $\Phi = -GM/r$** from [[Gravitational Fields]].

$$\frac{\Delta\Phi}{c^2} = \frac{GM_E}{c^2}\left(\frac{1}{R_E} - \frac{1}{r}\right) = \frac{3.986 \times 10^{14}}{9.0 \times 10^{16}}\left(\frac{1}{6.371 \times 10^6} - \frac{1}{2.656 \times 10^7}\right) = 5.29 \times 10^{-10}.$$

Over a day of $86\,400$ s that is $45.7\ \mu$s gained. [[Special Relativity]] takes back $7.2\ \mu$s for the orbital speed, leaving $+38.5\ \mu$s a day, or $11.5$ km of ranging error a day at the speed of light.

### Example 3: where the two effects cancel

*At what orbital radius does a satellite's clock keep time with a clock on the ground?*

**Trigger:** "keeps time" means the gravitational gain equals the kinematic loss. **Tools: the potential form for the gain; the first-order time dilation $\tfrac12 v^2/c^2$ for the loss; $v^2 = GM/r$ for a circular orbit** from [[Circular Motion]].

Gain per unit time: $\dfrac{GM}{c^2}\left(\dfrac{1}{R} - \dfrac{1}{r}\right)$. Loss: $\dfrac{v^2}{2c^2} = \dfrac{GM}{2rc^2}$. Setting them equal,

$$\frac{1}{R} - \frac{1}{r} = \frac{1}{2r} \quad\Longrightarrow\quad \frac{1}{R} = \frac{3}{2r} \quad\Longrightarrow\quad r = \tfrac32 R = 9\,560 \text{ km},$$

an altitude of $3\,190$ km, independent of $G$, $M$ and $c$. Below it, speed wins and orbiting clocks run slow; above it, altitude wins and they run fast. The ISS at $420$ km loses $24.5\ \mu$s a day; GPS at $20\,180$ km gains $38.5$.

### Example 4: Newton's deflection of light, by impulse

*Treat light as a particle of speed $c$ and mass $m$ passing the Sun at closest approach $b$. Estimate the deflection.*

**Trigger:** a fast particle barely deflected: the path is nearly straight, so integrate the sideways force along the undeflected line. **Tool: impulse $= \int F_\perp\,\text{d}t$ changes the sideways momentum;** the [[Linear Momentum]] view of a force that acts briefly.

Along the straight line the particle is at distance $\sqrt{b^2 + x^2}$ from the Sun and the sideways component of the force is $F_\perp = \dfrac{GMm}{b^2 + x^2}\cdot\dfrac{b}{\sqrt{b^2 + x^2}}$. With $x = ct$,

$$\Delta p_\perp = \int_{-\infty}^{\infty} \frac{GMmb}{(b^2 + c^2t^2)^{3/2}}\,\text{d}t = \frac{GMmb}{c}\cdot\frac{2}{b^2} = \frac{2GMm}{bc}.$$

(Substitute $ct = b\tan\phi$; the integral becomes $\int\cos\phi\,\text{d}\phi$ from $-\pi/2$ to $\pi/2$, which is $2$.) The deflection angle is the sideways momentum over the forward momentum $mc$:

$$\theta_{\text{Newton}} = \frac{\Delta p_\perp}{mc} = \frac{2GM}{bc^2} = \frac{2 \times 6.674 \times 10^{-11} \times 1.989 \times 10^{30}}{6.957 \times 10^8 \times (2.998 \times 10^8)^2} = 4.25 \times 10^{-6} \text{ rad} = 0.88''.$$

The mass $m$ cancelled, as it must for anything falling. The rough estimate in the figure, force at closest approach times the time $2b/c$ spent within about $b$ of the Sun, gives the same answer, and the numerical integration in the model script confirms $0.876''$ to three figures. General relativity doubles it to $1.75''$: the impulse argument counts the curvature of time and misses the equal curvature of space.

### Example 5: a clock on a neutron star

*A neutron star has $1.4$ solar masses and a radius of $12$ km. How fast does a clock on its surface run, seen from far away, and how close is the star to being a black hole?*

**Trigger:** a strong field, where the weak-field fraction $GM/(rc^2)$ is no longer small. **Tool: the exact Schwarzschild factor $\sqrt{1 - r_s/r}$, with $r_s = 2GM/c^2$.**

$$r_s = \frac{2 \times 6.674 \times 10^{-11} \times 1.4 \times 1.989 \times 10^{30}}{(2.998 \times 10^8)^2} = 4.13 \text{ km}, \qquad \sqrt{1 - \frac{4.13}{12}} = 0.81.$$

A second on the surface is $1.24$ s to us, a $19\,\%$ effect, and the weak-field formula $1 - GM/(rc^2) = 0.83$ is already visibly wrong. The star's radius is $2.9\,r_s$: squeeze it to a third of its size and it would be a black hole. Light leaving its surface is redshifted by the same factor, and redshifts of this size have been reported in the spectra of gas on neutron-star surfaces.

## Common Misconceptions (Teaching Notes)

### 1. "Astronauts float because there is no gravity in space"

At the ISS's altitude of $420$ km, $g$ is $8.7\ \text{m s}^{-2}$, nine tenths of its value on the ground. The astronauts float because they are falling, continuously, around the Earth, with the station falling around it with them. This is the falling lift of the opening paragraph, and it is the single best everyday illustration of the equivalence principle.

**Fix:** ask what would happen to a stationary space station. It would fall straight down, at $8.7\ \text{m s}^{-2}$.

### 2. "Light bends because photons have a little mass"

Photons have no mass, and the argument does not need them to: Example 4 cancels $m$ before the end. Light bends because the equivalence principle says everything that moves through a gravitational field falls, whether or not it has mass, and the full theory adds that space itself is curved near the Sun. The observed $1.75''$ is twice what any "photons are light particles with mass" story predicts. That factor of two is the evidence that it is the geometry, not the photon, that does it.

### 3. "The rubber sheet is the explanation"

The picture of a heavy ball denting a stretched sheet, with marbles rolling toward it, is a picture of a *result*, and it cheats: the marbles roll into the dent because the room's gravity pulls them down, so it uses gravity to explain gravity. It also shows only the curvature of space, when for everything slower than light it is the curvature of *time*, the fact that clocks run slow near a mass, that does almost all the work. A ball thrown across a room follows a parabola because its lower side is in slightly slower time.

**Fix:** use the falling lift and the two converging balls. They are what the theory actually says.

### 4. "Black holes suck things in"

Outside the horizon a black hole's gravity is the gravity of its mass, no more. Replace the Sun by a black hole of one solar mass and the Earth's orbit is unchanged. The horizon is special only in that nothing inside can get out, and its radius, $3$ km for a solar mass, is tiny. Things fall into black holes the way they fall into anything: only if they were heading there.

### 5. "General relativity replaced Newton"

Newton's law is general relativity's weak-field, slow-motion limit, to a fraction $GM/(rc^2)$: one part in $10^9$ at the Earth's surface, two parts in $10^6$ at the Sun's. Spacecraft are navigated with Newton plus corrections. What general relativity replaced was the *picture*, a force acting instantly across empty space, not the numbers, which it reproduces and then extends: to light, to clocks, to strong fields and to the universe as a whole.

### 6. "The clock effect is an illusion of signal delay"

The Pound–Rebka shift is not a delay; it is a permanent difference in rate, and the Hafele–Keating clocks came home carrying it in their readings. The same mistake is answered for motion in [[Special Relativity]]; here the case is stronger, because the two clocks never move relative to each other at all.

## Exam Notes

### AP Physics 1 and AP Physics C: Mechanics

Both course descriptions examine one statement, in Unit 2 under apparent weight. Essential knowledge **2.6.C.4**: "The equivalence principle states that an observer in a noninertial reference frame is unable to distinguish between an object's apparent weight and the gravitational force exerted on the object by a gravitational field." That is the lift on the ground and the lift under the rocket, and the questions that use it are the standard apparent-weight questions (2.6.C.1–C.3): a scale in an accelerating lift, and weightlessness as "the only force is gravity", which is the ISS misconception above. Nothing on light bending, clocks or curvature is examined.

### IB Physics (2025 guide)

Not examined. A.5 covers Galilean and special relativity only, and [[Special Relativity]] carries those rows.

### Where this is *not* examined

Cambridge 9702 and 0625 do not examine general relativity at any level; 9702 Topic 13 stops at Newtonian gravitational potential, which [[Gravitational Fields]] carries. Everything in this card beyond the equivalence-principle statement is enrichment, written because the GPS correction, the light-clock derivation and the 1919 eclipse are where the physics a student already knows turns into the physics of the universe.

## Beyond the syllabus

> [!info] The field equations, in one line
> Recall that special relativity's interval, $(c\Delta t)^2 - (\Delta x)^2 - (\Delta y)^2 - (\Delta z)^2$, is the same for all inertial observers. General relativity lets the coefficients in that expression depend on position, and collects them in the **metric** $g_{\mu\nu}$, ten functions of place and time. Einstein's equations, $G_{\mu\nu} = \dfrac{8\pi G}{c^4}\,T_{\mu\nu}$, set a measure of the metric's curvature on the left equal to the density and flow of energy and momentum on the right. The constant is tiny, $2 \times 10^{-43}$ in SI units, which is why it takes a star to curve space-time noticeably. The Schwarzschild factor above is the solution for one spherical mass in empty space; the expanding universe of [[Hubble's Law and the Expanding Universe]] is the solution for matter spread uniformly everywhere, and Einstein's 1917 attempt to make that solution stand still introduced the cosmological constant that now names dark energy.

> [!info] Frame dragging
> A spinning mass drags space-time round with it, slightly. Gravity Probe B, a satellite carrying four of the roundest gyroscopes ever made, measured the drag of the spinning Earth in 2011: the gyroscope axes turned by $37 \pm 7$ milliarcseconds a year, against a predicted $39$. The same effect, enormously larger, sets the spin of the gas discs around black holes.

## Connections

- **Built on:** [[Special Relativity]] (flat space-time, and the kinematic half of the GPS correction), [[Gravitational Fields]] (the potential $-GM/r$, which becomes the clock-rate formula), [[Doppler Effect]] (the ceiling clock receding from the floor's flashes), [[Newton's Laws of Motion]] and [[Linear Momentum]] (the impulse deflection).
- **Tools used:** [[Binomial Series]] (the Schwarzschild factor's weak-field limit), [[Circular Motion]] ($v^2 = GM/r$ in Example 3).
- **Where it points next:** [[Stellar Evolution]] (the remnants that become black holes), [[Hubble's Law and the Expanding Universe]] (the cosmological solution), [[Superposition and Interference]] (how LIGO listens).
- **Story:** [[The 1919 Eclipse]].

## Sources

- Einstein, A. (1907). Über das Relativitätsprinzip und die aus demselben gezogenen Folgerungen. *Jahrbuch der Radioaktivität und Elektronik*, 4, 411–462. The equivalence principle, gravitational time dilation and light bending first appear here; the "happiest thought" is Einstein's own description in a 1920 manuscript for *Nature*.
- Einstein, A. (1911). Über den Einfluß der Schwerkraft auf die Ausbreitung des Lichtes. *Annalen der Physik*, 35, 898–908. The half-value $0.83''$ (with the constants of the day).
- Einstein, A. (1916). Die Grundlage der allgemeinen Relativitätstheorie. *Annalen der Physik*, 49, 769–822. The full theory; $1.75''$; Mercury's $43''$.
- Pound, R. V., & Rebka, G. A. (1960). Apparent weight of photons. *Physical Review Letters*, 4, 337–341. Measured $(2.57 \pm 0.26) \times 10^{-15}$ against $2.46 \times 10^{-15}$. Pound, R. V., & Snider, J. L. (1965). *Physical Review Letters*, 13, 539–540: ratio $0.9990 \pm 0.0076$.
- Dyson, F. W., Eddington, A. S., & Davidson, C. (1920). *Philosophical Transactions A*, 220, 291–333. Sobral $1.98 \pm 0.12''$, Príncipe $1.61 \pm 0.30''$.
- Shapiro, S. S., Davis, J. L., Lebach, D. E., & Gregory, J. S. (2004). *Physical Review Letters*, 92, 121101. Radio deflection: $\gamma = 0.9998 \pm 0.0004$.
- Hafele, J. C., & Keating, R. E. (1972). Around-the-world atomic clocks: predicted relativistic time gains; observed relativistic time gains. *Science*, 177, 166–170. The gravitational and kinematic components quoted above are their Table 1.
- Ashby, N. (2003). Relativity in the Global Positioning System. *Living Reviews in Relativity*, 6, 1. The $10.229\,999\,995\,43$ MHz clock offset.
- Chou, C. W., Hume, D. B., Rosenband, T., & Wineland, D. J. (2010). Optical clocks and relativity. *Science*, 329, 1630–1633. The $33$ cm lift.
- Abbott, B. P., et al. (2016). Observation of gravitational waves from a binary black hole merger. *Physical Review Letters*, 116, 061102.
- Event Horizon Telescope Collaboration (2019). First M87 Event Horizon Telescope results. *Astrophysical Journal Letters*, 875, L1.
- Everitt, C. W. F., et al. (2011). Gravity Probe B: final results. *Physical Review Letters*, 106, 221101.
- All numbers quoted are computed in `general-relativity-model.py`.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{\Delta f}{f} = \dfrac{gh}{c^2}$ | `\dfrac{\Delta f}{f} = \dfrac{gh}{c^2}` | Gravitational frequency shift, uniform field |
| $\dfrac{\Delta\tau}{\tau} = \dfrac{\Delta\Phi}{c^2}$ | `\dfrac{\Delta\tau}{\tau} = \dfrac{\Delta\Phi}{c^2}` | Clock-rate difference, weak field |
| $r_s = \dfrac{2GM}{c^2}$ | `r_s = \dfrac{2GM}{c^2}` | Schwarzschild radius |
| $\sqrt{1 - r_s/r}$ | `\sqrt{1 - r_s/r}` | Exact clock factor at distance $r$ |
| $\theta = \dfrac{4GM}{bc^2}$ | `\theta = \dfrac{4GM}{bc^2}` | Deflection of light; Newton's picture gives $2GM/(bc^2)$ |
| $\Delta\varphi = \dfrac{6\pi GM}{a(1 - e^2)c^2}$ | `\Delta\varphi = \dfrac{6\pi GM}{a(1 - e^2)c^2}` | Perihelion advance per orbit |
| $G_{\mu\nu} = \dfrac{8\pi G}{c^4}T_{\mu\nu}$ | `G_{\mu\nu} = \dfrac{8\pi G}{c^4}T_{\mu\nu}` | Einstein's field equations |
