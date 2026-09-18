---
chinese: 衍射 (yǎnshè)
prerequisites:
  - "[[Progressive Waves]]"
  - "[[Stationary Waves]]"
  - "[[Superposition and Interference]]"
leads_to:
  - "[[Electromagnetic Spectrum]]"
  - "[[Wave-Particle Duality]]"
  - "[[Sound Waves]]"
tags:
  - subject/physics
  - domain/waves
  - domain/optics
  - level/IGCSE
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/9702-8-2
  - syllabus/9702-8-4
  - syllabus/IB-Physics-C-3-2
  - syllabus/IB-Physics-C-3-5
  - syllabus/IB-Physics-C-3-6
  - syllabus/AP-Physics-2-14-7
  - syllabus/AP-Physics-2-14-8
  - misconception/diffraction-changes-wavelength
  - misconception/highest-order-equals-number-of-fringes
  - misconception/diffraction-is-refraction
  - type/deep
---

# Diffraction 衍射

> *A wave does not know where the edge of a gap is. Every point of the wavefront that gets through keeps radiating in all directions, and what you see beyond the gap is those points adding up. Narrow the gap and there are fewer of them to disagree, so the wave spreads; make a row of gaps and their agreement becomes so strict that only a few directions survive at all.*

![[diffraction-manim.mp4]]

## Definition

### Formal

**Diffraction** is the spreading of a wave as it passes through a gap or around the edge of an obstacle, into the region that a straight-line path would leave in shadow. The effect is greatest when the gap or obstacle is comparable in size to the wavelength: a gap much wider than $\lambda$ lets the wave through almost unchanged with bent edges; a gap of about $\lambda$ or less turns it into near-semicircular wavefronts, as if from a point. Diffraction changes the *direction* of the wave's energy, never its wavelength, frequency or speed.

For a **single slit** of width $a$, the diffracted wave has an intensity pattern with a broad central maximum and **minima** at

$$a\sin\theta = m\lambda, \qquad m = 1, 2, 3, \dots$$

so the central maximum spans $-\lambda/a$ to $+\lambda/a$ in $\sin\theta$, twice the width of every other maximum, and the first side maximum carries under five per cent of the centre's intensity.

A **diffraction grating** is a large number $N$ of parallel slits a distance $d$ apart (given as *lines per metre*, $d$ is its reciprocal). Light of wavelength $\lambda$ falling on it normally is sent into a few sharp directions, the **orders**, where every slit's contribution is in step:

$$d\sin\theta = n\lambda, \qquad n = 0, \pm 1, \pm 2, \dots$$

The orders are at the same angles as two slits $d$ apart would give, but far sharper (angular width $\propto 1/N$) and far brighter ($\propto N^2$), with almost nothing between them. Because $\sin\theta \le 1$, the highest order is $n_{\max} = \lfloor d/\lambda \rfloor$, and a full screen shows $2n_{\max} + 1$ maxima.

### Intuitive

Stand in a corridor and listen to a conversation in a room whose door is ajar. You hear it: sound diffracts through the gap, because its wavelength, a metre or so, is comparable with the door. You cannot *see* into the room from the same spot, because light's wavelength is a thousandth of a millimetre and a door is a million wavelengths wide, so light goes straight. Same door, same physics, different ratio of gap to wavelength. The grating is a different trick: line up thousands of gaps at exact spacing, and a colour can only leave in the directions where the light from every gap arrives in step. Each colour has its own such directions, so white light fans into a spectrum, and measuring one angle gives you the wavelength to three figures with a protractor.

### 中文锚点

