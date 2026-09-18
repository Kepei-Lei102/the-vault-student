"""Ideal 2-D PET teaching model. NumPy only; no clinical data.
Line-integral projection bins with uniform total sensitivity per voxel.
Poisson counts, no attenuation/scatter/randoms, stationary emission sites,
and multiplicative Poisson maximum-likelihood (MLEM) reconstruction.
Run directly to check geometry, statistics, inference and numerical examples.
"""
import numpy as np
C = 299792458.0
ME = 9.1093837139e-31
EV = 1.602176634e-19


def chord(point, direction, radius=1.5):
    p=np.asarray(point,dtype=float); d=np.asarray(direction,dtype=float)
    d=d/np.linalg.norm(d)
    if np.dot(p,p)>=radius**2:raise ValueError('source must be inside ring')
    b=np.dot(p,d); root=np.sqrt(b*b+radius*radius-np.dot(p,p))
    return p+(-b-root)*d,p+(-b+root)*d


def line_weights(theta, offset, n=16):
    """Exact intersections of a parallel line with a square pixel grid [-1,1]^2."""
    normal=np.array([np.cos(theta),np.sin(theta)])
    direction=np.array([-np.sin(theta),np.cos(theta)])
    origin=offset*normal
    edges=np.linspace(-1,1,n+1)
    cuts=[]
    for axis in (0,1):
        if abs(direction[axis])>1e-12:
            cuts.extend((edges-origin[axis])/direction[axis])
    cuts=np.unique(np.round(cuts,12));w=np.zeros((n,n))
    for a,b in zip(cuts[:-1],cuts[1:]):
        point=origin+(a+b)/2*direction
        if np.all(point>-1) and np.all(point<1):
            ix,iy=np.floor((point+1)*n/2).astype(int)
            w[iy,ix]+=b-a
    return w.ravel()


def system(n=16, angles=36, channels=35):
    raw=np.stack([line_weights(t,s,n) for t in np.linspace(0,np.pi,angles,endpoint=False)
                  for s in np.linspace(-1.4,1.4,channels)])
    sensitivity=raw.sum(axis=0)
    assert np.all(sensitivity>0)
    # Teaching normalization: each voxel contributes one expected detected count
    # across all bins per unit x. It idealizes detector sensitivity, not attenuation.
    return raw/sensitivity


def phantom(n=16,shift=0.):
    v=-1+(np.arange(n)+.5)*2/n;x,y=np.meshgrid(v,v)
    f=.05*(x*x+y*y<.8**2)
    f+=np.exp(-((x+.32-shift)**2+(y-.25)**2)/.025)
    f+=.65*np.exp(-((x-.32-shift)**2+(y+.3)**2)/.05)
    return f/f.sum()


def reconstruct(A,counts,steps=80):
    x=np.full(A.shape[1],counts.sum()/A.shape[1])
    sensitivity=A.sum(axis=0)
    snapshots={};likelihood=[]
    for k in range(1,steps+1):
        expected=A@x
        ratio=np.divide(counts,expected,out=np.zeros_like(expected),where=expected>0)
        x*= (A.T@ratio)/sensitivity
        mu=A@x
        likelihood.append(float(np.sum(counts*np.log(np.maximum(mu,1e-300))-mu)))
        if k in (1,5,20,80):snapshots[k]=x.copy()
    return x,snapshots,np.array(likelihood)


def experiment(n=16,seed=17,total=30000,shift=0.):
    A=system(n);truth=phantom(n,shift).ravel()*total
    expected=A@truth;counts=np.random.default_rng(seed).poisson(expected).astype(float)
    answer,snapshots,ll=reconstruct(A,counts)
    return A,truth,counts,answer,snapshots,ll


def events(count=18,seed=17):
    rng=np.random.default_rng(seed);rho=phantom();indices=rng.choice(rho.size,count,p=rho.ravel())
    out=[]
    for ix in indices:
        y,x=divmod(int(ix),16);p=-1+(np.array([x,y])+.5)*2/16
        t=rng.uniform(0,np.pi);d=np.array([np.cos(t),np.sin(t)])
        left,right=chord(p,d)
        out.append((p,left,right))
    return out


def verify():
    rng=np.random.default_rng(92)
    for _ in range(1000):
        p=rng.uniform(-.7,.7,2);d=rng.normal(size=2);left,right=chord(p,d)
        assert np.isclose(np.linalg.norm(left),1.5) and np.isclose(np.linalg.norm(right),1.5)
        a,b=p-left,right-p
        assert np.isclose(a[0]*b[1]-a[1]*b[0],0,atol=1e-10)
        length=np.linalg.norm(right-left);dl=np.linalg.norm(p-left);dr=np.linalg.norm(right-p)
        assert np.isclose(dl+dr,length)
        dt=(dl-dr)/C
        assert np.isclose(C*dt/2,dl-length/2)
    assert np.isclose(line_weights(0,0).sum(),2)
    assert np.isclose(line_weights(np.pi/4,0).sum(),2*np.sqrt(2))
    assert np.isclose(line_weights(0,1.1).sum(),0)
    for n,seed,total,shift in [(16,17,30000,0),(12,99,9000,.15),(10,8,20000,-.12)]:
        A,t,y,x,s,ll=experiment(n,seed,total,shift)
        assert np.all(A>=0) and np.allclose(A.sum(axis=0),1)
        assert np.all(np.isfinite(x)) and np.all(x>=0)
        assert np.min(np.diff(ll))>-1e-7
        assert np.isclose(x.sum(),y.sum())
        rmse=lambda z:np.sqrt(np.mean((z/z.sum()-t/t.sum())**2))
        assert rmse(x)<rmse(np.ones_like(x))
        print('grid',n,'counts',int(y.sum()),'normalised RMSE',round(rmse(x),6),'uniform',round(rmse(np.ones_like(x)),6))
    A=system(8);zero,_,_=reconstruct(A,np.zeros(A.shape[0]),5);assert np.all(zero==0)
    e=ME*C*C
    print('One photon:',e,'J;',e/EV/1000,'keV')
    print('dt=200ps -> x=',C*200e-12/2,'m; 400ps FWHM ->',C*400e-12/2,'m FWHM')
    lam=np.log(2)/(2.04*60);N=2.85e-6/(15*1.66e-27)
    print('ON25/44 Q8:',lam,'s^-1;',lam*N,'positrons/s')
    print('PASS: 1000 chord/TOF cases, exact lengths, 3 changed reconstruction cases, likelihood monotonicity, zero counts.')


if __name__=='__main__':verify()
