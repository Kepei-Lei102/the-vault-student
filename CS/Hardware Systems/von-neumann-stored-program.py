# stack: Manim
# The stored-program idea: program and data share one read/write memory, and
# instructions are just numbers. Reprogram by loading different numbers -- not
# by rewiring. Shows the SAME machine run an ADD program, then get reprogrammed
# (one number changed in memory) into a MULTIPLY program. Code is data.
#
# Render (vault showcase, 4K):  manim -qk von-neumann-stored-program.py StoredProgram
# Layout still (fast check):    PIPE_STILL=1 manim -s -ql von-neumann-stored-program.py StoredProgram
#
# Vault palette: BG #1e1e1e, text #cccccc / #888888; semantic amber/purple/teal/green/red.

import os
from manim import *

config.background_color = "#1e1e1e"
TXT   = "#cccccc"
DIM   = "#888888"
AMBER = "#f59e0b"   # reprogram / highlight
PURPLE= "#7c3aed"   # CPU
TEAL  = "#0891b2"   # data values
GREEN = "#059669"   # result
RED   = "#dc2626"   # the single bus / bottleneck

MEMX = 2.0
YS = [2.3, 1.6, 0.9, 0.2, -0.5, -1.2]          # addresses 0..5
PROG = {0: ("30", "READ a"), 1: ("41", "ADD b"), 2: ("50", "WRITE result"),
        3: ("5", "a = 5"), 4: ("3", "b = 3"), 5: ("0", "result")}


