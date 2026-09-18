"""Regenerate lens figures: MPLCONFIGDIR=/tmp/lenses-mpl python3 lenses-figures.py.
Thin paraxial lens: outgoing slope = incoming slope - height/f.
All distances arbitrary but internally consistent; dotted lines are extrapolations.
"""
from pathlib import Path
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
P=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'text.color':'#888888','svg.fonttype':'none','svg.hashsalt':'vault'})
B='#2563eb';G='#059669';A='#f59e0b';T='#0891b2';R='#dc2626';D='#888888'
def save(fig,name):
 p=P/('lenses-'+name+'.svg');fig.savefig(p,transparent=True,metadata={'Date':None});plt.close(fig)
 s=p.read_text();s=re.sub(r'<svg[^>]*',lambda m:re.sub(r'width="[^"]*"','width="100%"',re.sub(r' height="[^"]*"','',m[0])),s,count=1)
 p.write_text('\n'.join(x.rstrip() for x in s.splitlines())+'\n')
def setup(ax,x=(-3.7,4),y=(-2.4,2.4),f=1):
 ax.set(xlim=x,ylim=y,aspect='equal');ax.axis('off')
 ax.axhline(0,color=D,lw=.8);ax.plot([0,0],[-1.55,1.55],color=T,lw=3)
 # Standard thin-lens arrows: outward for converging, inward for diverging.
 for z in [-1,1]:
  ax.annotate('',xy=(0,z*(1.55 if f>0 else 1.24)),xytext=(0,z*(1.24 if f>0 else 1.55)),arrowprops={'arrowstyle':'->','color':T,'lw':2})
 for fx in [-abs(f),abs(f)]:ax.plot(fx,0,'o',ms=3,color=D);ax.text(fx,-.25,'F',ha='center',fontsize=10)
def arrow(ax,x,h,color,label=None):
 ax.annotate('',xy=(x,h),xytext=(x,0),arrowprops={'arrowstyle':'-|>','color':color,'lw':2.5})
 if label:ax.text(x,h+(.18 if h>0 else -.28),label,ha='center',fontsize=10)
def rays(ax,u,f,h=.75,ys=None,xmax=4,back=True):
 if ys is None:ys=[h,0,-.7]
 for j,y in enumerate(ys):
  c=[B,A,G][j%3];s=(y-h)/u-y/f
  ax.plot([-u,0],[h,y],color=c,lw=1.2)
  ax.annotate('',xy=(-u*.42,h*.42+y*.58),xytext=(-u*.54,h*.54+y*.46),arrowprops={'arrowstyle':'->','color':c,'lw':1.2})
  ax.plot([0,xmax],[y,y+s*xmax],color=c,lw=1.2)
  if back and u*f/(u-f)<0:
   v=u*f/(u-f);ax.plot([v,0],[y+s*v,y],color=c,lw=1,ls='--')

def atlas():
 fig,axs=plt.subplots(3,2,figsize=(13,11),layout='constrained')
 cases=[(3,1,'Beyond 2f: real, inverted, smaller'),(2,1,'At 2f: real, inverted, same size'),(1.5,1,'Between f and 2f: real, inverted, larger'),(1,1,'At f: parallel output; no finite image'),(.6,1,'Inside f: virtual, upright, larger'),(2,-1,'Diverging: virtual, upright, smaller')]
 for ax,(u,f,title) in zip(axs.flat,cases):
  setup(ax);arrow(ax,-u,.65,B,'object');ax.set_title(title,fontsize=12,color=D,pad=8)
  if u==f:
   for j,y in enumerate([.65,0,-.65]):
    s=(y-.65)/u-y/f;c=[B,A,G][j];ax.plot([-u,0,4],[.65,y,y+4*s],color=c,lw=1.2)
  else:
   v=u*f/(u-f);hi=-v/u*.65;rays(ax,u,f,.65);arrow(ax,v,hi,G,'image')
 fig.suptitle('Follow one object point. The whole image is built point by point.',fontsize=16,color=D)
 save(fig,'atlas')
