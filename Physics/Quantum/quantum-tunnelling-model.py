"""Finite-barrier scattering and split-step evolution. Units hbar=m=1.
Run directly for independent boundary/flux and grid-convergence checks.
The Gaussian is a packet with an energy spread, not a monoenergetic state.
"""
import numpy as np
from scipy.constants import hbar, electron_mass, elementary_charge


def transmission(E, V=3., a=1.):
    E = np.asarray(E, dtype=float)
    # E=V limit avoids the removable 0/0 singularity.
    d = V-E
    s = np.empty_like(E)
    below, above = d > 1e-10, d < -1e-10
    s[below] = np.sinh(np.sqrt(2*d[below])*a)**2/d[below]
    s[above] = np.sin(np.sqrt(-2*d[above])*a)**2/(-d[above])
    s[~(below | above)] = 2*a*a
    return np.divide(4*E, 4*E+V*V*s, out=np.zeros_like(E), where=E>0)


def match(E=2., V=3., a=1.):
    """Solve four boundary equations for r,C,D,t; barrier is 0<x<a."""
    k, kap = np.sqrt(2*E), np.sqrt(2*(V-E))
    p, q, z = np.exp(kap*a), np.exp(-kap*a), np.exp(1j*k*a)
    M = np.array([[1,-1,-1,0],[-1j*k,-kap,kap,0],
                  [0,p,q,-z],[0,kap*p,-kap*q,-1j*k*z]],complex)
    r,C,D,t = np.linalg.solve(M, np.array([-1,-1j*k,0,0]))
    return r,C,D,t


def stationary(x, E=2., V=3., a=1.):
    r,C,D,t = match(E,V,a)
    k,kap = np.sqrt(2*E),np.sqrt(2*(V-E))
    x=np.asarray(x)
    phi=np.empty(x.shape,complex); der=phi.copy()
    l,b,h=x<0,(x>=0)&(x<=a),x>a
    phi[l]=np.exp(1j*k*x[l])+r*np.exp(-1j*k*x[l])
    der[l]=1j*k*(np.exp(1j*k*x[l])-r*np.exp(-1j*k*x[l]))
    phi[b]=C*np.exp(kap*x[b])+D*np.exp(-kap*x[b])
    der[b]=kap*(C*np.exp(kap*x[b])-D*np.exp(-kap*x[b]))
    phi[h]=t*np.exp(1j*k*x[h]);der[h]=1j*k*phi[h]
    return phi,der


def packet(dx=.05,dt=.0025,end=36.,sample=.1):
    n=round(204.8/dx)
    x=(np.arange(n)-n/2+.5)*dx
    k=2*np.pi*np.fft.fftfreq(n,dx)
    V=np.where(np.abs(x)<.5,3.,0.)
    psi=np.exp(-(x+30)**2/(4*6**2)+2j*x)
    psi/=np.sqrt(np.sum(abs(psi)**2)*dx)
    # Symmetric Strang splitting: V/2 -> kinetic -> V/2.
    pv=np.exp(-.5j*V*dt);pk=np.exp(-.5j*k*k*dt)
    steps=round(end/dt);stride=round(sample/dt)
    ts=[];dens=[];energies=[];probs=[]
    spec=abs(np.fft.fft(psi))**2;spec/=spec.sum()
    weighted=float(np.sum(spec*transmission(k*k/2)))
    tail=float(spec[k*k/2>3].sum())
    for j in range(steps+1):
        if j%stride==0:
            rho=abs(psi)**2
            ts.append(j*dt);dens.append(rho)
            probs.append([rho[x<-.5].sum()*dx,rho[abs(x)<.5].sum()*dx,rho[x>.5].sum()*dx])
            Hpsi=np.fft.ifft(.5*k*k*np.fft.fft(psi))+V*psi
            energies.append(float(np.vdot(psi,Hpsi).real*dx))
        if j<steps: psi=pv*np.fft.ifft(pk*np.fft.fft(pv*psi))
    return dict(x=x,time=np.array(ts),density=np.array(dens),probability=np.array(probs),energy=np.array(energies),weighted_T=weighted,above_barrier_tail=tail)


def verify():
    worst=0.
    for E in [.2,.8,1.5,2.,2.8]:
        for a in [.2,.5,1.,2.]:
            r,C,D,t=match(E,3.,a)
            T=float(transmission(E,3.,a))
            assert abs(abs(t)**2-T)<1e-12
            assert abs(abs(r)**2+T-1)<1e-12
            x=np.linspace(-2,a+2,1001);phi,der=stationary(x,E,3.,a)
            err=np.max(abs(np.imag(phi.conj()*der)-np.sqrt(2*E)*T));worst=max(worst,err)
            assert err<1e-11
    print('Boundary solution vs closed form; R+T; constant current: PASS; max flux error',worst)
    runs=[]
    for dx,dt in [(.1,.005),(.05,.0025),(.025,.00025)]:
        d=packet(dx,dt);runs.append(d)
        normerr=np.max(abs(d['probability'].sum(axis=1)-1))
        energyerr=np.max(abs(d['energy']-d['energy'][0]))
        err=abs(d['probability'][-1,2]-d['weighted_T'])
        print('dx,dt,Tpacket,Tweighted,error,normerr,energyerr:',dx,dt,d['probability'][-1,2],d['weighted_T'],err,normerr,energyerr)
        assert normerr<1e-10 and energyerr<.006
    assert abs(runs[-1]['probability'][-1,2]-runs[-1]['weighted_T'])<.001
    print('Above-barrier spectral probability:',runs[1]['above_barrier_tail'])
    print('Final left,barrier,right:',runs[1]['probability'][-1])
    kappa=np.sqrt(2*electron_mass*elementary_charge)/hbar
    for a_nm in [.5,1.]:
        T=1/(1+4*np.sinh(kappa*a_nm*1e-9)**2/4)
        print('Electron: E=1eV V=2eV; a_nm,kappa_nm,T:',a_nm,kappa*1e-9,T)
    return runs[1]

if __name__=='__main__': verify()
