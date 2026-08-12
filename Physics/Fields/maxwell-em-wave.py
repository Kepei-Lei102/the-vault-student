"""The self-carrying ripple: a plane electromagnetic wave in 3D.

E (blue, vertical) and B (teal, horizontal) perpendicular to each other
and to the direction of travel, in phase, propagating at c. Captions are
pre-registered fixed-in-frame at opacity 0 and swapped via opacity
animations (the ThreeDScene flicker lesson).

Render (from this folder):
    manim -qm maxwell-em-wave.py EMWave   # smoke
    manim -qk maxwell-em-wave.py EMWave   # 4K final
Copy the output beside the card as maxwell-em-wave.mp4, then clear
media/ + __pycache__/.
"""

import numpy as np
from manim import *

BG = "#1a1a1a"
GRAY = "#9a9a9a"
BLUE = "#2563eb"
TEAL = "#0891b2"
AMBER = "#f59e0b"

config.background_color = BG

A = 1.35          # field amplitude (scene units)
K = 1.6           # wavenumber
OMEGA = 1.9       # angular frequency
XMIN, XMAX = -5.2, 5.2
N_ARROWS = 27


class EMWave(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=72 * DEGREES, theta=-68 * DEGREES,
                                    zoom=0.82)

        axis = Line3D([XMIN - 0.4, 0, 0], [XMAX + 0.9, 0, 0], color=GRAY,
                      thickness=0.012)

        tr = ValueTracker(0.0)

        def phase(x):
            return A * np.sin(K * x - OMEGA * tr.get_value())

        def e_curve():
            return ParametricFunction(
                lambda x: np.array([x, phase(x), 0.0]),
                t_range=[XMIN, XMAX], color=BLUE, stroke_width=4.5)

        def b_curve():
            return ParametricFunction(
                lambda x: np.array([x, 0.0, phase(x)]),
                t_range=[XMIN, XMAX], color=TEAL, stroke_width=4.5)

        def e_arrows():
            g = VGroup()
            for x in np.linspace(XMIN, XMAX, N_ARROWS):
                v = phase(x)
                if abs(v) > 0.06:
                    g.add(Line([x, 0, 0], [x, v, 0], color=BLUE,
                               stroke_width=2.6, stroke_opacity=0.75))
            return g

        def b_arrows():
            g = VGroup()
            for x in np.linspace(XMIN, XMAX, N_ARROWS):
                v = phase(x)
                if abs(v) > 0.06:
                    g.add(Line([x, 0, 0], [x, 0, v], color=TEAL,
                               stroke_width=2.6, stroke_opacity=0.75))
            return g

        Ec = always_redraw(e_curve)
        Bc = always_redraw(b_curve)
        Ea = always_redraw(e_arrows)
        Ba = always_redraw(b_arrows)

        # fixed-in-frame legend + captions, ALL pre-registered at opacity 0
        legend = VGroup(
            Text("E — electric field", font_size=26, color=BLUE, weight=BOLD),
            Text("B — magnetic field", font_size=26, color=TEAL, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_corner(UL, buff=0.5)

        caps = [
            Text("perpendicular to each other — and to the direction of travel",
                 font_size=27, color=GRAY),
            Text("in phase: E and B crest together (no taking turns)",
                 font_size=27, color=GRAY),
            Text("each field's change regenerates the other — the ripple carries itself",
                 font_size=27, color=AMBER),
            Text("speed locked by two bench constants:  1/√(μ₀ε₀) = 3.00 × 10⁸ m/s — light",
                 font_size=27, color=BLUE),
        ]
        for c in caps:
            c.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(legend, *caps)
        legend.set_opacity(0)
        for c in caps:
            c.set_opacity(0)

        self.add(axis, Ea, Ba, Ec, Bc)
        self.play(legend.animate.set_opacity(1), run_time=0.8)

        def show(i, prev=None, rt=0.5):
            anims = [caps[i].animate.set_opacity(1)]
            if prev is not None:
                anims.append(caps[prev].animate.set_opacity(0))
            self.play(*anims, run_time=rt)

        self.begin_ambient_camera_rotation(rate=0.014)

        show(0)
        self.play(tr.animate.set_value(6), run_time=6, rate_func=linear)
        show(1, prev=0)
        self.play(tr.animate.set_value(12), run_time=6, rate_func=linear)
        show(2, prev=1)
        self.play(tr.animate.set_value(18), run_time=6, rate_func=linear)
        show(3, prev=2)
        self.play(tr.animate.set_value(24.5), run_time=6.5, rate_func=linear)
        self.stop_ambient_camera_rotation()
        self.wait(0.6)
