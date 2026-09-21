"""Specific Heat Capacity — two experiments run in numbers, and their two figures.

1. electrical_method()  — a 1.00 kg aluminium block (true c = 900 J/kg/K) with a 48 W immersion heater.
                          The block also loses energy to the room at a rate proportional to its excess
                          temperature, so the measured c = Pt / (m * rise) comes out too LARGE.
                          How much too large, with and without insulation, and how to beat it.
2. evaporation()        — a million molecules with a thermal spread of kinetic energies.  Let only the
                          fastest escape from the surface and the average energy of those left behind
                          falls: the liquid cools.  A breeze stops escaped molecules falling back.

Run:  python3 specific-heat-lab.py      (numpy + matplotlib; writes two SVGs beside this script)
"""
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
GREY, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": GREY, "axes.labelcolor": GREY, "axes.edgecolor": GREY, "xtick.color": GREY,
                     "ytick.color": GREY, "font.size": 11, "svg.fonttype": "none", "font.family": "DejaVu Sans"})


def save(fig, name):
    path = os.path.join(HERE, name)
    fig.savefig(path, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)
    s = open(path).read()
    s = re.sub(r'<svg([^>]*?) width="[^"]*" height="[^"]*"', r'<svg\1 width="100%"', s, count=1)
    open(path, "w").write(s)
    print("  wrote", name)


def heat(m, c, P, k, minutes, dt=0.5):
    """dE = (P - k * excess) dt.  k is the loss rate in watts per kelvin above the room."""
    t = np.arange(0, minutes * 60 + dt, dt)
    rise = np.zeros_like(t)
    for i in range(1, len(t)):
        rise[i] = rise[i - 1] + (P - k * rise[i - 1]) * dt / (m * c)
    return t, rise


def electrical_method(m=1.00, c=900.0, P=48.0):
    runs = {"no losses (ideal)": 0.0, "lagged with insulation": 0.25, "bare block": 1.2}
    out = {}
    for name, k in runs.items():
        t, rise = heat(m, c, P, k, 10)
        measured = P * t[-1] / (m * rise[-1])
        early = P * 120 / (m * rise[t == 120][0])
        out[name] = (t, rise)
        print(f"  {name:24s} rise after 10 min {rise[-1]:5.1f} K  ->  c = Pt/(m rise) = {measured:5.0f} J/kg/K "
              f"({100*(measured-c)/c:+5.1f} %);  using only the first 2 min: {early:4.0f}")
    print(f"  (true value {c:.0f}.  Every loss makes the rise smaller, so the answer is always too big, never too small.)")
    fig, ax = plt.subplots(figsize=(10, 5.6))
    for (name, (t, rise)), col in zip(out.items(), (GREEN, AMBER, RED)):
        ax.plot(t / 60, rise, color=col, lw=2.2, label=name)
    ax.set_xlabel("heating time / minutes"); ax.set_ylabel("temperature rise / K")
    ax.set_title("1.00 kg of aluminium, 48 W heater: the losses bend the line", color=GREY, fontsize=12, loc="left")
    ax.annotate("same gradient at the start:\nnothing has warmed up enough to leak yet", (1.2, 3.6), xytext=(2.3, 0.6), fontsize=10, color=GREY,
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, labelcolor=GREY, loc="upper left")
    save(fig, "specific-heat-electrical-method.svg")


def evaporation(n=1_000_000, seed=5):
    rng = np.random.default_rng(seed)
    E = rng.gamma(1.5, 1.0, n)                    # kinetic energies in units of kT: mean 1.5
    escape = 6.0                                  # energy needed to break free of the neighbours, in kT
    gone = E > escape
    print(f"  mean kinetic energy before: {E.mean():.3f} kT;  fraction able to escape: {100*gone.mean():.2f} %")
    print(f"  mean energy of the escapers: {E[gone].mean():.2f} kT;  of those left behind: {E[~gone].mean():.3f} kT")
    print(f"  one round of escapes cools the liquid by {100*(1 - E[~gone].mean()/E.mean()):.1f} % in absolute temperature "
          f"(about {293*(1 - E[~gone].mean()/E.mean()):.0f} K at room temperature)")
    print(f"  each escaper carried {E[gone].mean()/E.mean():.1f} times the average share")
    fig, ax = plt.subplots(figsize=(10, 5.2))
    bins = np.linspace(0, 10, 101)
    ax.hist(E[~gone], bins=bins, color=matplotlib.colors.to_rgba(BLUE, 0.35), edgecolor=BLUE, lw=0.4, label="stay in the liquid")
    ax.hist(E[gone], bins=bins, color=matplotlib.colors.to_rgba(RED, 0.55), edgecolor=RED, lw=0.4, label="energetic enough to escape from the surface")
    ax.axvline(E.mean(), color=GREY, ls="--", lw=1.2); ax.text(E.mean() + 0.1, ax.get_ylim()[1] * 0.92, "average before", fontsize=10)
    ax.axvline(escape, color=RED, ls=":", lw=1.2)
    ax.set_yscale("log"); ax.set_xlabel("kinetic energy of a molecule / kT"); ax.set_ylabel("number of molecules (log scale)")
    ax.set_title("Evaporation takes the fast ones, so the average falls", color=GREY, fontsize=12, loc="left")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, labelcolor=GREY, loc="upper right", bbox_to_anchor=(1, 0.86))
    save(fig, "specific-heat-evaporation.svg")


if __name__ == "__main__":
    print("1. the electrical method, with honest losses")
    electrical_method()
    print("\n2. evaporation as the escape of the fastest molecules")
    evaporation()
