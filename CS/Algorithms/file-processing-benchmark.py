"""
file-processing-benchmark.py — finding one record: scan versus seek, measured.

Companion to [[File Processing and Exception Handling]].  Builds files of
fixed-length 37-byte records at several sizes, then times

  * SERIAL scan  — read record after record until the key turns up (the key
    is planted in the middle, so a scan reads n/2 records on average);
  * RANDOM seek  — hash the key, seek to slot × record size, read one record.

Writes file-processing-seek-vs-scan.svg (matplotlib, both-theme safe) and
prints the table used in the card.   Run:  python3 file-processing-benchmark.py
"""
from __future__ import annotations

import os
import struct
import tempfile
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

FMT = "<Bi24sd"
RECORD_SIZE = struct.calcsize(FMT)


def build(path: str, n: int) -> None:
    with open(path, "wb") as f:
        for k in range(n):
            f.write(struct.pack(FMT, 1, k, b"name", 0.0))


def serial_find(path: str, key: int) -> int:
    with open(path, "rb") as f:
        while raw := f.read(RECORD_SIZE):
            if struct.unpack(FMT, raw)[1] == key:
                return key
    return -1


def random_find(path: str, key: int, slots: int) -> int:
    with open(path, "rb") as f:
        f.seek((key % slots) * RECORD_SIZE)      # hash = key MOD slots; identity here
        return struct.unpack(FMT, f.read(RECORD_SIZE))[1]


def timeit(fn, reps: int) -> float:
    t = time.perf_counter()
    for _ in range(reps):
        fn()
    return (time.perf_counter() - t) / reps


def main() -> None:
    d = tempfile.mkdtemp()
    sizes = [1_000, 3_000, 10_000, 30_000, 100_000, 300_000]
    scan_ms, seek_us = [], []
    print(f"{'records':>9} {'file':>9} {'serial scan':>13} {'random seek':>13} {'ratio':>8}")
    for n in sizes:
        p = os.path.join(d, f"r{n}.dat")
        build(p, n)
        key = n // 2
        reps = max(3, 300_000 // n)
        s = timeit(lambda: serial_find(p, key), reps)
        r = timeit(lambda: random_find(p, key, n), 2000)
        assert serial_find(p, key) == key == random_find(p, key, n)
        scan_ms.append(s * 1e3); seek_us.append(r * 1e6)
        print(f"{n:>9,} {os.path.getsize(p)/1e6:>7.1f}MB {s*1e3:>10.2f} ms {r*1e6:>10.1f} µs {s/r:>8,.0f}×")

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=100)
    fig.patch.set_alpha(0); ax.set_facecolor("none")
    ax.plot(sizes, [v / 1e3 for v in scan_ms], "o-", color="#dc2626", lw=2, label="serial scan (reads n/2 records)")
    ax.plot(sizes, [v / 1e6 for v in seek_us], "s-", color="#059669", lw=2, label="random file (hash, one seek, one read)")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel("records in the file", color="#888")
    ax.set_ylabel("time to find one record (s)", color="#888")
    ax.set_title("Finding one record by key: the cost of not knowing where it is", color="#888", fontsize=11)
    for sp in ax.spines.values():
        sp.set_color("#888")
    ax.tick_params(colors="#888", which="both")
    ax.grid(True, which="major", color="#888", alpha=0.25, lw=0.6)
    leg = ax.legend(frameon=False, fontsize=9)
    for t in leg.get_texts():
        t.set_color("#888")
    ax.annotate(f"{scan_ms[-1]/1e3:.2f} s", (sizes[-1], scan_ms[-1] / 1e3), textcoords="offset points",
                xytext=(-48, -14), color="#dc2626", fontsize=9)
    ax.annotate(f"{seek_us[-1]:.0f} µs", (sizes[-1], seek_us[-1] / 1e6), textcoords="offset points",
                xytext=(-40, -16), color="#059669", fontsize=9)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file-processing-seek-vs-scan.svg")
    fig.tight_layout()
    fig.savefig(out, format="svg", transparent=True)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
