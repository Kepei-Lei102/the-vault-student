"""Manim scene for [[Partial Derivatives and the Gradient]].

Compass — on the contour map of the hill h = 400 - 0.001x^2 - 0.002y^2, a walking direction u turns through
          a full circle at P(100, 50).  A bar shows the slope felt in that direction, D_u h = grad h . u.
          The bar peaks when u lines up with the fixed gradient arrow, is zero along the contour, and goes
          negative beyond it.
Smoke:  manim -ql --fps 15 partial-derivatives-manim.py Compass
Final:  manim -qk partial-derivatives-manim.py Compass     ->  partial-derivatives-compass.mp4
"""
import numpy as np
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H, TEAL_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
GX, GY = -0.2, -0.2
MAG = float(np.hypot(GX, GY))


class Compass(Scene):
    def construct(self):
        title = Text("One arrow on the map gives the slope in every direction", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        # map: 1 scene unit = 50 m; summit placed left of centre
        O = np.array([-3.3, -0.35, 0]); k = 1 / 50
        to_scene = lambda x, y: O + np.array([x * k, y * k, 0])
        contours = VGroup()
        for level in (395, 390, 385, 380, 375, 370):
            a, b = np.sqrt((400 - level) / 0.001) * k, np.sqrt((400 - level) / 0.002) * k
            own = level == 385                                   # the contour through P, drawn in teal
            contours.add(Ellipse(width=2 * a, height=2 * b, color=TEAL_H if own else GREY_T, stroke_width=3 if own else 1.5).move_to(O))
        summit = Triangle(color=GREEN_H, fill_opacity=1).scale(0.09).move_to(O)
        summit_l = Text("summit", font_size=18, color=GREEN_H).next_to(summit, DOWN, buff=0.1)
        P = to_scene(100, 50)
        dotP = Dot(P, color=AMBER_H, radius=0.09); P_l = Text("P", font_size=22, color=AMBER_H).next_to(dotP, UR, buff=0.06)
        self.add(contours, summit, summit_l, dotP, P_l)

        grad = Arrow(P, P + 1.25 * np.array([GX, GY, 0]) / MAG, buff=0, color=RED_H, stroke_width=6, max_tip_length_to_length_ratio=0.2)
        grad_l = Text("gradient", font_size=20, color=RED_H).next_to(grad.get_center(), DR, buff=0.12)

        th = ValueTracker(0.0)
        udir = lambda: np.array([np.cos(th.get_value()), np.sin(th.get_value()), 0])
        walker = always_redraw(lambda: Arrow(P, P + 1.25 * udir(), buff=0, color=BLUE_H, stroke_width=6, max_tip_length_to_length_ratio=0.2))
        slope = lambda: GX * np.cos(th.get_value()) + GY * np.sin(th.get_value())

        # the meter on the right
        base = np.array([4.1, -0.35, 0]); H = 2.3
        axis = Line(base + DOWN * H, base + UP * H, color=GREY_T, stroke_width=2)
        zero = Line(base + LEFT * 0.75, base + RIGHT * 0.75, color=GREY_T, stroke_width=2)
        ticks = VGroup(*[Line(base + UP * H * s + LEFT * 0.12, base + UP * H * s + RIGHT * 0.12, color=GREY_T, stroke_width=2) for s in (-1, 1)])
        lab = VGroup(Text("+0.283", font_size=18, color=GREY_T).next_to(base + UP * H, RIGHT, buff=0.25),
                     Text("-0.283", font_size=18, color=GREY_T).next_to(base + DOWN * H, RIGHT, buff=0.25),
                     Text("0", font_size=18, color=GREY_T).next_to(base + RIGHT * 0.75, RIGHT, buff=0.12),
                     Text("slope felt", font_size=20, color=BLUE_H).next_to(base + UP * H, UP, buff=0.3))

        def bar():
            s = slope() / MAG
            hgt = max(abs(s) * H, 0.02)
            col = GREEN_H if s >= 0 else PURPLE_H
            r = Rectangle(width=0.7, height=hgt, color=col, fill_opacity=0.6, stroke_width=0)
            return r.move_to(base + UP * (hgt / 2) * (1 if s >= 0 else -1))
        meter = always_redraw(bar)
        self.add(axis, zero, ticks, lab, meter, walker)

        cap = Text("blue: the way you walk.  Teal: the contour through P.  Due east, the slope is -0.2", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(cap); self.wait(2)

        def say(text, colour=GREY_T):
            nonlocal cap
            self.remove(cap); cap = Text(text, font_size=22, color=colour).to_edge(DOWN, buff=0.3); self.add(cap)

        def turn_to(deg, t=2.5, hold=1.6):
            self.play(th.animate.set_value(np.radians(deg)), run_time=t, rate_func=smooth); self.wait(hold)

        say("turn to due north: the slope is -0.2 again"); turn_to(90)
        say("those two readings are the partial derivatives; draw them as one red arrow", RED_H)
        self.play(GrowArrow(grad), FadeIn(grad_l), run_time=1.2); self.wait(2)
        say("keep turning.  Along the contour the ground is level: slope 0", GREEN_H); turn_to(135, t=2)
        say("lined up with the gradient: the steepest climb, +0.283", RED_H); turn_to(225, t=3, hold=2.2)
        say("along the contour again: 0", GREEN_H); turn_to(315, t=3)
        say("directly against the gradient: the steepest way down, -0.283", PURPLE_H); turn_to(405, t=3, hold=2.2)
        say("the reading is always the gradient's length times cos(angle between the arrows)"); turn_to(720 + 45, t=9, hold=0.5)
        say("so two numbers, measured east and north, know every direction"); self.wait(3)
