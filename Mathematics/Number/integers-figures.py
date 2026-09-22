"""Regenerate both transparent figures: python3 integers-figures.py."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
OUT=Path(__file__).resolve().parent
DIM='#888888'; BLUE='#64b5f6'; GREEN='#66bb6a'; RED='#ef5350'
plt.rcParams.update({'font.family':'DejaVu Sans','text.color':DIM,'svg.fonttype':'none','svg.hashsalt':'vault'})
def save(fig,name):
    p=OUT/name
    fig.savefig(p,transparent=True,metadata={'Date':None},bbox_inches='tight',pad_inches=.22)
    s=p.read_text();s=re.sub(r'<svg([^>]*?)width="[^"]+" height="[^"]+"',r'<svg\1width="100%"',s,count=1);p.write_text('\n'.join(line.rstrip() for line in s.splitlines())+'\n');plt.close(fig)
def line(ax):
    ax.set_xlim(-6,6);ax.set_ylim(-.75,1.5);ax.axis('off')
    ax.annotate('',(5.7,0),(-5.7,0),arrowprops={'arrowstyle':'<->','color':DIM})
    for x in range(-5,6):
        ax.plot([x,x],[-.07,.07],color=DIM,lw=1)
        ax.text(x,-.27,str(x),ha='center',va='top',fontsize=12)
fig,axs=plt.subplots(2,1,figsize=(10,4.8))
for a in axs:line(a)
a=axs[0];a.set_title('Subtracting −5 undoes a move to the left',fontsize=15,loc='left',color=DIM)
a.scatter([-3],[0],color=BLUE,s=75,zorder=4);a.scatter([2],[0],color=GREEN,s=75,zorder=4)
a.annotate('',(2,.65),(-3,.65),arrowprops={'arrowstyle':'->','color':GREEN,'lw':3})
a.text(-.5,1.0,'−3 − (−5) = −3 + 5 = 2',ha='center',fontsize=14)
a=axs[1];a.set_title('Negation reflects a position in zero',fontsize=15,loc='left',color=DIM)
a.scatter([-3],[0],color=BLUE,s=75,zorder=4);a.scatter([3],[0],color=GREEN,s=75,zorder=4)
a.plot([-3,0,3],[.35,1,.35],color=DIM,ls='--');a.text(0,1.12,'opposites: −3 and 3',ha='center',fontsize=13)
fig.tight_layout(h_pad=1.8);save(fig,'integers-number-line.svg')
fig,axs=plt.subplots(3,1,figsize=(9,5.7))
for a,(pos,neg) in zip(axs,[(0,3),(1,4),(2,5)]):
    a.set_xlim(-.5,9);a.set_ylim(-.65,.8);a.axis('off')
    a.text(-.3,.05,f'({pos}, {neg})',fontsize=17,va='center')
    for n,start,color,sign in [(pos,2,GREEN,'+'),(neg,4.5,RED,'−')]:
        for i in range(n):
            a.add_patch(Circle((start+i*.52,0),.18,edgecolor=color,facecolor='none',lw=2))
            a.text(start+i*.52,0,sign,ha='center',va='center',fontsize=13)
    a.text(8.1,0,'−3',fontsize=20,va='center',ha='center')
axs[0].text(2,.55,'Positive counts',fontsize=12);axs[0].text(4.5,.55,'Negative counts',fontsize=12);axs[0].text(8.1,.55,'Value',ha='center',fontsize=12)
fig.suptitle('Different records. The same integer.',fontsize=18,color=DIM,y=.99)
fig.text(.5,.02,'Add one to both counts: the net value stays unchanged.',ha='center',fontsize=13)
fig.subplots_adjust(top=.9,bottom=.1,hspace=.25);save(fig,'integers-equivalent-pairs.svg')
