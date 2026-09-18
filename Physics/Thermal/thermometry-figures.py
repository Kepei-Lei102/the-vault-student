"""Regenerate the illustrative calibration figure; matplotlib, theme-neutral SVG."""
from pathlib import Path
import re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'vault','text.color':'#888888','axes.labelcolor':'#888888','xtick.color':'#888888','ytick.color':'#888888','axes.edgecolor':'#888888','font.size':11})
x=np.linspace(0,100,301);y=x+.002*x*(x-100)
fig,ax=plt.subplots(1,2,figsize=(10,3.7),layout='constrained')
ax[0].plot(x,x,color='#059669',label='Linear sensors (overlap)');ax[0].plot(x,y,color='#7c3aed',label='Curved sensor')
ax[0].scatter([0,100],[0,100],color='#f59e0b',zorder=3)
ax[0].scatter([50],[45],color='#7c3aed',zorder=3)
ax[0].set(xlabel='Reference temperature / °C',ylabel='Linear indication / °C',title='Two correct endpoints can hide curvature')
ax[0].legend(frameon=False,fontsize=9)
ax[1].plot(x,y-x,color='#dc2626');ax[1].axhline(0,color='#888888',lw=.7);ax[1].set(xlabel='Reference temperature / °C',ylabel='Indication error / °C',title='Test the middle, not just the ends')
for a in ax:a.grid(alpha=.15);a.set_facecolor('none')
p=Path(__file__).with_name('thermometry-calibration.svg');fig.savefig(p,transparent=True,metadata={'Date':None});plt.close(fig)
s=p.read_text();s=re.sub(r'width="[^"]+" height="[^"]+"','width="100%"',s,count=1);p.write_text('\n'.join(line.rstrip() for line in s.splitlines())+'\n')
