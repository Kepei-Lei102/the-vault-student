"""Manim scenes for [[Special Relativity]].

LightClock    — two identical light clocks.  One stays put; one moves to the right at 0.6c.  Light moves at the same
                speed along both paths, so the moving clock's longer zigzag takes longer per tick: 4 ticks to the
                stationary clock's 5 (gamma = 1.25).
Simultaneity  — a flash goes off in the middle of a carriage moving at 0.6c.  Top: the carriage's own frame, where
                the light reaches both ends together.  Bottom: the platform's frame, drawn to scale, where the rear
                wall runs into the light and the front wall runs away from it, so the rear is hit first.
Smoke:  manim -ql --fps 15 special-relativity-manim.py LightClock Simultaneity
Final:  manim -qk special-relativity-manim.py LightClock Simultaneity
"""
import numpy as np
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H, TEAL_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
BETA = 0.6
GAMMA = 1 / np.sqrt(1 - BETA**2)


def tri(u):
    """Triangle wave: 0 -> 1 -> 0 over u in [0, 1], repeating."""
    u = u % 1.0
    return 2 * u if u < 0.5 else 2 - 2 * u


class LightClock(Scene):
    def construct(self):
        self.add(Text("Two identical light clocks.  Light always travels at the same speed.", font_size=26, color=GREY_T).to_edge(UP, buff=0.25))
        H = 1.6                       # mirror separation, scene units
        C = 1.0                       # speed of light in scene units per second of video
        T0 = 2 * H / C                # proper tick period (3.2 s of video)
        TM = GAMMA * T0               # the moving clock's tick as seen here (4 s)
        V = BETA * C
        y0 = -0.9
        xA, xB0 = -6.0, -4.0
        t = ValueTracker(0.0)

        def mirrors(x, col):
            return VGroup(Line([x - 0.45, y0, 0], [x + 0.45, y0, 0], color=col, stroke_width=6), Line([x - 0.45, y0 + H, 0], [x + 0.45, y0 + H, 0], color=col, stroke_width=6))

        clockA = mirrors(xA, GREY_T)
        photonA = always_redraw(lambda: Dot([xA, y0 + H * tri(t.get_value() / T0), 0], color=AMBER_H, radius=0.11))
        clockB = always_redraw(lambda: mirrors(xB0 + V * t.get_value(), BLUE_H))
        photonB = always_redraw(lambda: Dot([xB0 + V * t.get_value(), y0 + H * tri(t.get_value() / TM), 0], color=AMBER_H, radius=0.11))

        def trail():
            tt = t.get_value(); n = max(2, int(tt * 30))
            pts = [[xB0 + V * s, y0 + H * tri(s / TM), 0] for s in np.linspace(0, tt, n)]
            return VMobject(color=AMBER_H, stroke_width=2.5, stroke_opacity=0.6).set_points_as_corners(pts)
        pathB = always_redraw(trail)

        def trailA():
            tt = t.get_value()
            return Line([xA, y0, 0], [xA, y0 + H * (1 if tt > T0 / 2 else tri(tt / T0)), 0], color=AMBER_H, stroke_width=2.5, stroke_opacity=0.6)
        pathA = always_redraw(trailA)

        labA = Text("at rest", font_size=20, color=GREY_T).move_to([xA, y0 - 0.45, 0])
        labB = always_redraw(lambda: Text("moving at 0.6c", font_size=20, color=BLUE_H).move_to([xB0 + V * t.get_value(), y0 - 0.45, 0]))
        cntA = always_redraw(lambda: Text(f"ticks: {int(t.get_value() / T0 + 1e-6)}", font_size=24, color=GREY_T).move_to([xA, y0 + H + 0.5, 0]))
        cntB = always_redraw(lambda: Text(f"ticks: {int(t.get_value() / TM + 1e-6)}", font_size=24, color=BLUE_H).move_to([xB0 + V * t.get_value(), y0 + H + 0.5, 0]))
        self.add(clockA, clockB, pathA, pathB, photonA, photonB, labA, labB, cntA, cntB)

        cap = Text("one tick = light goes up and comes back", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(cap); self.wait(1.5)

        def say(s, col=GREY_T):
            nonlocal cap
            self.remove(cap); cap = Text(s, font_size=22, color=col).to_edge(DOWN, buff=0.3); self.add(cap)

        say("the moving clock's light has to travel along a diagonal, at the very same speed", AMBER_H)
        self.play(t.animate.set_value(8.0), run_time=8.0, rate_func=linear)
        say("the diagonal is longer, so each tick of the moving clock takes longer: 2 ticks against 2.5", BLUE_H); self.wait(2.0)
        self.play(t.animate.set_value(16.0), run_time=8.0, rate_func=linear)
        say("after 5 ticks of the clock at rest, the moving clock has ticked 4 times: a factor of 1.25", GREEN_H); self.wait(3.0)
        say("nothing is wrong with the moving clock.  Time itself runs at a different rate between the two.", GREY_T); self.wait(3.5)


class Simultaneity(Scene):
    def construct(self):
        self.add(Text("One flash in the middle of a carriage.  Which end does the light reach first?", font_size=26, color=GREY_T).to_edge(UP, buff=0.25))
        C = 1.0                                   # light speed, scene units per second of video
        L0 = 4.8                                  # the carriage's length in its own frame
        L = L0 / GAMMA                            # contracted length on the platform (3.84)
        V = BETA * C
        yT, yP = 1.35, -1.55
        t = ValueTracker(0.0)

        # ---- top: the carriage frame ----
        self.add(Text("riding in the carriage", font_size=22, color=BLUE_H).move_to([-4.9, yT + 1.0, 0]))
        carT = Rectangle(width=L0, height=0.9, color=BLUE_H, stroke_width=3).move_to([0, yT, 0])
        midT = Dot([0, yT, 0], color=GREY_T, radius=0.05)
        t_hit_T = (L0 / 2) / C
        lT = always_redraw(lambda: Dot([-min(C * t.get_value(), L0 / 2), yT, 0], color=AMBER_H, radius=0.11))
        rT = always_redraw(lambda: Dot([+min(C * t.get_value(), L0 / 2), yT, 0], color=AMBER_H, radius=0.11))
        hitT = always_redraw(lambda: VGroup(*[Star(n=6, outer_radius=0.22, color=GREEN_H, fill_opacity=1).move_to([s * L0 / 2, yT, 0]) for s in (-1, 1)])
                             if t.get_value() >= t_hit_T else VGroup(Dot([0, 9, 0], radius=0.001), Dot([0, 9, 0], radius=0.001)))

        # ---- bottom: the platform frame ----
        self.add(Text("standing on the platform", font_size=22, color=PURPLE_H).move_to([-4.7, yP + 1.0, 0]))
        x0 = -3.2                                 # where the middle of the carriage is when the flash goes off
        t_rear = (L / 2) / (C + V)                # light going backwards meets the rear wall coming forwards
        t_front = (L / 2) / (C - V)               # light going forwards has to chase the front wall
        carP = always_redraw(lambda: Rectangle(width=L, height=0.9, color=PURPLE_H, stroke_width=3).move_to([x0 + V * t.get_value(), yP, 0]))
        flash = Dot([x0, yP, 0], color=GREY_T, radius=0.05)
        lP = always_redraw(lambda: Dot([x0 - C * t.get_value(), yP, 0], color=AMBER_H, radius=0.11) if t.get_value() < t_rear else Dot([0, 9, 0], radius=0.001))
        rP = always_redraw(lambda: Dot([x0 + C * t.get_value(), yP, 0], color=AMBER_H, radius=0.11) if t.get_value() < t_front else Dot([0, 9, 0], radius=0.001))
        star = lambda x, col: Star(n=6, outer_radius=0.22, color=col, fill_opacity=1).move_to([x, yP, 0])
        far = lambda: Dot([0, 9, 0], radius=0.001)
        hitR = always_redraw(lambda: star(x0 + V * t.get_value() - L / 2, RED_H) if t.get_value() >= t_rear else far())
        hitF = always_redraw(lambda: star(x0 + V * t.get_value() + L / 2, GREEN_H) if t.get_value() >= t_front else far())
        arrow = Arrow([x0 + 1.2, yP - 0.85, 0], [x0 + 2.6, yP - 0.85, 0], buff=0, color=PURPLE_H, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        arrow_l = Text("0.6c", font_size=20, color=PURPLE_H).next_to(arrow, RIGHT, buff=0.1)
        self.add(carT, midT, lT, rT, hitT, carP, flash, lP, rP, hitR, hitF, arrow, arrow_l)

        cap = Text("same carriage, same flash, watched from two places", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(cap); self.wait(2)

        def say(s, col=GREY_T):
            nonlocal cap
            self.remove(cap); cap = Text(s, font_size=22, color=col).to_edge(DOWN, buff=0.3); self.add(cap)

        say("light leaves the middle at the same speed in both directions, for both observers", AMBER_H)
        self.play(t.animate.set_value(t_rear), run_time=t_rear * 1.6, rate_func=linear)
        say("platform: the rear wall ran to meet the light.  It is hit already.", RED_H); self.wait(2.2)
        self.play(t.animate.set_value(t_hit_T), run_time=(t_hit_T - t_rear) * 1.6, rate_func=linear)
        say("carriage: both ends are hit at the same moment", GREEN_H); self.wait(2.2)
        self.play(t.animate.set_value(t_front), run_time=(t_front - t_hit_T) * 1.6, rate_func=linear)
        say("platform: the front wall ran away from the light, and is hit much later", GREEN_H); self.wait(2.2)
        say("both accounts are correct.  Whether two separated events are simultaneous depends on who asks.", GREY_T); self.wait(4)
