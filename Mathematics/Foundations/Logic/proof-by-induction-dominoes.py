"""Proof by Induction — the domino argument, staged honestly.

Beat 1: both pillars — the base pushes, the step relays, everything falls.
Beat 2: no base case — "n = n+1": a flawless relay that nothing ever pushes.
Beat 3: one broken step — the cascade dies at the gap; all beyond it survives.

Render:  manim -qk proof-by-induction-dominoes.py InductionDominoes
House style: bg #1a1a1a, captions #9a9a9a, green = proven truth, amber = the push.
Deterministic — no seed stamp.
"""

from manim import *

BG = "#1a1a1a"
GRAYT = "#9a9a9a"
GREEN = "#059669"
AMBER = "#f59e0b"
RED = "#dc2626"

config.background_color = BG

BASE_Y = -0.4          # dominoes stand on this line
DOM_H = 1.2
DOM_W = 0.16
LEAN = -34 * DEGREES   # resting lean when caught by the next domino
FLAT = -85 * DEGREES   # nothing to catch it


class InductionDominoes(Scene):
    def swap_caption(self, text, color=GRAYT, font_size=30):
        cap = Text(text, color=color, font_size=font_size, line_spacing=0.9)
        cap.move_to(DOWN * 3.35)
        anims = [FadeIn(cap, run_time=0.35)]
        if getattr(self, "_cap", None) is not None:
            anims.append(FadeOut(self._cap, run_time=0.25))
        self._cap = cap
        self.play(*anims)

    def make_row(self, xs, labels=True):
        doms, labs = VGroup(), VGroup()
        for i, x in enumerate(xs):
            d = Rectangle(width=DOM_W, height=DOM_H)
            d.set_stroke(GRAYT, 2.5).set_fill(GRAYT, 0.15)
            d.move_to([x, BASE_Y + DOM_H / 2, 0])
            doms.add(d)
            if labels:
                t = Text(f"P({i + 1})", color=GRAYT, font_size=17)
                t.move_to([x, BASE_Y - 0.32, 0])
                labs.add(t)
        return doms, labs

    def push_arrow(self, x0):
        return Arrow([x0 - 1.0, 1.15, 0], [x0 - 0.12, 0.62, 0], buff=0,
                     color=AMBER, stroke_width=4,
                     max_tip_length_to_length_ratio=0.22)

    def construct(self):
        self.beat_both_pillars()
        self.beat_no_base()
        self.beat_broken_step()

    # ------------------------------------------------------------------
    def beat_both_pillars(self):
        xs = [-3.1 + 0.6 * i for i in range(10)]
        doms, labs = self.make_row(xs)
        self.play(FadeIn(doms), FadeIn(labs), run_time=1.0)
        self.swap_caption("a claim for every n is infinitely many claims —\none domino per case")
        self.wait(1.8)

        push = self.push_arrow(xs[0])
        self.swap_caption("pillar one, the base: prove P(1) —\npush the first domino")
        self.play(Create(push), run_time=0.6)
        self.play(Rotate(doms[0], LEAN, about_point=doms[0].get_corner(DR)),
                  labs[0].animate.set_color(GREEN),
                  FadeOut(push), run_time=0.7)

        self.swap_caption("pillar two, the step: prove P(k) forces P(k+1) —\neach one knocks over the next")
        angles = [LEAN] * 8 + [FLAT]
        self.play(
            LaggedStart(*[Rotate(doms[i + 1], angles[i],
                                 about_point=doms[i + 1].get_corner(DR))
                          for i in range(9)], lag_ratio=0.22),
            LaggedStart(*[labs[i + 1].animate.set_color(GREEN)
                          for i in range(9)], lag_ratio=0.22),
            run_time=4.5)
        self.swap_caption("two finite proofs, infinitely many truths —\nthis is the whole machine")
        self.wait(2.6)
        self.play(FadeOut(doms), FadeOut(labs), run_time=0.7)

    # ------------------------------------------------------------------
    def beat_no_base(self):
        xs = [-3.1 + 0.6 * i for i in range(10)]
        doms, labs = self.make_row(xs)
        self.play(FadeIn(doms), FadeIn(labs), run_time=0.9)
        self.swap_caption('"n = n + 1" — the step is flawless:\nperfect spacing, all the way down the line')
        self.wait(2.2)
        self.swap_caption("but nobody pushed.\nnothing falls — ever")
        self.wait(2.6)
        self.swap_caption("a base case is not ceremony —\nit is the only push there is")
        self.wait(2.4)
        self.play(FadeOut(doms), FadeOut(labs), run_time=0.7)

    # ------------------------------------------------------------------
    def beat_broken_step(self):
        xs = [-3.4 + 0.6 * i for i in range(5)] + \
             [0.9 + 0.6 * i for i in range(5)]
        doms, labs = self.make_row(xs)
        gap_lab = Text("the gap", color=RED, font_size=20)
        gap_lab.move_to([0.05, BASE_Y - 0.32, 0])
        self.play(FadeIn(doms), FadeIn(labs), run_time=0.9)
        self.swap_caption("one k where the step fails —\na gap in the relay (the horses' k = 1)")
        self.play(FadeIn(gap_lab), run_time=0.5)
        self.wait(1.4)

        push = self.push_arrow(xs[0])
        self.play(Create(push), run_time=0.5)
        angles = [LEAN, LEAN, LEAN, LEAN, FLAT]
        self.play(
            LaggedStart(*[Rotate(doms[i], angles[i],
                                 about_point=doms[i].get_corner(DR))
                          for i in range(5)], lag_ratio=0.25),
            LaggedStart(*[labs[i].animate.set_color(GREEN)
                          for i in range(5)], lag_ratio=0.25),
            FadeOut(push), run_time=3.0)
        self.swap_caption("truth falls only up to the gap —\nevery case beyond it stays standing, unproven")
        self.wait(2.6)
        self.swap_caption("so check the step at its smallest k:\nthat is where the cracks hide")
        self.wait(3.0)
