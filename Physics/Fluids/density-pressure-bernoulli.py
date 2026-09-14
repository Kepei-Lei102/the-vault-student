"""Continuity and Bernoulli, checked along a pipe.

A pipe narrows from 5 cm to 2 cm diameter and climbs 1 m.  Continuity fixes the
speed at every cross-section; Bernoulli says p + rho v^2/2 + rho g h is the same
number everywhere along a streamline.  The script computes all three terms at
twenty stations and prints the sum -- constant to the last digit -- then does
Torricelli's tank and a garden-hose nozzle.

Run:  python3 density-pressure-bernoulli.py
"""
import math
g, rho = 9.81, 1000.0
d1, d2 = 0.05, 0.02; v1 = 1.5; p1 = 2.0e5; h1 = 0.0
A1 = math.pi * d1**2 / 4
print(f"{'x/m':>5} {'d/cm':>5} {'v/(m/s)':>8} {'h/m':>5} {'p/kPa':>8} {'rho v^2/2':>10} {'rho g h':>8} {'sum/kPa':>8}")
for i in range(21):
    x = i / 20
    d = d1 + (d2 - d1) * x; h = x * 1.0
    A = math.pi * d**2 / 4; v = v1 * A1 / A                         # continuity
    p = p1 + 0.5 * rho * (v1**2 - v**2) + rho * g * (h1 - h)        # Bernoulli
    tot = p + 0.5 * rho * v**2 + rho * g * h
    if i % 4 == 0: print(f"{x:5.2f} {d*100:5.1f} {v:8.2f} {h:5.2f} {p/1e3:8.1f} {0.5*rho*v**2/1e3:10.1f} {rho*g*h/1e3:8.1f} {tot/1e3:8.1f}")
print(f"\nthe narrow, high end runs at {v:.1f} m/s and {p/1e3:.0f} kPa: faster and at lower pressure -- the Venturi effect\n")
# Torricelli: tank with a hole h below the surface
for h in (0.5, 2.0):
    print(f"hole {h} m below the surface: v = sqrt(2 g h) = {math.sqrt(2*g*h):.2f} m/s -- the speed of free fall through h")
# garden hose: 15 mm hose at 2 m/s, thumb over the end leaving 6 mm
v_h, d_h, d_n = 2.0, 0.015, 0.006
v_n = v_h * (d_h / d_n)**2
print(f"\nhose 15 mm at 2.0 m/s, thumb leaves a 6 mm gap: v = {v_n:.0f} m/s; pressure drop across the gap {0.5*rho*(v_n**2 - v_h**2)/1e3:.0f} kPa")
