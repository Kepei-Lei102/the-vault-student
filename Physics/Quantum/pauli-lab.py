"""Ideal-fermion models for Pauli Exclusion Principle. Python 3, no dependencies.
Assumptions: noninteracting spin-1/2 particles; 1-D hard-wall well or a
large 3-D periodic box. All energies are kinetic energies.
"""
from math import pi, sqrt, exp, isclose

HBAR = 1.054571817e-34
M_E = 9.1093837139e-31
K_B = 1.380649e-23
EV = 1.602176634e-19
C = 299792458


def modes_1d(count):
    if not isinstance(count, int) or count < 0:
        raise ValueError('count must be a nonnegative integer')
    return [i // 2 + 1 for i in range(count)]


def energy_1d(count, width_ratio=1.0):
    """Energy in units of E1 at reference width L0."""
    if width_ratio <= 0:
        raise ValueError('width_ratio must be positive')
    return sum(j*j for j in modes_1d(count)) / width_ratio**2


def fermi_gas(density):
    """3-D, T=0, nonrelativistic ideal electrons, two spin states."""
    if density <= 0:
        raise ValueError('density must be positive')
    kf = (3*pi*pi*density)**(1/3)
    ef = HBAR**2*kf*kf/(2*M_E)
    return dict(kf=kf, ef=ef, tf=ef/K_B, pressure=2*density*ef/5,
                vf=HBAR*kf/M_E)


def fermi_occupation(energy_minus_mu, kbt):
    if kbt <= 0:
        raise ValueError('kbt must be positive')
    x = energy_minus_mu/kbt
    if x >= 0:
        z = exp(-x)
        return z/(1+z)
    return 1/(1+exp(x))


def count_periodic_states(radius):
    """Integer k-grid points inside radius, including both spin states."""
    r = int(radius)
    return 2*sum(x*x+y*y+z*z <= radius*radius
                 for x in range(-r, r+1) for y in range(-r, r+1)
                 for z in range(-r, r+1))


def verify():
    assert modes_1d(6) == [1, 1, 2, 2, 3, 3]
    assert energy_1d(6) == 28
    assert isclose(energy_1d(6, .8), 43.75)
    assert energy_1d(7)-energy_1d(6) == 16
    # At even N=2m, two particles occupy each mode; check exact sum.
    for m in range(1, 31):
        assert energy_1d(2*m) == m*(m+1)*(2*m+1)/3
    # Force from an independent finite difference of energy versus width.
    L, step = .9, 1e-6
    numerical_force = -(energy_1d(6,L+step)-energy_1d(6,L-step))/(2*step)
    assert isclose(numerical_force, 2*energy_1d(6,L)/L, rel_tol=1e-8)
    g = fermi_gas(8e28)
    assert isclose(g['ef']/EV, 6.770136, rel_tol=2e-5)
    assert g['vf']/C < .01
    assert isclose(fermi_gas(16e28)['pressure']/g['pressure'],2**(5/3))
    assert isclose(fermi_gas(16e28)['ef']/g['ef'],2**(2/3))
    # Derivative at fixed N: U=(3/5) N E_F(N/V).
    N, V, dv = 8e28, 1., 1e-5
    U = lambda v: .6*N*fermi_gas(N/v)['ef']
    pressure_fd = -(U(V+dv)-U(V-dv))/(2*dv)
    assert isclose(pressure_fd,g['pressure'],rel_tol=1e-8)
    assert fermi_occupation(0,.1) == .5
    for x in [.001,.1,1,20,1000]:
        assert isclose(fermi_occupation(x,.1)+fermi_occupation(-x,.1),1)
    # Compare a discrete count with volume approximation, without assuming
    # monotone convergence (lattice-shell errors oscillate).
    assert abs(count_periodic_states(20)/(2*4*pi*20**3/3)-1) < .005
    print('PASS: filling, compression force, pressure derivative, FD symmetry, 3-D count')


def main():
    verify()
    print('Six particles:',modes_1d(6),'U0 =',energy_1d(6),'U(0.8L0) =',energy_1d(6,.8))
    g=fermi_gas(8e28)
    print(f"kF = {g['kf']:.6g} /m; EF = {g['ef']/EV:.6g} eV")
    print(f"TF = {g['tf']:.6g} K; P = {g['pressure']:.6g} Pa; vF/c = {g['vf']/C:.6g}")
    for r in [5,10,20]:
        exact=count_periodic_states(r); approx=2*4*pi*r**3/3
        print(f'k-grid radius {r}: {exact} states; continuum {approx:.1f}; error {100*(exact/approx-1):+.3f}%')

if __name__ == '__main__':
    main()
