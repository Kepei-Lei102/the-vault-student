"""
Manim sort visualizations for The Vault — CS/Algorithms/Sorting.md
Renders six MP4s on the SAME shuffled 50-element array:
  SortRace      -> sort-race.mp4   (all five sorts at once, shared tick = 1 comparison)
  BubbleSort    -> sort-bubble.mp4
  SelectionSort -> sort-selection.mp4
  InsertionSort -> sort-insertion.mp4
  MergeSort     -> sort-merge.mp4   (boxes around partially-sorted runs)
  QuickSort     -> sort-quicksort.mp4   (pivot drawn red)

Each algorithm is instrumented to emit one FRAME per comparison/operation:
  frame = {v: values, a: active(amber), d: done(green), p: pivot(red),
           c: comparison count, bx: settled sorted-run boxes, ab: active box}
A ValueTracker advances a "tick"; updaters paint the bars (and, for merge, the
run-boxes) and the counter from frame[int(tick)]. Wall-clock progress is
proportional to comparisons — the race is fair.

Render (iteration):  python3 -m manim -qm sort-visualizations.py SortRace
Render (committed):  manim -qk sort-visualizations.py SortRace
  then BubbleSort SelectionSort InsertionSort MergeSort QuickSort, and copy each
  media/videos/sort-visualizations/2160p60/<Scene>.mp4 to ./sort-<name>.mp4
"""
from manim import *
import numpy as np
import random

# ---------- Vault palette (Manim track, dark MP4 background) ----------
BG      = "#1e1e1e"
TXT     = "#cccccc"
TXT_DIM = "#888888"
BLUE    = "#2563eb"
GREEN   = "#059669"
AMBER   = "#f59e0b"
RED     = "#dc2626"
config.background_color = BG

N = 50
random.seed(7)
ARR = random.sample(range(1, N + 1), N)   # fixed permutation of 1..50
MAXV = N

def F_(v, a=(), d=(), c=0, p=(), bx=(), ab=None):
    return {"v": list(v), "a": set(a), "d": set(d), "c": c,
            "p": set(p), "bx": list(bx), "ab": ab}

# ---------------- frame instrumentation ----------------
def bubble_frames(arr):
    a = arr[:]; n = len(a); F = [F_(a)]; c = 0; locked = set()
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            c += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]; swapped = True
            F.append(F_(a, [j, j + 1], locked, c))
        locked.add(n - 1 - i)
        if not swapped:
            break
    F.append(F_(a, (), range(n), c))
    return F

def selection_frames(arr):
    a = arr[:]; n = len(a); F = [F_(a)]; c = 0
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            c += 1
            if a[j] < a[m]: m = j
            F.append(F_(a, [i, j, m], range(i), c))
        a[i], a[m] = a[m], a[i]
    F.append(F_(a, (), range(n), c))
    return F

def insertion_frames(arr):
    a = arr[:]; n = len(a); F = [F_(a, (), [0])]; c = 0
    for i in range(1, n):
        key = a[i]; j = i - 1
        while j >= 0:
            c += 1
            if a[j] > key:
                a[j + 1] = a[j]; j -= 1
                F.append(F_(a, [j + 1, j + 2], range(i + 1), c))
            else:
                F.append(F_(a, [j + 1], range(i + 1), c)); break
        a[j + 1] = key
        F.append(F_(a, [j + 1], range(i + 1), c))
    F.append(F_(a, (), range(n), c))
    return F

