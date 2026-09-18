"""Generate deterministic potential figures and independently check card numerics.
Run: MPLCONFIGDIR=/tmp/vault-mpl python3 electric-potential-verify.py
"""
from pathlib import Path
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad
HERE=Path(__file__).resolve().parent
K=8.9875517923e9; E=1.602176634e-19; M=9.1093837139e-31; C=299792458.
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'vault','font.size':12,'text.color':'#888','axes.labelcolor':'#888','xtick.color':'#888','ytick.color':'#888','axes.edgecolor':'#888'})
def save(fig,name):
 p=HERE/name;fig.savefig(p,transparent=True,metadata={'Date':None},bbox_inches='tight')
 s=p.read_text();s=re.sub(r'<svg[^>]*>',lambda m:re.sub(r'width="[^"]+"','width="100%"',re.sub(r' height="[^"]+"','',m.group())),s,count=1)
 p.write_text('\n'.join(l.rstrip() for l in s.splitlines())+'\n');plt.close(fig)
def potential(p,charges):
 return sum(q/np.linalg.norm(np.asarray(p)-np.asarray(r),axis=-1) for q,r in charges)
def field(p,charges):
 p=np.asarray(p);return sum(q*(p-np.asarray(r))/np.linalg.norm(p-np.asarray(r),axis=-1)[...,None]**3 for q,r in charges)
def figures():
 fig,axs=plt.subplots(1,2,figsize=(11,4.8))
 xx=np.linspace(-2.8,2.8,360);yy=np.linspace(-2,2,280);x,y=np.meshgrid(xx,yy);p=np.stack([x,y],axis=-1)
 for ax,sign,title in zip(axs,[1,-1],['+Q, +Q: midpoint E = 0, V > 0','+Q, −Q: midpoint V = 0, E ≠ 0']):
  charges=[(1,[-1,0]),(sign,[1,0])];v=potential(p,charges)
  mask=((x+1)**2+y*y<.15**2)|((x-1)**2+y*y<.15**2);v=np.ma.masked_where(mask,v)
  levels=[.6,.9,1.2,1.5,1.8,2.1,2.4,3.] if sign==1 else [-3,-2,-1,-.5,0,.5,1,2,3]
  contours=ax.contour(x,y,v,levels=levels,colors='#7c3aed',linewidths=1)
  ax.clabel(contours,fontsize=9,colors='#888',inline=True)
  qx,qy=np.meshgrid(np.linspace(-2.5,2.5,10),np.linspace(-1.7,1.7,8));qp=np.stack([qx,qy],axis=-1);ef=field(qp,charges);norm=np.linalg.norm(ef,axis=-1)
  ax.quiver(qx,qy,ef[...,0]/norm,ef[...,1]/norm,color='#0891b2',scale=25,width=.004)
  ax.scatter([-1,1],[0,0],s=160,c=['#2563eb','#2563eb' if sign==1 else '#dc2626'],zorder=4)
  ax.scatter([0],[0],s=35,c='#059669',zorder=4)
  ax.set(xlim=(-2.8,2.8),ylim=(-2,2),aspect='equal');ax.set_title(title,fontsize=12,pad=12);ax.axis('off')
 fig.tight_layout();save(fig,'electric-potential-maps.svg')
 fig,axs=plt.subplots(1,2,figsize=(10,4))
 r=np.linspace(0,4,401);v=np.ones_like(r);v[r>1]=1/r[r>1]
 axs[0].plot(r,v,color='#7c3aed',lw=2.5);axs[0].set(xlabel='r / R',ylabel='V / (kQ/R)',title='Potential is continuous')
 axs[1].plot([0,1],[0,0],color='#2563eb',lw=2.5);ro=np.linspace(1,4,300);axs[1].plot(ro,1/ro**2,color='#2563eb',lw=2.5)
 axs[1].scatter([1,1],[0,1],s=40,facecolors='none',edgecolors='#2563eb',zorder=4)
 axs[1].set(xlabel='r / R',ylabel='Eᵣ / (kQ/R²)',title='Field jumps across surface charge')
 for ax in axs:
  ax.axvline(1,color='#888',ls='--',alpha=.5);ax.set(xlim=(0,4),ylim=(-.05,1.18));ax.spines[['top','right']].set_visible(False)
  ax.text(.48,1.08,'inside',ha='center');ax.text(2.5,1.08,'outside',ha='center')
 fig.tight_layout();save(fig,'electric-potential-sphere.svg')
