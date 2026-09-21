"""Every number quoted in [[Special Relativity]], computed.

Run:  python3 special-relativity-model.py        (numpy only)
"""
import numpy as np

c = 299_792_458.0
gamma = lambda b: 1 / np.sqrt(1 - b * b)


def gammas():
    print("== the Lorentz factor ==")
    rows = [("walking, 1.5 m/s", 1.5 / c), ("airliner, 250 m/s", 250 / c), ("ISS, 7.66 km/s", 7660 / c), ("GPS satellite, 3.87 km/s", 3874 / c),
            ("0.1c", 0.1), ("0.5c", 0.5), ("0.6c", 0.6), ("0.8c", 0.8), ("0.866c", np.sqrt(3) / 2), ("0.9c", 0.9), ("0.99c", 0.99),
            ("0.995c (the 1963 muons)", 0.995), ("0.999c", 0.999)]
    for name, b in rows:
        g = gamma(b)
        print(f"   {name:28s} gamma = {g:.12g}   gamma - 1 = {g - 1:.3e}")
    b = 250 / c
    print(f"   airliner: a clock loses {(gamma(b) - 1) * 3600 * 1e9:.3f} ns per hour of flight")
    b = 7660 / c
    print(f"   ISS: {(gamma(b) - 1) * 86400 * 365.25 * 1e3:.2f} ms per year (special relativity alone); six months: {(gamma(b)-1)*86400*182.6*1e3:.2f} ms")


def light_clock():
    print("\n== the light clock at 0.6c ==")
    b = 0.6
    print(f"   gamma = {gamma(b)}; the clock at rest ticks 5 times while the moving one ticks {5 / gamma(b):.0f}")
    L = 0.15
    print(f"   a 15 cm clock ticks every {2 * L / c * 1e9:.3f} ns at rest and every {gamma(b) * 2 * L / c * 1e9:.3f} ns when it moves at 0.6c")


def muons():
    print("\n== muons ==")
    tau = 2.197e-6
    print(f"   mean lifetime {tau*1e6} microseconds; at c it would cover {c * tau:.0f} m in one lifetime")
    b = 0.995; g = gamma(b); h = 1907.0
    t_earth = h / (b * c); t_muon = t_earth / g
    print(f"   Frisch and Smith: 1907 m at 0.995c takes {t_earth*1e6:.2f} microseconds on the ground's clocks = {t_earth/tau:.2f} lifetimes")
    print(f"   gamma = {g:.2f}, so the muon ages {t_muon*1e6:.3f} microseconds = {t_muon/tau:.3f} lifetimes")
    print(f"   surviving fraction: no relativity {np.exp(-t_earth/tau):.4f}  ->  of 565 per hour, {565*np.exp(-t_earth/tau):.0f} would arrive")
    print(f"   surviving fraction: with relativity {np.exp(-t_muon/tau):.4f} ->  of 565 per hour, {565*np.exp(-t_muon/tau):.0f} would arrive (they counted 409)")
    print(f"   measured 409/565 = {409/565:.4f} -> time elapsed for the muons {-np.log(409/565)*tau*1e6:.3f} microseconds -> factor {t_earth/(-np.log(409/565)*tau):.1f}")
    print(f"   in the muon's frame the mountain is {h/g:.0f} m tall and rushes past in {h/g/(b*c)*1e6:.3f} microseconds")
    h = 15000.0; b = 0.999; g = gamma(b)
    print(f"   from 15 km at 0.999c: gamma {g:.1f}; without relativity {np.exp(-h/(b*c)/tau):.2e} survive; with it {np.exp(-h/(b*c)/g/tau):.3f}; atmosphere is {h/g:.0f} m thick to the muon")


