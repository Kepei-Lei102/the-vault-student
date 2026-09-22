"""Manim scene for [[Multiple Integrals]].

SweepTwoWays — the region between y = x^2 and y = x, described twice.  First a vertical strip sweeps from x = 0 to x = 1: its
               bottom end rides the parabola and its top end rides the line, so the inner limits are y = x^2 and y = x.  Then a
               horizontal strip sweeps from y = 0 to y = 1: it enters at the line (x = y) and leaves at the parabola (x = sqrt y).
               Same region, same integral (1/24 for f = xy), two sets of limits.  The inner limits are read off the strip's ends.
Smoke:  manim -ql --fps 15 multiple-integrals-manim.py SweepTwoWays
Final:  manim -qk multiple-integrals-manim.py SweepTwoWays
"""
import numpy as np
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b"


class SweepTwoWays(Scene):
    def construct(self):
        self.add(Text("One region, two descriptions: the ends of the strip are the inner limits", font_size=26, color=GREY_T).to_edge(UP, buff=0.25))
        ax = Axes(x_range=[0, 1.15, 0.5], y_range=[0, 1.15, 0.5], x_length=5.0, y_length=5.0, tips=False,
                  axis_config={"color": GREY_T, "stroke_width": 2, "include_ticks": True}).move_to([-3.2, 0.1, 0])
        P = lambda X, Y: ax.c2p(X, Y)
        xs = np.linspace(0, 1, 80)
        region = Polygon(*[P(X, X * X) for X in xs], *[P(X, X) for X in xs[::-1]], color=BLUE_H, stroke_width=0, fill_color=BLUE_H, fill_opacity=0.3)
        parab = ax.plot(lambda X: X * X, x_range=[0, 1.07], color=GREEN_H, stroke_width=4)
        line = ax.plot(lambda X: X, x_range=[0, 1.07], color=RED_H, stroke_width=4)
        l1 = Text("y = x", font_size=22, color=RED_H).move_to(P(0.62, 0.86)); l2 = Text("y = x²", font_size=22, color=GREEN_H).move_to(P(0.98, 0.72))
        xl = Text("x", font_size=22, color=GREY_T).next_to(ax, RIGHT, buff=0.1).shift(DOWN * 2.3); yl = Text("y", font_size=22, color=GREY_T).next_to(ax, UP, buff=0.05).shift(LEFT * 2.4)
        one_x = Text("1", font_size=20, color=GREY_T).move_to(P(1, -0.07)); one_y = Text("1", font_size=20, color=GREY_T).move_to(P(-0.06, 1))
        self.add(ax, region, parab, line, l1, l2, xl, yl, one_x, one_y)

        cap = Text("the region between the line and the parabola", font_size=24, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(cap); self.wait(1.5)

        def say(s, col=GREY_T):
            nonlocal cap
            self.remove(cap); cap = Text(s, font_size=24, color=col).to_edge(DOWN, buff=0.3); self.add(cap)

        def panel(lines, y0):
            g = VGroup(*[Text(t, font="Menlo", font_size=22, color=c) for t, c in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
            return g.move_to([3.6, y0, 0])

        # ---------- vertical strips ----------
        t = ValueTracker(0.05)
        w = 0.03
        strip = always_redraw(lambda: Polygon(P(t.get_value() - w, (t.get_value() - w)**2), P(t.get_value() + w, (t.get_value() + w)**2),
                                              P(t.get_value() + w, t.get_value() + w), P(t.get_value() - w, t.get_value() - w),
                                              color=AMBER_H, stroke_width=2, fill_color=AMBER_H, fill_opacity=0.7))
        bot = always_redraw(lambda: Dot(P(t.get_value(), t.get_value()**2), color=GREEN_H, radius=0.09))
        top = always_redraw(lambda: Dot(P(t.get_value(), t.get_value()), color=RED_H, radius=0.09))
        read = always_redraw(lambda: panel([(f"x = {t.get_value():.2f}", AMBER_H), (f"from y = {t.get_value()**2:.2f}  (parabola)", GREEN_H), (f"up to y = {t.get_value():.2f}  (line)", RED_H)], 1.6))
        say("hold x still.  The strip runs UP: it starts on the parabola and ends on the line.", AMBER_H)
        self.add(strip, bot, top, read); self.wait(1.2)
        self.play(t.animate.set_value(0.95), run_time=7, rate_func=smooth)
        res1 = panel([("inner:  y from x² to x", GREY_T), ("outer:  x from 0 to 1", GREY_T), ("∫∫ xy dy dx = 1/24", AMBER_H)], -0.6)
        say("the ends moved as x moved, so the inner limits are functions of x: x² and x", GREY_T)
        self.play(FadeIn(res1), run_time=0.8); self.wait(2.8)
        self.play(FadeOut(strip), FadeOut(bot), FadeOut(top), FadeOut(read), run_time=0.6)

        # ---------- horizontal strips ----------
        s = ValueTracker(0.05)
        strip2 = always_redraw(lambda: Polygon(P(s.get_value() - w, s.get_value() - w), P(np.sqrt(max(s.get_value() - w, 0)), s.get_value() - w),
                                               P(np.sqrt(s.get_value() + w), s.get_value() + w), P(s.get_value() + w, s.get_value() + w),
                                               color=PURPLE_H, stroke_width=2, fill_color=PURPLE_H, fill_opacity=0.7))
        lft = always_redraw(lambda: Dot(P(s.get_value(), s.get_value()), color=RED_H, radius=0.09))
        rgt = always_redraw(lambda: Dot(P(np.sqrt(s.get_value()), s.get_value()), color=GREEN_H, radius=0.09))
        read2 = always_redraw(lambda: panel([(f"y = {s.get_value():.2f}", PURPLE_H), (f"from x = {s.get_value():.2f}  (line)", RED_H), (f"across to x = {np.sqrt(s.get_value()):.2f}  (parabola)", GREEN_H)], 1.6))
        say("now hold y still.  The strip runs ACROSS: it starts on the line and ends on the parabola.", PURPLE_H)
        self.add(strip2, lft, rgt, read2); self.wait(1.2)
        self.play(s.animate.set_value(0.95), run_time=7, rate_func=smooth)
        res2 = panel([("inner:  x from y to √y", GREY_T), ("outer:  y from 0 to 1", GREY_T), ("∫∫ xy dx dy = 1/24", PURPLE_H)], -2.35)
        say("same curves, read the other way round: x = y and x = √y", GREY_T)
        self.play(FadeIn(res2), run_time=0.8); self.wait(2.8)
        self.play(FadeOut(strip2), FadeOut(lft), FadeOut(rgt), FadeOut(read2), run_time=0.6)
        say("the outer limits are always numbers.  Only the inner limits may depend on the other variable.", GREEN_H)
        self.wait(4.5)
