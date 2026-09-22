"""Manim scene for [[Java Classes]].

Construct — what  BankAccount ada = new BankAccount("Ada", 100.0);  does, in order: memory is set aside for a new object
            with every field at its default value; the constructor runs with this pointing at that object and the arguments
            copied into its parameters; each assignment fills a field; the class variable accountsOpened goes up; the reference
            is handed back and stored in ada.  A second new repeats it for bob, and the class variable is seen to be shared.
Smoke:  manim -ql --fps 15 java-classes-manim.py Construct
Final:  manim -qk java-classes-manim.py Construct
"""
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b"


def code_block(lines, centre, size=19):
    rows = VGroup()
    for k, (indent, txt, col) in enumerate(lines):
        t = Text(txt, font="Menlo", font_size=size, color=col)
        t.move_to([0, -0.36 * k, 0], aligned_edge=LEFT).shift(RIGHT * 0.5 * indent)
        rows.add(t)
    return rows.move_to(centre)


def obj_box(pos, name, fields, col=BLUE_H):
    box = RoundedRectangle(width=4.3, height=1.8, corner_radius=0.12, color=col, stroke_width=4, fill_color=col, fill_opacity=0.10).move_to(pos)
    title = Text(name, font_size=20, color=col).next_to(box, UP, buff=0.08)
    rows = VGroup(*[Text(f, font="Menlo", font_size=20, color=GREY_T) for f in fields]).arrange(DOWN, aligned_edge=LEFT, buff=0.14).move_to(pos)
    return VGroup(box, title, rows)


