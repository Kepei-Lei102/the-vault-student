#!/usr/bin/env python3
"""Rebuild the DAW audio lab and figures. NumPy + SciPy + Matplotlib.
Run: python3 daw-lab.py [--out DIRECTORY]
All musical stems are original procedural synthesis. The unmodified atrium IR
is by Liam G / Conner's IR Library; see daw-room-ir-LICENSE.txt and the card.
Offline teaching DSP: retain Biquad/Compressor objects across streaming blocks.
"""
from pathlib import Path
import argparse
import json
import math
import re
import numpy as np
from scipy.io import wavfile
from scipy import signal

FS = 48000
HERE = Path(__file__).resolve().parent


def db_gain(db):
    return 10 ** (np.asarray(db) / 20)


def rms(x):
    return np.sqrt(np.mean(np.asarray(x) ** 2))


def read_wav(path):
    fs, x = wavfile.read(path)
    if np.issubdtype(x.dtype, np.signedinteger):
        x = x.astype(float) / (2 ** (np.iinfo(x.dtype).bits - 1))
    elif x.dtype == np.uint8:
        x = (x.astype(float) - 128) / 128
    else:
        x = x.astype(float)
    return fs, x


def write_wav(path, x, fs=FS, seed=2026):
    """PCM16 bounce: TPDF dither, round once; refuse overload, never normalise."""
    x = np.asarray(x)
    if not np.all(np.isfinite(x)) or np.max(np.abs(x)) > .98:
        raise ValueError('Leave sample-peak headroom before the PCM16 bounce.')
    rng = np.random.default_rng(seed)
    dither = rng.random(x.shape) - rng.random(x.shape)  # +/- 1 LSB
    q = np.rint(x * 32768 + dither)
    assert np.min(q) >= -32768 and np.max(q) <= 32767
    wavfile.write(path, fs, q.astype(np.int16))


def pan(x, position):
    """Mono -> stereo; -1 left, 0 centre, +1 right. Constant sum of squares."""
    theta = (np.asarray(position) + 1) * np.pi / 4
    return np.column_stack((x * np.cos(theta), x * np.sin(theta)))


def peaking_eq(fs, f0, q, gain_db):
    """RBJ peaking EQ, W3C Audio EQ Cookbook; a0 normalised to one."""
    a = 10 ** (gain_db / 40)
    w = 2 * np.pi * f0 / fs
    alpha = np.sin(w) / (2 * q)
    b = np.array([1 + alpha*a, -2*np.cos(w), 1-alpha*a])
    den = np.array([1 + alpha/a, -2*np.cos(w), 1-alpha/a])
    return b / den[0], den / den[0]


class Biquad:
    def __init__(self, b, a):
        self.b, self.a = b, a
        self.x1 = self.x2 = self.y1 = self.y2 = 0.

    def process(self, x):
        y = np.empty_like(x, dtype=float)
        b, a = self.b, self.a
        for n, v in enumerate(x):
            o = b[0]*v + b[1]*self.x1 + b[2]*self.x2 - a[1]*self.y1 - a[2]*self.y2
            y[n] = o
            self.x2, self.x1, self.y2, self.y1 = self.x1, v, self.y1, o
        return y


class Compressor:
    """Hard-knee, feed-forward, peak detector; one-pole smoothing in linear amplitude.
    Time constants are 63% step-response times, not universal plugin definitions.
    No lookahead or makeup gain. Mono only; a stereo design should link channels.
    """
    def __init__(self, fs=FS, threshold=-20, ratio=4, attack=.005, release=.12):
        self.threshold, self.ratio = threshold, ratio
        self.aa = np.exp(-1/(fs*attack))
        self.ar = np.exp(-1/(fs*release))
        self.env = 0.

    def process(self, x):
        y, trace = np.empty_like(x), np.empty_like(x)
        for n, v in enumerate(x):
            target = abs(v)
            a = self.aa if target > self.env else self.ar
            self.env = a*self.env + (1-a)*target
            level = 20*np.log10(max(self.env, 1e-12))
            gr = min(0., (self.threshold-level)*(1-1/self.ratio))
            trace[n] = gr
            y[n] = v * db_gain(gr)
        return y, trace


def delay(x, seconds=.25, feedback=.35, fs=FS, tail=2.):
    """y[n] = x[n] + feedback*y[n-D]; finite exported tail."""
    d = round(seconds*fs)
    if d < 1 or abs(feedback) >= 1:
        raise ValueError('Positive delay and |feedback| < 1 required.')
    y = np.pad(x, (0, round(tail*fs))).astype(float)
    # Each d-sample slice only depends on the preceding, already finished slice.
    for start in range(d, len(y), d):
        end = min(start+d, len(y))
        y[start:end] += feedback*y[start-d:end-d]
    return y


