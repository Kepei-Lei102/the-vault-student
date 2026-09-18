"""Deterministic SVG ray geometry; run from any directory. Stack: matplotlib."""
from pathlib import Path
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc
OUT=Path(__file__).resolve().parent
B,G,A,P,T,GREY='#2563eb','#059669','#f59e0b','#7c3aed','#0891b2','#888888'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'text.color':GREY,'svg.fonttype':'none','svg.hashsalt':'vault'})
def base(title,xlim,ylim,size=(8,5)):
 f,a=plt.subplots(figsize=size); a.set_aspect('equal'); a.axis('off');a.set(xlim=xlim,ylim=ylim); a.set_title(title,pad=18,color=GREY,fontsize=15);return f,a
def line(a,p,q,c=GREY,ls='-',lw=2):a.plot(*zip(p,q),color=c,ls=ls,lw=lw)
def ray(a,p,q,c=B):
 line(a,p,q,c); p,q=np.array(p),np.array(q); a.annotate('',xy=p+.62*(q-p),xytext=p+.45*(q-p),arrowprops={'arrowstyle':'->','color':c,'lw':2})
def label(a,x,y,t,**kw):a.text(x,y,t,color=GREY,**kw)
def save(f,name):
 p=OUT/name; f.savefig(p,transparent=True,bbox_inches='tight',metadata={'Date':None});plt.close(f)
 s=p.read_text();s=re.sub(r'<svg\b([^>]+)>',lambda m:'<svg'+re.sub(r'\sheight="[^"]+"','',re.sub(r'width="[^"]+"','width="100%"',m[1]))+'>',s,count=1);p.write_text('\n'.join(line.rstrip() for line in s.splitlines())+'\n')
def refract(d,n,ratio):
 # n points into incident medium; return transmitted unit direction.
 c=-np.dot(d,n); k=1-ratio**2*(1-c*c)
 if k<0:return None
 return ratio*d+(ratio*c-np.sqrt(k))*n

