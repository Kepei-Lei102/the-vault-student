"""Archimedes' bounds on pi, redone his way.

Measurement of the Circle, Proposition 3: the circumference is less than
3 1/7 of the diameter and more than 3 10/71 of it.  He starts from a regular
hexagon inscribed in and circumscribed about the circle, doubles the number
of sides four times (12, 24, 48, 96), and at each step bounds the perimeters
with rational numbers, rounding the square roots the safe way -- inscribed
perimeters rounded down, circumscribed rounded up -- so the bounds stay honest.

This script repeats the doubling with exact arithmetic (Fractions of high-
precision square roots), prints the bounds at each step, and checks them
against his two fractions.

Run:  python3 archimedes-pi.py
"""
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec = 60

def sqrt_frac(x, lo=True):
    """A rational just below (lo) or just above the square root of x, to 40 places."""
    d = Decimal(x.numerator) / Decimal(x.denominator)
    r = d.sqrt()
    f = Fraction(str(r))
    return f if (f * f <= x) == lo else (f - Fraction(1, 10**35) if lo else f + Fraction(1, 10**35))

# unit circle. Inscribed regular n-gon side s_n; circumscribed n-gon side t_n.
# Doubling: s_{2n} = sqrt(2 - sqrt(4 - s_n^2)),  t_{2n} = (sqrt(4 + t_n^2) - 2) * 2 / t_n ... use the classical
# half-angle forms with sines and tangents: inscribed perimeter = 2n sin(pi/n), circumscribed = 2n tan(pi/n).
n = 6
sin_lo = Fraction(1, 2)                 # sin(pi/6) exactly
tan_hi = sqrt_frac(Fraction(1, 3), lo=False)   # tan(pi/6) = 1/sqrt3, rounded up
print(f"{'sides':>5} {'inscribed perimeter / d':>26} {'circumscribed perimeter / d':>30}")
for step in range(5):
    lower = n * sin_lo; upper = n * tan_hi
    print(f"{n:5d} {float(lower):26.6f} {float(upper):30.6f}")
    if n == 96: break
    # half-angle: sin(x/2) = sqrt((1 - cos x)/2) with cos x = sqrt(1 - sin^2 x); round DOWN
    cos_hi = sqrt_frac(1 - sin_lo * sin_lo, lo=False)
    sin_lo = sqrt_frac((1 - cos_hi) / 2, lo=True)
    # tan(x/2) = tan x / (1 + sqrt(1 + tan^2 x)); round UP (denominator rounded down)
    sec_lo = sqrt_frac(1 + tan_hi * tan_hi, lo=True)
    tan_hi = tan_hi / (1 + sec_lo)
    n *= 2
A_lo, A_hi = Fraction(3) + Fraction(10, 71), Fraction(3) + Fraction(1, 7)
print(f"\nArchimedes: 3 10/71 = {float(A_lo):.6f} < pi < 3 1/7 = {float(A_hi):.6f}")
print(f"96-gon here:            {float(lower):.6f} < pi < {float(upper):.6f}")
print(f"his lower bound is below the 96-gon's: {A_lo <= lower};  his upper bound is above it: {A_hi >= upper}")
print("(he rounded his square roots to whole-number fractions by hand; the true value is 3.141593)")
