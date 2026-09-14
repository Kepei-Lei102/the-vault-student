"""The Challenger O-ring data the night before the launch.

Twenty-three shuttle flights before 51-L, with the launch temperature and the number of
primary O-rings (of six) that showed erosion or blow-by (Dalal, Fowlkes and Hoadley,
JASA 84 (1989), Table 1; the Rogers Commission Report, vol. 1, p. 146). The engineers at
Thiokol plotted only the seven flights that had incidents and saw no trend; the sixteen
clean flights, all warm, were left off the chart. This script plots both views and fits
the logistic regression the 1989 paper fitted.

Run:  python3 feynman-oring.py   -> feynman-oring.svg
"""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

temp = np.array([66,70,69,68,67,72,73,70,57,63,70,78,67,53,67,75,70,81,76,79,75,76,58])
dist = np.array([ 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 1])
n = 6
# logistic regression, per O-ring, by Newton's method (no scipy needed)
X = np.column_stack([np.ones_like(temp, float), temp.astype(float)])
b = np.zeros(2)
for _ in range(50):
    p = 1/(1+np.exp(-X@b))
    W = n*p*(1-p)
    grad = X.T@(dist - n*p)
    H = -(X.T*W)@X
    b = b - np.linalg.solve(H, grad)
print(f"logistic fit per O-ring: logit p = {b[0]:.3f} + {b[1]:.4f} T   (the 1989 paper: 5.085 - 0.1156 T)")
def p_ring(T): return 1/(1+np.exp(-(b[0]+b[1]*T)))
for T in (31, 53, 70):
    print(f"T = {T} F: p(one ring damaged) = {p_ring(T):.3f}, expected damaged of six = {n*p_ring(T):.2f}, p(at least one) = {1-(1-p_ring(T))**n:.3f}")
launch = 31
fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
fig.patch.set_alpha(0)
G = "#888"
for ax, title, mask in [(axes[0], "what Thiokol looked at: the seven flights with damage", dist > 0),
                        (axes[1], "all twenty-three flights, and the fitted curve", np.ones_like(dist, bool))]:
    ax.set_facecolor("none")
    j = np.random.default_rng(1).uniform(-0.4, 0.4, size=temp.size)
    ax.scatter(temp[dist>0] + j[dist>0], dist[dist>0], s=70, color="#dc2626", zorder=3, label="flights with O-ring damage")
    if ax is axes[1]:
        ax.scatter(temp[dist==0] + j[dist==0], dist[dist==0], s=70, facecolors="none", edgecolors="#2563eb", linewidths=1.8, zorder=3, label="clean flights (left off the chart)")
        Ts = np.linspace(28, 85, 200)
        ax.plot(Ts, n*p_ring(Ts), color="#7c3aed", lw=2, label="expected damaged rings of six (logistic fit)")
        ax.axvline(launch, color="#f59e0b", lw=2, ls="--")
        ax.text(launch+1, 4.3, "51-L launched\nat 31 F", color="#f59e0b", fontsize=9, va="top")
        ax.set_xlim(26, 85)
    else:
        ax.set_xlim(50, 82)
    ax.set_ylim(-0.3, 4.6)
    ax.set_yticks([0,1,2,3,4])
    ax.set_xlabel("launch temperature (degrees F)", color=G)
    ax.set_ylabel("O-rings damaged (of six)", color=G)
    ax.set_title(title, color=G, fontsize=10)
    ax.tick_params(colors=G)
    for s in ax.spines.values(): s.set_color(G)
    leg = ax.legend(loc="upper right", fontsize=8, frameon=False)
    for t in leg.get_texts(): t.set_color(G)
fig.tight_layout()
fig.savefig("feynman-oring.svg", transparent=True)
print("wrote feynman-oring.svg")
