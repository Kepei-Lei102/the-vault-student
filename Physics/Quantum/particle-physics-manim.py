"""Manim companion for Particle Physics.md.

    manim -qk particle-physics-manim.py BetaDecay      (4K; copy the MP4 to particle-physics-beta-decay.mp4)

A neutron's three quark lines run left to right. One down quark turns into an up quark and throws off a W⁻; the W⁻
lives for a moment and becomes an electron and an antineutrino. The bookkeeping is checked on screen at both vertices:
charge, baryon number and electron number before and after. Then the same diagram is read for β⁺ decay by swapping
the roles, which is why one picture is the whole of 9702 11.2.5.
"""
from manim import *
import numpy as np

BLUE_, RED_, AMBER_, GREEN_, PURPLE_, GREY_ = "#60a5fa", "#f87171", "#fbbf24", "#34d399", "#c4b5fd", "#9ca3af"


def wavy(p, q, n=7, amp=0.12, color=AMBER_):
    p, q = np.array(p), np.array(q); d = q - p; L = np.linalg.norm(d); u = d / L; nrm = np.array([-u[1], u[0], 0])
    pts = [p + u * L * t + nrm * amp * np.sin(2 * np.pi * n * t) for t in np.linspace(0, 1, 120)]
    return VMobject(color=color, stroke_width=4).set_points_smoothly(pts)


class BetaDecay(Scene):
    def construct(self):
        self.camera.background_color = "#0b0f19"
        title = Text("β⁻ decay, one quark at a time", font_size=40, color=WHITE).to_edge(UP, buff=0.3)
        self.play(FadeIn(title))
        ys = [-1.6, -0.6, 0.4]; x0, xv, x1 = -5.5, -1.0, 4.5
        labels_in = ["u", "d", "d"]; labels_out = ["u", "d", "u"]; cols = [PURPLE_, PURPLE_, RED_]
        lines_in = VGroup(*[Line([x0, y, 0], [xv, y, 0], color=c, stroke_width=4) for y, c in zip(ys, cols)])
        tags_in = VGroup(*[Text(l, font_size=30, color=c).next_to(ln, LEFT, buff=0.15) for l, ln, c in zip(labels_in, lines_in, cols)])
        n_lab = Text("neutron (udd)", font_size=26, color=GREY_).next_to(lines_in, UP, buff=0.25).shift(LEFT*1.0)
        cap = Text("A neutron: two down quarks and an up quark, travelling in time from left to right.", font_size=24, color=GREY_).to_edge(DOWN, buff=0.25)
        self.play(*[Create(l) for l in lines_in], FadeIn(tags_in), FadeIn(n_lab), FadeIn(cap)); self.wait(0.8)

        # the vertex: d -> u + W-
        vertex = Dot([xv, ys[2], 0], radius=0.09, color=WHITE)
        lines_out = VGroup(*[Line([xv, y, 0], [x1, y, 0], color=c, stroke_width=4) for y, c in zip(ys, cols)])
        tags_out = VGroup(*[Text(l, font_size=30, color=c).next_to(ln, RIGHT, buff=0.15) for l, ln, c in zip(labels_out, lines_out, cols)])
        p_lab = Text("proton (uud)", font_size=26, color=GREY_).next_to(lines_out, UP, buff=0.25).shift(RIGHT*1.0)
        cap2 = Text("At one point the down quark becomes an up quark. Charge −1/3 became +2/3: something carried away −1.", font_size=24, color=GREY_).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(vertex), *[Create(l) for l in lines_out], FadeIn(tags_out), FadeIn(p_lab), FadeOut(cap), FadeIn(cap2)); self.wait(0.8)
        w = wavy([xv, ys[2], 0], [1.2, 2.2, 0]); w_lab = Text("W⁻", font_size=30, color=AMBER_).next_to(w, LEFT, buff=0.1).shift(UP*0.4)
        cap3 = Text("That something is a W⁻ boson: charge −1, mass 80 GeV, borrowed for 10⁻²⁵ s.", font_size=24, color=GREY_).to_edge(DOWN, buff=0.25)
        self.play(Create(w), FadeIn(w_lab), FadeOut(cap2), FadeIn(cap3)); self.wait(0.8)
        v2 = Dot([1.2, 2.2, 0], radius=0.09, color=WHITE)
        e_line = Line([1.2, 2.2, 0], [4.5, 2.9, 0], color=BLUE_, stroke_width=4); e_lab = Text("e⁻", font_size=30, color=BLUE_).next_to(e_line, RIGHT, buff=0.1)
        nu_line = Line([4.5, 1.5, 0], [1.2, 2.2, 0], color=BLUE_, stroke_width=4).add_tip(tip_length=0.2); nu_lab = Text("ν̄ₑ", font_size=30, color=BLUE_).next_to([4.6, 1.5, 0], RIGHT, buff=0.1)
        cap4 = Text("The W⁻ becomes an electron and an antineutrino. The backwards arrow is how a diagram writes 'anti'.", font_size=24, color=GREY_).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(v2), Create(e_line), FadeIn(e_lab), Create(nu_line), FadeIn(nu_lab), FadeOut(cap3), FadeIn(cap4)); self.wait(1.0)

        # bookkeeping
        book = VGroup(
            Text("charge:        −1/3  →  +2/3 + (−1)     ✓", font_size=24, color=GREEN_),
            Text("baryon number:   1   →   1  + 0        ✓", font_size=24, color=GREEN_),
            Text("electron number: 0   →   0  + (+1) + (−1) ✓", font_size=24, color=GREEN_),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).scale(0.85).move_to([-2.4, -2.35, 0])
        cap5 = Text("Every vertex balances the books. Nothing else is allowed to happen.", font_size=24, color=GREY_).to_edge(DOWN, buff=0.25)
        self.play(FadeOut(cap4), FadeIn(cap5), LaggedStart(*[FadeIn(b, shift=RIGHT*0.2) for b in book], lag_ratio=0.3)); self.wait(1.4)

        # beta-plus: swap
        cap6 = Text("β⁺ decay is the same picture with u → d and a W⁺ that becomes e⁺ and νₑ. One diagram, both decays.", font_size=23, color=GREY_).to_edge(DOWN, buff=0.25)
        new_in = [Text(l, font_size=30, color=c).move_to(t) for l, t, c in zip(["u", "d", "u"], tags_in, [PURPLE_, PURPLE_, RED_])]
        new_out = [Text(l, font_size=30, color=c).move_to(t) for l, t, c in zip(["u", "d", "d"], tags_out, [PURPLE_, PURPLE_, RED_])]
        self.play(FadeOut(cap5), FadeIn(cap6), *[Transform(a, b) for a, b in zip(tags_in, new_in)], *[Transform(a, b) for a, b in zip(tags_out, new_out)],
                  Transform(n_lab, Text("proton (uud)", font_size=26, color=GREY_).move_to(n_lab)), Transform(p_lab, Text("neutron (udd)", font_size=26, color=GREY_).move_to(p_lab)),
                  Transform(w_lab, Text("W⁺", font_size=30, color=AMBER_).move_to(w_lab)), Transform(e_lab, Text("e⁺", font_size=30, color=BLUE_).move_to(e_lab)), Transform(nu_lab, Text("νₑ", font_size=30, color=BLUE_).move_to(nu_lab)),
                  FadeOut(book), run_time=1.5)
        self.wait(2.0)