衍射是波穿过缝隙或绕过障碍物边缘时向"影子区"扩散的现象。它的强弱只取决于一个比值：缝宽与波长之比。缝比波长宽得多，波几乎直着穿过去，只有边缘弯一点；缝和波长差不多或更窄，穿过去的波就像从一个点发出的半圆形波面。衍射改变的是波能量传播的方向，波长、频率和速度都不变——这是最容易记错的一点。为什么会这样？惠更斯的解释：波面上每一点都是一个新的小波源，缝里能通过的那些点各自向四面八方发波，缝外看到的是它们的叠加；缝越窄，点越少，彼此越难互相抵消，波就散得越开。对宽度为 $a$ 的单缝，暗纹出现在满足 $a\sin\theta = m\lambda$ 的方向上，中央亮纹的宽度是其他亮纹的两倍。衍射光栅是大量等距（间距 $d$）的平行狭缝：只有在每一条缝发出的光都恰好同相的方向上才有亮线，即 $d\sin\theta = n\lambda$——位置和双缝一样，但因为要求"所有缝一齐同意"，亮线极窄、极亮，中间几乎全黑。因为 $\sin\theta \le 1$，最高级次是 $d/\lambda$ 向下取整；整个屏幕上的亮线数是它的两倍加一。这张卡里的每一个图样都是把惠更斯小波逐点相加算出来的，公式是从图样里读出来的，不是放进去的。

---

## Part I — Why a wave spreads: Huygens

Christiaan Huygens's construction (1678) is the one idea under everything in this card. **Every point on a wavefront acts as a source of secondary wavelets, and the new wavefront is the envelope of those wavelets.** For a wave in open water this only reproduces the wave: the wavelets from a long straight front add up to another long straight front, because the sideways contributions of neighbouring points cancel. Put a barrier in the way and the cancellation is spoiled at the edges. The points near the edge have no neighbours on one side to cancel their sideways wavelets, so the wave leaks round the corner. That is diffraction at an edge.

Through a **gap**, the same argument sets the size of the effect. If the gap is many wavelengths wide, most points in it have neighbours on both sides, the sideways wavelets cancel over most of the width, and the wave goes on nearly straight with only its two edges bent. If the gap is about a wavelength, there are too few points for the cancellation to work at all, and the wavelets add to something close to a single point source: semicircular wavefronts, spreading into the whole half-plane beyond.

![[diffraction-ripple-gaps.svg|700]]

`diffraction-sim.py` does not use Huygens' rule; it solves the two-dimensional wave equation on a grid, with a wall and a gap, and Huygens' picture is what comes out. Ten wavelengths past the barrier, the amplitude at $45^\circ$ off-axis is a large fraction of the on-axis amplitude for a gap of half a wavelength and a small one for a gap of six. The **9702 and IGCSE fact** is the qualitative version: *the narrower the gap relative to the wavelength, the greater the spreading*, and the wavelength itself is unchanged. The examiners' report for June 2022 notes that more candidates picked the wrong answer than the right one on exactly this: "for a gap that is much wider than the wavelength, the spreading of the wave, and hence the diffraction angle, is less than for a smaller gap. The wavelength is unaffected."

> [!tip] Diffraction is not refraction
> Refraction is a change of *speed* at a boundary between two media, and the wavelength changes with it. Diffraction is spreading past an edge in *one* medium, and nothing about the wave changes except where it is going. The examiners see the two confused every year.

---

## Part II — The single slit: minima at $a\sin\theta = m\lambda$

Now make Huygens quantitative. Treat the slit of width $a$ as a row of point sources, and look at the sum far away in a direction $\theta$. The script does exactly this, four hundred sources across the slit, their wavelets added with the phase each has acquired, and squares the sum.

![[diffraction-single-slit.svg|700]]

The pattern has a broad central maximum and a series of much weaker side maxima, with **minima** at $\sin\theta = 0.200, 0.399, 0.599, 0.798$ for $a = 5\lambda$: exactly $m\lambda/a$. Here is why, without the sum. Take the direction where the wavelet from the top edge of the slit has travelled exactly one wavelength further than the wavelet from the bottom edge, so $a\sin\theta = \lambda$. Pair each point in the top half of the slit with the point $a/2$ below it: those two are half a wavelength apart in path, so they cancel. Every point has a partner, everything cancels, and the direction is dark. The same pairing with the slit cut into four gives the second minimum at $a\sin\theta = 2\lambda$, and so on. Between the minima the cancellation is incomplete and a little light survives: the first side maximum is $4.7\%$ of the centre, the second $1.6\%$.

Two consequences follow, both measured in the figure's second panel:

