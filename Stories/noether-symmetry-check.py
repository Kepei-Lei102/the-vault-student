"""Noether's first theorem, checked by brute force: symmetry present, conservation holds; symmetry broken, it fails.

Run: python3 noether-symmetry-check.py
Two particles on a line, integrated with a fine step. Three worlds:
  A. the only force is between the two particles, V(x1 - x2): shifting both particles changes nothing (translation
     symmetry), and the total momentum should be conserved; V does not depend on t, and the energy should be too.
  B. add a hill under them, V_ext(x): the world now has a special place, translation symmetry is gone, and momentum
     drifts; energy is still conserved because nothing depends on the time.
  C. make the spring between them stiffen with time, k(t): no special place, so momentum is conserved; but the
     laws change with time, and energy is not.
Every number printed is the largest drift of the quantity over the run, relative to its starting size.
"""
import numpy as np
from scipy.integrate import solve_ivp

m1, m2 = 1.0, 2.0

def run(k_of_t, ext_force, ext_pot, T=20.0):
    def rhs(t, s):
        x1, x2, v1, v2 = s
        k = k_of_t(t); f = -k * (x1 - x2 - 1.0)          # spring between them, natural length 1
        return [v1, v2, (f + ext_force(x1)) / m1, (-f + ext_force(x2)) / m2]
    sol = solve_ivp(rhs, [0, T], [0.0, 1.3, 0.4, -0.1], rtol=1e-10, atol=1e-12, dense_output=True)
    t = np.linspace(0, T, 4001); x1, x2, v1, v2 = sol.sol(t)
    p = m1 * v1 + m2 * v2
    E = 0.5 * m1 * v1**2 + 0.5 * m2 * v2**2 + 0.5 * k_of_t(t) * (x1 - x2 - 1.0)**2 + ext_pot(x1) + ext_pot(x2)
    drift = lambda q: np.max(np.abs(q - q[0])) / max(abs(q[0]), 1e-12)
    return drift(p), drift(E)

worlds = {
    "A. spring only: no special place, no special time": (lambda t: 4.0, lambda x: 0.0, lambda x: 0.0 * x),
    "B. add a hill under them: a special place":         (lambda t: 4.0, lambda x: -0.6 * x, lambda x: 0.3 * x**2),
    "C. spring stiffens with time: a special time":      (lambda t: 4.0 + 0.8 * t, lambda x: 0.0, lambda x: 0.0 * x),
}
print(f"{'world':52s} {'momentum drift':>15s} {'energy drift':>13s}")
for name, (k, F, V) in worlds.items():
    dp, dE = run(k, F, V)
    print(f"{name:52s} {dp:15.1e} {dE:13.1e}")
print("\nA: both conserved to integration accuracy. B: momentum wanders, energy holds. C: energy wanders, momentum holds.")
print("Noether, 1918: each conserved quantity is a symmetry, and each symmetry a conserved quantity. The table is the theorem's fingerprint.")
