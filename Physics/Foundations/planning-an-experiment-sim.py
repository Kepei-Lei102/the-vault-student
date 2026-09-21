"""Planning an Experiment — the numbers behind the card.

Every rule of a good plan is a claim about what happens to the answer if you break it.
Each function below breaks one rule on a simulated bench and measures the damage.

1. range_and_number()  — resistance of a wire against its length.  Same instruments, same
                         noise; only the plan differs: how many lengths, how widely spread,
                         repeated or not.  The spread of the fitted gradient over 4000
                         simulated experiments is the price of each plan.
2. two_points()        — a filament lamp's V–I curve sampled at 2 points and at 6.  Two
                         points always make a perfect straight line; the curve is invisible.
3. uncontrolled()      — cooling under insulation of different thickness, with the starting
                         temperature (a) controlled, (b) drifting downward as the kettle
                         cools between trials.  The drift is a confounder: it fakes part of
                         the effect being investigated, or hides part of it, depending only
                         on the order the trials were done in.
4. timing()            — timing one swing of a pendulum against timing twenty, with a human
                         reaction-time error on the start and the stop.

Run:  python3 planning-an-experiment-sim.py
"""
import os
import numpy as np

S = os.environ.get("VAULT_SCRATCH", "/tmp")
rng = np.random.default_rng(11)

# --------------------------------------------------------------------------------------
# 1. Range and number of readings
# --------------------------------------------------------------------------------------
TRUE_K = 5.20          # ohm per metre: constantan, 0.35 mm diameter
SIGMA_R = 0.08         # ohm: what a 0.01 A ammeter and 0.01 V voltmeter give on ~2 ohm


def fitted_gradient(lengths, repeats=1):
    R = TRUE_K * lengths + rng.normal(0, SIGMA_R, (repeats, len(lengths)))
    return np.polyfit(lengths, R.mean(axis=0), 1)[0]


def range_and_number(trials=4000):
    plans = {
        "2 lengths, 0.40–0.60 m":              (np.linspace(0.40, 0.60, 2), 1),
        "5 lengths, 0.40–0.60 m (narrow)":     (np.linspace(0.40, 0.60, 5), 1),
        "2 lengths, 0.10–1.00 m":              (np.linspace(0.10, 1.00, 2), 1),
        "5 lengths, 0.10–1.00 m (wide)":       (np.linspace(0.10, 1.00, 5), 1),
        "5 lengths, wide, each repeated ×3":   (np.linspace(0.10, 1.00, 5), 3),
        "10 lengths, wide":                    (np.linspace(0.10, 1.00, 10), 1),
    }
    out = {}
    for name, (L, rep) in plans.items():
        g = np.array([fitted_gradient(L, rep) for _ in range(trials)])
        out[name] = g.std()
        print(f"  {name:36s} gradient = {g.mean():.2f} ± {g.std():.3f} Ω/m   ({100*g.std()/TRUE_K:4.1f} %)")
    np.save(f"{S}/plan-gradient-spreads.npy", np.array(list(out.values())))
    return out


# --------------------------------------------------------------------------------------
# 2. Two points always make a line
# --------------------------------------------------------------------------------------
def lamp_current(V):
    """A 6 V filament lamp: resistance rises as the filament heats, I ∝ V^0.6 roughly."""
    return 0.30 * (V / 6.0) ** 0.6


def two_points():
    for n in (2, 6):
        V = np.linspace(1.0, 6.0, n)
        I = lamp_current(V)
        m, c = np.polyfit(I, V, 1)
        resid = V - (m * I + c)
        print(f"  {n} readings: straight-line fit V = {m:.1f} I + {c:.2f};  largest miss {np.abs(resid).max():.3f} V"
              + ("   <- a perfect line, and a wrong conclusion" if n == 2 else "   <- the curve shows"))
    V = np.array([1.0, 6.0]); I = lamp_current(V)
    print(f"  resistance at 1 V: {V[0]/I[0]:.1f} Ω;  at 6 V: {V[1]/I[1]:.1f} Ω  (the lamp is not an ohmic conductor)")


# --------------------------------------------------------------------------------------
# 3. An uncontrolled variable
# --------------------------------------------------------------------------------------
ROOM = 22.0


def cooling_rate(thickness_mm, start_temp, minutes=5.0):
    """Newton cooling; the rate constant falls with insulation thickness."""
    k = 0.060 / (1 + 0.35 * thickness_mm)            # per minute
    end = ROOM + (start_temp - ROOM) * np.exp(-k * minutes)
    return (start_temp - end) / minutes               # °C per minute, as the exam defines it


def uncontrolled():
    thick = np.array([0, 2, 4, 6, 8], dtype=float)
    controlled = np.array([cooling_rate(t, 80.0) for t in thick])
    # the kettle is boiled once; each later trial is poured 4 °C cooler
    drifting_start = 88.0 - 4.0 * np.arange(5)
    drifting = np.array([cooling_rate(t, s) for t, s in zip(thick, drifting_start)])
    print("  thickness (mm):          ", thick)
    print("  rate, start fixed at 80°C:", np.round(controlled, 2), "°C/min")
    print("  start temperatures used:  ", drifting_start)
    print("  rate, start drifting:     ", np.round(drifting, 2), "°C/min")
    true_drop = 100 * (1 - controlled[-1] / controlled[0])
    fake_drop = 100 * (1 - drifting[-1] / drifting[0])
    print(f"  8 mm of insulation cuts the rate by {true_drop:.0f} % (controlled) but appears to cut it by {fake_drop:.0f} % (drifting)")
    # the same drift with the trials done in the opposite order: thickest insulation first
    reverse = np.array([cooling_rate(t, s) for t, s in zip(thick, drifting_start[::-1])])
    hide_drop = 100 * (1 - reverse[-1] / reverse[0])
    print("  rate, thickest first:     ", np.round(reverse, 2), "°C/min")
    print(f"  done thickest-first, the same drift makes the cut look like {hide_drop:.0f} %")
    np.save(f"{S}/plan-cooling.npy", np.vstack([thick, controlled, drifting, reverse]))
    return true_drop, fake_drop, hide_drop


# --------------------------------------------------------------------------------------
# 4. Timing one swing or twenty
# --------------------------------------------------------------------------------------
def timing(trials=20000, period=1.42, reaction_sigma=0.10):
    for n in (1, 10, 20):
        measured = n * period + rng.normal(0, reaction_sigma, trials) - rng.normal(0, reaction_sigma, trials)
        T = measured / n
        print(f"  time {n:2d} swing(s): T = {T.mean():.3f} ± {T.std():.3f} s   ({100*T.std()/period:4.1f} %)")


if __name__ == "__main__":
    print("1. range and number of readings (true gradient 5.20 Ω/m)")
    range_and_number()
    print("\n2. two points always make a line")
    two_points()
    print("\n3. an uncontrolled variable")
    uncontrolled()
    print("\n4. timing one swing or twenty (true period 1.42 s)")
    timing()