- **The central maximum is twice as wide as the others**, spanning $-\lambda/a$ to $+\lambda/a$ in $\sin\theta$ while every other maximum spans $\lambda/a$.
- **Narrow slit, wide spread.** The half-width of the central maximum is $\theta_1 = \sin^{-1}(\lambda/a)$: $6.9^\circ$ for $a = 5\lambda$, $17.4^\circ$ for $a = 2\lambda$ (with $\lambda = 600$ nm), $36.8^\circ$ for $a = \lambda$. Below $a = \lambda$ there is no minimum at all: the slit is a point source, and the script finds the intensity at $60^\circ$ still eleven per cent of the centre's. Change the wavelength instead and the same rule runs the other way: at $a = 2\,\mu$m, blue light ($450$ nm) spreads to $13^\circ$ and red ($700$ nm) to $20^\circ$. Longer wavelength, more spreading.

The A-Level asks for the *qualitative* effect of gap width relative to wavelength and stops there; IB HL and AP Physics 2 ask for the formula, and for the intensity graph with its wide central peak and small side lobes.

---

## Part III — Two slits, honestly: the envelope and the missing order

[[Superposition and Interference]] drew Young's fringes as equally bright, which is true only for slits of zero width. Real slits have a width $a$, so each slit sends its light into Part II's single-slit pattern, and the two-slit interference can only happen where that pattern lets any light go. The result is Young's fringes, spaced by $\lambda/d$ in $\sin\theta$, sitting inside a single-slit envelope of half-width $\lambda/a$.

![[diffraction-double-envelope.svg|700]]

The script sums two slits of width $2\,\mu$m with centres $10\,\mu$m apart. The bright fringes are at $d\sin\theta/\lambda = 0, 1, 2, 3, 4$ as Young says, with heights $1.00, 0.88, 0.58, 0.26, 0.06$: the envelope. And the **fifth order is missing**. It should be at $\sin\theta = 5\lambda/d = 0.300$, and that is exactly where the single-slit minimum $\lambda/a = 0.300$ falls, because $d/a = 5$. When $d/a$ is a whole number, that order is always absent; the fringes are there, but each slit alone sends no light in that direction, so there is nothing for them to interfere with. IB's HL C.3.5 asks for this picture and the words *modulated by the single-slit envelope*; AP's 14.8 calls it the interference pattern "superimposed within the envelope created by single-slit diffraction".

---

## Part IV — The grating: many slits, and why the orders are sharp

Now the syllabus's main instrument. A **diffraction grating** is thousands of parallel slits, or ruled lines on glass, with a spacing $d$ so small that a typical grating has $300$ to $600$ lines per millimetre, so $d = 1/(\text{lines per metre})$ is a few micrometres, a few wavelengths of light.

![[diffraction-grating-geometry.svg|700]]

**Where the maxima are.** Light falling normally on the grating leaves each slit as a Huygens wavelet. In a direction $\theta$, the wavelet from each slit has travelled $d\sin\theta$ further than the one from its neighbour. If that extra path is a whole number of wavelengths, *every* slit's light is in step with every other's, and the direction is bright:

$$d\sin\theta = n\lambda.$$

This is the same condition as for two slits $d$ apart, and the maxima are at the same angles. The difference is what happens *between* them.

**Why they are sharp.** With two slits, a direction slightly off a maximum has the two wavelets slightly out of step, and the intensity falls off gently: broad fringes. With a thousand slits, a direction slightly off a maximum has the thousandth slit's wavelet out of step with the first by a thousand times that small phase, which is enough to cancel it, and everything between cancels pairwise. Only directions where the agreement is *exact* survive.

![[diffraction-grating-n.svg|700]]

The script adds the wavelets from $N$ slits and reads off the result. With $d = 2.5\,\mu$m and $\lambda = 600$ nm the principal maxima sit at $\sin\theta = 0, 0.240, 0.480, \dots$ for every $N$; the first-order peak has a width of $7.0^\circ$ for two slits, $2.6^\circ$ for five, $0.63^\circ$ for twenty and $0.13^\circ$ for a hundred, width $\propto 1/N$; and its height is $25\times$, $400\times$ and $10{,}000\times$ one slit's for $N = 5, 20, 100$: $N^2$, because $N$ amplitudes add in step before they are squared. The small secondary maxima between the orders (there are $N - 2$ of them) shrink to nothing as $N$ grows. That is why a grating's spectrum is a set of fine bright lines and a double slit's is a smear of bands.

