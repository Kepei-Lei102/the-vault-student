---
chinese: 傅里叶变换 (Fùlǐyè biànhuàn)
prerequisites:
  - "[[Fourier Series]]"
  - "[[Euler's Formula and De Moivre's Theorem]]"
  - "[[Integration]]"
leads_to:
  - "[[Digital Audio Workstation]]"
tags:
  - subject/mathematics
  - domain/trigonometry
  - level/university
  - type/definition
  - type/proof
  - type/visual-tool
  - notation/complex-exponential
  - misconception/fft-is-a-different-transform
  - misconception/zero-padding-adds-resolution
---

# Fourier Transform 傅里叶变换

## The question — what is inside a recording?

A synthesiser can *build* a sound by adding oscillations. A spectrum analyser does the reverse: you give it samples, and it tells you how strongly different oscillations are present. Nothing inside the laptop recognises a violin. It multiplies, adds and changes coordinates.

[[Fourier Series]] describes a repeating signal using harmonics of one fundamental. A clap, a whole song and a changing voltage need a wider language. There are three related objects to keep separate:

| Object | Input | Output |
|---|---|---|
| Fourier series | a periodic function of continuous time | discrete harmonic coefficients |
| Continuous Fourier transform | a suitable function on the whole time axis | a function of continuous frequency |
| Discrete Fourier transform (DFT) | a finite vector of $N$ samples | a finite vector of $N$ frequency coordinates |

An **FFT**, or fast Fourier transform, is an algorithm for computing a DFT. It changes the amount of work, not the mathematical answer.

