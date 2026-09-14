"""The imaginary number earns its keep: complex impedance vs the honest differential equation.

A series RLC circuit driven by V0 cos(wt):  L dI/dt + R I + Q/C = V0 cos wt,  I = dQ/dt.
Two ways to the steady-state current:
  (1) the ODE, integrated numerically (RK4) until the transient has died;
  (2) the phasor shortcut: Z = R + j(wL - 1/(wC)),  I = V0 / Z,  amplitude |I|, phase -arg Z.
If (2) is right it must agree with (1) at every frequency. It does.

Run:  python3 alternating-current-impedance.py   -> alternating-current-resonance.svg
"""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
R, L, C, V0 = 10.0, 10e-3, 1.0e-6, 1.0
w0 = 1/np.sqrt(L*C); f0 = w0/(2*np.pi); Q = w0*L/R
print(f"R = {R} ohm, L = {L*1e3} mH, C = {C*1e6} uF -> f0 = {f0:.1f} Hz, Q = {Q:.1f}, bandwidth f0/Q = {f0/Q:.1f} Hz")

def phasor(f):
    w = 2*np.pi*f; Z = R + 1j*(w*L - 1/(w*C)); I = V0/Z
    return abs(I), np.angle(I)          # amplitude, phase of I relative to V

def ode(f, cycles=60, steps=400):
    w = 2*np.pi*f; dt = 1/(f*steps)
    y = np.array([0.0, 0.0])            # [Q, I]
    def d(t, y): return np.array([y[1], (V0*np.cos(w*t) - R*y[1] - y[0]/C)/L])
    ts, Is = [], []
    for n in range(cycles*steps):
        t = n*dt
        k1 = d(t, y); k2 = d(t+dt/2, y+dt*k1/2); k3 = d(t+dt/2, y+dt*k2/2); k4 = d(t+dt, y+dt*k3)
        y = y + dt*(k1+2*k2+2*k3+k4)/6
        if n >= (cycles-4)*steps: ts.append(t+dt); Is.append(y[1])
    ts, Is = np.array(ts), np.array(Is)
    # fit I(t) = a cos wt + b sin wt over the last four cycles -> amplitude and phase
    A = np.column_stack([np.cos(w*ts), np.sin(w*ts)]); a, b = np.linalg.lstsq(A, Is, rcond=None)[0]
    return np.hypot(a, b), -np.arctan2(b, a)   # I = A cos(wt - d): phase of I relative to V is -d

print(f"{'f / Hz':>8} {'|I| phasor':>11} {'|I| ODE':>9} {'phase phasor':>13} {'phase ODE':>10}")
for f in [300, 800, 1200, 1500, f0, 1700, 2100, 3000, 8000]:
    ap, pp = phasor(f); ao, po = ode(f)
    print(f"{f:8.0f} {ap*1e3:9.3f} mA {ao*1e3:7.3f} mA {np.degrees(pp):10.1f} deg {np.degrees(po):7.1f} deg")

fs = np.linspace(200, 6000, 1200); amp = np.array([phasor(f)[0] for f in fs]); ph = np.array([phasor(f)[1] for f in fs])
pts = [300, 800, 1200, 1500, f0, 1700, 2100, 3000, 5000]; num = [ode(f) for f in pts]
G = "#888"; fig, ax = plt.subplots(1, 2, figsize=(11, 4)); fig.patch.set_alpha(0)
ax[0].plot(fs, amp*1e3, color="#7c3aed", lw=2, label="|V0 / Z|  (complex impedance)")
ax[0].scatter(pts, [n[0]*1e3 for n in num], s=48, facecolors="none", edgecolors="#dc2626", linewidths=1.8, zorder=3, label="differential equation, integrated")
ax[0].axvline(f0, color="#f59e0b", ls="--", lw=1); ax[0].text(f0+60, 95, f"f0 = {f0:.0f} Hz", color="#f59e0b", fontsize=9)
ax[0].set_xlabel("frequency / Hz", color=G); ax[0].set_ylabel("current amplitude / mA", color=G); ax[0].set_title("series RLC, 1 V drive: resonance", color=G, fontsize=10)
ax[1].plot(fs, np.degrees(ph), color="#7c3aed", lw=2); ax[1].scatter(pts, [np.degrees(n[1]) for n in num], s=48, facecolors="none", edgecolors="#dc2626", linewidths=1.8, zorder=3)
ax[1].axhline(0, color=G, lw=0.8); ax[1].axvline(f0, color="#f59e0b", ls="--", lw=1)
ax[1].set_xlabel("frequency / Hz", color=G); ax[1].set_ylabel("phase of I relative to V / degrees", color=G); ax[1].set_title("below f0 the capacitor wins (I leads); above, the inductor (I lags)", color=G, fontsize=10)
ax[1].text(3000, 60, "capacitive: I leads V", color=G, fontsize=9); ax[1].text(3000, -70, "inductive: I lags V", color=G, fontsize=9)
leg = ax[0].legend(loc="upper right", fontsize=8, frameon=False)
for tx in leg.get_texts(): tx.set_color(G)
for a in ax:
    a.set_facecolor("none"); a.tick_params(colors=G)
    for s in a.spines.values(): s.set_color(G)
fig.tight_layout(); fig.savefig("alternating-current-resonance.svg", transparent=True); print("wrote alternating-current-resonance.svg")
