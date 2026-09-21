"""Manim scenes for [[Affective Computing]].
Scene 1  Shadows — a person's state moves about the pleasant/aroused plane.  A skin sensor reads only the
                   state's shadow on the vertical axis; words read only its shadow on the horizontal one.
                   When the state slides from delight to fury, the skin reading does not move at all.
Scene 2  Smiles  — 100 people, 30 of them happy.  People smile 70 % of the time when happy and 30 % of
                   the time when not.  A perfect smile detector flags 42; 21 of those are happy.
Smoke:  manim -ql --fps 15 affective-computing-manim.py Shadows Smiles
Final:  manim -qk affective-computing-manim.py Shadows Smiles      (two separate clips)"""
import numpy as np
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H, TEAL_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"


class Shadows(Scene):
    def construct(self):
        title = Text("A sensor sees a shadow of the feeling, not the feeling", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        c = np.array([-2.2, -0.15, 0]); R = 2.5
        axes = VGroup(Line(c + LEFT * R, c + RIGHT * R, color=GREY_T, stroke_width=2), Line(c + DOWN * R, c + UP * R, color=GREY_T, stroke_width=2),
                      DashedVMobject(Circle(radius=R, color=GREY_T, stroke_width=1.5).move_to(c), num_dashes=70))
        labs = VGroup(Text("pleasant", font_size=18, color=GREY_T).next_to(c + RIGHT * R, RIGHT, buff=0.1), Text("unpleasant", font_size=18, color=GREY_T).next_to(c + LEFT * R, LEFT, buff=0.1),
                      Text("aroused", font_size=18, color=GREY_T).next_to(c + UP * R, UP, buff=0.08), Text("quiet", font_size=18, color=GREY_T).next_to(c + DOWN * R, DOWN, buff=0.08))
        words = {"delighted": (0.72, 0.62), "furious": (-0.72, 0.62), "miserable": (-0.75, -0.5), "content": (0.72, -0.55)}
        wl = VGroup(*[Text(w, font_size=18, color=GREEN_H if x > 0 else RED_H).move_to(c + R * np.array([x * 1.0, y * 1.12, 0])) for w, (x, y) in words.items()])
        self.add(axes, labs, wl)
        x, y = ValueTracker(0.62), ValueTracker(0.5)
        P = lambda: c + R * np.array([x.get_value(), y.get_value(), 0])
        dot = always_redraw(lambda: Dot(P(), color=AMBER_H, radius=0.13))
        sh_v = always_redraw(lambda: VGroup(DashedLine(P(), c + R * np.array([0, y.get_value(), 0]), color=TEAL_H, stroke_width=2), Dot(c + R * np.array([0, y.get_value(), 0]), color=TEAL_H, radius=0.09)))
        sh_h = always_redraw(lambda: VGroup(DashedLine(P(), c + R * np.array([x.get_value(), 0, 0]), color=PURPLE_H, stroke_width=2), Dot(c + R * np.array([x.get_value(), 0, 0]), color=PURPLE_H, radius=0.09)))
        bx = np.array([3.7, 0, 0])
        def meter(tracker, colour, label, ypos):
            base = bx + UP * ypos
            frame = Rectangle(width=3.0, height=0.34, color=GREY_T, stroke_width=1.5).move_to(base)
            fill = always_redraw(lambda: Rectangle(width=max(0.02, 1.5 * (tracker.get_value() + 1)), height=0.34, color=colour, fill_opacity=0.55, stroke_width=0).move_to(base).align_to(frame, LEFT))
            return VGroup(frame, Text(label, font_size=18, color=colour).next_to(frame, UP, buff=0.1)), fill
        m1, f1 = meter(y, TEAL_H, "skin conductance reads: arousal", 1.3)
        m2, f2 = meter(x, PURPLE_H, "word sentiment reads: pleasantness", -0.2)
        self.add(sh_v, sh_h, dot, m1, f1, m2, f2)
        cap = Text("the amber dot is how the person really feels", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(cap); self.wait(2)

        def go(nx, ny, text, t=3.0, hold=1.6):
            nonlocal cap
            self.remove(cap); cap = Text(text, font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3); self.add(cap)
            self.play(x.animate.set_value(nx), y.animate.set_value(ny), run_time=t); self.wait(hold)
        go(-0.62, 0.5, "delight turns to fury: the skin reading does not move at all", t=4, hold=2.5)
        go(-0.65, -0.45, "fury sinks into misery: now the arousal reading falls", t=3)
        go(0.6, -0.5, "misery lifts into contentment: the skin sensor sees nothing happen", t=4, hold=2.5)
        go(0.62, 0.5, "each sensor reports one shadow; neither reports the feeling", t=3, hold=3)


class Smiles(Scene):
    def construct(self):
        title = Text("A perfect smile detector is a poor happiness detector", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        people = [("happy", True)] * 21 + [("happy", False)] * 9 + [("not", True)] * 21 + [("not", False)] * 49
        order = np.random.default_rng(4).permutation(100)
        pos = {}
        dots = VGroup()
        for slot, k in enumerate(order):
            p = np.array([-5.4 + (slot % 20) * 0.57, 1.9 - (slot // 20) * 0.62, 0]); pos[k] = p
            dots.add(Dot(p, color=GREY_T, radius=0.17).set_opacity(0.45))
        self.add(dots)
        cap = Text("100 people", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.35); self.add(cap); self.wait(1.5)
        idx = {k: slot for slot, k in enumerate(order)}
        happy = [k for k, (s, _) in enumerate(people) if s == "happy"]; smiling = [k for k, (_, sm) in enumerate(people) if sm]
        self.remove(cap); cap = Text("30 of them are happy (green). Nobody can see that from outside.", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.35); self.add(cap)
        self.play(*[dots[idx[k]].animate.set_color(GREEN_H).set_opacity(0.9) for k in happy], run_time=1.5); self.wait(2)
        rings = VGroup(*[Circle(radius=0.25, color=AMBER_H, stroke_width=4).move_to(pos[k]) for k in smiling])
        self.remove(cap); cap = Text("42 are smiling: 21 of the happy ones, and 21 who are being polite, nervous or photographed", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.35); self.add(cap)
        self.play(FadeIn(rings), run_time=1.5); self.wait(2.5)
        self.remove(cap); cap = Text("the detector flags every ring correctly, and reports: 42 happy people", font_size=22, color=AMBER_H).to_edge(DOWN, buff=0.35); self.add(cap); self.wait(2.5)
        count = VGroup(Text("flagged: 42", font_size=26, color=AMBER_H), Text("of those, happy: 21", font_size=26, color=GREEN_H), Text("a flag is right 50 % of the time", font_size=26, color=RED_H)).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to([0, -2.0, 0])
        self.remove(cap)
        for line in count:
            self.play(FadeIn(line), run_time=0.6); self.wait(1.0)
        end = Text("the camera made no mistake: the error is in the step from face to feeling", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.25)
        self.add(end); self.wait(3.5)
