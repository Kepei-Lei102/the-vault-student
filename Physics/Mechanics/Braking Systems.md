---
chinese: 制动系统 (zhìdòng xìtǒng)
prerequisites:
  - "[[The Friction Limit]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Forces and Equilibrium]]"
  - "[[Work, Energy and Power]]"
  - "[[SUVAT]]"
  - "[[Friction (Vocab)]]"
  - "[[Circular Motion]]"
leads_to:
  - "[[Stories/From the Grid to the Garage]]"
  - "[[From the Grid to the Garage]]"
tags:
  - subject/physics
  - domain/mechanics
  - domain/engineering
  - domain/control-systems
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/9702-3-2
  - syllabus/IB-Physics-A-2-2
  - syllabus/AP-Physics-1-2-7
  - syllabus/AP-Physics-C-Mech-2-7
  - type/deep
  - type/engineering
  - type/glamour
  - notation/slip-ratio
  - notation/brake-bias
  - misconception/abs-stops-faster-always
  - misconception/brake-equals-friction
  - misconception/brake-pedal-controls-force
  - misconception/regen-replaces-friction-brakes
---

# Braking Systems 制动系统

## Why this card exists

[[The Friction Limit]] taught the *physics* of grip — $F \leq \mu_s N$, the friction circle, the cliff edge between static and kinetic. **This card is the engineering story of how to live around that limit when your job is to make a two-tonne vehicle stop.** A brake isn't a force; a brake is a whole system designed to convert kinetic energy to heat in a hurry without (a) crossing the friction limit at the tire, (b) melting itself, or (c) losing the ability to also steer while it's working.

The card's question, in one sentence: *given the friction-limit theory, what does it actually take to engineer a vehicle that stops?*

The hunter's trace: **every brake-system design choice is an answer to one of three constraints — friction-limit at the tire, heat-dissipation at the rotor, or driver-input fidelity at the pedal.** Once you've internalised that triad, every brake feature — calipers, vented rotors, ABS, brake bias, regen, downshift braking, the whole catalogue — falls into a slot.

The card you are reading is, in a sense, *the* glamour card of the friction series — the place where rubber meets road meets engineering meets the open question of whether you can also steer while you're doing it. F1, motorcycles, EVs, ABS, the Stoppie limit, all of it.

### 中文锚点

**制动系统 (zhìdòng xìtǒng)** = 把动能转换成热能、并把这个过程**控制在轮胎与地面之间的摩擦极限以内**的整套机械与电子装置。

| English | 中文 | 备注 |
|---|---|---|
| Brake caliper | 制动卡钳 (zhìdòng kǎqián) | The clamp that squeezes the pads onto the rotor |
| Brake pad | 刹车片 (shāchē piàn) | The friction material that wears down |
| Brake rotor / disc | 刹车盘 (shāchē pán) | The spinning disc bolted to the wheel |
| Brake fluid | 刹车油 (shāchē yóu) | Hydraulic fluid that transmits pedal force |
| Hydraulic line | 液压管路 (yèyā guǎnlù) | The high-pressure tubing |
| Brake fade | 制动衰退 (zhìdòng shuāituì) | Loss of braking effectiveness from overheating |
| ABS (Anti-lock Braking System) | 防抱死制动系统 (fáng bàosǐ zhìdòng xìtǒng) | Modulates pressure to prevent wheel lockup |
| Traction control | 牵引力控制 (qiānyǐn lì kòngzhì) | ABS's mirror twin during acceleration |
| ESC (Electronic Stability Control) | 电子稳定控制 (diànzǐ wěndìng kòngzhì) | Per-wheel braking to correct yaw |
| Regenerative braking | 再生制动 (zàishēng zhìdòng) | Motor-as-generator brakes by extracting kinetic energy as electricity |
| Engine braking | 发动机制动 (fādòngjī zhìdòng) | Using compression/friction in the engine itself to slow the car |
| Brake bias | 制动力分配 (zhìdòng lì fēnpèi) | Front-vs-rear braking force ratio |
| Slip ratio | 滑移率 (huáyí lǜ) | Difference between wheel surface speed and road speed |
| Stoppie | 前轮抬起急刹 (qián lún tái qǐ jí shā) | Motorcycle pivoting forward over front wheel under hard braking |

中文物理教材通常把制动只讲到 $F = \mu N$ 这一层。**真实工程**远比公式复杂——从踏板到轮胎之间隔着液压、几何、热力学、控制理论、电磁感应五层独立系统，每一层都有自己的极限。这张卡讲的是这五层如何**协同**工作，并且如何在驾驶员意图与摩擦极限之间架起一座可控的桥。

---

## The mechanism — what physically happens when you press the pedal

A modern disc-brake system has five stages between your foot and the road:

1. **Pedal force.** You press the brake pedal with maybe $200-400~\text{N}$ of foot force. A mechanical lever (the pedal itself, plus a vacuum-assisted servo called the *brake booster*) multiplies this by a factor of 4–10×, giving the master cylinder $\sim 2000~\text{N}$ of input.
2. **Hydraulic amplification.** The master cylinder pushes brake fluid through narrow hydraulic lines to the caliper at each wheel. Brake fluid is **nearly incompressible** — that's the whole point, because it lets the system transmit force without losing fidelity. By Pascal's principle, the small piston in the master cylinder $\times$ its short stroke equals the large pistons in the calipers $\times$ their tiny stroke, but with the force ratio of the piston areas. A typical brake caliper piston is many times the area of the master cylinder piston, giving another 4–6× force multiplication.
3. **Pad-on-rotor friction.** The caliper squeezes a pair of friction pads against both faces of a steel (or, in performance cars, carbon-ceramic) rotor disc. The pad-rotor friction coefficient $\mu_{\text{pad}}$ is typically $0.35-0.45$ at operating temperature for street pads, higher for race compounds. Crucially, the friction force here is *not* at the tire-road interface — it's much higher in magnitude than tire-road friction, because the rotor radius is smaller than the wheel radius, so the torque has to be bigger to produce the same wheel-deceleration torque.
4. **Wheel-deceleration torque.** The friction at the pad-rotor contact produces a *torque* opposing wheel rotation: $\tau_{\text{brake}} = F_{\text{pad}} \times r_{\text{rotor effective}}$, where $r_{\text{rotor effective}}$ is the mean radius at which the pads contact the rotor. This torque decelerates the wheel's spin.
5. **Tire-road friction (the gatekeeper).** The decelerating wheel demands tire-road friction to slow the *vehicle* (not just the wheel). And here is where every brake-system story circles back: **the tire-road friction is bounded above by $\mu_s N$** — exactly the limit [[The Friction Limit]] is about. If the pad-rotor torque demands more tire-road friction than $\mu_s N$ can provide, the wheel locks. The wheel is now rotating *slower than the road is passing under it* (in fact, not rotating at all), and you have transitioned from static to kinetic friction. *That is the catastrophe ABS is designed to prevent.*

