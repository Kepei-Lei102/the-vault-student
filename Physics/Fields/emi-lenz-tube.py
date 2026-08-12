"""The copper-tube race: free fall vs Lenz braking, side by side.

Render (from this folder):
    manim -qm emi-lenz-tube.py LenzTube    # smoke
    manim -qk emi-lenz-tube.py LenzTube    # 4K final
Copy the output beside the card as emi-lenz-tube.mp4, then clear
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

config.background_color = BG

TOP = 2.6
BOT = -2.4


def magnet_at(x, y):
    m = VGroup(
        Rectangle(width=0.62, height=0.4, stroke_color=BLUE, stroke_width=2.5,
                  fill_color=BLUE, fill_opacity=0.25),
        Text("N", font_size=17, color=GRAY, weight=BOLD),
    )
    m[1].move_to(m[0])
    m.move_to(np.array([x, y, 0]))
    return m


class LenzTube(Scene):
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=25, color=color).to_edge(DOWN, buff=0.32)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.25), FadeIn(cap, run_time=0.35))
        else:
            self.play(FadeIn(cap, run_time=0.35))
        self._cap = cap

    def construct(self):
        x_air, x_tube = -2.7, 2.7

        title_a = Text("free air", font_size=24, color=GRAY, weight=BOLD).move_to(np.array([x_air, 3.3, 0]))
        title_t = Text("copper tube", font_size=24, color=AMBER, weight=BOLD).move_to(np.array([x_tube, 3.3, 0]))

        wall1 = Rectangle(width=0.22, height=TOP - BOT + 0.6, stroke_width=0,
                          fill_color=GRAY, fill_opacity=0.35).move_to(np.array([x_tube - 0.62, (TOP + BOT) / 2, 0]))
        wall2 = wall1.copy().move_to(np.array([x_tube + 0.62, (TOP + BOT) / 2, 0]))
        floor = Line(np.array([-4.2, BOT - 0.35, 0]), np.array([4.2, BOT - 0.35, 0]),
                     color=GRAY, stroke_width=2.5)

        # progress trackers: 0 at top, 1 at bottom
        pa = ValueTracker(0.0)
        pt = ValueTracker(0.0)

        def y_of(p):
            return TOP + (BOT - TOP) * p

        mag_a = always_redraw(lambda: magnet_at(x_air, y_of(min(pa.get_value(), 1.0))))
        mag_t = always_redraw(lambda: magnet_at(x_tube, y_of(min(pt.get_value(), 1.0))))

        def eddies():
            y = y_of(min(pt.get_value(), 1.0))
            up = Ellipse(width=1.5, height=0.3, stroke_color=RED, stroke_width=2.5,
                         stroke_opacity=0.9, fill_opacity=0).move_to(np.array([x_tube, y + 0.62, 0]))
            dn = Ellipse(width=1.5, height=0.3, stroke_color=RED, stroke_width=2.5,
                         stroke_opacity=0.9, fill_opacity=0).move_to(np.array([x_tube, y - 0.62, 0]))
            drag = Arrow(np.array([x_tube + 1.05, y - 0.25, 0]), np.array([x_tube + 1.05, y + 0.55, 0]),
                         color=GREEN, stroke_width=3.5, tip_length=0.16, buff=0)
            lab = Text("drag", font_size=16, color=GREEN).next_to(drag, RIGHT, buff=0.08)
            return VGroup(up, dn, drag, lab)
        eddies_m = always_redraw(eddies)

        self.play(FadeIn(title_a), FadeIn(title_t), FadeIn(wall1), FadeIn(wall2),
                  FadeIn(floor), run_time=0.8)
        self.add(mag_a, mag_t)
        self.swap_caption("two identical magnets, released together")
        self.wait(0.6)
        self.add(eddies_m)

        # the race: air magnet falls in ~1.1 s (accelerating), tube magnet crawls
        self.play(
            pa.animate(rate_func=rate_functions.ease_in_quad).set_value(1.0),
            pt.animate(rate_func=linear).set_value(0.22),
            run_time=1.15,
        )
        self.play(Flash(np.array([x_air, BOT - 0.15, 0]), color=BLUE, flash_radius=0.5),
                  pt.animate.set_value(0.34), run_time=0.5, rate_func=linear)
        self.swap_caption("the tube magnet is STILL going — its changing flux swirls eddy currents", color=RED)
        self.play(pt.animate.set_value(0.62), run_time=1.8, rate_func=linear)
        self.swap_caption("Lenz: the eddies' field opposes the change — a drag with no contact", color=GREEN)
        self.play(pt.animate.set_value(0.9), run_time=1.8, rate_func=linear)
        self.play(pt.animate.set_value(1.0), run_time=0.7, rate_func=linear)
        self.swap_caption("no friction anywhere — the fall was fought by induction alone")
        self.wait(1.6)
