"""How Feynman opened the safes at Los Alamos (Surely You're Joking, 'Safecracker Meets Safecracker').

A Mosler three-wheel combination lock: each wheel is a number from 0 to 99, so the label
says 100^3 = 1 000 000 combinations. Feynman found two things. (1) The mechanism forgives
an error of ±2 on each number, so only every fifth number is distinct: 20 per wheel.
(2) While a safe stands open, the last two numbers can be read off the dial by feel in
a few seconds and written in a notebook — leaving one wheel to search.

Run:  python3 feynman-safe.py
"""
per_try = 10           # seconds per full try of a three-number combination, by hand
def fmt(s):
    return f"{s/3600:.1f} h" if s < 86400*2 else f"{s/86400:.0f} days"
label   = 100**3
tol     = 20**3
lasttwo = 20
print(f"combinations on the label:            {label:>9,}   worst case {fmt(label*per_try)}")
print(f"with the +/-2 tolerance (20 per wheel): {tol:>9,}   worst case {fmt(tol*per_try)}, average {fmt(tol*per_try/2)}")
print(f"knowing the last two numbers:           {lasttwo:>9,}   worst case {fmt(lasttwo*per_try)} -> {lasttwo*per_try/60:.0f} minutes")
# what he actually tried first: the factory settings and the physicist's favourites
defaults = ["25-0-25", "50-25-50"]
constants = {"pi 3.14159": "31-41-59", "e 2.71828": "27-18-28", "sqrt2 1.41421": "14-14-21"}
print("factory defaults tried first:", ", ".join(defaults))
print("then the constants a physicist would pick:", ", ".join(f"{k} -> {v}" for k, v in constants.items()))
print("\nthe password lesson: the label counts a million; the attacker's model counted twenty.")