def bundle():
 fig,axs=plt.subplots(2,1,figsize=(12,7),layout='constrained')
 for i,ax in enumerate(axs):
  setup(ax,x=(-3.7,2.7),y=(-1.5,1.8));u=3;v=1.5
  for h,c in [(.8,B),(-.45,A)]:
   ys=np.linspace(-1.1,1.1,9);ys=ys if i==0 else ys[ys<0]
   for y in ys:
    ax.plot([-u,0,v],[h,y,-v/u*h],color=c,lw=1,alpha=.65)
   ax.plot(-u,h,'o',color=c);ax.plot(v,-v/u*h,'o',color=c)
  if i:ax.plot([0,0],[0,1.55],color=D,lw=9);ax.text(.15,1.35,'opaque cover',fontsize=10)
  ax.text(-3.5,1.4,'two object points');ax.text(1.25,1.4,'two image points')
  ax.set_title('Whole lens: many paths from each point' if i==0 else 'Half covered: fewer paths, same image positions — dimmer',color=D,fontsize=14)
 save(fig,'bundle')
def geometry():
 fig,ax=plt.subplots(figsize=(12,5),layout='constrained');setup(ax,x=(-3.6,2.8),y=(-1.6,1.8))
 u=3;v=1.5;h=.9;hi=-.45
 arrow(ax,-u,h,B,'object');arrow(ax,v,hi,G,'image')
 ax.plot([-u,0,v],[h,0,hi],color=A,lw=2,label='central ray')
 ax.plot([-u,0,v],[h,h,hi],color=B,lw=2)
 for x1,x2,y,label in [(-u,0,-1.1,'u'),(0,v,-1.1,'v'),(0,1,1.3,'f')]:
  ax.annotate('',(x2,y),(x1,y),arrowprops={'arrowstyle':'<->','color':D});ax.text((x1+x2)/2,y+.1,label,ha='center')
 ax.text(-3.35,.4,'hₒ');ax.text(1.65,-.35,'hᵢ < 0');ax.text(.15,.95,'height hₒ at lens')
 ax.set_title('Two similar-triangle ratios describe the same image height',color=D,fontsize=16)
 save(fig,'geometry')
def vision():
 fig,axs=plt.subplots(2,2,figsize=(13,7),layout='constrained')
 # Effective eye plane at x=0, retina x=3.5. Corrector x=-2.
 for ax,kind,correct in [(axs[0,0],'myopia',False),(axs[0,1],'myopia',True),(axs[1,0],'hyperopia',False),(axs[1,1],'hyperopia',True)]:
  ax.set(xlim=(-4.4,5.5),ylim=(-1.8,1.8),aspect='equal');ax.axis('off');ax.axhline(0,color=D,lw=.6)
  retina=3.5;fe=2.5 if kind=='myopia' else 5.
  ax.plot([0,0],[-1.3,1.3],color=T,lw=4);ax.text(0,1.55,'effective eye lens',ha='center',fontsize=10)
  ax.plot([retina,retina],[-1.3,1.3],color=G,lw=3);ax.text(retina,-1.6,'retina',ha='center',fontsize=10)
  # Far-object example for both; hyperopic eye here is unaccommodated.
  if correct:
   # q = outgoing slope at eye / eye height = 1/fe - 1/retina.
   q=1/fe-1/retina;s=q/(1-2*q);fc=-1/s
   ax.plot([-2,-2],[-1.3,1.3],color=A,lw=3)
   ax.text(-2,-1.6,'diverging' if fc<0 else 'converging',ha='center',fontsize=10)
  else:s=0
  for y in [-.9,0,.9]:
   ye=y+2*s*y;out=s*y-ye/fe
   ax.plot([-4,-2,0,5.2],[y,y,ye,ye+5.2*out],color=B,lw=1.4)
  ax.set_title(('Myopia' if kind=='myopia' else 'Hyperopia')+(' — corrected' if correct else ' — without correction'),color=D,fontsize=13)
 fig.suptitle('One simplified, unaccommodated eye model; rays shown from a distant point',color=D,fontsize=14)
 save(fig,'vision')
if __name__=='__main__':atlas();bundle();geometry();vision()
