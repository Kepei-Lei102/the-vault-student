"""Rectification and smoothing, simulated — ideal diodes, a real RC decay.

The rectifier output follows the input whenever the input can push charge into the
capacitor (|Vin| > Vc); otherwise the capacitor discharges through the load with
Vc = V exp(-t/RC). Checks the two Paper 4 questions against the scheme's shortcut:
  June 2022 P41 Q5(c): R = 1.2 kOhm, Vin = 6.0 sin 25 pi t (T = 0.08 s), ripple 10% -> C
  June 2025 P44 Q8(b): full-wave, ripple 33% of V0 -> time constant in terms of T

Run:  python3 alternating-current-rectifier.py   -> alternating-current-rectification.svg
"""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
G = "#888"

def smooth(t, vin_abs, tau):
    """capacitor voltage for an ideal full-wave rectifier feeding R || C."""
    v = np.zeros_like(t); v[0] = vin_abs[0]; dt = t[1]-t[0]
    for i in range(1, len(t)):
        decayed = v[i-1]*np.exp(-dt/tau)
        v[i] = max(decayed, vin_abs[i])
    return v

def ripple(tau_over_T, halfwave=False, n=200000):
    T = 1.0; t = np.linspace(0, 6*T, n); vin = np.sin(2*np.pi*t/T)
    src = np.maximum(vin, 0) if halfwave else np.abs(vin)
    v = smooth(t, src, tau_over_T*T)
    last = v[t > 4*T]
    return last.max() - last.min()

# June 2025 P44 Q8: 33% ripple, full-wave. Scheme: discharge time read as 11T/30, tau = 0.90 T
tau = 0.90
print(f"full-wave, tau = 0.90 T: simulated ripple = {100*ripple(tau):.1f}% of V0 (scheme reads 33% -> tau = 0.90 T)")
# invert: what tau gives exactly 33%?
lo, hi = 0.2, 3.0
for _ in range(40):
    mid = (lo+hi)/2
    if ripple(mid, n=60000) > 0.33: lo = mid
    else: hi = mid
print(f"exact tau for a 33% ripple (full-wave): {mid:.2f} T   — the scheme's graphical shortcut is within 3%")
# June 2022 P41 Q5: half-wave? No — four diodes, full-wave. T = 0.08 s, R = 1200, ripple 10%.
T = 0.08; R = 1200.0
lo, hi = 0.2, 20.0
for _ in range(40):
    mid = (lo+hi)/2
    if ripple(mid, n=60000) > 0.10: lo = mid
    else: hi = mid
C = mid*T/R
print(f"June 2022 P41 Q5(c)(iii): 10% ripple -> tau = {mid:.2f} T = {mid*T:.3f} s -> C = {C*1e6:.0f} uF  (scheme: 0.034 s discharge, C = 270 uF)")

# figure: half-wave, full-wave, smoothed (three tau values)
t = np.linspace(0, 3, 3000); vin = np.sin(2*np.pi*t)
fig, ax = plt.subplots(1, 3, figsize=(13, 3.6)); fig.patch.set_alpha(0)
ax[0].plot(t, vin, color=G, lw=1, ls=":"); ax[0].plot(t, np.maximum(vin, 0), color="#2563eb", lw=2); ax[0].set_title("half-wave: one diode, half the cycles wasted", color=G, fontsize=10)
ax[1].plot(t, vin, color=G, lw=1, ls=":"); ax[1].plot(t, np.abs(vin), color="#7c3aed", lw=2); ax[1].set_title("full-wave: four diodes, the negative halves flipped up", color=G, fontsize=10)
ax[2].plot(t, np.abs(vin), color="#7c3aed", lw=1, ls=":")
for tau_T, col, lab in [(0.3, "#dc2626", "RC = 0.3 T"), (0.9, "#f59e0b", "RC = 0.9 T  (ripple 33%, June 2025 P44)"), (5.0, "#059669", "RC = 5 T")]:
    ax[2].plot(t, smooth(t, np.abs(vin), tau_T), color=col, lw=2, label=lab)
ax[2].set_title("smoothed: a capacitor across the load", color=G, fontsize=10)
leg = ax[2].legend(loc="lower right", fontsize=8, frameon=False)
for tx in leg.get_texts(): tx.set_color(G)
for a in ax:
    a.set_facecolor("none"); a.tick_params(colors=G); a.set_xlabel("time / periods", color=G); a.set_ylim(-1.15, 1.15)
    a.axhline(0, color=G, lw=0.8)
    for s in a.spines.values(): s.set_color(G)
ax[0].set_ylabel("V / V0", color=G)
fig.tight_layout(); fig.savefig("alternating-current-rectification.svg", transparent=True); print("wrote alternating-current-rectification.svg")
