"""Motion under a variable force — companion clip for [[Linear Motion under a Variable Force]].

Chapter 1 — Drive against drag (J26/31 numbers: 6.4 kg, 8 N drive, 0.5v² resistance,
from rest): the resistive arrow grows with v² until it matches the drive; speed and
distance readouts; the terminal speed line.

Chapter 2 — Falling through air (N24/32: g = 10, 0.1v² per kg): the same story
vertically, with the exact v = 10 tanh t and the no-drag ghost for comparison.

Render:  manim -qk variable-force-see-it-move.py VariableForceSeeItMove
"""
import numpy as np
from manim import *

GREY_TXT = "#888888"; BLUE_ = "#2563eb"; RED_ = "#dc2626"; GREEN_ = "#059669"; AMBER_ = "#f59e0b"; PURPLE_ = "#7c3aed"


class VariableForceSeeItMove(Scene):
    def construct(self):
        self.chapter_drive()
        self.chapter_fall()

    def chapter_drive(self):
        title = Text("Drive against drag", font_size=40, color=WHITE)
        sub = Text("6.4 kg, 8 N drive, resistance 0.5 v squared, from rest", font_size=24, color=GREY_TXT).next_to(title, DOWN)
        self.play(FadeIn(title), FadeIn(sub)); self.wait(1.2); self.play(FadeOut(title), FadeOut(sub))

        m, F, kq = 6.4, 8.0, 0.5
        T_END = 8.0
        # exact: v = 4 tanh(t/1.6); x = 6.4 ln cosh(t/1.6)
        v_of = lambda t: 4*np.tanh(t/1.6)
        x_of = lambda t: 6.4*np.log(np.cosh(t/1.6))

        track = Line(LEFT*6.5, RIGHT*6.5, color=GREY_TXT, stroke_width=3).shift(DOWN*1.2)
        tt = ValueTracker(0.0)
        # the cart moves in a scrolling frame: keep the cart fixed-ish, scroll ticks? simpler: map x to screen with scale
        SC = 0.36  # screen units per metre (x reaches ~ 27 m at t=8 → 11 units; scroll instead)
        def cart_x(): return -5.0 + SC*min(x_of(tt.get_value()), 27.0)
        cart = always_redraw(lambda: Square(side_length=0.6, color=AMBER_, fill_color=AMBER_, fill_opacity=0.9).move_to(RIGHT*cart_x() + DOWN*0.9))
        drive = always_redraw(lambda: Arrow(RIGHT*cart_x() + DOWN*0.9, RIGHT*(cart_x() + 0.25*F) + DOWN*0.9, buff=0.3, color=GREEN_, stroke_width=6, max_tip_length_to_length_ratio=0.2).shift(UP*0.55))
        def drag_arrow():
            v = v_of(tt.get_value()); R = kq*v*v
            end = RIGHT*(cart_x() - 0.25*R) + DOWN*0.9
            return Arrow(RIGHT*cart_x() + DOWN*0.9, end, buff=0.3, color=RED_, stroke_width=6, max_tip_length_to_length_ratio=0.2).shift(DOWN*0.55)
        drag = always_redraw(drag_arrow)
        lab_d = always_redraw(lambda: Text("8 N", font_size=22, color=GREEN_).next_to(drive, UP, buff=0.1))
        lab_r = always_redraw(lambda: Text(f"0.5v² = {kq*v_of(tt.get_value())**2:.1f} N", font_size=22, color=RED_).next_to(drag, DOWN, buff=0.1))
        read = always_redraw(lambda: VGroup(
            Text(f"t = {tt.get_value():.1f} s", font_size=28, color=GREY_TXT),
            Text(f"v = {v_of(tt.get_value()):.2f} m/s", font_size=28, color=BLUE_),
            Text(f"x = {x_of(tt.get_value()):.1f} m", font_size=28, color=GREY_TXT),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR, buff=0.6))
        # speed bar with terminal line
        bar_base = np.array([-5.5, 2.4, 0]); 
        bar = always_redraw(lambda: Rectangle(width=v_of(tt.get_value())*1.5+1e-3, height=0.35, fill_color=BLUE_, fill_opacity=0.85, stroke_width=0).move_to(bar_base + RIGHT*(v_of(tt.get_value())*0.75)))
        term = Line(bar_base + RIGHT*6 + UP*0.35, bar_base + RIGHT*6 + DOWN*0.35, color=RED_, stroke_width=3)
        term_lab = Text("terminal 4 m/s: drag = drive", font_size=22, color=GREY_TXT).next_to(term, RIGHT, buff=0.15)
        bar_lab = Text("speed", font_size=22, color=GREY_TXT).next_to(bar_base, LEFT, buff=0.2)

        self.play(Create(track), FadeIn(bar_lab), Create(term), FadeIn(term_lab))
        self.add(cart, drive, drag, lab_d, lab_r, read, bar)
        self.wait(0.6)
        self.play(tt.animate.set_value(T_END), run_time=12, rate_func=linear)
        note = Text("the drag arrow grows with v², the drive does not — so the gap closes and the speed stops changing",
                    font_size=24, color=GREY_TXT).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note)); self.wait(2.2)
        self.play(*[FadeOut(mo) for mo in self.mobjects])

    def chapter_fall(self):
        title = Text("Falling through air", font_size=40, color=WHITE)
        sub = Text("g = 10, resistance 0.1 v squared per kilogram — the exact solution is a tanh", font_size=24, color=GREY_TXT).next_to(title, DOWN)
        self.play(FadeIn(title), FadeIn(sub)); self.wait(1.2); self.play(FadeOut(title), FadeOut(sub))

        v_of = lambda t: 10*np.tanh(t); y_of = lambda t: 10*np.log(np.cosh(t))   # depth fallen
        v_free = lambda t: 10*t; y_free = lambda t: 5*t*t
        T_END = 3.2
        tt = ValueTracker(0.0)
        top = np.array([-2.5, 3.2, 0]); SC = 0.19
        def pos(y): return top + DOWN*SC*y
        ball = always_redraw(lambda: Dot(pos(y_of(tt.get_value())), radius=0.17, color=AMBER_))
        ghost = always_redraw(lambda: Dot(pos(min(y_free(tt.get_value()), 34)), radius=0.12, color=GREY_TXT, fill_opacity=0.5).shift(RIGHT*1.4))
        ghost_lab = Text("no drag", font_size=20, color=GREY_TXT).move_to(top + RIGHT*1.4 + UP*0.35)
        ball_lab = Text("with v² drag", font_size=20, color=AMBER_).move_to(top + UP*0.35)
        wt = always_redraw(lambda: Arrow(pos(y_of(tt.get_value())), pos(y_of(tt.get_value())) + DOWN*1.2, buff=0.2, color=GREEN_, stroke_width=6, max_tip_length_to_length_ratio=0.2))
        dr = always_redraw(lambda: Arrow(pos(y_of(tt.get_value())), pos(y_of(tt.get_value())) + UP*(0.012*v_of(tt.get_value())**2), buff=0.2, color=RED_, stroke_width=6, max_tip_length_to_length_ratio=0.2))
        read = always_redraw(lambda: VGroup(
            Text(f"t = {tt.get_value():.1f} s", font_size=28, color=GREY_TXT),
            Text(f"v = {v_of(tt.get_value()):.2f} m/s", font_size=28, color=BLUE_),
            Text(f"v = 10 tanh t", font_size=24, color=GREY_TXT),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR, buff=0.6))
        # v-t graph on the right
        ax = Axes(x_range=[0, 3.2, 1], y_range=[0, 12, 5], x_length=4.2, y_length=2.6, axis_config={"color": GREY_TXT, "include_tip": False}).move_to(RIGHT*3.6 + DOWN*1.3)
        curve = always_redraw(lambda: ax.plot(lambda s: 10*np.tanh(s), x_range=[0, max(tt.get_value(), 1e-3)], color=BLUE_))
        tline = DashedLine(ax.c2p(0, 10), ax.c2p(3.2, 10), color=RED_)
        tlab = Text("terminal 10 m/s", font_size=20, color=GREY_TXT).next_to(tline, UP, buff=0.05)
        self.play(FadeIn(ball_lab), FadeIn(ghost_lab), Create(ax), Create(tline), FadeIn(tlab))
        self.add(ball, ghost, wt, dr, read, curve)
        self.wait(0.5)
        self.play(tt.animate.set_value(T_END), run_time=9, rate_func=linear)
        note = Text("weight fixed, drag grows with v²: the curve bends over — a tanh, never quite reaching 10", font_size=24, color=GREY_TXT).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note)); self.wait(2.2)
        self.play(*[FadeOut(mo) for mo in self.mobjects]); self.wait(0.3)