![[braking-caliper-rotor-cross-section.svg|640]]

Notice the chain: **pedal $\to$ hydraulics $\to$ pad-rotor friction $\to$ wheel torque $\to$ tire-road friction.** Four amplifications and one gatekeeper. The first four are designed to be over-powered relative to the fifth — modern brakes can apply *much more* torque than the tire-road interface can use. The driver's input is, effectively, a *request* for deceleration; the tire-road interface enforces the *limit*.

> [!info] The pedal feels like it controls force — it actually controls hydraulic pressure
> Students sometimes assume the brake pedal is connected to the brake by a force-multiplying lever and that's it. The booster + master cylinder + hydraulics is closer to a *pressure regulator*: pedal travel and pressure are roughly proportional (modulated by the booster), and that pressure becomes a pad clamping force. The clamping force then becomes a friction force, which then becomes a torque, which then *demands* tire-road grip.
>
> So when a driver says "I pressed harder," they're really saying "I commanded more hydraulic pressure." Whether that pressure becomes more *deceleration* depends entirely on whether the tire-road friction can absorb the extra demand. Past the friction limit, pressing harder does **nothing useful** — the wheel just locks, friction collapses to kinetic, and you stop more slowly than you would have with less pressure.

### Caliper architectures — single-piston floating vs multi-piston fixed

Stage 3 of the chain above ("pad-on-rotor friction") hides a real engineering choice. There are two families of caliper geometry, and the differences explain a lot of what you see in performance brakes.

