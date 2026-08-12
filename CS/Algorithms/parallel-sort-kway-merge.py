"""
Manim — the k-way merge for  CS/Algorithms/Parallel and External Sorting.md
Renders ONE MP4:  parallel-sort-kway-merge.mp4

Shows the heart of external (and parallel) merge sort: fold k sorted runs into
one sorted stream using a min-heap that holds the current FRONT of each run.
Each step: the root (smallest of the k fronts) leaves to the output, the next
element of that run enters the root, and a sift-down restores the heap -- so
every output element costs O(log k), independent of run size.

k = 4 runs: A[1,8,12] B[2,5,11] C[3,7,9] D[4,6,10]  ->  output 1..12.
The first 8 pops are animated in full (heap stays a 4-node tree, real
sift-downs); the tail drains quickly with a caption.

Render (check): python3 -m manim -qm parallel-sort-kway-merge.py KWayMerge
Render (final): manim -qk parallel-sort-kway-merge.py KWayMerge
  then copy media/videos/parallel-sort-kway-merge/2160p60/KWayMerge.mp4
       -> ./parallel-sort-kway-merge.mp4   and   rm -rf media
"""
import os
from manim import *

BG="#1e1e1e"; TXT="#cccccc"; DIM="#888888"
BLUE="#2563eb"; GREEN="#059669"; AMBER="#f59e0b"; TEAL="#0891b2"; RED="#dc2626"
config.background_color = BG

RUNS   = {0:[1,8,12], 1:[2,5,11], 2:[3,7,9], 3:[4,6,10]}
RUNCOL = {0:BLUE, 1:GREEN, 2:AMBER, 3:TEAL}
RUNLBL = {0:"A", 1:"B", 2:"C", 3:"D"}

# heap-slot positions (a 4-node binary tree): 0=root, 1/2=children, 3=child of 1
SLOT = {0:(1.9, 2.0, 0), 1:(0.6, 0.55, 0), 2:(3.2, 0.55, 0), 3:(0.0, -0.9, 0)}
EDGES = [(0,1),(0,2),(1,3)]
DETAIL_POPS = 8
STOP = int(os.environ.get("KMERGE_STOP", "0"))   # truncate for still-checking

# ---- simulate the first DETAIL_POPS pops, recording every animation op ----
def simulate():
    heap = [{"v":RUNS[r][0],"run":r,"pos":0} for r in range(4)]   # [1,2,3,4] is already a heap
    ops = []
    def sift_down(i):
        n=len(heap)
        while True:
            l,r,s=2*i+1,2*i+2,i
            if l<n and heap[l]["v"]<heap[s]["v"]: s=l
            if r<n and heap[r]["v"]<heap[s]["v"]: s=r
            if s==i: break
            heap[i],heap[s]=heap[s],heap[i]
            ops.append(("swap",i,s)); i=s
    out=[]
    for _ in range(DETAIL_POPS):
        root=heap[0]
        ops.append(("pop",root["v"],root["run"]))
        out.append(root["v"])
        r,pos=root["run"],root["pos"]
        nv=RUNS[r][pos+1]
        heap[0]={"v":nv,"run":r,"pos":pos+1}
        ops.append(("refill",nv,r,pos+1))
        sift_down(0)
    return ops

OPS = simulate()


