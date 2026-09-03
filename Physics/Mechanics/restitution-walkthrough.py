# Animation stack: Manim (the bay's standard; slow exam-paced, per the
# standing preference for trace-by-hand exam topics).
# Render:  manim -qk restitution-walkthrough.py ObliqueWalkthrough
# then copy the MP4 beside the card and delete media/ and __pycache__/.
"""The June 2026 Paper 33 oblique impact, one decision per beat:
components split at contact, the perpendicular pair copied through,
then momentum + NEL assembled along the line of centres with the sign
convention on screen the whole way. Ends on the sign trap the published
scheme prices at A0."""
from manim import *
import numpy as np

GREY = ManimColor("#888888")
BLUE = ManimColor("#2563eb")
GREEN = ManimColor("#059669")
AMBER = ManimColor("#f59e0b")
RED = ManimColor("#dc2626")
TEAL = ManimColor("#0891b2")


class ObliqueWalkthrough(Scene):
    def construct(self):
        title = Text("Oblique impact, step by step - June 2026 Paper 33",
                     font_size=30, color=GREY).to_edge(UP, buff=0.32)
        self.play(FadeIn(title), run_time=0.8)

        # spheres on the line of centres, upper-left of frame
        cA, cB = np.array([-4.0, 0.6, 0]), np.array([-2.6, 0.6, 0])
        loc = Line([-6.6, 0.6, 0], [-0.4, 0.6, 0], color=GREY, stroke_width=2,
                   stroke_opacity=0.7)
        loc_lab = Text("line of centres", font_size=20, color=GREY)
        loc_lab.next_to(loc, RIGHT, buff=0.15)
        sA = Circle(radius=0.7, color=BLUE, fill_opacity=0.15,
                    stroke_width=3).move_to(cA)
        sB = Circle(radius=0.7, color=TEAL, fill_opacity=0.15,
                    stroke_width=3).move_to(cB)
        tA = Text("A", font_size=24, color=GREY).move_to(cA)
        tB = Text("B", font_size=24, color=GREY).move_to(cB)
        self.play(Create(loc), FadeIn(loc_lab), FadeIn(sA), FadeIn(sB),
                  FadeIn(tA), FadeIn(tB), run_time=1.0)

        given = MathTex(
            r"\cos\alpha = \tfrac45 \quad \cos\beta = \tfrac{24}{25} \quad"
            r"\cos\theta = \tfrac35 \quad \cos\varphi = \tfrac45",
            font_size=34, color=GREY).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(given), run_time=0.8)
        self.wait(1.4)

        note_ref = [given]
        def say(mobj):
            self.play(ReplacementTransform(note_ref[0], mobj.to_edge(DOWN, buff=0.4)),
                      run_time=0.7)
            note_ref[0] = mobj

        # incoming arrows
        vA_arrow = Arrow(cA + np.array([-1.8, -1.25, 0]), cA + np.array([-0.45, -0.32, 0]),
                         color=BLUE, stroke_width=5, buff=0)
        vB_arrow = Arrow(cB + np.array([1.9, -0.55, 0]), cB + np.array([0.5, -0.15, 0]),
                         color=TEAL, stroke_width=5, buff=0)
        aLab = MathTex(r"u_A,\ \alpha", font_size=30, color=BLUE).next_to(vA_arrow, LEFT, buff=0.1)
        bLab = MathTex(r"u_B,\ \beta", font_size=30, color=TEAL).next_to(vB_arrow, RIGHT, buff=0.1)
        self.play(GrowArrow(vA_arrow), GrowArrow(vB_arrow), FadeIn(aLab), FadeIn(bLab),
                  run_time=1.0)
        self.wait(1.0)

        # Step 1: perpendicular components preserved
        s1 = Text("smooth spheres: each PERPENDICULAR component is untouched",
                  font_size=25, color=GREEN)
        say(s1)
        eq1 = MathTex(r"u_A\sin\alpha = v_A\sin\theta", font_size=36, color=GREEN)
        eq1.move_to([3.4, 1.7, 0])
        eq1b = MathTex(r"\tfrac35 u_A = \tfrac45 v_A \ \Rightarrow\ v_A = \tfrac34 u_A",
                       font_size=34, color=GREY).next_to(eq1, DOWN, buff=0.25)
        self.play(FadeIn(eq1), run_time=0.8)
        self.wait(0.8)
        self.play(FadeIn(eq1b), run_time=0.8)
        self.wait(1.4)
        s2 = MathTex(r"\text{part (a): } 1 - \left(\tfrac34\right)^2 = \tfrac{7}{16} = 43.75\%\ \text{of A's KE lost}",
                     font_size=30, color=GREEN)
        say(s2)
        self.wait(1.8)

        eq2 = MathTex(r"u_B\sin\beta = v_B\sin\varphi \ \Rightarrow\ v_B = \tfrac{7}{15} u_B",
                      font_size=34, color=GREEN).next_to(eq1b, DOWN, buff=0.35)
        self.play(FadeIn(eq2), run_time=0.8)
        self.wait(1.2)

        # Step 2: sign convention banner
        s3 = Text("now the line of centres - and first, THE SIGN CONVENTION",
                  font_size=25, color=AMBER)
        say(s3)
        conv = Arrow([-6.3, -0.6, 0], [-4.9, -0.6, 0], color=AMBER,
                     stroke_width=5, buff=0)
        conv_lab = Text("positive", font_size=20, color=AMBER).next_to(conv, DOWN, buff=0.08)
        self.play(GrowArrow(conv), FadeIn(conv_lab), run_time=0.8)
        self.wait(1.2)

        # Step 3: momentum along LoC
        s4 = Text("momentum along the line of centres - B approaches negative, A rebounds negative",
                  font_size=23, color=AMBER)
        say(s4)
        mom = MathTex(
            r"m\!\left(\tfrac45 u_A\right) - m\!\left(\tfrac{24}{25}u_B\right)"
            r"= -m\!\left(\tfrac34 u_A\right)\!\tfrac35 + m\!\left(\tfrac7{15}u_B\right)\!\tfrac45",
            font_size=30, color=GREY).move_to([0.3, -1.0, 0])
        self.play(FadeIn(mom), run_time=0.9)
        self.wait(2.2)
        momr = MathTex(r"\Rightarrow\ u_B = \tfrac{15}{16}\,u_A",
                       font_size=34, color=AMBER).next_to(mom, DOWN, buff=0.3)
        self.play(FadeIn(momr), run_time=0.8)
        self.wait(1.6)

        # Step 4: NEL
        s5 = Text("Newton's experimental law: separation over approach, same signs",
                  font_size=24, color=AMBER)
        say(s5)
        nel = MathTex(
            r"e = \frac{\tfrac35 v_A + \tfrac45 v_B}{\tfrac45 u_A + \tfrac{24}{25}u_B}",
            font_size=34, color=GREY).move_to([4.6, -1.2, 0])
        self.play(FadeIn(nel), run_time=0.9)
        self.wait(1.8)

        ans = MathTex(r"e = \tfrac{8}{17} \approx 0.471", font_size=44, color=GREEN)
        ans.move_to([4.6, -2.4, 0])
        box = SurroundingRectangle(ans, color=GREEN, buff=0.22, stroke_width=2.5)
        s6 = Text("the published answer - four marks", font_size=25, color=GREEN)
        say(s6)
        self.play(FadeIn(ans), Create(box), run_time=0.9)
        self.wait(1.8)

        # the trap
        trap = Text("mix the sign conventions and you get e = -0.335: the scheme scores it A0",
                    font_size=24, color=RED)
        say(trap)
        self.wait(2.2)
        s7 = Text("a negative e is never physics - it is always the sign alarm",
                  font_size=25, color=RED)
        say(s7)
        self.wait(2.0)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.9)
