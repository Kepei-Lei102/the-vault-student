"""Manim: pins and rails — invariant lines under M = (2 2; 0 1), then the undo.

One continuous scene, three beats:
  1. The plane with three marked lines: y = -x/2 (amber), the x-axis (green),
     y = x (red), each carrying dots. M = (2 2; 0 1) is the stretch-then-shear
     of 9231/13 N24 Q1 with k = 2.
  2. Apply M. The amber line's dots freeze (line of invariant points — its
     pinned line y = (1-k)/k x = -x/2), the green dots slide x2 along the
     x-axis (invariant line — a rail), the red line swings to y = x/4.
  3. Apply M^-1 — everything walks home; the pins never noticed either trip.

Dots are animated with move_to alongside ApplyMatrix: both use the straight-line
homotopy p -> ((1-t)I + tM)p, so they stay in step and the dots stay round.

Render (4K):  manim -qk invariant-lines-flow.py InvariantLinesFlow
Then copy media/videos/invariant-lines-flow/2160p60/InvariantLinesFlow.mp4
  -> invariant-lines-flow.mp4  beside the card, and delete media/ + __pycache__.
"""

import numpy as np
from manim import (
    Scene, VGroup, Dot, Line, Text, MathTex, FadeIn, FadeOut, ApplyMatrix,
    UP, DOWN, LEFT, RIGHT,
)

BG = "#1e1e1e"
TXT = "#cccccc"
GREY = "#9ca3af"
GREEN = "#059669"
REDC = "#dc2626"
AMBER = "#f59e0b"
FONT = "Helvetica Neue"

M = np.array([[2.0, 2.0], [0.0, 1.0]])
MINV = np.linalg.inv(M)


def v3(x, y):
    return np.array([x, y, 0.0])


def apply2(A, p):
    q = A @ np.array(p[:2])
    return v3(q[0], q[1])


class InvariantLinesFlow(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("What does the machine refuse to move?",
                     font=FONT, font_size=34, color=TXT).to_edge(UP, buff=0.35)
        mtex = MathTex(r"\mathbf{M} = \begin{pmatrix} 2 & 2 \\ 0 & 1 \end{pmatrix}",
                       color=TXT).scale(0.9).to_corner(UP + RIGHT, buff=0.5).shift(DOWN * 0.75)

        # background grid, drawn wide so the shear has room
        grid = VGroup()
        for x in range(-10, 11):
            grid.add(Line(v3(x, -4.6), v3(x, 4.6), color=GREY,
                          stroke_opacity=0.13, stroke_width=1.5))
        for y in range(-4, 5):
            grid.add(Line(v3(-10.5, y), v3(10.5, y), color=GREY,
                          stroke_opacity=0.13, stroke_width=1.5))

        # the three marked lines
        pinned = Line(v3(-3.6, 1.8), v3(3.6, -1.8), color=AMBER, stroke_width=5)
        rail = Line(v3(-3.0, 0.0), v3(3.0, 0.0), color=GREEN, stroke_width=5)
        swing = Line(v3(-1.6, -1.6), v3(1.6, 1.6), color=REDC, stroke_width=4)

        pin_pts = [(-3.0, 1.5), (-1.5, 0.75), (1.5, -0.75), (3.0, -1.5)]
        rail_pts = [(-2.0, 0.0), (-1.0, 0.0), (1.0, 0.0), (2.0, 0.0)]
        swing_pts = [(1.2, 1.2)]
        pin_dots = VGroup(*[Dot(v3(*p), color=AMBER, radius=0.075) for p in pin_pts])
        rail_dots = VGroup(*[Dot(v3(*p), color=GREEN, radius=0.075) for p in rail_pts])
        swing_dots = VGroup(*[Dot(v3(*p), color=REDC, radius=0.075) for p in swing_pts])

        lab_pin = Text("y = −x/2", font=FONT, font_size=24, color=AMBER)
        lab_pin.move_to(v3(-4.5, 2.15))
        lab_rail = Text("the x-axis", font=FONT, font_size=24, color=GREEN)
        lab_rail.move_to(v3(3.9, 0.42))
        lab_swing = Text("y = x", font=FONT, font_size=24, color=REDC)
        lab_swing.move_to(v3(1.05, 1.85))

        plane = VGroup(grid, pinned, rail, swing)

        self.play(FadeIn(title), FadeIn(mtex), FadeIn(grid), run_time=1.2)
        self.play(FadeIn(pinned), FadeIn(rail), FadeIn(swing),
                  FadeIn(pin_dots), FadeIn(rail_dots), FadeIn(swing_dots),
                  FadeIn(lab_pin), FadeIn(lab_rail), FadeIn(lab_swing),
                  run_time=1.2)
        self.wait(1.2)

        # ---------------------------------------------- beat 2: apply M
        go = Text("apply M", font=FONT, font_size=26, color=TXT)
        go.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(go), run_time=0.5)
        moves = [d.animate.move_to(apply2(M, d.get_center()))
                 for d in [*pin_dots, *rail_dots, *swing_dots]]
        self.play(ApplyMatrix(M, plane), *moves,
                  FadeOut(lab_swing), run_time=4.0)
        self.wait(0.4)

        note_pin = Text("pinned — every point fixed", font=FONT,
                        font_size=24, color=AMBER).move_to(v3(-4.35, 2.15))
        note_rail = Text("a rail — slid ×2 along itself", font=FONT,
                         font_size=24, color=GREEN).move_to(v3(4.15, -0.5))
        note_swing = Text("moved — not invariant", font=FONT,
                          font_size=24, color=REDC).move_to(v3(4.9, 0.72))
        self.play(FadeOut(go), FadeOut(lab_pin), FadeIn(note_pin), run_time=0.7)
        self.play(FadeOut(lab_rail), FadeIn(note_rail), run_time=0.7)
        self.play(FadeIn(note_swing), run_time=0.7)
        self.wait(1.8)

        # ---------------------------------------------- beat 3: the undo
        undo = MathTex(r"\text{now } \mathbf{M}^{-1} \text{ — the undo}",
                       color=TXT).scale(0.8).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(undo), FadeOut(note_swing), run_time=0.7)
        moves_back = [d.animate.move_to(apply2(MINV, d.get_center()))
                      for d in [*pin_dots, *rail_dots, *swing_dots]]
        self.play(ApplyMatrix(MINV, plane), *moves_back, run_time=3.2)
        self.wait(0.5)

        final = Text("the rails slid there and back — the pins never noticed either trip",
                     font=FONT, font_size=27, color=TXT).to_edge(DOWN, buff=0.45)
        self.play(FadeOut(undo), FadeOut(note_pin), FadeOut(note_rail),
                  FadeIn(final), run_time=0.9)
        self.wait(2.4)
