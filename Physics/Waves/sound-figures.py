"""Figures for [[Sound]].  python3 sound-figures.py
Numbers quoted on the figures are the printed output of sound-lab.py.
Every SVG: text #888, width=100%, no background, checked in light and dark."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GREY, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": GREY, "axes.labelcolor": GREY, "xtick.color": GREY,
                     "ytick.color": GREY, "axes.edgecolor": GREY, "svg.fonttype": "none", "font.size": 9.5})


def style(ax):
    ax.set_facecolor("none")
    for sp in ax.spines.values():
        sp.set_color(GREY)


def save(fig, name):
    fig.patch.set_alpha(0)
    fig.savefig(name, format="svg", bbox_inches="tight", transparent=True)
    plt.close(fig)
    txt = open(name).read()
    txt = txt.replace('width="', 'data-w="', 1).replace('height="', 'data-h="', 1)
    txt = txt.replace("<svg ", '<svg width="100%" ', 1)
    open(name, "w").write(txt)


# 1. compressions and rarefactions: particles above, pressure below
lam, A = 2.0, 0.22
x0 = np.linspace(0, 8, 97); rng = np.random.default_rng(1)
fig, axes = plt.subplots(2, 1, figsize=(10, 5.2), sharex=True, gridspec_kw={"height_ratios": [1.1, 1]})
ax = axes[0]; style(ax)
for row in np.linspace(0.15, 0.85, 7):
    x = x0 + A * np.sin(2 * np.pi * x0 / lam) + rng.normal(0, 0.012, x0.size)
    ax.scatter(x, np.full_like(x, row), s=9, color=TEAL, alpha=0.8, lw=0)
for c in (1.0, 3.0, 5.0, 7.0): ax.text(c, 1.0, "C", ha="center", fontsize=11, color=RED, weight="bold")
for r in (0.0, 2.0, 4.0, 6.0, 8.0): ax.text(r, 1.0, "R", ha="center", fontsize=11, color=BLUE, weight="bold")
ax.annotate("", xy=(3.0, -0.08), xytext=(1.0, -0.08), arrowprops=dict(arrowstyle="<->", color=GREY)); ax.text(2.0, -0.2, "one wavelength λ", ha="center", fontsize=9, color=GREY)
ax.annotate("", xy=(7.6, -0.08), xytext=(6.2, -0.08), arrowprops=dict(arrowstyle="->", color=AMBER, lw=2)); ax.text(6.9, -0.2, "wave travels; particles only shuttle to and fro", ha="center", fontsize=9, color=AMBER)
ax.set_ylim(-0.3, 1.15); ax.set_yticks([]); ax.set_title("Air particles in a sound wave: C = compression (crowded, high pressure), R = rarefaction (spread out, low pressure)", fontsize=9.8)
ax = axes[1]; style(ax)
xx = np.linspace(0, 8, 600); p = -np.cos(2 * np.pi * xx / lam)     # pressure excess ∝ −ds/dx
ax.plot(xx, p, color=PURPLE, lw=2); ax.axhline(0, color=GREY, lw=0.8, ls=":")
ax.text(8.05, 0.0, "atmospheric\npressure", fontsize=8, color=GREY, va="center")
ax.set_ylabel("pressure"); ax.set_yticks([]); ax.set_xlabel("distance along the direction of travel"); ax.set_xticks([])
ax.set_title("The same instant as a graph: compressions are the peaks of pressure, rarefactions the troughs", fontsize=9.8)
fig.tight_layout(); save(fig, "sound-compressions.svg")

# 2. what the oscilloscope shows: two rows of two
t = np.linspace(0, 10, 1000)
panels = [("quiet, low pitch", 0.35, 0.3, GREY), ("loud, same pitch: larger amplitude", 1.0, 0.3, RED),
          ("same loudness, higher pitch: more waves in the same time", 0.35, 0.75, BLUE), ("loud and high", 1.0, 0.75, PURPLE)]
fig, axes = plt.subplots(2, 2, figsize=(10, 5.6), sharex=True, sharey=True)
for ax, (title, amp, f, col) in zip(axes.ravel(), panels):
    style(ax); ax.plot(t, amp * np.sin(2 * np.pi * f * t), color=col, lw=2); ax.axhline(0, color=GREY, lw=0.6, ls=":")
    ax.set_ylim(-1.25, 1.25); ax.set_xticks(np.arange(0, 11, 1)); ax.set_yticks(np.arange(-1, 1.1, 0.5)); ax.grid(color=GREY, alpha=0.18)
    ax.set_xticklabels([]); ax.set_yticklabels([]); ax.set_title(title, fontsize=9.5)
fig.suptitle("A microphone and an oscilloscope: height is amplitude (loudness), crowding is frequency (pitch); the two are independent", fontsize=10, color=GREY)
fig.tight_layout(); save(fig, "sound-traces.svg")

# 3. speeds: media, and temperature
fig, axes = plt.subplots(2, 1, figsize=(9, 6.6))
ax = axes[0]; style(ax)
names = ["air (20 °C)", "water", "steel"]; v = [343, 1485, 5048]
ax.barh(names, v, color=[TEAL, BLUE, GREY], alpha=0.75)
for i, val in enumerate(v): ax.text(val + 60, i, f"{val} m/s", va="center", fontsize=9, color=GREY)
ax.set_xlim(0, 6200); ax.set_xlabel("speed of sound / m per s"); ax.invert_yaxis()
ax.set_title("Gas < liquid < solid: steel is 6 500 × denser than air and 1.4 million × stiffer, and the stiffness wins", fontsize=9.8)
ax = axes[1]; style(ax)
th = np.linspace(-20, 45, 100); ax.plot(th, 331.3 * np.sqrt(1 + th / 273.15), color=AMBER, lw=2)
ax.axhspan(330, 350, color=GREEN, alpha=0.12); ax.text(-19, 346.5, "the range to quote for air: 330–350 m/s", fontsize=8.5, color=GREEN)
ax.set_xlabel("air temperature / °C"); ax.set_ylabel("speed of sound in air / m per s")
ax.set_title("Why air has a range and not one number: warmer air, faster molecules, faster sound", fontsize=9.8)
fig.tight_layout(); save(fig, "sound-speeds.svg")

# 4. measuring the speed: what each method costs
fig, ax = plt.subplots(figsize=(9, 4.2)); style(ax)
m = ["see then hear,\n60 m, stopwatch", "see then hear,\n500 m, stopwatch", "clap with the echo,\n20 claps, 50 m wall", "two microphones\n1 m apart, ms timer", "two microphones\n3 m apart, ms timer"]
u = [80.4, 9.6, 4.2, 1.0, 0.3]
ax.bar(m, u, color=[RED, AMBER, AMBER, GREEN, GREEN], alpha=0.75); ax.set_yscale("log"); ax.set_ylim(0.15, 300)
for i, val in enumerate(u): ax.text(i, val * 1.25, f"{val} %", ha="center", fontsize=9, color=GREY)
ax.set_ylabel("uncertainty in the speed / %  (log scale)"); ax.tick_params(axis="x", labelsize=8)
ax.set_title("The stopwatch is always wrong by about 0.14 s: make the time long, or take the human out", fontsize=10)
fig.tight_layout(); save(fig, "sound-measure.svg")

# 5. who hears what
animals = [("elephant", 14, 12_000), ("human (young)", 20, 20_000), ("human (age 60)", 20, 12_000), ("dog", 65, 45_000), ("cat", 45, 64_000), ("bat", 2_000, 110_000), ("dolphin", 75, 150_000)]
fig, ax = plt.subplots(figsize=(9.5, 4.2)); style(ax)
for i, (n, lo, hi) in enumerate(animals):
    ax.barh(i, hi - lo, left=lo, color=PURPLE if n.startswith("human") else TEAL, alpha=0.7, height=0.55)
    ax.text(hi * 1.12, i, f"{lo:,} Hz – {hi/1000:g} kHz", va="center", fontsize=8.3, color=GREY)
ax.axvspan(20, 20_000, color=PURPLE, alpha=0.07)
ax.axvline(20, color=GREY, lw=0.8, ls=":"); ax.axvline(20_000, color=GREY, lw=0.8, ls=":")
ax.text(9, 6.75, "infrasound", fontsize=8.5, color=GREY, ha="center"); ax.text(120_000, 6.75, "ultrasound", fontsize=8.5, color=GREY, ha="center"); ax.set_ylim(7.1, -0.6)
ax.set_xscale("log"); ax.set_xlim(4, 900_000); ax.set_yticks(range(len(animals))); ax.set_yticklabels([a[0] for a in animals])
ax.set_xlabel("frequency / Hz  (log scale)"); ax.set_title("'Audible' is a fact about the listener: the shaded band is the human 20 Hz – 20 kHz", fontsize=10)
fig.tight_layout(); save(fig, "sound-hearing-ranges.svg")
print("five SVGs written")