def merge_frames(arr):
    a = arr[:]; n = len(a); c = [0]
    runs = [(i, i + 1) for i in range(n)]      # current maximal sorted runs
    F = [F_(a, bx=list(runs))]
    def ms(lo, hi):
        if hi - lo <= 1: return
        mid = (lo + hi) // 2
        ms(lo, mid); ms(mid, hi)
        runs[:] = [r for r in runs if r[1] <= lo or r[0] >= hi]   # drop the two child runs
        left = a[lo:mid]; right = a[mid:hi]; li = ri = 0; pos = lo
        def push():
            F.append(F_(a, [pos - 1], (), c[0], bx=list(runs), ab=(lo, hi)))
        while li < len(left) and ri < len(right):
            c[0] += 1
            if left[li] <= right[ri]: a[pos] = left[li]; li += 1
            else: a[pos] = right[ri]; ri += 1
            pos += 1; push()
        while li < len(left):
            a[pos] = left[li]; li += 1; pos += 1; push()
        while ri < len(right):
            a[pos] = right[ri]; ri += 1; pos += 1; push()
        runs.append((lo, hi)); runs.sort()
        F.append(F_(a, (), (), c[0], bx=list(runs)))
    ms(0, n)
    F.append(F_(a, (), range(n), c[0], bx=[(0, n)]))
    return F

def quick_frames(arr):
    a = arr[:]; n = len(a); F = [F_(a)]; c = [0]; locked = set()
    def qs(lo, hi):                       # Lomuto, last element pivot
        if hi - lo <= 1:
            if hi - lo == 1: locked.add(lo)
            return
        pivot = a[hi - 1]; store = lo
        for j in range(lo, hi - 1):
            c[0] += 1
            F.append(F_(a, [j, store], locked, c[0], p=[hi - 1]))   # pivot is red
            if a[j] < pivot:
                a[store], a[j] = a[j], a[store]; store += 1
        a[store], a[hi - 1] = a[hi - 1], a[store]
        locked.add(store)
        F.append(F_(a, [store], locked, c[0]))     # pivot dropped into final slot (green)
        qs(lo, store); qs(store + 1, hi)
    qs(0, n)
    F.append(F_(a, (), range(n), c[0]))
    return F

BUILDERS = {
    "Bubble sort": bubble_frames, "Selection sort": selection_frames,
    "Insertion sort": insertion_frames, "Merge sort": merge_frames,
    "Quicksort": quick_frames,
}

# ---------------- drawing ----------------
def make_bars(values, x_left, width, baseline, max_h, bar_gap=0.85):
    n = len(values); slot = width / n; bw = slot * bar_gap
    g = VGroup()
    for i, v in enumerate(values):
        h = max(0.02, v / MAXV * max_h)
        r = Rectangle(width=bw, height=h, fill_color=BLUE, fill_opacity=0.9,
                      stroke_color=BLUE, stroke_width=1)
        r.move_to([x_left + (i + 0.5) * slot, baseline + h / 2, 0])
        g.add(r)
    return g, slot

def bar_painter(group, frames, tick, x_left, slot, baseline, max_h):
    def upd(grp):
        idx = int(np.clip(int(tick.get_value()), 0, len(frames) - 1))
        fr = frames[idx]; vals = fr["v"]; act = fr["a"]; dn = fr["d"]; pv = fr["p"]
        for i, bar in enumerate(grp):
            h = max(0.02, vals[i] / MAXV * max_h)
            bar.stretch_to_fit_height(h)
            bar.move_to([x_left + (i + 0.5) * slot, baseline + h / 2, 0])
            col = GREEN if i in dn else (RED if i in pv else (AMBER if i in act else BLUE))
            bar.set_fill(col, opacity=0.9); bar.set_stroke(col, width=1)
    group.add_updater(upd)
    return group

def box_painter(pool, frames, tick, x_left, slot, baseline, max_h):
    cy = baseline + max_h / 2; bh = max_h + 0.22
    def upd(grp):
        idx = int(np.clip(int(tick.get_value()), 0, len(frames) - 1))
        fr = frames[idx]
        boxlist = [(s, e, "set") for (s, e) in fr["bx"] if e - s >= 2]
        if fr["ab"] is not None:
            boxlist.append((fr["ab"][0], fr["ab"][1], "act"))
        for k, rect in enumerate(grp):
            if k < len(boxlist):
                s, e, kind = boxlist[k]
                w = (e - s) * slot
                rect.stretch_to_fit_width(w); rect.stretch_to_fit_height(bh)
                rect.move_to([x_left + (s + e) / 2 * slot, cy, 0])
                col = AMBER if kind == "act" else TXT_DIM
                rect.set_stroke(col, width=(2.4 if kind == "act" else 1.4), opacity=1.0)
                rect.set_fill(opacity=0)
            else:
                rect.set_stroke(opacity=0); rect.set_fill(opacity=0)
    grp = VGroup(*[Rectangle(width=1, height=1, fill_opacity=0, stroke_opacity=0) for _ in pool])
    grp.add_updater(upd)
    return grp


