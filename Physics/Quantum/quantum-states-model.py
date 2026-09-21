"""Exact infinite-well model. xi=x/L; tau=E1*t/hbar; densities are L*|psi|².
Run directly for quadrature, finite-difference and sampling checks. NumPy/SciPy.
"""
import numpy as np
from scipy.integrate import simpson
from scipy.linalg import eigh_tridiagonal
H=6.62607015e-34
HBAR=H/(2*np.pi)
M_E=9.1093837139e-31
EV=1.602176634e-19
C=299792458.

def phi(xi,n):
    return np.sqrt(2)*np.sin(n*np.pi*np.asarray(xi))

def psi(xi,tau,coeff=(1/np.sqrt(2),1/np.sqrt(2))):
    return sum(c*phi(xi,n)*np.exp(-1j*n*n*tau) for n,c in enumerate(coeff,1))

def density(xi,tau,kind='coherent'):
    if kind=='stationary':return np.abs(psi(xi,tau,(1,)))**2
    if kind=='mixture':return .5*(phi(xi,1)**2+phi(xi,2)**2)
    if kind=='coherent':return np.abs(psi(xi,tau))**2
    raise ValueError(kind)

def left_probability(tau):return .5+4/(3*np.pi)*np.cos(3*tau)
def mean_position(tau):return .5-16/(9*np.pi**2)*np.cos(3*tau)
def energy_ev(n=1,L=1e-9,m=M_E):return n*n*H*H/(8*m*L*L*EV)

def sample_positions(tau,count=12000,seed=804):
    """Discrete-grid inverse CDF approximation to identically prepared measurements."""
    x=np.linspace(0,1,20001);pdf=density(x,tau);cdf=np.cumsum(pdf);cdf/=cdf[-1]
    return np.interp(np.random.default_rng(seed).random(count),cdf,x)

def verify():
    x=np.linspace(0,1,20001);left=x<=.5
    for n in range(1,5):
        assert abs(simpson(phi(x,n)**2,x=x)-1)<1e-12
        assert abs(phi(0,n))<1e-12 and abs(phi(1,n))<1e-12
        for m in range(1,n):assert abs(simpson(phi(x,n)*phi(x,m),x=x))<1e-12
    for tau in np.linspace(0,2*np.pi,41):
        for kind in ['stationary','coherent','mixture']:
            rho=density(x,tau,kind);assert rho.min()>-1e-14
            assert abs(simpson(rho,x=x)-1)<1e-12
        assert abs(simpson(density(x,tau)[left],x=x[left])-left_probability(tau))<1e-11
        assert abs(simpson(x*density(x,tau),x=x)-mean_position(tau))<1e-11
        # An independent expanded-density identity, including the interference term.
        expanded=.5*(phi(x,1)**2+phi(x,2)**2)+phi(x,1)*phi(x,2)*np.cos(3*tau)
        assert np.max(abs(expanded-density(x,tau)))<1e-12
    # Differential equation i*dpsi/dtau=-(1/pi²)*d²psi/dxi², checked numerically.
    dx=1e-4;dt=1e-5;z=np.linspace(.01,.99,211);t=.37
    residual=1j*(psi(z,t+dt)-psi(z,t-dt))/(2*dt)+(psi(z+dx,t)-2*psi(z,t)+psi(z-dx,t))/(dx*dx*np.pi**2)
    assert np.max(abs(residual))<4e-7
    # Independent discrete Hamiltonian eigenvalues converge to 1,4,9,16.
    errors=[]
    for N in [300,600]:
        h=1/(N+1);d=np.full(N,2/(np.pi*h)**2);e=np.full(N-1,-1/(np.pi*h)**2)
        vals=eigh_tridiagonal(d,e,select='i',select_range=(0,3),eigvals_only=True)
        errors.append(np.max(abs(vals-np.arange(1,5)**2)))
    assert errors[1]<errors[0]/3.9
    for t in [0,np.pi/6,np.pi/3]:
        freq=np.mean(sample_positions(t)<.5);p=left_probability(t)
        assert abs(freq-p)<5*np.sqrt(p*(1-p)/12000)
    # Gaussian uncertainty checked by direct quadrature of the state and derivative.
    for sigma in [.3,1.,2.]:
        z=np.linspace(-10*sigma,10*sigma,20001)
        g=(2*np.pi*sigma*sigma)**(-.25)*np.exp(-z*z/(4*sigma*sigma))
        dg=-z*g/(2*sigma*sigma)
        dx2=simpson(z*z*g*g,x=z);dp2_over_hbar2=simpson(dg*dg,x=z)
        assert abs(np.sqrt(dx2*dp2_over_hbar2)-.5)<1e-12
    print('PASS: normalization, orthogonality, boundaries, evolving density, interval probability, mean position, numerical Schrödinger residual, independent eigenvalue convergence, Gaussian uncertainty, sampling.')
    print('1 nm electron: E1=',energy_ev(),'eV; gap=',3*energy_ev(),'eV; photon wavelength=',H*C/(3*energy_ev()*EV)*1e9,'nm')
    print('Left probabilities:',[left_probability(t) for t in [0,np.pi/6,np.pi/3]])
    print('Finite-difference eigenvalue errors:',errors)
if __name__=='__main__':verify()