**Hear the ingredients first:** [[Fourier Series#First example — build an A4 piano-style note|build an A4 piano-style sound by adding sine waves]], then use the FFT to recover the steady mixture’s 440, 880, 1320, … Hz ingredients. Synthesis adds the components; analysis finds them.

### 中文锚点

听一段钢琴录音，耳朵只收到一股混在一起的声波，你却能跟着哼出里面的音。电脑没有耳朵，但可以拿不同快慢的振动去试：把录音和一个候选振动逐点相乘，再把结果加起来。快慢对得上，贡献就容易积累；对不上，正负贡献往往互相抵消。傅里叶变换就是这样把一段起伏变成一份“各个频率有多少”的配方。它找的是振动成分，不会自动分清哪一部分是钢琴、哪一部分是人声。

## 1. A frequency probe that remembers phase

By Euler's formula, $e^{-2\pi ift}=\cos(2\pi ft)-i\sin(2\pi ft)$. Multiplying a signal by this probe tests **two quadratures** together: cosine and sine, a quarter-cycle apart. A real signal may align poorly with cosine and strongly with sine; keeping both avoids losing a component just because the recording started at a different moment.

For an absolutely integrable signal, meaning $\int_{-\infty}^{\infty}|x(t)|\,dt<\infty$, define

$$\boxed{X(f)=\int_{-\infty}^{\infty}x(t)e^{-2\pi ift}\,dt.}$$

Frequency $f$ is in cycles per second (Hz) when $t$ is in seconds. $X(f)$ is complex: its magnitude and phase both matter. If $x$ is measured in volts, $X$ has units volt-seconds. It is a **density of frequency contribution**, not directly the voltage amplitude of a single sinusoid.

Under suitable inversion hypotheses,

$$\boxed{x(t)=\int_{-\infty}^{\infty}X(f)e^{2\pi ift}\,df.}$$

For example, if $x$ is absolutely integrable and has bounded variation near $t$, the symmetrically truncated inverse integral converges to $[x(t^-)+x(t^+)]/2$, hence to $x(t)$ at a continuity point. Bounded variation means finite accumulated variation locally; a finite collection of smooth pieces is a familiar sufficient case. Square-integrable signals instead admit an $L^2$ transform and inversion in the mean-square sense, through a further theorem. These are sufficient frameworks, not a claim that every formal integral converges. [NIST, Fourier-transform inversion](https://dlmf.nist.gov/1.14.i)

> [!warning] Check the convention before copying a formula
> With angular frequency $\omega=2\pi f$, a common convention is $\widehat x(\omega)=\int x(t)e^{-i\omega t}\,dt$ and $x(t)=\frac1{2\pi}\int\widehat x(\omega)e^{i\omega t}\,d\omega$. Some authors distribute the constants symmetrically. A missing $2\pi$ can be a convention mismatch rather than an algebra error. Here we use **Hz** throughout.

### How the series opens into a transform

Start with a compactly supported pulse inside $[-T/2,T/2]$ and repeat it every $T$. Its series coefficients are

$$c_k=\frac1T\int_{-T/2}^{T/2}x(t)e^{-2\pi i(k/T)t}\,dt
=\frac1T X(k/T).$$

The frequency spacing is $\Delta f=1/T$, so its reconstruction is

$$\sum_k c_ke^{2\pi i(k/T)t}
=\sum_k X(k\Delta f)e^{2\pi ik\Delta f t}\,\Delta f.$$

As the repeated copies move farther apart, the lines crowd together and this has the shape of a Riemann sum for the inverse integral. The factor $\Delta f$ is essential: each individual coefficient shrinks while their number per Hz grows. This motivates the transform; justifying the infinite sum and limit requires the inversion hypotheses, not merely a convincing picture.

## 2. Worked example — a short pulse needs a broad spectrum

Let $x(t)=1$ for $|t|<\tau/2$ and zero outside. Values at the two endpoints do not change its integral.

**Trigger:** constant height on one finite interval. **Tool:** integrate the complex exponential over that interval.

$$X(f)=\int_{-\tau/2}^{\tau/2}e^{-2\pi ift}\,dt
=\frac{e^{-\pi if\tau}-e^{\pi if\tau}}{-2\pi if}
=\frac{\sin(\pi f\tau)}{\pi f}
=\tau\,\operatorname{sinc}(f\tau).$$

Our **normalised sinc** is $\operatorname{sinc}(u)=\sin(\pi u)/(\pi u)$, with value 1 at zero. Thus $X(0)=\tau$, exactly the pulse's area. The first zeros are at $f=\pm1/\tau$. Halving the duration doubles their distance from zero.

![[fourier-transform-pulse.svg|1000]]

*A narrower unit-height pulse has a lower central value $X(0)$ but a wider frequency spread. The right panel plots the signed real transform, not its magnitude.*

This is why a sudden click requires many frequencies. The rectangular example has long sinc tails; it does **not** have a finite bandwidth. A pure sinusoid sustained forever is the opposite extreme: it is not absolutely integrable and is represented by delta spikes in the distributional theory, not by pretending the ordinary integral converges.

### Three rules, derived by substitution

**Linearity:** an integral distributes over a sum, so $ax+by\leftrightarrow aX+bY$.

**Delay:** for $y(t)=x(t-t_0)$, substitute $u=t-t_0$:

$$Y(f)=\int x(u)e^{-2\pi if(u+t_0)}du=e^{-2\pi ift_0}X(f).$$

A delay leaves magnitude unchanged and tilts phase. A whole-recording **magnitude** spectrum therefore cannot tell you when that recording began; the full complex transform retains the timing information.

**Time scaling:** for real $a\ne0$, $x(at)\leftrightarrow |a|^{-1}X(f/a)$, by $u=at$ and reversing integration limits if $a<0$. Playing a waveform twice as fast halves its duration and doubles its frequencies. Preserving pitch while changing duration needs more than this operation.

For finite-energy signals, **Plancherel's theorem** gives $\int|x(t)|^2dt=\int|X(f)|^2df$ in this convention: the continuous counterpart of Parseval. It is a theorem about these transforms, not proof that arbitrary numerical spectra already have the right normalisation.

## 3. The DFT — coordinates for a finite list

A computer receives samples $x_0,\ldots,x_{N-1}$ taken at spacing $\Delta t=1/f_s$. Define

$$\boxed{X_k=\sum_{n=0}^{N-1}x_ne^{-2\pi ikn/N},\qquad k=0,\ldots,N-1.}$$

These $X_k$ are **discrete sums**; their units equal those of the samples. They are not the same object as the continuous $X(f)$. When sampling and time truncation errors are controlled, the finite-record quadrature is $X(f_k)\approx\Delta t\,X_k$, with $f_k=kf_s/N$. That approximation needs both adequate sampling and a suitable observation interval.

### Why these probes separate exactly

Set $q=e^{2\pi i(k-\ell)/N}$. If $k\ne\ell$ modulo $N$, then $q\ne1$ but $q^N=1$, and the geometric sum gives

$$\sum_{n=0}^{N-1}e^{2\pi i(k-\ell)n/N}
=\frac{1-q^N}{1-q}=0.$$

If $k=\ell$, all $N$ terms equal 1 and the sum is $N$. These roots-of-unity probes are orthogonal under the discrete sum. They form $N$ independent directions in an $N$-dimensional complex vector space: no coordinates are missing.

![[fourier-transform-probes.svg|1000]]

*For the complex input $x_n=e^{2\pi i3n/8}$, the probe $k=2$ leaves eight rotating unit contributions whose sum is zero. The matching probe $k=3$ leaves eight contributions equal to 1. The right-hand sum is 8, not 1.*

Substitute the forward definition into the proposed inverse and exchange these **finite** sums:

$$\frac1N\sum_{k=0}^{N-1}X_ke^{2\pi ikm/N}
=\sum_{n=0}^{N-1}x_n\left(\frac1N\sum_{k=0}^{N-1}e^{2\pi ik(m-n)/N}\right)=x_m.$$

Therefore

$$\boxed{x_n=\frac1N\sum_{k=0}^{N-1}X_ke^{2\pi ikn/N}.}$$

There is no convergence issue here. Forward then inverse returns the exact finite vector in exact arithmetic; floating-point computation adds rounding error. Using the same orthogonality when expanding the squared inverse gives discrete Parseval:

$$\sum_{n=0}^{N-1}|x_n|^2=\frac1N\sum_{k=0}^{N-1}|X_k|^2.$$

### Worked example — four samples, all coordinates visible

Take $x=[1,0,-1,0]$. **Trigger:** only two entries are nonzero. **Tool:** substitute them before expanding a full matrix.

$$X_k=1-e^{-\pi ik}=1-(-1)^k,\qquad X=[0,2,0,2].$$

The inverse is $x_n=\tfrac12e^{2\pi in/4}+\tfrac12e^{2\pi i3n/4}=\cos(\pi n/2)$ at integer $n$. Bin 3 is the negative-frequency partner of bin 1. Both are needed to make a real cosine. If $f_s=8$ Hz, the bins represent 0, 2, $\pm4$, and $-2$ Hz respectively.

## 4. Reading the bins without inventing information

The DFT frequency spacing is $\Delta f=f_s/N=1/(N\Delta t)$. The period of the DFT's implied repetition is $N\Delta t$, although the time from the first recorded sample to the last is $(N-1)\Delta t$.

For even $N$, bins above $N/2$ represent negative frequencies $(k-N)f_s/N$; bin $N/2$ is the shared Nyquist endpoint. For odd $N$ there is no bin exactly at $f_s/2$. NumPy's `fftfreq` supplies the signed axis; `rfftfreq` supplies the nonnegative axis for real-input `rfft`. [NumPy conventions](https://numpy.org/doc/stable/reference/routines.fft.html)

For real samples, $X_{N-k}=\overline{X_k}$. To see why, conjugate the defining sum: $\overline{x_n}=x_n$ and $e^{-2\pi in}=1$.

**Amplitude calibration.** For a rectangular record containing an integer number of cycles of $A\cos(2\pi kn/N+\phi)$, away from DC and Nyquist, $X_k=(NA/2)e^{i\phi}$. Thus $2|X_k|/N$ is its peak amplitude. At DC or the even-$N$ Nyquist bin, do **not** double. Mean-square/RMS and power-density plots require different scaling; a raw FFT magnitude is not automatically a calibrated dB meter.

**Aliasing happens before the transform.** Sampling $e^{2\pi ift}$ at $t=n/f_s$ cannot distinguish $f$ from $f+mf_s$, because the extra factor is $e^{2\pi imn}=1$. At 8 kHz, real cosines at 5 kHz and 3 kHz have identical samples. No FFT can recover which was present. A suitably band-limited analogue input and an anti-alias filter are part of the acquisition system; see [[Sound Encoding]].

## 5. The FFT — reuse the same half-sized answers

A direct DFT computes $N$ sums with $N$ terms each: $O(N^2)$ work. For $N$ a power of two, split the samples into even and odd indices. Put $W_N=e^{-2\pi i/N}$.

**Trigger:** the kernel exponent factors when $n=2r$ or $2r+1$. **Tool:** partition a sum, then reuse $W_N^2=W_{N/2}$.

$$X_k=\sum_{r=0}^{N/2-1}x_{2r}W_{N/2}^{kr}
+W_N^k\sum_{r=0}^{N/2-1}x_{2r+1}W_{N/2}^{kr}
=E_k+W_N^kO_k.$$

The two half-sized transforms repeat after $N/2$ bins, while $W_N^{k+N/2}=-W_N^k$. Hence a pair of outputs costs one shared product:

$$\boxed{X_k=E_k+W_N^kO_k,\qquad X_{k+N/2}=E_k-W_N^kO_k.}$$

This pair is a **butterfly**. Recurse until each transform contains one sample. Each of the $\log_2N$ levels has $N/2$ butterflies, so the total is $O(N\log N)$. Induction proves correctness: length 1 is exact; assuming the halves are correct, the displayed identity reconstructs every full-length bin. [Cooley and Tukey, 1965](https://web.stanford.edu/class/cme324/classics/cooley-tukey.pdf)

```python
import numpy as np

def fft_radix2(x):
    x = np.asarray(x, dtype=complex)
    N = len(x)
    if x.ndim != 1 or N == 0 or N & (N - 1):
        raise ValueError("Use a nonempty vector of power-of-two length")
    if N == 1:
        return x.copy()
    E = fft_radix2(x[::2])
    O = fft_radix2(x[1::2])
    t = np.exp(-2j * np.pi * np.arange(N // 2) / N) * O
    return np.concatenate((E + t, E - t))

x = np.array([1, 0, -1, 0])
print(np.round(fft_radix2(x), 10))  # [0, 2, 0, 2], complex dtype
assert np.allclose(fft_radix2(x), np.fft.fft(x))
```

This implementation requires power-of-two lengths; **the DFT does not**. Production FFT libraries support other lengths and factorisations. Zero padding changes the input vector and its frequency grid, even when it also makes a computation convenient.

### Measure the saving — and the overhead

One run of the companion lab on an arm64 Mac, Python 3.11/NumPy 2.4.1; medians of five runs after a warm-up. The direct implementation builds its dense exponential matrix on every call. Times are illustrative, not a hardware-independent promise.

| $N$ | Direct DFT terms $N^2$ | Radix-2 butterflies | Direct / ms | Python radix-2 / ms | NumPy FFT / ms |
|---|---|---|---|---|---|
| 128 | 16,384 | 448 | 0.316 | 0.550 | 0.0043 |
| 256 | 65,536 | 1,024 | 1.309 | 1.193 | 0.0048 |
| 512 | 262,144 | 2,304 | 4.791 | 1.882 | 0.0060 |
| 1,024 | 1,048,576 | 5,120 | 17.436 | 3.716 | 0.0089 |

A direct term and a butterfly are different units of work. Their counts expose growth; the measured times include allocation, exponentials and interpreter overhead. For tiny vectors the recursive Python implementation loses. Its advantage emerges with size. [[Big-O Notation]] describes the growth, not the stopwatch result at every input.

## 6. A window changes the question

A recording lasts for a finite interval. Taking that piece amounts to multiplying the longer signal by a window $w(t)$. Even a pure sinusoid becomes a finite burst. Its spectrum spreads, as the rectangular-pulse example predicted.

In DFT language, repeating a cut-out containing a non-integer number of cycles generally creates a mismatch at the seam. Many DFT components are then needed to reproduce the finite sample vector. This is **spectral leakage**, not new instruments appearing in the recording.

A Hann window tapers both ends towards zero. For the symmetric length-$N$ version,

$$w_n=\frac12\left(1-\cos\frac{2\pi n}{N-1}\right),\qquad 0\le n<N.$$

It reduces distant sidelobes but broadens the main lobe. Close frequencies may become harder to separate even while a weak, well-separated tone becomes easier to see. Tapering also changes amplitude: for an isolated tone near a bin centre, $2|\operatorname{DFT}(wx)_k|/\sum_nw_n$ is the usual coherent-gain correction. It is not an exact cure for arbitrary off-bin tones or overlapping components.

![[fourier-transform-windows.svg|1000]]

*Same 64 samples, same 8.5-cycle cosine. Upper row: rectangular versus Hann weighting, and the windowed spectra. Lower row: zero padding supplies more plotted frequency points, while a genuinely longer record can separate two nearby tones. Spectra are normalised as labelled, not interchangeable power-density estimates.*

**Zero padding is interpolation of the finite-record spectrum.** Appending zeros replaces $\sum_{n=0}^{N-1}x_ne^{-2\pi ifn/f_s}$ by samples on a finer frequency grid; it does not change that function or lengthen the observed data. It can improve peak-location interpolation, but it cannot create the resolving power of a longer observation. “Bin spacing” and “ability to distinguish two tones” are not synonyms.

## 7. A spectrogram — ask locally, then move

Listen first. The generated tone stays at 220 Hz, rises smoothly, then stays at 440 Hz.

![[fourier-transform-changing-tone.wav]]

A full complex transform can reconstruct this recording. But its magnitude plot does not directly display the order of the events. For that, analyse short overlapping pieces: the **short-time Fourier transform (STFT)**.

For a length-$M$ window and hop $H$ samples, one local-phase convention is

$$S_{m,k}=\sum_{r=0}^{M-1}x_{mH+r}w_r e^{-2\pi ikr/M}.$$

Zero padding at the recording boundaries may be used so the end samples receive adequate window coverage. A **spectrogram** plots $|S_{m,k}|^2$, often in dB relative to an explicitly chosen reference. It omits phase; the complex STFT retains it.

![[fourier-transform-spectrogram.svg|1000]]

*The same 4-second signal at 8 kHz: 32 ms versus 128 ms Hann windows, with a quarter-window hop. Each plot uses power relative to its own maximum. The long window narrows steady-tone bands; the short window localises the changing part more tightly.*

**The trade-off is physical information, not a plotting defect.** A short window sees too few cycles to distinguish nearby frequencies well. A long window gathers those cycles but mixes a longer period of change. Reducing the hop puts frames closer together; it does not shorten each frame or sharpen its intrinsic time resolution.

### Can the pieces be put back together?

Yes, with complex phase and compatible analysis/synthesis windows. Inverse-transform a frame to recover $x_{mH+r}w_r$. Multiply by $w_r$ again, place it at its original sample positions and add overlapping frames. At sample $n$ the total is $x_n\sum_m w_{n-mH}^2$. Divide by that weight sum:

$$x_n=\frac{\sum_m \bigl[\operatorname{IDFT}(S_m)\bigr]_{n-mH}w_{n-mH}}
{\sum_m w_{n-mH}^2},$$

where out-of-frame window entries are zero and the denominator must be nonzero. The companion uses boundary padding and overlapping Hann windows, checks coverage and recovers the original samples. A picture of magnitudes alone cannot perform this inverse. [SciPy STFT and inverse](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.ShortTimeFFT.html)

![[fourier-transform-manim.mp4]]

*Watch the probe contributions cancel or align; then follow a sliding window and its spectrum. The final scene adds delayed copies to make audible echoes. Audio uses synthetic signals; no speech or music recording is required.*

## 8. Convolution — how a room answers every sample

Clap in a stairwell. The direct arrival is followed by reflections. An **impulse response** $h$ describes how a linear, time-invariant system responds to one unit impulse; linearity permits scaling and addition, and time invariance permits shifting the same response.

Write a discrete input as a sum of weighted, shifted impulses. Each sample $x_m$ contributes a shifted copy $x_mh_{n-m}$. Adding the responses gives

$$\boxed{y_n=(x*h)_n=\sum_m x_mh_{n-m}.}$$

For continuous signals, the corresponding definition is $(x*h)(t)=\int x(u)h(t-u)\,du$. A measured room response can therefore put a dry recording into that acoustic model. The room and signal chain must behave sufficiently linearly and remain effectively unchanged; distortion or moving geometry need more than one fixed response.

### Derive the convolution theorem

**Trigger:** a shifted copy inside an integral. **Tools:** exchange integrals under absolute-integrability assumptions, then substitute $v=t-u$.

$$\begin{aligned}
\mathcal F\{x*h\}(f)
&=\int\!\int x(u)h(t-u)e^{-2\pi ift}\,du\,dt\\
&=\int x(u)e^{-2\pi ifu}\,du\;\int h(v)e^{-2\pi ifv}\,dv
=X(f)H(f).
\end{aligned}$$

A long sum of delayed copies becomes pointwise multiplication. Conversely, multiplication in time corresponds to convolution in frequency under suitable hypotheses. That explains leakage another way: the finite window's spectrum spreads each original frequency component.

For a sinusoidal input to an LTI system, $H(f)$ is the complex gain at that frequency. Thus an equaliser changes magnitude **and phase** according to its frequency response. A practical EQ need not run an FFT; short recursive filters can implement it directly.

### Worked example — the circular-wrap trap

Let $x=[1,2,3]$ and $h=[1,\tfrac12]$. **Trigger:** one original plus a half-strength delayed copy. **Tool:** write each overlap.

$$y=[1,\;2+\tfrac12,\;3+1,\;\tfrac32]=[1,2.5,4,1.5].$$

The output has length $3+2-1=4$. Multiplying two **3-point** DFTs and inverting gives $[2.5,2.5,4]$: the final 1.5 wrapped onto the start. The DFT product computes **circular convolution**, in which sample indices are taken modulo the transform length.

For finite sequences of lengths $L_x,L_h$, pad both to at least $L_x+L_h-1$. Then no nonzero tail wraps and the circular answer equals the wanted linear convolution. [SciPy convolution](https://docs.scipy.org/doc/scipy/tutorial/signal.html#convolution-correlation)

```python
x = np.array([1., 2., 3.])
h = np.array([1., .5])
L = len(x) + len(h) - 1
result = np.fft.ifft(np.fft.fft(x, L) * np.fft.fft(h, L)).real
print(result)                         # [1.  2.5 4.  1.5]
assert np.allclose(result, np.convolve(x, h))
```

**Hear the operation:** first three dry plucks, then exactly the same samples convolved with a synthetic four-arrival response: delays 0, 0.24, 0.48 and 0.72 seconds; gains 1, 0.55, 0.30 and 0.16. The files share the same gain scale. This is an echo model, not a recording of a real room or a dense reverb algorithm.

![[fourier-transform-dry.wav]]

![[fourier-transform-echo.wav]]

## 9. Beyond syllabus — why this mathematics is everywhere

Recall that a Fourier transform measures coordinates against oscillations. The variable need not be time: in an image, spatial frequency counts how rapidly brightness changes across distance.

**CT reconstruction.** For an ideal parallel-beam projection $p_\theta(s)$ of an object $\rho(x,y)$, integrate along lines perpendicular to direction $(\cos\theta,\sin\theta)$. Substituting the rotated coordinates into its 1-D Fourier transform gives

$$\widehat p_\theta(f)=\iint\rho(x,y)e^{-2\pi if(x\cos\theta+y\sin\theta)}dx\,dy
=\widehat\rho(f\cos\theta,f\sin\theta).$$

A projection supplies a radial slice of the object's 2-D transform. Multiple angles fill different slices; this underlies Fourier reconstruction and the filtering step in filtered back-projection. Real scanners require geometry, sampling and noise corrections. [[X-rays and CT]] supplies the acquisition context. [Kak and Slaney, reconstruction theory](https://epubs.siam.org/doi/10.1137/1.9780898719277.ch3)

**MRI uses a different measurement.** Magnetic gradients encode position in phase; under the basic imaging model, the measured signal samples spatial Fourier space, called *k-space*. An inverse transform reconstructs the spatial distribution. MRI does not collect X-ray projection shadows. [Stanford, MRI signal equation and k-space](https://web.stanford.edu/class/rad229/Notes.html)

**Audio fingerprints.** The published Shazam method selects spectrogram peaks and hashes pairs using their frequencies and time separation. Matching many pairs at one time offset identifies a recording. The transform supplies stable features; indexing and verification do the recognition. It is not “one FFT knows the song”, nor is this account a claim about every detail of the current service. [Wang's original paper](https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf)

**Compression.** Baseline JPEG uses the related discrete cosine transform (DCT); MP3 and AAC use filter-bank/modified-DCT machinery. Transform coordinates make selective quantisation useful, but a reversible coordinate change alone saves no information. Discarding or coarsening coefficients and coding the result produces the compression. See [[Compression]] and [Brandenburg, MP3 and AAC Explained](https://www.iis.fraunhofer.de/content/dam/iis/de/doc/ame/conference/AES-17-Conference_mp3-and-AAC-explained_AES17.pdf).

**Time-stretch and pitch correction.** A phase vocoder analyses overlapping frames, estimates phase progression and synthesises with a changed time spacing. It must adjust phase coherently; stretching a spectrogram picture is insufficient. Resampling then supplies a route to a changed pitch at restored duration. Transients and phase relationships make high-quality processing harder than this outline. These are applications of the STFT and resynthesis, not consequences of the time-scaling rule alone. [Julius O. Smith, phase vocoder](https://ccrma.stanford.edu/~jos/sasp/Phase_Vocoder.html)

## Hands-on — make a prediction before changing a parameter

Run `python3 fourier-transform-lab.py --audio --bench` beside its source. NumPy and SciPy are required. It checks direct DFT versus the recursive FFT and NumPy, inverse reconstruction, Parseval, pulse quadrature, amplitude/phase, aliasing, STFT reconstruction and padded convolution.

1. Change the tone from a bin-centred frequency to halfway between bins. Predict leakage before looking.
2. Double the zero-padding length while holding the recorded samples fixed. Predict which grid changes and which information does not.
3. Use a longer STFT window. Predict the steady-tone bandwidth and the spread around the glide.
4. Move the echo delays. Predict when the copies arrive; add them directly and compare with the FFT result.
5. Replace each complex transform coefficient by its magnitude before inverting. Predict why a real waveform may emerge but the original timing does not return.

## Common misconceptions

- **“FFT is an approximation to the DFT.”** The algorithm computes the same finite sum; rounding is numerical, not a new definition.
- **“The highest plotted peak is the loudest instrument.”** Peaks are frequency components. One instrument produces many; several instruments can share one.
- **“More FFT bins mean finer measured resolution.”** Distinguish a longer observation from zero padding the same observation.
- **“Windowing improves everything.”** Sidelobes, main-lobe width and amplitude calibration trade against each other.
- **“Frequency analysis forgets time.”** Full complex coefficients preserve the finite vector. Magnitudes alone discard phase; an STFT makes local timing easier to inspect.
- **“Multiply spectra and get ordinary convolution.”** A finite DFT gives circular convolution; pad enough to prevent wraparound.

## Exam Notes

**Cambridge/OxfordAQA maths:** the inspected 0580, 0606, 9709, 9231, 9260 and 9660 specifications do not prescribe Fourier-transform integrals, DFT/FFT algorithms, STFT or the convolution theorem. This is enrichment built from their integration, complex-number and series tools. “Transformations” in those specifications does not mean Fourier analysis.

**Edexcel IAL, IB AA/AI and AP Calculus AB/BC:** the inspected specifications/frameworks do not name this transform package as required content. A power-series topic is not Fourier-transform coverage. No formula-sheet entitlement or past-paper attribution is claimed; the examples are original teaching exercises and measured computations.

**Physics and CS:** harmonics, digital sound and sampling provide connections to 0625/9702 and 0478/9618. The detailed transforms and implementation here are not thereby required on those boards. Use their existing waves and data-representation treatments for the assessed scope.

## Connections

- **Prerequisite:** [[Fourier Series]] — harmonic projection and the periodic starting point.
- **Algebra underneath:** [[Euler's Formula and De Moivre's Theorem]], [[De Moivre at Work]] — complex oscillations and finite sums of roots of unity.
- **Calculus:** [[Integration]] — the continuous transform and substitution proofs.
- **Computing:** [[Big-O Notation]], [[Recursion]] — why divide-and-conquer changes the work.
- **Signals:** [[Sound Encoding]], [[Compression]], [[Sound]] — samples, coding and timbre.
- **Imaging:** [[X-rays and CT]] — measurements from which an image is reconstructed.
- **Application:** [[Digital Audio Workstation]] — processing recorded sound with buffers, filters and effects.

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $X(f)$ | `X(f)` | continuous transform in Hz convention |
| $X_k$ | `X_k` | unnormalised forward DFT coefficient |
| $f_s$ | `f_s` | sample rate |
| $W_N=e^{-2\pi i/N}$ | `W_N=e^{-2\pi i/N}` | forward DFT root |
| $\Delta f=f_s/N$ | `\Delta f=f_s/N` | DFT bin spacing |
| $S_{m,k}$ | `S_{m,k}` | complex STFT frame/bin |
| $x*h$ | `x*h` | convolution |