**How many orders.** Since $\sin\theta$ cannot exceed $1$, $n \le d/\lambda$. For the script's grating $d/\lambda = 4.17$, so four orders on each side and nine maxima in all on a screen that wraps round. The examiners' reports return to this arithmetic every year: candidates find $n_{\max}$ correctly and then give it as the number of fringes, forgetting the other side and the central maximum. **Total on a full screen $= 2n_{\max} + 1$**, and $n_{\max}$ is rounded *down*, never to the nearest integer.

**Measuring a wavelength.** This is the syllabus's second outcome for the grating, without the spectrometer. Shine the light through a grating of known $d$ onto a screen a measured distance away; measure the distance from the central spot to the $n$th-order spot, get $\theta$ from the tangent, and $\lambda = d\sin\theta/n$. Use a high order for accuracy, since the same angular error is a smaller fraction of a larger angle; or, as June 2021's question does, measure $\theta$ for several known wavelengths, plot $\sin\theta$ against $\lambda$, and read $n/d$ off the gradient. With a *white* source each order is a full spectrum, violet innermost, and the second-order red overlaps the third-order violet: $2 \times 700 > 3 \times 400$.

**Grating against double slit**, since 9702 asks for the comparison in words: same positions for the maxima; the grating's are much sharper, much brighter, and have dark space between them, so its spectra are resolvable into separate lines where the double slit's blur together.

---

## Where it is the working tool

- **Every spectrometer.** The grating is how a chemist reads which elements are in a flame, how an astronomer reads a star's composition and its redshift, and how the fibre-optic internet packs a hundred colours down one fibre and separates them again at the far end (a grating in a box called a demultiplexer). The line spectra of [[Wave-Particle Duality]]'s energy levels are seen through one.
- **The limit of every camera, telescope and microscope.** A lens is an aperture, so a point of light is imaged as Part II's pattern, a disc of half-angle $1.22\lambda/D$ for a circular aperture. Two stars closer than that cannot be told apart, however good the glass; this is why big telescopes are big, why radio telescopes are enormous (a $3$ cm wavelength needs a $300$ m dish for the resolution a $6$ cm lens gets in visible light), and why a microscope cannot see anything smaller than about half a wavelength of the light it uses, which is the reason electron microscopes exist.
- **The CD, the DVD and the beetle.** The pits on a compact disc are $1.6\,\mu$m apart, a grating of $625$ lines per millimetre, which is why it throws a rainbow; the DVD's $0.74\,\mu$m spacing throws a wider one. Iridescent beetles, butterfly wings and peacock feathers are gratings grown from chitin, colour with no pigment.
- **X-ray crystallography.** A crystal's atomic planes are a three-dimensional grating with $d$ of a few tenths of a nanometre, so they diffract X-rays and nothing longer; the pattern of spots gives the atoms' arrangement, and Rosalind Franklin's Photograph 51 of 1952 is the diffraction pattern of DNA.
- **Radio and Wi-Fi round corners.** A $12$ cm Wi-Fi wave diffracts round a door frame; a $0.5$ mm 60 GHz link does not, which is why the fast bands need line of sight. Long-wave radio at kilometre wavelengths diffracts over hills.
- **Why the bass comes through the wall.** A $1$ kHz sound has a $34$ cm wavelength and diffracts through an open door; a $10$ kHz sound at $3$ cm barely does. What you hear from the next room is the low end because of Part I, not because the wall filters.

---

## Worked examples — every tool named

### Example 1 — how many fringes on the semicircular screen (Cambridge 9702, June 2024 Paper 22, Q6)

