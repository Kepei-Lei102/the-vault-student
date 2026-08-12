"""The three Faraday demo costumes, animated.

Scenes:
    MagnetCoil    — magnet into coil, galvanometer kick proportional to speed
    RodRails      — rod on rails in 3D; the camera swings 90 degrees and back
    RotatingCoil  — the window turning; hands off to the generator animation

Render (from this folder):
    manim -qm emi-demos.py MagnetCoil RodRails RotatingCoil    # smoke
    manim -qk emi-demos.py MagnetCoil RodRails RotatingCoil    # 4K final
Copy outputs beside the card as emi-demo-magnet-coil.mp4,
emi-demo-rod-rails.mp4, emi-demo-rotating-coil.mp4; then clear
media/ + __pycache__/.
"""

import numpy as np
from manim import *

BG = "#1a1a1a"
GRAY = "#9a9a9a"
BLUE = "#2563eb"
GREEN = "#059669"
AMBER = "#f59e0b"
RED = "#dc2626"
TEAL = "#0891b2"
PURPLE = "#7c3aed"

config.background_color = BG


class CaptionMixin:
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=26, color=color).to_edge(DOWN, buff=0.35)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.25), FadeIn(cap, run_time=0.35))
        else:
            self.play(FadeIn(cap, run_time=0.35))
        self._cap = cap


class MagnetCoil(CaptionMixin, Scene):
    def construct(self):
        # coil
        coil = VGroup(*[
            Ellipse(width=0.5, height=2.2, stroke_color=PURPLE, stroke_width=5)
            .move_to(RIGHT * (1.2 + 0.42 * i) + UP * 0.6)
            for i in range(5)
        ])
        wire = Line(coil[-1].get_center() + RIGHT * 0.25, RIGHT * 4.6 + UP * 0.6,
                    color=GRAY, stroke_width=2.5)
        # galvanometer
        g_c = RIGHT * 4.6 + DOWN * 1.3
        g_face = Circle(radius=0.85, color=GRAY, stroke_width=3).move_to(g_c)
        g_lab = Text("G", font_size=24, color=GRAY).move_to(g_c + DOWN * 0.45)
        wire2 = Line(RIGHT * 4.6 + UP * 0.6, g_c + UP * 0.85, color=GRAY, stroke_width=2.5)
        kick = ValueTracker(0.0)   # -1 .. 1

        def needle():
            a = kick.get_value() * 1.05   # radians of deflection
            return Line(g_c, g_c + 0.72 * np.array([np.sin(a), np.cos(a), 0]),
                        color=RED, stroke_width=4)
        needle_m = always_redraw(needle)
        zero_tick = Line(g_c + UP * 0.72, g_c + UP * 0.85, color=GRAY, stroke_width=2)

        # magnet
        mag = VGroup(
            Rectangle(width=1.5, height=0.75, stroke_color=BLUE, stroke_width=3,
                      fill_color=BLUE, fill_opacity=0.2),
            Text("N        S", font_size=22, color=GRAY, weight=BOLD),
        )
        mag[1].move_to(mag[0])
        mag.move_to(LEFT * 4.6 + UP * 0.6)

        self.play(FadeIn(coil), FadeIn(wire), FadeIn(wire2), FadeIn(g_face),
                  FadeIn(g_lab), FadeIn(zero_tick), FadeIn(mag), run_time=0.9)
        self.add(needle_m)

        self.swap_caption("push the magnet in slowly — a small, steady kick")
        self.play(mag.animate.shift(RIGHT * 3.4), kick.animate.set_value(0.35),
                  run_time=2.6, rate_func=linear)
        self.play(kick.animate.set_value(0.0), run_time=0.4)
        self.swap_caption("hold it still INSIDE the coil — flux high, unchanging: zero", color=TEAL)
        self.wait(1.4)
        self.swap_caption("now pull it out FAST — bigger kick, opposite way", color=AMBER)
        self.play(mag.animate.shift(LEFT * 3.4), kick.animate.set_value(-0.9),
                  run_time=0.9, rate_func=linear)
        self.play(kick.animate.set_value(0.0), run_time=0.5)
        self.wait(0.4)
        self.swap_caption("faster, more turns, stronger magnet — all mean a bigger kick")
        self.wait(1.8)


