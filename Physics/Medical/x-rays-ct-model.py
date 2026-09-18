"""Exact pixel ray lengths, ideal parallel-beam CT. NumPy only.
Synthetic 12x12 phantom; monochromatic, noiseless baseline, no scatter.
Run from anywhere: python3 x-rays-ct-model.py. No patient data.
"""
import numpy as np
from pathlib import Path
N=12
EDGES=np.linspace(-1,1,N+1)
DETECTORS=np.linspace(-1.36,1.36,29)
def ray(theta,s):
    normal=np.array([np.cos(theta),np.sin(theta)])
    direction=np.array([-np.sin(theta),np.cos(theta)])
    origin=s*normal
    crossings=[]
    for axis in (0,1):
        if abs(direction[axis])>1e-10:
            crossings.extend((EDGES-origin[axis])/direction[axis])
    ts=np.unique(np.round(crossings,12)); weights=np.zeros((N,N))
    for lo,hi in zip(ts[:-1],ts[1:]):
        mid=origin+(lo+hi)/2*direction
        if np.all(mid>-1) and np.all(mid<1):
            j,i=np.floor((mid+1)*N/2).astype(int)
            weights[i,j]+=hi-lo
    return weights.ravel()
def phantom():
    q=(EDGES[:-1]+EDGES[1:])/2;x,y=np.meshgrid(q,q)
    f=np.zeros((N,N));f[(x/.85)**2+(y/.9)**2<1]=.18
    f[((x+.3)/.24)**2+((y-.25)/.27)**2<1]=.9
    f[((x-.3)/.19)**2+((y+.2)/.42)**2<1]=.55
    return f
ANGLES=np.linspace(0,np.pi,48,endpoint=False)
def system(angles=ANGLES):return np.stack([ray(a,s) for a in angles for s in DETECTORS])
def build():
    truth=phantom();A=system();b=A@truth.ravel()
    solutions={}
    for count in (2,4,8,16,48):
        ids=np.linspace(0,48,count,endpoint=False,dtype=int)
        rows=np.concatenate([np.arange(k*len(DETECTORS),(k+1)*len(DETECTORS)) for k in ids])
        solution,_,rank,_=np.linalg.lstsq(A[rows],b[rows],rcond=1e-10)
        solutions[count]=solution.reshape(N,N)
    return truth,A,b,solutions
if __name__=='__main__':
    from math import exp,log,isclose
    truth,A,b,solutions=build()
    assert np.all(A>=0)
    assert isclose(ray(0,0).sum(),2,abs_tol=1e-9)
    assert isclose(ray(np.pi/4,0).sum(),2*np.sqrt(2),abs_tol=1e-9)
    assert isclose(ray(np.pi/2,.2).sum(),2,abs_tol=1e-9)
    assert np.max(np.abs(np.sum(A,axis=1)))<=2*np.sqrt(2)+1e-9
    assert np.max(abs(solutions[48]-truth))<1e-9
    # Unmeasured angles: forward-predict from the reconstructed image.
    hold=system(np.array([.123,.789,1.234]));assert np.max(abs(hold@solutions[48].ravel()-hold@truth.ravel()))<1e-9
    # A different object tests data changes, not only the illustrated phantom.
    changed=np.arange(N*N,dtype=float).reshape(N,N)/(N*N)*.3
    recovered=np.linalg.lstsq(A,A@changed.ravel(),rcond=1e-10)[0]
    assert np.max(abs(recovered-changed.ravel()))<1e-9
    assert np.allclose(ray(.37,.21),ray(.37+np.pi,-.21),atol=1e-9)
    transmission=np.exp(-b);assert np.allclose(-np.log(transmission),b)
    # Real Cambridge question and original voltage/2x2 examples.
    small=np.array([[1,1,0,0],[0,0,1,1],[1,0,1,0],[0,1,0,1],[1,0,0,1]],float)
    assert np.linalg.matrix_rank(small[:4])==3 and np.linalg.matrix_rank(small)==4
    assert np.allclose(np.linalg.lstsq(small,[3,7,4,6,5],rcond=None)[0],[1,2,3,4])
    mu=(-log(.053)-.35*3.7)/2.1
    assert isclose(exp(-.35*5.8),.131335521,rel_tol=1e-7)
    print('2025 Q10(b): IB/I0=',exp(-.35*5.8),'mu_Q=',mu,'per cm')
    print('80 kV minimum wavelength:',6.62607015e-34*299792458/(1.602176634e-19*80000),'m')
    for n,f in solutions.items():print(n,'views: RMS error',np.sqrt(np.mean((f-truth)**2)))
    print('Ray geometry, log attenuation, reconstruction and held-out-angle checks passed.')
