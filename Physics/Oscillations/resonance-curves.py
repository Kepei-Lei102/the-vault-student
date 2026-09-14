"""Three figures for the Resonance card.

  resonance-curves.svg   amplitude and phase lag against driving frequency for three Q
  resonance-phase.svg    driver and response in time, below / at / above resonance
  resonance-buildup.svg  the ring building up at resonance from rest, two Q

Run:  python3 resonance-curves.py
"""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
G = "#888"; BLUE = "#2563eb"; AMBER = "#f59e0b"; RED = "#dc2626"; GREEN = "#059669"; PURPLE = "#7c3aed"

def style(ax):
    ax.set_facecolor("none"); ax.tick_params(colors=G)
    for s in ax.spines.values(): s.set_color(G)
    ax.xaxis.label.set_color(G); ax.yaxis.label.set_color(G); ax.title.set_color(G)

def A(r, Q):   # amplitude / static deflection, r = w/w0
    return 1 / np.sqrt((1 - r**2)**2 + (r / Q)**2)
def phi(r, Q):
    return np.degrees(np.arctan2(r / Q, 1 - r**2))

# ---- 1. resonance curves ----
r = np.linspace(0, 2.2, 1200)
fig, (a1, a2) = plt.subplots(2, 1, figsize=(9, 7.2), sharex=True, gridspec_kw=dict(height_ratios=[2, 1.1]))
fig.patch.set_alpha(0)
for Q, c, lab in [(1, RED, "Q = 1 (heavy)"), (3, AMBER, "Q = 3"), (10, BLUE, "Q = 10 (light)")]:
    a1.plot(r, A(r, Q), color=c, lw=2, label=lab)
    a2.plot(r, phi(r, Q), color=c, lw=2)
    rp = np.sqrt(max(1 - 1 / (2 * Q**2), 0)); a1.scatter([rp], [A(rp, Q)], color=c, s=28, zorder=3)
a1.axhline(1, color=G, lw=0.8, ls="--"); a1.text(2.18, 1.1, "static deflection F₀/k", color=G, fontsize=9, ha="right")
a1.annotate("peak ≈ Q × F₀/k", xy=(1.0, 10), xytext=(1.35, 9.3), color=BLUE, fontsize=9, arrowprops=dict(arrowstyle="->", color=BLUE, lw=1))
a1.annotate("", xy=(0.95, 10 / np.sqrt(2)), xytext=(1.05, 10 / np.sqrt(2)), arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1))
a1.text(1.07, 7.0, "width ≈ f₀/Q", color=BLUE, fontsize=9, va="center")
a1.text(1.28, 4.2, "more damping: lower, broader,\npeak slightly below f₀", color=G, fontsize=9)
a1.set_ylabel("amplitude ÷ static deflection"); a1.set_ylim(0, 11); a1.set_xlim(0, 2.2)
a1.legend(frameon=False, labelcolor=G, fontsize=9, loc="upper right")
a1.set_title("the response to a steady push of fixed size, as its frequency is turned up")
a2.axhline(90, color=G, lw=0.8, ls="--"); a2.set_yticks([0, 90, 180]); a2.set_ylabel("lag of x behind F / °")
a2.set_xlabel("driving frequency ÷ natural frequency  (f / f₀)")
a2.text(0.15, 20, "in phase\n(spring in charge)", color=G, fontsize=9)
a2.text(1.55, 150, "antiphase\n(mass in charge)", color=G, fontsize=9)
a2.text(1.03, 100, "90° at f₀, whatever Q", color=G, fontsize=9)
style(a1); style(a2); fig.tight_layout(); fig.savefig("resonance-curves.svg", transparent=True); plt.close(fig)

# ---- 2. phase in time ----
t = np.linspace(0, 4 * 2 * np.pi, 800)
fig, axs = plt.subplots(1, 3, figsize=(12, 3.4)); fig.patch.set_alpha(0)
Q = 6
for ax, rr, title in zip(axs, [0.5, 1.0, 2.0], ["below resonance  f = ½ f₀", "at resonance  f = f₀", "above resonance  f = 2 f₀"]):
    w = rr; amp = A(rr, Q); lag = np.radians(phi(rr, Q))
    ax.plot(t, np.cos(w * t), color=AMBER, lw=1.6, label="driving force F")
    ax.plot(t, amp / max(A(1.0, Q), 1) * np.cos(w * t - lag) * (max(A(1.0, Q), 1) / amp if rr == 1.0 else 1), color=BLUE, lw=2, label="displacement x")
    ax.set_title(f"{title}  —  lag {phi(rr, Q):.0f}°", fontsize=10); ax.set_yticks([]); ax.set_xticks([])
    ax.axhline(0, color=G, lw=0.6); style(ax)
axs[0].set_ylim(-1.9, 1.15); axs[0].legend(frameon=False, labelcolor=G, fontsize=9, loc="lower left", ncol=2)
axs[1].text(0.5, -0.12, "x is a quarter cycle behind F: the force is in step with the velocity, so every push adds energy",
            transform=axs[1].transAxes, ha="center", va="top", color=BLUE, fontsize=9)
fig.tight_layout(); fig.savefig("resonance-phase.svg", transparent=True); plt.close(fig)

# ---- 3. build-up ----
fig, ax = plt.subplots(figsize=(11, 3.8)); fig.patch.set_alpha(0)
t = np.linspace(0, 40 * 2 * np.pi, 6000)
for Q, c in [(5, AMBER), (20, BLUE)]:
    g = 1 / (2 * Q)
    x = Q * (1 - np.exp(-g * t)) * np.sin(t)          # exact for w = w0: x = (Q F0/k)(1 - e^{-γt}) sin ω0 t
    ax.plot(t / (2 * np.pi), x, color=c, lw=1.1, label=f"Q = {Q}: settles in about {3*Q/np.pi:.0f} cycles")
    ax.plot(t / (2 * np.pi), Q * (1 - np.exp(-g * t)), color=c, lw=0.9, ls="--")
    ax.plot(t / (2 * np.pi), -Q * (1 - np.exp(-g * t)), color=c, lw=0.9, ls="--")
ax.set_xlabel("cycles since the driver was switched on"); ax.set_ylabel("x ÷ static deflection")
ax.set_title("switched on at the natural frequency: the ring grows to Q × static deflection, taking about Q/π cycles to reach 63 %")
ax.legend(frameon=False, labelcolor=G, fontsize=9, loc="upper left"); style(ax)
fig.tight_layout(); fig.savefig("resonance-buildup.svg", transparent=True); plt.close(fig)
print("wrote resonance-curves.svg resonance-phase.svg resonance-buildup.svg")
