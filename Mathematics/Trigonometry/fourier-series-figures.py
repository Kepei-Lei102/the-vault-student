"""Stack: matplotlib SVG. Transparent, deterministic, at most two panels across."""
from pathlib import Path
import importlib.util,re,os
os.environ.setdefault('MPLCONFIGDIR','/tmp/fourier-build/mpl')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('lab',ROOT/'fourier-series-lab.py');lab=importlib.util.module_from_spec(spec);spec.loader.exec_module(lab)
GREY='#888888';BLUE='#4678c8';PINK='#cc0066';ORANGE='#c86432';GREEN='#059669'
plt.rcParams.update({'svg.hashsalt':'vault-fourier-series','svg.fonttype':'none','font.size':13,'text.color':GREY,'axes.labelcolor':GREY,'xtick.color':GREY,'ytick.color':GREY,'axes.edgecolor':GREY,'axes.titlecolor':GREY,'figure.facecolor':'none','axes.facecolor':'none'})
def style(ax):
 ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.14,color=GREY);ax.axhline(0,color=GREY,lw=.7)
def save(fig,name):
 fig.savefig(ROOT/name,transparent=True,bbox_inches='tight',metadata={'Date':None})
 p=ROOT/name;s=p.read_text();s=re.sub(r'<svg[^>]*>',lambda m:re.sub(r' height="[^"]*"','',re.sub(r'width="[^"]*"','width="100%"',m[0])),s,count=1);p.write_text(s);plt.close(fig)
theta=np.linspace(-np.pi,np.pi,2401)
fig,axes=plt.subplots(3,2,figsize=(11,9.4),gridspec_kw={'width_ratios':[1.35,1]});fig.subplots_adjust(hspace=.64,wspace=.3)
for row,N in enumerate((1,9,31)):
 ax,bx=axes[row];style(ax);style(bx)
 ax.plot(theta,np.sign(theta),color=GREY,ls='--',lw=1.2,label='target ±1')
 ax.plot(theta,lab.square_sum(theta,N),color=PINK,lw=1.8,label='finite sum')
 ax.set(xlim=(-np.pi,np.pi),ylim=(-1.5,1.5),title=f'Highest harmonic N = {N}',xlabel='phase θ (radians)');ax.set_xticks([-np.pi,0,np.pi],['−π','0','π']);ax.legend(fontsize=10,frameon=False,labelcolor=GREY,loc='upper left')
 ns=np.arange(1,N+1,2);bx.bar(ns,4/np.pi/ns,width=.65,color=BLUE,alpha=.85);bx.set(xlim=(0,32),ylim=(0,1.42),title='Sine coefficients $b_n$',xlabel='harmonic number n');bx.set_xticks([1,9,17,25,31]);bx.set_yticks([0,.5,1])
fig.suptitle('One waveform, two descriptions: shape and harmonic weights',fontsize=17,y=1.01)
save(fig,'fourier-series-harmonics.svg')
fig=plt.figure(figsize=(11,7.8));gs=fig.add_gridspec(2,2,hspace=.58,wspace=.28);top=fig.add_subplot(gs[0,:]);style(top)
f=np.sin(theta)+.5*np.sin(3*theta);top.plot(theta,f,color=PINK,lw=2);top.set(title='A mixture: f(θ) = sin θ + 0.5 sin 3θ',xlabel='θ');top.set_xticks([-np.pi,0,np.pi],['−π','0','π'])
for j,n in enumerate((1,2)):
 ax=fig.add_subplot(gs[1,j]);style(ax);y=f*np.sin(n*theta)
 ax.plot(theta,y,color=BLUE,lw=1.6);ax.fill_between(theta,0,y,where=y>=0,color=BLUE,alpha=.17);ax.fill_between(theta,0,y,where=y<0,color=ORANGE,alpha=.17)
 ax.set(title=f'Multiply by sin {n}θ',xlabel='θ',ylim=(-1.3,1.3));ax.set_xticks([-np.pi,0,np.pi],['−π','0','π'])
 ax.text(.5,-.32,'Signed area / π = '+('1: matching component survives' if n==1 else '0: positive and negative cancel'),transform=ax.transAxes,ha='center',fontsize=11,color=GREY)
fig.suptitle('Projection: multiply, then average over a whole period',fontsize=17,y=.99)
save(fig,'fourier-series-projection.svg')
fig,axes=plt.subplots(1,2,figsize=(11,4.5));fig.subplots_adjust(wspace=.32,bottom=.24)
for ax in axes:style(ax)
colors=[BLUE,ORANGE,PINK]
x=np.linspace(-.45,.45,5001)
for N,c in zip((7,31,127),colors):
 axes[0].plot(x,lab.square_sum(x,N),color=c,label=f'N={N}',lw=1.5)
 z=np.linspace(0,11,2501);axes[1].plot(z,lab.square_sum(z/(N+1),N),color=c,lw=1.5)
axes[0].plot(x,np.sign(x),color=GREY,ls='--');axes[0].set(title='Ringing occupies a narrower region',xlabel='phase θ',ylim=(-1.35,1.35));axes[0].legend(frameon=False,labelcolor=GREY,fontsize=10)
axes[1].axhline(1,color=GREY,ls='--');axes[1].axhline(1.17898,color=GREY,ls=':',lw=1);axes[1].set(xlim=(0,11),ylim=(0,1.35),title='Magnify by N+1: peak persists',xlabel='rescaled phase (N+1)θ');axes[1].set_xticks([0,np.pi,2*np.pi,3*np.pi],['0','π','2π','3π']);axes[1].annotate('limit ≈ 1.17898',xy=(np.pi,1.17898),xytext=(4.4,.55),arrowprops={'arrowstyle':'->','color':GREY},color=GREY,fontsize=12)
fig.text(.5,.03,'A jump from −1 to +1 has height 2. Overshoot ≈ 0.17898 = 8.949% of that jump.',ha='center',color=GREY,fontsize=12)
save(fig,'fourier-series-gibbs.svg')
fig,axes=plt.subplots(1,2,figsize=(11,4.2));fig.subplots_adjust(wspace=.3,bottom=.2)
for ax in axes:style(ax)
axes[0].plot(theta,np.sin(theta)+.5*np.sin(3*theta),color=BLUE,label='sin θ + 0.5 sin 3θ')
axes[0].plot(theta,np.sin(theta)+.5*np.cos(3*theta),color=PINK,label='sin θ + 0.5 cos 3θ')
axes[0].set(title='Different relative phase, different shape',xlabel='θ',ylim=(-1.65,1.65));axes[0].set_xticks([-np.pi,0,np.pi],['−π','0','π']);axes[0].legend(frameon=False,labelcolor=GREY,fontsize=9)
axes[1].bar([1,3],[1,.5],width=.5,color=BLUE,alpha=.8);axes[1].set(xlim=(0,5),ylim=(0,1.2),title='Identical magnitude spectrum',xlabel='harmonic number n',ylabel='amplitude');axes[1].set_xticks([1,2,3,4]);axes[1].text(.5,.86,'Both mean squares = (1² + 0.5²)/2 = 0.625',transform=axes[1].transAxes,ha='center',fontsize=10,color=GREY)
save(fig,'fourier-series-phase.svg')
print('Wrote four theme-compatible SVGs.')
