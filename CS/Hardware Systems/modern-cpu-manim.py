"""Manim companion for The Modern CPU vs the Textbook Model.

    manim -qk modern-cpu-manim.py InOrderVsOutOfOrder     (4K; copy the MP4 to modern-cpu-out-of-order.mp4)

Eight instructions as two Gantt charts. Instruction 2 is a load that misses the cache and waits six cycles. Top: an
in-order machine, where everything behind the load waits. Bottom: an out-of-order machine, where the independent
instructions behind it run during the wait and the results still commit in program order. Then a branch is
mispredicted and the work fetched after it is thrown away: the price of guessing.
"""
from manim import *

BLUE_, RED_, AMBER_, GREEN_, PURPLE_, TEAL_, GREY_ = "#60a5fa", "#f87171", "#fbbf24", "#34d399", "#c4b5fd", "#67e8f9", "#9ca3af"
PROG = [("1  load a", TEAL_), ("2  load b  (cache miss)", RED_), ("3  c = a + 1", BLUE_), ("4  d = c × 2", BLUE_), ("5  e = b + d", PURPLE_), ("6  f = a − 3", BLUE_), ("7  branch on f", AMBER_), ("8  g = f + 1", BLUE_)]
X0, CW, RH = -2.4, 0.5, 0.21          # cycle axis origin, width per cycle, row height


class InOrderVsOutOfOrder(Scene):
    def construct(self):
        self.camera.background_color = "#0b0f19"
        title = Text("A cache miss, two machines", font_size=36, color=WHITE).to_edge(UP, buff=0.2)
        self.play(FadeIn(title))
        col = VGroup(*[Text(t, font_size=19, color=c) for t, c in PROG]).arrange(DOWN, aligned_edge=LEFT, buff=0.12).to_edge(LEFT, buff=0.35).shift(DOWN*0.4)
        self.play(LaggedStart(*[FadeIn(m) for m in col], lag_ratio=0.08))

        def gantt(y_top, name):
            rows = VGroup(*[Text(str(i + 1), font_size=13, color=GREY_).move_to([X0 - 0.25, y_top - RH * i, 0]) for i in range(8)])
            axis = Line([X0, y_top - RH * 7.6, 0], [X0 + CW * 15, y_top - RH * 7.6, 0], color=GREY_, stroke_width=1.5)
            ticks = VGroup(*[Line([X0 + CW * i, y_top - RH * 7.6 - 0.05, 0], [X0 + CW * i, y_top - RH * 7.6 + 0.05, 0], color=GREY_, stroke_width=1) for i in range(16)])
            nums = VGroup(*[Text(str(i), font_size=12, color=GREY_).move_to([X0 + CW * i, y_top - RH * 7.6 - 0.18, 0]) for i in (0, 5, 10, 15)])
            lab = Text(name, font_size=20, color=WHITE).move_to([X0 + CW * 7.5, y_top + 0.3, 0])
            return VGroup(rows, axis, ticks, nums, lab)
        Y1, Y2 = 2.25, -0.9
        g1, g2 = gantt(Y1, "in order: each instruction waits for the one before"), gantt(Y2, "out of order: ready instructions run during the wait")
        self.play(FadeIn(g1), FadeIn(g2))
        cap = Text("Instruction 2 misses the cache: its result arrives at cycle 7. Instructions 3, 4, 6 and 7 do not need it.", font_size=21, color=GREY_).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(cap))

        def block(i, start, dur, y_top):
            t, c = PROG[i]; x = X0 + CW * start; w = CW * dur
            return Rectangle(width=w - 0.04, height=RH * 0.8, color=c, fill_color=c, fill_opacity=0.6, stroke_width=1).move_to([x + w / 2, y_top - RH * i, 0])
        sched_in = [(0, 0, 1), (1, 1, 6), (2, 7, 1), (3, 8, 1), (4, 9, 1), (5, 10, 1), (6, 11, 1), (7, 12, 1)]
        sched_ooo = [(0, 0, 1), (1, 1, 6), (2, 1, 1), (3, 2, 1), (5, 2, 1), (6, 3, 1), (7, 4, 1), (4, 7, 1)]
        b_in = VGroup(*[block(i, s, d, Y1) for i, s, d in sched_in]); b_ooo = VGroup(*[block(i, s, d, Y2) for i, s, d in sched_ooo])
        self.play(LaggedStart(*[GrowFromEdge(b, LEFT) for b in b_in], lag_ratio=0.22, run_time=3.5))
        self.play(LaggedStart(*[GrowFromEdge(b, LEFT) for b in b_ooo], lag_ratio=0.22, run_time=3.5))
        d1 = Text("done at cycle 13", font_size=17, color=RED_).move_to([X0 + CW * 13.6, Y1 - RH * 7, 0]).shift(RIGHT*0.6)
        d2 = Text("done at cycle 8", font_size=17, color=GREEN_).move_to([X0 + CW * 9.2, Y2 - RH * 4, 0]).shift(RIGHT*0.4)
        cap2 = Text("Same eight instructions. The out-of-order core spent the wait doing the work that did not depend on it.", font_size=21, color=GREY_).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(d1), FadeIn(d2), FadeOut(cap), FadeIn(cap2)); self.wait(1.2)
        cap3 = Text("Results still become visible in program order, 1 to 8. From outside, the contract held.", font_size=21, color=GREY_).to_edge(DOWN, buff=0.22)
        by_prog = [b_ooo[[k for k, (i, _, _) in enumerate(sched_ooo) if i == j][0]] for j in range(8)]
        self.play(FadeOut(cap2), FadeIn(cap3))
        self.play(LaggedStart(*[Indicate(h, color=WHITE, scale_factor=1.25) for h in by_prog], lag_ratio=0.3, run_time=3.2)); self.wait(0.5)
        cap4 = Text("Now suppose the branch at 7 was guessed wrong. Instruction 8 was fetched on the wrong path and is discarded.", font_size=20, color=GREY_).to_edge(DOWN, buff=0.22)
        wrong = b_ooo[6]; cross = Cross(wrong, stroke_color=RED_, stroke_width=3)
        self.play(FadeOut(cap3), FadeIn(cap4), Create(cross), wrong.animate.set_opacity(0.25)); self.wait(0.8)
        refetch = block(7, 10, 1, Y2)
        refl = VGroup(Text("refetched on the right path", font_size=14, color=AMBER_), Text("(10 to 20 cycles later on a real core)", font_size=14, color=AMBER_)).arrange(DOWN, buff=0.04, aligned_edge=LEFT).next_to(refetch, UP, buff=0.06).align_to(refetch, LEFT)
        cap5 = Text("A modern predictor is right about 95 times in 100. The other 5 cost this; the sorted-versus-unsorted experiment measures it.", font_size=19, color=GREY_).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(cap4), FadeIn(cap5), GrowFromEdge(refetch, LEFT), FadeIn(refl)); self.wait(2.0)
