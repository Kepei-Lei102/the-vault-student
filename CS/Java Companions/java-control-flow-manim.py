"""Manim scene for [[Java Control Flow]].

NestedLoops — what "the inner loop must finish before the outer loop moves on" looks like.  Left: a 3 x 4 grid filled by
              for row / for col, one cell per run of the innermost statement, with the two counters shown.  The outer counter
              changes 3 times while the inner one changes 12.  Right: the triangular loop  (col <= row), whose inner limit
              depends on the outer variable, so the count is 1 + 2 + 3 + 4 = 10 and not 16.
Smoke:  manim -ql --fps 15 java-control-flow-manim.py NestedLoops
Final:  manim -qk java-control-flow-manim.py NestedLoops
"""
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b"
S = 0.95          # cell size


def code_block(lines, centre):
    """Text strips leading spaces, so the indentation is put back by shifting each line."""
    rows = VGroup()
    for k, (indent, txt, col) in enumerate(lines):
        t = Text(txt, font="Menlo", font_size=19, color=col)
        t.move_to([0, -0.36 * k, 0], aligned_edge=LEFT).shift(RIGHT * 0.5 * indent)
        rows.add(t)
    return rows.move_to(centre)


def cell(x, y, col=GREY_T, op=0.0):
    return Square(side_length=S, color=col, stroke_width=2, fill_color=AMBER_H, fill_opacity=op).move_to([x, y, 0])


class NestedLoops(Scene):
    def construct(self):
        self.add(Text("A loop inside a loop: the inner one runs from start to finish, every time", font_size=26, color=GREY_T).to_edge(UP, buff=0.25))
        cap = Text("for each row ... the whole inner loop", font_size=24, color=GREY_T).to_edge(DOWN, buff=0.35)
        self.add(cap); self.wait(1.5)

        def say(s, col=GREY_T):
            nonlocal cap
            self.remove(cap); cap = Text(s, font_size=24, color=col).to_edge(DOWN, buff=0.35); self.add(cap)

        # ---------- left: the rectangle ----------
        x0, y0 = -6.0, 0.55
        code1 = code_block([(0, "for (int row = 1; row <= 3; row++) {", BLUE_H), (1, "for (int col = 1; col <= 4; col++) {", PURPLE_H),
                            (2, "count++;", AMBER_H), (1, "}", PURPLE_H), (0, "}", BLUE_H)], [-3.9, 2.15, 0])
        grid = VGroup(*[cell(x0 + c * S, y0 - r * S) for r in range(3) for c in range(4)])
        self.play(FadeIn(code1), FadeIn(grid), run_time=0.8)
        row_t = Text("row = 1", font="Menlo", font_size=22, color=BLUE_H).move_to([-1.3, 0.55, 0])
        col_t = Text("col = 1", font="Menlo", font_size=22, color=PURPLE_H).move_to([-1.3, 0.0, 0])
        cnt_t = Text("count = 0", font="Menlo", font_size=22, color=AMBER_H).move_to([-1.3, -0.55, 0])
        self.add(row_t, col_t, cnt_t)
        count = 0
        for r in range(3):
            new_row = Text(f"row = {r + 1}", font="Menlo", font_size=22, color=BLUE_H).move_to(row_t)
            self.remove(row_t); row_t = new_row; self.add(row_t)
            if r == 1:
                say("row moved on by one; col starts again from 1", BLUE_H)
            for c in range(4):
                count += 1
                new_col = Text(f"col = {c + 1}", font="Menlo", font_size=22, color=PURPLE_H).move_to(col_t)
                new_cnt = Text(f"count = {count}", font="Menlo", font_size=22, color=AMBER_H).move_to(cnt_t)
                self.remove(col_t, cnt_t); col_t, cnt_t = new_col, new_cnt; self.add(col_t, cnt_t)
                self.play(grid[r * 4 + c].animate.set_fill(AMBER_H, opacity=0.55), run_time=0.45 if r else 0.7)
            self.wait(0.9)
        say("3 rows of 4: the innermost line ran 3 x 4 = 12 times", AMBER_H); self.wait(2.2)

        # ---------- right: the triangle ----------
        x1, y1 = 1.0, 0.55
        code2 = code_block([(0, "for (int row = 1; row <= 4; row++) {", BLUE_H), (1, "for (int col = 1; col <= row; col++) {", PURPLE_H),
                            (2, "count++;", AMBER_H), (1, "}", PURPLE_H), (0, "}", BLUE_H)], [3.3, 2.15, 0])
        ghost = VGroup(*[cell(x1 + c * S, y1 - r * S, op=0.0).set_stroke(opacity=0.25) for r in range(4) for c in range(4)])
        say("now the inner limit is  col <= row :  it depends on the outer variable", PURPLE_H)
        self.play(FadeIn(code2), FadeIn(ghost), run_time=0.8); self.wait(1.2)
        row2 = Text("row = 1", font="Menlo", font_size=22, color=BLUE_H).move_to([5.9, 0.55, 0])
        cnt2 = Text("count = 0", font="Menlo", font_size=22, color=AMBER_H).move_to([5.9, -0.55, 0]); self.add(row2, cnt2)
        count = 0
        for r in range(4):
            new_r = Text(f"row = {r + 1}", font="Menlo", font_size=22, color=BLUE_H).move_to(row2)
            self.remove(row2); row2 = new_r; self.add(row2)
            for c in range(r + 1):
                count += 1
                new = Text(f"count = {count}", font="Menlo", font_size=22, color=AMBER_H).move_to(cnt2)
                self.remove(cnt2); cnt2 = new; self.add(cnt2)
                sq = ghost[r * 4 + c]
                self.play(sq.animate.set_fill(AMBER_H, opacity=0.55).set_stroke(opacity=1), run_time=0.45)
            self.wait(0.7)
        say("1 + 2 + 3 + 4 = 10, not 4 x 4 = 16.  To count the runs, ask how far the inner loop goes each time.", GREEN_H)
        self.wait(4.5)