def verify():
 like=[(1,[-1,0]),(1,[1,0])];dipole=[(1,[-1,0]),(-1,[1,0])]
 assert potential([0,0],like)==2 and np.linalg.norm(field([0,0],like))==0
 assert potential([0,0],dipole)==0 and np.allclose(field([0,0],dipole),[2,0])
 # Independent finite differences of potential recover both field components.
 for p in [np.array([.2,.7]),np.array([2.,1.])]:
  grad=np.array([(potential(p+1e-5*d,dipole)-potential(p-1e-5*d,dipole))/2e-5 for d in np.eye(2)])
  assert np.allclose(-grad,field(p,dipole),rtol=1e-8)
 # Line integrals over independently parameterised paths: straight and sine detour.
 for h in [0,.8,2.]:
  val=quad(lambda t: np.dot(field([1+t,h*np.sin(np.pi*t)],[(1,[0,0])]),[1,h*np.pi*np.cos(np.pi*t)]),0,1,epsabs=1e-12)[0]
  assert abs(val-.5)<1e-11
 # AP 2024 rod integral, derivative, far-field limit.
 for x in [4.1,7,100]:
  numeric=quad(lambda s:1/(x-s),0,4)[0];analytic=np.log(x/(x-4));assert np.isclose(numeric,analytic)
  h=1e-5;dv=(np.log((x+h)/(x+h-4))-np.log((x-h)/(x-h-4)))/(2*h)
  assert np.isclose(-dv,4/(x*(x-4)),rtol=1e-6)
 # Bisector integral and ring are independently quadrature-checked.
 for a,y in [(1,.2),(1,2),(3,1)]:assert np.isclose(quad(lambda s:1/np.sqrt(s*s+y*y),-a,a)[0],2*np.arcsinh(a/y))
 assert np.isclose(quad(lambda theta:1/np.sqrt(2**2+3**2),0,2*np.pi)[0],2*np.pi/np.sqrt(13))
 kin=5000*E;nr=np.sqrt(2*kin/M);gamma=1+kin/(M*C*C);rel=C*np.sqrt(1-gamma**-2)
 # AP 2003 electron: direct force-work equals potential-energy decrease.
 assert np.isclose(quad(lambda r:-1/r**2,3,1)[0],1-1/3)
 pairs=np.array([2e-9,2e-9,-1e-9]);u=sum(K*pairs[i]*pairs[j]/.2 for i in range(3) for j in range(i+1,3));assert abs(u)<1e-22
 # Hands-on midpoint discretisation must converge toward quadrature result.
 errors=[]
 for n in [100,1000,10000]:
  t=np.linspace(0,1,n+1);p=np.column_stack([1+t,.8*np.sin(np.pi*t)]);value=np.sum(field((p[1:]+p[:-1])/2,[(1,[0,0])])*np.diff(p,axis=0));errors.append(abs(value-.5))
 assert errors[2]<errors[1]<errors[0]
 # Companion M7: varying-resistivity integral, constant cross-section.
 for alpha in [-.5,0,2]:assert np.isclose(quad(lambda x:3*(1+alpha*x/2)/4,0,2)[0],3*2/4*(1+alpha/2))
 print(f'PASS: signs, gradients, 3 routes, rod/ring/bisector quadrature, assembly, AP electron, hands-on convergence; 5keV speeds {nr:.6g} / {rel:.6g} m/s')
if __name__=='__main__':verify();figures()
