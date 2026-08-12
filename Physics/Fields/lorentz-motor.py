"""The d.c. motor — the couple, the dead point, and the commutator's flip.

Renders lorentz-motor.mp4 (embed beside the card).
Smoke: manim -qm lorentz-motor.py DCMotor
Final: manim -qk lorentz-motor.py DCMotor
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

CENTER_M = np.array([0.0, -0.2, 0.0])
R = 2.2


class DCMotor(Scene):
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=28, color=color).to_edge(DOWN, buff=0.3)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap), FadeIn(cap), run_time=0.6)
        else:
            self.play(FadeIn(cap), run_time=0.6)
        self._cap = cap

    def construct(self):
        title = Text("The d.c. motor: a couple with a trick", font_size=32, color=GRAY).to_edge(UP, buff=0.3)

        # ---- the field ----
        n_pole = Rectangle(width=0.8, height=4.6, stroke_color=AMBER, stroke_width=2.5,
                           fill_color=AMBER, fill_opacity=0.15).move_to([-5.6, -0.2, 0])
        s_pole = Rectangle(width=0.8, height=4.6, stroke_color=TEAL, stroke_width=2.5,
                           fill_color=TEAL, fill_opacity=0.15).move_to([5.6, -0.2, 0])
        lab_n = Text("N", font_size=34, color=AMBER, weight=BOLD).move_to(n_pole.get_center())
        lab_s = Text("S", font_size=34, color=TEAL, weight=BOLD).move_to(s_pole.get_center())
        field = VGroup(*[Arrow([-5.1, y, 0], [5.1, y, 0], buff=0, color=BLUE_,
                               stroke_width=2.2, max_tip_length_to_length_ratio=0.02,
                               stroke_opacity=0.35)
                         for y in [1.6, 0.4, -0.8, -2.0]])
        lab_b = Text("B", font_size=26, color=BLUE_).move_to([-4.6, 2.0, 0])

        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(n_pole), FadeIn(s_pole), FadeIn(lab_n), FadeIn(lab_s),
                  FadeIn(field), FadeIn(lab_b), run_time=1.2)

        # ---- the coil, seen along its axle ----
        phi = ValueTracker(0.0)

        def wire_pos(sign):
            a = phi.get_value()
            return CENTER_M + sign * R * np.array([np.cos(a), np.sin(a), 0.0])

        def make_wire(sign):
            p = wire_pos(sign)
            out_of_page = np.cos(phi.get_value()) * sign >= 0  # right half carries "out"
            ring = Circle(radius=0.17, stroke_color=AMBER, stroke_width=3).move_to(p)
            if out_of_page:
                mark = Dot(p, radius=0.055, color=AMBER)
            else:
                d = 0.10
                mark = VGroup(
                    Line(p + np.array([-d, -d, 0]), p + np.array([d, d, 0]),
                         stroke_color=AMBER, stroke_width=3),
                    Line(p + np.array([-d, d, 0]), p + np.array([d, -d, 0]),
                         stroke_color=AMBER, stroke_width=3))
            return VGroup(ring, mark)

        def make_force(sign):
            p = wire_pos(sign)
            up = np.cos(phi.get_value()) * sign >= 0
            direction = np.array([0, 1.25, 0]) if up else np.array([0, -1.25, 0])
            start = p + (direction / np.linalg.norm(direction)) * 0.3
            return Arrow(start, p + direction, buff=0, color=GREEN, stroke_width=6,
                         max_tip_length_to_length_ratio=0.25)

        rod = always_redraw(lambda: Line(wire_pos(1), wire_pos(-1),
                                         stroke_color=GRAY, stroke_width=3.5))
        wire_a = always_redraw(lambda: make_wire(1))
        wire_b = always_redraw(lambda: make_wire(-1))
        force_a = always_redraw(lambda: make_force(1))
        force_b = always_redraw(lambda: make_force(-1))
        pivot = Dot(CENTER_M, radius=0.09, color=GRAY)

        # commutator: split ring turning with the coil + fixed brushes
        def make_ring():
            a = phi.get_value()
            return VGroup(
                Arc(radius=0.42, start_angle=a + 0.18, angle=PI - 0.36,
                    stroke_color=AMBER, stroke_width=5).move_arc_center_to(CENTER_M),
                Arc(radius=0.42, start_angle=a + PI + 0.18, angle=PI - 0.36,
                    stroke_color=TEAL, stroke_width=5).move_arc_center_to(CENTER_M))
        comm = always_redraw(make_ring)
        brush_l = Rectangle(width=0.16, height=0.3, stroke_width=0, fill_color=GRAY,
                            fill_opacity=0.9).move_to(CENTER_M + np.array([-0.68, 0, 0]))
        brush_r = brush_l.copy().move_to(CENTER_M + np.array([0.68, 0, 0]))

        self.play(FadeIn(rod), FadeIn(wire_a), FadeIn(wire_b), FadeIn(pivot),
                  FadeIn(comm), FadeIn(brush_l), FadeIn(brush_r), run_time=1.0)
        self.play(FadeIn(force_a), FadeIn(force_b), run_time=0.6)
        self.swap_caption("Current out on one side, in on the other: opposite forces - a couple.")
        self.wait(1.6)

        self.swap_caption("The couple turns the coil toward the vertical...", GREEN)
        self.play(phi.animate.set_value(80 * DEGREES), run_time=3.0, rate_func=rate_functions.ease_in_sine)

        self.swap_caption("...the dead point - where the split-ring commutator flips the current.", AMBER)
        self.play(phi.animate.set_value(90 * DEGREES), run_time=0.7, rate_func=linear)
        self.play(Flash(pivot, color=AMBER, flash_radius=0.9, line_length=0.35), run_time=0.6)
        self.play(phi.animate.set_value(120 * DEGREES), run_time=0.9, rate_func=linear)

        self.swap_caption("Flipped current, same push: the torque never changes sign.", GREEN)
        self.play(phi.animate.set_value(360 * DEGREES), run_time=3.6, rate_func=linear)

        self.swap_caption("And so it spins. Every fan, drill and wiper is this loop.")
        self.play(phi.animate.set_value(2 * 360 * DEGREES), run_time=3.0, rate_func=rate_functions.ease_in_out_sine)
        self.wait(1.6)
