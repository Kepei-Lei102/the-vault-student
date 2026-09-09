"""Roofline model (Williams, Waterman, Patterson 2009) for one NVIDIA H100 SXM:
peak dense fp16 ≈ 989 TFLOP/s, HBM3 bandwidth ≈ 3.35 TB/s, so the ridge sits at ≈ 295 FLOP/byte.
Any workload left of the ridge is bound by moving bytes, not by arithmetic.
Regenerate: python3 true-io-bound-roofline.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PEAK, BW = 989e12, 3.35e12
ridge = PEAK / BW
GREY = "#888888"
x = np.logspace(-1, 4, 400)
roof = np.minimum(BW * x, PEAK)
fig, ax = plt.subplots(figsize=(8.6, 5.2)); fig.patch.set_alpha(0); ax.set_facecolor("none")
ax.plot(x, roof / 1e12, color=GREY, lw=2)
ax.fill_between(x, 1e-2, roof / 1e12, where=x < ridge, color="#dc2626", alpha=0.10)
ax.fill_between(x, 1e-2, roof / 1e12, where=x >= ridge, color="#059669", alpha=0.10)
ax.axvline(ridge, color=GREY, lw=0.6, ls=":")
pts = [  # (intensity FLOP/byte, label, colour, dx, dy)
    (1,    "LLM decode, one user\n(1 FLOP per weight byte)", "#dc2626"),
    (32,   "LLM decode, 32 users batched", "#dc2626"),
    (0.25, "external merge sort\n(compare once per byte read)", "#dc2626"),
    (2000, "prefill / big matrix multiply", "#059669"),
]
for it, label, col in pts:
    yv = min(BW * it, PEAK) / 1e12
    ax.plot(it, yv, "o", color=col, ms=7)
    ax.annotate(label, (it, yv), textcoords="offset points", xytext=(8, -26) if it < ridge else (-60, -40),
                fontsize=8.5, color=GREY)
ax.text(ridge * 1.08, 1.5e-1, f"ridge ≈ {ridge:.0f} FLOP/byte", color=GREY, fontsize=8.5, rotation=90, va="bottom")
ax.text(0.14, 350, "memory-bound:\nmore FLOPs would not help", color="#dc2626", fontsize=9, alpha=0.9)
ax.text(1200, 4, "compute-bound:\nmore bandwidth\nwould not help", color="#059669", fontsize=9, alpha=0.9)
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlim(0.1, 1e4); ax.set_ylim(0.1, 3000)
ax.set_xlabel("arithmetic intensity — FLOPs performed per byte moved from memory (log)", color=GREY)
ax.set_ylabel("attainable TFLOP/s (log)", color=GREY)
for s in ax.spines.values(): s.set_color(GREY)
ax.tick_params(colors=GREY, labelsize=8, which="both")
fig.suptitle("Roofline of one H100: left of the ridge, the chip is waiting for bytes", color=GREY, fontsize=10.5)
fig.tight_layout(rect=(0, 0, 1, 0.96)); fig.savefig("true-io-bound-roofline.svg", transparent=True)
print("ridge", ridge)
