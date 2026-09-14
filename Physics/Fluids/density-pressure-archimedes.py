"""Archimedes' principle, from pressure -- and three things that float.

Part 1: a cube submerged in water.  Pressure is computed on each face from
dp = rho g dh, multiplied by area and summed as vectors.  The sides cancel, the
bottom beats the top by exactly rho g V, whatever the depth -- no principle
assumed, just pressure and geometry.  Then the same for a cube that is only
partly under: the upthrust equals the weight of the water displaced.

Part 2: what floats, and how much of it shows.

Run:  python3 density-pressure-archimedes.py
"""
import math
g, rho_w = 9.81, 1000.0

print("PART 1 -- upthrust from pressure alone\n")
s = 0.20; V = s**3
for depth_top in (0.0, 1.0, 5.0):
    p_top = rho_w * g * depth_top; p_bot = rho_w * g * (depth_top + s)
    F_top = p_top * s * s; F_bot = p_bot * s * s
    # sides: pressure varies with depth; integrate over strips
    n = 1000; F_left = sum(rho_w * g * (depth_top + (i + 0.5) * s / n) * s * (s / n) for i in range(n)); F_right = F_left
    net = F_bot - F_top
    print(f"cube of side {s} m, top at depth {depth_top:4.1f} m: bottom push {F_bot:8.1f} N, top push {F_top:8.1f} N, sides {F_left:7.1f} N each (cancel)")
    print(f"     net upward = {net:.2f} N = rho g V = {rho_w*g*V:.2f} N  -> independent of depth\n")

print("partly submerged cube (weight of displaced water vs upthrust):")
for frac in (0.25, 0.5, 0.917):
    p_bot = rho_w * g * frac * s
    print(f"  {frac*100:5.1f}% under: bottom push {p_bot*s*s:6.2f} N = weight of displaced water {rho_w*g*V*frac:6.2f} N")

print("\nPART 2 -- what floats\n")
things = [("ice in sea water", 917, 1025), ("ice in fresh water", 917, 1000), ("oak", 750, 1000), ("a person, lungs full", 985, 1000),
          ("a person, lungs empty", 1050, 1000), ("steel cube", 7900, 1030), ("a steel ship, hull + air", 500, 1030), ("hot air at 100 C in 15 C air", 0.946, 1.225)]
for name, rho_o, rho_f in things:
    frac = rho_o / rho_f
    print(f"  {name:<32} rho_object/rho_fluid = {frac:6.3f} -> " + (f"floats, {frac*100:.0f}% submerged" if frac < 1 else "sinks"))
# hot-air balloon lift: 2500 m3 envelope
Vb = 2500; lift = (1.225 - 0.946) * Vb * g
print(f"\n  2500 m3 of 100 C air in 15 C air: upthrust - weight of hot air = {lift:.0f} N -> lifts {lift/g:.0f} kg of envelope, basket and people")
# ship: 100 000 t container ship displaces its own mass of sea water
print(f"  a 100 000-tonne ship displaces {1e8/1030:.0f} m3 of sea water: the hull below the waterline is that big, however much steel it holds")
