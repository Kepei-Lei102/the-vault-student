"""Regenerate PET geometry and reconstruction figures; NumPy/matplotlib."""
from pathlib import Path
import importlib.util
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).parent
spec=importlib.util.spec_from_file_location('petmodel',P/'pet-model.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'vault-pet','text.color':'#888888','axes.labelcolor':'#888888','xtick.color':'#888888','ytick.color':'#888888','axes.edgecolor':'#888888','font.family':'DejaVu Sans','font.size':12})
def save(fig,name):
 p=P/name;fig.savefig(p,transparent=True,bbox_inches='tight',metadata={'Date':None});plt.close(fig)
 s=p.read_text();s=re.sub(r'(<svg\b[^>]*?)\swidth="[^"]*"',r'\1 width="100%"',s,count=1);s=re.sub(r'(<svg\b[^>]*?)\sheight="[^"]*"',r'\1',s,count=1);p.write_text("\n".join(line.rstrip() for line in s.splitlines())+"\n")
fig,axes=plt.subplots(2,1,figsize=(9,7),gridspec_kw={'height_ratios':[1.35,1]})
a=axes[0];a.set_aspect('equal');a.set_xlim(-1.9,1.9);a.set_ylim(-1.8,1.8);a.axis('off')
t=np.linspace(0,2*np.pi,300);a.plot(1.5*np.cos(t),1.5*np.sin(t),color='#2563eb',lw=2)
p=np.array([.45,.25]);left,right=m.chord(p,[1,.2]);a.plot([left[0],right[0]],[left[1],right[1]],color='#0891b2',lw=2)
a.scatter([left[0],right[0]],[left[1],right[1]],color='#2563eb',s=80);a.scatter(*p,color='#f59e0b',s=70)
a.annotate('annihilation site',p,xytext=(-.8,.95),arrowprops={'arrowstyle':'->','color':'#888888'},ha='center')
a.text(left[0]-.18,left[1]-.18,'L',ha='center');a.text(right[0]+.18,right[1]+.14,'R',ha='center')
for dest in [left,right]:
 start=p+.13*(dest-p);end=p+.65*(dest-p);a.annotate('',end,xytext=start,arrowprops={'arrowstyle':'->','color':'#f59e0b','lw':2})
a.set_title('A detector pair identifies a line through the source',pad=12)
a.text(0,-1.76,'Near-rest pair: two nearly opposite 511 keV photons',ha='center',fontsize=11)
a=axes[1];a.axis('off');a.set_xlim(-5,5);a.set_ylim(-1.2,1.5)
a.plot([-4,4],[0,0],color='#0891b2',lw=2);a.scatter([-4,4],[0,0],color='#2563eb',s=90);a.scatter([1],[0],color='#f59e0b',s=90)
a.text(-4,-.35,'L at −D/2',ha='center');a.text(4,-.35,'R at +D/2',ha='center');a.text(0,-.35,'0',ha='center');a.text(1,-.35,'x',ha='center')
a.annotate('',(1,.55),xytext=(-4,.55),arrowprops={'arrowstyle':'<->','color':'#888888'});a.text(-1.5,.68,'D/2 + x',ha='center')
a.annotate('',(4,.55),xytext=(1,.55),arrowprops={'arrowstyle':'<->','color':'#888888'});a.text(2.5,.68,'D/2 − x',ha='center')
a.text(0,-.95,'tL − tR = 2x/c     so     x = c(tL − tR)/2     (positive towards R)',ha='center',fontsize=12)
a.set_title('The difference removes the unknown emission time',pad=12)
fig.tight_layout(h_pad=2);save(fig,'pet-line-and-time.svg')
A,truth,counts,answer,snaps,ll=m.experiment();vmax=(truth/truth.sum()).max()
fig,axes=plt.subplots(1,2,figsize=(9,4.7))
for a,v,title in zip(axes,[truth,answer],['Known synthetic source','Reconstruction: 80 iterations']):
 a.imshow((v/v.sum()).reshape(16,16),origin='lower',extent=[-1,1,-1,1],vmin=0,vmax=vmax,cmap='inferno',interpolation='nearest');a.set_title(title);a.set_xlabel('x (model units)');a.set_ylabel('y (model units)');a.set_xticks([-1,0,1]);a.set_yticks([-1,0,1])
fig.text(.5,.03,'29,749 detected counts • same scale • ideal model, not clinical data',ha='center',fontsize=11)
fig.tight_layout(rect=[0,.08,1,1]);save(fig,'pet-reconstruction.svg')
