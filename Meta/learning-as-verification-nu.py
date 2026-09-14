"""Why is it "minus one, minus one"?  Verify the degrees of freedom by simulation.

A chi-squared goodness-of-fit statistic with k cells has nu = k - 1 - p degrees
of freedom, where p is the number of parameters you estimated from the data.
The card's claim is that this is a COUNT, not a rule: each estimated parameter is
one more equation the misses must satisfy, so one fewer of them is free.

This script does not trust the count.  It draws thousands of samples from a
Poisson distribution, fits the mean from each sample (p = 1), bins the counts
into k cells, computes X^2, and asks which chi-squared curve the statistics
actually follow: the one with k - 1 (forgetting the fitted mean) or k - 2.
Then it does the same for an r x c independence table against (r-1)(c-1).

Run:  python3 learning-as-verification-nu.py
"""
import numpy as np
from scipy import stats

rng = np.random.default_rng(3)
lam_true, N, trials = 2.3, 300, 4000
edges = [0, 1, 2, 3, 4, 5]                       # cells: 0,1,2,3,4, 5+  -> k = 6
k = len(edges)
X2 = []
for _ in range(trials):
    x = rng.poisson(lam_true, N)
    lam_hat = x.mean()                            # ONE parameter estimated from the data
    p = [stats.poisson.pmf(v, lam_hat) for v in edges[:-1]] + [1 - stats.poisson.cdf(edges[-1] - 1, lam_hat)]
    E = N * np.array(p)
    O = np.array([np.sum(x == v) for v in edges[:-1]] + [np.sum(x >= edges[-1])])
    X2.append(np.sum((O - E) ** 2 / E))
X2 = np.array(X2)
print(f"goodness of fit: k = {k} cells, Poisson mean estimated from the data (p = 1)")
print(f"{'candidate nu':>14} {'sim mean':>9} {'chi2 mean':>10} {'sim 95th pct':>13} {'chi2 95th':>10} {'KS p-value':>11}")
for nu in (k - 1, k - 2, k - 3):
    ks = stats.kstest(X2, "chi2", args=(nu,))
    print(f"{nu:>14} {X2.mean():9.2f} {nu:10d} {np.percentile(X2, 95):13.2f} {stats.chi2.ppf(0.95, nu):10.2f} {ks.pvalue:11.3f}")
print("-> the statistics follow chi2 with nu = k - 2: the fitted mean really does cost a degree of freedom.\n")

# ---- independence: (r-1)(c-1) ----
r, c = 3, 4; pr = rng.dirichlet(np.ones(r)); pc = rng.dirichlet(np.ones(c))
X2i = []
for _ in range(trials):
    table = rng.multinomial(400, np.outer(pr, pc).ravel()).reshape(r, c)
    stat, _, dof, _ = stats.chi2_contingency(table, correction=False)
    X2i.append(stat)
X2i = np.array(X2i)
print(f"independence: {r} x {c} table -> scipy says dof = {dof}; the count (r-1)(c-1) = {(r-1)*(c-1)}")
print(f"{'candidate nu':>14} {'sim 95th pct':>13} {'chi2 95th':>10} {'KS p-value':>11}")
for nu in (r * c - 1, (r - 1) * (c - 1)):
    ks = stats.kstest(X2i, "chi2", args=(nu,))
    print(f"{nu:>14} {np.percentile(X2i, 95):13.2f} {stats.chi2.ppf(0.95, nu):10.2f} {ks.pvalue:11.3f}")
print("-> rc - 1 cells, minus (r-1) + (c-1) fitted marginals, = (r-1)(c-1) free misses.")

# ---- figure ----
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
G = "#888"
fig, ax = plt.subplots(figsize=(9, 3.8)); fig.patch.set_alpha(0); ax.set_facecolor("none")
ax.hist(X2, bins=60, density=True, color="#2563eb", alpha=0.35, label="4 000 simulated X² (Poisson fit, 6 cells)")
xx = np.linspace(0, 20, 400)
ax.plot(xx, stats.chi2.pdf(xx, k - 1), color="#dc2626", lw=2, ls="--", label="χ² with ν = 5  (forgot the fitted mean)")
ax.plot(xx, stats.chi2.pdf(xx, k - 2), color="#059669", lw=2.4, label="χ² with ν = 4  (cells − 1 − parameters)")
ax.set_xlabel("X²", color=G); ax.set_ylabel("density", color=G); ax.tick_params(colors=G)
for s in ax.spines.values(): s.set_color(G)
ax.legend(frameon=False, labelcolor=G, fontsize=9)
ax.set_title("the count says ν = 6 − 1 − 1; the simulation agrees, and refuses the rule that forgot the parameter", color=G, fontsize=10)
fig.tight_layout(); fig.savefig("learning-as-verification-nu.svg", transparent=True); print("\nwrote learning-as-verification-nu.svg")
