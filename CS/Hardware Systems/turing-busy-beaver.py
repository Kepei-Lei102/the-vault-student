# stack: Manim
# The 3-state busy beaver: the most productive 3-state, 2-symbol Turing machine
# that still halts. Starts on a blank tape, halts after exactly 14 steps leaving
# six 1s. Drives the animation from a ground-truth simulation of the champion
# table  A0:1RB A1:1RH | B0:0RC B1:1RB | C0:1LC C1:1LA.
#
# Render (vault showcase, 4K):  manim -qk turing-busy-beaver.py BusyBeaver
# Layout still (fast check):    PIPE_STILL=1 manim -s -ql turing-busy-beaver.py BusyBeaver
#
# Vault palette: BG #1e1e1e, text #cccccc / #888888; semantic amber/purple/teal/green.

import os
from manim import *

config.background_color = "#1e1e1e"
TXT   = "#cccccc"
DIM   = "#888888"
AMBER = "#f59e0b"   # head / firing rule
PURPLE= "#7c3aed"   # finite control / state
TEAL  = "#0891b2"   # a 1 on the tape
GREEN = "#059669"   # halted / the harvest of 1s
BLUE  = "#2563eb"

TABLE = {('A',0):(1,'R','B'), ('A',1):(1,'R','H'),
         ('B',0):(0,'R','C'), ('B',1):(1,'R','B'),
         ('C',0):(1,'L','C'), ('C',1):(1,'L','A')}

def simulate():
    tape, head, state, steps = {}, 0, 'A', []
    n = 0
    while state != 'H' and n < 100:
        sym = tape.get(head, 0)
        w, mv, ns = TABLE[(state, sym)]
        steps.append((state, head, sym, w, mv, ns))
        tape[head] = w
        head += 1 if mv == 'R' else -1
        state = ns
        n += 1
    return steps, tape

LO, HI = -2, 6
CW, CH = 1.0, 0.92
TY = 0.5

def cx(i):
    return -4.0 + (i + 2) * CW


