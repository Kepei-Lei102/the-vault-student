"""Manim: the odometer — why the arc-length integral works.

Act 1  A winding road. One chord is the map's ruler (the crow's flight) and it
       lies short. Double the chords — 2, 4, 8, 16, 32, 64 — and the chord total
       climbs, from below, onto the road's true length.
Act 2  Magnify one strip. As dx shrinks the blue arc flattens onto its green
       chord and dy/dx settles onto the tangent slope: Pythagoras on the chord,
       factor dx out of the root, add every chord, let dx -> 0 — the sum
       becomes the integral, and the integral is the number the chords were
       climbing to.

Every point is computed from f; nothing is placed by eye.

Render (from this folder):
    manim -ql arc-length-odometer.py ArcLengthOdometer    # smoke (480p15)
    manim -qk arc-length-odometer.py ArcLengthOdometer    # 4K final
Copy media/videos/arc-length-odometer/2160p60/ArcLengthOdometer.mp4
  -> arc-length-odometer.mp4 beside the card, then rm -rf media/ __pycache__/.
"""

import numpy as np
from manim import (
    Scene, VGroup, VMobject, Axes, Text, MathTex, Dot, Line, Rectangle,
    DecimalNumber, Integer, ValueTracker, always_redraw,
    FadeIn, FadeOut, Transform, Create, Write, ChangeDecimalToValue, Indicate,
    UP, DOWN, LEFT, RIGHT, UL, DR, config,
)

BG = "#1e1e1e"
TXT = "#cccccc"
GREY = "#9a9a9a"
BLUE = "#2563eb"     # the curve
GREEN = "#059669"    # the chords / ds
AMBER = "#f59e0b"    # dx
RED = "#dc2626"      # dy
FONT = "Helvetica Neue"

config.background_color = BG

A, B = 0.0, 4.0


def f(x):
    return 1.6 + 0.9 * np.sin(1.4 * x - 0.4) + 0.1 * x


def fp(x):
    return 1.26 * np.cos(1.4 * x - 0.4) + 0.1


_xs = np.linspace(A, B, 200001)
TRUE_LEN = float(np.trapezoid(np.sqrt(1.0 + fp(_xs) ** 2), _xs))


def chord_points(n):
    xs = np.linspace(A, B, n + 1)
    return xs, f(xs)


def chord_total(n):
    xs, ys = chord_points(n)
    return float(np.sum(np.hypot(np.diff(xs), np.diff(ys))))


STAGES = [1, 2, 4, 8, 16, 32, 64]
X0 = 1.0          # the strip magnified in Act 2 (f' = 0.75 there, gentle bow)
H_START, H_END = 0.7, 0.04
W = 4.0           # on-screen width of the magnified strip


def note(s, size=24, color=GREY):
    return Text(s, font=FONT, font_size=size, color=color)


