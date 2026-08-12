"""The pipeline race: uniform RISC syllables vs a fat CISC sentence.

Two identical 4-stage pipelines run on the same clock. The RISC lane
feeds uniform one-cycle instructions and stays full; the CISC lane hits
a multi-cycle MULT that parks in EXECUTE and starves everything behind
it. Completion counters keep the score.

Render (from this folder):
    manim -qm cisc-risc-pipeline.py PipelineRace   # smoke
    manim -qk cisc-risc-pipeline.py PipelineRace   # 4K final
Copy the output beside the card as cisc-risc-pipeline.mp4, then clear
media/ + __pycache__/.
"""

import numpy as np
from manim import *

BG = "#1a1a1a"
GRAY = "#9a9a9a"
GREEN = "#059669"
AMBER = "#f59e0b"
RED = "#dc2626"
PURPLE = "#7c3aed"

config.background_color = BG

STAGES = ["F", "D", "E", "W"]
N_INSTR = 7
TICKS = 13
EXEC_COST_CISC = [1, 4, 1, 1, 3, 1, 1]   # instruction 2 is a MULT, 5 is memory-op


def schedule_risc():
    # instr i is in stage s at tick i + s
    occ = [dict() for _ in range(TICKS + 1)]
    done = [0] * (TICKS + 1)
    for t in range(TICKS + 1):
        for i in range(N_INSTR):
            s = t - i
            if 0 <= s < 4:
                occ[t][i] = s
        done[t] = sum(1 for i in range(N_INSTR) if t - i >= 4)
    return occ, done


def schedule_cisc():
    # simple in-order sim with multi-cycle EXECUTE
    occ = [dict() for _ in range(TICKS + 1)]
    done = [0] * (TICKS + 1)
    stage = {i: -1 for i in range(N_INSTR)}   # -1 waiting, 0..3 stages, 4 done
    e_left = {i: 0 for i in range(N_INSTR)}
    for t in range(1, TICKS + 1):
        for i in range(N_INSTR):               # advance from the front
            if stage[i] == 3:
                stage[i] = 4
            elif stage[i] == 2:
                e_left[i] -= 1
                if e_left[i] <= 0 and not any(stage[j] == 3 for j in range(i)):
                    stage[i] = 3
            elif stage[i] == 1:
                if not any(stage[j] == 2 for j in range(i)):
                    stage[i] = 2
                    e_left[i] = EXEC_COST_CISC[i]
                    e_left[i] -= 0
            elif stage[i] == 0:
                if not any(stage[j] == 1 for j in range(i)):
                    stage[i] = 1
            elif stage[i] == -1:
                if not any(stage[j] == 0 for j in range(i)):
                    stage[i] = 0
                    break                        # one issue per tick
        for i in range(N_INSTR):
            if 0 <= stage[i] < 4:
                occ[t][i] = stage[i]
        done[t] = sum(1 for i in range(N_INSTR) if stage[i] == 4)
    return occ, done