class StoredProgram(Scene):
    def construct(self):
        still = os.environ.get("PIPE_STILL")

        title = Text("The stored-program idea", color=TXT, weight=BOLD).scale(0.6).move_to([0, 3.55, 0])
        sub = Text("program and data share one memory — and instructions are just numbers",
                   color=DIM).scale(0.36).next_to(title, DOWN, buff=0.12)

        # ---- CPU ----
        cpu = RoundedRectangle(width=2.7, height=1.7, corner_radius=0.14,
                               stroke_color=PURPLE, stroke_width=2.5,
                               fill_color=PURPLE, fill_opacity=0.12).move_to([-4.0, 0.55, 0])
        cpu_lbl = Text("CPU", color=PURPLE, weight=BOLD).scale(0.7).move_to([-4.0, 0.78, 0])
        cpu_sub = Text("(never rewired)", color=DIM).scale(0.34).move_to([-4.0, 0.28, 0])

        # ---- single bus (bottleneck) ----
        bus = Line([-2.65, 0.55, 0], [1.2, 0.55, 0], color=RED, stroke_width=4)
        bus.add_tip(tip_length=0.18, at_start=True)
        bus.add_tip(tip_length=0.18)
        bus_lbl = Text("one bus", color=RED).scale(0.32).move_to([-0.72, 0.85, 0])

        # ---- memory ----
        mem_hdr = Text("MEMORY", color=TEAL, weight=BOLD).scale(0.5).move_to([MEMX, 2.95, 0])
        boxes, addrs, decs = {}, {}, {}
        for a, y in zip(range(6), YS):
            boxes[a] = Rectangle(width=1.5, height=0.6, stroke_color=DIM, stroke_width=1.5,
                                 fill_opacity=0).move_to([MEMX, y, 0])
            addrs[a] = Text(str(a), color=DIM).scale(0.4).move_to([MEMX - 1.06, y, 0])
            decs[a] = Text(PROG[a][1], color=DIM).scale(0.4)
            decs[a].next_to(boxes[a], RIGHT, buff=0.22).align_to(boxes[a], LEFT).shift(RIGHT * 1.95)
        for a in range(6):
            decs[a].move_to([MEMX + 2.05, YS[a], 0]).align_to([MEMX + 0.9, 0, 0], LEFT)

        # ---- status (left, under CPU) ----
        task_t = Text("task:  —", color=TXT).scale(0.46).move_to([-4.0, -1.7, 0])
        res_t = Text("result:  —", color=TXT).scale(0.46).move_to([-4.0, -2.35, 0])

        cap = Text("A von Neumann machine: program and data live in one memory.",
                   color=TXT).scale(0.42).move_to([0, -3.35, 0])

        frame = VGroup(cpu, cpu_lbl, cpu_sub, bus, bus_lbl, mem_hdr,
                       *boxes.values(), *addrs.values(), *decs.values(), task_t, res_t)

        self.play(FadeIn(title), FadeIn(sub), run_time=0.8)
        self.play(FadeIn(frame), run_time=1.0)
        self.play(FadeIn(cap), run_time=0.5)

        # ---- load program A (numbers stream into memory) ----
        vals = {}
        def newcap(s, color=TXT):
            nonlocal cap
            nc = Text(s, color=color).scale(0.42).move_to([0, -3.35, 0])
            self.play(FadeOut(cap, shift=DOWN * 0.1), FadeIn(nc, shift=DOWN * 0.1), run_time=0.7)
            cap = nc

        if not still:
            newcap("Load Program A. Each instruction is stored as a number — code is data.")
        loads = []
        for a in range(6):
            color = TEAL if a >= 3 else TXT
            vals[a] = Text(PROG[a][0], color=color).scale(0.5).move_to([MEMX, YS[a], 0])
            loads.append(FadeIn(vals[a], shift=LEFT * 0.2))
        self.play(LaggedStart(*loads, lag_ratio=0.12), run_time=1.6)

        if still:
            return

        def run_program(task, taskcol, result):
            # fetch instructions 0,1,2 in turn
            for a in (0, 1, 2):
                self.play(Indicate(boxes[a], color=AMBER, scale_factor=1.12),
                          Indicate(vals[a], color=AMBER, scale_factor=1.12), run_time=0.5)
            nt = Text(f"task:  {task}", color=taskcol, weight=BOLD).scale(0.46).move_to([-4.0, -1.7, 0])
            self.play(Transform(task_t, nt), run_time=0.4)
            nr_val = Text(str(result), color=GREEN, weight=BOLD).scale(0.5).move_to([MEMX, YS[5], 0])
            nres = Text(f"result:  {result}", color=GREEN, weight=BOLD).scale(0.46).move_to([-4.0, -2.35, 0])
            self.play(FadeTransform(vals[5], nr_val), Transform(res_t, nres),
                      Indicate(boxes[5], color=GREEN, scale_factor=1.2), run_time=0.6)
            vals[5] = nr_val

        newcap("The CPU reads the numbers as instructions and runs them:  5 + 3 = 8.")
        run_program("ADD", TEAL, 8)

        # ---- reprogram: change ONE number in memory ----
        self.wait(0.3)
        newcap("A different task? Don't rewire the machine — load a different number.", AMBER)
        nv = Text("62", color=AMBER, weight=BOLD).scale(0.5).move_to([MEMX, YS[1], 0])
        ndec = Text("MUL b", color=AMBER).scale(0.4).move_to(decs[1].get_center())
        self.play(FadeTransform(vals[1], nv), FadeTransform(decs[1], ndec),
                  Indicate(boxes[1], color=AMBER, scale_factor=1.25), run_time=0.9)
        vals[1] = nv
        decs[1] = ndec

        newcap("Same wires, same data (5 and 3) — one new instruction:  5 × 3 = 15.")
        run_program("MULTIPLY", AMBER, 15)

        # ---- code is data ----
        self.wait(0.3)
        newcap("That 62 is an instruction to the CPU — but it is only a number. Code is data.")
        self.play(Indicate(vals[1], color=TXT, scale_factor=1.6), run_time=0.9)

        # ---- punchline ----
        self.wait(0.3)
        self.play(FadeOut(cap), run_time=0.4)
        punch = Text(
            "Change the numbers in memory, change what the computer is.\n"
            "Turing's universal machine — finally built.",
            color=TXT, line_spacing=0.85, weight=BOLD).scale(0.46)
        punch.move_to([0, -3.15, 0])
        self.play(FadeIn(punch), run_time=0.9)
        self.wait(1.5)
