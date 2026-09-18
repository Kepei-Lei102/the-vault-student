"""Regenerate the two Nuclear Physics teaching plots; no external data download."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({'svg.fonttype':'none','font.family':'DejaVu Sans','font.size':11,
                     'text.color':'#888888','axes.labelcolor':'#888888','axes.edgecolor':'#888888',
                     'xtick.color':'#888888','ytick.color':'#888888','figure.facecolor':'none',
                     'axes.facecolor':'none','savefig.facecolor':'none'})

def save(fig, name):
    path=ROOT / name
    fig.savefig(path, format='svg', bbox_inches='tight', transparent=True)
    s=path.read_text()
    s=re.sub(r'<svg([^>]+)>',lambda m:'<svg'+re.sub(r'\s(?:width|height)="[^"]*"','',m[1])+' width="100%">',s,count=1)
    path.write_text("\n".join(line.rstrip() for line in s.splitlines()) + "\n")
    plt.close(fig)

def style(ax):
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.15,color='#888888')

fig,ax=plt.subplots(figsize=(8.6,4.5))
t=np.linspace(0,4,400); source=80*2**(-t)
ax.plot(t,source+20,color='#7c3aed',lw=2.5,label='Measured: source + background')
ax.plot(t,source,color='#2563eb',lw=2.5,label='Source after subtraction')
ax.axhline(20,color='#f59e0b',ls='--',lw=1.7,label='Constant background')
for x,y in [(0,80),(1,40),(2,20)]:
    ax.scatter([x],[y],color='#2563eb',s=30,zorder=3)
    ax.annotate(str(y),(x,y),xytext=(7,7),textcoords='offset points',color='#888888')
ax.set(xlim=(-.07,4.08),ylim=(0,113),xlabel='Time / half-lives',ylabel='Expected count rate / counts s⁻¹',title='Halve the source contribution, not the raw reading')
ax.set_xticks(range(5));style(ax);ax.legend(frameon=False,loc='upper right',fontsize=10)
save(fig,'nuclear-decay-background.svg')

# Rounded teaching landmarks, not a fitted mass model: nuclei with equal A can differ.
a=np.array([1,2,4,12,16,40,56,62,120,208,238])
b=np.array([0,1.112,7.074,7.680,7.976,8.551,8.790,8.795,8.505,7.868,7.570])
fig,ax=plt.subplots(figsize=(8.6,4.7))
ax.plot(a,b,color='#2563eb',lw=2.4,marker='o',ms=3)
ax.annotate('He-4',(4,7.074),xytext=(20,6.3),arrowprops={'arrowstyle':'-','color':'#888888'},color='#888888')
ax.annotate('Iron / nickel region',(60,8.8),xytext=(65,9.25),color='#888888')
ax.annotate('U-238',(238,7.57),xytext=(192,6.5),arrowprops={'arrowstyle':'-','color':'#888888'},color='#888888')
ax.annotate('',xy=(49,8.35),xytext=(12,4.1),arrowprops={'arrowstyle':'->','lw':2,'color':'#059669'})
ax.text(32,4.8,'Fusion of light nuclei',color='#888888')
ax.annotate('',xy=(116,8.15),xytext=(224,7.0),arrowprops={'arrowstyle':'->','lw':2,'color':'#7c3aed'})
ax.text(114,5.9,'Fission of heavy nuclei',color='#888888')
ax.set(xlim=(0,250),ylim=(0,10),xlabel='Nucleon number A',ylabel='Binding energy per nucleon / MeV',title='More tightly bound products have lower rest energy')
style(ax)
fig.text(.13,-.02,'Rounded isotope landmarks joined as a guide; not every nuclide lies on one curve.',fontsize=9,color='#888888')
save(fig,'nuclear-binding-energy.svg')
