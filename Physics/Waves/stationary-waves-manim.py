"""
stationary-waves-manim.py — two scenes for [[Stationary Waves]].

Scene 1  TwoBecomeOne — a wave travelling right (blue) and its reflection travelling left
                        (red) drawn live with their sum (purple): the sum stops travelling;
                        grey node dots never move, antinodes swing to twice the amplitude.
Scene 2  StringModes  — a string fixed at both ends, driven at f1, 2f1, 3f1: the loops
                        appear one by one, and two tracked beads show in-phase motion within
                        a loop and antiphase motion across a node.

Smoke:   manim -ql --fps 15 stationary-waves-manim.py TwoBecomeOne StringModes
Final:   manim -qk stationary-waves-manim.py TwoBecomeOne StringModes
then concat with ffmpeg to stationary-waves-manim.mp4 and rm -rf media __pycache__.
"""
from manim import *
import numpy as np

GREY = "#888888"
BLUE, RED, GREEN, AMBER, PURPLE = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed"
LAM, PERIOD, A = 3.0, 2.0, 0.6


class TwoBecomeOne(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("Two equal waves, opposite directions — the sum stops travelling", font_size=30, color=GREY).to_edge(UP, buff=0.3)
        self.play(FadeIn(title))
        k, w = 2 * PI / LAM, 2 * PI / PERIOD
        t = ValueTracker(0.0)
        xs = np.linspace(-6.4, 4.6, 400)

        def curve(fn, col, y0, width=2.5):
            return always_redraw(lambda: VMobject(color=col, stroke_width=width).set_points_smoothly(
                [[x, y0 + fn(x, t.get_value()), 0] for x in xs]))

        y_top, y_mid, y_bot = 2.1, 0.6, -1.5
        f1 = lambda x, tt: A * np.sin(k * x - w * tt)
        f2 = lambda x, tt: A * np.sin(k * x + w * tt)
        fs = lambda x, tt: f1(x, tt) + f2(x, tt)
        c1 = curve(f1, BLUE, y_top); c2 = curve(f2, RED, y_mid); cs = curve(fs, PURPLE, y_bot, 3.5)
        l1 = Text("travelling\nright", font_size=17, color=BLUE, line_spacing=0.8).move_to([5.8, y_top, 0])
        l2 = Text("travelling left\n(the reflection)", font_size=17, color=RED, line_spacing=0.8).move_to([5.8, y_mid, 0])
        ls = Text("their sum", font_size=17, color=PURPLE).move_to([5.8, y_bot, 0])
        for y in (y_top, y_mid, y_bot):
            self.add(Line([-6.4, y, 0], [4.6, y, 0], color=GREY, stroke_width=1, stroke_opacity=0.5))
        self.add(c1, c2, cs)
        self.play(FadeIn(l1), FadeIn(l2), FadeIn(ls), run_time=0.5)
        # node dots on the sum: where sin kx = 0
        nodes = VGroup(*[Dot([x, y_bot, 0], radius=0.07, color=GREY) for x in np.arange(-6, 4.6, LAM / 2)])
        self.play(t.animate.set_value(PERIOD), run_time=4.0, rate_func=linear)
        self.play(FadeIn(nodes), run_time=0.4)
        cap = Text("grey dots: nodes, always zero  ·  between them: antinodes, swinging to 2A  ·  nothing moves sideways",
                   font_size=18, color=GREY).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(cap), run_time=0.4)
        self.play(t.animate.set_value(3.5 * PERIOD), run_time=10.0, rate_func=linear)
        self.wait(0.5)


class StringModes(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("A string fixed at both ends: only L = nλ/2 survives", font_size=30, color=GREY).to_edge(UP, buff=0.3)
        self.play(FadeIn(title))
        L = 10.0; x0 = -5.0
        xs = np.linspace(0, L, 300)
        t = ValueTracker(0.0)
        n = ValueTracker(1.0)
        amp = 1.1
        wall_l = Line([x0, -1.2, 0], [x0, 1.2, 0], color=GREY, stroke_width=6)
        wall_r = Line([x0 + L, -1.2, 0], [x0 + L, 1.2, 0], color=GREY, stroke_width=6)
        self.add(wall_l, wall_r)

        def shape():
            nn = n.get_value(); tt = t.get_value()
            f = nn * 0.5                                    # f_n = n f1, f1 = 0.5 Hz in scene time
            return VMobject(color=BLUE, stroke_width=3.5).set_points_smoothly(
                [[x0 + x, amp * np.sin(nn * PI * x / L) * np.cos(2 * PI * f * tt), 0] for x in xs])
        string = always_redraw(shape)
        self.add(string)
        env = always_redraw(lambda: VGroup(
            VMobject(color=BLUE, stroke_width=1, stroke_opacity=0.35).set_points_smoothly([[x0 + x, amp * np.sin(n.get_value() * PI * x / L), 0] for x in xs]),
            VMobject(color=BLUE, stroke_width=1, stroke_opacity=0.35).set_points_smoothly([[x0 + x, -amp * np.sin(n.get_value() * PI * x / L), 0] for x in xs])))
        self.add(env)
        # two tracked beads: same loop, then across a node (for n = 2)
        def bead(xf, col):
            return always_redraw(lambda: Dot([x0 + xf * L, amp * np.sin(n.get_value() * PI * xf) * np.cos(2 * PI * n.get_value() * 0.5 * t.get_value()), 0], radius=0.11, color=col))
        b1 = bead(0.20, AMBER); b2 = bead(0.30, AMBER); b3 = bead(0.70, GREEN)
        self.add(b1, b2, b3)
        cap = Text("n = 1, the first harmonic: one loop, f₁ = v / 2L", font_size=22, color=GREY).move_to([0, -2.0, 0])
        cap2 = Text("", font_size=18, color=GREY).to_edge(DOWN, buff=0.3)
        self.add(cap2)
        self.play(FadeIn(cap))
        self.play(t.animate.set_value(3.0), run_time=4.0, rate_func=linear)
        for nn, lab, note in ((2, "n = 2: two loops, f = 2f₁", "amber beads in one loop move together; the green bead across the node moves opposite"),
                              (3, "n = 3: three loops, f = 3f₁", "every point in a loop is in phase; adjacent loops are in antiphase; nodes never move")):
            newcap = Text(lab, font_size=22, color=GREY).move_to([0, -2.0, 0])
            newcap2 = Text(note, font_size=18, color=GREY).to_edge(DOWN, buff=0.3)
            self.play(n.animate.set_value(nn), Transform(cap, newcap), Transform(cap2, newcap2), run_time=1.2)
            self.play(t.animate.set_value(t.get_value() + 3.0), run_time=4.5, rate_func=linear)
        self.wait(0.6)
