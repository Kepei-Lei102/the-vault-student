"""Regenerate both polarisation figures and independently check the calculations."""
from pathlib import Path
import re
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle

HERE=Path(__file__).resolve().parent
GREY='#888888'; BLUE='#2563eb'; GREEN='#059669'; PURPLE='#7c3aed'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'text.color':GREY,
 'axes.labelcolor':GREY,'xtick.color':GREY,'ytick.color':GREY,
 'svg.fonttype':'none','svg.hashsalt':'vault','mathtext.default':'regular'})

def save(fig,name):
    fig.patch.set_alpha(0)
    path=HERE/name
    fig.savefig(path,transparent=True,metadata={'Date':None})
    s=path.read_text()
    def root(m):
        r=re.sub(r'\s(?:width|height)="[^"]*"','',m.group())
        return r[:-1]+' width="100%">'
    s=re.sub(r'<svg\b[^>]*>',root,s,count=1)
    path.write_text("\n".join(line.rstrip() for line in s.splitlines())+"\n")
    plt.close(fig)

def style(ax):
    ax.set_facecolor('none')
    for edge in ['top','right']:ax.spines[edge].set_visible(False)
    for edge in ['bottom','left']:ax.spines[edge].set_color(GREY)
    ax.grid(alpha=.15,color=GREY)

fig,(a,b)=plt.subplots(1,2,figsize=(11,4.8),gridspec_kw={'width_ratios':[1,1.3]})
fig.subplots_adjust(left=.04,right=.97,bottom=.20,top=.79,wspace=.34)
fig.text(.04,.94,'PROJECT THE FIELD. THEN SQUARE.',fontsize=17,weight='bold')
a.set_aspect('equal');a.set_xlim(-.12,1.32);a.set_ylim(-.15,1.12);a.axis('off')
t=np.deg2rad(40);end=np.array([np.cos(t),np.sin(t)])
a.plot([-.08,1.2],[0,0],color=GREY,lw=1.2)
a.annotate('',xy=end,xytext=(0,0),arrowprops={'arrowstyle':'->','color':BLUE,'lw':3})
a.annotate('',xy=(end[0],0),xytext=(0,0),arrowprops={'arrowstyle':'->','color':GREEN,'lw':4})
a.plot([end[0],end[0]],[0,end[1]],'--',color=GREY,lw=1)
a.add_patch(Arc((0,0),.50,.50,theta1=0,theta2=40,color=GREY))
a.text(.29,.065,r'$\theta$',fontsize=14)
a.text(.20,.49,r'Incident $E_0$',rotation=40)
a.text(end[0]+.035,.38,'Rejected\ncomponent',fontsize=10)
a.text(.40,-.115,r'Passed: $E_0\cos\theta$',ha='center',fontsize=12)
a.text(.08,1.02,'View along the beam',fontsize=12)
a.text(1.19,-.10,'Axis',fontsize=10,ha='center')
style(b)
x=np.linspace(0,360,1001);y=np.cos(np.deg2rad(x))**2
b.plot(x,y,color=GREEN,lw=2.8)
b.scatter([0,90,180,270,360],[1,0,1,0,1],color=GREEN,s=22)
b.set_xlim(0,360);b.set_ylim(-.04,1.10)
b.set_xticks([0,90,180,270,360]);b.set_yticks([0,.25,.5,.75,1])
b.set_xlabel('Relative angle θ / degrees',labelpad=9)
b.set_ylabel('Transmitted intensity / incident intensity',fontsize=10)
b.set_title(r'$I/I_0=\cos^2\theta$',color=GREY,pad=12)
fig.text(.04,.05,'The angle compares two transverse directions; it is not the angle at which the ray hits the sheet.',fontsize=11)
save(fig,'polarisation-projection-and-malus.svg')

