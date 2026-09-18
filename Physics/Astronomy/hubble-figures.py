"""Deterministic, transparent matplotlib figures. Synthetic models labelled."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import re
ROOT=Path(__file__).parent
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'vault','font.family':'DejaVu Sans','font.size':11,'text.color':'#888888','axes.labelcolor':'#888888','axes.edgecolor':'#888888','xtick.color':'#888888','ytick.color':'#888888'})
def save(fig,name):
 p=ROOT/name;fig.savefig(p,transparent=True,metadata={'Date':None},bbox_inches='tight');plt.close(fig)
 s=p.read_text();s=re.sub(r'width="[^"]+" height="[^"]+"', 'width="100%"',s,count=1);p.write_text('\n'.join(line.rstrip() for line in s.splitlines())+'\n')
fig,axs=plt.subplots(1,2,figsize=(11,4.1),layout='constrained')
d=np.array([10,20,35,50,70,90,110]);noise=np.array([-260,220,-170,280,-250,160,-90]);v=70*d+noise
axs[0].scatter(d,v,color='#2563eb',label='Synthetic galaxies')
axs[0].plot([0,120],[0,8400],color='#059669',label='Model: 70 km/s per Mpc')
axs[0].set(xlabel='Distance / Mpc',ylabel='Recession speed / km s⁻¹',title='Linear axes: gradient gives H₀',xlim=(0,120),ylim=(0,9000))
axs[0].legend(frameon=False,fontsize=9)
x=np.linspace(10,120,100);axs[1].plot(np.log10(x),np.log10(70*x),color='#7c3aed')
axs[1].set(xlabel='log₁₀ [d / Mpc]',ylabel='log₁₀ [v / (km s⁻¹)]',title='Log–log axes: gradient gives 1')
axs[1].text(.06,.85,'log v = log 70 + log d\n(unit-normalised values)',transform=axs[1].transAxes)
for ax in axs:ax.grid(alpha=.15)
save(fig,'hubble-axes-and-scatter.svg')
fig,ax=plt.subplots(figsize=(8,4.8),layout='constrained')
for p,col,label in [(1,'#2563eb','Coasting: age = 1/H₀'),(2/3,'#059669','Matter-only flat: age = 2/(3H₀)'),(.5,'#7c3aed','Radiation-only flat: age = 1/(2H₀)')]:
 u=np.linspace(-p,0.18,400);ax.plot(u,np.maximum(0,1+u/p)**p,color=col,label=label)
ax.plot([-.25,.2],[.75,1.2],'--',color='#888888',label='Shared present tangent')
ax.scatter([0],[1],color='#f59e0b',zorder=5)
ax.set(xlabel='Time relative to now, in units of 1/H₀',ylabel='Scale factor a (now = 1)',title='Same H₀ today, different expansion histories',xlim=(-1.05,.2),ylim=(0,1.25))
ax.axvline(0,color='#888888',alpha=.4);ax.legend(loc='lower right',frameon=False,fontsize=9);ax.grid(alpha=.15)
save(fig,'hubble-time-and-age.svg')