class PipelineRace(Scene):
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=25, color=color).to_edge(DOWN, buff=0.3)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.2), FadeIn(cap, run_time=0.3))
        else:
            self.play(FadeIn(cap, run_time=0.3))
        self._cap = cap

    def lane(self, y, color, title):
        boxes = VGroup()
        labels = VGroup()
        for k, s in enumerate(STAGES):
            b = Square(side_length=1.05, stroke_color=color, stroke_width=2.5,
                       fill_color=color, fill_opacity=0.06).move_to(RIGHT * (0.4 + 1.25 * k) + UP * y)
            boxes.add(b)
            labels.add(Text(s, font_size=20, color=GRAY).next_to(b, UP, buff=0.08))
        t = Text(title, font_size=23, color=color, weight=BOLD).move_to(LEFT * 4.9 + UP * (y + 0.75))
        return boxes, labels, t

    def construct(self):
        occ_r, done_r = schedule_risc()
        occ_c, done_c = schedule_cisc()

        boxes_r, labs_r, title_r = self.lane(1.85, GREEN, "RISC — uniform syllables")
        boxes_c, labs_c, title_c = self.lane(-0.9, AMBER, "CISC — one fat sentence")

        def chips(color, names):
            g = []
            for i in range(N_INSTR):
                c = VGroup(
                    RoundedRectangle(corner_radius=0.08, width=0.92, height=0.5,
                                     stroke_color=color, stroke_width=2,
                                     fill_color=color, fill_opacity=0.28),
                    Text(names[i], font_size=15, color=GRAY, weight=BOLD),
                )
                c[1].move_to(c[0])
                g.append(c)
            return g

    # names: CISC i2 is MULT (the fat one)
        names_r = [f"i{k+1}" for k in range(N_INSTR)]
        names_c = ["i1", "MULT", "i3", "i4", "MEM", "i6", "i7"]
        chips_r = chips(GREEN, names_r)
        chips_c = chips(AMBER, names_c)

        def queue_pos(i, y):
            return LEFT * (2.1 + 0.75 * i) + UP * y

        for i in range(N_INSTR):
            chips_r[i].move_to(queue_pos(i, 1.85))
            chips_c[i].move_to(queue_pos(i, -0.9))

        cnt_r = Text("done: 0", font_size=22, color=GREEN, weight=BOLD).move_to(RIGHT * 6.1 + UP * 1.85)
        cnt_c = Text("done: 0", font_size=22, color=AMBER, weight=BOLD).move_to(RIGHT * 6.1 + DOWN * 0.9)
        clock = Text("tick 0", font_size=22, color=GRAY, weight=BOLD).to_edge(UP, buff=0.3)

        self.play(FadeIn(boxes_r), FadeIn(labs_r), FadeIn(title_r),
                  FadeIn(boxes_c), FadeIn(labs_c), FadeIn(title_c),
                  *[FadeIn(c) for c in chips_r], *[FadeIn(c) for c in chips_c],
                  FadeIn(cnt_r), FadeIn(cnt_c), FadeIn(clock), run_time=1.0)
        self.swap_caption("same clock, same four stages — different diets")

        def stage_pos(s, y):
            return RIGHT * (0.4 + 1.25 * s) + UP * y

        said_stall = False
        for t in range(1, TICKS + 1):
            anims = []
            for i in range(N_INSTR):
                if i in occ_r[t]:
                    anims.append(chips_r[i].animate.move_to(stage_pos(occ_r[t][i], 1.85)))
                elif t - i >= 4:
                    anims.append(chips_r[i].animate.move_to(RIGHT * 5.35 + UP * 1.85).set_opacity(0))
                if i in occ_c[t]:
                    anims.append(chips_c[i].animate.move_to(stage_pos(occ_c[t][i], -0.9)))
                elif occ_c[t - 1].get(i) == 3 and i not in occ_c[t]:
                    anims.append(chips_c[i].animate.move_to(RIGHT * 5.35 + DOWN * 0.9).set_opacity(0))
            nc = Text(f"tick {t}", font_size=22, color=GRAY, weight=BOLD).to_edge(UP, buff=0.3)
            anims.append(Transform(clock, nc))
            nr = Text(f"done: {done_r[t]}", font_size=22, color=GREEN, weight=BOLD).move_to(cnt_r)
            anims.append(Transform(cnt_r, nr))
            ncc = Text(f"done: {done_c[t]}", font_size=22, color=AMBER, weight=BOLD).move_to(cnt_c)
            anims.append(Transform(cnt_c, ncc))
            self.play(*anims, run_time=0.5)
            if t == 4 and not said_stall:
                self.swap_caption("MULT parks in EXECUTE — everything behind it starves", color=RED)
                said_stall = True
            if t == 9:
                self.swap_caption("the RISC lane never missed a beat", color=GREEN)

        self.swap_caption("fixed and simple keeps the factory full — that is the whole RISC bet")
        self.wait(1.6)
