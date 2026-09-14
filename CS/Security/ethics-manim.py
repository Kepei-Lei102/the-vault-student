"""
ethics-manim.py — two scenes for [[Ethics and Ownership]].

Scene 1  ProxyBias    — a hiring model audited four ways: the bars for two groups of
                        equal ability, the protected column deleted (the gap survives
                        through the postcode), the proxy deleted, the labels cleaned.
                        Numbers are from ethics-bias-demo.py.
Scene 2  CopyleftFlow — one library, two licences: code flows into a closed product
                        under a permissive licence; under the GPL the obligation flows
                        back out and the product must open.

Smoke:   manim -ql --fps 15 ethics-manim.py ProxyBias CopyleftFlow
Final:   manim -qk ethics-manim.py ProxyBias CopyleftFlow
then concat with ffmpeg to ethics-manim.mp4 and rm -rf media __pycache__.
"""
from manim import *

GREY = "#888888"
BLUE, RED, GREEN, AMBER, PURPLE, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"

# (label, rate A, rate B) from ethics-bias-demo.py
MODELS = [
    ("all columns, trained on the old decisions", 71, 8),
    ("protected column DELETED, same training", 47, 26),
    ("postcode deleted too", 36, 33),
    ("all columns, trained on FAIR decisions", 71, 70),
]


class ProxyBias(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("Hire rate at EQUAL ability — group A vs group B", font_size=32, color=GREY).to_edge(UP, buff=0.3)
        self.play(FadeIn(title))
        base_y = -1.6
        axis = Line([-5.5, base_y, 0], [5.5, base_y, 0], color=GREY)
        self.play(Create(axis))
        scale = 0.045                                    # 1 % = 0.045 units
        barA = Rectangle(width=1.4, height=0.01, color=BLUE, fill_color=BLUE, fill_opacity=0.7).move_to([-1.0, base_y, 0], aligned_edge=DOWN)
        barB = Rectangle(width=1.4, height=0.01, color=RED, fill_color=RED, fill_opacity=0.7).move_to([1.0, base_y, 0], aligned_edge=DOWN)
        labA = Text("group A", font_size=20, color=BLUE).next_to(barA, DOWN, buff=0.15)
        labB = Text("group B", font_size=20, color=RED).next_to(barB, DOWN, buff=0.15)
        self.play(FadeIn(barA), FadeIn(barB), FadeIn(labA), FadeIn(labB))
        valA = Text("", font_size=22, color=BLUE); valB = Text("", font_size=22, color=RED)
        gap = Text("", font_size=24, color=AMBER).move_to([0, 2.15, 0])
        cap = Text("", font_size=22, color=GREY).move_to([0, 2.7, 0])
        self.add(valA, valB, gap, cap)
        for i, (label, a, b) in enumerate(MODELS):
            newA = Rectangle(width=1.4, height=max(a * scale, 0.01), color=BLUE, fill_color=BLUE, fill_opacity=0.7).move_to([-1.0, base_y, 0], aligned_edge=DOWN)
            newB = Rectangle(width=1.4, height=max(b * scale, 0.01), color=RED, fill_color=RED, fill_opacity=0.7).move_to([1.0, base_y, 0], aligned_edge=DOWN)
            nvA = Text(f"{a}%", font_size=22, color=BLUE).next_to(newA, UP, buff=0.1)
            nvB = Text(f"{b}%", font_size=22, color=RED).next_to(newB, UP, buff=0.1)
            ng = Text(f"gap {a - b:+d} points", font_size=24, color=AMBER if a - b > 5 else GREEN).move_to([0, 2.15, 0])
            nc = Text(f"model {i + 1}: {label}", font_size=22, color=GREY).move_to([0, 2.7, 0])
            self.play(Transform(barA, newA), Transform(barB, newB), Transform(valA, nvA), Transform(valB, nvB),
                      Transform(gap, ng), Transform(cap, nc), run_time=1.2)
            self.wait(1.6)
            if i == 1:
                note = Text("the postcode is 57% correlated with group: the model reads it instead", font_size=20, color=AMBER).to_edge(DOWN, buff=0.4)
                self.play(FadeIn(note)); self.wait(1.8); self.play(FadeOut(note))
        moral = Text("the bias lived in the old decisions; a model trained on them learns to repeat them", font_size=21, color=GREY).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(moral)); self.wait(2.2)


class CopyleftFlow(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("Same library, two licences: which way does the obligation flow?", font_size=30, color=GREY).to_edge(UP, buff=0.3)
        self.play(FadeIn(title))

        def box(label, sub, pos, col, w=3.4):
            r = RoundedRectangle(width=w, height=1.3, corner_radius=0.15, color=col, fill_color=col, fill_opacity=0.12).move_to(pos)
            t = Text(label, font_size=22, color=col).move_to(r.get_center() + UP * 0.25)
            s = Text(sub, font_size=15, color=GREY).move_to(r.get_center() + DOWN * 0.3)
            return VGroup(r, t, s)

        # top row: permissive
        lib1 = box("library (MIT)", "keep the notice, otherwise free", [-4, 1.5, 0], GREEN)
        app1 = box("your app", "closed source, sold for a fee", [4, 1.5, 0], RED)
        arr1 = Arrow(lib1.get_right(), app1.get_left(), color=GREY, buff=0.15)
        self.play(FadeIn(lib1), FadeIn(app1), GrowArrow(arr1))
        code1 = Dot(color=GREEN, radius=0.12).move_to(lib1.get_right())
        self.add(code1)
        self.play(code1.animate.move_to(app1.get_left()), run_time=1.2)
        ok1 = Text("allowed: the code goes in, nothing has to come out", font_size=19, color=GREEN).next_to(app1, DOWN, buff=0.15)
        self.play(FadeIn(ok1), FadeOut(code1)); self.wait(1.0)

        # bottom row: GPL
        lib2 = box("library (GPL)", "copyleft: same licence downstream", [-4, -1.4, 0], PURPLE)
        app2 = box("your app", "wants to stay closed…", [4, -1.4, 0], RED)
        arr2 = Arrow(lib2.get_right(), app2.get_left(), color=GREY, buff=0.15)
        self.play(FadeIn(lib2), FadeIn(app2), GrowArrow(arr2))
        code2 = Dot(color=PURPLE, radius=0.12).move_to(lib2.get_right())
        self.add(code2)
        self.play(code2.animate.move_to(app2.get_left()), run_time=1.2)
        self.play(FadeOut(code2))
        back = Arrow(app2.get_left() + DOWN * 0.45, lib2.get_right() + DOWN * 0.45, color=PURPLE, buff=0.15, stroke_width=5)
        blab = Text("the licence travels with the code", font_size=17, color=PURPLE).next_to(back, DOWN, buff=0.08)
        self.play(GrowArrow(back), FadeIn(blab))
        app2_new = box("your app", "must open: GPL, source and all", [4, -1.4, 0], PURPLE)
        self.play(Transform(app2, app2_new), run_time=0.9)
        self.wait(0.8)
        moral = Text("copyright makes both enforceable: the author owns the code, the licence is the permission attached to it",
                     font_size=19, color=GREY).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(moral)); self.wait(2.2)
