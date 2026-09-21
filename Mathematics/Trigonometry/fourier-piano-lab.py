"""A4 additive-synthesis teaching model, NOT a fitted acoustic-piano model.
Run with --build for PCM16 audio + deterministic SVG. Requires numpy/scipy/matplotlib.
All oscillators, weights and envelopes are explicit; no samples or soundfont.
"""
from pathlib import Path
import argparse,json,re
import numpy as np
from scipy.io import wavfile
ROOT=Path(__file__).resolve().parent
FS=48000;F0=440.;GAIN=.24
N=np.arange(1,13)
A=np.array([1,.65,.42,.24,.16,.10,.07,.05,.035,.025,.018,.012])
TAU=2.8/(1+.18*(N-1)**1.4)
CENTS=np.array([-1.2,0,1.2]);UNISON=np.array([.25,.5,.25]);B=.00015
STAGES=[('sine',1,False,False,3),('four',4,False,False,3),('twelve',12,False,False,3),('struck',12,True,False,5),('piano',12,True,True,5)]

def envelope(t):
    t=np.asarray(t);u=t[:,None]
    return (1-np.exp(-u/.003))*(.65*np.exp(-u/(.18*TAU))+.35*np.exp(-u/TAU))

def partials(t,count=12,struck=False,strings=False):
    t=np.asarray(t);freq=N[:count]*F0
    if strings:
        freq=freq*np.sqrt((1+B*N[:count]**2)/(1+B))
        oscillators=np.sin(2*np.pi*t[:,None,None]*freq[None,:,None]*2**(CENTS[None,None,:]/1200))
        carriers=oscillators@UNISON
    else:carriers=np.sin(2*np.pi*t[:,None]*freq)
    return GAIN*A[:count]*carriers*(envelope(t)[:,:count] if struck else 1)

def signal(count,struck,strings,seconds):
    t=np.arange(round(FS*seconds))/FS;x=partials(t,count,struck,strings).sum(axis=1)
    # Playback fades, separate from the struck-note envelope. No sharp file edges.
    edge=np.minimum(1,(t[-1]-t)/.08)
    if not struck:edge*=np.minimum(1,t/.015)
    return t,x*np.maximum(edge,0)

def build_audio():
    pieces=[];report={}
    for key,count,struck,strings,seconds in STAGES:
        t,x=signal(count,struck,strings,seconds)
        assert abs(x).max()<.95
        pcm=np.rint(x*32767).astype(np.int16);path=ROOT/f'fourier-piano-{key}.wav';wavfile.write(path,FS,pcm)
        sr,y=wavfile.read(path);assert sr==FS and len(y)==round(FS*seconds)
        assert np.max(abs(y.astype(float)/32767-x))<=.500001/32767
        report[key]={'seconds':seconds,'peak':float(abs(x).max()),'rms':float(np.sqrt(np.mean(x*x)))}
        pieces.append(pcm)
    gap=np.zeros(round(.65*FS),dtype=np.int16)
    ladder=np.concatenate([z for i,p in enumerate(pieces) for z in ([gap,p] if i else [p])]);wavfile.write(ROOT/'fourier-piano-ladder.wav',FS,ladder)
    report['ladder_seconds']=len(ladder)/FS;return report

