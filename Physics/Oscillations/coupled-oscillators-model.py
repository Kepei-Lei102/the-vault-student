"""Exact linear equal-oscillator model; figures and video use these parameters.
Run directly to check analytic motion against an independent ODE integration.
"""
import numpy as np
M, K, C, A = 1.0, 4.0, 0.42, 0.4
WP, WM = np.sqrt(K/M), np.sqrt((K+2*C)/M)
SWAP = np.pi/(WM-WP)

def state(t, mode='mixed'):
    t = np.asarray(t)
    ap, am = (A, 0) if mode == 'plus' else ((0, A) if mode == 'minus' else (A/2, A/2))
    qp, qm = ap*np.cos(WP*t), am*np.cos(WM*t)
    vp, vm = -ap*WP*np.sin(WP*t), -am*WM*np.sin(WM*t)
    return qp+qm, qp-qm, vp+vm, vp-vm

def energies(t, mode='mixed'):
    x1,x2,v1,v2=state(t,mode)
    return .5*M*v1*v1+.5*K*x1*x1, .5*M*v2*v2+.5*K*x2*x2, .5*C*(x2-x1)**2

if __name__ == '__main__':
    from scipy.integrate import solve_ivp
    ts=np.linspace(0,2*SWAP,2001)
    def rhs(t,y):
        x1,x2,v1,v2=y
        return v1,v2,(-K*x1+C*(x2-x1))/M,(-K*x2+C*(x1-x2))/M
    for mode in ('plus','minus','mixed'):
        exact=np.array(state(ts,mode))
        sol=solve_ivp(rhs,(0,ts[-1]),exact[:,0],t_eval=ts,rtol=1e-11,atol=1e-13)
        err=np.max(np.abs(exact-sol.y)); E=sum(energies(ts,mode))
        assert err<2e-9 and np.ptp(E)<1e-12
        print(mode, 'ODE max error',format(err,'.3g'),'energy drift',format(np.ptp(E),'.3g'))
    print('omega+',WP,'omega-',WM,'first envelope handover',SWAP)
    print('handover state',state(SWAP),'energy stores',energies(SWAP))
    # General unequal case: mass-weighted orthogonality and residual.
    MM=np.diag([1.,2.]); KK=np.array([[4.42,-.42],[-.42,6.42]])
    from scipy.linalg import eigh
    vals,vec=eigh(KK,MM)
    assert np.allclose(vec.T@MM@vec,np.eye(2))
    assert np.allclose(KK@vec,MM@vec@np.diag(vals))
    print('unequal-mass eigenproblem: PASS',np.sqrt(vals))