def simultaneity():
    print("\n== the train: two lightning strikes ==")
    b = 0.6; g = gamma(b); L0 = 300.0          # proper length of the train, metres
    print(f"   train 300 m long in its own frame, moving at 0.6c; on the platform it measures {L0/g:.0f} m")
    # platform frame S: strikes at t=0 at x=0 (rear) and x=L0/g (front).  Train frame S': t' = g (t - v x / c^2)
    x_front = L0 / g
    t_rear = g * (0 - b * 0 / c); t_front = g * (0 - b * x_front / c)
    print(f"   simultaneous on the platform (t = 0 for both); on the train: rear t' = {t_rear*1e6:.3f}, front t' = {t_front*1e6:.3f} microseconds")
    print(f"   so on the train the FRONT strike happens first, by {abs(t_front)*1e6:.2f} microseconds = v L0 / c^2 = {b*L0/c*1e6:.2f}")


def lorentz_example():
    print("\n== a Lorentz transformation, and the invariant interval ==")
    b = 0.6; g = gamma(b)
    x, t = 3.0, 5.0                             # light-seconds and seconds, so c = 1
    xp = g * (x - b * t); tp = g * (t - b * x)
    print(f"   v = 0.6c, gamma = {g}; event (x = 3 light-seconds, t = 5 s) -> x' = {xp:.4f} light-seconds, t' = {tp:.4f} s")
    print(f"   (c t)^2 - x^2 = {t*t - x*x:.4f}   (c t')^2 - x'^2 = {tp*tp - xp*xp:.4f}   both in light-seconds squared")
    x, t = 5.0, 4.0
    xp = g * (x - b * t); tp = g * (t - b * x)
    print(f"   a second event (x = 5, t = 4) -> x' = {xp:.4f}, t' = {tp:.4f}; interval squared {t*t-x*x:.4f} and {tp*tp-xp*xp:.4f} (negative: space-like)")


def velocities():
    print("\n== adding velocities ==")
    add = lambda u, v: (u + v) / (1 + u * v)
    for u, v in [(0.6, 0.6), (0.9, 0.9), (0.5, 1.0), (1e-6, 1e-6)]:
        print(f"   {u}c and {v}c -> {add(u, v):.12g}c   (plain sum {u+v}c)")
    print(f"   IB form u' = (u - v)/(1 - uv/c^2): u = 0.8c, v = -0.6c -> u' = {(0.8+0.6)/(1+0.48):.4f}c")


def twins():
    print("\n== the twins ==")
    b = 0.8; g = gamma(b); d = 4.0
    print(f"   4 light-years at 0.8c: {2*d/b:.0f} years on Earth, {2*d/b/g:.0f} years for the traveller; gamma = {g:.4f}")


def energy():
    print("\n== energy ==")
    me, mp = 9.1093837e-31, 1.67262192e-27; eV = 1.602176634e-19
    print(f"   electron rest energy {me*c*c/eV/1e6:.4f} MeV; proton {mp*c*c/eV/1e6:.2f} MeV")
    print(f"   1 g of mass = {1e-3*c*c:.3e} J = {1e-3*c*c/4.184e12:.1f} kilotonnes of TNT")
    for b in (0.1, 0.5, 0.9, 0.99):
        print(f"   v = {b}c: (gamma-1) m c^2 is {(gamma(b)-1)/(0.5*b*b):.4f} times (1/2) m v^2")
    E = 6.8e12 * eV; g = E / (mp * c * c)
    print(f"   LHC proton at 6.8 TeV: gamma = {g:.0f}; c - v = {c * (1 - np.sqrt(1 - 1/g**2)):.2f} m/s")
    Msun_loss = 3.828e26 / (c * c)
    print(f"   the Sun radiates 3.828e26 W, so it loses {Msun_loss:.3e} kg every second")


def gps():
    print("\n== GPS ==")
    GM, RE, r = 3.986004418e14, 6.371e6, 2.656e7
    v = np.sqrt(GM / r)
    sr = -(v * v / (2 * c * c)) * 86400 * 1e6
    gr = (GM / (c * c)) * (1 / RE - 1 / r) * 86400 * 1e6
    print(f"   orbital speed {v:.0f} m/s; special relativity {sr:.2f}, gravity {gr:+.2f}, net {sr+gr:+.2f} microseconds per day")
    print(f"   left uncorrected, {abs(sr+gr)*1e-6*c/1000:.1f} km of ranging error per day")


if __name__ == "__main__":
    gammas(); light_clock(); muons(); simultaneity(); lorentz_example(); velocities(); twins(); energy(); gps()