def checks():
    t=np.arange(FS)/FS;x=partials(t).sum(axis=1);spectrum=2*abs(np.fft.rfft(x))/FS
    recovered=spectrum[(N*F0).astype(int)];err=float(max(abs(recovered-GAIN*A)))
    assert err<1e-12
    # Independently sum each oscillator; do not use the vectorised oscillator bank.
    t=np.arange(0,.19,1/FS);answer=np.zeros_like(t)
    for n,a,tau in zip(N,A,TAU):
        f=n*F0*np.sqrt((1+B*n*n)/(1+B))
        e=(1-np.exp(-t/.003))*(.65*np.exp(-t/(.18*tau))+.35*np.exp(-t/tau))
        for cents,w in zip(CENTS,UNISON):answer+=GAIN*a*w*e*np.sin(2*np.pi*f*2**(cents/1200)*t)
    err2=float(max(abs(answer-partials(t,strings=True,struck=True).sum(axis=1))));assert err2<1e-12
    assert np.all(np.diff(TAU)<0)
    assert N[-1]*F0*np.sqrt((1+B*N[-1]**2)/(1+B))*2**(max(CENTS)/1200)<FS/2
    early=envelope(np.array([.05]))[0];late=envelope(np.array([2.]))[0]
    assert late[-1]/late[0]<early[-1]/early[0]
    return {'fft_amplitude_max_error':err,'independent_sum_max_error':err2,'highest_carrier_Hz':float(N[-1]*F0*np.sqrt((1+B*N[-1]**2)/(1+B))*2**(max(CENTS)/1200))}

def figure():
    import matplotlib;matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'svg.hashsalt':'vault','svg.fonttype':'none','font.size':11,'font.family':'DejaVu Sans','text.color':'#888888','axes.labelcolor':'#888888','axes.edgecolor':'#888888','xtick.color':'#888888','ytick.color':'#888888','axes.titlecolor':'#888888'})
    fig,ax=plt.subplots(2,2,figsize=(11,7.8));blue='#4678c8';pink='#cc0066';green='#059669'
    t=np.linspace(0,2/F0,1400);p=partials(t)
    for n,c in zip([0,1,2],[blue,pink,green]):ax[0,0].plot(t*1000,p[:,n],color=c,label=f'{N[n]*440} Hz × {A[n]:g}',lw=1.5)
    ax[0,0].plot(t*1000,p[:,:3].sum(axis=1),color='#c86432',lw=2,label='sum of these three')
    ax[0,0].set(title='Add at the SAME instant',xlabel='time / ms',ylabel='sample amplitude')
    for count,c in [(1,blue),(4,green),(12,pink)]:ax[0,1].plot(t*1000,p[:,:count].sum(axis=1),color=c,label=f'{count} harmonic'+('s' if count!=1 else ''),lw=1.4)
    ax[0,1].set(title='Same A4 pitch; different repeating shape',xlabel='time / ms',ylabel='sample amplitude')
    sec=np.linspace(0,4,600)
    for n,c in zip([0,3,11],[blue,green,pink]):ax[1,0].plot(sec,envelope(sec)[:,n],color=c,label=f'harmonic {n+1}')
    ax[1,0].set(title='Then give the partials different decays',xlabel='time since strike / s',ylabel='envelope multiplier',ylim=(0,1))
    for n,offset,c,label in [(0,-.17,blue,'steady recipe'),(1,.17,pink,'after 1 s (struck)')]:
        heights=GAIN*A if n==0 else GAIN*A*envelope(np.array([1.]))[0]
        ax[1,1].bar(N+offset,heights,width=.34,color=c,alpha=.85,label=label)
    ax[1,1].set(title='High partials fade faster in this model',xlabel='harmonic number n (frequency = n × 440 Hz)',ylabel='sinusoid amplitude',xticks=[1,2,4,6,8,10,12])
    for a in ax.flat:
        a.set_facecolor('none');a.spines[['top','right']].set_visible(False);a.grid(color='#888888',alpha=.15);a.legend(framealpha=0,labelcolor='#888888',fontsize=9)
    fig.tight_layout(pad=1.6);path=ROOT/'fourier-piano-addition.svg';fig.savefig(path,transparent=True,metadata={'Date':None})
    s=path.read_text();s=re.sub(r'(<svg\b[^>]*?)width="[^"]+"',r'\1width="100%"',s,count=1);s=re.sub(r'(<svg\b[^>]*?)height="[^"]+"',r'\1',s,count=1);path.write_text(s);plt.close(fig)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--build',action='store_true');args=parser.parse_args();report={'checks':checks()}
    if args.build:report['audio']=build_audio();figure()
    print(json.dumps(report,indent=2))
