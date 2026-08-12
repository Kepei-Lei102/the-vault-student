"""RPN evaluation on a stack, run live: 6 2 + 5 1 - x  (= 32).

One left-to-right pass: numbers push; an operator pops two (first pop
is the RIGHT operand), applies, pushes the result. Deterministic.

Render (from this folder):
    manim -qm compiler-rpn-stack.py RPNStack   # smoke
    manim -qk compiler-rpn-stack.py RPNStack   # 4K final
Copy the output beside the card as compiler-rpn-stack.mp4, then clear
media/ + __pycache__/.
"""

from manim import *

BG = "#1a1a1a"
GRAY = "#9a9a9a"
BLUE = "#2563eb"
GREEN = "#059669"
TEAL = "#0891b2"
AMBER = "#f59e0b"
PURPLE = "#7c3aed"

config.background_color = BG

TOKENS = ["6", "2", "+", "5", "1", "-", "×"]
STACK_BASE = LEFT * 4.6 + DOWN * 2.6
STACK_STEP = UP * 0.78


class RPNStack(Scene):
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=25, color=color).to_edge(DOWN, buff=0.3)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.2), FadeIn(cap, run_time=0.3))
        else:
            self.play(FadeIn(cap, run_time=0.3))
        self._cap = cap

    def chip(self, txt, color=BLUE):
        c = VGroup(
            RoundedRectangle(corner_radius=0.1, width=1.0, height=0.66,
                             stroke_color=color, stroke_width=2.5,
                             fill_color=color, fill_opacity=0.25),
            Text(txt, font_size=30, color=GRAY, weight=BOLD),
        )
        c[1].move_to(c[0])
        return c

    def construct(self):
        title = Text("6  2  +  5  1  -  ×", font_size=34, color=GRAY,
                     weight=BOLD).to_edge(UP, buff=0.4)
        sub = Text("read left to right — push numbers; an operator pops two, applies, pushes",
                   font_size=22, color=GRAY).next_to(title, DOWN, buff=0.2)

        # token strip
        strip = VGroup(*[self.chip(t, PURPLE if t in "+-×" else BLUE)
                         for t in TOKENS]).arrange(RIGHT, buff=0.28)
        strip.move_to(UP * 1.35)
        pointer = Triangle(color=AMBER, fill_color=AMBER, fill_opacity=1
                           ).scale(0.14).rotate(180 * DEGREES)
        pointer.next_to(strip[0], UP, buff=0.12)

        # stack area
        stack_lab = Text("the stack", font_size=24, color=TEAL, weight=BOLD
                         ).move_to(STACK_BASE + RIGHT * 1.75 + DOWN * 0.36)
        floor = Line(STACK_BASE + LEFT * 0.75 + DOWN * 0.42,
                     STACK_BASE + RIGHT * 0.75 + DOWN * 0.42,
                     color=TEAL, stroke_width=3)

        self.play(FadeIn(title), FadeIn(sub), FadeIn(strip), FadeIn(pointer),
                  FadeIn(stack_lab), FadeIn(floor), run_time=1.0)

        stack = []

        def spos(i):
            return STACK_BASE + STACK_STEP * i

        work = Text("", font_size=28).move_to(RIGHT * 2.2 + DOWN * 1.2)

        steps = [
            ("6", None), ("2", None),
            ("+", ("6", "2", "8", "6 + 2 = 8")),
            ("5", None), ("1", None),
            ("-", ("5", "1", "4", "5 - 1 = 4  (second pop on the LEFT)")),
            ("×", ("8", "4", "32", "8 × 4 = 32")),
        ]

        for idx, (tok, op) in enumerate(steps):
            self.play(pointer.animate.next_to(strip[idx], UP, buff=0.12),
                      run_time=0.35)
            if op is None:
                c = self.chip(tok, TEAL)
                c.move_to(strip[idx].get_center())
                self.add(c)
                self.play(c.animate.move_to(spos(len(stack))), run_time=0.55)
                stack.append(c)
                if idx == 1:
                    self.swap_caption("numbers: just push")
            else:
                left, right, res, sentence = op
                b = stack.pop()   # first pop  = right operand
                a = stack.pop()   # second pop = left operand
                note = Text(sentence, font_size=27, color=AMBER, weight=BOLD
                            ).move_to(RIGHT * 2.4 + DOWN * 1.1)
                self.play(b[0].animate.set_fill(AMBER), a[0].animate.set_fill(AMBER),
                          run_time=0.3)
                self.play(a.animate.move_to(RIGHT * 1.15 + DOWN * 1.9).scale(0.8),
                          b.animate.move_to(RIGHT * 3.55 + DOWN * 1.9).scale(0.8),
                          FadeIn(note), run_time=0.6)
                r = self.chip(res, GREEN)
                r.move_to(RIGHT * 2.4 + DOWN * 1.9)
                self.play(FadeOut(a), FadeOut(b), FadeIn(r), run_time=0.5)
                self.play(r.animate.move_to(spos(len(stack))), FadeOut(note),
                          run_time=0.6)
                stack.append(r)
                if tok == "+":
                    self.swap_caption("an operator pops TWO — first pop is the RIGHT operand", color=PURPLE)
                if tok == "-":
                    self.swap_caption("watch the minus: pop 1, pop 5 — compute 5 - 1, never 1 - 5", color=AMBER)

        self.swap_caption("one pass, no brackets, no precedence — the answer is what remains: 32", color=GREEN)
        self.play(stack[0][0].animate.set_stroke(GREEN, width=5), run_time=0.5)
        self.wait(1.8)