class KWayMerge(Scene):
    def construct(self):
        title = Text("k-way merge: fold k sorted runs into one", color=TXT, weight=BOLD).scale(0.7)
        title.to_edge(UP, buff=0.28)
        sub = Text("a min-heap returns the smallest of the k fronts in O(log k)", color=DIM).scale(0.42)
        sub.next_to(title, DOWN, buff=0.1)
        self.play(FadeIn(title), FadeIn(sub))

        # ---- run rows on the left ----
        run_y = {0:2.35, 1:1.55, 2:0.75, 3:-0.05}
        self.run_cells = {}          # (run, pos) -> cell VGroup
        self.run_next  = {r:0 for r in range(4)}
        for r in range(4):
            lbl = Text(RUNLBL[r], color=RUNCOL[r], weight=BOLD).scale(0.5).move_to([-6.7, run_y[r], 0])
            self.add(lbl)
            for j,val in enumerate(RUNS[r]):
                c = self.cell(val, RUNCOL[r], [-6.1 + j*0.62, run_y[r], 0])
                self.run_cells[(r,j)] = c
                self.add(c)
        runs_cap = Text("4 sorted runs", color=DIM).scale(0.38).move_to([-6.0, 3.0, 0])
        self.add(runs_cap)

        # ---- heap skeleton (edges + slot rings + labels), grouped so the tail can fade it ----
        self.heap_skel = VGroup()
        for a,b in EDGES:
            self.heap_skel.add(Line(SLOT[a], SLOT[b], color=DIM, stroke_width=2).set_opacity(0.4))
        for i in SLOT:
            self.heap_skel.add(Circle(radius=0.34, color=DIM, stroke_width=1.5).set_opacity(0.35).move_to(SLOT[i]))
        self.heap_skel.add(Text("min-heap", color=DIM).scale(0.42).move_to([1.9, 2.72, 0]))
        self.heap_skel.add(Text("root = smallest", color=DIM).scale(0.34).next_to(SLOT[0], RIGHT, buff=0.2))
        self.add(self.heap_skel)

        # ---- output row ----
        self.out_x0, self.out_dx, self.out_y = -5.9, 0.56, -2.95
        out_lbl = Text("output (sorted):", color=DIM).scale(0.42).move_to([-5.0, -2.3, 0])
        self.add(out_lbl)
        self.out_count = 0

        # ---- lift each run's front into the heap (build the initial heap) ----
        self.slot_tok = {}
        lifts=[]
        for r in range(4):
            tok = self.token(RUNS[r][0], r)
            tok.move_to(self.run_cells[(r,0)].get_center())
            self.add(tok)
            self.slot_tok[r] = tok
            self.run_cells[(r,0)].set_opacity(0.18)
            self.run_next[r] = 1
            lifts.append(tok.animate.move_to(SLOT[r]))
        self.play(*lifts, run_time=1.2)
        self.wait(0.4)

        # ---- replay the recorded ops ----
        done = 0
        for op in OPS:
            if op[0] == "pop":
                _, val, run = op
                self.do_pop()
                done += 1
            elif op[0] == "refill":
                _, val, run, pos = op
                self.do_refill(run, pos)
            elif op[0] == "swap":
                self.do_swap(op[1], op[2])
            if STOP and done >= STOP:
                self.wait(1.0); return

        # ---- fast-forward the tail (9..12): fade the whole heap, then drain ----
        remaining = VGroup(*list(self.slot_tok.values()))
        self.play(FadeOut(self.heap_skel), FadeOut(remaining), run_time=0.5)
        tail_cap = Text("…the heap keeps draining the same way — output stays sorted",
                        color=DIM).scale(0.44).move_to([1.4, 0.8, 0])
        self.play(FadeIn(tail_cap))
        tail = [(9,2),(10,3),(11,1),(12,0)]
        cells=[]
        for val,run in tail:
            cells.append(self.out_cell(val, run))
        self.play(LaggedStart(*[FadeIn(c, shift=UP*0.2) for c in cells], lag_ratio=0.35), run_time=1.6)

        punch = Text("every element out in O(log k) — the merge that scales to disks and clusters",
                     color=TXT).scale(0.46).to_edge(DOWN, buff=0.25)
        self.play(Write(punch)); self.wait(2.2)

    # ---------- helpers ----------
    def cell(self, value, color, center):
        sq = RoundedRectangle(width=0.5, height=0.5, corner_radius=0.08,
                              color=color, stroke_width=2, fill_color=color, fill_opacity=0.12)
        t = Text(str(value), color=TXT).scale(0.42)
        return VGroup(sq, t).move_to(center)

    def token(self, value, run):
        c = Circle(radius=0.32, color=RUNCOL[run], stroke_width=3,
                   fill_color=RUNCOL[run], fill_opacity=0.28)
        t = Text(str(value), color=TXT, weight=BOLD).scale(0.44)
        return VGroup(c, t)

    def do_pop(self):
        tok = self.slot_tok.pop(0, None)
        if tok is None: return
        target = [self.out_x0 + self.out_count*self.out_dx, self.out_y, 0]
        self.out_count += 1
        self.play(tok.animate.scale(0.85).move_to(target), run_time=0.6)

    def do_refill(self, run, pos):
        src = self.run_cells[(run, pos)]
        tok = self.token(RUNS[run][pos], run)
        tok.move_to(src.get_center())
        self.add(tok)
        src.set_opacity(0.18)
        self.slot_tok[0] = tok
        self.play(tok.animate.move_to(SLOT[0]), run_time=0.6)

    def do_swap(self, i, j):
        ti, tj = self.slot_tok[i], self.slot_tok[j]
        self.play(ti.animate.move_to(SLOT[j]), tj.animate.move_to(SLOT[i]), run_time=0.55)
        self.slot_tok[i], self.slot_tok[j] = tj, ti

    def out_cell(self, value, run):
        pos = self.out_count
        self.out_count += 1
        return self.token(value, run).scale(0.85).move_to(
            [self.out_x0 + pos*self.out_dx, self.out_y, 0])
