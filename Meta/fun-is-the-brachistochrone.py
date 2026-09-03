"""Figure for [[Fun Is the Brachistochrone]]: three slides from A to B under gravity,
timed by numerical integration — the straight line, a steep-then-flat 'drill' path,
and the cycloid, which wins by dipping BELOW the straight line first.

Run: python3 fun-is-the-brachistochrone.py   (from Meta/)
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams.update({"svg.hashsalt": "vault", "font.size": 12, "text.color": "#888888",
                     "axes.edgecolor": "#888888", "axes.labelcolor": "#888888",
                     "xtick.color": "#888888", "ytick.color": "#888888", "svg.fonttype": "none"})
g = 9.81
A = (0.0, 0.0); B = (2.0, -1.0)       # metres; B is 2 across, 1 down

def descent_time(xs, ys):
    """Bead from rest at (0,0) sliding frictionlessly along the polyline; energy gives speed."""
    t = 0.0
    for i in range(1, len(xs)):
        y0, y1 = -ys[i-1], -ys[i]           # depth below A (positive)
        v0, v1 = np.sqrt(2*g*max(y0, 0)), np.sqrt(2*g*max(y1, 0))
        ds = np.hypot(xs[i]-xs[i-1], ys[i]-ys[i-1])
        t += ds / max((v0+v1)/2, 1e-9)
    return t

# straight line
xs_l = np.linspace(A[0], B[0], 4000); ys_l = np.linspace(A[1], B[1], 4000)
# cycloid through B: x = R(θ - sinθ), y = -R(1 - cosθ); solve R,θ_B
from scipy.optimize import brentq
f = lambda th: (1-np.cos(th))/(th-np.sin(th)) - (-B[1])/B[0]
thB = brentq(f, 0.1, 2*np.pi-0.01); R = B[0]/(thB-np.sin(thB))
th = np.linspace(0, thB, 4000); xs_c = R*(th-np.sin(th)); ys_c = -R*(1-np.cos(th))
# steep-then-flat: drop 0.9 m at x=0.3, then glide (the 'drill first, then coast' path)
xs_s = np.concatenate([np.linspace(0, 0.3, 1500), np.linspace(0.3, 2.0, 2500)])
ys_s = np.concatenate([np.linspace(0, -0.9, 1500), np.linspace(-0.9, -1.0, 2500)])

T = {"straight line": descent_time(xs_l, ys_l), "steep drop, then coast": descent_time(xs_s, ys_s),
     "cycloid (brachistochrone)": descent_time(xs_c, ys_c)}
for k, v in T.items(): print(f"{k:28s} {v:.3f} s")

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(xs_l, ys_l, color="#888888", lw=2, ls="--", label=f"straight line — {T['straight line']:.2f} s")
ax.plot(xs_s, ys_s, color="#dc2626", lw=2, ls=":", label=f"steep drop, then coast — {T['steep drop, then coast']:.2f} s")
ax.plot(xs_c, ys_c, color="#2563eb", lw=3, label=f"cycloid — {T['cycloid (brachistochrone)']:.2f} s  (fastest)")
ax.fill_between(xs_c, ys_c, np.interp(xs_c, xs_l, ys_l), color=(37/255, 99/255, 235/255, 0.12))
ax.plot(*A, "o", color="#059669", ms=9); ax.plot(*B, "o", color="#f59e0b", ms=9)
ax.text(A[0]-0.05, A[1]+0.06, "A  (start)", color="#888888", ha="left")
ax.text(B[0]+0.03, B[1]-0.02, "B  (the goal)", color="#888888", ha="left", va="top")
ax.text(0.95, -0.78, "the detour that wins:\nsteeper first, faster all the way", color="#888888", fontsize=11, ha="center")
ax.set_xlim(-0.2, 2.5); ax.set_ylim(-1.35, 0.25); ax.set_aspect("equal")
ax.set_xticks([]); ax.set_yticks([])
for s_ in ("top", "right", "left", "bottom"): ax.spines[s_].set_visible(False)
leg = ax.legend(loc="lower left", frameon=False, fontsize=10.5)
for t_ in leg.get_texts(): t_.set_color("#888888")
ax.set_title("Same start, same goal, gravity only — which slide gets there first?", color="#888888", fontsize=12)
fig.savefig("fun-is-the-brachistochrone.svg", format="svg", bbox_inches="tight", transparent=True, metadata={"Date": None})
print("wrote fun-is-the-brachistochrone.svg")