Light of wavelength $520$ nm falls normally on a grating with line separation $3.8 \times 10^{-6}$ m; the pattern forms on a semicircular screen centred on the grating. *(a) Determine the total number of bright fringes.* — *Tool: $d\sin\theta = n\lambda$ with the largest possible angle, $\theta = 90^\circ$, selected because a semicircular screen catches every direction up to $90^\circ$:* $n_{\max} = (3.8 \times 10^{-6} \times \sin 90^\circ)/(520 \times 10^{-9}) = 7.3$, rounded down to $7$. *Tool: both sides plus the centre:* $2 \times 7 + 1 = 15$. *(Scheme: $n = d\sin\theta/\lambda$, C1; $7.3$, C1; $15$, given as an integer, A1. The reports list $7$, $8$, $14$ and $16$ as the common wrong answers: the highest order, the rounded-up order, and both without the centre.)*

*(b) The light is replaced with red light. (i) Is its frequency greater, less or the same? (ii) What happens to the number of fringes?* — Red has the **lower** frequency, so the **longer** wavelength; $n_{\max} = d/\lambda$ falls, so **fewer** fringes. *(B1; M1 A1. Not proportional: the report warns against "the number of fringes is inversely proportional to the wavelength", because $n_{\max}$ is a floor, not a ratio.)*

### Example 2 — the order at a given angle, and fewer lines (Cambridge 9702, March 2026 Paper 22, Q5(c))

