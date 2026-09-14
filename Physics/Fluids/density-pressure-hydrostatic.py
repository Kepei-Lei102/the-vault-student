"""Hydrostatic pressure, built from slabs -- and every number in the card, recomputed.

Part 1 derives dp = rho g dh the way the syllabus asks: stack thin horizontal
slabs of fluid, each adds its own weight per unit area, and sum.  With constant
density the sum is a straight line (water); with density proportional to
pressure it is an exponential (the atmosphere) -- the same slab sum, integrated
numerically against the closed forms.

Part 2 recomputes the worked examples against their published mark schemes.

Run:  python3 density-pressure-hydrostatic.py
"""
import math
g = 9.81

print("PART 1 -- pressure from a stack of slabs\n")
rho_w = 1000.0; H = 10994.0                       # Challenger Deep
n = 100000; dh = H / n; p = 0.0
for _ in range(n): p += rho_w * g * dh            # each slab: weight / area = rho g dh
print(f"water, constant density: {n:,} slabs to {H:.0f} m -> {p/1e6:.1f} MPa   (rho g h = {rho_w*g*H/1e6:.1f} MPa; about {p/1.013e5:.0f} atmospheres)")
# atmosphere: rho = p / (R_s T)  (isothermal ideal gas), so dp/dh = -(g / R_s T) p
Rs, T = 287.0, 288.0; p0 = 101325.0; Hs = Rs * T / g
p = p0; h = 0.0; dh = 1.0; out = {}
for step in range(20000):
    rho = p / (Rs * T); p -= rho * g * dh; h += dh
    if int(h) in (1000, 5000, 8849): out[int(h)] = p
for hh, pp in out.items():
    print(f"air, density tracks pressure: h = {hh:5d} m -> {pp/1e3:6.1f} kPa   (closed form p0 e^(-h/H) = {p0*math.exp(-hh/Hs)/1e3:6.1f} kPa)")
print(f"scale height H = R T / g = {Hs:.0f} m: air pressure falls by a factor e every {Hs/1000:.1f} km; water pressure rises 1 atm every {1.013e5/(rho_w*g):.1f} m\n")

print("PART 2 -- the worked examples, against their schemes\n")
# 9702 N23/23 Q1(b): cylinder density with uncertainties
D, L, M = 26.2e-3, 0.162, 0.247
rho = 4 * M / (math.pi * D**2 * L)
pct = 0.1/26.2*100 + 2*0.1/26.2*100 + 1/162*100      # scheme: %M + 2%D + %L with %M = 0.4 given
pct = 0.4 + 2*(0.1/26.2*100) + (1/162*100)
print(f"N23/23 Q1: rho = {rho:.3g} kg/m3 (scheme 2.83e3); % uncertainty = 0.4 + 2(0.4) + 0.6 = {pct:.1f}% (scheme 1.8%)")
# 9702 N23/23 Q3(b): airship
U, rho_air = 93000, 1.2
V = U / (rho_air * g); m = (U + 3000) / g
print(f"N23/23 Q3: V = U/(rho g) = {V:.0f} m3 (scheme 7900); m = (93000 + 3000)/g = {m:.0f} kg (scheme 9800)")
# 9702 M25/22 Q2(b): cylinder held down by a beam
U = 11 * g + 1300; A = math.pi * 0.39**2; y = U / (990 * g * A)
print(f"M25/22 Q2: upthrust = 11 g + 1300 = {U:.0f} N (scheme 1400); y = U/(rho g A) = {y:.2f} m (scheme 0.30)")
# 9702 M22/22 Q1: sphere in liquid
V = 4/3 * math.pi * (2.1e-3)**3; rho_l = 4.8e-4 / (g * V); v = (7.2e-4 - 4.8e-4) / (17 * 2.1e-3)
print(f"M22/22 Q1: rho = U/(gV) = {rho_l:.0f} kg/m3 (scheme 1300); terminal v = {v*1e3:.1f} mm/s (scheme 6.7e-3 m/s)")
# 0625 M21/42 Q1: glass window, pressures, vacuum tube
W = 2.6e3 * 0.02 * 0.15 * 10; F = (1.3e5 - 1.0e5) * 0.15; rho_liq = 9.6e4 / (10 * 12)
print(f"0625 M21/42 Q1: W = rho V g = {W:.0f} N (scheme 78, g = 10); F = dp A = {F:.2g} N outwards (scheme 4.5e3); rho = p/gh = {rho_liq:.0f} kg/m3 (scheme 800)")
# 0625 M26/42 Q2/Q4: steel cube; sea water depth
print(f"0625 M26/42: V = 110/7900 = {110/7900:.3f} m3 (scheme 0.014); dp = 1030 x 10 x 2.50 = {1030*10*2.5/1e3:.2f} kPa")
