"""Regenerate three transparent, deterministic matplotlib SVGs beside this source."""
from pathlib import Path
import importlib.util,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('qm',D/'quantum-states-model.py');qm=importlib.util.module_from_spec(s);s.loader.exec_module(qm)
G='#888888';B='#2563eb';P='#7c3aed';T='#0891b2';A='#f59e0b';GREEN='#059669'
plt.rcParams.update({'text.color':G,'axes.labelcolor':G,'axes.edgecolor':G,'xtick.color':G,'ytick.color':G,'font.size':12,'svg.fonttype':'none','svg.hashsalt':'vault'})
def style(ax):
 ax.set_facecolor('none');ax.spines[['right','top']].set_visible(False);ax.grid(color=G,alpha=.15)
def save(fig,name):
 p=D/name;fig.savefig(p,transparent=True,bbox_inches='tight',metadata={'Date':None});t=p.read_text();t=re.sub(r'<svg width="[^"]+" height="[^"]+"','<svg width="100%"',t,count=1);p.write_text('\n'.join(l.rstrip() for l in t.splitlines())+'\n');plt.close(fig)
x=np.linspace(0,1,1001)
fig,axes=plt.subplots(2,2,figsize=(10,7.4))
for i,n in enumerate([1,2]):
 a,b=axes[i];phi=qm.phi(x,n)
 for ax in [a,b]:style(ax);ax.set_xlabel('Position x / L');ax.set_xlim(0,1)
 a.plot(x,phi,color=B,lw=2);a.axhline(0,color=G,lw=.7);a.set_ylim(-1.65,1.65);a.set_ylabel('Scaled amplitude');a.set_title(f'n = {n}: amplitude has a sign',fontsize=13)
 b.plot(x,phi**2,color=GREEN,lw=2);b.fill_between(x,phi**2,where=(x>=.25)&(x<=.75),color=GREEN,alpha=.16);b.set_ylim(0,2.4);b.set_ylabel('Scaled density');b.set_title('Density is non-negative; area is probability',fontsize=12)
 b.text(.5,2.17,'middle-half probability = '+('0.8183' if n==1 else '0.5000'),ha='center',fontsize=10)
fig.tight_layout(h_pad=2,w_pad=2);save(fig,'quantum-states-amplitude-density.svg')
fig,axes=plt.subplots(2,1,figsize=(9,7.4))
for ax in axes:style(ax);ax.set_xlim(0,1);ax.set_xlabel('Position x / L');ax.set_ylabel('Scaled density')
for tau,col,label in [(0,B,'relative phase 0'),(np.pi/6,P,'relative phase π/2'),(np.pi/3,T,'relative phase π')]:axes[0].plot(x,qm.density(x,tau),color=col,lw=2,label=label)
axes[0].set_ylim(0,4.3);axes[0].legend(frameon=False,labelcolor=G,ncol=3,loc='upper center',fontsize=10);axes[0].set_title('Coherent superposition: the relative phase matters',pad=12)
axes[1].plot(x,qm.density(x,0,'mixture'),color=G,lw=2,label='50–50 mixture, at every time');axes[1].set_ylim(0,2.2);axes[1].legend(frameon=False,labelcolor=G,loc='upper center');axes[1].set_title('Random preparation: add probabilities, no cross term',pad=12)
fig.tight_layout(h_pad=2);save(fig,'quantum-states-superposition-mixture.svg')
fig,axes=plt.subplots(1,2,figsize=(10,4.6))
for ax,L in zip(axes,[1,.5]):
 style(ax);ax.set_xlim(-.15,1.15);ax.set_ylim(0,39);ax.set_xlabel('Position / original width');ax.set_ylabel('Energy / original E₁');ax.set_title(f'Width = {L:g} × original width',pad=12)
 ax.axvline(0,color=G,lw=2);ax.axvline(L,color=G,lw=2)
 for n,col in zip([1,2,3],[B,P,T]):
  en=n*n/L**2;ax.plot([0,L],[en,en],color=col,lw=2);ax.text(L+.04,en,f'n={n}: {en:g}',va='center',fontsize=11)
fig.suptitle('Half the width: four times each energy and each gap',fontsize=14)
fig.tight_layout();save(fig,'quantum-states-confinement.svg')
