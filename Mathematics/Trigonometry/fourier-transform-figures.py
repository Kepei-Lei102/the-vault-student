"""Deterministic matplotlib SVGs. Figures are mathematical plots, not generated art."""
from pathlib import Path
import importlib.util, re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('lab',ROOT/'fourier-transform-lab.py');lab=importlib.util.module_from_spec(spec);spec.loader.exec_module(lab)
plt.rcParams.update({'svg.hashsalt':'vault','font.size':12,'text.color':'#888888','axes.labelcolor':'#888888','axes.edgecolor':'#888888','xtick.color':'#888888','ytick.color':'#888888','axes.titlecolor':'#888888','svg.fonttype':'none','font.family':'DejaVu Sans'})
P='#cc0066';B='#4678c8';O='#c86432';G='#888888'
def finish(fig,name):
    for ax in fig.axes:
        ax.set_facecolor('none');ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.15,color=G)
        if ax.get_legend_handles_labels()[0]:ax.legend(framealpha=0,labelcolor=G,fontsize=10)
    fig.tight_layout(pad=1.7)
    p=ROOT/f'fourier-transform-{name}.svg';fig.savefig(p,transparent=True,metadata={'Date':None})
    s=p.read_text();s=re.sub(r'(<svg\b[^>]*?)width="[^"]+"',r'\1width="100%"',s,count=1);s=re.sub(r'(<svg\b[^>]*?)height="[^"]+"',r'\1',s,count=1);p.write_text(s)
    qa=Path('/tmp/fourier-transform-build');qa.mkdir(exist_ok=True)
    for theme,c in [('light','white'),('dark','#1e1e1e')]:fig.savefig(qa/f'{name}-{theme}.png',facecolor=c,dpi=120)
    plt.close(fig)

def pulse():
    fig,ax=plt.subplots(1,2,figsize=(11,4.2))
    for tau,c in [(1,B),(.5,P)]:
        ax[0].plot([-1.5,-tau/2,-tau/2,tau/2,tau/2,1.5],[0,0,1,1,0,0],color=c,lw=2,label=f'duration {tau:g} s')
        f=np.linspace(-6,6,1401);ax[1].plot(f,tau*np.sinc(f*tau),color=c,lw=2,label=f'duration {tau:g} s')
    ax[0].set(title='One pulse; no periodic repetition',xlabel='time / s',ylabel='signal amplitude',ylim=(-.12,1.4))
    ax[1].set(title='Narrower in time, broader in frequency',xlabel='frequency / Hz',ylabel='real X(f) / amplitude·s',ylim=(-.3,1.3))
    finish(fig,'pulse')

def probes():
    fig,ax=plt.subplots(1,2,figsize=(11,4.8))
    for a,k in zip(ax,[2,3]):
        terms=np.exp(2j*np.pi*(3-k)*np.arange(8)/8);points=np.r_[0,np.cumsum(terms)]
        for n in range(8):
            z0,z1=points[n:n+2];a.annotate('',(z1.real,z1.imag),(z0.real,z0.imag),arrowprops={'arrowstyle':'->','color':B if k==2 else P,'lw':2})
        a.scatter(points[0].real,points[0].imag,s=50,color=O,zorder=4,label='start')
        end=points[-1];a.scatter(end.real,end.imag,marker='x',s=80,color=P,zorder=5,label='sum')
        a.set(xlabel='real part',ylabel='imaginary part',title=f'Probe k = {k}: sum = {0 if k==2 else 8}')
        a.set_aspect('equal');a.axhline(0,color=G,lw=.7);a.axvline(0,color=G,lw=.7)
    ax[0].set(xlim=(-1.5,2.5),ylim=(-.7,3.3));ax[1].set(xlim=(-.7,8.7),ylim=(-2.6,2.6))
    finish(fig,'probes')

def windows():
    fig,ax=plt.subplots(2,2,figsize=(11,8.6));fs=64;N=64;t=np.arange(N)/fs;x=np.cos(2*np.pi*8.5*t);w=np.hanning(N)
    ax[0,0].plot(t,x,color=B,lw=1.5,label='rectangular: original samples');ax[0,0].plot(t,x*w,color=P,lw=1.5,label='Hann: tapered samples')
    ax[0,0].set(title='Same 8.5-cycle record',xlabel='time / s',ylabel='amplitude',ylim=(-1.4,1.4))
    f=np.fft.rfftfreq(16384,1/fs)
    for win,c,label in [(np.ones(N),B,'rectangular'),(w,P,'Hann')]:
        a=abs(np.fft.rfft(x*win,16384))/sum(win)*2
        ax[0,1].plot(f,20*np.log10(np.maximum(a,1e-5)),color=c,label=label,lw=1.6)
    ax[0,1].set(title='Lower sidelobes; a wider main lobe',xlabel='frequency / Hz',ylabel='dB relative to unit amplitude',xlim=(0,18),ylim=(-70,4))
    f64=np.fft.rfftfreq(N,1/fs);a64=abs(np.fft.rfft(x))*2/N
    ax[1,0].plot(f64,a64,'o',color=B,label='64-point FFT: 1 Hz grid')
    f512=np.fft.rfftfreq(512,1/fs);ax[1,0].plot(f512,abs(np.fft.rfft(x,512))*2/N,color=P,label='512-point FFT: 0.125 Hz grid')
    ax[1,0].set(title='Zero padding: same observed 1 second',xlabel='frequency / Hz',ylabel='amplitude estimate',xlim=(5,12),ylim=(0,1.18))
    for size,c in [(64,B),(256,P)]:
        t=(np.arange(size)-size/2)/fs;y=np.cos(2*np.pi*8*t)+np.cos(2*np.pi*8.75*t)
        ax[1,1].plot(f,abs(np.fft.rfft(y,16384))*2/size,color=c,label=f'{size/fs:g} s actually observed')
    ax[1,1].set(title='Two tones: 8 Hz and 8.75 Hz',xlabel='frequency / Hz',ylabel='amplitude estimate',xlim=(6,11),ylim=(0,2.1))
    finish(fig,'windows')

def spectrogram():
    _,x,_=lab.demo_signal();fig,axes=plt.subplots(2,1,figsize=(10.8,7.2))
    for a,M in zip(axes,[256,1024]):
        tt,S,_,w,_=lab.analysis(x,M,M//4);f=np.fft.rfftfreq(M,1/lab.FS)
        power=abs(S)**2;dB=10*np.log10(np.maximum(power/power.max(),1e-8))
        im=a.pcolormesh(tt,f,dB.T,cmap='viridis',vmin=-60,vmax=0,shading='auto',rasterized=True)
        a.set(xlim=(0,4),ylim=(100,600),xlabel='time / s',ylabel='frequency / Hz',title=f'Hann window {M/lab.FS*1000:g} ms; hop {M/4/lab.FS*1000:g} ms')
        cb=fig.colorbar(im,ax=a,pad=.025);cb.set_label('dB relative to plot maximum');cb.ax.tick_params(colors=G);cb.outline.set_edgecolor(G)
    finish(fig,'spectrogram')

if __name__=='__main__':pulse();probes();windows();spectrogram()