class RodRails(CaptionMixin, ThreeDScene):
    def construct(self):
        # rails along x, rod along y, B up (+z)
        rail1 = Line3D(start=np.array([-3.4, -1.2, 0]), end=np.array([3.2, -1.2, 0]),
                       color=GRAY, thickness=0.02)
        rail2 = Line3D(start=np.array([-3.4, 1.2, 0]), end=np.array([3.2, 1.2, 0]),
                       color=GRAY, thickness=0.02)
        endwire = Line3D(start=np.array([-3.4, -1.2, 0]), end=np.array([-3.4, 1.2, 0]),
                         color=GRAY, thickness=0.02)
        bulb = Sphere(center=np.array([-3.4, 0, 0]), radius=0.16,
                      resolution=(12, 12)).set_color(AMBER).set_opacity(0.25)

        b_arrows = VGroup(*[
            Arrow3D(start=np.array([x, y, 0.05]), end=np.array([x, y, 1.15]),
                    color=TEAL, thickness=0.015, base_radius=0.035)
            for x in (-1.6, 0.6, 2.4) for y in (-0.65, 0.65)
        ])

        rod_x = ValueTracker(0.4)

        def rod():
            x = rod_x.get_value()
            return Line3D(start=np.array([x, -1.2, 0]), end=np.array([x, 1.2, 0]),
                          color=PURPLE, thickness=0.045)
        rod_m = always_redraw(rod)

        def charge():
            # a positive carrier drifting toward -y as the rod moves
            x = rod_x.get_value()
            frac = (x - 0.4) / 2.2 if x > 0.4 else 0.0
            return Dot3D(point=np.array([x, 0.8 - 1.5 * min(frac, 1.0), 0.06]),
                         radius=0.07, color=AMBER)
        charge_m = always_redraw(charge)

        b_lab = Text("B — up, out of the plane", font_size=22, color=TEAL)
        b_lab.to_corner(UR, buff=0.4)

        cap_specs = [
            ("the flat view — rod on rails, field pointing at you", GRAY),
            ("now swing the view — the diagram becomes a machine", GRAY),
            ("B stands up from the plane; the rod sweeps through it", TEAL),
            ("every free charge rides the rod through B — F = Bqv, along the rod", AMBER),
            ("back to the flat view — the rod is a battery: E = BLv", PURPLE),
        ]
        caps = []
        for txt, col in cap_specs:
            cp = Text(txt, font_size=24, color=col).to_edge(DOWN, buff=0.35)
            cp.set_opacity(0)
            caps.append(cp)

        # start top-down: the textbook view; register EVERYTHING fixed up front
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.add(rail1, rail2, endwire, bulb, b_arrows, rod_m, charge_m)
        self.add_fixed_in_frame_mobjects(b_lab, *caps)

        def show(i, rt=0.45):
            anims = [caps[i].animate.set_opacity(1)]
            anims += [caps[j].animate.set_opacity(0) for j in range(len(caps)) if j != i]
            self.play(*anims, run_time=rt)

        show(0)
        self.play(rod_x.animate.set_value(1.4), run_time=2.0, rate_func=linear)
        self.wait(0.4)
        show(1)
        self.move_camera(phi=68 * DEGREES, theta=-135 * DEGREES, run_time=3.0)
        show(2)
        self.play(rod_x.animate.set_value(2.6), run_time=2.4, rate_func=linear)
        self.wait(0.3)
        show(3)
        self.play(rod_x.animate.set_value(0.6), run_time=2.8, rate_func=linear)
        self.wait(0.3)
        show(4)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=2.6)
        self.play(rod_x.animate.set_value(2.2), run_time=1.8, rate_func=linear)
        self.wait(1.4)


class RotatingCoil(CaptionMixin, Scene):
    def construct(self):
        c = UP * 0.7
        field = VGroup(*[
            Arrow(c + LEFT * 2.6 + UP * dy, c + RIGHT * 2.6 + UP * dy,
                  color=TEAL, stroke_width=2.5, tip_length=0.16, buff=0)
            for dy in (0.95, 0.0, -0.95)
        ])
        th = ValueTracker(0.0)

        def coil():
            a = th.get_value()
            d = np.array([np.sin(a), np.cos(a), 0.0]) * 1.25
            return VGroup(
                Line(c - d, c + d, color=PURPLE, stroke_width=7),
                Dot(c - d, radius=0.08, color=PURPLE),
                Dot(c + d, radius=0.08, color=PURPLE),
            )
        coil_m = always_redraw(coil)

        # flux meter
        base = DOWN * 1.9
        def meter():
            f = np.cos(th.get_value())
            w = abs(f) * 2.6 + 0.001
            col = TEAL if f >= 0 else BLUE
            bar = Rectangle(width=w, height=0.42, stroke_width=0,
                            fill_color=col, fill_opacity=0.75)
            bar.move_to(base + RIGHT * (w / 2 if f >= 0 else -w / 2))
            return bar
        meter_m = always_redraw(meter)
        tick = Line(base + UP * 0.32, base + DOWN * 0.32, color=GRAY, stroke_width=2.5)
        m_lab = Text("flux through the window", font_size=22, color=GRAY).next_to(base, DOWN, buff=0.45)

        self.play(FadeIn(field), FadeIn(tick), FadeIn(m_lab), run_time=0.7)
        self.add(coil_m, meter_m)
        self.swap_caption("the window turns — the flux swings, sign and all")
        self.play(th.animate.set_value(2 * TAU), run_time=7.0, rate_func=linear)
        self.swap_caption("a swinging flux is a CHANGING flux — the generator is born", color=AMBER)
        self.play(th.animate.set_value(3 * TAU), run_time=3.0, rate_func=linear)
        self.wait(1.0)
