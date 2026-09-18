"""Generate the two deterministic, theme-safe CT plots."""
from pathlib import Path
import importlib.util,re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('ctmodel',HERE/'x-rays-ct-model.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'vault','text.color':'#888888','axes.labelcolor':'#888888','axes.edgecolor':'#888888','xtick.color':'#888888','ytick.color':'#888888','font.size':12})
def save(fig,name):
 p=HERE/name;fig.savefig(p,transparent=True,metadata={'Date':None});plt.close(fig)
 s=re.sub(r'<svg\s+width="[^"]+"\s+height="[^"]+"','<svg width="100%"',p.read_text(),count=1)
 p.write_text('\n'.join(l.rstrip() for l in s.splitlines())+'\n')
truth,A,b,sol=m.build()
fig,axs=plt.subplots(2,2,figsize=(10,9),layout='constrained')
for ax,data,title in [(axs[0,0],truth,'Known synthetic slice'),(axs[0,1],sol[2],'Reconstruction from 2 angles'),(axs[1,0],sol[4],'Reconstruction from 4 angles'),(axs[1,1],sol[48],'Reconstruction from 48 angles')]:
 ax.pcolormesh(m.EDGES,m.EDGES,data,cmap='viridis',vmin=0,vmax=.9,shading='flat');ax.set_aspect('equal');ax.set_title(title,color='#888888');ax.set(xlabel='x / model length',ylabel='y / model length')
fig.suptitle('Same object, same pixel grid; more directions add constraints',color='#888888')
save(fig,'x-rays-ct-reconstruction.svg')
fig,axs=plt.subplots(2,1,figsize=(9,7),layout='constrained')
x=np.linspace(0,8,200)
for mu,col in [(.35,'#2563eb'),(.78,'#7c3aed')]:axs[0].plot(x,np.exp(-mu*x),label=f'mu = {mu} per cm',color=col)
axs[0].set(xlabel='Path length / cm',ylabel='Transmitted fraction',title='Attenuation multiplies along a path');axs[0].legend(frameon=False);axs[0].grid(alpha=.15)
axs[1].pcolormesh(np.linspace(-1.875,178.125,49),np.linspace(-1.36-(2.72/28)/2,1.36+(2.72/28)/2,30),b.reshape(48,29).T,cmap='viridis',shading='flat')
axs[1].set(xlabel='Projection angle / degrees',ylabel='Detector position / model length',title='Sinogram: logarithmic attenuation, not a picture of the object')
save(fig,'x-rays-ct-attenuation-sinogram.svg')
