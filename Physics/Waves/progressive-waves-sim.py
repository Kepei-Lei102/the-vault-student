"""
progressive-waves-sim.py — a wave is coupled SHM, run for real.

Companion to [[Progressive Waves]].

A string is modelled as N beads of mass m joined by massless segments under
tension T (the model the card's "coupled oscillators" section describes). The
left end is driven in SHM at frequency f; the right end is fixed but too far
away to matter. Newton's second law is integrated bead by
bead (velocity Verlet). Nothing about waves is put in — no wavelength, no
speed, no v = f·lambda — and the script then MEASURES:

  1. the wave speed, by timing the front's arrival at two markers;
  2. the wavelength, from the distance between successive crests;
  3. that v = f·lambda holds to the numerical accuracy of the model;
  4. that v = sqrt(T/mu) — the speed set by the medium, not by the driver:
     doubling f halves lambda and leaves v unchanged;
  5. that the energy carried per unit time grows as amplitude², from the
     work done by the driver;
  6. that a bead in the middle moves ONLY transversely — its x never changes.

Run:  python3 progressive-waves-sim.py
"""
from __future__ import annotations

import math

import numpy as np


def run(f: float, A: float, T: float = 4.0, mu: float = 0.01, L: float = 60.0, N: int = 3000,
        t_end: float = 2.0):
    """Simulate; return (x positions, history of y snapshots, times, driver power)."""
    dx = L / N
    m = mu * dx
    v_theory = math.sqrt(T / mu)
    dt = 0.25 * dx / v_theory                      # comfortably inside the stability limit
    steps = int(t_end / dt)
    x = np.linspace(0, L, N + 1)
    y = np.zeros(N + 1); vy = np.zeros(N + 1)

    def accel(y):
        a = np.zeros_like(y)
        a[1:-1] = (T / m) * (y[2:] - 2 * y[1:-1] + y[:-2]) / dx    # transverse force from the two neighbours
        return a

    snaps, times = [], []
    power_acc = 0.0; power_n = 0
    a = accel(y)
    for s in range(steps):
        t = s * dt
        y[0] = A * math.sin(2 * math.pi * f * t)                   # the driver
        vy[0] = A * 2 * math.pi * f * math.cos(2 * math.pi * f * t)
        vy += 0.5 * dt * a
        y += dt * vy
        y[0] = A * math.sin(2 * math.pi * f * (t + dt)); y[-1] = 0.0
        a = accel(y)
        vy += 0.5 * dt * a
        vy[0] = A * 2 * math.pi * f * math.cos(2 * math.pi * f * (t + dt)); vy[-1] = 0.0
        # power delivered by the driver = (transverse force from bead 1 on bead 0) * (driver velocity)
        if t > t_end * 0.6:                                        # steady state only
            F = T * (y[1] - y[0]) / dx                              # pull of the string on the driven end
            power_acc += -F * vy[0]; power_n += 1                  # driver works against that pull
        if s % 10 == 0:
            snaps.append(y.copy()); times.append(t)
    Pth = 0.5 * mu * (2 * math.pi * f) ** 2 * A ** 2 * v_theory       # the textbook power of a string wave
    return x, np.array(snaps), np.array(times), power_acc / power_n, v_theory, Pth


def measure_speed(x, snaps, times, A):
    """Time at which the disturbance first exceeds A/10 at two marker positions."""
    marks = [0.8, 2.0]
    arr = []
    for xm in marks:
        i = int(np.argmin(abs(x - xm)))
        k = int(np.argmax(abs(snaps[:, i]) > A / 10))
        arr.append(times[k])
    return (marks[1] - marks[0]) / (arr[1] - arr[0])


def measure_wavelength(x, snap, lo=0.5, hi=5.5):
    """Distance between successive crests in the steady region."""
    sel = (x > lo) & (x < hi)
    xs, ys = x[sel], snap[sel]
    crests = [xs[i] for i in range(1, len(ys) - 1) if ys[i] > ys[i - 1] and ys[i] >= ys[i + 1] and ys[i] > 0]
    gaps = np.diff(crests)
    return float(np.mean(gaps)), len(crests)


def main():
    T, mu = 4.0, 0.01
    print(f"string: tension {T} N, mass per length {mu} kg/m  ->  sqrt(T/mu) = {math.sqrt(T/mu):.1f} m/s")
    print(f"{'f (Hz)':>7} {'A (m)':>6} {'v measured':>11} {'lambda':>8} {'f*lambda':>9} {'power (W)':>10} {'½μω²A²v':>9}")
    results = []
    for f, A in ((10.0, 0.02), (20.0, 0.02), (10.0, 0.04)):
        x, snaps, times, P, v_th, Pth = run(f, A, T, mu)
        v = measure_speed(x, snaps, times, A)
        lam, n = measure_wavelength(x, snaps[-1])
        results.append((f, A, v, lam, P))
        print(f"{f:>7.1f} {A:>6.2f} {v:>9.1f} m/s {lam:>6.3f} m {f*lam:>7.1f} m/s {P:>10.4f} {Pth:>9.4f}")
    (f1, A1, v1, l1, P1), (f2, A2, v2, l2, P2), (f3, A3, v3, l3, P3) = results
    assert abs(v1 - 20) / 20 < 0.05 and abs(v2 - 20) / 20 < 0.05, "speed should be sqrt(T/mu) = 20 m/s"
    assert abs(f1 * l1 - 20) / 20 < 0.05 and abs(f2 * l2 - 20) / 20 < 0.05, "v = f lambda"
    print(f"\ndoubling f: lambda {l1:.3f} -> {l2:.3f} m (ratio {l1/l2:.2f}), speed unchanged — the medium sets v, the source sets f")
    print(f"doubling A: power {P1:.4f} -> {P3:.4f} W (ratio {P3/P1:.2f}) — energy flow grows as A²")
    # transverse-only motion: bead x never changes by construction; show the y-motion of one bead is SHM
    x, snaps, times, *_ = run(10.0, 0.02, T, mu)
    i = int(np.argmin(abs(x - 1.5)))
    ys = snaps[times > 1.2, i]; ts = times[times > 1.2]
    amp = (ys.max() - ys.min()) / 2
    # fit period from zero crossings
    zc = ts[1:][(ys[:-1] < 0) & (ys[1:] >= 0)]
    Tm = float(np.mean(np.diff(zc)))
    print(f"bead at x = 1.5 m: amplitude {amp:.4f} m (driver 0.0200), period {Tm:.4f} s (driver {1/10:.4f}) — every bead does the driver's SHM, late")
    # phase difference between two beads a quarter wavelength apart
    j = int(np.argmin(abs(x - (1.5 + l1 / 4))))
    yi = snaps[times > 1.2, i]; yj = snaps[times > 1.2, j]
    lag = np.argmax(np.correlate(yj - yj.mean(), yi - yi.mean(), "full")) - (len(yi) - 1)
    dt_snap = times[1] - times[0]
    print(f"bead a quarter wavelength further on lags by {lag*dt_snap:.4f} s = {lag*dt_snap*10:.2f} T  (expected 0.25 T = 90 degrees)")


if __name__ == "__main__":
    main()
