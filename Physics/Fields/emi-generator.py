"""The a.c. generator: rotating window, live flux and e.m.f. traces.

The e.m.f. graph is the slope of the flux graph — peaks where flux crosses
zero, zeros where flux peaks. Final act doubles the rotation speed: the
e.m.f. doubles in amplitude AND frequency; the flux amplitude does not.

Render (from this folder):
    manim -qm emi-generator.py ACGenerator     # smoke
    manim -qk emi-generator.py ACGenerator     # 4K final
Copy the output beside the card as emi-generator.mp4, then clear
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

T_SLOW = 4 * PI          # two revolutions at omega = 1
T_MAX = 6 * PI           # then two more at omega = 2


def theta_of(t):
    return t if t <= T_SLOW else T_SLOW + 2 * (t - T_SLOW)


def omega_of(t):
    return 1.0 if t <= T_SLOW else 2.0


class ACGenerator(Scene):
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=26, color=color).to_edge(DOWN, buff=0.35)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.25), FadeIn(cap, run_time=0.35))
        else:
            self.play(FadeIn(cap, run_time=0.35))
        self._cap = cap

    def construct(self):
        t = ValueTracker(0.0)

        # ---------- left: poles, field, rotating coil ----------
        c = LEFT * 4.5 + UP * 0.55
        pole_n = VGroup(
            RoundedRectangle(corner_radius=0.08, width=0.75, height=3.1,
                             stroke_color=BLUE, stroke_width=3, fill_color=BLUE, fill_opacity=0.18),
            Text("N", font_size=30, color=GRAY, weight=BOLD),
        )
        pole_n[1].move_to(pole_n[0])
        pole_n.move_to(c + LEFT * 2.15)
        pole_s = VGroup(
            RoundedRectangle(corner_radius=0.08, width=0.75, height=3.1,
                             stroke_color=RED, stroke_width=3, fill_color=RED, fill_opacity=0.15),
            Text("S", font_size=30, color=GRAY, weight=BOLD),
        )
        pole_s[1].move_to(pole_s[0])
        pole_s.move_to(c + RIGHT * 2.15)

        field = VGroup(*[
            Arrow(c + LEFT * 1.7 + UP * dy, c + RIGHT * 1.7 + UP * dy,
                  color=TEAL, stroke_width=2.5, tip_length=0.16, buff=0)
            for dy in (1.05, 0.0, -1.05)
        ])

        def coil():
            th = theta_of(t.get_value())
            d = np.array([np.sin(th), np.cos(th), 0.0]) * 1.15
            line = Line(c - d, c + d, color=PURPLE, stroke_width=7)
            ends = VGroup(Dot(c - d, radius=0.075, color=PURPLE),
                          Dot(c + d, radius=0.075, color=PURPLE))
            return VGroup(line, ends)

        coil_m = always_redraw(coil)
        spin = CurvedArrow(c + UP * 1.7 + LEFT * 0.55, c + UP * 1.7 + RIGHT * 0.55,
                           angle=-1.1, color=AMBER, stroke_width=3, tip_length=0.16)

        # ---------- right: stacked live graphs ----------
        ax_flux = Axes(x_range=[0, T_MAX, T_MAX + 1], y_range=[-1.4, 1.4, 10],
                       x_length=6.3, y_length=1.9,
                       axis_config={"color": GRAY, "stroke_width": 1.6,
                                    "include_ticks": False, "include_tip": False}
                       ).move_to(RIGHT * 3.35 + UP * 1.75)
        ax_emf = Axes(x_range=[0, T_MAX, T_MAX + 1], y_range=[-2.4, 2.4, 10],
                      x_length=6.3, y_length=2.4,
                      axis_config={"color": GRAY, "stroke_width": 1.6,
                                   "include_ticks": False, "include_tip": False}
                      ).move_to(RIGHT * 3.35 + DOWN * 1.35)
        lab_flux = Text("flux NΦ", font_size=21, color=TEAL, weight=BOLD).next_to(ax_flux, UP, buff=0.08).align_to(ax_flux, LEFT)
        lab_emf = Text("e.m.f.", font_size=21, color=AMBER, weight=BOLD).next_to(ax_emf, UP, buff=0.08).align_to(ax_emf, LEFT)

        def flux_curve():
            tn = max(t.get_value(), 0.02)
            return ax_flux.plot(lambda x: np.cos(theta_of(x)), x_range=[0, tn, 0.04],
                                color=TEAL, stroke_width=3)

        def emf_curve():
            tn = max(t.get_value(), 0.02)
            return ax_emf.plot(lambda x: omega_of(x) * np.sin(theta_of(x)), x_range=[0, tn, 0.04],
                               color=AMBER, stroke_width=3)

        flux_m = always_redraw(flux_curve)
        emf_m = always_redraw(emf_curve)

        def marks():
            tv = max(t.get_value(), 0.02)
            th = theta_of(tv)
            w = omega_of(tv)
            fy, ey = np.cos(th), w * np.sin(th)
            pf = ax_flux.c2p(tv, fy)
            pe = ax_emf.c2p(tv, ey)
            dt_ = 0.55
            slope = -w * np.sin(th)
            p1 = ax_flux.c2p(max(tv - dt_, 0.0), fy - min(tv, dt_) * slope)
            p2 = ax_flux.c2p(tv + dt_, fy + dt_ * slope)
            tang = Line(p1, p2, color=GREEN, stroke_width=4.5)
            conn = DashedLine(pf, pe, color=GRAY, stroke_width=1.5, dash_length=0.09)
            return VGroup(tang, conn, Dot(pf, radius=0.065, color=TEAL),
                          Dot(pe, radius=0.065, color=AMBER))
        marks_m = always_redraw(marks)

        self.play(FadeIn(pole_n), FadeIn(pole_s), FadeIn(field), FadeIn(spin),
                  FadeIn(ax_flux), FadeIn(ax_emf), FadeIn(lab_flux), FadeIn(lab_emf), run_time=1.0)
        self.add(coil_m, flux_m, emf_m, marks_m)

        self.swap_caption("watch the GREEN tangent on the flux graph — its slope is the whole story")
        # to first edge-on position (theta = pi/2)
        self.play(t.animate.set_value(PI / 2), run_time=2.2, rate_func=linear)
        self.swap_caption("window EMPTY — flux sweeps through zero fastest: e.m.f. maximum", color=AMBER)
        self.wait(0.9)
        # to face-on inverted (theta = pi) then full turn (theta = 2 pi)
        self.play(t.animate.set_value(2 * PI), run_time=4.0, rate_func=linear)
        self.swap_caption("window FULL — flux at its peak, momentarily unchanging: e.m.f. zero", color=TEAL)
        self.wait(0.9)
        self.play(t.animate.set_value(T_SLOW), run_time=4.5, rate_func=linear)
        self.swap_caption("the tangent's slope IS the e.m.f. below — steep flux, tall e.m.f.; flat flux, zero", color=GREEN)
        self.wait(1.0)

        # double speed
        self.swap_caption("now double the rotation speed…", color=GRAY)
        self.play(t.animate.set_value(T_MAX), run_time=4.5, rate_func=linear)
        self.swap_caption("twice the peaks, twice as often — and the flux amplitude never changed", color=AMBER)
        self.wait(1.8)
