"""Manim companion for How a Language Model Works.

    manim -qk language-model-manim.py Attention     (4K; copy the MP4 to language-model-attention.mp4)

One attention step, slowed down. A sentence arrives as a row of vectors. The last word asks a question (its query),
every earlier word answers with a key, the match scores become weights through a softmax, and the last word's new
vector is the weighted mix of the earlier words' values. Then one word in the sentence changes, and the weights move.
"""
from manim import *

BLUE_, RED_, AMBER_, GREEN_, PURPLE_, TEAL_, GREY_ = "#60a5fa", "#f87171", "#fbbf24", "#34d399", "#c4b5fd", "#67e8f9", "#9ca3af"


class Attention(Scene):
    def construct(self):
        self.camera.background_color = "#0b0f19"
        title = Text("One attention step", font_size=40, color=WHITE).to_edge(UP, buff=0.3)
        self.play(FadeIn(title))
        words = ["The", "bank", "by", "the", "river", "was", "steep"]
        weights1 = [0.04, 0.42, 0.03, 0.03, 0.40, 0.08]          # what "steep" attends to
        words2 = ["The", "bank", "by", "the", "square", "was", "closed"]
        weights2 = [0.05, 0.55, 0.04, 0.03, 0.25, 0.08]
        xs = [-5.4 + 1.8 * i for i in range(7)]
        boxes = VGroup(*[VGroup(RoundedRectangle(width=1.5, height=0.7, corner_radius=0.12, color=BLUE_, stroke_width=3).move_to([x, 1.8, 0]),
                                Text(w, font_size=28, color=WHITE).move_to([x, 1.8, 0])) for x, w in zip(xs, words)])
        cap = Text("A sentence arrives as seven vectors, one per token, each already carrying where it sits.", font_size=24, color=GREY_).to_edge(DOWN, buff=0.4)
        self.play(LaggedStart(*[FadeIn(b, shift=UP*0.2) for b in boxes], lag_ratio=0.12), FadeIn(cap)); self.wait(0.6)

        # the query
        last = boxes[-1]; qlab = Text("query: what does 'steep' need to know?", font_size=24, color=AMBER_).next_to(last, DOWN, buff=0.35).shift(LEFT*1.6)
        self.play(last[0].animate.set_color(AMBER_), FadeIn(qlab))
        cap2 = Text("The last token asks a question of every earlier one. Each earlier token answers with its key.", font_size=24, color=GREY_).to_edge(DOWN, buff=0.4)
        self.play(FadeOut(cap), FadeIn(cap2))
        arrows = VGroup(*[Arrow(last[0].get_bottom() + DOWN*0.05, boxes[i][0].get_bottom() + DOWN*0.05, path_arc=0.9, color=PURPLE_, stroke_width=3, buff=0.05, max_tip_length_to_length_ratio=0.08) for i in range(6)])
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.1)); self.wait(0.4)

        # weights as bars
        cap3 = Text("The matches go through a softmax and become weights that sum to one.", font_size=24, color=GREY_).to_edge(DOWN, buff=0.4)
        self.play(FadeOut(cap2), FadeIn(cap3), FadeOut(arrows), FadeOut(qlab))
        bars = VGroup(); labels = VGroup()
        for i, w in enumerate(weights1):
            bar = Rectangle(width=0.9, height=max(0.05, 3.2*w), color=PURPLE_, fill_color=PURPLE_, fill_opacity=0.7, stroke_width=1).move_to([xs[i], 0.9 - 0.0, 0], aligned_edge=UP).shift(DOWN*0.0)
            bar.align_to([xs[i], 0.9, 0], UP)
            lab = DecimalNumber(w, num_decimal_places=2, font_size=24, color=PURPLE_).next_to(bar, DOWN, buff=0.1)
            bars.add(bar); labels.add(lab)
        self.play(LaggedStart(*[GrowFromEdge(b, UP) for b in bars], lag_ratio=0.1), FadeIn(labels)); self.wait(0.5)

        # the mix
        cap4 = Text("'steep' is rebuilt as the weighted mix of the earlier tokens' values: mostly 'bank' and 'river'.", font_size=24, color=GREY_).to_edge(DOWN, buff=0.4)
        self.play(FadeOut(cap3), FadeIn(cap4))
        newvec = VGroup(RoundedRectangle(width=1.5, height=0.7, corner_radius=0.12, color=GREEN_, stroke_width=3, fill_color=GREEN_, fill_opacity=0.15).move_to([xs[-1], -2.4, 0]),
                        Text("steep′", font_size=28, color=GREEN_).move_to([xs[-1], -2.4, 0]))
        flows = VGroup(*[Line(bars[i].get_bottom() + DOWN*0.35, newvec[0].get_left() + LEFT*0.05, color=GREEN_, stroke_width=1 + 8*weights1[i], stroke_opacity=0.25 + 0.75*weights1[i]) for i in range(6)])
        self.play(LaggedStart(*[Create(f) for f in flows], lag_ratio=0.08), FadeIn(newvec)); self.wait(1.2)
        note = Text("a river bank, then", font_size=24, color=GREEN_).next_to(newvec, LEFT, buff=0.3)
        self.play(FadeIn(note)); self.wait(0.8)

        # change a word, the weights move
        cap5 = Text("Change one word. The same weights are recomputed from the new sentence, and 'bank' now means money.", font_size=23, color=GREY_).to_edge(DOWN, buff=0.4)
        self.play(FadeOut(cap4), FadeIn(cap5), FadeOut(flows), FadeOut(note))
        new_texts = []
        for i, (w_old, w_new) in enumerate(zip(words, words2)):
            if w_old != w_new:
                t = Text(w_new, font_size=28, color=RED_).move_to(boxes[i][1]); new_texts.append((i, t))
        self.play(*[Transform(boxes[i][1], t) for i, t in new_texts], *[boxes[i][0].animate.set_color(RED_) for i, _ in new_texts])
        anims = []
        for i, w in enumerate(weights2):
            nb = Rectangle(width=0.9, height=max(0.05, 3.2*w), color=PURPLE_, fill_color=PURPLE_, fill_opacity=0.7, stroke_width=1); nb.align_to([xs[i], 0.9, 0], UP).set_x(xs[i])
            anims += [Transform(bars[i], nb), labels[i].animate.set_value(w).next_to(nb, DOWN, buff=0.1)]
        self.play(*anims, run_time=1.6)
        newvec2 = Text("closed′", font_size=28, color=GREEN_).move_to(newvec[1])
        flows2 = VGroup(*[Line(bars[i].get_bottom() + DOWN*0.35, newvec[0].get_left() + LEFT*0.05, color=GREEN_, stroke_width=1 + 8*weights2[i], stroke_opacity=0.25 + 0.75*weights2[i]) for i in range(6)])
        note2 = Text("a bank with a door, then", font_size=24, color=GREEN_).next_to(newvec, LEFT, buff=0.3)
        self.play(Transform(newvec[1], newvec2), LaggedStart(*[Create(f) for f in flows2], lag_ratio=0.08), FadeIn(note2)); self.wait(1.0)
        cap6 = Text("Nothing was looked up. The weights are arithmetic on the vectors, learned from predicting the next token.", font_size=23, color=GREY_).to_edge(DOWN, buff=0.4)
        self.play(FadeOut(cap5), FadeIn(cap6)); self.wait(2.0)
