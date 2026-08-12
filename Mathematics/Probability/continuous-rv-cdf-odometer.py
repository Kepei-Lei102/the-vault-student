"""The cdf as odometer: sweep the pdf, watch the accumulated area climb to 1.

The triangle pdf from the card's Example 3 (f = x/4 on [0,2], (4-x)/4 on
[2,4]). A scan line sweeps left to right; the area collected so far pours
into the cdf panel, which climbs steepest exactly where the density peaks
and ends at 1.

Render (from this folder):
    manim -qm continuous-rv-cdf-odometer.py CdfOdometer   # smoke
    manim -qk continuous-rv-cdf-odometer.py CdfOdometer   # 4K final
Copy the output beside the card as continuous-rv-cdf-odometer.mp4, then
clear media/ + __pycache__/.
"""

from manim import *

BG = "#1a1a1a"
GRAY = "#9a9a9a"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
GREEN = "#059669"
AMBER = "#f59e0b"

config.background_color = BG


def pdf(x):
    return x / 4 if x <= 2 else (4 - x) / 4


def cdf(x):
    return x * x / 8 if x <= 2 else 1 - (4 - x) ** 2 / 8


class CdfOdometer(Scene):
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=26, color=color).to_edge(DOWN, buff=0.35)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.2), FadeIn(cap, run_time=0.3))
        else:
            self.play(FadeIn(cap, run_time=0.3))
        self._cap = cap

    def construct(self):
        axis_kw = dict(color=GRAY, include_ticks=True, include_numbers=True,
                       font_size=22, decimal_number_config={"num_decimal_places": 0,
                                                            "color": GRAY})
        ax1 = Axes(x_range=[0, 4.4, 1], y_range=[0, 0.62, 0.25],
                   x_length=5.4, y_length=3.4,
                   axis_config=axis_kw,
                   y_axis_config={"decimal_number_config": {"num_decimal_places": 2,
                                                           "color": GRAY}},
                   ).shift(LEFT * 3.35 + UP * 0.35)
        ax2 = Axes(x_range=[0, 4.4, 1], y_range=[0, 1.12, 0.5],
                   x_length=5.4, y_length=3.4,
                   axis_config=axis_kw,
                   y_axis_config={"decimal_number_config": {"num_decimal_places": 1,
                                                           "color": GRAY}},
                   ).shift(RIGHT * 3.35 + UP * 0.35)

        t1 = Text("pdf  f(x) — the speedometer", font_size=25, color=PURPLE,
                  weight=BOLD).next_to(ax1, UP, buff=0.25)
        t2 = Text("cdf  F(x) — the odometer", font_size=25, color=GREEN,
                  weight=BOLD).next_to(ax2, UP, buff=0.25)

        pdf_graph = ax1.plot(pdf, x_range=[0, 4], use_smoothing=False,
                             color=PURPLE, stroke_width=5)
        one_line = DashedLine(ax2.c2p(0, 1), ax2.c2p(4.4, 1), color=GRAY,
                              stroke_width=2, dash_length=0.08)

        tr = ValueTracker(0.001)

        area = always_redraw(lambda: ax1.get_area(
            pdf_graph, x_range=[0, tr.get_value()], color=BLUE, opacity=0.35,
            stroke_width=0))
        scan = always_redraw(lambda: Line(
            ax1.c2p(tr.get_value(), 0),
            ax1.c2p(tr.get_value(), max(pdf(tr.get_value()), 0.02)),
            color=BLUE, stroke_width=4))
        Fcurve = always_redraw(lambda: ax2.plot(
            cdf, x_range=[0, max(tr.get_value(), 0.01)], use_smoothing=False,
            color=GREEN, stroke_width=5))
        dot = always_redraw(lambda: Dot(
            ax2.c2p(tr.get_value(), cdf(tr.get_value())), color=GREEN, radius=0.07))
        readout = always_redraw(lambda: Text(
            f"area so far = {cdf(tr.get_value()):.2f}", font_size=24, color=BLUE,
            weight=BOLD).move_to(ax2.c2p(2.95, 0.17)))

        self.play(FadeIn(ax1), FadeIn(ax2), FadeIn(t1), FadeIn(t2),
                  Create(pdf_graph), FadeIn(one_line), run_time=1.2)
        self.add(area, scan, Fcurve, dot, readout)
        self.swap_caption("F(x) = the area collected so far")

        self.play(tr.animate.set_value(1.5), run_time=4, rate_func=linear)
        self.wait(0.4)
        self.play(tr.animate.set_value(2.0), run_time=1.4, rate_func=linear)
        self.swap_caption("density peaks here — so F climbs steepest here:  slope of F = height of f",
                          color=AMBER)
        self.wait(0.8)
        self.play(tr.animate.set_value(4.0), run_time=5, rate_func=linear)
        self.swap_caption("every cdf ends at 1 — the whole rod weighs 1", color=GREEN)
        self.wait(1.8)
