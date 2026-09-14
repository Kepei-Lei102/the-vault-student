"""Producing an answer versus checking one: the asymmetry, timed.

Three pairs, each a task whose CHECK is trivial and whose PRODUCTION is not:
  1. multiply two primes  /  recover them from the product   (factoring)
  2. sign a message with a private key  /  verify it with the public key
  3. fill a sudoku  /  check a filled grid
The point of the card: in every pair the checker needs less knowledge, less time,
and no access to the method that produced the answer -- and can still refuse a
wrong one with certainty.

Run:  python3 learning-as-verification-asymmetry.py
"""
import time, random, math
from sympy import isprime, factorint, nextprime

def timed(f):
    t = time.perf_counter(); r = f(); return r, time.perf_counter() - t

# ---- 1. multiply vs factor ----
random.seed(7)
p = nextprime(random.randrange(10**11, 10**12)); q = nextprime(random.randrange(10**11, 10**12))
n, t_mul = timed(lambda: p * q)
_, t_chk = timed(lambda: p * q == n)                       # verifying a claimed factorisation
fac, t_fac = timed(lambda: factorint(n))                   # producing it from scratch
print("1. factoring")
print(f"   n = {n}  ({len(str(n))} digits)")
print(f"   multiply p*q            : {t_mul*1e6:8.1f} us")
print(f"   check a claimed p, q    : {t_chk*1e6:8.1f} us")
print(f"   find p, q from n        : {t_fac*1e3:8.1f} ms   (sympy factorint: Pollard rho / ECM)")
print(f"   ratio produce / check   : {t_fac/t_chk:,.0f}x\n")

# ---- 2. sign vs verify (textbook RSA, small keys, no padding -- for the asymmetry only) ----
P = nextprime(random.randrange(2**255, 2**256)); Q = nextprime(random.randrange(2**255, 2**256))
N = P * Q; e = 65537; d = pow(e, -1, (P - 1) * (Q - 1))
msg = int.from_bytes(b"the answer is 42", "big")
sig, t_sign = timed(lambda: pow(msg, d, N))                # needs the private exponent d (512 bits)
ok, t_ver = timed(lambda: pow(sig, e, N) == msg)           # needs only e = 65537
bad = (sig + 1)
print("2. signatures")
print(f"   sign with private key   : {t_sign*1e6:8.1f} us   (exponent has {d.bit_length()} bits)")
print(f"   verify with public key  : {t_ver*1e6:8.1f} us   (exponent has {e.bit_length()} bits)  -> {ok}")
print(f"   verify a forged sig     : {pow(bad, e, N) == msg}   (one bit off, refused)\n")

# ---- 3. sudoku: solve vs check ----
def check(g):
    rows = all(sorted(r) == list(range(1, 10)) for r in g)
    cols = all(sorted(g[r][c] for r in range(9)) == list(range(1, 10)) for c in range(9))
    boxes = all(sorted(g[r + i][c + j] for i in range(3) for j in range(3)) == list(range(1, 10))
                for r in (0, 3, 6) for c in (0, 3, 6))
    return rows and cols and boxes

def solve(g, calls=[0]):
    for r in range(9):
        for c in range(9):
            if g[r][c] == 0:
                for v in range(1, 10):
                    calls[0] += 1
                    if all(g[r][k] != v for k in range(9)) and all(g[k][c] != v for k in range(9)) and \
                       all(g[r//3*3 + i][c//3*3 + j] != v for i in range(3) for j in range(3)):
                        g[r][c] = v
                        if solve(g, calls): return True
                        g[r][c] = 0
                return False
    return True

puzzle = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
g = [row[:] for row in puzzle]; calls = [0]
_, t_solve = timed(lambda: solve(g, calls))
_, t_check = timed(lambda: check(g))
g2 = [row[:] for row in g]; g2[0][0], g2[0][1] = g2[0][1], g2[0][0]     # swap two cells
print("3. sudoku")
print(f"   solve by backtracking   : {t_solve*1e3:8.1f} ms   ({calls[0]:,} placements tried)")
print(f"   check the filled grid   : {t_check*1e6:8.1f} us   -> {check(g)}")
print(f"   check a grid with two   : {check(g2)}   (cells swapped: refused)")

# ---- figure: the three pairs on one log-time axis ----
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
G = "#888"
pairs = [("factor a 23-digit\nsemiprime", t_fac, t_chk), ("sign with a\n512-bit key", t_sign, t_ver), ("solve a\nsudoku", t_solve, t_check)]
fig, ax = plt.subplots(figsize=(9, 3.6)); fig.patch.set_alpha(0); ax.set_facecolor("none")
y = range(len(pairs))
ax.barh([i + 0.18 for i in y], [p[1] * 1e6 for p in pairs], height=0.34, color="#dc2626", alpha=0.85, label="produce the answer")
ax.barh([i - 0.18 for i in y], [p[2] * 1e6 for p in pairs], height=0.34, color="#059669", alpha=0.85, label="check a given answer")
for i, (lab, tp, tc) in enumerate(pairs):
    ax.text(tp * 1e6 * 1.25, i + 0.18, f"{tp/tc:,.0f}× slower", va="center", fontsize=9, color="#dc2626")
ax.set_xscale("log"); ax.set_xlim(right=max(p[1] for p in pairs) * 1e6 * 60); ax.set_yticks(list(y)); ax.set_yticklabels([p[0] for p in pairs], color=G)
ax.set_xlabel("time / microseconds (log scale)", color=G); ax.tick_params(colors=G)
for s in ax.spines.values(): s.set_color(G)
ax.legend(frameon=False, labelcolor=G, fontsize=9, loc="lower right")
ax.set_title("the same three problems, timed both ways on this machine", color=G, fontsize=10)
fig.tight_layout(); fig.savefig("learning-as-verification-asymmetry.svg", transparent=True)
print("\nwrote learning-as-verification-asymmetry.svg")