def convolution(x, h):
    """Linear mono-to-stereo convolution using a zero-padded NumPy FFT."""
    if h.ndim == 1:
        h = h[:, None]
    length = len(x) + len(h) - 1
    size = 1 << (length-1).bit_length()
    return np.fft.irfft(np.fft.rfft(x, size)[:, None] *
                       np.fft.rfft(h, size, axis=0), size, axis=0)[:length]


def room_ir():
    fs, h = read_wav(HERE / 'daw-room-ir.wav')
    g = math.gcd(fs, FS)
    h = signal.resample_poly(h, FS//g, fs//g, axis=0)
    if h.ndim == 1:
        h = np.column_stack((h, h))
    # Preserve the recording's onset/tail and stereo relation; choose an explicit
    # energy scaling for this artistic application, not physical SPL calibration.
    return h / np.sqrt(np.sum(h*h) / h.shape[1])


def stretch(x, factor, size=2048, hop=256):
    """Basic mono phase vocoder: factor > 1 lengthens without changing pitch.
    Interpolate magnitudes, unwrap phase residuals, advance at output hop.
    No transient phase locking / formant model / stereo coherence treatment.
    """
    pad = size//2
    xp = np.pad(x, (pad, size))
    win = np.hanning(size)
    starts = range(0, len(xp)-size+1, hop)
    frames = np.array([np.fft.rfft(xp[i:i+size]*win) for i in starts]).T
    steps = np.arange(0, frames.shape[1]-1, 1/factor)
    expected = 2*np.pi*hop*np.arange(size//2+1)/size
    phase = np.angle(frames[:, 0])
    out = np.zeros((len(steps)-1)*hop+size)
    weight = np.zeros_like(out)
    for j, pos in enumerate(steps):
        k, frac = int(pos), pos % 1
        mag = (1-frac)*abs(frames[:, k]) + frac*abs(frames[:, k+1])
        block = np.fft.irfft(mag*np.exp(1j*phase), size)*win
        out[j*hop:j*hop+size] += block
        weight[j*hop:j*hop+size] += win*win
        residual = np.angle(frames[:, k+1])-np.angle(frames[:, k])-expected
        residual -= 2*np.pi*np.round(residual/(2*np.pi))
        phase += expected + residual
    out /= np.maximum(weight, 1e-12)
    wanted = round(len(x)*factor)
    return np.pad(out[pad:pad+wanted], (0, max(0, wanted-len(out[pad:]))))


def pitch_shift(x, semitones):
    """Stretch by p, then resample to original length; basic demonstration."""
    from fractions import Fraction
    p = 2**(semitones/12)
    slow = stretch(x, p)
    ratio = Fraction(1/p).limit_denominator(10000)
    result = signal.resample_poly(slow, ratio.numerator, ratio.denominator)
    return np.pad(result[:len(x)], (0, max(0, len(x)-len(result))))


def synthesise():
    length = 8*FS
    melody, bass, drums = [np.zeros(length) for _ in range(3)]
    rng = np.random.default_rng(17)
    notes = [69, 72, 76, 72, 67, 71, 74, 71, 65, 69, 72, 69, 67, 71, 74, 76]
    for j, midi in enumerate(notes):
        t = np.arange(int(.9*FS))/FS
        f = 440 * 2**((midi-69)/12)
        note = sum(np.sin(2*np.pi*f*k*t)*np.exp(-t*(3+.6*k))/k
                   for k in range(1, 9))
        note *= (1-np.exp(-t/.002)) * (.55 if j%4 == 0 else .23)
        start = j*FS//2; count = min(len(note), length-start)
        melody[start:start+count] += note[:count]
    for j, midi in enumerate([45, 43, 41, 43]):
        t = np.arange(2*FS)/FS; f = 440*2**((midi-69)/12)
        env = (1-np.exp(-t/.012))*np.exp(-t*1.5)
        bass[j*2*FS:(j+1)*2*FS] = .30*env*(np.sin(2*np.pi*f*t)+.3*np.sin(4*np.pi*f*t))
    for j in range(16):
        t = np.arange(FS//3)/FS
        hit = .23*np.sin(2*np.pi*(55*t+45*.03*(1-np.exp(-t/.03))))*np.exp(-t*25)
        hit += .04*rng.normal(size=len(t))*np.exp(-t*70)
        drums[j*FS//2:j*FS//2+len(t)] += hit
    return melody, bass, drums


def pair(a, b, match_rms=False):
    """A, .6 s silence, B; one common gain, optional B RMS match first."""
    # Gentle comparison boundaries prevent the cut itself becoming the effect.
    a, b = a.copy(), b.copy()
    for v in (a, b):
        count = min(round(.005*FS), len(v)//2)
        ramp = np.linspace(0, 1, count).reshape((-1,)+(1,)*(v.ndim-1))
        v[:count] *= ramp
        v[-count:] *= ramp[::-1]
    if match_rms:
        b = b * rms(a)/max(rms(b), 1e-12)
    if a.ndim != b.ndim:
        a = np.column_stack((a, a))/np.sqrt(2)
    joined = np.concatenate((a, np.zeros((int(.6*FS),)+a.shape[1:]), b))
    return joined * min(1., .85/max(np.max(np.abs(joined)), 1e-12))


def save_svg(fig, path):
    import matplotlib.pyplot as plt
    fig.savefig(path, transparent=True, bbox_inches='tight', metadata={'Date': None})
    s = path.read_text()
    s = re.sub(r'<svg([^>]*?)width="[^"]+" height="[^"]+"', r'<svg\1width="100%"', s, count=1)
    path.write_text('\n'.join(line.rstrip() for line in s.splitlines())+'\n')
    plt.close(fig)


def figures(out, b, a, impulse, gr, source, compressed, h):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'svg.hashsalt':'vault', 'svg.fonttype':'none',
        'text.color':'#888888', 'axes.labelcolor':'#888888', 'axes.edgecolor':'#888888',
        'xtick.color':'#888888', 'ytick.color':'#888888', 'font.size':11,
        'axes.spines.top':False, 'axes.spines.right':False, 'legend.frameon':False})
    fig, ax = plt.subplots(figsize=(9, 3.4), layout='constrained')
    f = np.fft.rfftfreq(len(impulse), 1/FS)
    measured = 20*np.log10(np.maximum(abs(np.fft.rfft(impulse)), 1e-12))
    fw, response = signal.freqz(b, a, worN=8192, fs=FS)
    ax.semilogx(fw, 20*np.log10(abs(response)), color='#7c3aed', label='Coefficient prediction')
    picks = np.unique(np.geomspace(30, 20000, 34).astype(int))
    ax.scatter(picks, np.interp(picks, f, measured), color='#059669', s=16, label='FFT of computed impulse response')
    ax.set(xlim=(30,20000), ylim=(-10,1), xlabel='Frequency (Hz)', ylabel='Gain (dB)', title='A 1.2 kHz bell cut: −9 dB, Q = 0.8')
    ax.grid(alpha=.15, color='#888888'); ax.legend(loc='lower left')
    save_svg(fig, out/'daw-eq.svg')
    fig, axes = plt.subplots(1, 2, figsize=(10,3.5), layout='constrained')
    levels = np.linspace(-40,0,300)
    axes[0].plot(levels, levels, '--', color='#9ca3af', label='Unprocessed')
    axes[0].plot(levels, np.where(levels<=-20, levels, -20+(levels+20)/4), color='#7c3aed', label='4:1, threshold −20 dBFS')
    axes[0].set(xlabel='Steady detector level (dBFS)',ylabel='Output level (dBFS)',title='Static rule, after settling'); axes[0].legend(fontsize=9)
    t = np.arange(len(source))/FS
    axes[1].plot(t[::48], source[::48], color='#2563eb', alpha=.55, label='Input')
    axes[1].plot(t[::48], compressed[::48], color='#059669', label='Output')
    axes[1].set(xlim=(0,.45),xlabel='Time (s)',ylabel='Sample amplitude',title='Attack lets the initial peak through'); axes[1].legend(fontsize=9)
    for ax in axes: ax.grid(alpha=.15,color='#888888')
    save_svg(fig,out/'daw-compressor.svg')
    fig, axes = plt.subplots(1,2,figsize=(10,3.3),layout='constrained')
    t = np.arange(len(h))/FS
    axes[0].plot(t[::24],h[::24,0],color='#0891b2',lw=.6)
    axes[0].set(xlabel='Time since file start (s)',ylabel='Scaled amplitude',title='Recorded atrium: left impulse channel')
    freq = np.fft.rfftfreq(len(h),1/FS)
    mag = 20*np.log10(np.maximum(abs(np.fft.rfft(h[:,0])),1e-9))
    axes[1].semilogx(freq,mag,color='#7c3aed',lw=.6)
    axes[1].set(xlim=(40,20000),xlabel='Frequency (Hz)',ylabel='Magnitude (dB; arbitrary gain)',title='A room colours sound as well as extending it')
    for ax in axes: ax.grid(alpha=.15,color='#888888')
    save_svg(fig,out/'daw-room.svg')


def verify(b, a, h):
    rng = np.random.default_rng(8)
    x = rng.normal(size=13007)*.05
    y = Biquad(b,a).process(x)
    obj = Biquad(b,a)
    blocked = np.concatenate([obj.process(x[i:i+128]) for i in range(0,len(x),128)])
    assert np.max(abs(y-signal.lfilter(b,a,x))) < 1e-12
    assert np.array_equal(y, blocked)
    full, _ = Compressor().process(x)
    obj = Compressor()
    chunked = np.concatenate([obj.process(x[i:i+128])[0] for i in range(0,len(x),128)])
    assert np.array_equal(full, chunked)
    test = convolution(x[:1000],h[:300])
    assert np.max(abs(test[:,0]-np.convolve(x[:1000],h[:300,0]))) < 1e-12
    delta = np.zeros(100); delta[0]=1
    echo = delay(delta, .01, .5, fs=1000, tail=.1)
    assert np.allclose(echo[::10], .5**np.arange(len(echo[::10])))
    assert np.allclose(np.sum(pan(x,.37)**2,axis=1),x*x)
    t = np.arange(2*FS)/FS; tone = .2*np.sin(2*np.pi*440*t)
    slow = stretch(tone,1.5); shifted = pitch_shift(tone, 3)
    def dominant(v):
        v=v[FS//4:-FS//4]; spectrum=abs(np.fft.rfft(v*np.hanning(len(v))))
        return np.argmax(spectrum)*FS/len(v)
    fslow, fshift = dominant(slow), dominant(shifted)
    assert len(slow)==round(1.5*len(tone)) and abs(fslow-440)<1
    assert len(shifted)==len(tone) and abs(fshift-440*2**(.25))<1
    identity = stretch(tone,1)
    assert np.max(abs(identity[2048:-2048]-tone[2048:-2048]))<1e-8
    # 48 -> 16 kHz: 12 kHz must be rejected rather than folded to 4 kHz.
    high = np.sin(2*np.pi*12000*np.arange(FS)/FS)
    down = signal.resample_poly(high,1,3)
    attenuation=20*np.log10(rms(down[100:-100])/rms(high))
    assert attenuation < -55
    # Non-subtractive TPDF quantisation error: no DC bias over fractional inputs.
    means=[]
    for frac in [.05,.25,.5,.75,.95]:
        d=rng.random(200000)-rng.random(200000)
        means.append(float(np.mean(np.rint(frac+d)-frac)))
    assert max(abs(v) for v in means)<.006
    return {'block_state':'bit-identical for EQ and compressor',
            'eq_reference_max_error':float(np.max(abs(y-signal.lfilter(b,a,x)))),
            'phase_vocoder_hz':fslow,'pitch_shift_hz':fshift,
            'src_12k_rejection_db':float(attenuation),'tpdf_mean_error_lsb':means,
            'ir_samples_48k':len(h)}


def build(out):
    out.mkdir(parents=True,exist_ok=True)
    melody,bass,drums=synthesise()
    for name, x in [('keys',melody),('bass',bass),('drums',drums)]:
        write_wav(out/f'daw-stem-{name}.wav',x)
    b,a = peaking_eq(FS,1200,.8,-9)
    eq = Biquad(b,a).process(melody)
    comp, gr = Compressor().process(melody)
    h = room_ir()
    wet = convolution(melody[:2*FS], h)
    dry = np.pad(pan(melody[:2*FS],0),((0,len(wet)-2*FS),(0,0)))
    # Scale the wet return explicitly; this is an artistic send-level choice.
    wet *= .35*rms(dry)/rms(wet)
    write_wav(out/'daw-eq-ab.wav',pair(melody[:4*FS],eq[:4*FS],True))
    write_wav(out/'daw-compressor-ab.wav',pair(melody[:4*FS],comp[:4*FS],True))
    write_wav(out/'daw-delay-ab.wav',pair(melody[:2*FS],delay(melody[:2*FS])))
    write_wav(out/'daw-room-ab.wav',pair(dry,dry+wet))
    phrase = melody[:2*FS]
    write_wav(out/'daw-stretch-ab.wav',pair(phrase,stretch(phrase,1.5)))
    write_wav(out/'daw-pitch-ab.wav',pair(phrase,pitch_shift(phrase,3)))
    impulse=np.zeros(65536);impulse[0]=1
    figures(out,b,a,Biquad(b,a).process(impulse),gr,melody,comp,h)
    result=verify(b,a,h)
    result['audio']={}
    for p in sorted(out.glob('daw-*.wav')):
        fs,x=read_wav(p)
        result['audio'][p.name]={'fs':fs,'seconds':len(x)/fs,'channels':1 if x.ndim==1 else x.shape[1],
             'peak':float(np.max(abs(x))),'rms':float(rms(x))}
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path,default=HERE)
    build(parser.parse_args().out)
