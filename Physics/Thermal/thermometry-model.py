"""Illustrative sensor calibration and lumped thermal response; run with numpy."""
import numpy as np

def signals(celsius):
    t=np.asarray(celsius)
    return 10+.4*t, 100+.385*t, .04*t+.00008*t*(t-100)

def indicated(x, x0, x100):
    if x100 == x0: raise ValueError('Calibration span must be nonzero')
    return 100*(np.asarray(x)-x0)/(x100-x0)

def response(time, initial, bath, tau):
    if tau<=0: raise ValueError('Time constant must be positive')
    return bath+(initial-bath)*np.exp(-np.asarray(time)/tau)

def equilibrium(c_object,t_object,c_probe,t_probe):
    if min(c_object,c_probe)<=0: raise ValueError('Heat capacities must be positive')
    return (c_object*t_object+c_probe*t_probe)/(c_object+c_probe)

def check():
    for t in [0,100]:
        for x,x0,x100 in zip(signals(t),signals(0),signals(100)):
            assert np.isclose(indicated(x,x0,x100),t)
    assert np.isclose(indicated(signals(50)[2],0,4),45)
    ts=np.linspace(0,100,1001); emfs=signals(ts)[2]
    assert np.all(np.diff(emfs)>0)
    errors=indicated(emfs,0,4)-ts
    assert np.isclose(errors.min(),-5)
    for tau in [2,6,10]:
        assert np.isclose(response(tau,20,80,tau),80-60/np.e)
        # Independent forward integration, not reusing the analytic response.
        dt=tau/20000; y=20.
        for _ in range(20000): y+=dt*(80-y)/tau
        assert abs(y-response(tau,20,80,tau))<.001
    tf=equilibrium(4.2,60,.42,20)
    assert abs(4.2*(tf-60)+.42*(tf-20))<1e-12
    gas=273.15*(7.83-2.31)/(8.69-2.31)
    print(f'Calibration endpoints pass; curved sensor max error {errors.min():.1f} C.')
    print(f'Response checked against Euler integration; loading equilibrium={tf:.5f} C.')
    print(f'Exam gas thermometer: {gas:.5f} K, {gas-273.15:.5f} C.')

if __name__=='__main__': check()
