"""Erdős, run: (1) the party problem R(3,3) = 6 by brute force — every one of the 32 768 red/blue colourings of the
six-person party contains three mutual friends or three mutual strangers, and a five-person party that does not;
(2) the 1947 probabilistic method — a random colouring of K_n has, on average, fewer than one monochromatic K_k
whenever n < 2^(k/2), so a colouring with none must exist.  Run: python3 erdos-ramsey.py"""
from itertools import combinations
from math import comb

def has_mono_triangle(n, colouring):        # colouring: dict {(i,j): 0/1}
    for a, b, c in combinations(range(n), 3):
        if colouring[(a,b)] == colouring[(a,c)] == colouring[(b,c)]: return True
    return False

# (1) K5: the pentagon colouring — sides red, diagonals blue — has no monochromatic triangle
pairs5 = list(combinations(range(5), 2))
pent = {(i,j): 0 if (j - i) % 5 in (1, 4) else 1 for i, j in pairs5}
print("five people, sides red / diagonals blue, mono triangle?", has_mono_triangle(5, pent))
# K6: try every colouring
pairs6 = list(combinations(range(6), 2)); total = 2 ** len(pairs6); bad = 0
for mask in range(total):
    col = {p: (mask >> k) & 1 for k, p in enumerate(pairs6)}
    if not has_mono_triangle(6, col): bad += 1
print(f"six people: {total} colourings tried, {bad} without a monochromatic triangle  -> R(3,3) = 6")

# (2) Erdős 1947: expected number of monochromatic K_k in a random 2-colouring of K_n
def expected_mono(n, k): return comb(n, k) * 2 ** (1 - comb(k, 2))
for k in (5, 10, 20, 40):
    n = 2 ** (k // 2)
    print(f"k={k:2d}: with n = 2^(k/2) = {n:>8}, expected monochromatic K_k = {expected_mono(n, k):.3g}  (< 1, so some colouring has none: R({k},{k}) > {n})")
print("nobody knows R(5,5); it is between 43 and 46. Erdős: if aliens demand R(6,6) or they destroy us, attack the aliens.")
