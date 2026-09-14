"""Brouwer's weak counterexample, decided.

Brouwer asked: does the block 0123456789 occur somewhere in the decimal
expansion of pi?  In 1908 nobody knew, and he built a real number x whose
digits copy pi's until such a block appears -- so "x = 0 or x != 0" could
not be asserted, because nobody could say which.  The point was never that
the answer is unknowable; it was that "true or false" is not yet a proof.

In 1997 Kanada's team found the block, starting at decimal position
17,387,594,880.  This script checks the smaller cousins that a laptop can
reach: the first occurrence of 0, 01, 012, 0123, ... in pi, computed here
(mpmath; half a million digits takes about half a minute) rather than trusted from a table.

Run:  python3 hilbert-brouwer-pi-digits.py
"""
import sys

def pi_digits(n):
    """First n decimal digits of pi after the point."""
    import mpmath
    mpmath.mp.dps = n + 20
    return mpmath.nstr(mpmath.mp.pi, n + 10, strip_zeros=False)[2:n + 2]

N = int(sys.argv[1]) if len(sys.argv) > 1 else 500_000
d = pi_digits(N)
print(f"pi = 3.{d[:30]}...   ({N:,} digits computed)\n")
print(f"{'block':<12}{'first position':>16}")
for L in range(1, 11):
    block = "0123456789"[:L]
    p = d.find(block)
    pos = f"{p + 1:,}" if p >= 0 else f"not in the first {N:,}"
    print(f"{block:<12}{pos:>16}")
print("\n0123456789 first appears at position 17,387,594,880 (Kanada, 1997) --")
print("Brouwer's undecided number turned out to be nonzero. He never said it wasn't.")
