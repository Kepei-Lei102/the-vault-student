"""Deterministic transparent SVGs; numeric curves are calculated, not sketched."""
from pathlib import Path
import importlib.util,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('qm',D/'quantum-tunnelling-model.py');qm=importlib.util.module_from_spec(spec);spec.loader.exec_module(qm)
G='#888888';B='#2563eb';P='#7c3aed';GREEN='#059669';A='#f59e0b'
plt.rcParams.update({'text.color':G,'axes.labelcolor':G,'axes.edgecolor':G,'xtick.color':G,'ytick.color':G,'font.size':12,'svg.fonttype':'none','svg.hashsalt':'vault'})
def style(ax):
 ax.set_facecolor('none');ax.spines[['right','top']].set_visible(False);ax.grid(color=G,alpha=.15)
def save(fig,name):
 p=D/name;fig.savefig(p,transparent=True,bbox_inches='tight',metadata={'Date':None});s=p.read_text();s=re.sub(r'<svg\b[^>]*>',lambda m: re.sub(r' height="[^"]+"','',re.sub(r' width="[^"]+"',' width="100%"',m.group(0))),s,count=1);s=s.replace('<text>','<text style="fill: #888888">');p.write_text('\n'.join(l.rstrip() for l in s.splitlines())+'\n');plt.close(fig)
x=np.linspace(-3,4,1801);phi,_=qm.stationary(x)
fig,axs=plt.subplots(2,1,figsize=(10,7),sharex=True)
for ax in axs:style(ax);ax.axvspan(0,1,color=P,alpha=.12);ax.set_xlim(-3,4)
axs[0].plot([-3,0,0,1,1,4],[0,0,3,3,0,0],color=P,lw=2)
axs[0].axhline(2,color=A,ls='--',label='Incident energy E = 2');axs[0].set_ylim(-.25,4.2);axs[0].set_ylabel('Energy (model units)');axs[0].legend(loc='upper right',frameon=False,labelcolor=G)
axs[0].text(.5,3.3,'V₀ = 3',ha='center');axs[0].set_title('A finite barrier connects two allowed regions',pad=12)
axs[1].plot(x,phi.real,color=B,lw=2,label='Real part of φ');axs[1].plot(x,abs(phi),color=GREEN,lw=2,ls='--',label='Modulus |φ|');axs[1].axhline(0,color=G,lw=.8)
axs[1].set_ylim(-2.1,2.65);axs[1].set_ylabel('Amplitude (incident = 1)');axs[1].set_xlabel('Position x (model units)');axs[1].legend(loc='upper right',frameon=False,labelcolor=G,ncol=2,fontsize=11)
axs[1].text(2.1,-1.55,f'T = {qm.transmission(2):.3f}; same energy',ha='center',fontsize=11)
fig.tight_layout(h_pad=1.4);save(fig,'quantum-tunnelling-barrier.svg')
fig,axs=plt.subplots(1,2,figsize=(10,4.6));kap=5.123167
for ax in axs:style(ax);ax.set_xlabel('Barrier width a (nm)')
a=np.linspace(0,1.2,300);exact=1/np.cosh(kap*a)**2;approx=4*np.exp(-2*kap*a)
axs[0].plot(a,exact,color=B,lw=2);axs[0].set_ylabel('Transmission probability T');axs[0].set_ylim(0,1.08);axs[0].set_title('Exact: E = 1 eV, V₀ = 2 eV',fontsize=13)
axs[1].semilogy(a,exact,color=B,lw=2,label='Exact');sel=a>.45;axs[1].semilogy(a[sel],approx[sel],color=A,ls='--',lw=2,label='Opaque approximation');axs[1].set_ylim(1e-5,2);axs[1].set_title('Log scale reveals the exponential',fontsize=13);axs[1].legend(frameon=False,labelcolor=G,fontsize=10)
for av in [.5,1.]:
 tv=1/np.cosh(kap*av)**2;axs[1].plot(av,tv,'o',color=GREEN);axs[1].annotate(f'{av:.1f} nm: {tv:.5f}',(av,tv),xytext=(-35,17),textcoords='offset points',fontsize=10,color=G)
fig.tight_layout();save(fig,'quantum-tunnelling-sensitivity.svg')
fig,axs=plt.subplots(1,2,figsize=(10,4.8),sharey=True)
for ax in axs:
 style(ax);ax.set_xlim(-.6,2.9);ax.set_ylim(-1,3.6);ax.set_xticks([]);ax.set_yticks([]);ax.set_xlabel('Position across the tunnel dielectric',fontsize=10)
 ax.axhline(.5,color=A,ls='--',lw=1.3);ax.text(-.55,.67,'E',fontsize=11)
axs[0].set_ylabel('Electron potential energy (schematic)')
# No absolute semiconductor calibration is implied by these diagram coordinates.
axs[0].plot([-.6,0,0,1.5,1.5,2.8],[0,0,3,-.6,-.6,-.6],color=P,lw=2)
turn=(3-.5)/2.4
axs[0].fill_between([0,turn],[3,.5],[.5,.5],color=P,alpha=.16)
axs[0].annotate('',xy=(turn,.13),xytext=(0,.13),arrowprops={'arrowstyle':'<->','color':G});axs[0].text(turn/2,-.13,'shorter forbidden width',ha='center',fontsize=10)
axs[0].set_title('WRITE: strong field tilts the barrier',fontsize=12,pad=15)
axs[1].plot([-.6,0,0,1.5,1.5,2.8],[0,0,3,3,0,0],color=P,lw=2)
axs[1].fill_between([0,1.5],[3,3],[.5,.5],color=P,alpha=.16)
axs[1].annotate('',xy=(1.5,.13),xytext=(0,.13),arrowprops={'arrowstyle':'<->','color':G});axs[1].text(.75,-.13,'wider forbidden region',ha='center',fontsize=10)
axs[1].plot([2.1],[.5],'o',color=GREEN);axs[1].text(2.1,1.0,'stored\ncharge',ha='center',fontsize=11)
axs[1].set_title('RETAIN: remove programming field',fontsize=12,pad=15)
for ax in axs:ax.text(.75,3.28,'insulating barrier',ha='center',fontsize=10);ax.text(2.2,-.8,'storage side',ha='center',fontsize=10)
fig.tight_layout();save(fig,'quantum-tunnelling-flash.svg')