class BusyBeaver(Scene):
    def construct(self):
        steps, final_tape = simulate()
        still = os.environ.get("PIPE_STILL")

        # ---- title ----
        title = Text("The 3-state busy beaver", color=TXT, weight=BOLD).scale(0.62).move_to([0, 3.45, 0])
        sub = Text("the most steps a 3-state machine can run — and still halt",
                   color=DIM).scale(0.36).next_to(title, DOWN, buff=0.13)

        # ---- tape ----
        cells, vals = {}, {}
        for i in range(LO, HI + 1):
            r = Rectangle(width=CW, height=CH, stroke_color=DIM, stroke_width=1.6,
                          fill_opacity=0).move_to([cx(i), TY, 0])
            t = Text("0", color=DIM).scale(0.6).move_to([cx(i), TY, 0])
            cells[i], vals[i] = r, t
        tape_dots_l = Text("…", color=DIM).scale(0.7).move_to([cx(LO) - 0.7, TY, 0])
        tape_dots_r = Text("…", color=DIM).scale(0.7).move_to([cx(HI) + 0.7, TY, 0])
        tape_cap = Text("tape (unbounded; starts all 0)", color=DIM).scale(0.34).move_to([0, TY - 0.78, 0])

        # ---- head ----
        head_pos = [0]
        outline = Rectangle(width=CW, height=CH, stroke_color=AMBER, stroke_width=4,
                            fill_opacity=0).move_to([cx(0), TY, 0])
        ptr = Polygon([cx(0) - 0.16, TY + CH/2 + 0.42, 0],
                      [cx(0) + 0.16, TY + CH/2 + 0.42, 0],
                      [cx(0), TY + CH/2 + 0.10, 0],
                      color=AMBER, fill_color=AMBER, fill_opacity=1, stroke_width=0)
        head = VGroup(outline, ptr)

        # ---- finite control (state) + step counter ----
        sbox = RoundedRectangle(width=2.1, height=0.95, corner_radius=0.12,
                                stroke_color=PURPLE, stroke_width=2.5,
                                fill_color=PURPLE, fill_opacity=0.12).move_to([-4.55, 2.3, 0])
        sttl = Text("state", color=DIM).scale(0.34).move_to([-4.55, 2.55, 0])
        slbl = Text("A", color=PURPLE, weight=BOLD).scale(0.7).move_to([-4.55, 2.12, 0])
        counter = Text("step 0 / 14", color=TXT).scale(0.46).move_to([4.35, 2.3, 0])

        # ---- caption ----
        cap = Text("Starts in state A on a blank tape.", color=TXT).scale(0.42).move_to([0, -1.15, 0])

        # ---- rule table (delta) ----
        colx = {'A': -0.7, 'B': 1.15, 'C': 3.0}
        rowy = {0: -2.35, 1: -3.05}
        bw, bh = 1.55, 0.6
        rule_boxes, table_grp = {}, VGroup()
        dlabel = Text("rule-book δ", color=DIM).scale(0.4).move_to([-3.05, -1.78, 0])
        table_grp.add(dlabel)
        for s, x in colx.items():
            table_grp.add(Text(s, color=PURPLE, weight=BOLD).scale(0.5).move_to([x, -1.78, 0]))
        for sym, y in rowy.items():
            table_grp.add(Text(f"reads {sym}", color=DIM).scale(0.38).move_to([-3.05, y, 0]))
        for s, x in colx.items():
            for sym, y in rowy.items():
                w, mv, ns = TABLE[(s, sym)]
                box = Rectangle(width=bw, height=bh, stroke_color=DIM, stroke_width=1.3,
                                fill_opacity=0).move_to([x, y, 0])
                txt = Text(f"{w}  {mv}  {ns}", color=TXT).scale(0.4).move_to([x, y, 0])
                rule_boxes[(s, sym)] = box
                table_grp.add(box, txt)
        legend = Text("each cell:  write · move · next-state      (H = halt)",
                      color=DIM).scale(0.33).move_to([0.1, -3.6, 0])
        table_grp.add(legend)

        # ---- assemble ----
        self.play(FadeIn(title), FadeIn(sub), run_time=0.8)
        self.play(*[FadeIn(cells[i]) for i in range(LO, HI + 1)],
                  *[FadeIn(vals[i]) for i in range(LO, HI + 1)],
                  FadeIn(tape_dots_l), FadeIn(tape_dots_r), FadeIn(tape_cap), run_time=0.8)
        self.play(FadeIn(head), FadeIn(sbox), FadeIn(sttl), FadeIn(slbl),
                  FadeIn(counter), FadeIn(table_grp), run_time=0.8)
        self.play(FadeIn(cap), run_time=0.5)

        if still:
            return

        self.wait(0.6)

        move_word = {'R': "step right", 'L': "step left"}
        for k, (state, hd, sym, w, mv, ns) in enumerate(steps):
            halting = (ns == 'H')
            # 1) light up the firing rule + narrate
            new_cap = Text(
                f"state {state} reads {sym}  →  write {w}, {move_word[mv]}, "
                + ("HALT" if halting else f"go to {ns}"),
                color=(GREEN if halting else TXT)).scale(0.42).move_to([0, -1.15, 0])
            self.play(Indicate(rule_boxes[(state, sym)], color=AMBER, scale_factor=1.18),
                      FadeOut(cap, shift=DOWN * 0.12), FadeIn(new_cap, shift=DOWN * 0.12),
                      run_time=0.9)
            cap = new_cap
            # 2) write the symbol under the head
            nv = Text(str(w), color=(TEAL if w == 1 else DIM)).scale(0.6).move_to([cx(hd), TY, 0])
            self.play(FadeTransform(vals[hd], nv), run_time=0.5)
            vals[hd] = nv
            # 3) change state + advance the step counter
            ncount = Text(f"step {k+1} / 14", color=TXT).scale(0.46).move_to([4.35, 2.3, 0])
            nstate = Text(ns if not halting else "HALT",
                          color=(GREEN if halting else PURPLE), weight=BOLD)
            nstate.scale(0.7 if not halting else 0.5).move_to([-4.55, 2.12, 0])
            self.play(Transform(slbl, nstate), Transform(counter, ncount), run_time=0.45)
            # 4) move the head (unless we just halted)
            if not halting:
                shift = RIGHT * CW if mv == 'R' else LEFT * CW
                self.play(head.animate.shift(shift), run_time=0.5)
                head_pos[0] += 1 if mv == 'R' else -1

        # ---- halt / harvest ----
        self.wait(0.4)
        done = Text("Halted after 14 steps.", color=GREEN, weight=BOLD).scale(0.5).move_to([0, -1.15, 0])
        self.play(FadeOut(cap), FadeIn(done))
        cap = done
        ones = sorted(i for i, v in final_tape.items() if v == 1 and LO <= i <= HI)
        tally = None
        for n, i in enumerate(ones, start=1):
            tcount = Text(str(n), color=GREEN, weight=BOLD).scale(0.55).move_to([0, TY + 1.25, 0])
            anims = [Indicate(vals[i], color=GREEN, scale_factor=1.4)]
            anims.append(FadeIn(tcount) if tally is None else FadeTransform(tally, tcount))
            self.play(*anims, run_time=0.38)
            tally = tcount
        six = Text(f"{len(ones)} ones — the record Σ(3) = {len(ones)}",
                   color=GREEN).scale(0.4).next_to(tally, RIGHT, buff=0.25)
        self.play(FadeIn(six), run_time=0.5)

        self.wait(0.5)
        punch = Text(
            "Three states halt at step 14. But BB(n) is uncomputable —\n"
            "no program can predict how long an arbitrary machine runs.",
            color=TXT, line_spacing=0.8).scale(0.4)
        punch.move_to([0, -2.55, 0])
        self.play(FadeOut(table_grp), run_time=0.5)
        self.play(FadeIn(punch), run_time=0.8)
        self.wait(1.4)
