"""The loop from the card, traced live: source highlight, registers, memory.

Render (from this folder):
    manim -qm asm-trace.py AsmTrace    # smoke
    manim -qk asm-trace.py AsmTrace    # 4K final
Copy the output beside the card as asm-trace.mp4, then clear
media/ + __pycache__/.
"""

import numpy as np
from manim import *

BG = "#1a1a1a"
GRAY = "#9a9a9a"
BLUE = "#2563eb"
GREEN = "#059669"
AMBER = "#f59e0b"
RED = "#dc2626"
TEAL = "#0891b2"
PURPLE = "#7c3aed"

config.background_color = BG

SRC = [
    "       LDM  #0",
    "       STO  201",
    "LOOP:  LDD  201",
    "       INC  ACC",
    "       STO  201",
    "       LDD  201",
    "       CMP  200",
    "       JPN  LOOP",
    "       OUT",
    "       END",
]


class AsmTrace(Scene):
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=25, color=color).to_edge(DOWN, buff=0.32)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.2), FadeIn(cap, run_time=0.3))
        else:
            self.play(FadeIn(cap, run_time=0.3))
        self._cap = cap

    def construct(self):
        # ---- source listing, left ----
        lines = VGroup(*[
            Text(s, font="Menlo", font_size=23,
                 color=(TEAL if s.startswith("LOOP") else GRAY))
            for s in SRC
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.22).move_to(LEFT * 4.2 + UP * 0.35)
        src_title = Text("source", font_size=22, color=GRAY, weight=BOLD).next_to(lines, UP, buff=0.3)

        # ---- registers and memory, right ----
        def cellbox(label, value, color, pos):
            box = RoundedRectangle(corner_radius=0.1, width=2.5, height=0.85,
                                   stroke_color=color, stroke_width=3,
                                   fill_color=color, fill_opacity=0.10).move_to(pos)
            lab = Text(label, font_size=19, color=GRAY).next_to(box, LEFT, buff=0.25)
            val = Text(value, font="Menlo", font_size=26, color=GRAY, weight=BOLD).move_to(box)
            return box, lab, val

        acc_box, acc_lab, self.acc = cellbox("ACC", "?", PURPLE, RIGHT * 3.4 + UP * 2.3)
        num_box, num_lab, self.num = cellbox("cell 200  NUM", "3", TEAL, RIGHT * 3.4 + UP * 1.1)
        cnt_box, cnt_lab, self.cnt = cellbox("cell 201  COUNT", "?", AMBER, RIGHT * 3.4 + DOWN * 0.1)
        flag_box, flag_lab, self.flag = cellbox("equal flag", "-", GREEN, RIGHT * 3.4 + DOWN * 1.3)

        round_lab = Text("round 0", font_size=22, color=GRAY, weight=BOLD).move_to(RIGHT * 3.4 + DOWN * 2.35)
        self.round_lab = round_lab

        self.play(FadeIn(lines), FadeIn(src_title),
                  *[FadeIn(m) for m in (acc_box, acc_lab, self.acc, num_box, num_lab, self.num,
                                        cnt_box, cnt_lab, self.cnt, flag_box, flag_lab, self.flag, round_lab)],
                  run_time=1.0)

        self.hl = SurroundingRectangle(lines[0], color=YELLOW, buff=0.09, stroke_width=3.5, corner_radius=0.08)
        self.play(Create(self.hl), run_time=0.4)

        def set_val(mobj, new, color=GRAY):
            t = Text(new, font="Menlo", font_size=26, color=color, weight=BOLD).move_to(mobj)
            self.play(Transform(mobj, t, run_time=0.3))

        def step(i, rt=0.45):
            self.play(self.hl.animate.become(
                SurroundingRectangle(lines[i], color=YELLOW, buff=0.09, stroke_width=3.5, corner_radius=0.08)
            ), run_time=rt)

        def set_round(n):
            t = Text(f"round {n}", font_size=22, color=AMBER, weight=BOLD).move_to(self.round_lab)
            self.play(Transform(self.round_lab, t, run_time=0.25))

        # ---- init ----
        self.swap_caption("setup: put 0 into COUNT")
        set_val(self.acc, "0", PURPLE)
        step(1); set_val(self.cnt, "0", AMBER)

        # ---- three rounds ----
        for rnd in (1, 2, 3):
            set_round(rnd)
            if rnd == 1:
                self.swap_caption("round 1: load COUNT, add one, store it back")
            elif rnd == 2:
                self.swap_caption("round 2: same four steps — the loop is a habit")
            else:
                self.swap_caption("round 3: watch the comparison this time", color=AMBER)
            step(2); set_val(self.acc, str(rnd - 1), PURPLE)
            step(3); set_val(self.acc, str(rnd), PURPLE)
            step(4); set_val(self.cnt, str(rnd), AMBER)
            step(5)
            step(6)
            eq = (rnd == 3)
            set_val(self.flag, "EQUAL" if eq else "not equal", GREEN if eq else RED)
            step(7)
            if not eq:
                self.swap_caption(f"COUNT is {rnd}, NUM is 3 — not equal: JPN jumps back to LOOP", color=RED)
            else:
                self.swap_caption("COUNT equals NUM — JPN does NOT jump: fall through", color=GREEN)
            self.wait(0.4)

        # ---- exit ----
        step(8)
        self.swap_caption("OUT writes the ACC — then END hands back control")
        step(9)
        self.wait(0.6)
        self.swap_caption("the exam's trace table is exactly this movie, written down as rows", color=TEAL)
        self.wait(1.6)