fig=plt.figure(figsize=(11,6.8));gs=fig.add_gridspec(2,1,height_ratios=[1,1.3])
a=fig.add_subplot(gs[0]);b=fig.add_subplot(gs[1])
fig.subplots_adjust(left=.095,right=.955,bottom=.14,top=.85,hspace=.70)
fig.text(.05,.95,'ONE EXTRA FILTER CAN LET LIGHT THROUGH',fontsize=17,weight='bold')
a.set_xlim(0,10);a.set_ylim(-.3,1.3);a.axis('off')
# Schematic optical train: small circles are face-on transmission-axis symbols.
for cx,deg,lab in [(1.1,90,'Vertical input'),(4.5,45,'Middle axis: 45°'),(7.8,0,'Horizontal analyser')]:
    a.add_patch(Circle((cx,.55),.38,facecolor='none',edgecolor=GREY,lw=1))
    v=.34*np.array([np.cos(np.deg2rad(deg)),np.sin(np.deg2rad(deg))])
    a.plot([cx-v[0],cx+v[0]],[.55-v[1],.55+v[1]],color=PURPLE,lw=3)
    a.text(cx,1.11,lab,ha='center',fontsize=11)
for x0,x1,lab in [(1.65,3.9,'I₀'),(5.05,7.2,'I₀ / 2'),(8.35,9.65,'I₀ / 4')]:
    a.annotate('',xy=(x1,.55),xytext=(x0,.55),arrowprops={'arrowstyle':'->','color':GREEN,'lw':2})
    a.text((x0+x1)/2,.08,lab,ha='center',fontsize=13)
a.text(5,-.30,'Light travels left to right. Symbols show the axes viewed along the beam.',ha='center',fontsize=10)
style(b)
x=np.linspace(0,90,501);y=np.cos(np.deg2rad(x))**2*np.sin(np.deg2rad(x))**2
b.plot(x,y,color=PURPLE,lw=3);b.scatter([0,45,90],[0,.25,0],color=PURPLE)
b.set_xlim(0,90);b.set_ylim(-.01,.31);b.set_xticks([0,15,30,45,60,75,90]);b.set_yticks([0,.125,.25])
b.set_yticklabels(['0','1/8','1/4']);b.set_xlabel('Middle-axis angle α to the vertical / degrees',labelpad=9)
b.set_ylabel('Final intensity / I₀')
b.text(45,.277,'Best angle: 45°: one quarter transmitted',ha='center',fontsize=11)
fig.text(.095,.035,'Without the middle filter: zero. Insert it after the horizontal analyser: still zero.',fontsize=11)
save(fig,'polarisation-third-filter.svg')

# Independent vector-projection and intensity-product checks, including signed angles.
rng=np.random.default_rng(9702)
for _ in range(1000):
    angles=rng.uniform(-2*np.pi,2*np.pi,5)
    e=np.array([np.cos(angles[0]),np.sin(angles[0])])
    power=1.
    for before,after in zip(angles[:-1],angles[1:]):
        u=np.array([np.cos(after),np.sin(after)])
        e=np.outer(u,u)@e
        power*=np.cos(after-before)**2
    assert np.isclose(e@e,power,atol=1e-12)
ph=np.diag([1.,0.]);pv=np.diag([0.,1.]);p45=np.ones((2,2))/2
assert np.allclose(ph@pv,0)
assert np.allclose(ph@p45@pv,np.array([[0.,.5],[0.,0.]]))
I1=8.5*np.cos(np.deg2rad(35))**2
alpha=35+np.rad2deg(np.arccos(np.sqrt(5.2/I1)))
assert round(alpha)==52
amp=np.cos(np.deg2rad(70));assert round(amp,2)==.34
assert np.isclose(np.mean(np.cos(np.linspace(0,np.pi,10000,endpoint=False))**2),.5)
# Circular light gives orientation-independent half transmission on time average.
phase=np.linspace(0,2*np.pi,10000,endpoint=False)
E=np.array([np.cos(phase),np.sin(phase)])
for angle in np.linspace(0,np.pi,21):
    u=np.array([np.cos(angle),np.sin(angle)])
    assert np.isclose(np.mean((u@E)**2)/np.mean(np.sum(E*E,axis=0)),.5)
print(f'1000 projection chains passed; first intensity={I1:.8f}; alpha={alpha:.8f}; amplitude={amp:.8f}')
print('Matrix order, unpolarised average and 21 circular-analyser orientations passed.')
