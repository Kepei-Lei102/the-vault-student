"""Fourier lab: explicit DFT/FFT, finite-window STFT, echo and independent checks.
Requires numpy/scipy. Run --audio to regenerate PCM16 WAVs; --bench for timings.
Signals are synthetic, with fixed gain (not separately loudness-normalised).
"""
from pathlib import Path
import argparse, json, time, platform
import numpy as np
from scipy.integrate import quad
from scipy.io import wavfile
ROOT = Path(__file__).resolve().parent
FS = 8000

def dft(x):
    x = np.asarray(x, dtype=complex)
    if x.ndim != 1 or len(x) == 0:
        raise ValueError('expected a nonempty one-dimensional vector')
    n = np.arange(len(x))
    return np.exp(-2j*np.pi*np.outer(n,n)/len(x)) @ x

def fft_radix2(x):
    x = np.asarray(x, dtype=complex)
    if x.ndim != 1 or len(x) == 0 or len(x) & (len(x)-1):
        raise ValueError('length must be a positive power of two')
    if len(x) == 1:
        return x.copy()
    E, O = fft_radix2(x[::2]), fft_radix2(x[1::2])
    t = np.exp(-2j*np.pi*np.arange(len(x)//2)/len(x)) * O
    return np.concatenate((E+t, E-t))

def fft_convolve(x, h):
    L = len(x) + len(h) - 1
    nfft = 1 << (L-1).bit_length()
    y = np.fft.ifft(np.fft.fft(x,nfft) * np.fft.fft(h,nfft))[:L]
    return np.real_if_close(y)

def analysis(x, M=512, hop=128):
    """Full-window complex STFT, with zero padding at both signal boundaries."""
    if not 0 < hop <= M//2:
        raise ValueError('this demonstration uses overlapping Hann frames')
    w = np.hanning(M)
    z = np.pad(x,(M,M))
    starts = np.arange(0,len(z)-M+1,hop)
    frames = np.array([np.fft.rfft(z[s:s+M]*w) for s in starts])
    centers = (starts + (M-1)/2 - M)/FS
    return centers, frames, starts, w, len(z)

def synthesis(frames, starts, w, padded_length, original_length):
    M = len(w); y = np.zeros(padded_length); weight = np.zeros(padded_length)
    for S,s in zip(frames,starts):
        y[s:s+M] += np.fft.irfft(S,n=M)*w
        weight[s:s+M] += w*w
    keep = slice(M,M+original_length)
    if np.any(weight[keep] <= 1e-12):
        raise ValueError('uncovered output samples')
    return y[keep]/weight[keep]

def demo_signal():
    t = np.arange(4*FS)/FS
    # Integrate frequency analytically to keep phase continuous at both joins.
    u = np.clip(t-1.5,0,1)
    cycles = 220*t + 110*u*u + 220*np.maximum(t-2.5,0)
    freq = 220 + 220*u
    fade = np.minimum(1,np.minimum(t/.025,(t[-1]-t)/.025))
    return t, .32*np.sin(2*np.pi*cycles)*fade, freq

def echo_signal():
    # Three plucks: additive tones below Nyquist, shaped by an attack/decay envelope.
    t = np.arange(3*FS)/FS; x = np.zeros(len(t))
    for onset, f in [(0.15,330),(1.1,440),(2.05,550)]:
        u=t-onset; mask=(u>=0)&(u<.55); z=u[mask]
        env=(1-np.exp(-z/.004))*np.exp(-z/.09)
        x[mask] += .32*env*(np.sin(2*np.pi*f*z)+.3*np.sin(4*np.pi*f*z))
    h=np.zeros(int(.72*FS)+1);h[0]=1;h[int(.24*FS)]=.55;h[int(.48*FS)]=.30;h[int(.72*FS)]=.16
    return x,h,fft_convolve(x,h)

def write_audio():
    _,changing,_=demo_signal(); x,h,y=echo_signal()
    signals={'changing-tone':changing,'dry':x,'echo':y}
    report={}
    for name,a in signals.items():
        assert np.max(np.abs(a))<.95
        p=ROOT/f'fourier-transform-{name}.wav'
        pcm=np.rint(a*32767).astype(np.int16);wavfile.write(p,FS,pcm)
        sr,r=wavfile.read(p);assert sr==FS
        assert np.max(abs(r.astype(float)/32767-a))<=.500001/32767
        report[name]={'seconds':len(a)/FS,'peak':float(np.max(abs(a))),'rms':float(np.sqrt(np.mean(a*a)))}
    return report

def checks():
    rng=np.random.default_rng(20260920); report={}
    errors=[]
    for N in (1,2,4,8,16,32,64,128):
        x=rng.normal(size=N)+1j*rng.normal(size=N)
        X=dft(x);Y=fft_radix2(x)
        errors.append(float(np.max(abs(X-Y))))
        np.testing.assert_allclose(Y,np.fft.fft(x),atol=2e-12)
        np.testing.assert_allclose(np.fft.ifft(Y),x,atol=2e-12)
        np.testing.assert_allclose(np.sum(abs(x)**2),np.sum(abs(Y)**2)/N,rtol=1e-12)
    for N in (3,5,7,11):
        x=rng.normal(size=N);np.testing.assert_allclose(dft(x),np.fft.fft(x),atol=2e-12)
        try:fft_radix2(x)
        except ValueError:pass
        else:raise AssertionError('radix2 accepted invalid length')
    report['max_dft_fft_disagreement']=max(errors)
    x=np.array([1.,0.,-1.,0.]);np.testing.assert_allclose(dft(x),[0,2,0,2],atol=1e-14)
    # Finite rectangular pulse: independent real/imaginary quadrature.
    pulse=[]
    for tau in (.1,.7,2.):
        for f in (0,.3,2.5,7):
            integral=quad(lambda t:np.cos(2*np.pi*f*t),-tau/2,tau/2,epsabs=1e-12)[0]
            expected=tau*np.sinc(f*tau);pulse.append(abs(integral-expected))
    report['pulse_quadrature_error']=max(pulse)
    N=64;k=7;n=np.arange(N);A=.8;phi=.43
    X=dft(A*np.cos(2*np.pi*k*n/N+phi));np.testing.assert_allclose(2*X[k]/N,A*np.exp(1j*phi),atol=2e-14)
    np.testing.assert_allclose(dft(np.roll(x,1)),dft(x)*np.exp(-2j*np.pi*np.arange(4)/4),atol=2e-14)
    # Aliased tones produce identical *samples* before any FFT is attempted.
    t=np.arange(400)/FS; np.testing.assert_allclose(np.cos(2*np.pi*5000*t),np.cos(2*np.pi*3000*t),atol=4e-13)
    # Zero padding resamples the same finite-record DTFT; original bins are retained.
    z=rng.normal(size=32);np.testing.assert_allclose(np.fft.fft(z,128)[::4],np.fft.fft(z),atol=1e-13)
    x=np.array([1.,2.,3.]);h=np.array([1.,.5])
    np.testing.assert_allclose(fft_convolve(x,h),[1,2.5,4,1.5],atol=1e-14)
    circ=np.fft.ifft(np.fft.fft(x,3)*np.fft.fft(h,3)).real
    np.testing.assert_allclose(circ,[2.5,2.5,4],atol=1e-14)
    for a,b in [(3,7),(31,17),(128,65)]:
        x=rng.normal(size=a);h=rng.normal(size=b)
        np.testing.assert_allclose(fft_convolve(x,h),np.convolve(x,h),atol=2e-13)
    _,x,_=demo_signal();tt,S,starts,w,L=analysis(x)
    recovered=synthesis(S,starts,w,L,len(x));report['stft_reconstruction_max_error']=float(max(abs(x-recovered)))
    assert report['stft_reconstruction_max_error']<3e-15
    freq=np.fft.rfftfreq(len(w),1/FS)
    for center,target in [(.6,220),(3.2,440)]:
        row=np.argmin(abs(tt-center));peak=freq[np.argmax(abs(S[row]))];assert abs(peak-target)<=FS/len(w)
    dry,h,wet=echo_signal();manual=np.zeros(len(wet))
    for d in np.flatnonzero(h):manual[d:d+len(dry)]+=h[d]*dry
    report['echo_vs_delayed_copies_error']=float(max(abs(wet-manual)));assert report['echo_vs_delayed_copies_error']<1e-14
    # Deliberately lose phase: it must not reconstruct the changing recording.
    bad=np.fft.irfft(abs(np.fft.rfft(dry)),n=len(dry));assert np.linalg.norm(dry-bad)>.1
    return report

def benchmark():
    rng=np.random.default_rng(4);rows=[]
    for N in (128,256,512,1024):
        x=rng.normal(size=N);row={'N':N,'direct_terms':N*N,'radix2_butterflies':N//2*int(np.log2(N))}
        for label,fn in [('direct_ms',dft),('radix2_ms',fft_radix2),('numpy_ms',np.fft.fft)]:
            fn(x);times=[]
            for _ in range(5):
                t=time.perf_counter();fn(x);times.append((time.perf_counter()-t)*1000)
            row[label]=float(np.median(times))
        rows.append(row)
    return {'environment':platform.platform(),'python':platform.python_version(),'numpy':np.__version__,'rows':rows}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--audio',action='store_true');p.add_argument('--bench',action='store_true');a=p.parse_args()
    out={'checks':checks()}
    if a.audio:out['audio']=write_audio()
    if a.bench:out['benchmark']=benchmark()
    print(json.dumps(out,indent=2))