**Single-piston floating caliper** — what's on ~95% of road cars. One hydraulic piston, on the *inboard* side only. When fluid pressure rises, the piston pushes the inboard pad toward the rotor. The reaction force on the caliper body slides the entire caliper *outboard* on lubricated steel guide pins, and that motion pulls the outboard pad against the rotor's other face. End state: **both pads clamped with equal force** (Newton's third law transmitted through the slide pins) within roughly 10–20 ms of brake application. Generic-explainer 3D animations exaggerate the inboard-then-outboard sequence for visibility, but at real-world timescales the two contacts are essentially simultaneous. Cheap to manufacture, low part count, easy to service. Right choice for almost any normal car.

**Fixed multi-piston caliper** — 2-piston, 4-piston, 6-piston, sometimes 8 or more. No floating, no slide pins. The caliper is rigidly bolted to the upright, and pistons sit on *both* sides of the rotor, pushing each pad directly. Common modern configurations: 4-piston fronts on M-cars and Audi RS, 6-piston Brembos on high-end sports cars, 8-piston on track-prepared cars, 10+ on hypercars and motorsport.

**What extra pistons actually buy you:**

1. **Even pressure across a longer pad.** A single big piston pushing on the centre of a long pad applies most force at that point — pad's leading and trailing edges get less pressure, the rotor sees a central hot-spot, and the pad wears unevenly. Splitting the same total force across multiple smaller pistons distributes pressure uniformly along the pad's length. Longer pads = more contact area = more friction capacity AND more heat sink without local hot-spotting.
2. **Stiffer caliper → linear pedal feel.** Floating calipers have to slide on pins under load; any slop or deflection bleeds pedal pressure into mechanical compliance instead of clamping force. Fixed multi-piston calipers are rigid bridges across the rotor — pedal-pressure to clamping-force is much more linear, which lets the driver modulate finely right at the friction limit (which, per [[The Friction Limit]], is exactly where they want to live).
3. **More total piston-bore area = more clamping force per unit fluid pressure.** Six small pistons can have more total area than one giant single piston the caliper geometry could fit. Same brake-line pressure, more clamping torque.
4. **Thermal mass spread across multiple pistons + rigid caliper body.** More material in contact with the pad backplates means more heat sunk *away* from the pads — and crucially away from the brake fluid sitting behind the pistons, which is the boil-fade weak link.
5. **Stepped (variable-bore) pistons — the racing detail.** Top-shelf 6-piston racing calipers (Brembo, AP Racing, Endless in F1 and endurance) use *different-sized* pistons at the leading vs trailing edge of the pad. Trailing-edge pistons are larger, applying more clamping force on the trailing side. This compensates for the friction drag trying to pull the pad in the direction of rotor rotation, which would otherwise cause **taper wear** (pad ends up thicker on the leading edge than the trailing edge after one stint). This IS asymmetric pressure across the pad — but spatially, not temporally. All pistons engaged simultaneously throughout the stop; the asymmetry is in their relative sizes.

**What multi-piston does NOT do: stage engagement in time.** Even with six pistons per side, all six push the pad against the rotor essentially simultaneously when the driver presses the pedal. Full clamping force is available the moment fluid pressure builds; finer modulation comes from *how hard* the driver presses (and from the linear-pedal-feel benefit above), not from sequenced piston engagement. The closest analogue to "staged" in real brake systems is the **proportioning valve** in the hydraulic plumbing — a passive valve that limits *rear* brake-line pressure proportionally to demand, to prevent rear-axle lockup before the front. That's about brake *bias* across axles, not staged engagement at one wheel.

### What changes at $v = 0$ — the end-of-stop bobble

The "feels different at full stop" sensation has three real causes, all converging in the last ~0.5 second of every stop. None of them are the brake itself engaging differently — the caliper has been clamping with the same force throughout.

1. **Pad-rotor friction transitions from kinetic to static.** While the rotor is spinning under the pad, the contact operates at $\mu_k$ (kinetic). At $v = 0$, the contact snaps to $\mu_s$ (static) — same cliff-edge transition documented in [[The Friction Limit]]. The torque now holding the wheel stationary is suddenly larger than the torque that was decelerating it a millisecond earlier; there's a tiny settling lurch as the wheel transitions from "being slowed" to "being held."
2. **Suspension nose-dive reverses.** During deceleration, weight transfers forward and the front suspension compresses. When deceleration drops to zero, the front springs push back and the front of the car rocks slightly toward level. You feel this as the end-of-stop bobble — it's mechanical-spring physics, not braking.
3. **In an automatic transmission, the torque converter unlocks.** At low road speed the torque converter still has some slip; near zero it transitions to fully unlocked. Manuals get the equivalent effect from the driver pressing the clutch. Either way, the small forward-creep force from drivetrain coupling disappears, and the car settles into its "fully stopped" state.

> [!tip] Watch the mechanism — 3D animation
> Two embeds of the same standard floating-caliper explainer (piston → inboard pad → caliper slides on pins → outboard pad — both pads then clamped together for the entire braking event). Pick the platform you have access to.
>
> - **Bilibili (in China)**: [bilibili.com/video/BV1rs4y1D7M6](https://www.bilibili.com/video/BV1rs4y1D7M6/)
> - **YouTube**: [youtu.be/hD2z1P5qMUY](https://youtu.be/hD2z1P5qMUY) — *"How do disc brakes work in cars and light vehicles. (3D animation)"* by No User Serviceable Parts, 2019.
>
> Watch the floating-caliper geometry in the video, then come back here for the multi-piston upgrade story above. Both videos exaggerate the inboard-then-outboard sequence for visibility; the real temporal gap is milliseconds, and both pads stay engaged for the entire stop.

---

## Heat — the central constraint

When a $1500~\text{kg}$ car decelerates from $30~\text{m s}^{-1}$ to rest, it sheds

$$\Delta KE = \tfrac{1}{2}(1500)(30)^2 = 675{,}000~\text{J} = 675~\text{kJ}$$

of kinetic energy. With four brake rotors each weighing $\sim 8~\text{kg}$ and specific heat capacity $c \approx 450~\text{J kg}^{-1}\text{K}^{-1}$ for steel, a single hard stop dumps roughly

$$\Delta T = \frac{675{,}000}{4 \times 8 \times 450} \approx 47~\text{K}$$

into the rotors all at once. *Repeat that ten times in succession down a mountain pass and the rotors are at 500 °C.* Repeat it once per lap for 50 laps and you're in F1 territory.

### Brake fade

**Brake fade** is the loss of braking effectiveness when the system gets too hot. It has two distinct mechanisms:

1. **Mechanical fade ("green fade")** — at temperatures above ~200–300 °C, the binder resins in the brake pad begin to outgas. These gases form a thin film between pad and rotor that *reduces* the effective $\mu_{\text{pad}}$. The brake pedal feels normal, but the pad simply isn't gripping the rotor as hard. The pad has to be "bedded in" (heated and cooled a few times in a controlled break-in cycle) to drive off most of the outgassing before the pad's $\mu$ stabilises.
2. **Fluid fade ("boil fade")** — at brake fluid temperatures above its boiling point (typically 230–280 °C for DOT 4 / DOT 5.1 fluid when fresh, lower when old and water-contaminated), the fluid vaporises in the calipers. Vapour is *compressible*. The pedal now spongs to the floor with very little pressure transmitted to the pads. This is the more dangerous failure mode because pedal feel goes away suddenly.

Both fades recover once the system cools — but "cool" might mean several minutes of light pedal use, by which time you may have already gone off the road. The Pikes Peak hill climb and Alpine downhill driving are the canonical brake-fade torture tests.

> [!warning] The Eurodrive moment — why mountain passes have runaway lanes
> Long descents in the Alps, Rockies, or Sierra Nevada often have **runaway truck ramps** — gravel-filled uphill escape lanes carved into the mountainside. They exist because trucks brake-fading on a long descent run out of stopping power *catastrophically* and need a way to come to rest without hitting traffic at the bottom.
>
> The correct technique on a long descent is to **shift to a low gear and use engine braking** to hold speed, reserving the friction brakes for actual emergencies. *Engine braking generates no heat in the brake system — only in the engine, which has a much larger thermal mass and active cooling.* Truckers who descend on the brakes alone are courting fade; truckers who descend in the right gear arrive cool. The same principle applies to descents in any vehicle. See §"Engine braking" below.

### Vented and drilled rotors

Performance rotors are **vented** — they're actually two rotor faces separated by radial vanes that act as a centrifugal pump. Spinning the rotor blows air through the vanes from the inside to the outside, dramatically improving heat dissipation. **Drilled** rotors have through-holes that further increase surface area and break up the gas film responsible for green fade. **Slotted** rotors have shallow grooves on the face that serve the same purpose. Race and sports cars often combine all three.

### F1 brakes — the extreme case

A modern F1 brake disc is **carbon-carbon composite**, not steel. Carbon-carbon's specific heat is roughly twice steel's *and* it retains structural strength at temperatures where steel would soften and warp. F1 rotors operate at **500–1000 °C glowing orange** for the duration of every braking event — the orange glow you see during a Monaco GP under-braking shot is real, not stylised. The discs are bored with thousands of tiny radial holes to handle gas escape and heat dissipation, and a single set lasts about one race weekend before the carbon-carbon is worn through.

The brake-pad material is also carbon-carbon, paired with the rotor, giving a $\mu_{\text{pad}}$ that **rises with temperature** up to ~600 °C and only then begins to fade. This is the opposite of road brakes — cold F1 brakes barely work, which is why the first lap of every race involves drivers weaving aggressively to warm up everything (tires AND brakes).

---

## ABS — the friction limit, engineered around

The single most consequential brake-system invention of the last 50 years. Mass-produced from Bosch's launch on the Mercedes S-Class in 1978, mandatory in the EU since 2004 on all new passenger cars and since 2016 on motorcycles.

### The slip ratio

When a wheel is rolling freely with no brake applied, the tire's contact-patch surface velocity equals the road's velocity past the contact patch — they match exactly. Call this **0% slip**. When the brake is locking the wheel completely so it's not rotating at all, the contact patch is at rest while the road races past — **100% slip**. The **slip ratio** $s$ interpolates between these:

$$s = \frac{v_{\text{road}} - r\omega_{\text{wheel}}}{v_{\text{road}}}$$

where $v_{\text{road}}$ is the vehicle's road speed and $r\omega_{\text{wheel}}$ is the tire's circumferential speed at the contact patch.

The key empirical fact, recalled here so the reader doesn't have to scroll up to [[The Friction Limit]] §"Stribeck curve":

**The effective tire-road friction coefficient is not maximum at $s = 0$. It peaks around $s = 0.10-0.20$ (10–20% slip), then drops as slip increases toward 100% (lockup).** A fully locked wheel is operating at $\mu_k$; a perfectly rolling wheel is operating below the available $\mu_s$; the peak grip lives at a small but nonzero slip ratio where the contact patch is doing a tiny controlled "creep" against the road, with peak microscopic interlock.

![[braking-slip-ratio-curve.svg|720]]

ABS exploits this. The control loop:


1. **Wheel-speed sensors** at each wheel measure $\omega_{\text{wheel}}$ many times per second (typical 50–100 Hz).
2. A **computed road speed** $v_{\text{road}}$ comes from cross-checking against the other three wheels (the wheels not currently locking are giving you the right answer).
3. If the slip ratio for any one wheel rises above the Stribeck peak (i.e., the wheel is about to lock), the **hydraulic modulator** in the brake circuit briefly *releases* pressure for that wheel — just for a few milliseconds.
4. As soon as the wheel speed recovers and slip drops back toward the peak, full pressure is restored.

This pulses 5–20 times per second per wheel, *per* wheel independently. The pedal feels notchy through your foot during a hard ABS stop — that's the modulator opening and closing. The car stops as fast as the four contact patches will allow, and crucially, **the wheels keep rolling, so you keep the ability to steer.** Pre-ABS, locked wheels meant the car slid in a straight line regardless of steering input. ABS gives back steering authority during emergency braking — that is its real superpower, not so much the stopping distance.

> [!warning] ABS does not always stop faster — it stops *steerable*
> A persistent myth. On dry tarmac, ABS-equipped and non-ABS cars stop in similar distances if a non-ABS driver is *skilled enough* to threshold-brake right at the friction peak. ABS is a robotised version of that skilled driver, applied independently to each of four wheels.
>
> Where ABS actually loses distance is on **loose surfaces** — gravel, deep snow, sand. A locked wheel on gravel builds up a wedge of loose material in front of it that *adds* to its deceleration. ABS keeps the wheel rolling and prevents the wedge from forming. So a Nordic rally driver's instinct on snow is to *disable* ABS — the locked-wheel wedge is faster on that surface than the rolling-wheel peak.
>
> The case for ABS is **never** "shortest stopping distance unconditionally." It's "shortest stopping distance *while retaining steering authority* on the surface most drivers spend most of their time on." That's a different claim. Once you understand it, you can predict where ABS wins (dry/wet tarmac in a panic stop with a swerve required) and where it loses (loose surfaces with no swerve required).

### Traction control — ABS's mirror twin

The same hardware that prevents the brake from locking a wheel can prevent the engine from spinning a wheel.

**Traction control** uses the same wheel-speed sensors. If one driven wheel is rotating *faster* than the road speed (slip ratio negative, the wheel is spinning), the system either:

- *Brakes that one wheel* using the ABS hydraulics (so the differential transfers torque to the other wheel), or
- *Cuts engine torque* by retarding ignition timing or closing the throttle, until the spin stops.

The physics is identical to ABS — you're holding the slip ratio near the Stribeck peak. The control direction is just reversed: ABS releases pressure to *reduce* slip-from-too-much-braking; TC applies pressure (or cuts engine) to *reduce* slip-from-too-much-throttle. Together they bracket the friction limit from both sides.

### ESC — yaw correction by per-wheel braking

**Electronic Stability Control** is the third generation, adding a **yaw-rate sensor** and a **steering-angle sensor** to the ABS hardware. The car continuously computes whether its actual yaw rate matches the driver-commanded yaw rate (from steering angle + speed). When they diverge — typically when the car is understeering ("pushing wide" out of a corner) or oversteering ("snap rotation" toward the inside of the corner) — ESC brakes one *individual* wheel to apply a counter-yaw torque.

- **Understeer correction:** brake the *inside rear* wheel. The asymmetric drag pulls the rear inward, rotating the car back toward the line.
- **Oversteer correction:** brake the *outside front* wheel. The asymmetric drag pulls the front outward, opposing the spin.

ESC is mandatory in the EU since 2014 and the US since 2012, and is credited with a roughly **30% reduction in fatal single-vehicle crashes**. It is, after seatbelts and airbags, probably the most consequential passive safety system to hit mass-market cars.

The shared theme: **ABS, traction control, and ESC are all closed-loop controllers that use individual-wheel braking to keep the car operating just inside the friction circle.** Different inputs (brake pedal demand vs throttle vs steering), same actuator (individual-wheel brake pressure modulation), same governing physics ($F \leq \mu_s N$ at each contact patch).

---

## Regenerative braking — using the motor as a generator

In an EV or hybrid, every electric motor on the drivetrain is also a generator (a fact of electromagnetic induction — Faraday's law applies in both directions). When the driver lifts off the accelerator or presses the brake, the motor's electronics reverse the current direction: instead of pushing current through the motor to make it spin the wheels, **the motor's spinning is *driven by* the wheels, and it pumps current back into the battery.** This generates a retarding torque on the wheels — i.e., a brake force — and at the same time recovers part of the kinetic energy as stored electrical energy. Friction-brake systems convert kinetic energy to heat and dissipate it; regenerative-brake systems convert it to electricity and *bank* it.

The efficiency numbers vary by system but a typical modern EV recovers ~60–70% of the braking-event kinetic energy as battery charge, with the remainder lost to electrical resistance, motor inefficiency, and the inverter. Over an urban drive cycle full of stop-and-go traffic, regen typically extends the range by **15–25%**.

Two important caveats that drivers should know:

1. **Regen alone cannot bring the car to a complete stop on a dry road.** The retarding torque vanishes as wheel speed drops toward zero (because generator output scales with rotational speed). So all EVs still have conventional hydraulic friction brakes for the last few km/h of every stop, for emergency stops at high deceleration that exceed the motor's regen capability, and as a redundancy for the inevitable day the regen system fails. The friction brakes are *less worn* in EVs because they do less work, but they are not gone.
2. **Regen is also bounded by the friction limit at the tire.** A motor that wants to apply $20{,}000~\text{N m}$ of regen torque to the rear wheels cannot do so if the tire-road friction would lock the rear wheels at half that torque — the EV's traction-control system will reduce regen torque to stay below the Stribeck peak. Regen interacts with ABS exactly the way friction-brake torque does: it's another way to demand grip from the contact patch, and the gatekeeper is the same.

> [!info] One-pedal driving and the brake-blend handoff
> Modern EVs offer **one-pedal driving** — lifting your foot off the accelerator triggers aggressive regen, often enough to bring you to a near-stop without ever touching the brake pedal. The driver experience is "I drive with one foot on one pedal, and the car decelerates the moment I lift."
>
> The engineering challenge under the hood is the **brake-blend handoff** — when the driver does press the brake pedal in an EV, the car must decide how much of the requested deceleration comes from regen and how much from the friction brakes. The handoff has to be *invisible* to the driver, even though the two systems have very different feel and response time. Get it right and the EV feels like it has telepathic brakes. Get it wrong and the brake pedal feels lumpy and inconsistent. The brake-blend control software is one of the more sophisticated pieces of code in an EV.

---

## Engine braking — the brake you didn't know you had

In any internal-combustion vehicle, taking your foot off the throttle while in gear causes the engine to act as an *air pump that the wheels are turning against*. The closed throttle creates a vacuum on the intake stroke; the compression stroke compresses air against atmospheric back-pressure that no longer matches; the exhaust stroke is forced. The net result is a retarding torque transmitted from the engine back through the drivetrain to the wheels. This is **engine braking** (also called **compression braking**).

In a manual transmission you can amplify engine braking by **downshifting** — selecting a lower gear forces the engine to spin faster at the same road speed, multiplying the pumping losses. A downshift from 5th to 3rd at high road speed produces dramatic deceleration without touching the brake pedal.

Large trucks have a dedicated **engine retarder** (often a "Jake brake," patented by Jacobs Vehicle Systems in 1965) that *deliberately* opens the exhaust valves at the top of the compression stroke. The compressed air vents to atmosphere instead of pushing the piston back down, so the energy of compression is dissipated as noise and heat in the exhaust rather than being recovered. The result is much more aggressive engine braking, at the cost of the very loud bark that makes Jake brakes illegal in many residential areas.

The crucial property of engine braking: **the heat goes into the engine, not into the brake system.** Engines have radiators, oil coolers, and a much larger thermal mass than rotors. They are designed to dissipate hundreds of kilowatts of heat continuously. Brakes are designed to dissipate hundreds of kilowatts of heat in *bursts*. On a long descent, this difference is the difference between arriving and not arriving.

EVs achieve the same effect via regen. The regen retarding torque does the work, the kinetic energy goes to the battery instead of to heat, and the friction brakes stay cold. This is one reason EVs are extraordinarily well-suited to mountain driving: the long descent that destroys an ICE car's brakes *recharges* an EV's battery.

---

## Brake bias and weight transfer

Under hard braking, weight transfers **forward** because of the inertial torque about the centre of mass. The forward wheels carry more normal force; the rear wheels carry less. From [[The Friction Limit]] we know $F_{\text{friction,max}} = \mu_s N$, so the front tires can support *more* braking force than the rears.

**Brake bias** is the front-to-rear distribution of brake torque. A typical street car runs ~65/35 front/rear bias; a track car runs 70/30 or higher. The bias is engineered into the system via different caliper sizes (bigger pistons up front), different pad areas, and sometimes an adjustable **brake-bias bar** in the pedal box (mandatory on race cars).

The penalty for wrong bias:

- **Too much front bias** → front wheels lock first → the car ploughs straight ahead with no steering authority (the dreaded "understeer-on-the-brakes" scenario). Survivable but slow.
- **Too much rear bias** → rear wheels lock first → the car *spins* because the rear has no lateral grip to resist any small yaw perturbation. Often unrecoverable in a road car.

Manufacturers tune bias slightly forward of the dynamic ideal so that, in a worst-case panic stop, you ploughed-understeer rather than spun. Modern ABS makes this much less critical because per-wheel modulation prevents *any* wheel from fully locking, but the underlying bias still sets the steady-state pressure distribution between front and rear.

### Worked example — calculating the optimal front bias

A car of mass $1500~\text{kg}$ has a wheelbase of $2.5~\text{m}$. The centre of mass is $1.1~\text{m}$ behind the front axle and $0.5~\text{m}$ above the road. If the car decelerates at $a = 8~\text{m s}^{-2}$ (about $0.8g$, a hard panic stop), what fraction of the total normal force is on the front axle?

Take moments about the rear-axle contact point. In the *non-inertial* frame of the decelerating car, there's a forward pseudo-force $ma = 12{,}000~\text{N}$ acting through the centre of mass. Gravity $mg = 14{,}715~\text{N}$ acts vertically through the centre of mass. The front-axle normal force $N_f$ acts upward at horizontal distance $2.5~\text{m}$ from the rear-axle contact.

Sum of moments about the rear contact (counter-clockwise positive):

$$N_f \times 2.5 = mg \times (2.5 - 1.1) + ma \times 0.5$$
$$N_f \times 2.5 = 14{,}715 \times 1.4 + 12{,}000 \times 0.5 = 20{,}601 + 6{,}000 = 26{,}601$$
$$N_f \approx 10{,}640~\text{N}$$

Total weight $mg = 14{,}715~\text{N}$, so the front axle carries $10{,}640/14{,}715 \approx 72\%$ of the load during this stop. Brake bias should be roughly 72/28 front/rear to put each wheel at the same fraction of its friction limit. The static (parked) front-load fraction for the same car is just $(2.5 - 1.1)/2.5 = 56\%$, so weight transfer under hard braking adds 16% of the total weight to the front axle — a huge dynamic effect that the bias must account for.

This is why race cars have adjustable bias bars: as fuel burns off, the car's centre of mass shifts and the optimal bias drifts. The driver adjusts it from the cockpit mid-race.

---

## Motorcycle braking — and the Stoppie limit

A motorcycle has only two wheels and most of the dynamic weight transfer under braking. The two complications:

1. **Brake bias has to be modulated by the rider in real time.** A bike's front brake provides the overwhelming majority of stopping power (typically 70–90% at the limit), and the rear is for fine control and slow-speed manoeuvring. *Squeezing only the front lever at high lean angles can lock the front wheel and produce an instant low-side crash*; squeezing only the rear loses most of the available grip. Riders are trained to use both, with the ratio depending on lean angle.

2. **Hard braking can pivot the bike over the front wheel.** If the deceleration $a$ is large enough that the inertial torque about the front contact patch exceeds the gravitational torque holding the bike down, **the rear wheel lifts off the ground.** This is the **Stoppie** — colloquially "the endo" — and at extreme decelerations the bike pivots fully over and lands on the rider. Stunt riders do brief controlled stoppies on purpose; emergency-braking on a bike requires holding the deceleration *just below* the stoppie limit.

The Stoppie limit derivation. Let $h$ be the height of the bike + rider centre of mass and $L_r$ be the horizontal distance from the front contact patch to the centre of mass. Take moments about the front contact patch in the decelerating frame. The rear wheel lifts off when the rear-axle normal force reaches zero, which occurs when:

$$ma \times h = mg \times L_r$$

$$\boxed{\; a_{\text{Stoppie}} = g \, \frac{L_r}{h} \;}$$

For a typical sportbike, $L_r \approx 0.75~\text{m}$ and $h \approx 0.65~\text{m}$, giving $a_{\text{Stoppie}} \approx 11.3~\text{m s}^{-2} \approx 1.15g$. *On a high-grip surface with sticky tires, the bike can decelerate at the Stoppie limit before exceeding the tire friction limit — so motorcycle braking is fundamentally geometry-bounded, not friction-bounded, at the limit.* This is also why MotoGP riders sometimes lift the rear wheel slightly under maximum trail-braking into a corner: they're operating at the geometric limit, not the rubber limit.

By contrast, in a four-wheeled car the equivalent "tip-over" deceleration is much higher than the friction limit because the wheelbase is long and the centre of mass is low. Cars are friction-limited; bikes are geometry-limited. The same friction-limit theory applies to both, but the binding constraint flips.

> [!tip] Why a fixed-gear cyclist can also do a stoppie
> The same derivation works for any two-wheeled vehicle with a low wheelbase-to-height ratio. A skilled fixed-gear cyclist applying back-pressure on the pedals (which is their entire brake) can lift the rear wheel and pivot the bike forward at a deceleration of perhaps $0.7-0.9g$. Mountain bikers descending technical terrain do this routinely as a deliberate technique. The physics is identical to the MotoGP case — only the absolute numbers change.

---

## Exam Notes

### Cambridge 9702 (A-Level Physics)

Braking is never a topic of its own; it is the standard *application* inside **§3.2 Non-uniform motion** — "qualitative understanding of frictional forces and viscous/drag forces", where a braking car is the textbook example — and it surfaces in Paper 2 / Paper 4 compound questions as "calculate the deceleration of a car of mass … braking from … over …" (Newton's second law + SUVAT, or the work–energy route $F\,d = 	frac12 mv^2$). The brake-bias moments derivation matches the style of §4.1 turning-effects questions and is a natural stretch for a strong candidate; the ABS and Stribeck material is beyond the syllabus.

### Cambridge 0625 (IGCSE Physics)

§1.5 Forces treats friction qualitatively, and §1.7 Energy the KE-to-heat transfer; a braking question is "describe the energy transfers when a car brakes" and "state the effect of a resultant force" — no calculation beyond $F = ma$ and $	frac12 mv^2$.

### IB Physics (A.2 Forces and momentum)

A.2.2 (contact forces, friction) and A.3 (work, energy, power) carry braking as the context for friction-limit and energy-conservation questions; the heat section of this page (KE $	o$ thermal energy as a worked $\Delta T$) and the regenerative-braking section answer the two question shapes IB actually sets.

### AP Physics 1 / AP Physics C: Mechanics

Unit 2 §2.7 (kinetic and static friction) and the energy unit both use braking as an application; AP C can frame the brake-bias moments calculation as a free-response part. The friction-limit treatment lives in [[The Friction Limit]].

### Where it is *not* examined

No board examines brakes as a topic: ABS, the slip curve, brake bias and regenerative systems are engineering enrichment. What every board examines is the physics underneath — friction limits, $F = ma$ under deceleration, and energy leaving as heat — and those are the parts of this page to revise.

---

## Common Misconceptions

### 1. "ABS always stops faster"

No. ABS holds slip at the Stribeck peak, which is the friction-maximum on tarmac. On gravel, snow, or sand, a *locked* wheel builds a wedge of loose material that adds to deceleration, and pure-locking can outperform ABS on those surfaces. The case for ABS is **steerability during a panic stop on the surface most drivers use most of the time** — that's a much narrower claim than "always faster."

**Fix:** discuss the slip-ratio curve. Ask: "Where is the peak? What does locked-wheel deceleration depend on?" Make the surface dependence explicit.

### 2. "Pressing the brake pedal harder always brakes harder"

Up to the friction limit, yes. Past the friction limit, pressing harder either (a) does nothing if ABS is intervening, or (b) locks the wheels if ABS is absent, *reducing* deceleration because kinetic $\mu_k < \mu_s$. The pedal commands hydraulic pressure, but the tire-road interface enforces the actual deceleration.

**Fix:** walk through the five-stage chain. Show that the gatekeeper is at the tire, not the pedal.

### 3. "The brake itself is the friction"

Conflating two different friction interfaces. The brake pad rubs against the rotor at one $\mu_{\text{pad}}$; the tire rubs against the road at a *different* $\mu_{\text{tire-road}}$. The pad-rotor friction *applies a torque* that the tire-road friction must then *cash in* as deceleration. Cars have huge pad-rotor friction reserves but limited tire-road friction, which is why brake systems are designed to be *over-powered* relative to tire grip.

**Fix:** label the two interfaces in a freebody diagram and ask which one is bigger. (Pad-rotor wins by a wide margin.)

### 4. "EVs don't need conventional brakes any more"

False. Regen tapers to zero as wheel speed approaches zero, cannot handle the deceleration of an emergency stop, and would leave the car with no redundancy in the event of a regen-system fault. Every road-legal EV has conventional hydraulic friction brakes; they're just used less.

**Fix:** ask the student to predict what the regen torque does as $v \to 0$. The generator output scales with rotational speed, so regen torque vanishes — friction brakes pick up the last few km/h.

### 5. "Engine braking wears out the engine"

A persistent garage myth. Engine braking puts the engine under the same compression and exhaust cycles it experiences under normal operation, just without fuel ignition. Modern engines are designed with thousands of times the wear margin needed for occasional engine braking. The argument that you should "use the brakes because they're cheaper to replace than the engine" misses that brake-fade on a long descent can kill you, while engine wear from light-throttle engine-braking will not measurably shorten the engine's life.

**Fix:** quote a manufacturer recommendation. Most owner's manuals for vehicles sold in mountainous markets explicitly recommend engine braking on long descents.

---

## Beyond syllabus

### The differential — and why one-wheel-spin used to mean stranded

A standard open differential lets the two driven wheels rotate at different speeds (necessary for cornering, since the inner wheel travels a shorter arc). The side effect: **if one wheel loses grip, all the engine torque is delivered to that wheel** and it spins freely while the gripping wheel does nothing. Pre-traction-control, this is why a single icy patch could leave a rear-wheel-drive car stranded with one rear wheel spinning uselessly.

Modern traction-control systems use the ABS hardware to **brake the spinning wheel**, which forces the differential to deliver torque to the gripping wheel. The same hardware that prevents lockup under braking enables drive under low traction. Engineering economy at its finest — three different problems (panic stopping, traction loss under power, stability under cornering) solved by *one* hardware platform.

### Brake-by-wire — the future of brake-blend

Modern EVs and some performance cars (Alfa Romeo Giulia QV, Toyota Mirai) use **brake-by-wire** where the brake pedal is electrically connected to the hydraulic actuator rather than mechanically. The pedal becomes a *sensor* whose output (pedal force and travel) is interpreted by the brake controller, which then decides how much hydraulic pressure to apply at each wheel, and *separately* how much regen torque to command.

This decoupling lets the brake-blend software handle the regen-to-friction handoff completely invisibly. The downside is that the pedal feel is *simulated* (via a pedal-feel emulator) rather than mechanical, which has historically been a tuning challenge. Toyota's first-generation Prius had brake-by-wire that famously felt "wooden" — Toyota spent the next two generations refining the simulator to match the feel of a conventional hydraulic system.

The deepest consequence: in a brake-by-wire system, the brake pedal is no longer a direct mechanical request for braking force. It is a *driver intent input* that the car interprets in the context of regen state, ABS state, ESC state, road conditions, and battery state-of-charge. This is the same evolution that happened to throttle pedals 20 years ago (drive-by-wire) — the brake pedal is following.

### Cooling ducts and aerodynamic brake-cooling

F1 and high-end road cars route ducted airflow from the front of the car to the inner face of each brake rotor. The ducts are sized to deliver enough cool-air mass-flow to keep the rotors below the boil-fade temperature even during sustained high-speed driving. Below a critical airspeed, however, the ducts deliver insufficient flow and the brakes overheat — which is why F1 drivers are sometimes told to "cool the brakes" on a slow lap by lifting and coasting on the straights to let airflow catch up.

The cooling duct is a great example of **active thermal management** at the engineering scale: you can either make the thermal mass huge (carbon-carbon rotors, big trucks with steel drums the size of pizza pans) or make the heat removal aggressive (ducted airflow, water cooling, oil-jet cooling on race motorcycles), and most extreme applications do both.

### Brake-by-light — the future-future

Research prototypes of **piezoelectric brakes** and **electromagnetic brakes** are in development. Both eliminate the hydraulic stage entirely: piezoelectric pads apply variable force directly from a control voltage; electromagnetic brakes use a copper rotor and a switchable magnetic field to apply eddy-current braking with no contact at all. Eddy-current brakes are already standard on roller coasters, Shinkansen trains, and gym treadmills (the resistance dial on a recumbent bike is exactly this). The challenge for cars is delivering enough braking torque at low speed (eddy-current force scales with speed and goes to zero at rest — same problem as regen) and at acceptable cost.

The deep continuity: every brake mechanism, from cave-man drag-foot to F1 carbon-carbon to electromagnetic eddy-current, is converting kinetic energy into some other form of energy that can be safely dissipated or stored. The friction limit at the tire is the unchanged gatekeeper across all of them.

---

## The hunter's payoff — what this card teaches you to trace

Three causal traces this card equips you with:

1. **"Where does the energy go?"** Given any braking event, follow the kinetic energy through the system: tire-road interface (a tiny amount as heat) → pad-rotor contact (most of it, as heat) → rotor thermal mass (briefly stored) → ambient air (eventually). In an EV, a parallel branch goes wheel → drivetrain → motor-as-generator → inverter → battery (most of it, as stored electricity). *The total $\Delta KE$ is conserved; the engineering is about routing.*

2. **"What's the binding constraint?"** Cars are friction-limited (the tire-road $\mu_s N$ caps deceleration). Bikes are geometry-limited (the Stoppie threshold caps deceleration before friction matters). Long descents are heat-limited (rotors fade before friction matters). For any given braking scenario, identify which of {friction, geometry, heat} is the active constraint, and the right engineering response follows.

3. **"What does the control system do?"** ABS, traction control, ESC, regen-blend, brake-bias control are all closed-loop controllers operating around the friction limit. For each, identify the sensor (wheel speed, yaw rate, pedal position), the actuator (hydraulic pressure, engine torque, regen current), and the setpoint (Stribeck peak, target yaw rate, target deceleration). The control structure repeats across systems; only the variables change.

These three traces — energy routing, binding constraint, control structure — generalise from car brakes to elevator braking, aircraft anti-skid, locomotive blended braking, roller coaster eddy-current zones, and (with adjusted vocabulary) to any system where you need to remove kinetic energy under operational constraints. Once you can run the trace cold, you can read a new vehicle's brake-system spec sheet and predict how it will feel before you ever press the pedal.

---

## Connections

- **Parent:** [[The Friction Limit]] — every brake-system constraint cashes out as the $F \leq \mu_s N$ inequality at the tire-road interface. This card is the engineering side of that physics.
- **Prerequisites:**
   - [[Newton's Laws of Motion]] — N2 ($F = ma$) is the link between brake force and deceleration; N1 motivates the weight-transfer analysis.
   - [[Forces and Equilibrium]] — the moments-about-the-rear-axle calculation in the brake-bias derivation uses static-equilibrium machinery from this card.
   - [[Work, Energy and Power]] — the $\Delta KE = \tfrac{1}{2}mv^2$ accounting for heat dissipation is the energy-conservation framework.
   - [[SUVAT]] — stopping-distance calculations use $v^2 = u^2 - 2as$ with $a = \mu g$ as the deceleration.
   - [[Friction (Vocab)]] — the vocabulary card with definitions of $\mu_s$, $\mu_k$, and the contact-friction setup.

- **Cross-domain bridges:**
   - **Control engineering** — ABS, traction control, ESC are all closed-loop bang-bang or PID controllers operating around a setpoint at the friction-limit boundary. The slip-ratio control is the canonical introductory example used in mechatronics curricula.
   - **Electromagnetic induction** — regenerative braking is Faraday's law in action: a motor driven by external torque becomes a generator. The retarding torque on the wheels is the back-EMF of the generator extracting electrical work.
   - **Thermodynamics** — brake fade is a first-law accounting problem (where does the heat go?) combined with material-temperature limits. Specific heat capacity and surface convection set the thermal-mass design budget.
   - **Materials science** — pad compounds, rotor metallurgy, brake-fluid chemistry. The carbon-carbon brakes used in F1 are a direct technology transfer from spacecraft heat-shield development.

- **Misconceptions cleared:** ABS does **not** always stop faster (only with steering authority on most-common surfaces); the brake pedal does **not** directly command brake force (it commands hydraulic pressure, which becomes torque, which then *requests* tire-road friction); the brake-pad-rotor friction is **not** the same as the tire-road friction (different interfaces, different coefficients, different magnitudes); EVs **do** still have conventional brakes (regen vanishes near zero speed); engine braking does **not** measurably wear out the engine (manufacturer-recommended on long descents).

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\mu_{\text{pad}}$ | `\mu_{\text{pad}}` | Pad-rotor friction coefficient (≈ 0.35–0.45 street, higher race) |
| $\mu_{\text{tire-road}}$ | `\mu_{\text{tire-road}}` | Tire-road friction coefficient (≈ 0.7–1.5 for rubber on tarmac) |
| $\tau_{\text{brake}} = F_{\text{pad}}\, r_{\text{rotor}}$ | `\tau_{\text{brake}} = F_{\text{pad}}\, r_{\text{rotor}}` | Wheel-deceleration torque from pad-rotor contact |
| $s = (v_{\text{road}} - r\omega)/v_{\text{road}}$ | `s = (v_{\text{road}} - r\omega)/v_{\text{road}}` | Slip ratio: 0 free-rolling, 1 locked |
| $\Delta KE = \tfrac{1}{2}mv^2$ | `\Delta KE = \tfrac{1}{2}mv^2` | Energy dissipated in a stop from $v$ to rest |
| $\Delta T = \Delta KE / (m c)$ | `\Delta T = \Delta KE / (m c)` | Rotor temperature rise for a single stop |
| $a_{\text{Stoppie}} = g\, L_r / h$ | `a_{\text{Stoppie}} = g\, L_r / h` | Two-wheeled vehicle's geometric brake limit (rear wheel lifts off) |
| $N_f \times W = mg(W - L_r) + ma\, h$ | `N_f \times W = mg(W - L_r) + ma\, h` | Front-axle normal force during braking deceleration $a$ |
