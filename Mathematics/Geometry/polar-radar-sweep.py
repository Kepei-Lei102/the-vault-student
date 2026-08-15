"""Manim: the radar sweep — a polar curve is a graph of r(θ), read while turning.

Two beats:
  1. r = 3 + 2 sin θ   — the arm sweeps once; the side graph is read live; the
     limaçon appears as the *wrapped* reading. r never hits 0, so the curve
     never visits the pole.
  2. r = sin 3θ        — the reading hits zero; wherever the graph dips below
     the axis there is NO curve (Cambridge's r ≥ 0), and each petal enters and
     leaves the pole exactly at the zeros. Three arches → three petals.

Render (4K):  manim -qk polar-radar-sweep.py PolarRadarSweep
Then copy media/videos/polar-radar-sweep/2160p60/PolarRadarSweep.mp4
  -> polar-radar-sweep.mp4  beside the card, and delete media/ + __pycache__.
"""

import numpy as np
from manim import (
    Scene, VGroup, Axes, Dot, Line, Text, MathTex, TracedPath, ValueTracker,
    Circle, DashedVMobject, always_redraw, FadeIn, FadeOut, Create, Write,
    UP, DOWN, LEFT, RIGHT, ORIGIN, PI, RED, interpolate_color, rgb_to_color,
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


def polar_grid(center, unit, radii, labels=True):
    g = VGroup()
    for R in radii:
        g.add(Circle(radius=R * unit, color=GREY, stroke_opacity=0.25,
                     stroke_width=1.5).move_to(center))
    for a in np.arange(0, 2 * np.pi, np.pi / 4):
        g.add(Line(center, center + unit * radii[-1] * np.array([np.cos(a), np.sin(a), 0]),
                   color=GREY, stroke_opacity=0.16, stroke_width=1.5))
    init = Line(center, center + unit * radii[-1] * 1.12 * RIGHT,
                color=GREY, stroke_opacity=0.7, stroke_width=2.5)
    g.add(init)
    if labels:
        lab = Text("initial line", font=FONT, font_size=20, color=GREY)
        lab.next_to(init.get_end(), DOWN, buff=0.15)
        g.add(lab)
    return g


class PolarRadarSweep(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ------------------------------------------------ beat 1: limaçon
        title = Text("A polar curve is a graph of r(θ) — read while turning",
                     font=FONT, font_size=34, color=TXT).to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1.4)

        C = LEFT * 3.6 + DOWN * 0.7
        U = 0.42                                     # units per r
        grid = polar_grid(C, U, [1, 3, 5])
        rlabs = VGroup(*[Text(str(R), font=FONT, font_size=18, color=GREY)
                         .move_to(C + U * R * np.array([np.cos(1.25), np.sin(1.25), 0]))
                         for R in [1, 3, 5]])

        ax = Axes(x_range=[-PI, PI, PI / 2], y_range=[0, 5.6, 1],
                  x_length=5.3, y_length=3.4,
                  axis_config={"color": GREY, "stroke_width": 2,
                               "include_ticks": True, "tick_size": 0.05},
                  ).shift(RIGHT * 3.3 + DOWN * 0.8)
        xl = MathTex(r"\theta", color=TXT).scale(0.7).next_to(ax.x_axis.get_end(), RIGHT, buff=0.15)
        yl = MathTex(r"r", color=TXT).scale(0.7).next_to(ax.y_axis.get_end(), LEFT, buff=0.18)
        eq = MathTex(r"r = 3 + 2\sin\theta", color=BLUE).scale(0.85)
        eq.next_to(ax, UP, buff=0.45)

        f = lambda t: 3 + 2 * np.sin(t)
        graph = ax.plot(f, x_range=[-PI, PI], color=BLUE, stroke_width=4)

        self.play(FadeIn(grid), FadeIn(rlabs), Create(ax), FadeIn(xl), FadeIn(yl), run_time=1.2)
        self.play(Create(graph), Write(eq), run_time=1.6)
        self.wait(0.4)

        t = ValueTracker(-PI)
        arm = always_redraw(lambda: Line(
            C, C + U * f(t.get_value()) * np.array([np.cos(t.get_value()), np.sin(t.get_value()), 0]),
            color=AMBER, stroke_width=5))
        tip = always_redraw(lambda: Dot(
            C + U * f(t.get_value()) * np.array([np.cos(t.get_value()), np.sin(t.get_value()), 0]),
            color=PURPLE, radius=0.06))
        reader = always_redraw(lambda: Dot(
            ax.c2p(t.get_value(), f(t.get_value())), color=AMBER, radius=0.07))
        drop = always_redraw(lambda: Line(
            ax.c2p(t.get_value(), 0), ax.c2p(t.get_value(), f(t.get_value())),
            color=AMBER, stroke_width=2, stroke_opacity=0.5))
        trace = TracedPath(tip.get_center, stroke_color=PURPLE, stroke_width=5)

        self.add(arm, tip, reader, drop, trace)
        self.play(t.animate.set_value(PI), run_time=9, rate_func=lambda x: x)
        self.wait(0.3)

        note = Text("r is never zero — the curve never visits the pole",
                    font=FONT, font_size=24, color=GREEN)
        note.next_to(ax, DOWN, buff=0.45)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(1.6)

        self.play(*[FadeOut(m) for m in
                    [grid, rlabs, ax, xl, yl, eq, graph, arm, tip, reader, drop, trace, note]],
                  run_time=0.9)

        # ------------------------------------------------ beat 2: the rose and r >= 0
        t2title = Text("Where the graph goes negative, there is no curve at all",
                       font=FONT, font_size=32, color=TXT).to_edge(UP, buff=0.4)
        self.play(FadeOut(title), FadeIn(t2title), run_time=0.9)

        C2 = LEFT * 3.6 + DOWN * 0.55
        U2 = 1.75
        grid2 = polar_grid(C2, U2, [1], labels=False)
        ax2 = Axes(x_range=[0, 2 * PI, PI / 3], y_range=[-1.2, 1.4, 1],
                   x_length=5.6, y_length=3.4,
                   axis_config={"color": GREY, "stroke_width": 2,
                                "include_ticks": True, "tick_size": 0.05},
                   ).shift(RIGHT * 3.3 + DOWN * 0.7)
        eq2 = MathTex(r"r = \sin 3\theta", color=BLUE).scale(0.85).next_to(ax2, UP, buff=0.25)
        g = lambda th: np.sin(3 * th)
        graph2 = ax2.plot(g, x_range=[0, 2 * PI], color=BLUE, stroke_width=4)

        # shade the three negative arches
        shades = VGroup(*[
            ax2.get_area(graph2, x_range=[(2 * k + 1) * PI / 3, (2 * k + 2) * PI / 3],
                         color=REDC, opacity=0.16)
            for k in range(3)])

        self.play(FadeIn(grid2), Create(ax2), Create(graph2), Write(eq2), run_time=1.5)
        self.play(FadeIn(shades), run_time=0.8)
        nolab = Text("r < 0 — no curve", font=FONT, font_size=22, color=REDC)
        nolab.next_to(ax2, DOWN, buff=0.4)
        self.play(FadeIn(nolab), run_time=0.6)
        self.wait(0.5)

        t2 = ValueTracker(0.0)

        def arm2():
            v = t2.get_value(); r = g(v)
            if r <= 1e-3:
                return Dot(C2, color=AMBER, radius=0.05)
            return Line(C2, C2 + U2 * r * np.array([np.cos(v), np.sin(v), 0]),
                        color=AMBER, stroke_width=5)
        armM = always_redraw(arm2)
        reader2 = always_redraw(lambda: Dot(
            ax2.c2p(t2.get_value(), g(t2.get_value())), color=AMBER, radius=0.07))
        self.add(armM, reader2)

        petal_count = VGroup()
        for k in range(3):
            a, b = 2 * k * PI / 3, (2 * k + 1) * PI / 3
            tipf = (lambda: C2 + U2 * max(g(t2.get_value()), 0.0)
                    * np.array([np.cos(t2.get_value()), np.sin(t2.get_value()), 0]))
            tr = TracedPath(tipf, stroke_color=GREEN, stroke_width=5)
            self.add(tr)
            t2.set_value(a)
            self.play(t2.animate.set_value(b), run_time=2.6, rate_func=lambda x: x)
            self.remove(tr)
            self.add(tr.copy().clear_updaters())
            num = Text(str(k + 1), font=FONT, font_size=26, color=GREEN)
            mid = a + PI / 6
            num.move_to(C2 + U2 * 1.22 * np.array([np.cos(mid), np.sin(mid), 0]))
            petal_count.add(num)
            self.play(FadeIn(num), run_time=0.3)
            if k < 2:
                # sweep the dead zone: arm collapsed at the pole
                self.play(t2.animate.set_value(b + PI / 3), run_time=1.6,
                          rate_func=lambda x: x)

        final = Text("three arches at or above zero — three petals, read not memorised",
                     font=FONT, font_size=25, color=TXT).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(final), run_time=0.8)
        self.wait(2.2)