class _SortBase(Scene):
    def run_single(self, name, boxes=False):
        frames = BUILDERS[name](ARR)
        total_cmp = frames[-1]["c"]
        title = Text(name, color=TXT, font_size=42, weight=BOLD).to_edge(UP, buff=0.4)
        x_left, width, baseline, max_h = -6.4, 12.8, -3.0, 5.4
        bars, slot = make_bars(ARR, x_left, width, baseline, max_h)
        tick = ValueTracker(0)
        self.add(bars)
        if boxes:
            boxgrp = box_painter(range(N), frames, tick, x_left, slot, baseline, max_h)
            self.add(boxgrp)
        bar_painter(bars, frames, tick, x_left, slot, baseline, max_h)
        clabel = Text("comparisons:", color=TXT_DIM, font_size=26)
        counter = Integer(0, color=TXT, font_size=26)
        cgrp = VGroup(clabel, counter).arrange(RIGHT, buff=0.18).next_to(title, DOWN, buff=0.25)
        counter.add_updater(lambda m: m.set_value(frames[min(int(tick.get_value()), len(frames) - 1)]["c"]))
        self.add(title, cgrp)
        run_t = float(np.clip(len(frames) / 70.0, 6.0, 26.0))
        self.play(tick.animate.set_value(len(frames) - 1), run_time=run_t, rate_func=linear)
        counter.set_value(total_cmp)
        self.wait(1.5)

    def run_race(self):
        names = ["Bubble sort", "Selection sort", "Insertion sort", "Merge sort", "Quicksort"]
        specs = {nm: BUILDERS[nm](ARR) for nm in names}
        maxlen = max(len(f) for f in specs.values())
        title = Text("Five sorts, one shuffled list — racing by comparisons",
                     color=TXT, font_size=30, weight=BOLD).to_edge(UP, buff=0.18)
        self.add(title)
        tick = ValueTracker(0)
        x_left, width, max_h = -3.6, 8.6, 0.92
        row_y = [2.15, 0.83, -0.49, -1.81, -3.13]
        mobs = []
        for nm, by in zip(names, row_y):
            frames = specs[nm]
            bars, slot = make_bars(ARR, x_left, width, by, max_h)
            bar_painter(bars, frames, tick, x_left, slot, by, max_h)
            label = Text(nm, color=TXT, font_size=22).move_to([-5.8, by + 0.45, 0])
            counter = Integer(0, color=TXT_DIM, font_size=22).move_to([5.9, by + 0.45, 0])
            counter.add_updater(lambda m, fr=frames: m.set_value(fr[min(int(tick.get_value()), len(fr) - 1)]["c"]))
            self.add(bars, label, counter)
            mobs.append((frames, counter))
        run_t = float(np.clip(maxlen / 55.0, 12.0, 30.0))
        self.play(tick.animate.set_value(maxlen - 1), run_time=run_t, rate_func=linear)
        for frames, counter in mobs:
            counter.set_value(frames[-1]["c"])
        self.wait(2.0)


class SortRace(_SortBase):
    def construct(self): self.run_race()

class BubbleSort(_SortBase):
    def construct(self): self.run_single("Bubble sort")

class SelectionSort(_SortBase):
    def construct(self): self.run_single("Selection sort")

class InsertionSort(_SortBase):
    def construct(self): self.run_single("Insertion sort")

class MergeSort(_SortBase):
    def construct(self): self.run_single("Merge sort", boxes=True)

class QuickSort(_SortBase):
    def construct(self): self.run_single("Quicksort")
