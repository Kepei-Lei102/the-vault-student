"""Runnable teaching checks: python3 ultrasound-model.py. SI units throughout.
Ideal plane-wave normal incidence, real positive impedances, no interface loss.
Intensity attenuation coefficient mu, NOT pressure-amplitude attenuation.
"""
from math import exp, log, isclose

def reflection(z1,z2):
 if min(z1,z2)<=0:raise ValueError('Impedances must be positive')
 return ((z2-z1)/(z2+z1))**2

def depth(time,speed=1540):return speed*time/2

def echo_fraction(z1,z2,mu,d):return reflection(z1,z2)*exp(-2*mu*d)

def run():
 z1,z2=1100*1600,1900*4100
 print(f'March 2025 Q4(d)(ii): transmitted = {100*(1-reflection(z1,z2)):.3f}%')
 mu=-log(.62)/.021
 print(f'June 2025 Q10(c): mu = {mu:.6f} /m = {mu/100:.6f} /cm')
 print(f'Echo at 78 microseconds: depth = {depth(78e-6)*100:.3f} cm')
 for d in (.01,.03,.06):print(f'd={d*100:.0f} cm: echo/send={echo_fraction(1.5e6,1.8e6,mu,d):.6f}')
 # Conservation across interface derived independently from pressure transmission.
 for a,b in [(1,1),(1,3),(3,1),(400,1.5e6),(1.76e6,7.79e6)]:
  r=(b-a)/(a+b);tp=2*b/(a+b)
  assert isclose(r*r+tp*tp*a/b,1,abs_tol=1e-12)
  assert isclose(reflection(a,b),reflection(b,a))
 assert reflection(4,4)==0
 assert isclose(exp(-mu*.021),.62)
 assert isclose(exp(-mu*.042),.62**2)
 # Compare direct round-trip loss with two separately propagated legs.
 assert isclose(echo_fraction(1.5e6,1.8e6,mu,.03),exp(-mu*.03)*reflection(1.5e6,1.8e6)*exp(-mu*.03))
 assert isclose(depth(2*.06/1540),.06)
 # Integrate dI/dx=-mu I with independent small Euler steps.
 value=1.;dx=.021/20000
 for _ in range(20000):value-=mu*value*dx
 assert abs(value-.62)<1e-5
 print('All physical-consistency checks passed.')
if __name__=='__main__':run()
