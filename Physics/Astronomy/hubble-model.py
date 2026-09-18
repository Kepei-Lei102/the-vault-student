"""Reproducible teaching models, not a fit to observed cosmological data.
Run: python3 hubble-model.py
"""
import math
import numpy as np
C=299792458.0
MPC=3.085677581491367e22
YEAR=365.25*86400

def hubble_si(km_s_mpc):
    if not math.isfinite(km_s_mpc) or km_s_mpc<=0: raise ValueError('H must be finite and positive')
    return km_s_mpc*1000/MPC

def relative_flow(points,observer,a,da):
    """Fixed comoving coordinates; proper positions a*q, velocities da*q."""
    q=np.asarray(points,float)-np.asarray(observer,float)
    return a*q,da*q

def through_origin(d,v):
    d=np.asarray(d,float);v=np.asarray(v,float)
    if d.shape!=v.shape or d.ndim!=1 or not np.all(np.isfinite(d)) or not np.all(np.isfinite(v)) or np.dot(d,d)==0:
        raise ValueError('finite paired 1D data with nonzero distances required')
    return np.dot(d,v)/np.dot(d,d)

def flat_matter_lambda_age(h,om):
    """Analytic age for flat matter+Lambda, radiation neglected; 0<Omega_m<=1."""
    if not (math.isfinite(h) and h>0 and 0<om<=1):raise ValueError('invalid model parameters')
    if om==1:return 2/(3*h)
    ol=1-om
    return 2/(3*h*math.sqrt(ol))*math.asinh(math.sqrt(ol/om))

def check():
    rng=np.random.default_rng(173)
    for _ in range(100):
        q=rng.normal(size=(30,3));obs=rng.normal(size=3);a=rng.uniform(.2,3);da=rng.uniform(.01,2)
        r,v=relative_flow(q,obs,a,da)
        assert np.allclose(v,(da/a)*r)
        assert math.isclose(through_origin(np.linalg.norm(r,axis=1),np.linalg.norm(v,axis=1)),da/a)
    h=hubble_si(70)
    d=np.array([20,40,60,80,100.]);v=70*d
    assert math.isclose(through_origin(d,v),70)
    assert math.isclose(through_origin(1.1*d,v),70/1.1)
    assert math.isclose(np.polyfit(np.log10(d),np.log10(v),1)[0],1)
    assert math.isclose(10**np.polyfit(np.log10(d),np.log10(v),1)[1],70)
    # Independent quadrature for flat matter+Lambda: a=u^2 removes endpoint singularity.
    u=np.linspace(0,1,200001)
    for om in [.1,.3,.7,1.]:
        numeric=np.trapezoid(2*u*u/np.sqrt(om+(1-om)*u**6),u)/h
        assert math.isclose(numeric,flat_matter_lambda_age(h,om),rel_tol=1e-9)
    for bad in [0,-1,float('nan'),float('inf')]:
        try:hubble_si(bad)
        except ValueError:pass
        else:raise AssertionError('bad H accepted')
    print('100 observer changes: invariant v=Hr; fit/calibration/log-axis checks pass.')
    print(f'H(70)={h:.9g} s^-1; Hubble time={1/h/YEAR/1e9:.5f} Gyr')
    print(f'Flat matter-only age={flat_matter_lambda_age(h,1)/YEAR/1e9:.5f} Gyr')
    print(f'Flat matter+Lambda (Omega_m=.3) age={flat_matter_lambda_age(h,.3)/YEAR/1e9:.5f} Gyr')
    print('Analytic ages agree with independent quadrature for four densities.')
if __name__=='__main__':check()
