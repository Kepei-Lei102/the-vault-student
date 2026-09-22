"""Educational models, not a part model. Run with Python 3; no dependencies."""
from math import exp, log, isclose
from itertools import product
VDD, VIL, VIH = 3.3, 0.8, 2.0

def inverter(v):
    if not 0 <= v <= VDD:
        raise ValueError('This toy model only covers the supply range')
    if v <= VIL:
        return VDD - 0.2 * v / VIL
    if v >= VIH:
        return 0.2 * (VDD - v) / (VDD - VIH)
    return 3.1 - 2.9 * (v - VIL) / (VIH - VIL)

def logic(v):
    return 0 if 0 <= v <= VIL else 1 if VIH <= v <= VDD else None

def cmos_paths(a, b, kind):
    if kind == 'NAND':
        pull_down, pull_up = a and b, (not a) or (not b)
    elif kind == 'NOR':
        pull_down, pull_up = a or b, (not a) and (not b)
    else:
        raise ValueError(kind)
    assert pull_down != pull_up  # exactly one rail connected for valid bits
    return int(pull_up)

def charge(t, r=1000, c=10e-12, supply=VDD):
    return supply * (1 - exp(-t / (r * c)))

def check():
    # Verify contracts across 3301 inputs, not merely chosen rail examples.
    for i in range(3301):
        v = i / 1000
        if logic(v) is not None:
            assert logic(inverter(v)) == 1 - logic(v)
            assert logic(inverter(inverter(v))) == logic(v)
    for a, b in product((False, True), repeat=2):
        assert cmos_paths(a,b,'NAND') == int(not (a and b))
        assert cmos_paths(a,b,'NOR') == int(not (a or b))
    for boundary in (VIL, VIH):
        assert abs(inverter(boundary-1e-9)-inverter(boundary+1e-9)) < 1e-7
    assert logic(1.1) is None
    assert isclose(inverter(inverter(.65)), .025)
    r,c=1000,10e-12
    assert isclose(charge(r*c*log(2)), VDD/2)
    assert isclose(charge(-r*c*log(1-2/VDD)), 2)
    # Independent numerical energy integrals over 20 RC, trapezoidal rule.
    n=20000;dt=20*r*c/n
    supplied=stored_path=heat=0.0
    for i in range(n+1):
        v=charge(i*dt,r,c);current=(VDD-v)/r
        w=.5 if i in (0,n) else 1
        supplied+=w*VDD*current*dt
        stored_path+=w*v*current*dt
        heat+=w*r*current**2*dt
    assert isclose(supplied, c*VDD**2, rel_tol=1e-6)
    assert isclose(stored_path,.5*c*VDD**2,rel_tol=1e-6)
    assert isclose(heat,.5*c*VDD**2,rel_tol=1e-6)
    assert isclose(supplied,stored_path+heat,rel_tol=1e-12)
    print('PASS: voltage contracts, 8 transistor-network cases, RC thresholds and energy integrals')

if __name__ == '__main__':
    check()
    v=.65
    for stage in range(3):
        print(stage,round(v,4),logic(v));v=inverter(v)
    print('t50/ns',1000*10e-12*log(2)/1e-9)
    print('t to 2V/ns',-1000*10e-12*log(1-2/3.3)/1e-9)
    print('charge/pJ',10e-12*3.3**2/1e-12)
    print('load power/uW',.2*10e-12*3.3**2*10e6/1e-6)
