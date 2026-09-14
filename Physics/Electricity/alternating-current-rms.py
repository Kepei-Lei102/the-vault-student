"""Why r.m.s. — the square, the mean, the root, drawn.

I = I0 sin(wt). Power in a resistor is I^2 R, so what matters for heating is the
MEAN of I^2, not the mean of I (which is zero). sin^2 averages to 1/2 over a cycle,
so <I^2> = I0^2 / 2 and the steady current with the same heating is I0/sqrt(2).
The second row is the June 2021 Paper 42 Q10 square wave: I^2 is constant, so
r.m.s. = peak.

Run:  python3 alternating-current-rms.py   -> alternating-current-rms.svg
"""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
G = "#888"; I0 = 2.6
t = np.linspace(0, 2, 2000)
sine = I0*np.sin(2*np.pi*t)
square = 2.0*np.sign(np.sin(2*np.pi*t + 1e-9))
print(f"sine: mean I = {sine.mean():+.3f}, mean I^2 = {np.mean(sine**2):.3f} = I0^2/2 = {I0**2/2:.3f}, rms = {np.sqrt(np.mean(sine**2)):.3f} = I0/sqrt2 = {I0/np.sqrt(2):.3f}")
print(f"square: mean I^2 = {np.mean(square**2):.3f}, rms = {np.sqrt(np.mean(square**2)):.3f} = peak")
fig, ax = plt.subplots(2, 2, figsize=(11, 6.2)); fig.patch.set_alpha(0)
for row, (I, name) in enumerate([(sine, "sinusoidal, peak 2.6 A"), (square, "square wave, peak 2.0 A (June 2021 P42 Q10)")]):
    a = ax[row, 0]; a.plot(t, I, color="#2563eb", lw=2); a.axhline(0, color=G, lw=0.8)
    a.axhline(I.mean(), color="#dc2626", lw=1.2, ls="--"); a.text(1.02, I.mean()+0.15, f"mean I = {I.mean():.1f} A", color="#dc2626", fontsize=9)
    a.set_title(f"current: {name}", color=G, fontsize=10); a.set_ylabel("I / A", color=G); a.set_ylim(-3.2, 3.2)
    b = ax[row, 1]; b.plot(t, I**2, color="#7c3aed", lw=2); b.axhline(0, color=G, lw=0.8)
    m = np.mean(I**2); b.axhline(m, color="#059669", lw=1.6, ls="--")
    b.text(1.02, m+0.35, f"mean of I² = {m:.2f} A²  ->  r.m.s. = √{m:.2f} = {np.sqrt(m):.2f} A", color="#059669", fontsize=9)
    b.set_title("the square, and its mean (this is what heats the resistor)", color=G, fontsize=10); b.set_ylabel("I² / A²", color=G); b.set_ylim(-0.5, 7.8)
    if row == 0: b.axhline(I0**2, color="#f59e0b", lw=1, ls=":"); b.text(1.02, I0**2+0.2, "peak² = 6.76 A² — the mean is exactly half", color="#f59e0b", fontsize=9)
for a in ax.flat:
    a.set_facecolor("none"); a.tick_params(colors=G); a.set_xlabel("time / periods", color=G)
    for s in a.spines.values(): s.set_color(G)
fig.tight_layout(); fig.savefig("alternating-current-rms.svg", transparent=True); print("wrote alternating-current-rms.svg")
