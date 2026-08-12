"""Lorentz force in motion — the circle, and the velocity selector.

Renders lorentz-orbits.mp4 (embed beside the card).
Smoke: manim -qm lorentz-orbits.py LorentzOrbits
Final: manim -qk lorentz-orbits.py LorentzOrbits
"""
import numpy as np
from manim import *

BLUE_ = "#2563eb"
AMBER = "#f59e0b"
TEAL = "#0891b2"
GREEN = "#059669"
RED_ = "#dc2626"
GRAY = "#9a9a9a"

config.background_color = "#1a1a1a"


def cross_mark(point, scale=0.14, color=BLUE_, opacity=0.5):
    """B-into-page symbol: circle with an X."""
    c = Circle(radius=scale, stroke_color=color, stroke_width=1.6,
               stroke_opacity=opacity).move_to(point)
    d = scale * 0.6
    l1 = Line(point + np.array([-d, -d, 0]), point + np.array([d, d, 0]),
              stroke_color=color, stroke_width=1.6, stroke_opacity=opacity)
    l2 = Line(point + np.array([-d, d, 0]), point + np.array([d, -d, 0]),
              stroke_color=color, stroke_width=1.6, stroke_opacity=opacity)
    return VGroup(c, l1, l2)


class LorentzOrbits(Scene):
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=28, color=color).to_edge(DOWN, buff=0.3)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap), FadeIn(cap), run_time=0.6)
        else:
            self.play(FadeIn(cap), run_time=0.6)
        self._cap = cap

    def clear_cap(self):
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap), run_time=0.4)
            self._cap = None

    def construct(self):
        # ================= ACT 1 — THE CIRCLE =================
        title1 = Text("The sideways force makes circles", font_size=32, color=GRAY).to_edge(UP, buff=0.3)
        self.play(FadeIn(title1), run_time=0.8)

        region = RoundedRectangle(corner_radius=0.2, width=9.4, height=6.2,
                                  stroke_color=BLUE_, stroke_width=2,
                                  fill_color=BLUE_, fill_opacity=0.04).move_to([1.6, -0.2, 0])
        marks = VGroup(*[cross_mark([x, y, 0]) for x in [-2.4, 0.2, 2.8, 5.4]
                         for y in [2.3, -2.7]])
        marks.add(cross_mark([-2.4, -0.2, 0]), cross_mark([5.4, -0.2, 0]))
        lab_b = Text("B into the page", font_size=22, color=BLUE_).move_to([4.5, -2.2, 0])

        self.play(FadeIn(region), FadeIn(marks), FadeIn(lab_b), run_time=1.2)
        self.swap_caption("A positive charge flies into a magnetic field.")

        R = 2.1
        CTR = np.array([-1.5, 0.6, 0])
        entry = CTR + np.array([0, -R, 0])           # (-1.5, -1.5)

        charge = Dot(entry + np.array([-4.5, 0, 0]), radius=0.13, color=AMBER)
        plus = Text("+", font_size=20, color="#1a1a1a", weight=BOLD).move_to(charge.get_center())
        plus.add_updater(lambda m: m.move_to(charge.get_center()))
        self.add(charge, plus)
        self.play(charge.animate.move_to(entry), run_time=1.2, rate_func=linear)

        theta = ValueTracker(-PI / 2)
        charge.add_updater(lambda m: m.move_to(
            CTR + R * np.array([np.cos(theta.get_value()), np.sin(theta.get_value()), 0])))

        v_arrow = always_redraw(lambda: Arrow(
            charge.get_center(),
            charge.get_center() + 1.3 * np.array([-np.sin(theta.get_value()), np.cos(theta.get_value()), 0]),
            buff=0, color=TEAL, stroke_width=5, max_tip_length_to_length_ratio=0.22))
        f_arrow = always_redraw(lambda: Arrow(
            charge.get_center(),
            charge.get_center() - 1.0 * np.array([np.cos(theta.get_value()), np.sin(theta.get_value()), 0]),
            buff=0, color=GREEN, stroke_width=5, max_tip_length_to_length_ratio=0.28))
        lab_v = always_redraw(lambda: Text("v", font_size=24, color=TEAL).next_to(v_arrow.get_end(), UR, buff=0.05))
        lab_f = always_redraw(lambda: Text("F", font_size=24, color=GREEN).next_to(f_arrow.get_end(), LEFT, buff=0.08))

        self.add(v_arrow, f_arrow, lab_v, lab_f)
        self.swap_caption("The force is always perpendicular to the velocity.", GREEN)
        self.play(theta.animate.set_value(-PI / 2 + PI), run_time=3.2, rate_func=linear)

        trace = Circle(radius=R, stroke_color=AMBER, stroke_width=2,
                       stroke_opacity=0.5).move_to(CTR)
        self.add(trace)
        self.swap_caption("No push along the motion: speed never changes. A perfect circle.", AMBER)
        self.play(theta.animate.set_value(-PI / 2 + 2 * PI), run_time=3.2, rate_func=linear)

        radius_line = DashedLine(CTR, entry, color=GRAY, stroke_width=2)
        lab_r = Text("r = mv/qB", font_size=28, color=AMBER).move_to([-3.6, 2.6, 0])
        self.play(Create(radius_line), FadeIn(lab_r), run_time=0.8)
        self.swap_caption("And the lap time is 2 pi m / qB - the speed cancels out.")
        self.play(theta.animate.set_value(-PI / 2 + 3 * PI), run_time=2.6, rate_func=linear)
        self.wait(0.6)

        charge.clear_updaters()
        plus.clear_updaters()
        self.clear_cap()
        self.play(*[FadeOut(m) for m in [title1, region, marks, lab_b, charge, plus,
                                         v_arrow, f_arrow, lab_v, lab_f, trace, radius_line, lab_r]],
                  run_time=0.8)

        # ================= ACT 2 — VELOCITY SELECTOR =================
        title2 = Text("Crossed fields: the velocity selector", font_size=32, color=GRAY).to_edge(UP, buff=0.3)
        self.play(FadeIn(title2), run_time=0.8)

        region2 = Rectangle(width=8.0, height=4.6, stroke_color=BLUE_, stroke_width=2,
                            fill_color=BLUE_, fill_opacity=0.04).move_to([0.3, -0.3, 0])
        e_arrows = VGroup(*[Arrow([x, 1.4, 0], [x, 0.4, 0], buff=0, color=AMBER,
                                  stroke_width=3.5, max_tip_length_to_length_ratio=0.25)
                            for x in [-2.9, -1.3, 0.3, 1.9, 3.5]])
        lab_e = Text("E", font_size=24, color=AMBER).move_to([-3.5, 1.05, 0])
        marks2 = VGroup(*[cross_mark([x, -1.7, 0]) for x in [-2.9, -1.3, 0.3, 1.9, 3.5]])
        lab_b2 = Text("B into the page", font_size=20, color=BLUE_).move_to([2.7, -2.25, 0])

        wall_top = Line([4.3, 1.6, 0], [4.3, 0.4, 0], color=GRAY, stroke_width=7)
        wall_bot = Line([4.3, -1.0, 0], [4.3, -2.2, 0], color=GRAY, stroke_width=7)

        self.play(FadeIn(region2), FadeIn(e_arrows), FadeIn(lab_e),
                  FadeIn(marks2), FadeIn(lab_b2), FadeIn(wall_top), FadeIn(wall_bot), run_time=1.4)
        self.swap_caption("Electric force pushes down. Magnetic force pushes up - and grows with speed.")
        self.wait(1.2)

        y0 = -0.3
        path_fast = VMobject().set_points_smoothly(
            [[-6.4, y0, 0], [-3.7, y0, 0], [-1.5, y0 + 0.35, 0], [0.8, y0 + 1.25, 0], [2.6, y0 + 2.6, 0]])
        path_ok = Line([-6.4, y0, 0], [6.3, y0, 0])
        path_slow = VMobject().set_points_smoothly(
            [[-6.4, y0, 0], [-3.7, y0, 0], [-1.5, y0 - 0.35, 0], [0.8, y0 - 1.25, 0], [2.6, y0 - 2.6, 0]])

        fast = Dot([-6.4, y0, 0], radius=0.11, color=RED_)
        ok = Dot([-6.4, y0, 0], radius=0.11, color=GREEN)
        slow = Dot([-6.4, y0, 0], radius=0.11, color=AMBER)

        self.add(fast, ok, slow)
        self.swap_caption("Three speeds enter. Only one balance is possible.", GRAY)
        self.play(
            MoveAlongPath(fast, path_fast, rate_func=linear, run_time=2.6),
            MoveAlongPath(slow, path_slow, rate_func=rate_functions.ease_in_sine, run_time=3.4),
            MoveAlongPath(ok, path_ok, rate_func=linear, run_time=4.0),
        )
        lab_fast = Text("too fast: magnetic wins", font_size=22, color=RED_).move_to([4.2, 2.6, 0])
        lab_slow = Text("too slow: electric wins", font_size=22, color=AMBER).move_to([4.4, -2.85, 0])
        lab_ok = Text("v = E/B sails through", font_size=24, color=GREEN).move_to([4.7, 0.25, 0])
        self.play(FadeIn(lab_fast), FadeIn(lab_slow), FadeIn(lab_ok), run_time=0.9)
        self.swap_caption("qE = qvB at exactly one speed: v = E/B. The slit passes a single velocity.", GREEN)
        self.wait(2.4)

        self.clear_cap()
        self.play(*[FadeOut(m) for m in [title2, region2, e_arrows, lab_e, marks2, lab_b2,
                                         wall_top, wall_bot, fast, ok, slow,
                                         lab_fast, lab_slow, lab_ok]], run_time=0.8)

        # ================= CLOSING =================
        formula = Text("F = qE + qv x B", font_size=44, color=GRAY, weight=BOLD).move_to([0, 0.4, 0])
        self.play(FadeIn(formula), run_time=0.9)
        self.swap_caption("All steering, no pushing - nature's perfect sideways force.")
        self.wait(2.6)
