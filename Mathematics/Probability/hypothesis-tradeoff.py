"""The alpha-beta see-saw, and how n beats it.

Two worlds: H0's bell (innocent) and the true alternative's bell
(guilty), one cut line. Sweep the cut and watch alpha and beta trade;
then quadruple the sample so both bells sharpen and both errors fall.
Deterministic — no randomness, no seed.

Render (from this folder):
    manim -qm hypothesis-tradeoff.py TradeOff   # smoke
    manim -qk hypothesis-tradeoff.py TradeOff   # 4K final
Copy the output beside the card as hypothesis-tradeoff.mp4, then clear
media/ + __pycache__/.
"""

import numpy as np
from manim import *

BG = "#1a1a1a"
GRAY = "#9a9a9a"
BLUE = "#2563eb"
AMBER = "#f59e0b"
RED = "#dc2626"
PURPLE = "#7c3aed"
GREEN = "#059669"

config.background_color = BG

MU0, MU1 = 0.0, 2.2


def norm_cdf(z):
    from math import erf, sqrt
    return 0.5 * (1 + erf(z / sqrt(2)))


class TradeOff(Scene):
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=25, color=color).to_edge(DOWN, buff=0.3)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.2), FadeIn(cap, run_time=0.3))
        else:
            self.play(FadeIn(cap, run_time=0.3))
        self._cap = cap

    def construct(self):
        ax = Axes(x_range=[-3.6, 5.8, 1], y_range=[0, 0.95, 1],
                  x_length=11.6, y_length=4.6,
                  axis_config=dict(color=GRAY, include_ticks=False,
                                   include_numbers=False)
                  ).shift(DOWN * 0.55)

        cut = ValueTracker(1.1)
        sig = ValueTracker(1.0)     # shrinks when n grows

        def f0(x):
            s = sig.get_value()
            return np.exp(-((x - MU0) / s) ** 2 / 2) / (s * np.sqrt(2 * np.pi))

        def f1(x):
            s = sig.get_value()
            return np.exp(-((x - MU1) / s) ** 2 / 2) / (s * np.sqrt(2 * np.pi))

        bell0 = always_redraw(lambda: ax.plot(f0, x_range=[-3.6, 5.8],
                                              color=BLUE, stroke_width=4.5))
        bell1 = always_redraw(lambda: ax.plot(f1, x_range=[-3.6, 5.8],
                                              color=AMBER, stroke_width=4.5))
        a_area = always_redraw(lambda: ax.get_area(
            ax.plot(f0, x_range=[cut.get_value(), 5.8]),
            x_range=[cut.get_value(), 5.8], color=RED, opacity=0.5, stroke_width=0))
        b_area = always_redraw(lambda: ax.get_area(
            ax.plot(f1, x_range=[-3.6, cut.get_value()]),
            x_range=[-3.6, cut.get_value()], color=AMBER, opacity=0.35, stroke_width=0))
        line = always_redraw(lambda: Line(
            ax.c2p(cut.get_value(), 0), ax.c2p(cut.get_value(), 0.88),
            color=PURPLE, stroke_width=5))

        lab0 = Text("H0's world (innocent)", font_size=24, color=BLUE,
                    weight=BOLD).move_to(ax.c2p(-2.4, 0.62))
        lab1 = Text("the true state (guilty)", font_size=24, color=AMBER,
                    weight=BOLD).move_to(ax.c2p(4.55, 0.62))

        def a_val():
            s = sig.get_value()
            return 1 - norm_cdf((cut.get_value() - MU0) / s)

        def b_val():
            s = sig.get_value()
            return norm_cdf((cut.get_value() - MU1) / s)

        a_txt = always_redraw(lambda: Text(
            f"α = {a_val()*100:4.1f}%   convict the innocent", font_size=25,
            color=RED, weight=BOLD).to_corner(UL, buff=0.45))
        b_txt = always_redraw(lambda: Text(
            f"β = {b_val()*100:4.1f}%   the guilty walks free", font_size=25,
            color=AMBER, weight=BOLD).to_corner(UL, buff=0.45).shift(DOWN * 0.5))

        self.play(FadeIn(ax), Create(bell0), Create(bell1), FadeIn(line),
                  FadeIn(lab0), FadeIn(lab1), run_time=1.2)
        self.add(a_area, b_area, a_txt, b_txt)
        self.swap_caption("one cut line, two ways to be wrong — on opposite sides of it")
        self.wait(1.2)

        self.swap_caption("demand stronger proof (push the cut right): α falls... and β climbs", color=RED)
        self.play(cut.animate.set_value(2.1), run_time=3, rate_func=smooth)
        self.wait(0.6)
        self.swap_caption("go easy on conviction (pull it left): β falls... and α climbs", color=AMBER)
        self.play(cut.animate.set_value(0.35), run_time=3, rate_func=smooth)
        self.wait(0.6)
        self.swap_caption("the see-saw is the law: with a fixed sample, you only trade one error for the other")
        self.play(cut.animate.set_value(1.1), run_time=1.6)
        self.wait(0.8)

        self.swap_caption("the only way to beat it: MORE EVIDENCE — quadruple n, halve each bell's spread...",
                          color=GREEN)
        self.play(sig.animate.set_value(0.5), run_time=3, rate_func=smooth)
        self.wait(0.6)
        self.swap_caption("...and BOTH errors collapse. The see-saw bows to sample size.", color=GREEN)
        self.wait(2.0)
