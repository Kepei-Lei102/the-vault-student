"""Every latency on the ladder, rescaled so that one RAM access (100 ns) = one second of human time.
The point: the slow step is never the arithmetic; it is moving data — and the human rungs sit on the
same ladder, years above the disk.  Regenerate: python3 true-io-bound-ladder.py"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RAM = 100e-9                                   # the unit: one RAM access = 1 s
rows = [  # (label, real seconds, colour)
    ("register read (0.3 ns)",            0.3e-9, "#2563eb"),
    ("L1 cache hit (1 ns)",               1e-9,   "#2563eb"),
    ("L2 cache hit (4 ns)",               4e-9,   "#2563eb"),
    ("RAM access (100 ns)",               100e-9, "#2563eb"),
    ("SSD read (60 µs)",                  60e-6,  "#0891b2"),
    ("HDD seek (13 ms)",                  13e-3,  "#0891b2"),
    ("same-building network hop (0.5 ms)",0.5e-3, "#7c3aed"),
    ("Chengdu ↔ California round trip (150 ms)", 0.15, "#7c3aed"),
    ("a human blink (150 ms)",            0.15,   "#f59e0b"),
    ("a human reads one sentence (2 s)",  2.0,    "#f59e0b"),
    ("a human answers a message (1 h)",   3600.0, "#f59e0b"),
]
GREY = "#888888"
fig, ax = plt.subplots(figsize=(9.2, 5.6)); fig.patch.set_alpha(0); ax.set_facecolor("none")
ys = list(range(len(rows)))[::-1]
def human(sec):
    for unit, div in [("years", 3.15e7), ("months", 2.6e6), ("days", 86400), ("hours", 3600), ("min", 60), ("s", 1), ("ms", 1e-3)]:
        if sec >= div:
            v = sec / div
            return f"{v:.0f} {unit}" if v >= 10 else f"{v:.1f} {unit}"
for y, (label, t, col) in zip(ys, rows):
    h = t / RAM
    ax.barh(y, h, color=col, alpha=0.85, height=0.62)
    ax.text(h * 1.6, y, "≈ " + human(h), va="center", fontsize=8.5, color=GREY)
ax.set_yticks(ys); ax.set_yticklabels([r[0] for r in rows], fontsize=9, color=GREY)
ax.set_xscale("log"); ax.set_xlim(1e-3, 3e13)
marks = [(1, "1 s"), (60, "1 min"), (3600, "1 h"), (86400, "1 day"), (2.6e6, "1 month"),
         (3.15e7, "1 year"), (3.15e9, "100 years"), (3.15e10, "1000 years")]
for x, t in marks:
    ax.axvline(x, color=GREY, lw=0.5, ls=":")
    ax.text(x, len(rows) - 0.45, t, rotation=90, fontsize=7.5, color=GREY, va="bottom", ha="right")
ax.set_ylim(-0.7, len(rows) + 1.3)
ax.set_xlabel("the same delay in human time, if one RAM access took one second (log scale)", color=GREY)
for s in ax.spines.values(): s.set_color(GREY)
ax.tick_params(colors=GREY, labelsize=8)
fig.suptitle("The I/O ladder — real time in brackets, bar = the same delay rescaled so RAM = 1 s", color=GREY, fontsize=10.5)
fig.tight_layout(rect=(0, 0, 1, 0.96)); fig.savefig("true-io-bound-ladder.svg", transparent=True)
for label, t, _ in rows:
    print(f"{label:44s} {t/RAM:12.3g} human-seconds")
