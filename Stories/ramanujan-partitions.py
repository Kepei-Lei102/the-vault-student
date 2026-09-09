"""p(n), the number of partitions of n, computed exactly by Euler's pentagonal recurrence,
against the Hardy–Ramanujan asymptotic formula of 1918.  Regenerate: python3 ramanujan-partitions.py"""
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

N = 200
p = [0] * (N + 1); p[0] = 1
for n in range(1, N + 1):
    s = 0; k = 1
    while True:
        g1 = k * (3 * k - 1) // 2; g2 = k * (3 * k + 1) // 2
        if g1 > n: break
        sign = 1 if k % 2 else -1
        s += sign * p[n - g1]
        if g2 <= n: s += sign * p[n - g2]
        k += 1
    p[n] = s
hr = lambda n: math.exp(math.pi * math.sqrt(2 * n / 3)) / (4 * n * math.sqrt(3))
print("p(5) =", p[5], " p(100) =", p[100], " p(200) =", p[200])
for n in (10, 50, 100, 200):
    print(f"n={n:>3}  p(n)={p[n]:>16,}  HR={hr(n):>20,.0f}  ratio={hr(n)/p[n]:.4f}")
# Ramanujan's congruence check
print("p(5k+4) mod 5:", [p[5*k+4] % 5 for k in range(8)], " p(7k+5) mod 7:", [p[7*k+5] % 7 for k in range(6)])
# taxicab
cubes = {a**3 + b**3: (a, b) for a in range(1, 30) for b in range(a, 30)}
seen = {}
for a in range(1, 30):
    for b in range(a, 30):
        seen.setdefault(a**3 + b**3, []).append((a, b))
tc = sorted(k for k, v in seen.items() if len(v) >= 2)[:3]
print("taxicab:", [(k, seen[k]) for k in tc])

GREY = "#888888"
fig, ax = plt.subplots(figsize=(8.5, 4.8)); fig.patch.set_alpha(0); ax.set_facecolor("none")
ns = list(range(1, N + 1))
ax.semilogy(ns, [p[n] for n in ns], color="#2563eb", lw=2.2, label="p(n), exact (Euler's recurrence)")
ax.semilogy(ns, [hr(n) for n in ns], color="#f59e0b", lw=1.8, ls="--", label="Hardy–Ramanujan 1918:  e^{π√(2n/3)} / (4n√3)")
for s in ax.spines.values(): s.set_color(GREY)
ax.tick_params(colors=GREY, labelsize=9)
ax.set_xlabel("n", color=GREY); ax.set_ylabel("number of partitions of n", color=GREY)
ax.set_title("The partition function, and the formula that caught it", color=GREY, fontsize=11)
ax.annotate(f"p(200) = {p[200]:,}", xy=(200, p[200]), xytext=(95, p[200]/8), color="#2563eb", fontsize=9,
            arrowprops=dict(arrowstyle="-", color="#2563eb", lw=0.8))
ax.text(8, 3e10, "MacMahon computed p(200) by hand in 1918;\nthe formula lands within 3% at n = 200,\nand Rademacher made it exact in 1937.", color=GREY, fontsize=8.5, va="top")
leg = ax.legend(frameon=False, fontsize=9, loc="lower right")
for t in leg.get_texts(): t.set_color(GREY)
fig.tight_layout(); fig.savefig("ramanujan-partitions.svg", transparent=True); print("saved")
