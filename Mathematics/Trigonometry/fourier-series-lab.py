"""Fourier-series experiments. Run with --audio to regenerate the embedded WAVs.
Finite sums are evaluated directly; the FFT is used only as an independent check.
"""
from pathlib import Path
import argparse,json,wave
import numpy as np
from scipy.integrate import quad
from scipy.special import sici
ROOT=Path(__file__).resolve().parent
STAGES=(1,3,5,7,9,15,31)
RATE=48000
F0=220

def square_sum(theta, highest):
    theta=np.asarray(theta,dtype=float)
    return sum((4/np.pi/n)*np.sin(n*theta) for n in range(1,highest+1,2))

def triangle_sum(theta, highest):
    theta=np.asarray(theta,dtype=float)
    return sum((8/np.pi**2)*(-1)**((n-1)//2)*np.sin(n*theta)/n**2
               for n in range(1,highest+1,2))

def coefficients(f, period, highest, count=65536):
    t=(np.arange(count)+.5)*period/count-period/2
    y=f(t); a=np.zeros(highest+1);b=np.zeros(highest+1)
    a[0]=2*np.mean(y)
    for n in range(1,highest+1):
        a[n]=2*np.mean(y*np.cos(2*np.pi*n*t/period))
        b[n]=2*np.mean(y*np.sin(2*np.pi*n*t/period))
    return a,b

def verify():
    theta=(np.arange(262144)+.5)*2*np.pi/262144-np.pi
    basis=np.array([np.ones_like(theta)]+[f(n*theta) for n in range(1,5) for f in (np.cos,np.sin)])
    gram=basis@basis.T/len(theta)
    np.testing.assert_allclose(gram,np.diag([1]+[.5]*8),atol=2e-14)
    for n in range(1,21):
        # Independent adaptive integration on each side of the discontinuity.
        b=(quad(lambda x:-np.sin(n*x),-np.pi,0)[0]+quad(lambda x:np.sin(n*x),0,np.pi)[0])/np.pi
        assert abs(b-(4/(np.pi*n) if n%2 else 0))<1e-12
    errors=[]
    for N in (1,3,7,15,31,63):
        y=square_sum(theta,N);target=np.sign(theta)
        predicted=1-(8/np.pi**2)*sum(1/n**2 for n in range(1,N+1,2))
        measured=np.mean((target-y)**2)
        assert abs(measured-predicted)<2e-8
        errors.append(measured)
    assert all(a>b for a,b in zip(errors,errors[1:]))
    # Period changes must not change coefficient amplitudes.
    for T in (.4,2*np.pi,7):
        a,b=coefficients(lambda t:.4+.7*np.cos(4*np.pi*t/T)-.2*np.sin(6*np.pi*t/T),T,7)
        want_a=np.zeros(8);want_a[0]=.8;want_a[2]=.7
        want_b=np.zeros(8);want_b[3]=-.2
        np.testing.assert_allclose(a,want_a,atol=1e-13);np.testing.assert_allclose(b,want_b,atol=1e-13)
    # Least-squares minimality, tested against changed coefficients.
    base=square_sum(theta,7);truth=np.sign(theta)
    rng=np.random.default_rng(20260920)
    for _ in range(20):
        delta=rng.normal(size=8)
        perturb=sum(delta[n-1]*np.sin(n*theta) for n in range(1,9))
        actual=np.mean((truth-base-perturb)**2)-np.mean((truth-base)**2)
        assert abs(actual-.5*np.dot(delta,delta))<1e-8
    peak=float(square_sum(np.pi/256,255));limit=2/np.pi*sici(np.pi)[0]
    assert abs(peak-limit)<6e-6
    # Triangle: continuity improves coefficient decay; independent projection.
    a,b=coefficients(lambda t:2/np.pi*np.arcsin(np.sin(t)),2*np.pi,15)
    for n in range(1,16):
        want=8/np.pi**2*(-1)**((n-1)//2)/n**2 if n%2 else 0
        assert abs(b[n]-want)<2e-9
    # Independent finite differences verify the heat PDE, including its sign.
    x=np.linspace(.1,.9,81);kappa=.2;t=.3;h=1e-4
    for n in (1,2,5):
        def mode(x,t):return np.sin(n*np.pi*x)*np.exp(-kappa*(n*np.pi)**2*t)
        dt=(mode(x,t+h)-mode(x,t-h))/(2*h)
        dxx=(mode(x+h,t)-2*mode(x,t)+mode(x-h,t))/h**2
        np.testing.assert_allclose(dt,kappa*dxx,atol=1e-7,rtol=1e-5)
    # A Fejer mean stays in the square wave's range; compare two constructions.
    N=31;grid=theta[::16]
    averaged=sum(square_sum(grid,k) if k else np.zeros_like(grid) for k in range(N+1))/(N+1)
    tapered=sum((1-n/(N+1))*4/(np.pi*n)*np.sin(n*grid) for n in range(1,N+1,2))
    np.testing.assert_allclose(averaged,tapered,atol=2e-15)
    assert max(abs(tapered))<=1
    # Cubic distortion: project the nonlinear output independently.
    a,b=coefficients(lambda t:np.sin(t)-.4*np.sin(t)**3,2*np.pi,9)
    expected=np.zeros(10);expected[1]=.7;expected[3]=.1
    np.testing.assert_allclose(b,expected,atol=1e-14)
    np.testing.assert_allclose(a,0,atol=1e-14)
    report={'orthogonality_max_error':float(np.max(np.abs(gram-np.diag([1]+[.5]*8)))),
            'square_mse_N_1_3_7_15_31_63':errors,'gibbs_peak_N255':peak,
            'gibbs_limit':float(limit),'overshoot_fraction_of_jump':float((limit-1)/2)}
    print(json.dumps(report,indent=2));print('PASS: integrals, normalization, changed periods, projection, Parseval, Gibbs, triangle and heat modes.')
    return report

def write_wav(path,y):
    assert np.max(np.abs(y))<.95
    pcm=np.rint(y*32767).astype('<i2')
    with wave.open(str(path),'wb') as w:
        w.setnchannels(1);w.setsampwidth(2);w.setframerate(RATE);w.writeframes(pcm.tobytes())
    with wave.open(str(path),'rb') as w:
        assert w.getframerate()==RATE and w.getnframes()==len(y)
        recovered=np.frombuffer(w.readframes(w.getnframes()),dtype='<i2')/32767
        assert np.max(abs(y-recovered))<=.51/32767

def audio():
    samples=3*RATE;t=np.arange(samples)/RATE;theta=2*np.pi*F0*t
    ramp=int(.02*RATE);env=np.ones(samples)
    env[:ramp]=np.sin(np.linspace(0,np.pi/2,ramp))**2;env[-ramp:]=env[:ramp][::-1]
    ladder=[];stats=[]
    for N in STAGES:
        assert N*F0<RATE/2
        y=square_sum(theta,N)
        # Equal steady-state RMS, not equal perceived loudness.
        y*=.12/np.sqrt(np.mean(y*y))
        assert abs(np.sqrt(np.mean(y*y))-.12)<1e-12
        spectrum=np.fft.rfft(y)/samples
        for n in range(1,N+1):
            magnitude=2*abs(spectrum[n*F0*3])
            if n%2:assert abs(magnitude/(2*abs(spectrum[F0*3]))-1/n)<1e-12
            else:assert magnitude<1e-12
        y*=env;write_wav(ROOT/f'fourier-series-h{N:02d}.wav',y)
        ladder += [y,np.zeros(RATE//2)]
        stats.append({'highest_harmonic':N,'highest_frequency_Hz':N*F0,'peak':float(max(abs(y)))})
    write_wav(ROOT/'fourier-series-listening-ladder.wav',np.concatenate(ladder))
    print(json.dumps(stats,indent=2));print('PASS: WAV readback, no clipping, equal unfaded RMS, harmonic ratios, Nyquist bound.')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--audio',action='store_true');args=parser.parse_args()
    verify()
    if args.audio:audio()
