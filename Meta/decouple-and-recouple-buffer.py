"""Producer/consumer with a bounded buffer — the decoupling quantified.

A bursty producer (a CPU emitting print jobs, a network delivering video in
clumps) feeds a steady consumer (a printer, a video decoder) that can take one
item per tick. Between them sits a buffer of capacity B. B = 0 means the two are
directly coupled: a hand-over succeeds only if the consumer is free *this tick*.
We measure how often each side is forced to wait on the other's bad moments.

Regenerate:  python3 decouple-and-recouple-buffer.py   (writes the .svg beside it)
"""
import random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GREY = "#888888"
BLUE, GREEN, RED, AMBER = "#2563eb", "#059669", "#dc2626", "#f59e0b"

def simulate(B, ticks=200_000, p_burst=0.2, mean_burst=4, seed=1):
    """Return (consumer-idle fraction, producer-blocked fraction, occupancy trace)."""
    rng = random.Random(seed)
    buf = 0
    idle = blocked = 0
    trace = []
    for _ in range(ticks):
        # consumer first: takes one item that was already waiting at the start of the tick
        if buf > 0:
            buf -= 1
        else:
            idle += 1
        # producer: with prob p_burst emit a burst of geometric size (mean mean_burst)
        if rng.random() < p_burst:
            k = 1
            while rng.random() > 1 / mean_burst:
                k += 1
            room = B - buf
            take = min(k, room)
            buf += take
            blocked += k - take
        trace.append(buf)
    produced = ticks * p_burst * mean_burst
    return idle / ticks, blocked / produced, trace

sizes = [0, 2, 4, 8, 16, 32, 64]
idle_f, block_f = [], []
for B in sizes:
    i, b, _ = simulate(max(B, 1))
    idle_f.append(i); block_f.append(b)

# The B=0 case, done honestly: at most one item passes per tick, no storage.
def simulate_direct(ticks=200_000, p_burst=0.2, mean_burst=4, seed=1):
    rng = random.Random(seed); idle = blocked = 0
    for _ in range(ticks):
        if rng.random() < p_burst:
            k = 1
            while rng.random() > 1 / mean_burst:
                k += 1
            blocked += k - 1          # only one item can be handed over this tick
        else:
            idle += 1                 # nothing offered → consumer idles
    return idle / ticks, blocked / (ticks * p_burst * mean_burst)
idle_f[0], block_f[0] = simulate_direct()

_, _, trace = simulate(8, ticks=400, seed=7)

print("B  consumer-idle  producer-blocked")
for B, i, b in zip(sizes, idle_f, block_f):
    print(f"{B:>2}  {i:12.3f}  {b:16.3f}")

fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(9, 6.6), gridspec_kw={"height_ratios": [1, 1.3]})
fig.patch.set_alpha(0)
for ax in (ax0, ax1):
    ax.set_facecolor("none")
    for s in ax.spines.values(): s.set_color(GREY)
    ax.tick_params(colors=GREY, labelsize=9)
    ax.xaxis.label.set_color(GREY); ax.yaxis.label.set_color(GREY)
    ax.title.set_color(GREY)

ax0.fill_between(range(len(trace)), trace, step="post", color=BLUE, alpha=0.25)
ax0.step(range(len(trace)), trace, where="post", color=BLUE, lw=1.2)
ax0.axhline(8, color=RED, lw=1, ls="--")
ax0.text(398, 8.15, "buffer full (B = 8)", color=RED, ha="right", fontsize=9)
ax0.set_ylim(0, 9.5); ax0.set_xlim(0, 400)
ax0.set_ylabel("items waiting")
ax0.set_xlabel("time (ticks)")
ax0.set_title("A bursty producer, a steady consumer, and the buffer between them", fontsize=11)

x = range(len(sizes))
ax1.plot(x, [100*v for v in idle_f], "o-", color=GREEN, lw=1.6, label="consumer idle (waiting for work)")
ax1.plot(x, [100*v for v in block_f], "s-", color=RED, lw=1.6, label="producer blocked (buffer full)")
ax1.set_xticks(list(x)); ax1.set_xticklabels([str(s) for s in sizes])
ax1.set_xlabel("buffer capacity B (0 = directly coupled)")
ax1.set_ylabel("% of the time")
ax1.set_ylim(0, 95)
ax1.axvline(0, color=GREY, lw=0.6, ls=":")
leg = ax1.legend(frameon=False, fontsize=9, loc="upper right")
for t in leg.get_texts(): t.set_color(GREY)
ax1.set_title("Same producer, same consumer, same work — only the coupling changes", fontsize=11)
ax1.text(len(sizes)-1, 100*block_f[-1]+4, f"{100*block_f[-1]:.1f}%", color=RED, ha="center", fontsize=9)
ax1.text(0.5, 100*block_f[0]-14, f"{100*block_f[0]:.0f}% of output refused", color=RED, fontsize=9)
ax1.text(len(sizes)-1, 100*idle_f[-1]+4, f"{100*idle_f[-1]:.0f}% (the honest floor:\nproducer averages 0.8 item/tick)", color=GREEN, ha="right", fontsize=8.5)

fig.tight_layout()
fig.savefig("decouple-and-recouple-buffer.svg", transparent=True)
print("saved decouple-and-recouple-buffer.svg")
