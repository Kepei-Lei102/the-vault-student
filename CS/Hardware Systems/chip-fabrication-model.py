"""Every number in How a Chip Is Made.md: the resolution of a lithography tool, dies per wafer, yield against die area
and defect density, why chiplets, and what a transistor budget buys.   Run: python3 chip-fabrication-model.py
"""
import math
import numpy as np

# ── 1. how small a feature light can print: Rayleigh's criterion, CD = k1 * lambda / NA ─────────────────────
print("== smallest printable half-pitch, CD = k1 λ / NA  (k1 ≈ 0.28 is about the practical floor for single exposure)")
for name, lam, NA, k1 in [("i-line, 1990s", 365, 0.6, 0.6), ("ArF dry, 193 nm", 193, 0.93, 0.35), ("ArF immersion (water, n = 1.44)", 193, 1.35, 0.28),
                          ("EUV, 13.5 nm, NA 0.33", 13.5, 0.33, 0.35), ("high-NA EUV, NA 0.55", 13.5, 0.55, 0.35)]:
    print(f"   {name:34s} CD ≈ {k1 * lam / NA:6.1f} nm")
print("   The 5 nm 'node' has a metal half-pitch near 15 nm and a fin pitch near 27 nm; the node name stopped being a length around 2010.")

# ── 2. dies per wafer, by geometry ─────────────────────────────────────────────────────────────────────────
def dies_per_wafer(d_mm, a_mm2, edge_mm=3.0):
    """De Vries' estimate: area ratio minus the partial dies lost round the edge."""
    r = d_mm / 2 - edge_mm
    return int(math.pi * r**2 / a_mm2 - math.pi * 2 * r / math.sqrt(2 * a_mm2))
print("\n== dies per 300 mm wafer")
for name, a in [("phone SoC, 100 mm²", 100), ("laptop chip, 150 mm²", 150), ("GPU, 600 mm²", 600), ("reticle-limit die, 858 mm²", 858)]:
    print(f"   {name:28s} {dies_per_wafer(300, a):5d} dies")

# ── 3. yield: the Poisson model, Y = exp(−D·A), and why big dies are expensive ─────────────────────────────
print("\n== yield with defect density D (defects per cm²), Y = e^{-D A}")
for D in (0.05, 0.1, 0.2):
    row = "   D = {:.2f}: ".format(D) + "  ".join(f"{a} mm² → {math.exp(-D * a / 100) * 100:5.1f}%" for a in (50, 100, 150, 300, 600, 858))
    print(row)
D = 0.1
big = 800; four = 200
y_big = math.exp(-D * big / 100); y_four = math.exp(-D * four / 100)
n_big = dies_per_wafer(300, big); n_four = dies_per_wafer(300, four)
print(f"\n== one 800 mm² die against four 200 mm² chiplets at D = 0.1/cm²:")
print(f"   monolithic: {n_big} dies/wafer × {y_big*100:.0f}% yield = {n_big * y_big:.0f} good chips per wafer")
print(f"   chiplets:   {n_four} dies/wafer × {y_four*100:.0f}% yield = {n_four * y_four:.0f} good chiplets = {n_four * y_four / 4:.0f} four-chiplet products per wafer")
print(f"   the same silicon gives {n_four * y_four / 4 / (n_big * y_big):.1f}× as many products, before the cost of joining them")

# ── 4. cost per good die ────────────────────────────────────────────────────────────────────────────────────
print("\n== cost per good die at a wafer cost of $17 000 (a 5 nm-class wafer, public estimates 2023)")
for name, a in [("phone SoC, 100 mm²", 100), ("laptop chip, 150 mm²", 150), ("GPU, 600 mm²", 600)]:
    n = dies_per_wafer(300, a); y = math.exp(-0.1 * a / 100)
    print(f"   {name:24s} {n:4d} dies, yield {y*100:4.0f}% → ${17000 / (n * y):7.0f} per good die")

# ── 5. transistor budgets: what a density buys ──────────────────────────────────────────────────────────────
print("\n== transistor budgets (public figures)")
for name, year, count, area in [("Intel 4004", 1971, 2_250, 12), ("Intel 386", 1985, 275_000, 104), ("Pentium 4", 2000, 42_000_000, 217),
                                ("Apple A7", 2013, 1_000_000_000, 102), ("Apple M1 Max", 2021, 57_000_000_000, 432), ("Apple M2 Ultra", 2023, 134_000_000_000, 1020)]:
    print(f"   {name:14s} {year}  {count:>16,d} transistors  {count/area/1e6:8.2f} million per mm²")
print(f"   1971 → 2021: 50 years, ×{57e9/2250:,.0f} in count; a doubling every {50*12/math.log2(57e9/2250):.0f} months.")

# ── 6. the numbers of the process ───────────────────────────────────────────────────────────────────────────
print("\n== a modern logic process, order of magnitude")
print("   ~1 000 process steps, ~80 lithography exposures (a dozen of them EUV), ~3 months from bare wafer to finished chips")
print("   an EUV scanner: ~180 tonnes, ~$180 million, 13.5 nm light from tin droplets hit by a CO2 laser 50 000 times a second")
print("   a leading fab: $20–30 billion, 300 mm wafers, cleanroom air with fewer than 10 particles of 0.1 μm per cubic metre; a city street has ~10 million")