class ArcLengthOdometer(Scene):
    def construct(self):
        # ------------------------------------------------------------ Act 1
        title = Text("How long is the road?", font=FONT, font_size=40, color=TXT)
        title.to_edge(UP, buff=0.35)

        ax = Axes(
            x_range=[0, 4.4, 1], y_range=[0, 3.2, 1],
            x_length=7.2, y_length=4.6,
            axis_config={"color": GREY, "stroke_width": 2,
                         "include_ticks": False, "include_tip": False},
        ).to_edge(LEFT, buff=0.6).shift(DOWN * 0.45)

        curve = ax.plot(f, x_range=[A, B], color=BLUE, stroke_width=5)
        xpk = _xs[np.argmax(f(_xs))]
        road_lab = note("the road  y = f(x)", 26, BLUE)
        road_lab.move_to(ax.c2p(xpk, f(xpk) + 0.45))

        self.play(FadeIn(title), Create(ax), run_time=1.0)
        self.play(Create(curve), FadeIn(road_lab), run_time=1.6)

        # right-hand readout
        n_lab = note("chords:", 30, TXT)
        n_num = Integer(1, color=GREEN, font_size=44)
        n_num.add_updater(lambda m: m.next_to(n_lab, RIGHT, buff=0.25))
        n_row = VGroup(n_lab, n_num)
        tot_lab = note("total length of the chords", 26, TXT)
        tot_num = DecimalNumber(chord_total(1), num_decimal_places=3,
                                color=GREEN, font_size=44)
        tot_row = VGroup(tot_lab, tot_num).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        true_lab = note("the road's true length", 26, TXT)
        true_num = DecimalNumber(TRUE_LEN, num_decimal_places=3,
                                 color=BLUE, font_size=44)
        true_row = VGroup(true_lab, true_num).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        panel = VGroup(n_row, tot_row, true_row).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        panel.to_edge(RIGHT, buff=0.8).shift(UP * 0.6)

        caption = note("one chord: the map's ruler, as the crow flies — it lies short", 26, TXT)
        caption.to_edge(DOWN, buff=0.45)

        def make_poly(n):
            xs, ys = chord_points(n)
            poly = VMobject(color=GREEN, stroke_width=4)
            poly.set_points_as_corners([ax.c2p(x, y) for x, y in zip(xs, ys)])
            dots = VGroup(*[Dot(ax.c2p(x, y), radius=0.055, color=AMBER)
                            for x, y in zip(xs, ys)])
            return poly, dots

        poly, dots = make_poly(1)
        self.play(Create(poly), FadeIn(dots), FadeIn(n_row), FadeIn(tot_row),
                  FadeIn(caption), run_time=1.2)
        self.wait(1.2)

        cap2 = note("double the chords — every chord hugs the road tighter, and the total climbs", 26, TXT)
        cap2.to_edge(DOWN, buff=0.45)
        self.play(Transform(caption, cap2), run_time=0.6)

        for n in STAGES[1:]:
            new_poly, new_dots = make_poly(n)
            anims = [Transform(poly, new_poly), FadeOut(dots), FadeIn(new_dots),
                     ChangeDecimalToValue(tot_num, chord_total(n)),
                     n_num.animate.set_value(n)]
            if n == 8:
                anims.append(FadeIn(true_row))
            self.play(*anims, run_time=1.0)
            dots = new_dots
            self.wait(0.55)

        cap3 = note("a chord is never longer than its arc: the totals climb from below and never overshoot", 26, TXT)
        cap3.to_edge(DOWN, buff=0.45)
        self.play(Transform(caption, cap3), Indicate(tot_num, color=GREEN, scale_factor=1.15),
                  Indicate(true_num, color=BLUE, scale_factor=1.15), run_time=1.2)
        self.wait(1.6)

        # ------------------------------------------------------------ Act 2
        pic = VGroup(ax, curve, road_lab, poly, dots)
        title2 = Text("Why does the sum become an integral?  Magnify one strip.",
                      font=FONT, font_size=30, color=TXT)
        title2.to_edge(UP, buff=0.3).set_x(1.0)
        self.play(FadeOut(panel), FadeOut(caption), FadeOut(title),
                  pic.animate.scale(0.42).to_corner(UL, buff=0.3), run_time=1.4)
        self.play(FadeIn(title2), run_time=0.6)

        h = ValueTracker(H_START)
        O = np.array([-5.8, -3.25, 0.0])

        def mag(x):
            hv = h.get_value()
            return O + np.array([W * (x - X0) / hv, W * (f(x) - f(X0)) / hv, 0.0])

        def top():
            return mag(X0 + h.get_value())

        def arc_pts():
            return [mag(x) for x in np.linspace(X0, X0 + h.get_value(), 48)]

        def above_arc(frac, gap=0.45):
            """a point `gap` above the magnified arc at `frac` of the strip width"""
            pts = arc_pts()
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            xq = O[0] + frac * W
            return np.array([xq, float(np.interp(xq, xs, ys)) + gap, 0.0])

        def strip_box():
            xs = np.linspace(X0, X0 + h.get_value(), 50)
            ys = f(xs)
            lo = ax.c2p(xs[0], ys.min())
            hi = ax.c2p(xs[-1], ys.max())
            return Rectangle(width=hi[0] - lo[0] + 0.12, height=hi[1] - lo[1] + 0.12,
                             color=AMBER, stroke_width=2.5).move_to((lo + hi) / 2)

        zoom_box = always_redraw(strip_box)
        arc = always_redraw(lambda: VMobject(color=BLUE, stroke_width=7)
                            .set_points_smoothly(arc_pts()))
        chord = always_redraw(lambda: Line(O, top(), color=GREEN, stroke_width=5))
        base = Line(O, O + W * RIGHT, color=AMBER, stroke_width=5)
        rise = always_redraw(lambda: Line(O + W * RIGHT, top(), color=RED, stroke_width=5))

        dx_lab = MathTex(r"\Delta x", color=AMBER, font_size=42).next_to(base, DOWN, buff=0.18)
        dy_lab = always_redraw(lambda: MathTex(r"\Delta y", color=RED, font_size=42)
                               .next_to(rise, RIGHT, buff=0.18))
        ds_lab = always_redraw(lambda: MathTex(r"\Delta s", color=GREEN, font_size=42)
                               .move_to(above_arc(0.62)))
        # hang the label above-left of the arc: its bottom-right corner sits just above
        # the arc at 30% of the strip, and the arc only falls away to the left of that
        arc_lab = always_redraw(lambda: note("the curve", 24, BLUE)
                                .move_to(above_arc(0.30, 0.22), aligned_edge=DR))
        strip_note = note("this strip, magnified", 22, AMBER)
        strip_note.next_to(pic, DOWN, buff=0.15)

        self.play(Create(zoom_box), FadeIn(strip_note), run_time=0.6)
        self.play(FadeIn(base), FadeIn(dx_lab), Create(arc), Create(chord), Create(rise),
                  FadeIn(dy_lab), FadeIn(ds_lab), FadeIn(arc_lab), run_time=1.4)

        cap = note("shrink Δx — the arc flattens onto its chord; Δy/Δx settles onto the tangent slope", 22, TXT)
        cap.next_to(title2, DOWN, buff=0.18).set_x(1.0)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(0.6)
        self.play(h.animate.set_value(H_END), run_time=4.5)
        self.remove(arc_lab)

        cap_b = note("the arc–chord gap dies like Δx², the chord only like Δx:\n"
                     "summed over 1/Δx chords, the total error → 0.  That is why it works.", 22, TXT)
        cap_b.next_to(title2, DOWN, buff=0.18).set_x(1.0)
        self.play(Transform(cap, cap_b), run_time=0.7)
        self.wait(2.2)

        # the algebra — three rows; the first row rewrites itself in place
        # pieces are split where LaTeX compiles standalone; glyph slices inside the
        # roots were verified against an index-labelled still (sqrt, bar, then glyphs)
        L1 = MathTex(r"\Delta s", r"\approx", r"\sqrt{\Delta x^{2} + \Delta y^{2}}",
                     font_size=38, color=TXT)
        L1[0].set_color(GREEN); L1[2][2:4].set_color(AMBER); L1[2][6:8].set_color(RED)
        L2 = MathTex(r"\Delta s", r"\approx", r"\sqrt{1 + \left(\tfrac{\Delta y}{\Delta x}\right)^{2}}",
                     r"\;\Delta x", font_size=38, color=TXT)
        L2[0].set_color(GREEN); L2[2][5:7].set_color(RED); L2[2][8:10].set_color(AMBER); L2[3].set_color(AMBER)
        L3 = MathTex(r"s \approx \sum", r"\sqrt{1 + \left(\tfrac{\Delta y}{\Delta x}\right)^{2}}",
                     r"\;\Delta x", font_size=38, color=TXT)
        L3[1][5:7].set_color(RED); L3[1][8:10].set_color(AMBER); L3[2].set_color(AMBER)
        L4 = MathTex(r"s = \int_{a}^{b}", r"\sqrt{1 + \left(\tfrac{dy}{dx}\right)^{2}}",
                     r"\;dx", font_size=38, color=GREEN)
        L4[1][5:7].set_color(RED); L4[1][8:10].set_color(AMBER); L4[2].set_color(AMBER)
        n1 = note("Pythagoras on the chord", 21)
        n2 = note("factor Δx out of the root", 21)
        n3 = note("add every chord — Act 1", 21)
        n4 = note("Δx → 0:  Σ becomes ∫,  Δy/Δx becomes dy/dx", 21)

        final = MathTex(r"\int_{0}^{4}\sqrt{1 + f'(x)^{2}}\,dx = " + f"{TRUE_LEN:.3f}",
                        font_size=38, color=BLUE)
        final_note = note("— the number the chords were climbing to", 21, TXT)
        fin = VGroup(final, final_note).arrange(DOWN, aligned_edge=LEFT, buff=0.08)

        R1 = VGroup(L2, n2).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        R2 = VGroup(L3, n3).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        R3 = VGroup(L4, n4).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        rows = VGroup(R1, R2, R3).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        block = VGroup(rows, fin).arrange(DOWN, aligned_edge=LEFT, buff=0.34)
        # fit the block into the box right of the triangle and below the caption — computed, not eyeballed
        box_top = cap_b.get_bottom()[1] - 0.3
        box_bottom = -3.75
        box_left, box_right = -0.7, 7.1 - 0.5
        scale = min(1.0, (box_top - box_bottom) / block.height, (box_right - box_left) / block.width)
        block.scale(scale)
        block.next_to(cap_b, DOWN, buff=0.3).align_to(np.array([box_right, 0, 0]), RIGHT)
        L1.scale(scale).align_to(L2, LEFT).align_to(L2, UP)
        n1.scale(scale).align_to(n2, LEFT).align_to(n2, UP)

        self.play(Write(L1), FadeIn(n1), Indicate(base, color=AMBER), Indicate(rise, color=RED), run_time=1.4)
        self.wait(1.0)
        self.play(Transform(L1, L2), Transform(n1, n2), run_time=1.2)
        self.wait(1.0)
        self.play(Write(R2), Indicate(poly, color=GREEN, scale_factor=1.05), run_time=1.4)
        self.wait(1.0)
        self.play(Write(R3), run_time=1.4)
        self.wait(1.0)

        self.play(Write(final), FadeIn(final_note), run_time=1.4)
        self.wait(1.0)

        tag = Text("The odometer is an integral.", font=FONT, font_size=36, color=GREEN)
        tag.move_to(title2)
        self.play(Transform(title2, tag), run_time=0.8)
        self.wait(2.5)
