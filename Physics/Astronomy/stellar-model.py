"""Blackbody forward/inverse model. Run with Python + NumPy; SI throughout."""
import numpy as np
H=6.62607015e-34
C=299792458.
K=1.380649e-23
SIGMA=2*np.pi**5*K**4/(15*H**3*C**2)
B=2.897771955e-3
PC=648000/np.pi*149597870700.
def positive(*values):
    if any(np.any(~np.isfinite(v)) or np.any(np.asarray(v)<=0) for v in values):
        raise ValueError('Inputs must be finite and positive')
def spectrum(wavelength,temperature):
    """M_lambda: hemispherical surface exitance per metre, W m^-3."""
    w=np.asarray(wavelength,dtype=float);positive(w,temperature)
    x=H*C/(w*K*temperature)
    return 2*np.pi*H*C**2/w**5*np.exp(-x)/(-np.expm1(-x))
def luminosity(radius,temperature):
    positive(radius,temperature);return 4*np.pi*radius**2*SIGMA*temperature**4
def flux(radius,temperature,distance):
    positive(distance);return luminosity(radius,temperature)/(4*np.pi*distance**2)
def infer(peak,received,distance):
    positive(peak,received,distance)
    t=B/peak;l=4*np.pi*distance**2*received;r=np.sqrt(l/(4*np.pi*SIGMA*t**4))
    return t,l,r
def check():
    rng=np.random.default_rng(970225)
    for _ in range(1000):
        r=10**rng.uniform(6,11);t=10**rng.uniform(3,4.6);d=10**rng.uniform(15,23)
        rec=infer(B/t,flux(r,t,d),d)
        np.testing.assert_allclose(rec,[t,luminosity(r,t),r],rtol=1e-12)
        np.testing.assert_allclose(flux(2*r,t,2*d),flux(r,t,d),rtol=1e-12)
    for t in [300,3000,5800,10000,30000]:
        w=np.geomspace(B/t/1000,B/t*10000,150000)
        y=spectrum(w,t)
        integral=np.trapezoid(y,w)
        np.testing.assert_allclose(integral,SIGMA*t**4,rtol=2e-8)
        np.testing.assert_allclose(w[y.argmax()],B/t,rtol=1e-4)
        print('T',t,'peak nm',w[y.argmax()]*1e9,'integral / sigmaT4',integral/(SIGMA*t**4))
    # A grey screen transmitting 1/4 of all wavelengths biases inferred d by x2.
    l=luminosity(7e8,5800);f=l/(4*np.pi*(10*PC)**2)
    np.testing.assert_allclose(np.sqrt(l/(4*np.pi*(f/4))),20*PC)
    for bad in [0,-1,float('nan')]:
        try: infer(bad,1,1)
        except ValueError: pass
        else: raise AssertionError('invalid input accepted')
    print('Synthetic inference (T,L,R):',infer(500e-9,3.2e-10,20*PC))
    print('Sirius exam T:',(9.81e27/(4*np.pi*5.67e-8*(1.19e9)**2))**.25)
    print('Graph exam L,R:',4*np.pi*(6.4e3/3e-23),np.sqrt((4*np.pi*(6.4e3/3e-23))/(4*np.pi*5.67e-8*7000**4)))
    print('PASS: 1000 round trips and degeneracies, 5 integrated spectra, extinction, invalid inputs')
if __name__=='__main__':check()
