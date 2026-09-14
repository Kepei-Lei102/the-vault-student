"""Forced oscillations, checked by brute force.

The card claims a steady-state amplitude and phase lag for
    m x'' + b x' + k x = F0 cos(w t):
    A = (F0/m) / sqrt((w0^2 - w^2)^2 + (b w / m)^2),   tan(phi) = (b w / m) / (w0^2 - w^2).
This script integrates the equation with a fourth-order Runge-Kutta stepper,
waits for the transient to die, measures A and phi from the motion itself, and
prints them beside the formula.  Then it times how long the ring takes to
build up at resonance and compares with the card's "about Q/pi cycles to 63 %".

Run:  python3 resonance-sim.py            (m = k = 1, so w0 = 1 and Q = 1/b)
"""
import math

def simulate(Q, w, F0=1.0, cycles_settle=None, dt=None):
    m = k = 1.0; w0 = 1.0; b = 1.0 / Q
    gamma = b / (2 * m)
    T = 2 * math.pi / w
    if cycles_settle is None:
        cycles_settle = int(12 * Q / (w0 * T) * 1.0) + 5   # ~12/gamma of settling time, in driving periods
    dt = dt or T / 400
    def acc(t, x, v):
        return (F0 * math.cos(w * t) - b * v - k * x) / m
    x, v, t = 0.0, 0.0, 0.0
    n_settle = int(cycles_settle * T / dt)
    for _ in range(n_settle):
        k1x, k1v = v, acc(t, x, v)
        k2x, k2v = v + 0.5*dt*k1v, acc(t + 0.5*dt, x + 0.5*dt*k1x, v + 0.5*dt*k1v)
        k3x, k3v = v + 0.5*dt*k2v, acc(t + 0.5*dt, x + 0.5*dt*k2x, v + 0.5*dt*k2v)
        k4x, k4v = v + dt*k3v, acc(t + dt, x + dt*k3x, v + dt*k3v)
        x += dt*(k1x + 2*k2x + 2*k3x + k4x)/6; v += dt*(k1v + 2*k2v + 2*k3v + k4v)/6; t += dt
    # fit x(t) = C cos(wt) + S sin(wt) over two more periods (least squares on an orthogonal basis)
    n_fit = int(2 * T / dt); sc = ss = 0.0
    for _ in range(n_fit):
        k1x, k1v = v, acc(t, x, v)
        k2x, k2v = v + 0.5*dt*k1v, acc(t + 0.5*dt, x + 0.5*dt*k1x, v + 0.5*dt*k1v)
        k3x, k3v = v + 0.5*dt*k2v, acc(t + 0.5*dt, x + 0.5*dt*k2x, v + 0.5*dt*k2v)
        k4x, k4v = v + dt*k3v, acc(t + dt, x + dt*k3x, v + dt*k3v)
        x += dt*(k1x + 2*k2x + 2*k3x + k4x)/6; v += dt*(k1v + 2*k2v + 2*k3v + k4v)/6; t += dt
        sc += x * math.cos(w * t) * dt; ss += x * math.sin(w * t) * dt
    C, S = 2 * sc / (2 * T), 2 * ss / (2 * T)          # x = C cos wt + S sin wt = A cos(wt - phi)
    A = math.hypot(C, S); phi = math.atan2(S, C)
    A_th = (F0 / m) / math.hypot(w0**2 - w**2, b * w / m)
    phi_th = math.atan2(b * w / m, w0**2 - w**2)
    return A, phi, A_th, phi_th

Q = 10
print(f"Q = {Q}: steady state, simulated vs formula (amplitude in units of the static deflection F0/k)\n")
print(f"{'w/w0':>6} {'A sim':>9} {'A formula':>10} {'lag sim':>9} {'lag formula':>12}")
for r in (0.5, 0.8, 0.9, 0.95, 1.0, 1.05, 1.1, 1.25, 2.0):
    A, phi, A_th, phi_th = simulate(Q, r)
    print(f"{r:6.2f} {A:9.4f} {A_th:10.4f} {math.degrees(phi):8.1f}° {math.degrees(phi_th):11.1f}°")

print("\nAt resonance the peak is Q times the static deflection;")
print("the half-power points sit at w0(1 ± 1/2Q): width w0/Q.\n")

# build-up at resonance from rest: envelope A(1 - e^{-gamma t}); 63 % after 1/gamma = 2Q/w0 = Q/pi periods
print("Build-up at resonance from rest -- cycles needed to reach 63 % and 95 % of the final amplitude")
print(f"{'Q':>4} {'63% sim':>9} {'Q/pi':>7} {'95% sim':>9} {'3Q/pi':>7}")
for Q in (5, 10, 20):
    b = 1.0 / Q; w = 1.0; T = 2 * math.pi; dt = T / 400
    x, v, t = 0.0, 0.0, 0.0; peaks = []; last_x, last_v = 0.0, 0.0
    A_final = Q
    hit63 = hit95 = None
    def acc(t, x, v): return math.cos(t) - b * v - x
    for i in range(int(6 * Q * T / dt)):
        k1x, k1v = v, acc(t, x, v)
        k2x, k2v = v + 0.5*dt*k1v, acc(t + 0.5*dt, x + 0.5*dt*k1x, v + 0.5*dt*k1v)
        k3x, k3v = v + 0.5*dt*k2v, acc(t + 0.5*dt, x + 0.5*dt*k2x, v + 0.5*dt*k2v)
        k4x, k4v = v + dt*k3v, acc(t + dt, x + dt*k3x, v + dt*k3v)
        nx = x + dt*(k1x + 2*k2x + 2*k3x + k4x)/6; nv = v + dt*(k1v + 2*k2v + 2*k3v + k4v)/6
        if v > 0 and nv <= 0:          # a positive peak
            if hit63 is None and x >= 0.63 * A_final: hit63 = t / T
            if hit95 is None and x >= 0.95 * A_final: hit95 = t / T
        x, v, t = nx, nv, t + dt
    print(f"{Q:4d} {hit63:9.1f} {Q/math.pi:7.1f} {hit95:9.1f} {3*Q/math.pi:7.1f}")
