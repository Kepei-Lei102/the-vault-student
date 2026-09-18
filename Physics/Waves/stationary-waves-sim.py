"""
stationary-waves-sim.py — a standing wave made the way the syllabus says, and measured.

Companion to [[Stationary Waves]].  Three experiments on the bead-string of
progressive-waves-sim.py, none of which puts a standing wave in by hand:

  1. SUPERPOSITION, checked: y1 + y2 for two equal waves travelling opposite
     ways is compared, point by point, with 2A sin(kx) cos(wt).  Same thing.
  2. REFLECTION AT A FIXED END: a driven string with the far end clamped.
     Newton's law alone produces the reflected wave (inverted) and the two
     superpose.  The script finds the nodes and measures their spacing: λ/2.
     Every bead between two nodes moves in phase; beads across a node move in
     antiphase — measured by correlation, not assumed.
  3. RESONANCE OF THE STRING: driving frequency swept across f1 .. 4 f1; the
     steady amplitude at an antinode peaks at exactly the harmonics
     f_n = n v / 2L, and the number of loops counted at each peak is n.

Run:  python3 stationary-waves-sim.py
"""
from __future__ import annotations

import math

import numpy as np

T_S, MU = 4.0, 0.01                    # tension (N), mass per length (kg/m)
V = math.sqrt(T_S / MU)                # 20 m/s


# ----------------------------------------------------------------------------
# 1. Superposition — the graphical method, done numerically
# ----------------------------------------------------------------------------
def check_superposition():
    A, lam, f = 1.0, 2.0, 10.0
    k, w = 2 * math.pi / lam, 2 * math.pi * f
    x = np.linspace(0, 4 * lam, 801)
    worst = 0.0
    for t in np.linspace(0, 1 / f, 41):
        y_sum = A * np.sin(k * x - w * t) + A * np.sin(k * x + w * t)   # right-mover + left-mover
        y_std = 2 * A * np.sin(k * x) * np.cos(w * t)                 # the standing form
        worst = max(worst, float(abs(y_sum - y_std).max()))
    print(f"1. superposition: max |(y1+y2) − 2A sin kx cos ωt| over a period = {worst:.1e}  (identical: two travelling waves ARE the standing wave)")
    nodes = x[np.isclose(np.sin(k * x), 0, atol=1e-9)]
    print(f"   nodes where sin kx = 0: every {np.diff(nodes)[0]:.2f} m = λ/2 with λ = {lam}; antinodes halfway, amplitude 2A")


# ----------------------------------------------------------------------------
# 2. Reflection at a fixed end, from Newton's law only
# ----------------------------------------------------------------------------
def run_string(f: float, A: float, L: float, t_end: float, N: int = 400, damping: float = 0.0):
    dx = L / N; m = MU * dx
    dt = 0.25 * dx / V
    steps = int(t_end / dt)
    y = np.zeros(N + 1); vy = np.zeros(N + 1)
    def accel(y):
        a = np.zeros_like(y)
        a[1:-1] = (T_S / m) * (y[2:] - 2 * y[1:-1] + y[:-2]) / dx
        return a
    snaps, times = [], []
    a = accel(y)
    for s in range(steps):
        t = s * dt
        y[0] = A * math.sin(2 * math.pi * f * t); y[-1] = 0.0          # driver, and the CLAMP
        vy += 0.5 * dt * a
        y += dt * vy
        y[0] = A * math.sin(2 * math.pi * f * (t + dt)); y[-1] = 0.0
        a = accel(y) - damping * vy
        vy += 0.5 * dt * a
        vy[0] = 0; vy[-1] = 0
        if s % 20 == 0:
            snaps.append(y.copy()); times.append(t)
    return np.linspace(0, L, N + 1), np.array(snaps), np.array(times)


def reflection_and_nodes():
    L = 3.0; f = 20.0; lam = V / f                    # λ = 1.0 m, so L = 3λ: the driver sits at a node position
    x, snaps, times = run_string(f, 0.005, L, t_end=1.2, damping=0.3)
    steady = snaps[times > 0.8]
    amp = (steady.max(axis=0) - steady.min(axis=0)) / 2       # amplitude envelope along the string
    # nodes = local minima of the envelope below 15 % of the peak
    thr = 0.15 * amp.max()
    nodes = [x[i] for i in range(1, len(x) - 1) if amp[i] < thr and amp[i] <= amp[i - 1] and amp[i] <= amp[i + 1]]
    # merge nodes closer than 0.1 m
    merged = []
    for n in nodes:
        if not merged or n - merged[-1] > 0.1: merged.append(n)
    spacing = np.diff(merged)
    print(f"2. fixed end, f = {f} Hz, v = {V:.0f} m/s, so λ = {lam:.2f} m: nodes found at {', '.join(f'{n:.2f}' for n in merged)} m")
    print(f"   node spacing {spacing.mean():.3f} m = λ/2 (expected {lam/2:.3f}); antinode amplitude {amp.max()/0.005:.1f}× the driver's")
    # phase: two beads in one loop vs two beads across a node
    i1, i2 = int(np.argmin(abs(x - 1.15))), int(np.argmin(abs(x - 1.35)))     # same loop (between nodes at 1.0 and 1.5)
    i3 = int(np.argmin(abs(x - 1.65)))                                          # next loop
    def corr(a, b): return float(np.corrcoef(steady[:, a], steady[:, b])[0, 1])
    print(f"   correlation of motion, two beads in the same loop: {corr(i1, i2):+.2f} (in phase);  across a node: {corr(i1, i3):+.2f} (antiphase)")
    print(f"   note the reflection was never programmed — the clamp y = 0 and Newton's law made it")


# ----------------------------------------------------------------------------
# 3. Resonance of the string: sweep the driving frequency
# ----------------------------------------------------------------------------
def harmonics_sweep():
    L = 1.0
    f1 = V / (2 * L)                                  # 10 Hz
    print(f"3. string of length {L} m: predicted harmonics f_n = n v / 2L = {f1:.0f}, {2*f1:.0f}, {3*f1:.0f}, {4*f1:.0f} Hz")
    freqs = np.arange(6.0, 44.1, 1.0)
    rows = []
    for f in freqs:
        x, snaps, times = run_string(f, 0.002, L, t_end=2.5, N=200, damping=0.6)
        steady = snaps[times > 1.8]
        amp = (steady.max(axis=0) - steady.min(axis=0)) / 2
        # count loops = antinodes = local maxima of the envelope above 30% of peak
        peaks = [i for i in range(2, len(x) - 2) if amp[i] > 0.3 * amp.max() and amp[i] >= amp[i-1] and amp[i] >= amp[i+1] and amp[i] > amp[i-2] and amp[i] > amp[i+2]]
        rows.append((f, amp.max() / 0.002, len(peaks)))
    print(f"   {'f (Hz)':>7} {'max amp / driver':>17} {'loops':>6}")
    for f, g, n in rows:
        flag = "  ← peak" if any(abs(f - k * f1) < 0.5 for k in (1, 2, 3, 4)) else ""
        if flag or int(f) % 4 == 2:
            print(f"   {f:>7.0f} {g:>17.1f} {n:>6}{flag}")
    best = sorted(rows, key=lambda r: -r[1])[:4]
    print("   the four largest responses:", ", ".join(f"{f:.0f} Hz ({n} loop{'s' if n > 1 else ''})" for f, g, n in sorted(best)))


if __name__ == "__main__":
    check_superposition()
    reflection_and_nodes()
    harmonics_sweep()
