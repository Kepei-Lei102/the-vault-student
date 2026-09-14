"""
progressive-waves-figures.py — the static figures for [[Progressive Waves]].

  progressive-waves-two-graphs.svg   displacement–distance vs displacement–time, labelled
  progressive-waves-phase.svg        phase difference between points on one wave
  progressive-waves-intensity.svg    I ∝ A² and the inverse-square spread from a point source
  progressive-waves-cro.svg          a CRO trace and how time-base and Y-gain turn it into f and A
  progressive-waves-long-trans.svg   transverse and longitudinal snapshots of one particle row,
                                     with the longitudinal displacement graph beneath

All text #888, transparent background, verified light and dark.
Run:  python3 progressive-waves-figures.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

GREY = "#888"
BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"


def style(ax, xlabel="", ylabel="", title=""):
    ax.set_facecolor("none")
    for sp in ax.spines.values():
        sp.set_color(GREY)
    ax.tick_params(colors=GREY, labelsize=8)
    ax.set_xlabel(xlabel, color=GREY); ax.set_ylabel(ylabel, color=GREY)
    if title:
        ax.set_title(title, color=GREY, fontsize=10)
    ax.grid(True, color=GREY, alpha=0.18)


def two_graphs():
    lam, T, A = 2.0, 0.5, 1.5
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 3.6), dpi=100)
    fig.patch.set_alpha(0)
    x = np.linspace(0, 2 * lam, 400)
    a1.plot(x, A * np.sin(2 * np.pi * x / lam), color=BLUE, lw=2)
    a1.annotate("", (lam * 0.25, A + 0.25), (lam * 1.25, A + 0.25), arrowprops=dict(arrowstyle="<->", color=GREY))
    a1.text(lam * 0.75, A + 0.35, "wavelength λ", ha="center", color=GREY, fontsize=9)
    a1.annotate("", (lam * 1.75, 0), (lam * 1.75, -A), arrowprops=dict(arrowstyle="<->", color=RED))
    a1.text(lam * 1.75 + 0.06, -A / 2, "amplitude A", color=RED, fontsize=9, va="center")
    a1.axhline(0, color=GREY, lw=0.8)
    a1.set_ylim(-A - 0.5, A + 0.8); a1.set_xlim(0, 2 * lam)
    style(a1, "distance along the wave x / m", "displacement / cm", "Photograph: displacement against distance (t fixed)")
    a1.set_xticks([0, lam / 2, lam, 1.5 * lam, 2 * lam]); a1.set_xticklabels(["0", "1.0", "2.0", "3.0", "4.0"])
    t = np.linspace(0, 2 * T, 400)
    a2.plot(t, A * np.sin(2 * np.pi * t / T), color=TEAL, lw=2)
    a2.annotate("", (T * 0.25, A + 0.25), (T * 1.25, A + 0.25), arrowprops=dict(arrowstyle="<->", color=GREY))
    a2.text(T * 0.75, A + 0.35, "period T", ha="center", color=GREY, fontsize=9)
    a2.annotate("", (T * 1.75, 0), (T * 1.75, -A), arrowprops=dict(arrowstyle="<->", color=RED))
    a2.text(T * 1.75 + 0.015, -A / 2, "A", color=RED, fontsize=9, va="center")
    a2.axhline(0, color=GREY, lw=0.8)
    a2.set_ylim(-A - 0.5, A + 0.8); a2.set_xlim(0, 2 * T)
    style(a2, "time t / s", "displacement of ONE point / cm", "Film at one point: displacement against time (x fixed)")
    a2.set_xticks([0, T / 2, T, 1.5 * T, 2 * T]); a2.set_xticklabels(["0", "0.25", "0.50", "0.75", "1.00"])
    fig.text(0.5, -0.02, "same wave: λ = 2.0 m from the left graph, T = 0.50 s from the right, so v = λ/T = fλ = 4.0 m/s",
             ha="center", color=GREY, fontsize=9)
    fig.tight_layout()
    fig.savefig("progressive-waves-two-graphs.svg", format="svg", transparent=True, bbox_inches="tight")


def phase():
    lam = 2.0
    fig, ax = plt.subplots(figsize=(9, 3.4), dpi=100); fig.patch.set_alpha(0)
    x = np.linspace(0, 2 * lam, 400)
    ax.plot(x, np.sin(2 * np.pi * x / lam), color=BLUE, lw=2)
    pts = [(0.5, "P"), (1.0, "Q"), (1.5, "R"), (2.5, "S")]
    for xp, name in pts:
        ax.scatter([xp], [np.sin(2 * np.pi * xp / lam)], color=AMBER, s=50, zorder=3)
        ax.text(xp, np.sin(2 * np.pi * xp / lam) + 0.16, name, ha="center", color=AMBER, fontsize=11)
    ax.axhline(0, color=GREY, lw=0.8)
    style(ax, "distance x / m  (λ = 2.0 m)", "displacement", "Phase difference between points on one progressive wave")
    ax.set_ylim(-1.5, 1.6)
    ax.text(0.05, -1.35, "P→Q: λ/4 apart → 90° (π/2)      P→R: λ/2 → 180° (π), antiphase      P→S: λ → 360°, i.e. in phase      "
            "rule: Δφ = 360° × Δx/λ", color=GREY, fontsize=8.5)
    fig.tight_layout()
    fig.savefig("progressive-waves-phase.svg", format="svg", transparent=True)


def intensity():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 3.6), dpi=100); fig.patch.set_alpha(0)
    Aa = np.linspace(0, 3, 100)
    a1.plot(Aa, Aa ** 2, color=RED, lw=2)
    for a in (1, 2, 3):
        a1.scatter([a], [a * a], color=RED, s=40, zorder=3)
        a1.text(a + 0.06, a * a - 0.3, f"A = {a} → I = {a*a}", color=GREY, fontsize=9)
    style(a1, "amplitude A (arbitrary units)", "intensity I ∝ A²", "Double the amplitude, four times the intensity")
    a1.text(0.1, 7.6, "a particle in SHM carries energy ½mω²A²;\nthe wave delivers it, so power ∝ A²", color=GREY, fontsize=8.5, va="top")
    r = np.linspace(0.5, 4, 200)
    P = 100.0
    a2.plot(r, P / (4 * np.pi * r ** 2), color=GREEN, lw=2)
    for rr in (1, 2, 4):
        a2.scatter([rr], [P / (4 * np.pi * rr ** 2)], color=GREEN, s=40, zorder=3)
        a2.text(rr + 0.08, P / (4 * np.pi * rr ** 2) + 0.6, f"r = {rr}: {P/(4*np.pi*rr**2):.1f} W/m²", color=GREY, fontsize=9)
    style(a2, "distance from a 100 W point source r / m", "intensity I = P / 4πr²  (W/m²)", "Spread over a sphere: the inverse-square law")
    a2.text(1.9, 22, "same power, growing area 4πr²;\nI ∝ 1/r², so A ∝ 1/r", color=GREY, fontsize=8.5)
    fig.tight_layout()
    fig.savefig("progressive-waves-intensity.svg", format="svg", transparent=True)


def cro():
    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=100); fig.patch.set_alpha(0)
    ax.set_xlim(0, 10); ax.set_ylim(-4, 4)
    ax.set_xticks(range(11)); ax.set_yticks(range(-4, 5))
    ax.grid(True, color=GREY, alpha=0.45, lw=0.8)
    ax.tick_params(colors=GREY, labelsize=8)
    for sp in ax.spines.values():
        sp.set_color(GREY)
    ax.set_facecolor("none")
    # trace: period 4.0 cm, amplitude 2.5 cm
    x = np.linspace(0, 10, 600)
    ax.plot(x, 2.5 * np.sin(2 * np.pi * x / 4.0), color=GREEN, lw=2.2)
    ax.annotate("", (1, 3.3), (5, 3.3), arrowprops=dict(arrowstyle="<->", color=AMBER))
    ax.text(3, 3.45, "one cycle = 4.0 cm", ha="center", color=AMBER, fontsize=9)
    ax.annotate("", (7, 0), (7, 2.5), arrowprops=dict(arrowstyle="<->", color=RED))
    ax.text(7.1, 1.25, "2.5 cm", color=RED, fontsize=9, va="center")
    ax.set_title("CRO screen: 1 cm squares · time-base 0.50 ms/cm · Y-gain 2.0 V/cm", color=GREY, fontsize=10)
    ax.set_xlabel("time-base: each cm along = 0.50 ms   →   T = 4.0 × 0.50 = 2.0 ms,  f = 1/T = 500 Hz", color=GREY, fontsize=9)
    ax.set_ylabel("Y-gain: each cm up = 2.0 V  →  amplitude 2.5 × 2.0 = 5.0 V", color=GREY, fontsize=9)
    fig.tight_layout()
    fig.savefig("progressive-waves-cro.svg", format="svg", transparent=True)


def long_trans():
    lam = 2.0
    fig, (a1, a2, a3) = plt.subplots(3, 1, figsize=(9, 5.4), dpi=100, gridspec_kw={"height_ratios": [1.6, 1, 1.4]})
    fig.patch.set_alpha(0)
    x0 = np.linspace(0, 2 * lam, 41)
    # transverse
    a1.scatter(x0, 0.5 * np.sin(2 * np.pi * x0 / lam), color=BLUE, s=22)
    a1.plot(np.linspace(0, 2 * lam, 300), 0.5 * np.sin(2 * np.pi * np.linspace(0, 2 * lam, 300) / lam), color=BLUE, lw=0.8, alpha=0.4)
    a1.annotate("", (1.0, 0.0), (1.0, 0.5), arrowprops=dict(arrowstyle="<->", color=AMBER))
    a1.text(1.06, 0.25, "particle path: up–down", color=AMBER, fontsize=8, va="center")
    a1.annotate("", (3.6, -0.75), (2.6, -0.75), arrowprops=dict(arrowstyle="<-", color=GREY))
    a1.text(3.1, -0.9, "wave travels", ha="center", color=GREY, fontsize=8)
    a1.set_ylim(-1, 0.9); a1.set_xlim(-0.1, 2 * lam + 0.1); a1.set_yticks([])
    style(a1, "", "", "Transverse: vibration at right angles to the direction of travel  (rope, water surface, light, S-waves)")
    a1.grid(False)
    # longitudinal
    shift = 0.12 * np.sin(2 * np.pi * x0 / lam)
    a2.scatter(x0 + shift, np.zeros_like(x0), color=PURPLE, s=22)
    a2.annotate("", (0.95, 0.18), (1.25, 0.18), arrowprops=dict(arrowstyle="<->", color=AMBER))
    a2.text(1.1, 0.3, "particle path: to and fro", ha="center", color=AMBER, fontsize=8)
    a2.text(0.5, -0.32, "compression", ha="center", color=GREY, fontsize=8)
    a2.text(1.5, -0.32, "rarefaction", ha="center", color=GREY, fontsize=8)
    a2.text(2.5, -0.32, "compression", ha="center", color=GREY, fontsize=8)
    a2.set_ylim(-0.5, 0.5); a2.set_xlim(-0.1, 2 * lam + 0.1); a2.set_yticks([])
    style(a2, "", "", "Longitudinal: vibration along the direction of travel  (sound, spring, P-waves)")
    a2.grid(False)
    # longitudinal displacement graph
    xx = np.linspace(0, 2 * lam, 300)
    a3.plot(xx, np.sin(2 * np.pi * xx / lam), color=PURPLE, lw=2)
    a3.axhline(0, color=GREY, lw=0.8)
    a3.set_xlim(-0.1, 2 * lam + 0.1)
    style(a3, "position along the spring x", "displacement (+ = to the right)", "The SAME longitudinal wave drawn as a graph — looks transverse, is not")
    a3.text(0.5, -0.85, "zero displacement here, particles crowding in: a compression", color=GREY, fontsize=7.5, ha="center")
    a3.text(1.5, 0.75, "zero displacement here too, particles pulled apart: a rarefaction", color=GREY, fontsize=7.5, ha="center")
    fig.tight_layout()
    fig.savefig("progressive-waves-long-trans.svg", format="svg", transparent=True)


if __name__ == "__main__":
    two_graphs(); phase(); intensity(); cro(); long_trans()
    print("wrote five SVGs")
