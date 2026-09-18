"""Regenerate two deterministic, theme-independent stellar figures."""
from pathlib import Path
import importlib.util,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).parent
sp=importlib.util.spec_from_file_location('stellar',P/'stellar-model.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'stellar-vault','text.color':'#888888','axes.labelcolor':'#888888','axes.edgecolor':'#888888','xtick.color':'#888888','ytick.color':'#888888','font.size':12})
def save(fig,name):
 p=P/name;fig.savefig(p,transparent=True,bbox_inches='tight',metadata={'Date':None});plt.close(fig)
 s=p.read_text();s=re.sub(r'(<svg\b[^>]*?)\swidth="[^"]*"',r'\1 width="100%"',s,count=1);s=re.sub(r'(<svg\b[^>]*?)\sheight="[^"]*"',r'\1',s,count=1);p.write_text('\n'.join(l.rstrip() for l in s.splitlines())+'\n')
w=np.linspace(100,2500,1500)*1e-9
fig,ax=plt.subplots(figsize=(9,5))
for t,c in [(3000,'#dc2626'),(4500,'#f59e0b'),(6000,'#2563eb')]:
 y=m.spectrum(w,t)*1e-9/1000;ax.plot(w*1e9,y,label=f'{t} K',color=c,lw=2)
 peak=m.B/t;ax.scatter(peak*1e9,m.spectrum(peak,t)*1e-9/1000,color=c)
ax.set(xlabel='Wavelength / nm',ylabel='Surface power per area per wavelength\n/ kW m⁻² nm⁻¹',xlim=(100,2500),ylim=(0,None))
ax.set_title('Hotter: shorter peak wavelength, more power at every wavelength',pad=14)
ax.legend(labelcolor='#888888',frameon=False);ax.grid(alpha=.15,color='#888888');fig.tight_layout();save(fig,'stellar-blackbody-spectra.svg')
fig,axes=plt.subplots(1,2,figsize=(9,4.5))
x=np.linspace(1,4,100);axes[0].plot(x,1/x**2,color='#0891b2',lw=2);axes[0].scatter([1,2,4],[1,.25,.0625],color='#0891b2');axes[0].set(xlabel='Distance / initial distance',ylabel='Received flux / initial flux',title='Same star: spread the power',ylim=(0,1.05))
t=np.linspace(.5,2,100)
for r,c in [(1,'#2563eb'),(2,'#7c3aed')]:axes[1].plot(t,r*r*t**4,color=c,label=f'Radius = {r} × reference',lw=2)
axes[1].set(xlabel='Temperature / reference temperature',ylabel='Luminosity / reference luminosity',title='Change the star itself',ylim=(0,65));axes[1].legend(labelcolor='#888888',frameon=False,fontsize=10)
for a in axes:a.grid(alpha=.15,color='#888888')
fig.tight_layout();save(fig,'stellar-three-controls.svg')
