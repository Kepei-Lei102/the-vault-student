"""Manim: the tail that shrinks — Student's t collapsing onto the normal.

One scene, ~28 s. The standard normal is drawn as a fixed grey ghost. The
t-density starts at nu = 1 (fat, low-peaked) and morphs continuously as nu
climbs 1 -> 30, with a live counter, while the upper 2.5% critical value
slides from 12.7 (off the frame) in toward 1.96 and its readout ticks. Ends
on nu = 30 with the two curves nearly coincident and the moral on screen.

Render (4K):  manim -qk t-tail-shrinks.py TTailShrinks
Then copy media/videos/t-tail-shrinks/2160p60/TTailShrinks.mp4
  -> t-tail-shrinks.mp4  beside the card, and delete media/ + __pycache__.
"""

import numpy as np
from scipy import stats
from manim import (
    Scene, VGroup, Axes, Text, MathTex, DecimalNumber, ValueTracker, Line, Dot,
    always_redraw, FadeIn, FadeOut, Create, Write, UP, DOWN, LEFT, RIGHT,
)

BG = "#1e1e1e"
TXT = "#cccccc"
GREY = "#9ca3af"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
GREEN = "#059669"
REDC = "#dc2626"
AMBER = "#f59e0b"
FONT = "Helvetica Neue"


class TTailShrinks(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Student's t: the tail that shrinks as the sample grows",
                     font=FONT, font_size=34, color=TXT).to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1.3)

        ax = Axes(x_range=[-5, 5, 1], y_range=[0, 0.44, 0.1],
                  x_length=10.4, y_length=4.2,
                  axis_config={"color": GREY, "stroke_width": 2,
                               "include_ticks": True, "tick_size": 0.05},
                  y_axis_config={"include_ticks": False, "include_tip": False},
                  ).shift(DOWN * 0.55)
        xl = MathTex(r"t", color=TXT).scale(0.7).next_to(ax.x_axis.get_end(), RIGHT, buff=0.15)

        normal = ax.plot(lambda x: stats.norm.pdf(x), x_range=[-5, 5], color=GREY, stroke_width=4)
        nlab = MathTex(r"N(0,1)", color=GREY).scale(0.7).next_to(ax.c2p(0.55, 0.36), RIGHT, buff=0.15)

        self.play(Create(ax), FadeIn(xl), run_time=1.0)
        self.play(Create(normal), FadeIn(nlab), run_time=1.2)

        nu = ValueTracker(1.0)
        tcurve = always_redraw(lambda: ax.plot(
            lambda x: stats.t.pdf(x, nu.get_value()), x_range=[-5, 5],
            color=PURPLE, stroke_width=5))

        def crit_x():
            return float(stats.t.ppf(0.975, nu.get_value()))

        def cut():
            xc = min(crit_x(), 4.9)
            return Line(ax.c2p(xc, 0), ax.c2p(xc, 0.30), color=AMBER, stroke_width=4)
        cutline = always_redraw(cut)
        cutdot = always_redraw(lambda: Dot(ax.c2p(min(crit_x(), 4.9), 0), color=AMBER, radius=0.07))
        cut196 = Line(ax.c2p(1.96, 0), ax.c2p(1.96, 0.30), color=GREY, stroke_width=2.5,
                      stroke_opacity=0.7)
        lab196 = MathTex(r"1.96", color=GREY).scale(0.65).next_to(ax.c2p(1.96, 0.30), UP, buff=0.1)

        # readouts (top-right block)
        nu_label = Text("degrees of freedom  ν =", font=FONT, font_size=26, color=TXT)
        nu_num = DecimalNumber(1, num_decimal_places=0, color=BLUE, font_size=40)
        nu_num.add_updater(lambda m: m.set_value(round(nu.get_value())))
        row1 = VGroup(nu_label, nu_num).arrange(RIGHT, buff=0.25)

        cv_label = Text("upper 2.5% point  t =", font=FONT, font_size=26, color=TXT)
        cv_num = DecimalNumber(12.71, num_decimal_places=2, color=AMBER, font_size=40)
        cv_num.add_updater(lambda m: m.set_value(crit_x()))
        row2 = VGroup(cv_label, cv_num).arrange(RIGHT, buff=0.25)

        block = VGroup(row1, row2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        block.to_corner(UP + RIGHT, buff=0.5).shift(DOWN * 0.95)

        tlab = MathTex(r"t_{\nu}", color=PURPLE).scale(0.8).move_to(ax.c2p(-3.4, 0.30))

        self.play(FadeIn(tcurve), FadeIn(tlab), FadeIn(block), run_time=1.0)
        self.add(cutline, cutdot)
        self.wait(0.6)

        note1 = Text("ν = 1: the 2.5% point sits at 12.7 — off the frame", font=FONT,
                     font_size=24, color=AMBER).next_to(ax, DOWN, buff=0.35)
        self.play(FadeIn(note1), run_time=0.6)
        self.wait(1.4)
        self.play(FadeOut(note1), FadeIn(cut196), FadeIn(lab196), run_time=0.6)

        # the climb — slow at first (where it changes fastest), then coasting
        self.play(nu.animate.set_value(5), run_time=6.0, rate_func=lambda x: x)
        note2 = Text("ν = 5: the tail is already close — the surcharge on 1.96 is 40%",
                     font=FONT, font_size=24, color=TXT).next_to(ax, DOWN, buff=0.35)
        self.play(FadeIn(note2), run_time=0.5)
        self.wait(1.2)
        self.play(FadeOut(note2), run_time=0.4)
        self.play(nu.animate.set_value(30), run_time=7.0, rate_func=lambda x: x)

        final = Text("by ν = 30 the two curves are the same to the eye —\nthe normal is the t you get "
                     "when you have enough data to stop worrying about s",
                     font=FONT, font_size=23, color=TXT, line_spacing=0.9).next_to(ax, DOWN, buff=0.3)
        self.play(FadeIn(final), run_time=0.8)
        self.wait(2.6)
