"""Deterministic static figures for Ultrasound; regenerate beside this script."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import re
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'vault','font.size':12,'text.color':'#888888','axes.labelcolor':'#888888','xtick.color':'#888888','ytick.color':'#888888','axes.edgecolor':'#888888'})
def save(fig,name):
 p=OUT/name;fig.savefig(p,transparent=True,metadata={'Date':None});plt.close(fig)
 s=p.read_text();s=re.sub(r'<svg\s+width="[^"]+"\s+height="[^"]+"','<svg width="100%"',s,count=1);p.write_text("\n".join(line.rstrip() for line in s.splitlines()) + "\n")
fig,axs=plt.subplots(2,1,figsize=(9,6.7),layout='constrained')
t=np.linspace(0,100,2000);ts=np.array([2*.03/1540,2*.06/1540])*1e6
amp=.4*np.exp(-((t-ts[0])/1.5)**2)+.8*np.exp(-((t-ts[1])/1.5)**2)
axs[0].plot(t,amp,color='#059669');axs[0].set(xlabel='Return time / microseconds',ylabel='Echo envelope / arbitrary units',title='Timing gives depth: two synthetic echoes')
for time,d in zip(ts,[3,6]):axs[0].annotate(f'{d} cm: {time:.1f} us',xy=(time,.4 if d==3 else .8),xytext=(time-15,.93),arrowprops={'arrowstyle':'->','color':'#888888'},color='#888888')
axs[0].set_ylim(0,1.12);axs[0].grid(alpha=.15,color='#888888')
axs[1].axis('off');axs[1].text(.05,.85,'Same trace, displayed as brightness against depth',transform=axs[1].transAxes)
for d,b in [(3,.4),(6,.8)]:
 axs[1].plot([d,d],[0,.6],color='#059669',alpha=b,linewidth=16,solid_capstyle='butt');axs[1].text(d,-.14,f'{d} cm',ha='center')
axs[1].set(xlim=(0,8),ylim=(-.5,1));axs[1].text(0,-.42,'c = 1540 m/s; d = ct/2. Brightness gain is illustrative.',fontsize=11)
save(fig,'ultrasound-echo-depth.svg')
fig,axs=plt.subplots(2,1,figsize=(9,7),layout='constrained')
r=np.logspace(-3,3,500);axs[0].semilogx(r,((r-1)/(r+1))**2,color='#7c3aed');axs[0].set(xlabel='Impedance ratio Z2 / Z1',ylabel='Reflected intensity fraction R',title='Match the impedances to transmit the wave');axs[0].grid(alpha=.15,color='#888888')
d=np.linspace(0,10,400);axs[1].plot(d,np.exp(-.15*d),label='one-way survival exp(-mu d)',color='#f59e0b');axs[1].plot(d,np.exp(-.30*d),label='round-trip survival exp(-2 mu d)',color='#059669');axs[1].set(xlabel='One-way depth / cm',ylabel='Intensity survival fraction',title='Attenuation acts on the full path (mu = 0.15 per cm)');axs[1].legend(frameon=False);axs[1].grid(alpha=.15,color='#888888')
save(fig,'ultrasound-reflection-attenuation.svg')
