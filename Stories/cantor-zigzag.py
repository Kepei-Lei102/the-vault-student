"""The rationals are countable: Cantor's 1873 zigzag, as a function you can call both ways.

Walk the grid of p/q (p across, q down) along anti-diagonals p + q = 2, 3, 4, ...; skip
fractions not in lowest terms. index(p, q) says where p/q sits in the list; nth(k) says
what sits at position k. Every positive rational gets exactly one natural number.

Run:  python3 cantor-zigzag.py
"""
from math import gcd
def walk():
    s = 2
    while True:
        rng = range(1, s) if s % 2 == 0 else range(s-1, 0, -1)   # alternate direction: the zigzag
        for p in rng:
            q = s - p
            if gcd(p, q) == 1: yield (p, q)
        s += 1
def nth(k):
    for i, pq in enumerate(walk()):
        if i == k: return pq
def index(p, q):
    g = gcd(p, q); p, q = p//g, q//g
    for i, pq in enumerate(walk()):
        if pq == (p, q): return i
print("position:  " + "  ".join(f"{k:>5d}" for k in range(16)))
print("rational:  " + "  ".join(f"{p:>2d}/{q:<2d}" for p, q in (nth(k) for k in range(16))))
for p, q in [(1, 1), (3, 7), (22, 7), (355, 113)]:
    print(f"{p}/{q} sits at position {index(p, q)}, and nth({index(p, q)}) = {nth(index(p, q))}")
print("every fraction has a place; no fraction has two: the rationals are exactly as many as the naturals.")
