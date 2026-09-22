"""A cycle-level simulator of three processors running the same program, to put numbers on the textbook model
and the engine that replaced it.  Run: python3 modern-cpu-simulator.py   (writes modern-cpu-simulator.json)

The program is the branch experiment from modern-cpu-lab.c in a tiny RISC-like instruction set: for each element,
load it, compare, branch, and on the taken path add it to a running sum. Three machines execute it:
  textbook   one instruction at a time, each taking its full latency (fetch, decode, execute, memory, write back)
  pipeline   five stages, one instruction issued per cycle when nothing stalls; a load-use stall of 2 cycles;
             a static "not taken" branch guess with a 3-cycle flush when wrong
  ooo        a wide out-of-order core: fetch W per cycle, a reorder buffer of R entries, instructions issue
             when their operands are ready, results commit in program order; a 2-bit branch predictor per branch;
             a flush of the whole window when a branch was mispredicted
Latencies: add/compare 1, branch 1, load 4 (an L1 hit).  Every machine runs the same instruction stream on the
same data, unsorted and then sorted, so the only difference is the machine.
"""
import json, random
from collections import deque

random.seed(7)
N = 4000
data_unsorted = [random.randrange(256) for _ in range(N)]
data_sorted = sorted(data_unsorted)
LAT = {"load": 4, "add": 1, "cmp": 1, "br": 1, "addi": 1}

def program(data):
    """Unrolled instruction stream: (op, dest, srcs, extra). Registers are names; 'r_i' holds the loop counter."""
    ins = []
    for i, v in enumerate(data):
        ins.append(("load", f"v{i}", [], v))                     # v_i = a[i]
        ins.append(("cmp", f"c{i}", [f"v{i}"], v >= 128))          # c_i = a[i] >= 128
        ins.append(("br", None, [f"c{i}"], v >= 128))              # branch on c_i: taken iff a[i] >= 128
        if v >= 128:
            ins.append(("add", "sum", ["sum", f"v{i}"], None))     # sum += a[i]  (only on the taken path)
        ins.append(("addi", "i", ["i"], None))                     # i += 1
    return ins

def textbook(ins):
    return sum(5 + (LAT[op] - 1) for op, *_ in ins), 0

def pipeline(ins):
    cycles, mispred, ready_at = 0, 0, {}
    for k, (op, dest, srcs, extra) in enumerate(ins):
        stall = max([ready_at.get(s, 0) - cycles for s in srcs] + [0])
        cycles += 1 + stall
        if dest: ready_at[dest] = cycles + (LAT[op] - 1)
        if op == "br" and extra:                                    # static not-taken guess, wrong when taken
            mispred += 1; cycles += 3
    return cycles + 4, mispred                                      # drain the pipe

def ooo(ins, width=6, rob=128):
    cycles, mispred, k = 0, 0, 0
    window = deque()                                                # entries: [idx, op, dest, srcs, extra, done_at]
    ready_at = {}; pred = {}                                        # 2-bit counters by branch site (all branches share one site here)
    while k < len(ins) or window:
        cycles += 1
        # fetch up to `width` into the window, stopping at a mispredicted branch (must wait until it resolves)
        fetched = 0
        while k < len(ins) and len(window) < rob and fetched < width:
            window.append([k, *ins[k], None]); k += 1; fetched += 1
            if ins[k - 1][0] == "br":
                site = 0; c = pred.get(site, 2); guess = c >= 2
                if guess != ins[k - 1][3]:                          # misprediction: fetch stops here until the branch resolves
                    window[-1].append("mis"); break
        # issue every ready instruction (unlimited units, which flatters the core slightly; issue width bounds it)
        issued = 0
        for e in window:
            if e[5] is None and issued < width and all(ready_at.get(s, 0) <= cycles for s in e[3]):
                e[5] = cycles + LAT[e[1]]; issued += 1
                if e[2]: ready_at[e[2]] = e[5]
        # commit in order
        while window and window[0][5] is not None and window[0][5] <= cycles:
            e = window.popleft()
            if e[1] == "br":
                site = 0; c = pred.get(site, 2); taken = e[4]
                pred[site] = min(3, c + 1) if taken else max(0, c - 1)
                if len(e) > 6:                                      # mispredicted: throw away the window, refetch
                    mispred += 1; cycles += 3
                    for w in window:
                        if w[2] in ready_at: ready_at.pop(w[2], None)
                    k = e[0] + 1; window.clear()
    return cycles, mispred

out = {}
for label, data in (("unsorted", data_unsorted), ("sorted", data_sorted)):
    ins = program(data); n = len(ins); out[label] = {"instructions": n}
    print(f"== {label}: {n} instructions, {sum(1 for v in data if v >= 128)} taken branches of {N}")
    for name, fn in (("textbook", textbook), ("pipeline", pipeline), ("ooo", ooo)):
        cyc, mis = fn(ins); out[label][name] = {"cycles": cyc, "ipc": n / cyc, "mispredicts": mis}
        print(f"   {name:9s} {cyc:8d} cycles   IPC {n / cyc:.2f}   mispredicted branches {mis}")
json.dump(out, open("modern-cpu-simulator.json", "w"), indent=1)
print("wrote modern-cpu-simulator.json")