class Construct(Scene):
    def construct(self):
        self.add(Text("What one line does:  BankAccount ada = new BankAccount(\"Ada\", 100.0);", font_size=26, color=GREY_T).to_edge(UP, buff=0.25))
        cap = Text("the constructor, as written in the class", font_size=24, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(cap)

        def say(s, col=GREY_T):
            nonlocal cap
            self.remove(cap); cap = Text(s, font_size=24, color=col).to_edge(DOWN, buff=0.3); self.add(cap)

        code = code_block([(0, "public BankAccount(String owner, double opening) {", PURPLE_H),
                           (1, "this.owner = owner;", GREY_T), (1, "balance = opening;", GREY_T),
                           (1, "withdrawals = 0;", GREY_T), (1, "accountsOpened++;", GREY_T), (0, "}", PURPLE_H)], [-3.1, 1.7, 0], 18)
        cls = VGroup(RoundedRectangle(width=3.6, height=0.9, corner_radius=0.12, color=GREEN_H, stroke_width=4, fill_color=GREEN_H, fill_opacity=0.10).move_to([-4.4, -1.9, 0]),
                     Text("the class (one copy)", font_size=20, color=GREEN_H).move_to([-4.4, -1.15, 0]),
                     Text("accountsOpened = 0", font="Menlo", font_size=20, color=GREY_T).move_to([-4.4, -1.9, 0]))
        self.play(FadeIn(code), FadeIn(cls), run_time=0.8); self.wait(1.5)

        # 1. memory
        say("1.  new sets aside memory for an object, every field at its default value", BLUE_H)
        ada = obj_box([3.6, 1.3, 0], "a new BankAccount object", ["owner       = null", "balance     = 0.0", "withdrawals = 0"])
        self.play(FadeIn(ada), run_time=0.9); self.wait(2.2)

        # 2. parameters
        say("2.  the constructor starts: this points at the new object, the arguments are copied in", PURPLE_H)
        this_arrow = Arrow([-0.2, 1.3, 0], ada[0].get_left(), buff=0.1, color=PURPLE_H, stroke_width=5, max_tip_length_to_length_ratio=0.12)
        this_l = Text("this", font="Menlo", font_size=20, color=PURPLE_H).next_to(this_arrow, UP, buff=0.05)
        params = code_block([(0, 'owner   = "Ada"', AMBER_H), (0, "opening = 100.0", AMBER_H)], [3.6, -0.8, 0], 19)
        plab = Text("parameters (local to this call)", font_size=18, color=AMBER_H).next_to(params, DOWN, buff=0.12)
        self.play(GrowArrow(this_arrow), FadeIn(this_l), FadeIn(params), FadeIn(plab), run_time=0.9); self.wait(2.2)

        # 3. assignments
        hl = SurroundingRectangle(code[1], color=AMBER_H, buff=0.06)
        say('3.  this.owner = owner:  the field on the left, the parameter on the right', GREY_T)
        self.play(Create(hl), run_time=0.4)
        new = Text('owner       = "Ada"', font="Menlo", font_size=20, color=GREY_T).move_to(ada[2][0], aligned_edge=LEFT)
        self.play(Transform(ada[2][0], new), run_time=0.8); self.wait(1.4)
        say("balance = opening:  no name clash, so no this is needed", GREY_T)
        self.play(hl.animate.move_to(code[2]), run_time=0.4)
        new = Text("balance     = 100.0", font="Menlo", font_size=20, color=GREY_T).move_to(ada[2][1], aligned_edge=LEFT)
        self.play(Transform(ada[2][1], new), run_time=0.8); self.wait(1.2)
        self.play(hl.animate.move_to(code[3]), run_time=0.4); self.wait(0.8)
        say("accountsOpened++ changes the class variable, not anything in the object", GREEN_H)
        self.play(hl.animate.move_to(code[4]), run_time=0.4)
        new = Text("accountsOpened = 1", font="Menlo", font_size=20, color=GREY_T).move_to(cls[2])
        self.play(Transform(cls[2], new), Indicate(cls[0], color=GREEN_H, scale_factor=1.04), run_time=0.9); self.wait(1.4)

        # 4. return
        say("4.  the constructor ends; the reference to the finished object is handed back and stored in ada", BLUE_H)
        self.play(FadeOut(hl), FadeOut(this_arrow), FadeOut(this_l), FadeOut(params), FadeOut(plab), run_time=0.6)
        var = VGroup(RoundedRectangle(width=1.1, height=0.7, corner_radius=0.08, color=BLUE_H, stroke_width=4).move_to([0.4, -1.9, 0]),
                     Dot([0.4, -1.9, 0], color=BLUE_H, radius=0.08), Text("ada", font="Menlo", font_size=24, color=BLUE_H).move_to([-0.6, -1.9, 0]))
        arr = Arrow([0.4, -1.9, 0], ada[0].get_bottom() + LEFT * 1.2, buff=0.1, color=BLUE_H, stroke_width=5, max_tip_length_to_length_ratio=0.12)
        self.play(FadeIn(var), run_time=0.5); self.play(GrowArrow(arr), run_time=0.8); self.wait(2.0)

        # 5. a second object
        say('5.  new BankAccount("Bob") does it all again: its own fields, the SAME class variable', GREEN_H)
        bob = obj_box([3.6, -1.8, 0], "another object", ['owner       = "Bob"', "balance     = 0.0", "withdrawals = 0"])
        self.play(ada.animate.shift(UP * 0.35), run_time=0.6)
        self.remove(arr); arr = Arrow([0.4, -1.9, 0], ada[0].get_bottom() + LEFT * 1.2 + UP * 0.35, buff=0.1, color=BLUE_H, stroke_width=5, max_tip_length_to_length_ratio=0.12); self.add(arr)
        self.play(FadeIn(bob), run_time=0.8)
        new = Text("accountsOpened = 2", font="Menlo", font_size=20, color=GREY_T).move_to(cls[2])
        self.play(Transform(cls[2], new), Indicate(cls[0], color=GREEN_H, scale_factor=1.04), run_time=0.9); self.wait(1.5)
        say("two objects, two sets of fields; one class, one accountsOpened", GREY_T); self.wait(4)
