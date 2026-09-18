"""Regenerate figures and verify independent limits/numerics for Electric Field.
Run: MPLCONFIGDIR=/tmp/vault-mpl python3 electric-field-verify.py
"""
from pathlib import Path
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad, solve_ivp
HERE=Path(__file__).resolve().parent
K=8.9875517923e9; E_CHARGE=1.602176634e-19; MASS=9.11e-31
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'vault','font.size':12,'text.color':'#888','axes.labelcolor':'#888','xtick.color':'#888','ytick.color':'#888','axes.edgecolor':'#888'})
def field(point,sources):
    out=np.zeros(2)
    for q,r in sources:
        delta=np.asarray(point,dtype=float)-r;distance=np.linalg.norm(delta)
        if distance==0:raise ValueError('Point-source singularity')
        out+=K*q*delta/distance**3
    return out

def save(fig,name):
    p=HERE/name
    fig.savefig(p,transparent=True,metadata={'Date':None},bbox_inches='tight')
    s=p.read_text();s=re.sub(r'<svg[^>]*>',lambda m:re.sub(r'width="[^"]+"','width="100%"',re.sub(r' height="[^"]+"','',m.group())),s,count=1)
    p.write_text('\n'.join(line.rstrip() for line in s.splitlines())+'\n');plt.close(fig)

def figures():
    fig,axs=plt.subplots(1,2,figsize=(10,4.5))
    x=np.linspace(-2.5,2.5,160);y=np.linspace(-1.9,1.9,130);X,Y=np.meshgrid(x,y)
    for ax,sign,title in zip(axs,[-1,1],['+Q and -Q: fields add between','+Q and +Q: midpoint cancellation']):
        ex=np.zeros_like(X);ey=np.zeros_like(Y);mask=np.zeros_like(X,dtype=bool)
        for charge,cx in [(1,-1),(sign,1)]:
            r2=(X-cx)**2+Y**2;mask|=r2<.12**2
            ex+=charge*(X-cx)/r2**1.5;ey+=charge*Y/r2**1.5
            ax.scatter([cx],[0],s=340,facecolor='#2563eb' if charge>0 else '#dc2626',alpha=.8,zorder=4)
        ex=np.ma.array(ex,mask=mask);ey=np.ma.array(ey,mask=mask)
        ax.streamplot(X,Y,ex,ey,density=.75,color='#0891b2',linewidth=.85,arrowsize=1.15)
        if sign==1:ax.scatter([0],[0],s=20,color='#059669',zorder=5)
        ax.set(xlim=(-2.5,2.5),ylim=(-1.9,1.9),aspect='equal');ax.axis('off');ax.set_title(title,fontsize=12,color='#888')
    fig.tight_layout();save(fig,'electric-field-patterns.svg')
    fig,ax=plt.subplots(figsize=(9,4.5))
    ax.plot([0,40],[10,10],color='#dc2626',lw=3);ax.plot([0,40],[-10,-10],color='#2563eb',lw=3)
    for xx in np.linspace(2,38,10):ax.annotate('',xy=(xx,-8),xytext=(xx,8),arrowprops={'arrowstyle':'->','color':'#0891b2','alpha':.4})
    xx=np.linspace(0,40,250);a=E_CHARGE*1e4/MASS
    yy=.5*a*(xx/1000/2e7)**2*1000
    ax.plot(xx,yy,color='#059669',lw=2.8);ax.scatter(np.linspace(0,40,9),.5*a*(np.linspace(0,40,9)/1000/2e7)**2*1000,color='#059669',s=25)
    ax.annotate('electron path',xy=(25,float(.5*a*(.025/2e7)**2*1000)),xytext=(17,6.5),color='#888',arrowprops={'arrowstyle':'->','color':'#888'})
    ax.text(20,11,'Positive plate',ha='center');ax.text(20,-12.8,'Negative plate',ha='center')
    ax.text(1,-7,'E downward; force on electron upward',fontsize=12)
    ax.set(xlim=(-2,43),ylim=(-14,14),xlabel='Horizontal distance / mm',ylabel='Vertical displacement / mm')
    ax.spines[['top','right']].set_visible(False);fig.tight_layout();save(fig,'electric-field-motion.svg')

def verify():
    src=[(4e-9,np.array([0.,0.])),(1e-9,np.array([.3,0.]))]
    assert np.linalg.norm(field([.2,0],src))<1e-10
    assert field([.2,.01],src)[1]>0
    # Unlike charges: external null lies past the weaker source, at x=.60 m.
    src[1]=(-1e-9,np.array([.3,0.]))
    assert np.linalg.norm(field([.6,0],src))<1e-10
    for q1,q2 in [(4e-9,-1e-9),(2e-8,3e-8)]:
        a=q2*field([.3,.2],[(q1,np.array([0.,0.]))]);b=q1*field([0,0],[(q2,np.array([.3,.2]))]);assert np.allclose(a,-b,rtol=1e-12,atol=1e-20)
    helium=K*2*E_CHARGE**2/(170e-12)**2;assert np.isclose(helium,1.6e-8,rtol=.002)
    tension=K*(6e-8)**2/(.057**2*np.sin(np.deg2rad(12)));assert np.isclose(tension,.048,rtol=.004)
    # Numerical ODE independent of the analytic trajectory; energy-work check.
    a=E_CHARGE*1e4/MASS;t=.04/2e7
    sol=solve_ivp(lambda t,z:[z[2],z[3],0,a],(0,t),[0,0,2e7,0],rtol=1e-11,atol=1e-13)
    x,y,vx,vy=sol.y[:,-1];assert np.isclose(y,.5*a*t*t,rtol=1e-10)
    assert np.isclose(.5*MASS*(vx*vx+vy*vy-(2e7)**2),E_CHARGE*1e4*y,rtol=1e-10)
    assert y<.01
    # Continuous-source quadrature at several aspect ratios vs derived expression.
    for aa,yy in [(.2,.05),(.2,2.),(2.,.01)]:
        val=quad(lambda x:yy/(x*x+yy*yy)**1.5,-aa,aa,epsabs=1e-10)[0]
        exact=2*aa/(yy*np.sqrt(aa*aa+yy*yy));assert np.isclose(val,exact,rtol=1e-10)
    print(f'PASS: nulls, Newton III, helium F={helium:.6g} N, AP T={tension:.6g} N, electron y={y*1000:.6g} mm, ODE/work, line integrals')
if __name__=='__main__':
    verify();figures()