Light of wavelength $4.5 \times 10^{-7}$ m on a grating with $6.7 \times 10^{5}$ lines per metre; a bright spot at $37^\circ$ from the central spot. *(i) Its order.* — *Tool: $d = 1/(\text{lines per metre})$, the step most often skipped:* $d = 1/(6.7 \times 10^5) = 1.49 \times 10^{-6}$ m. *Tool: $n = d\sin\theta/\lambda$* $= (1.49 \times 10^{-6} \times \sin 37^\circ)/(4.5 \times 10^{-7}) = 2.0$, so $n = 2$. *(C1 C1 A1.)* *(ii) The grating is replaced by one with fewer lines per metre. Does the spacing of the spots increase, decrease or stay the same?* — Fewer lines per metre means **larger $d$**, so for each order $\sin\theta = n\lambda/d$ is smaller: the spots move *in*. **Decreases.** *(B1. The opposite of Young's $x = \lambda D/a$ only in appearance: both say that a larger spacing between sources gives a smaller angle.)*

### Example 3 — the intensity sketch (Cambridge 9702, November 2025 Paper 21, Q4(b))

Vertically polarised light of wavelength $540$ nm on a grating of spacing $5.0 \times 10^{-6}$ m; a circular screen; the central fringe has intensity $I_0$. *(i) Show that the first-order fringe is at $6.2^\circ$.* — *Tool: $\theta = \sin^{-1}(n\lambda/d)$* $= \sin^{-1}(540 \times 10^{-9}/5.0 \times 10^{-6}) = \sin^{-1}(0.108) = 6.2^\circ$. *(ii) The second order.* — $\sin^{-1}(0.216) = 12^\circ$. *(A1.)* *(iii) Sketch $I$ against $\theta$ from $-15^\circ$ to $+15^\circ$.* — Sharp peaks at $0$, $\pm 6^\circ$ and $\pm 12^\circ$, each reaching $I_0$ (the maxima of a grating are all of comparable height at these small angles), and **zero intensity between them**. *(Two B marks: the five peaks in the right places; peaks with nothing between. A sketch that draws Young's gently varying fringes loses the second mark: Part IV's figure is the point of the question.)*

### Example 4 — describe, then the graph (Cambridge 9702, June 2021 Paper 21, Q4(c)–(d))

*(c) Describe the diffraction of the light waves at the grating.* — The waves **spread out** as they pass through **each slit** of the grating. *(The report: "some simply stated that the waves spread"; the mark wants the spreading located at the slits, and it does not want the interference pattern, which was not asked.)* *(d) The angle $\theta$ of the fourth-order maximum is measured for several wavelengths; $\sin\theta$ is plotted against $\lambda$ and the gradient is $G$. (i) Express $d$ in terms of $G$.* — *Tool: $n\lambda = d\sin\theta$ rearranged as a straight line, $\sin\theta = (n/d)\lambda$, so the gradient is $n/d$ with $n = 4$:* $G = 4/d$, $d = 4/G$. *(C1 A1. The June 2024 report, on the same shape: "a significant number did not substitute the value of the order, clearly stated in the question as the fourth.")* *(ii) Sketch the line for the second-order maxima.* — Gradient $2/d$, **half** the printed line's, still through the origin, so at $700$ nm it is half the height. *(M1 A1.)*

### Example 5 — the best question from another board: all the colours in one order (IB Physics HL, May 2025 TZ2 Paper 2, Q4(c)–(d))

Light containing every wavelength from $550$ nm to $650$ nm falls normally on a grating of $580$ lines per millimetre. *(c) Why is the interference at the central point constructive?* — The path difference between the light from every slit is **zero** there, for every wavelength, so all arrive in phase. *(d) The largest order in which every wavelength of the beam is present.* — *Tool: the longest wavelength is the first to run out of orders, since $n_{\max} = d/\lambda$ is smallest for it:* $d = 1/(580 \times 10^3) = 1.72 \times 10^{-6}$ m, and $n \le d/\lambda_{\max} = 1.72 \times 10^{-6}/650 \times 10^{-9} = 2.65$, so **the second order** is the last complete one. *(Scheme, three marks: consider the largest wavelength or $\theta = 90^\circ$; $2.65$; $n = 2$. An answer of $3$ from using the smallest wavelength scores two of the three.)*

### Example 6 — more slits, same spacing (IB Physics HL, November 2021 Paper 2, Q8(d))

A graph shows the intensity after four slits: primary maxima with small secondary maxima between them. The number of slits is increased, their separation and width unchanged. *State what happens to (i) the angular position of the primary maxima, (ii) their width, (iii) the intensity of the secondary maxima.* — *Tool: Part IV's three facts.* (i) **Unchanged**, since $d\sin\theta = n\lambda$ depends on $d$ alone. (ii) **Narrower**, width $\propto 1/N$. (iii) **Decreases** (relative to the primaries), the secondaries fading towards zero as $N$ grows. The script's $N = 5 \to 100$ run is the question with numbers.

### Example 7 — the MCQ shapes (Cambridge 9702 Paper 1, from the June 2022 and November 2021 examiners' reports)

Three shapes that recur. *The highest order on a semicircular screen:* $n = d\sin 90^\circ/\lambda = (2.0 \times 10^{-6})/(5.4 \times 10^{-7}) = 3.7$, so the third order, and the report notes candidates must know that the maximum diffraction angle is $90^\circ$. *The overlap of orders with two wavelengths:* the $n$th order of $630$ nm coincides with the $(n+1)$th of $420$ nm when $n \times 630 = (n+1) \times 420$, giving $n = 2$; then $d$ follows from $2 \times 630 \times 10^{-9} = d\sin 31^\circ$. *The angle between two orders:* find both angles from $\sin\theta_n = n\lambda/d$ and **subtract**; the November 2021 report says a large proportion chose the angle of the second or third order alone, "which suggests candidates know how to use the diffraction grating equation. Candidates need to carefully read the question."

---

## Hands-on

- **`diffraction-sim.py`** — every pattern from Huygens wavelets summed: the single slit and its minima, the width-against-wavelength table, the two slits with their envelope and missing order, the grating from two slits to a hundred, and the two-dimensional ripple tank through four gaps. Change `d/a` in `double_slit()` to a non-integer and watch the missing order come back.
- **`diffraction-figures.py`** and **`diffraction-manim.py`** — the five figures, and the two films: three ripple tanks side by side, then one slit becoming a grating.
- **A CD and a laser pointer.** Shine the pointer at a CD at a shallow angle and catch the reflected spots on a wall: a reflection grating with $d = 1.6\,\mu$m. Measure the angle of the first-order spot and you have the pointer's wavelength to a few per cent. A DVD ($0.74\,\mu$m) throws the spots much wider, and a Blu-ray ($0.32\,\mu$m) so wide that a red pointer gets no first order at all: $\lambda > d$.
- **A finger and a streetlight.** Squint at a distant light through the narrowing gap between two fingers: as the gap closes the light spreads into a band with dark lines in it. That is Part II, with your fingers as the slit and your eye as the screen.

---

## Common Misconceptions (Teaching Notes)

### 1. "Diffraction changes the wavelength"
Nothing about the wave changes but its direction. Wavelength, frequency and speed are set by the source and the medium, and the gap is neither. The June 2022 report singled this out: the spreading angle changes with gap width; "the wavelength is unaffected".

### 2. "The highest order is the number of fringes"
$n_{\max} = \lfloor d/\lambda \rfloor$ is the order on *one side*. The screen shows $n_{\max}$ on each side and the central maximum: $2n_{\max} + 1$. And $7.3$ rounds to $7$, not $8$: a fraction of an order does not exist.

### 3. "Diffraction is refraction" (and "diffraction is interference")
Refraction bends a wave by changing its speed at a boundary; diffraction spreads it past an edge in one medium. And the *diffraction* at a grating is the spreading at each slit; the *interference* is what the spread waves then do. June 2021's question asked for the first and was answered with the second.

### 4. "A grating's maxima are in different places from a double slit's"
Same $d$, same angles. The grating's are sharper and brighter with dark gaps between; that is the whole comparison 9702 asks for.

### 5. "Number of fringes is inversely proportional to wavelength"
It is a floor function of $d/\lambda$, so it steps down as $\lambda$ rises and can stay the same across a range of wavelengths. Say *fewer*, with the reason; do not say *proportional*.

### 6. "Fewer lines per millimetre means a wider pattern"
Fewer lines means a *larger* $d$, and $\sin\theta = n\lambda/d$ *smaller*: the pattern closes up. The intuition "bigger spacing, bigger angle" is exactly backwards, for gratings and for Young's slits alike.

---

## Exam Notes

### Cambridge 9702 (§8.2 Diffraction and §8.4 The diffraction grating — Paper 1 and Paper 2)

§8.2 has two outcomes, both qualitative: explain the meaning of *diffraction*, and understand experiments that demonstrate it including the effect of gap width relative to wavelength, the ripple tank being the named example. No single-slit formula is examined. §8.4: recall and use $d\sin\theta = n\lambda$, and describe the use of a grating to measure a wavelength (the spectrometer is excluded). The worked Paper 2 questions in Examples 1–4 show these grating tasks: the number of fringes on a semicircular screen, an order from an angle with lines-per-metre to convert, an intensity sketch with peaks and nothing between, or a graph of $\sin\theta$ against $\lambda$. Paper 1 asks the three shapes of Example 7. Use [[Stationary Waves]] for §8.1 and [[Superposition and Interference]] for §8.3; together these topics cover superposition.

### Cambridge 0625 (§3.1 — Core Papers 1/3; Extended Papers 2/4)

Core: describe diffraction through a narrow gap, and the ripple tank showing diffraction due to a gap and due to an edge. Supplement: how wavelength and gap size affect diffraction through a gap, and how wavelength affects diffraction at an edge. The qualitative treatment and the ripple-tank experiment in [[Progressive Waves]] supply this scope; no diffraction formula or grating is required.

### IB Physics (C.3.2, and HL C.3.5–C.3.6)

C.3.2 (SL and HL): diffraction around bodies and through apertures, qualitatively, Part I. C.3.5 (HL): single-slit diffraction using the booklet’s small-angle relation $\theta \approx \lambda/b$ in radians (IB’s $b$ is the slit width; the full first-minimum condition is $\sin\theta=\lambda/b$), the double-slit pattern **modulated by the single-slit envelope**, and intensity graphs: Parts II and III. C.3.6 (HL): multiple slits and gratings with $n\lambda = d\sin\theta$, the sharpening with $N$, and the missing-wavelengths reasoning of Example 5. IB likes to ask what changes when $N$ changes (Example 6) and to combine the grating with a wavelength range.

### AP Physics 2 (Units 14.7 and 14.8)

14.7: diffraction as the spreading of a wave around an obstacle or through an opening, most pronounced when the opening is comparable to the wavelength; single-slit minima at $a\sin\theta = m\lambda$ and the intensity pattern. 14.8: the double-slit pattern as interference *within* the single-slit envelope, which with [[Superposition and Interference]]'s interference half completes the unit. Gratings appear as "multiple openings" with the same equation.

### Where it is *not* examined

- **AP Physics 1** and **AP Physics C** have no diffraction.
- **9702 does not examine** the single-slit formula, the intensity distribution of a single slit, the Rayleigh criterion, or the spectrometer; those are IB HL, AP 2 and Beyond.

---

## Connections

- **Builds on:** [[Progressive Waves]] — wavefronts, the ripple tank, and the qualitative diffraction it introduced; [[Stationary Waves]] — the superposition principle and its reason; [[Superposition and Interference]] — the superposition that every Huygens sum performs, and the double slit whose envelope Part III supplies.
- **Extends into:** [[Electromagnetic Spectrum]] — gratings as the way wavelengths are measured across it; [[Wave-Particle Duality]] — electron diffraction as the evidence that matter waves, and X-ray diffraction as the ruler for atoms; [[Sound Waves]] — why bass diffracts and treble does not.
- **Bridges:** [[Trigonometric Equations]] — every order is a $\sin^{-1}$ with a domain check.

---

## Beyond Syllabus

### The circular aperture, and Rayleigh's criterion
A round hole of diameter $D$ gives a central disc (the Airy disc) with its first dark ring at $\sin\theta = 1.22\lambda/D$, the $1.22$ coming from a Bessel function where the slit had a sine. Rayleigh's criterion says two point sources are *just resolved* when the centre of one's disc falls on the first minimum of the other's, $\theta_{\min} = 1.22\lambda/D$. A $300$ m radio dish at $3.2$ cm resolves $1.3 \times 10^{-4}$ rad; a $5$ mm pupil at $550$ nm resolves $1.3 \times 10^{-4}$ rad too, which is why the naked eye and a giant radio telescope have the same resolution and neither can split a car's headlights at ten kilometres.

### Fraunhofer and Fresnel
Everything in this card is *far-field* (Fraunhofer) diffraction: the screen far enough that the rays to a point are parallel. Close to the slit (Fresnel diffraction) the pattern is different and harder, and the ripple-tank images of Part I are Fresnel: the semicircles near a narrow gap are the near field of a point source.

### The pattern is a Fourier transform
The far-field amplitude in direction $\sin\theta$ is the Fourier transform of the aperture. A slit's transform is a sinc; a grating's is a comb of sharp peaks; a crystal's is the reciprocal lattice. This is why a lens, which brings the far field to its focal plane, is an analogue Fourier computer, and why optical processing was a serious technology before digital signal processing overtook it.

### Electrons through the same slits
Send electrons at a crystal (Davisson and Germer, 1927) or at a double slit (Jönsson, 1961) and they diffract like waves with $\lambda = h/p$, a few picometres, which is why an electron microscope resolves atoms where light cannot. The pattern builds up one electron at a time. That is where [[Wave-Particle Duality]] begins.

---

## LaTeX Reference

| Rendered | Source | Meaning |
|---|---|---|
| $a\sin\theta = m\lambda$ | `a\sin\theta = m\lambda` | single-slit minima, $m = 1, 2, \dots$ |
| $d\sin\theta = n\lambda$ | `d\sin\theta = n\lambda` | grating maxima, $n = 0, \pm1, \dots$ |
| $d = \dfrac{1}{\text{lines per metre}}$ | `d = \dfrac{1}{\text{lines per metre}}` | grating spacing |
| $n_{\max} = \lfloor d/\lambda \rfloor$ | `n_{\max} = \lfloor d/\lambda \rfloor` | highest order; $2n_{\max}+1$ maxima in all |
| $\sin\theta_{\min} = 1.22\,\lambda/D$ | `\sin\theta_{\min} = 1.22\,\lambda/D` | circular aperture, Rayleigh |
| $I \propto N^2$, width $\propto 1/N$ | `I \propto N^2` | grating orders as $N$ grows |
