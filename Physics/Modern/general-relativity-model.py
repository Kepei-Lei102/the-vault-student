"""Every number quoted in General Relativity.md, computed from constants.

Run:  python3 general-relativity-model.py
Weak-field formulas throughout, which is all the card uses: a clock deeper in a potential well by ΔΦ runs slow by
ΔΦ/c²; light passing a mass M at closest approach b is deflected by 2GM/(bc²) in Newton's picture and 4GM/(bc²) in
Einstein's; an orbit's perihelion advances by 6πGM/(a(1−e²)c²) per revolution. The Newtonian deflection is also
integrated numerically, to check the impulse argument the card makes by hand.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp

G, c = 6.674e-11, 2.998e8
M_sun, R_sun = 1.989e30, 6.957e8
M_E, R_E = 5.972e24, 6.371e6
g = G * M_E / R_E**2
day = 86400.0
arcsec = math.degrees(1) * 3600            # radians → arcseconds

print("== Gravitational time dilation, weak field: Δf/f = gh/c², Δτ/τ = ΔΦ/c²")
h_pr = 22.5                                   # Pound–Rebka tower, Harvard, 1959
print(f"Pound–Rebka, h = {h_pr} m: fractional shift {g*h_pr/c**2:.3e}   (measured 1960: (2.57 ± 0.26)e-15; 1965 Pound–Snider to 1%)")
print(f"One year at 1 m higher than your feet: head older by {g*1/c**2*365.25*day*1e9:.1f} ns")

print("\n== GPS")
r_gps = 26_562e3                              # semi-major axis of a GPS orbit
v_gps = math.sqrt(G * M_E / r_gps)
gr = (G*M_E/R_E - G*M_E/r_gps) / c**2 * day  # potential difference → seconds gained per day
sr = -(v_gps**2 / (2*c**2)) * day            # first-order time dilation, seconds lost per day
print(f"orbit r = {r_gps/1e3:.0f} km, v = {v_gps:.0f} m/s")
print(f"GR: satellite clock gains {gr*1e6:.1f} μs/day;  SR: loses {-sr*1e6:.1f} μs/day;  net {(gr+sr)*1e6:.1f} μs/day")
print(f"ranging error if uncorrected: {c*(gr+sr)/1e3:.1f} km per day")
f_shift = (gr + sr) / day
print(f"clocks set before launch to 10.23 MHz × (1 − {f_shift:.3e}) = {10.23e6*(1-f_shift):.5f} Hz")
r_cross = 1.5 * R_E
print(f"GR and SR cancel for a circular orbit at r = 1.5 R_E: altitude {(r_cross-R_E)/1e3:.0f} km")
r_iss = R_E + 420e3; v_iss = math.sqrt(G*M_E/r_iss)
print(f"ISS (420 km): GR +{(G*M_E/R_E - G*M_E/r_iss)/c**2*day*1e6:.1f} μs/day, SR −{v_iss**2/(2*c**2)*day*1e6:.1f} μs/day → net {((G*M_E/R_E - G*M_E/r_iss)/c**2 - v_iss**2/(2*c**2))*day*1e6:.1f} μs/day (astronauts age slower)")

print("\n== Hafele–Keating 1971 (published predictions, ns): gravitational east +144±14, west +179±18; kinematic east −184±18, west +96±10")
print(f"sums: east {144-184}, west {179+96}   (measured −59±10 and +273±7)")

print("\n== Schwarzschild radius r_s = 2GM/c² and the clock factor √(1 − r_s/r)")
for name, M, r in [("Sun", M_sun, R_sun), ("Earth", M_E, R_E), ("neutron star 1.4 M☉, 12 km", 1.4*M_sun, 12e3), ("white dwarf 1 M☉, 6000 km", M_sun, 6e6)]:
    rs = 2*G*M/c**2
    print(f"{name:28s} r_s = {rs:.4g} m   clock at surface runs at {math.sqrt(1-rs/r):.9f} of far-away rate  (slow by {(1-math.sqrt(1-rs/r)):.3e})")
print(f"black hole of 10 M☉: r_s = {2*G*10*M_sun/c**2/1e3:.1f} km;  Sagittarius A* 4.3e6 M☉: r_s = {2*G*4.3e6*M_sun/c**2/1e9:.1f} million km")

print("\n== Light deflection at the solar limb, b = R☉")
newton = 2*G*M_sun/(R_sun*c**2); einstein = 4*G*M_sun/(R_sun*c**2)
print(f"Newton (impulse): {newton*arcsec:.3f}\"   Einstein: {einstein*arcsec:.3f}\"   (Eddington 1919: 1.61 ± 0.30 and 1.98 ± 0.12; radio VLBI: 1.7499 ± 0.0003)")

# numerical check of the impulse argument: a particle at speed c on a nearly straight path past the Sun
def rhs(t, s):
    x, y, vx, vy = s; r3 = (x*x + y*y)**1.5
    return [vx, vy, -G*M_sun*x/r3, -G*M_sun*y/r3]
sol = solve_ivp(rhs, [0, 4000], [-6e11, R_sun, c, 0.0], rtol=1e-10, atol=1e-3, max_step=5.0)
vx, vy = sol.y[2, -1], sol.y[3, -1]
print(f"numerical Newtonian orbit of a speed-c particle past the Sun: deflection {abs(math.atan2(vy, vx))*arcsec:.3f}\"  (formula 2GM/(bc²) = {newton*arcsec:.3f}\")")

print("\n== Mercury's perihelion: Δφ = 6πGM/(a(1−e²)c²) per orbit")
a, e, T = 5.791e10, 0.2056, 87.969
per_orbit = 6*math.pi*G*M_sun/(a*(1-e*e)*c**2)
print(f"per orbit {per_orbit*arcsec:.4f}\";  orbits per century {36525/T:.1f};  per century {per_orbit*arcsec*36525/T:.1f}\"   (unexplained residual in 1859: 43\")")

print("\n== Gravitational waves: GW150914 (Abbott et al. 2016)")
print("strain ~1e-21 at Earth; the 4 km LIGO arms changed length by ~4e-18 m, a thousandth of a proton's width")
