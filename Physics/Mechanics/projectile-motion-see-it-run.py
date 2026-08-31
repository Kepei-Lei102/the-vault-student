"""Manim: Projectile Motion — see it run.

Act 1  The two coins: one dropped, one flicked sideways from the same height —
       strobe flashes show identical heights at every instant; one click.
Act 2  The monkey and hunter: aim straight at a target that lets go at the
       moment of firing — dart and target droop by the identical half-g-t-squared,
       so a straight aim cannot miss.
Act 3  One speed, many angles: the trajectory family, complementary pairs
       landing together, and the bounding parabola emerging over the top.

Paced slowly per house rule: one-clause captions, 2–4 s holds.

Render (from this folder):
    manim -ql projectile-motion-see-it-run.py ProjectileSeeItRun    # smoke
    manim -qk projectile-motion-see-it-run.py ProjectileSeeItRun    # 4K final
Copy media/videos/projectile-motion-see-it-run/2160p60/ProjectileSeeItRun.mp4
  -> projectile-motion-see-it-run.mp4 beside the card, then rm -rf media/ __pycache__/.
"""

import numpy as np
from manim import (
    Scene, VGroup, VMobject, Text, Dot, Line, DashedLine, Circle,
    FadeIn, FadeOut, Create, Transform, Flash,
    UP, DOWN, LEFT, RIGHT, config,
)

BG = "#1e1e1e"; TXT = "#cccccc"; GREY = "#9a9a9a"
BLUE = "#2563eb"; GREEN = "#059669"; AMBER = "#f59e0b"; RED = "#dc2626"; TEAL = "#0891b2"
FONT = "Helvetica Neue"
config.background_color = BG


def caption(s, size=26):
    return Text(s, font=FONT, font_size=size, color=TXT).to_edge(UP, buff=0.35)


