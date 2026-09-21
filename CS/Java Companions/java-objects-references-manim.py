"""Manim scene for [[Java Objects, References and Strings]].

PassReference — what "call by value" means when the value is a reference.  main holds `gate`, an arrow to a Counter object.
                clickTwice(gate): the parameter c is a COPY of the arrow, so it reaches the same object, and the clicks land on it.
                replace(gate):    c is again a copy; `c = new Counter(1000)` swings the copy to a new object.  gate never moves,
                and when the method ends the new object has no arrow left pointing at it.
Smoke:  manim -ql --fps 15 java-objects-references-manim.py PassReference
Final:  manim -qk java-objects-references-manim.py PassReference
"""
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b"


def var_box(name, pos, col):
    box = RoundedRectangle(width=1.1, height=0.7, corner_radius=0.08, color=col, stroke_width=4).move_to(pos)
    dot = Dot(pos, color=col, radius=0.08)
    lab = Text(name, font="Menlo", font_size=26, color=col).next_to(box, LEFT, buff=0.2)
    return VGroup(box, dot, lab)


def obj_box(pos, n, col=GREEN_H):
    box = RoundedRectangle(width=3.5, height=1.1, corner_radius=0.12, color=col, stroke_width=4, fill_color=col, fill_opacity=0.12).move_to(pos)
    txt = Text(f"count  {n}", font="Menlo", font_size=28, color=GREY_T).move_to(pos)
    return VGroup(box, txt)


def ptr(a, b, col):
    return Arrow(a, b, buff=0.08, color=col, stroke_width=5, max_tip_length_to_length_ratio=0.08)


class PassReference(Scene):
    def construct(self):
        self.add(Text("Java passes a copy of the arrow, never the object and never the variable", font_size=26, color=GREY_T).to_edge(UP, buff=0.25))
        cap = Text("Counter gate = new Counter(5);", font="Menlo", font_size=24, color=GREY_T).to_edge(DOWN, buff=0.35)

        def say(s, col=GREY_T):
            nonlocal cap
            self.remove(cap)
            cap = Text(s, font_size=24, color=col).to_edge(DOWN, buff=0.35)
            self.add(cap)

        # two regions: main on the left-top, the method on the left-bottom, the objects on the right
        main_lab = Text("main", font_size=22, color=BLUE_H).move_to([-5.6, 2.3, 0])
        meth_lab = Text("the method", font_size=22, color=PURPLE_H).move_to([-5.2, -0.5, 0])
        heap_lab = Text("objects", font_size=22, color=GREEN_H).move_to([3.4, 2.3, 0])
        gate = var_box("gate", [-3.2, 1.5, 0], BLUE_H)
        o1 = obj_box([3.4, 1.2, 0], 5)
        a_gate = ptr([-3.2, 1.5, 0], o1[0].get_left() + UP * 0.15, BLUE_H)
        self.add(main_lab, heap_lab, cap)
        self.play(FadeIn(gate), FadeIn(o1), run_time=0.8); self.play(GrowArrow(a_gate), run_time=0.8); self.wait(1.2)

        # ---- clickTwice ----
        say("clickTwice(gate);      the parameter c starts as a copy of gate's arrow", PURPLE_H)
        c = var_box("c", [-3.2, -1.3, 0], PURPLE_H)
        a_c = ptr([-3.2, -1.3, 0], o1[0].get_left() + DOWN * 0.15, PURPLE_H)
        ghost = a_gate.copy().set_color(PURPLE_H)
        self.play(FadeIn(meth_lab), FadeIn(c), run_time=0.7)
        self.play(Transform(ghost, a_c), run_time=1.4); self.remove(ghost); self.add(a_c); self.wait(2.0)
        for n in (6, 7):
            say("c.click();      it lands on the one object there is", PURPLE_H)
            new = Text(f"count  {n}", font="Menlo", font_size=28, color=GREY_T).move_to(o1[1])
            self.play(Indicate(o1[0], color=AMBER_H, scale_factor=1.06), Transform(o1[1], new), run_time=0.9); self.wait(1.0)
        say("the method ends; c disappears.  gate sees 7, because there was only ever one object", GREEN_H)
        self.play(FadeOut(c), FadeOut(a_c), FadeOut(meth_lab), run_time=0.8); self.wait(2.0)

        # ---- replace ----
        say("replace(gate);      again c starts as a copy of gate's arrow", PURPLE_H)
        c = var_box("c", [-3.2, -1.3, 0], PURPLE_H)
        a_c = ptr([-3.2, -1.3, 0], o1[0].get_left() + DOWN * 0.15, PURPLE_H)
        ghost = a_gate.copy().set_color(PURPLE_H)
        self.play(FadeIn(meth_lab), FadeIn(c), run_time=0.7)
        self.play(Transform(ghost, a_c), run_time=1.2); self.remove(ghost); self.add(a_c); self.wait(1.6)
        say("c = new Counter(1000);      a new object, and the COPY swings over to it", AMBER_H)
        o2 = obj_box([3.4, -1.6, 0], 1000, AMBER_H)
        self.play(FadeIn(o2), run_time=0.8)
        a_c2 = ptr([-3.2, -1.3, 0], o2[0].get_left(), PURPLE_H)
        self.play(Transform(a_c, a_c2), run_time=1.5); self.wait(1.8)
        say("gate's arrow did not move.  Assigning to a parameter changes the copy only.", BLUE_H)
        self.play(Indicate(a_gate, color=AMBER_H, scale_factor=1.03), run_time=1.2); self.wait(2.2)
        say("the method ends; c disappears, and nothing points at the new object any more", GREY_T)
        self.play(FadeOut(c), FadeOut(a_c), FadeOut(meth_lab), run_time=0.8)
        self.play(o2.animate.set_opacity(0.25), run_time=1.0); self.wait(2.0)
        say("a method can change the object you hand it.  It cannot change which object your variable points at.", GREEN_H)
        self.wait(4.0)
