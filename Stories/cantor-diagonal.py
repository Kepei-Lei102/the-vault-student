"""Cantor's two theorems, run.

1. The diagonal argument (1891): hand me ANY list of real numbers in [0,1) — as a Python
   function that returns the n-th number's decimal digits — and I build a number that is
   not on your list: its n-th digit differs from the n-th digit of your n-th number.
2. Cantor's theorem (1891): no set maps onto its own power set. For |S| = 1..4 every
   function S -> P(S) is tried by brute force; none is a surjection. The witness is
   always the same set: {x : x not in f(x)}.

Run:  python3 cantor-diagonal.py
"""
from itertools import product
from fractions import Fraction
import math

def digits_of(x, n):
    """first n decimal digits of a Fraction or float in [0,1)"""
    x = Fraction(x); out = []
    for _ in range(n):
        x *= 10; d = int(x); out.append(d); x -= d
    return out

def anti_diagonal(listing, n):
    """listing(k) -> the k-th real (Fraction) in [0,1). Returns n digits of a number not in the list."""
    ds = []
    for k in range(n):
        d = digits_of(listing(k), k+1)[k]        # the k-th digit of the k-th number
        ds.append(5 if d != 5 else 6)             # change it, avoiding 0 and 9 (no 0.4999.. = 0.5 ambiguity)
    return ds

# an attempt at listing "all" reals in [0,1): here the k-th entry is (k+1)/(k+7) — any rule at all will do,
# and that is the point: the argument never looks at what the rule is, only at the diagonal it produces.
def listing(k):
    return Fraction(k + 1, k + 7)

N = 12
d = anti_diagonal(listing, N)
print("list (first", N, "entries):")
for k in range(N):
    dg = digits_of(listing(k), N); print(f"  #{k:2d}  0." + "".join(map(str, dg)) + f"   <- digit {k}: {dg[k]}")
print("the diagonal digits: ", "".join(str(digits_of(listing(k), k+1)[k]) for k in range(N)))
print("Cantor's number:    0." + "".join(map(str, d)) + "  (every digit changed, so it differs from entry k at digit k, for every k)")
for k in range(N):
    assert digits_of(listing(k), k+1)[k] != d[k]
print("checked: differs from all", N, "listed numbers.  Add it to the list and the argument runs again — the list can never be complete.\n")

print("Cantor's theorem by brute force: no f: S -> P(S) is onto")
for n in range(1, 5):
    S = list(range(n)); subsets = [frozenset(c) for r in range(n+1) for c in __import__('itertools').combinations(S, r)]
    total = 0; surj = 0
    for f in product(subsets, repeat=n):            # every function S -> P(S)
        total += 1
        if len(set(f)) == len(subsets): surj += 1
        D = frozenset(x for x in S if x not in f[x])   # the diagonal set
        assert D not in f                               # ...is never hit
    print(f"  |S| = {n}: {total:6d} functions into the {len(subsets):2d} subsets, surjections found: {surj};  {{x : x not in f(x)}} was never in the image — every time")
print("so |P(S)| > |S| for every set, finite or not: there is no largest infinity.")
