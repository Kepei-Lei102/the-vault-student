"""The number behind the Nobel: the electron's anomalous magnetic moment a_e = (g-2)/2.

Dirac's equation says g = 2 exactly. Schwinger's one-loop correction (1948) — the single
Feynman diagram with one photon looping from the electron back to itself — adds alpha/(2 pi).
Higher orders add the next powers of (alpha/pi); the coefficients are the sums of 7, 72, 891
and 12 672 diagrams respectively (Laporta 2017; Aoyama, Kinoshita, Nio 2018).

Run:  python3 feynman-g2.py
"""
import math

alpha = 1 / 137.035999177          # CODATA 2022 fine-structure constant
x = alpha / math.pi
# QED coefficients of (alpha/pi)^n for a_e (mass-independent parts; the muon/tau loops shift the 10th digit)
C = [0.5,                          # Schwinger 1948, one diagram
     -0.328478965579193,           # Petermann / Sommerfield 1957, seven diagrams
     1.181241456587,               # Laporta–Remiddi 1996, 72 diagrams
     -1.912245764,                 # Laporta 2017, 891 diagrams
     6.737]                        # Aoyama–Kinoshita–Nio 2018, 12 672 diagrams (numerical)
measured = 0.00115965218059        # Fan, Myers, Sukumar, Gabrielse, PRL 130 (2023) — ±0.13e-12
print(f"alpha = 1/{1/alpha:.9f}")
running = 0.0
for n, c in enumerate(C, start=1):
    running += c * x**n
    print(f"order {n}: {c:+.12f} (alpha/pi)^{n}  ->  a_e = {running:.14f}")
print(f"measured      a_e = {measured:.14f}")
print(f"difference    {abs(running-measured):.1e}  (the hadronic and weak contributions, ~1.7e-12, are not included above)")
print(f"Schwinger alone: {C[0]*x:.9f} vs measured {measured:.9f} -> agrees to {-math.log10(abs(C[0]*x-measured)/measured):.1f} digits")
