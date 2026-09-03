"""Figures for [[Linear Motion under a Variable Force]].

  variable-force-two-views.svg  — one motion (J26/31: 8 N drive, 0.5v² drag, 6.4 kg), seen as v(x) and v(t):
                                  the two ODE forms are two windows on the same particle
  variable-force-tanh-vs-exp.svg — free fall with v² drag (tanh) vs linear drag (1−e^{−t}) at the same terminal speed
Run: python3 variable-force-figures.py   (from Physics/Mechanics/)
"""
import numpy as np, matplotlib as mpl, matplotlib.pyplot as plt
mpl.rcParams.update({"svg.hashsalt": "vault", "font.size": 12, "text.color": "#888888", "axes.edgecolor": "#888888",
                     "axes.labelcolor": "#888888", "xtick.color": "#888888", "ytick.color": "#888888", "svg.fonttype": "none"})
G = "#888888"; BLUE = "#2563eb"; RED = "#dc2626"; GREEN = "#059669"; AMBER = "#f59e0b"; PURPLE = "#7c3aed"
def save(fig, name):
    fig.savefig(name, format="svg", bbox_inches="tight", transparent=True, metadata={"Date": None}); plt.close(fig); print("wrote", name)

# ---- figure 1: J26/31 — v(x) = 4 sqrt(1 - e^{-x/6.4})  and  v(t) = 4 tanh(t/1.6)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.2))
xs = np.linspace(0, 25, 400); vx = 4*np.sqrt(1 - np.exp(-xs/6.4))
ts = np.linspace(0, 8, 400); vt = 4*np.tanh(ts/1.6)
for ax, X, V, lab, col in [(a1, xs, vx, "distance x (m)", BLUE), (a2, ts, vt, "time t (s)", PURPLE)]:
    ax.plot(X, V, color=col, lw=2.6)
    ax.axhline(4, color=RED, lw=1.2, ls="--"); ax.text(X[-1], 4.08, "terminal speed 4 m/s", color=G, ha="right", fontsize=10)
    ax.set_xlabel(lab); ax.set_ylabel("speed v (m/s)"); ax.set_ylim(0, 4.6)
    for s_ in ("top", "right"): ax.spines[s_].set_visible(False)
a1.plot([0.8], [4*np.sqrt(1-np.exp(-0.8/6.4))], "o", color=AMBER, ms=8); a1.annotate("x = 0.8 m gives v = 1.37", xy=(0.8, 1.37), xytext=(5, 1.0), color=G, fontsize=10, arrowprops=dict(arrowstyle="->", color=AMBER))
a1.set_title(r"asked for $v$ at a distance:  use  $v\,\frac{dv}{dx}$", color=G, fontsize=11)
a2.set_title(r"asked for $v$ at a time:  use  $\frac{dv}{dt}$", color=G, fontsize=11)
a1.text(12, 2.0, r"$v^2 = 16\left(1-e^{-x/6.4}\right)$", color=G, fontsize=12); a2.text(3.6, 2.0, r"$v = 4\tanh\frac{t}{1.6}$", color=G, fontsize=12)
fig.suptitle("Same particle, two questions: 8 N drive, 0.5v² drag, 6.4 kg, from rest", color=G, fontsize=12)
save(fig, "variable-force-two-views.svg")

# ---- figure 2: tanh vs exp at the same terminal speed 10 m/s (N24/32 numbers): v'=10-0.1v² vs v'=10-v
fig, ax = plt.subplots(figsize=(9, 4.4))
ts = np.linspace(0, 5, 500)
ax.plot(ts, 10*np.tanh(ts), color=BLUE, lw=2.6, label=r"$v^2$ drag:  $v = 10\tanh t$")
ax.plot(ts, 10*(1-np.exp(-ts)), color=GREEN, lw=2.2, ls="--", label=r"linear drag (same terminal speed):  $v = 10(1-e^{-t})$")
ax.plot(ts, 10*ts, color=G, lw=1, ls=":", label="no drag:  $v = gt$")
ax.axhline(10, color=RED, lw=1.2, ls="--"); ax.text(4.95, 10.2, "terminal speed 10 m/s", color=G, ha="right", fontsize=10)
ax.set_xlim(0, 5); ax.set_ylim(0, 12); ax.set_xlabel("time t (s)"); ax.set_ylabel("speed v (m/s)")
for s_ in ("top", "right"): ax.spines[s_].set_visible(False)
leg = ax.legend(loc="lower right", frameon=False, fontsize=10)
for t_ in leg.get_texts(): t_.set_color(G)
ax.set_title("Falling from rest, g = 10: the shape of the approach tells you the drag law", color=G, fontsize=11)
save(fig, "variable-force-tanh-vs-exp.svg")