def figures():
 f,a=base('A mirror: real rays, a virtual source',(-3.4,3.4),(-2.6,3.4))
 line(a,(0,-1.9),(0,2.2),T,lw=3);label(a,0,2.45,'plane mirror',ha='center')
 obj=np.array([-2.,.1]);im=np.array([2.,.1])
 for h in [.75,1.45]:
  hit=np.array([0.,h]); end=hit+1.3*np.array([-2.,h-.1]);ray(a,obj,hit);ray(a,hit,end,G);line(a,hit,im,P,'--',1.5)
 a.scatter(*obj,c=B,s=55);a.scatter(*im,c=P,s=55)
 label(a,-2,-.3,'object',ha='center');label(a,2,-.3,'virtual image',ha='center')
 line(a,obj,im,GREY,':',1); label(a,-1,-.7,'distance d',ha='center');label(a,1,-.7,'distance d',ha='center')
 label(a,-3.2,-2.2,'Solid: real rays. Dashed: backward extensions only.')
 save(f,'reflection-refraction-mirror.svg')
 f,a=base('Why the wavefront turns',(-.7,4.2),(-2.6,3.))
 i=np.deg2rad(50);r=np.arcsin(np.sin(i)/1.5);L=3.;C=np.array([L,0.]);O=np.zeros(2)
 v1t=L*np.sin(i);v2t=L*np.sin(r);BB=C+v1t*np.array([-np.sin(i),np.cos(i)]);D=v2t*np.array([np.sin(r),-np.cos(r)])
 a.axhspan(-2.6,0,color=T,alpha=.10);line(a,(-.5,0),(4.,0));line(a,O,BB,B);line(a,D,C,G)
 ray(a,BB,C,B);ray(a,O,D,G);line(a,O,C,GREY,':',1)
 for p,t,dx,dy in [(O,'A',-.28,.13),(BB,'B',-.27,.16),(C,'C',.08,.12),(D,'D',.08,-.26)]:a.scatter(*p,s=20,c=GREY);label(a,p[0]+dx,p[1]+dy,t)
 label(a,.65,2.5,'AB: incoming wavefront');label(a,1.4,-2.25,'CD: new wavefront')
 label(a,2.95,1.35,'BC = v₁ Δt',ha='center');label(a,-.55,-1.05,'AD = v₂ Δt',rotation=0,ha='right')
 label(a,3.35,-.6,'slower\nmedium',ha='center');label(a,.55,.24,'i');label(a,2.25,-.15,'r')
 # Angles between wavefronts and interface equal corresponding ray-normal angles.
 a.add_patch(Arc(O,.9,.9,theta1=0,theta2=50,color=A));a.add_patch(Arc(C,1,1,theta1=180,theta2=180+np.rad2deg(r),color=A))
 save(f,'reflection-refraction-wavefront.svg')
 f,a=base('A coin appears shallower: trace the outgoing rays backwards',(-1.8,2.7),(-2.5,2.1))
 a.axhspan(-2.5,0,color=T,alpha=.10);line(a,(-1.8,0),(2.7,0));obj=np.array([0.,-2.]);n=4/3
 for x in [-.22,.22]:
  hit=np.array([x,0]);i=np.arctan(abs(x)/2);r=np.arcsin(n*np.sin(i));d=np.array([np.sign(x)*np.sin(r),np.cos(r)]);end=hit+2*d
  ray(a,obj,hit,B);ray(a,hit,end,G);im=hit-(x/d[0])*d;line(a,hit,im,P,'--',1.5)
 a.scatter(0,-2,c=B,s=70);a.scatter(*im,c=P,s=45);label(a,.35,-2.1,'actual coin: 2.00 m');label(a,.35,-1.45,'apparent: ≈1.50 m')
 label(a,-1.65,.4,'air');label(a,-1.65,-.4,'water');label(a,.8,1.4,'towards observer')
 save(f,'reflection-refraction-depth.svg')
 f,axs=plt.subplots(2,2,figsize=(10,8));angles=[30,np.rad2deg(np.arcsin(1/1.5)),55]
 for a,i in zip(axs.flat,angles):
  a.set_aspect('equal');a.axis('off');a.set(xlim=(-2.6,2.6),ylim=(-2.6,1.6));a.axhspan(-2.6,0,color=T,alpha=.10);line(a,(-2.5,0),(2.5,0));line(a,(0,-2.5),(0,1.3),GREY,'--',1)
  t=np.deg2rad(i);ray(a,(-2.2*np.sin(t),-2.2*np.cos(t)),(0,0),B);ray(a,(0,0),(2.2*np.sin(t),-2.2*np.cos(t)),A)
  if i<=angles[1]+1e-8:
   r=np.arcsin(min(1,1.5*np.sin(t)));ray(a,(0,0),(2.3*np.sin(r),2.3*np.cos(r)),G)
  a.set_title(f'i = {i:.2f}°'+('  (critical)' if abs(i-angles[1])<1e-6 else ''),color=GREY,fontsize=13)
  label(a,-2.4,.7,'air');label(a,-2.4,-2.3,'glass, n = 1.50')
 axs[1,1].axis('off');axs[1,1].text(.05,.8,'Below critical: two paths\n\nAt critical: limiting ray along surface\n\nAbove critical: total reflection\n\nRay thickness does not show power.',transform=axs[1,1].transAxes,color=GREY,fontsize=12,va='top')
 f.tight_layout(pad=2);save(f,'reflection-refraction-critical.svg')
 f,a=base('An air bubble in water: the normal changes at each surface',(-3,3),(-1.4,2.1))
 a.add_patch(Circle((0,0),1,fill=False,ec=T,lw=2));label(a,-.25,-.6,'air');label(a,-2.7,-1,'water')
 for h,c,name in [(0,G,'B'),(.5,B,'A')]:
  p=np.array([-np.sqrt(1-h*h),h]);d=refract(np.array([1.,0]),p,4/3);q=p-2*np.dot(p,d)*d;e=refract(d,-q,3/4)
  ray(a,(-2.8,h),p,c);ray(a,p,q,c);ray(a,q,q+1.4*e,c);label(a,-2.8,h+.15,name)
  if h:
   line(a,p-0.4*p,p+.5*p,GREY,'--',1);line(a,q-.4*q,q+.5*q,GREY,'--',1)
   assert d[1]>0 and e[1]>d[1]
 label(a,-2.8,1.65,'B meets both surfaces normally. A bends at both.')
 save(f,'reflection-refraction-bubble.svg')

def checks():
 i=np.deg2rad(40);r=np.arcsin(np.sin(i)/1.5);assert abs(np.sin(i)-1.5*np.sin(r))<1e-12
 assert abs(np.rad2deg(r)-25.37399394)<1e-7
 assert abs(np.rad2deg(np.arcsin(1/1.5))-41.8103149)<1e-6
 # Reversibility through a parallel slab, and a forbidden transmitted direction.
 assert np.allclose(refract(refract(np.array([np.sin(i),-np.cos(i)]),np.array([0.,1.]),1/1.5),np.array([0.,1.]),1.5),[np.sin(i),-np.cos(i)])
 assert refract(np.array([np.sin(np.deg2rad(55)),np.cos(np.deg2rad(55))]),np.array([0.,-1.]),1.5) is None
 print('PASS: Snell, critical angle, slab reversibility, TIR, bubble geometry')
if __name__=='__main__':checks();figures()