class ProjectileSeeItRun(Scene):
    def construct(self):
        GROUND = -3.1

        # ================= Act 1 — the two coins
        cap = caption("one coin dropped, one flicked sideways — same instant, same height")
        floor = Line(np.array([-7, GROUND, 0]), np.array([7, GROUND, 0]), color=GREY, stroke_width=2)
        self.play(FadeIn(cap), Create(floor), run_time=1.0)

        y0, g2 = 2.6, 1.45          # start height, scene-units gravity/2
        vx = 1.35
        T = np.sqrt((y0 - GROUND) / g2)
        drop0 = np.array([-4.6, y0, 0]); fly0 = np.array([-4.0, y0, 0])
        d1 = Dot(drop0, radius=0.11, color=RED)
        d2 = Dot(fly0, radius=0.11, color=BLUE)
        self.play(FadeIn(d1), FadeIn(d2), run_time=0.8)
        self.wait(1.6)

        steps = 8
        for k in range(1, steps + 1):
            t = T * k / steps
            p1 = drop0 + np.array([0, -g2 * t**2, 0])
            p2 = fly0 + np.array([vx * t, -g2 * t**2, 0])
            g1 = Dot(p1, radius=0.07, color=RED).set_opacity(0.45)
            g2m = Dot(p2, radius=0.07, color=BLUE).set_opacity(0.45)
            link = DashedLine(p1, p2, color=GREY, stroke_width=1.4).set_opacity(0.6)
            self.play(d1.animate.move_to(p1), d2.animate.move_to(p2),
                      run_time=0.55, rate_func=lambda s: s)
            self.add(g1, g2m, link)
        cap2 = caption("level with each other at every flash — they land with one click")
        self.play(Transform(cap, cap2), Flash(d1, color=RED, flash_radius=0.35),
                  Flash(d2, color=BLUE, flash_radius=0.35), run_time=1.2)
        self.wait(3.0)
        self.play(*[FadeOut(m) for m in self.mobjects if m not in (cap, floor)], run_time=0.8)

        # ================= Act 2 — the monkey and hunter
        cap3 = caption("aim STRAIGHT at a target that lets go the moment you fire")
        self.play(Transform(cap, cap3), run_time=0.8)
        gun = np.array([-5.6, -2.2, 0])
        monkey0 = np.array([4.6, 2.2, 0])
        aim = DashedLine(gun, monkey0, color=GREY, stroke_width=1.6)
        m_dot = Dot(monkey0, radius=0.15, color=AMBER)
        branch = Line(monkey0 + np.array([-0.6, 0.35, 0]), monkey0 + np.array([0.6, 0.35, 0]),
                      color=GREY, stroke_width=2)
        hang = Line(monkey0 + np.array([0, 0.35, 0]), monkey0, color=GREY, stroke_width=1.2)
        dart = Dot(gun, radius=0.11, color=GREEN)
        self.play(Create(aim), FadeIn(branch), FadeIn(hang), FadeIn(m_dot), FadeIn(dart), run_time=1.2)
        self.wait(2.2)

        u_hat = (monkey0 - gun) / np.linalg.norm(monkey0 - gun)
        V = 3.4
        t_hit = np.linalg.norm(monkey0 - gun) / V
        gsc = 0.23
        cap4 = caption("both fall by the identical amount below where they would have been")
        self.play(Transform(cap, cap4), FadeOut(hang), run_time=0.7)
        steps = 10
        for k in range(1, steps + 1):
            t = t_hit * k / steps
            pd = gun + V * t * u_hat + np.array([0, -gsc * t**2, 0])
            pm = monkey0 + np.array([0, -gsc * t**2, 0])
            self.add(Dot(pd, radius=0.06, color=GREEN).set_opacity(0.4),
                     Dot(pm, radius=0.06, color=AMBER).set_opacity(0.4))
            self.play(dart.animate.move_to(pd), m_dot.animate.move_to(pm),
                      run_time=0.42, rate_func=lambda s: s)
        self.play(Flash(m_dot, color=AMBER, flash_radius=0.5), run_time=0.8)
        cap5 = caption("the droop below the aim line is the same ½gt² for both — you cannot miss")
        self.play(Transform(cap, cap5), run_time=0.8)
        self.wait(3.2)
        self.play(*[FadeOut(m) for m in self.mobjects if m not in (cap, floor)], run_time=0.8)

        # ================= Act 3 — one speed, many angles
        cap6 = caption("one launch speed, five angles — watch who lands together")
        self.play(Transform(cap, cap6), run_time=0.8)
        Vs = 2.62
        gsc = 0.62
        origin = np.array([-5.9, GROUND, 0])

        def traj(adeg):
            th = np.radians(adeg)
            tf = 2 * Vs * np.sin(th) / gsc
            ts = np.linspace(0, tf, 90)
            pts = [origin + np.array([Vs * np.cos(th) * t, Vs * np.sin(th) * t - 0.5 * gsc * t**2, 0])
                   for t in ts]
            v = VMobject(stroke_width=2.6)
            v.set_points_smoothly(pts)
            return v

        for a, col, hold in [(15, TEAL, 0.4), (75, TEAL, 1.6), (30, BLUE, 0.4), (60, BLUE, 1.6)]:
            c = traj(a); c.set_color(col)
            if a in (75, 60):
                c.set_stroke(opacity=0.75)
            self.play(Create(c), run_time=1.3)
            if hold > 1:
                self.wait(hold - 1)
        cap7 = caption("15° with 75°, 30° with 60° — complementary pairs share a landing point")
        self.play(Transform(cap, cap7), run_time=0.8)
        self.wait(2.0)
        c45 = traj(45); c45.set_color(GREEN); c45.set_stroke(width=4)
        self.play(Create(c45), run_time=1.5)
        cap8 = caption("45° goes furthest — when launch and landing share a height")
        self.play(Transform(cap, cap8), run_time=0.8)
        self.wait(2.0)

        xe = np.linspace(0, 2 * Vs**2 / gsc * 1.0, 120)
        env_pts = [origin + np.array([x, Vs**2 / (2 * gsc) - gsc * x**2 / (2 * Vs**2), 0])
                   for x in xe if Vs**2 / (2 * gsc) - gsc * x**2 / (2 * Vs**2) >= 0]
        env = VMobject(color=AMBER, stroke_width=2.4)
        env.set_points_smoothly(env_pts)
        from manim import DashedVMobject
        self.play(Create(DashedVMobject(env, num_dashes=45)), run_time=2.2)
        cap9 = caption("and over them all: the bounding parabola — beyond it, no angle can reach")
        self.play(Transform(cap, cap9), run_time=0.9)
        self.wait(4.0)
