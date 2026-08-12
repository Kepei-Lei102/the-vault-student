#!/usr/bin/env python3
"""
Parallel vs sequential merge-sort benchmark  —  data source for the Vault card
[[Parallel and External Sorting]].

It produces the numbers behind the "parallel helps big data, harms small data"
crossover: the same merge sort run (a) sequentially in one process and (b) in
parallel across all your CPU cores, measured over a range of dataset sizes.

TWO measurements, kept deliberately separate
--------------------------------------------
1. TIMING  — clean, uninstrumented sorts -> real wall-clock seconds.
             This is the crossover: at small N the cost of spinning up worker
             processes and shipping data to them dwarfs the work saved, so the
             parallel version is SLOWER; at large N the sorting work dominates
             and parallel pulls ahead.
2. COUNTS  — an instrumented merge sort -> comparisons and element-moves.
             Parallelism does NOT change these: the same elements get compared,
             just on different cores. So counts depend only on N (they grow like
             n*log2(n)), and they're reported once to show "same work, less time".
             (Merge sort is not in-place, so it MOVES elements rather than
             swapping them; that's why this reports moves, not swaps.)

How to run
----------
    python3 parallel-sort-benchmark.py

Edit SIZES / WORKERS below if you like. To reproduce a 10-million-element run,
add 10_000_000 to SIZES (expect a few minutes — pure-Python sorting is slow on
purpose; that slowness is exactly what makes parallelism worth it).

When it finishes it writes the results to  parallel-sort-results.json  (right
next to this script). Just run it and say "done" — no copy-paste needed; the
chart and the Manim race get built straight from that file.
"""

import os
import sys
import time
import json
import random
import heapq
import platform
import statistics
import multiprocessing as mp

# ----------------------------- configuration -----------------------------
WORKERS = mp.cpu_count()          # parallel processes (one per logical core)

# Dataset sizes to test. Small sizes show the overhead penalty; large sizes
# show the parallel win. Add 10_000_000 for the headline run (slower).
SIZES = [100, 1_000, 10_000, 50_000, 100_000, 500_000, 1_000_000, 2_000_000]

SEED = 20260624                   # fixed seed -> reproducible data

# Optional quick run without editing the file:
#   PSB_SIZES=100,1000,5000 python3 parallel-sort-benchmark.py
if os.environ.get("PSB_SIZES"):
    SIZES = [int(x) for x in os.environ["PSB_SIZES"].split(",")]

# Results are written here (next to this script) so Claude can read them directly.
RESULTS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "parallel-sort-results.json")


def runs_for(n):
    """More repeats where each run is cheap; fewer where a run is expensive."""
    if n <= 100_000:
        return 10
    if n <= 1_000_000:
        return 5
    return 3


# ------------------------- the sort (two flavours) -------------------------
def merge_sort(a):
    """Plain top-down merge sort. Returns a new sorted list (not in place)."""
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


def merge_sort_counted(a):
    """Same algorithm, instrumented. Returns (sorted_list, comparisons, moves)."""
    comps = [0]
    moves = [0]

    def msort(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = msort(lst[:mid])
        right = msort(lst[mid:])
        out = []
        i = j = 0
        while i < len(left) and j < len(right):
            comps[0] += 1                      # one key comparison
            if left[i] <= right[j]:
                out.append(left[i]); i += 1
            else:
                out.append(right[j]); j += 1
            moves[0] += 1                       # one element written into place
        while i < len(left):
            out.append(left[i]); i += 1; moves[0] += 1
        while j < len(right):
            out.append(right[j]); j += 1; moves[0] += 1
        return out

    return msort(a), comps[0], moves[0]


# --------------------------- parallel driver ---------------------------
def parallel_sort(data, workers):
    """
    Split into `workers` contiguous chunks, merge-sort each chunk in its own
    process, then k-way merge the sorted chunks back in the main process.

    A fresh worker pool is created *inside* this call on purpose: that is the
    real cost of "deciding to parallelize a job", and it is what punishes small
    datasets. The final k-way merge is inherently sequential — Amdahl's law made
    visible (the part you cannot parallelize caps the speed-up).
    """
    n = len(data)
    step = max(1, n // workers)
    chunks = [data[i:i + step] for i in range(0, n, step)]
    with mp.Pool(workers) as pool:
        sorted_chunks = pool.map(merge_sort, chunks)
    return list(heapq.merge(*sorted_chunks))


# ------------------------------- harness -------------------------------
def make_data(n, seed):
    rng = random.Random(seed)
    return [rng.random() for _ in range(n)]


def time_call(fn, *args):
    t0 = time.perf_counter()
    fn(*args)
    return time.perf_counter() - t0


def main():
    print(f"platform   : {platform.platform()}")
    print(f"python     : {sys.version.split()[0]}")
    print(f"cpu cores  : {WORKERS}  (start method: {mp.get_start_method()})")
    print(f"sizes      : {SIZES}")

    results = {
        "workers": WORKERS,
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "start_method": mp.get_start_method(),
        "timing": [],
        "counts": [],
    }

    # ---- 1. TIMING: sequential vs parallel, the crossover ----
    print("\n== TIMING  (mean seconds over repeated runs) ==")
    print(f"{'N':>11} {'runs':>5} {'seq (s)':>11} {'parallel (s)':>13} {'speedup':>8}")
    for n in SIZES:
        reps = runs_for(n)
        base = make_data(n, SEED)                       # merge_sort never mutates input
        seq = [time_call(merge_sort, base) for _ in range(reps)]
        par = [time_call(parallel_sort, base, WORKERS) for _ in range(reps)]
        s, p = statistics.mean(seq), statistics.mean(par)
        results["timing"].append({
            "n": n, "runs": reps,
            "seq_s": s, "par_s": p,
            "seq_std": statistics.pstdev(seq), "par_std": statistics.pstdev(par),
            "speedup": s / p,
        })
        print(f"{n:>11} {reps:>5} {s:>11.5f} {p:>13.5f} {s / p:>7.2f}x")

    # ---- 2. COUNTS: comparisons & moves (work done, independent of cores) ----
    print("\n== COUNTS  (mean over runs; parallelism does not change these) ==")
    print(f"{'N':>11} {'runs':>5} {'comparisons':>16} {'moves':>16}")
    for n in SIZES:
        if n > 2_000_000:        # instrumented pure-Python is slow; cap the counts
            continue
        reps = runs_for(n)
        cs, ms = [], []
        for r in range(reps):
            _, c, m = merge_sort_counted(make_data(n, SEED + r))
            cs.append(c); ms.append(m)
        c, m = statistics.mean(cs), statistics.mean(ms)
        results["counts"].append({"n": n, "runs": reps, "comparisons": c, "moves": m})
        print(f"{n:>11} {reps:>5} {c:>16.0f} {m:>16.0f}")

    with open(RESULTS_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n== RESULTS WRITTEN ==\n{RESULTS_PATH}")
    print("Done — just tell Claude the run finished and it will read this file.")


if __name__ == "__main__":
    main()
