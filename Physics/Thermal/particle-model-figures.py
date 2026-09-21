"""Regenerate the particle schematics and quantitative Boyle-law graph."""
from pathlib import Path
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'svg.hashsalt':'vault','svg.fonttype':'none','font.size':12,'text.color':'#888888','axes.labelcolor':'#888888','xtick.color':'#888888','ytick.color':'#888888','axes.edgecolor':'#888888'})

def save(fig,name):
    p=ROOT/name
    fig.savefig(p,transparent=True,metadata={'Date':None},bbox_inches='tight')
    s=p.read_text()
    s=re.sub(r'width="[^"]+" height="[^"]+"','width="100%"',s,count=1)
    p.write_text(s)
    plt.close(fig)

fig,axs=plt.subplots(2,2,figsize=(9,6.8))
fig.subplots_adjust(hspace=.25,wspace=.25)
for ax in axs.flat:
    ax.set(xlim=(0,10),ylim=(0,7)); ax.set_aspect('equal'); ax.axis('off')
for ax,title,sub in zip(axs.flat,['Solid','Liquid','Gas','Brownian motion'],['Close; ordered in this crystal','Close; irregular neighbours','Far apart; fill available space','The speck is NOT a molecule']):
    ax.set_title(title+'\n'+sub,color='#888888',fontsize=13)
    ax.add_patch(Rectangle((.3,.9),9.4,5.9,fill=False,edgecolor='#888888',lw=1))
solid=np.array([(3+i*.7,2+j*.7) for j in range(4) for i in range(6)])
liquid=solid+np.array([(.15*(-1)**i,.16*np.sin(i*4)) for i in range(24)])
gas=np.array([(1+i*1.55,1.65+j*1.45) for j in range(4) for i in range(6)])+np.random.default_rng(625).uniform(-.3,.3,(24,2))
for ax,pts,caption in zip(axs.flat,[solid,liquid,gas],['Vibrate about fixed positions','Move past one another','Travel between collisions']):
    for x,y in pts: ax.add_patch(Circle((x,y),.19,color='#2563eb',alpha=.8))
    ax.text(5,.15,caption,ha='center',fontsize=12)
ax=axs[1,1]
path=np.array([[3.6,3],[4.3,3.3],[4,4],[4.9,3.7],[5.5,4.4],[5.2,3.9]])
ax.plot(path[:,0],path[:,1],color='#f59e0b',lw=2)
ax.add_patch(Circle(path[-1],.5,facecolor='#f59e0b',alpha=.7))
for angle in np.linspace(0,2*np.pi,7,endpoint=False):
    v=np.array([np.cos(angle),np.sin(angle)])
    p=path[-1]+1.8*v
    ax.add_patch(Circle(p,.09,color='#0891b2'))
    ax.annotate('',xy=path[-1]+.65*v,xytext=p-.15*v,arrowprops={'arrowstyle':'->','color':'#0891b2','lw':1})
ax.text(5,1.35,'Tiny molecules give unequal kicks',ha='center',fontsize=11)
ax.text(5,.15,'Amber trail: positions of one speck',ha='center',fontsize=11)
fig.text(.5,.02,'Schematic: same particle size; spacing and molecular sizes not to scale.',ha='center',fontsize=11)
save(fig,'particle-model-states.svg')
fig,ax=plt.subplots(figsize=(8,4.7))
v=np.linspace(10,80,400)
ax.plot(v,4000/v,color='#2563eb',lw=2.6)
ax.scatter([20,40],[200,100],color='#059669',s=45,zorder=4)
ax.annotate('20 cm³, 200 kPa',xy=(20,200),xytext=(32,245),arrowprops={'arrowstyle':'->','color':'#888888'})
ax.annotate('40 cm³, 100 kPa',xy=(40,100),xytext=(48,165),arrowprops={'arrowstyle':'->','color':'#888888'})
ax.set(xlim=(0,85),ylim=(0,430),xlabel='Volume V / cm³',ylabel='Pressure p / kPa',title='Fixed amount, fixed temperature: pV = 4000 kPa cm³')
ax.spines[['top','right']].set_visible(False)
ax.grid(alpha=.15,color='#888888')
fig.text(.5,.01,'Halve V, double p. The curve is a hyperbola; it never meets either axis.',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.04,1,1))
save(fig,'particle-model-boyle.svg')
assert 4000/20 == 200 and 4000/40 == 100
assert np.allclose((4000/v)*v,4000)
# Different amount: scaling pV doubles every pressure at fixed V.
assert np.allclose(8000/v,2*4000/v)
