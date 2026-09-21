"""Matplotlib SVGs; regenerate from any cwd. Palette follows vault-svg.
Model is dynamically loaded because the adjacent filename uses hyphens.
"""
from pathlib import Path
import importlib.util, re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('coupled_model',D/'coupled-oscillators-model.py')
mod=importlib.util.module_from_spec(s);s.loader.exec_module(mod)
G='#888888'; B='#2563eb'; P='#7c3aed'; T='#0891b2'; O='#f59e0b'
plt.rcParams.update({'text.color':G,'axes.labelcolor':G,'axes.edgecolor':G,'xtick.color':G,'ytick.color':G,'font.size':12,'svg.fonttype':'none','svg.hashsalt':'vault'})
def save(fig,name):
    p=D/name
    fig.savefig(p,transparent=True,bbox_inches='tight',metadata={'Date':None})
    text=p.read_text();text=re.sub(r'<svg width="[^"]+" height="[^"]+"', '<svg width="100%"',text, count=1)
    p.write_text('\n'.join(line.rstrip() for line in text.splitlines())+'\n');plt.close(fig)
def spring(ax,a,b,y,color):
    xx=np.linspace(a,b,41);yy=np.zeros(41)+y
    yy[2:-2]=y+.065*np.where(np.arange(37)%2==0,1,-1)
    ax.plot(xx,yy,color=color,lw=1.7)
fig,axes=plt.subplots(2,1,figsize=(9,6.4))
for ax,sign,title,formula in zip(axes,[1,-1],['Together: coupling spring keeps its length','Opposite: coupling spring changes length'],[r'$x_1=x_2,\quad\omega_+=\sqrt{k/m}$',r'$x_1=-x_2,\quad\omega_-=\sqrt{(k+2\kappa)/m}$']):
    x1,x2=1.45+.28,4.05+sign*.28
    ax.set(xlim=(0,5.5),ylim=(-.65,1.05));ax.axis('off')
    ax.set_title(title,pad=8)
    for x in [0,5.5]:ax.plot([x,x],[-.25,.25],color=G,lw=3)
    spring(ax,0,x1-.19,0,B);spring(ax,x1+.19,x2-.19,0,P);spring(ax,x2+.19,5.5,0,T)
    for x,col,lab in [(x1,B,'1'),(x2,T,'2')]:
        ax.add_patch(plt.Rectangle((x-.19,-.18),.38,.36,fill=False,ec=col,lw=2));ax.text(x,0,lab,ha='center',va='center')
    for eq,x in [(1.45,x1),(4.05,x2)]:
        ax.plot([eq,eq],[-.4,.6],ls=':',color=G,alpha=.7)
        ax.annotate('',(x,.52),(eq,.52),arrowprops=dict(arrowstyle='->',color=G,lw=1.7))
    ax.text(.7,.24,'k',ha='center');ax.text(2.9,.24,'κ',ha='center');ax.text(4.85,.24,'k',ha='center')
    ax.text(2.75,-.55,formula,ha='center',fontsize=14)
fig.tight_layout(h_pad=2.0);save(fig,'coupled-oscillators-modes.svg')
fig,axes=plt.subplots(3,1,figsize=(9,9),sharex=True)
t=np.linspace(0,2*mod.SWAP,2200);x1,x2,*_=mod.state(t)
for ax in axes:
    ax.set_facecolor('none');ax.spines[['right','top']].set_visible(False);ax.grid(color=G,alpha=.15)
    ax.axvline(mod.SWAP,color=G,ls=':',lw=1)
axes[0].plot(t,x1,color=B,label='oscillator 1');axes[0].plot(t,mod.A*np.cos((mod.WM-mod.WP)*t/2),color=G,ls='--',alpha=.7,label='signed envelope')
axes[1].plot(t,x2,color=T,label='oscillator 2');axes[1].plot(t,mod.A*np.sin((mod.WM-mod.WP)*t/2),color=G,ls='--',alpha=.7,label='signed envelope')
for ax in axes[:2]:ax.set_ylabel('Displacement / m');ax.legend(frameon=False,labelcolor=G,loc='upper right');ax.set_ylim(-.6,.85)
E1,E2,Ec=mod.energies(t);total=(E1+E2+Ec)[0]
for e,c,l in [(E1,B,'E₁'),(E2,T,'E₂'),(Ec,P,'coupling spring'),(E1+E2+Ec,O,'total')]:axes[2].plot(t,e/total,color=c,label=l,lw=1.6)
axes[2].set(xlabel='Time / s',ylabel='Energy / initial total',ylim=(-.05,1.45));axes[2].legend(frameon=False,ncol=2,labelcolor=G,loc='upper center',fontsize=10)
axes[0].set_title('Two steady modes combine into a changing amplitude',pad=16)
axes[2].set_title('Exact energies: the coupling spring is a third store',fontsize=12)
fig.tight_layout(h_pad=1.3);save(fig,'coupled-oscillators-exchange.svg')
