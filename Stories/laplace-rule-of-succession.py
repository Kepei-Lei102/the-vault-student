"""
laplace-rule-of-succession.py — the sunrise problem, done Laplace's way and checked.

Companion to [[Stories/Laplace and Napoleon]].  In the Essai philosophique (1814)
Laplace asks: if the sun has risen every day of recorded history, how sure should we
be that it rises tomorrow?  His rule of succession: after n successes in n trials with
a uniform prior on the unknown probability p, the chance of one more success is
(n + 1)/(n + 2).  He took 5000 years of history and wrote the odds as 1 826 214 to 1.

This script (1) recomputes Laplace's number, (2) derives the rule by integrating over
the prior, and (3) checks it by simulation: draw p uniformly, run n trials, keep the
worlds where all n succeeded, and count how often trial n + 1 succeeds too.

Run:  python3 laplace-rule-of-succession.py
"""
import numpy as np
from math import comb

# 1. Laplace's number: 5000 Julian-ish years of sunrises
days = 5000 * 365.2426
print(f"1. 5000 years = {days:,.0f} days; rule of succession gives odds (n+1) : 1 = {days+1:,.0f} : 1")
print("   Laplace wrote 1 826 214 to 1 (Essai philosophique, 1814, using 365.2426 days/year).")

# 2. the derivation, numerically: P(next | n of n) = ∫ p^{n+1} dp / ∫ p^n dp = (n+1)/(n+2)
for n in (0, 1, 2, 10, 100):
    p = np.linspace(0, 1, 200001)
    num = np.trapezoid(p ** (n + 1), p); den = np.trapezoid(p ** n, p)
    print(f"2. n = {n:>3}: ∫p^(n+1)/∫p^n = {num/den:.4f}   rule (n+1)/(n+2) = {(n+1)/(n+2):.4f}")

# 3. simulation: a uniform prior over p, worlds filtered on 'all n so far succeeded'
rng = np.random.default_rng(1749)
W = 2_000_000
p = rng.random(W)
for n in (1, 3, 10):
    trials = rng.random((W, n + 1)) < p[:, None]
    ok = trials[:, :n].all(1)
    print(f"3. n = {n:>2}: of {ok.sum():,} worlds where all {n} succeeded, next succeeded in {trials[ok, n].mean():.4f}   rule {(n+1)/(n+2):.4f}")

# the general rule with s successes in n trials: (s+1)/(n+2)
n, s = 10, 7
trials = rng.random((W, n + 1)) < p[:, None]
ok = trials[:, :n].sum(1) == s
print(f"   s = {s} of n = {n}: next succeeded in {trials[ok, n].mean():.4f}   rule (s+1)/(n+2) = {(s+1)/(n+2):.4f}")
print("   — the '+1' and '+2' are the prior's two imaginary trials, one success and one failure: Laplace's hedge against certainty.")
