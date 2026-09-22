"""Manim scene for [[Vector Calculus]].

PaddleWheel — a tiny paddle wheel carried through three fields.  In the spreading field F = (x, y) it never turns: the
              field pushes equally on both sides.  In the rotating field G = (-y, x) it turns everywhere, including far from the
              centre, because the far paddle is always pushed harder than the near one.  In the shear H = (y, 0), where nothing
              visibly rotates, it turns anyway, clockwise, because the top paddle is pushed more than the bottom one.  Curl is
              what the wheel measures, and it is a local quantity: it is about the difference across the wheel, not about
              whether the field goes round in circles.
Smoke:  manim -ql --fps 15 vector-calculus-manim.py PaddleWheel
Final:  manim -qk vector-calculus-manim.py PaddleWheel
"""
import numpy as np
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b"

FIELDS = [("spreading  F = (x, y)", lambda p: np.array([p[0], p[1], 0]), 0.0, BLUE_H, "curl = 0:  the wheel does not turn", -4.2),
          ("rotating  G = (-y, x)", lambda p: np.array([-p[1], p[0], 0]), 2.0, PURPLE_H, "curl = 2 everywhere, even out here", 0.0),
          ("shear  H = (y, 0)", lambda p: np.array([p[1], 0, 0]), -1.0, AMBER_H, "curl = -1:  nothing goes round, and it still turns", 4.2)]


class PaddleWheel(Scene):
    def construct(self):
        self.add(Text("Curl is what a tiny paddle wheel measures, wherever you put it", font_size=26, color=GREY_T).to_edge(UP, buff=0.25))
        cap = Text("three fields; the wheel is placed at the same off-centre spot in each", font_size=24, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(cap)

        def say(s, col=GREY_T):
            nonlocal cap
            self.remove(cap); cap = Text(s, font_size=24, color=col).to_edge(DOWN, buff=0.3); self.add(cap)

        wheels, trackers = [], []
        for name, f, w, col, note, cx in FIELDS:
            self.add(Text(name, font_size=22, color=col).move_to([cx, 2.5, 0]))
            g = np.linspace(-1.75, 1.75, 8)
            arrows = VGroup()
            for X in g:
                for Y in g:
                    v = f((X, Y)) * 0.2
                    if np.linalg.norm(v) < 1e-6: continue
                    arrows.add(Arrow([cx + X, Y - 0.15, 0], [cx + X + v[0], Y - 0.15 + v[1], 0], buff=0, stroke_width=2.5, color=col, max_tip_length_to_length_ratio=0.35, max_stroke_width_to_length_ratio=8))
            self.add(arrows)
            px, py = cx + 0.9, 0.45 - 0.15
            ang = ValueTracker(0.0); trackers.append((ang, w))
            wheel = always_redraw(lambda a=ang, px=px, py=py: VGroup(Circle(radius=0.08, color=RED_H, fill_opacity=1).move_to([px, py, 0]),
                                                                    *[Line([px, py, 0], [px + 0.42 * np.cos(a.get_value() + q * np.pi / 2), py + 0.42 * np.sin(a.get_value() + q * np.pi / 2), 0], color=RED_H, stroke_width=6) for q in range(4)]))
            self.add(wheel); wheels.append((note, col))
        self.wait(1.5)
        say("let the field push on the paddles", GREY_T)
        # spin each wheel at a rate proportional to its curl (half the curl is the angular velocity)
        self.play(*[a.animate.set_value(a.get_value() + (w / 2) * 2 * np.pi * 0.9) for a, w in trackers], run_time=6, rate_func=linear)
        for k, (note, col) in enumerate(wheels):
            say(note, col)
            self.play(*[a.animate.set_value(a.get_value() + (w / 2) * 2 * np.pi * 0.45) for a, w in trackers], run_time=3, rate_func=linear)
        say("curl is local: it compares the push on one side of the wheel with the push on the other", GREEN_H)
        self.play(*[a.animate.set_value(a.get_value() + (w / 2) * 2 * np.pi * 0.6) for a, w in trackers], run_time=4, rate_func=linear)
        self.wait(1.5)
