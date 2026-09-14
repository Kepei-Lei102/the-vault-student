"""What Brouwer objected to, in one theorem.

Claim: there exist irrational numbers a and b with a^b rational.

The classical proof uses the law of excluded middle: sqrt(2)^sqrt(2) is
either rational or it is not.  Either way a pair exists -- but the proof
cannot tell you WHICH pair.  The constructive proof names its pair and
computes the rational number.  This script runs both, then reports what
was learned later (Gelfond-Schneider, 1934) about the undecided case.

Run:  python3 hilbert-brouwer-excluded-middle.py
"""
from decimal import Decimal, getcontext
getcontext().prec = 50

r2 = Decimal(2).sqrt()
t = r2 ** r2                                   # sqrt(2)^sqrt(2)

print("--- the classical proof (excluded middle) ---")
print(f"sqrt(2)^sqrt(2) = {t}")
print("case 1: it is rational  -> a = b = sqrt(2) works")
print("case 2: it is irrational -> a = sqrt(2)^sqrt(2), b = sqrt(2)")
print(f"        and a^b = (sqrt(2)^sqrt(2))^sqrt(2) = sqrt(2)^2 = {(t ** r2):.6f}")
print("one of the two cases holds; the proof never says which.\n")

print("--- the constructive proof (names its witnesses) ---")
a = r2
b = Decimal(9).ln() / Decimal(2).ln()          # log_2 9 = 2 log_2 3, irrational
print(f"a = sqrt(2) = {a:.12f}")
print(f"b = log_2 9 = {b:.12f}")
print(f"a^b = {(a ** b):.12f}   (exactly 3: sqrt(2)^(log_2 9) = 2^(log_2 3) = 3)")
print("b is irrational because 2^b = 9 and no power of 2 is 9 (odd).\n")

print("--- what happened to the undecided case ---")
print("Gelfond-Schneider (1934): sqrt(2)^sqrt(2) is transcendental,")
print("so case 2 is the true one -- decided forty years after Brouwer's")
print("thesis, by a theorem, not by the law of excluded middle.")
