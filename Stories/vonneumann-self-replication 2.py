# stack: Manim
# How self-reproduction actually works (von Neumann, ~1948): the blueprint must be
# used TWICE -- (1) INTERPRETED to build the offspring's body, then (2) COPIED
# unread to give the offspring its own blueprint. That second, non-interpreting
# step is what breaks the infinite regress. DNA does both (translation +
# replication); so does a two-line quine.
#
# Render (4K showcase):  manim -qk vonneumann-self-replication.py SelfReplication
# Layout still (fast):   PIPE_STILL=1 manim -s -ql vonneumann-self-replication.py SelfReplication
#
# Vault palette: BG #1e1e1e, text #cccccc / #888888; semantic purple/teal/green/blue/amber/red.

import os
from manim import *

config.background_color = "#1e1e1e"
TXT = "#cccccc"; DIM = "#888888"
PURPLE = "#7c3aed"  # the constructor (machine)
TEAL = "#0891b2"    # the blueprint phi (data)
GREEN = "#059669"   # interpret / build / complete
BLUE = "#2563eb"    # copy / inherit
AMBER = "#f59e0b"   # warning / highlight
RED = "#dc2626"     # the regress dead-end


def constructor(color=PURPLE):
    box = RoundedRectangle(width=2.5, height=1.0, corner_radius=0.13,
                           stroke_color=color, stroke_width=3,
                           fill_color=color, fill_opacity=0.13)
    t = Text("CONSTRUCTOR", color=color, weight=BOLD).scale(0.36).move_to(box.get_center())
    return VGroup(box, t)


def tape(filled=True, n=6, color=TEAL, label="φ (blueprint)"):
    cells = VGroup(*[
        Rectangle(width=0.4, height=0.4,
                  stroke_color=(color if filled else DIM), stroke_width=2,
                  fill_color=color, fill_opacity=(0.20 if filled else 0.0))
        for _ in range(n)])
    cells.arrange(RIGHT, buff=0.06)
    lbl = Text(label, color=(color if filled else DIM)).scale(0.32)
    grp = VGroup(cells, lbl)
    lbl.next_to(cells, DOWN, buff=0.12)
    return grp


class SelfReplication(Scene):
    def construct(self):
        still = os.environ.get("PIPE_STILL")

        title = Text("Self-replication: why the blueprint is read twice",
                     color=TXT, weight=BOLD).scale(0.58).to_edge(UP, buff=0.4)

        cap = Text("A parent: a universal constructor, plus a blueprint that describes it.",
                   color=TXT).scale(0.42).move_to([0, -3.25, 0])

        def newcap(s, color=TXT, rt=0.7):
            nonlocal cap
            nc = Text(s, color=color).scale(0.42).move_to([0, -3.25, 0])
            self.play(FadeOut(cap, shift=DOWN * 0.1), FadeIn(nc, shift=DOWN * 0.1), run_time=rt)
            cap = nc

        # ---- parent ----
        p_lbl = Text("PARENT", color=DIM).scale(0.34).move_to([-3.7, 2.15, 0])
        pc = constructor().move_to([-3.7, 1.25, 0])
        pphi = tape().move_to([-3.7, -0.55, 0])

        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(p_lbl), FadeIn(pc), FadeIn(pphi), run_time=0.9)
        self.play(FadeIn(cap), run_time=0.5)

        if still:
            return

        # ---- the regress problem ----
        self.wait(0.4)
        newcap("Could it just read itself and build a copy? Then φ must contain φ, "
               "containing φ ...", AMBER)
        reg = Text("φ  needs  φ  needs  φ  needs  ...", color=AMBER).scale(0.5).move_to([0.4, 0.5, 0])
        self.play(FadeIn(reg), run_time=0.7)
        cross = Line(reg.get_left() + LEFT * 0.1, reg.get_right() + RIGHT * 0.1,
                     color=RED, stroke_width=4)
        rfail = Text("infinite regress", color=RED, weight=BOLD).scale(0.4).next_to(reg, DOWN, buff=0.2)
        self.play(Create(cross), FadeIn(rfail), run_time=0.7)
        self.wait(0.5)
        self.play(FadeOut(reg), FadeOut(cross), FadeOut(rfail), run_time=0.5)

        newcap("von Neumann's fix: use the blueprint in TWO different ways.", AMBER)

        # ---- child placeholders ----
        c_lbl = Text("CHILD", color=DIM).scale(0.34).move_to([3.7, 2.15, 0])
        self.play(FadeIn(c_lbl), run_time=0.4)

        # ---- step 1: INTERPRET -> build the body ----
        ia = Arrow([-2.25, 0.6, 0], [2.35, 1.25, 0], color=GREEN, buff=0.15, stroke_width=4)
        ia_lbl = Text("1. interpret  ->  build body", color=GREEN).scale(0.36).move_to([0.0, 1.15, 0])
        cc = constructor(color=GREEN).move_to([3.7, 1.25, 0])
        self.play(Indicate(pphi[0], color=GREEN, scale_factor=1.1), Create(ia), FadeIn(ia_lbl), run_time=0.9)
        newcap("1. INTERPRET -- read φ as instructions and build the offspring's body.", GREEN)
        self.play(FadeIn(cc), run_time=0.8)

        # the gap: empty blueprint slot
        cphi_empty = tape(filled=False, label="(no blueprint)").move_to([3.7, -0.55, 0])
        self.play(FadeIn(cphi_empty), run_time=0.6)
        newcap("But the child has no blueprint of its own -- it is sterile. It cannot reproduce.", AMBER)
        self.play(Indicate(cphi_empty[0], color=AMBER, scale_factor=1.12),
                  Indicate(cphi_empty[1], color=AMBER, scale_factor=1.12), run_time=0.9)

        # ---- step 2: COPY -> inherit the blueprint ----
        ca = Arrow([-2.25, -0.55, 0], [2.35, -0.55, 0], color=BLUE, buff=0.15, stroke_width=4)
        ca_lbl = Text("2. copy  ->  inherit blueprint", color=BLUE).scale(0.36).move_to([0.0, -1.5, 0])
        self.play(Indicate(pphi[0], color=BLUE, scale_factor=1.1), Create(ca), FadeIn(ca_lbl), run_time=0.9)
        newcap("2. COPY -- duplicate φ as raw data, NEVER interpreting it, and hand it to the child.", BLUE)
        cphi = tape(filled=True).move_to([3.7, -0.55, 0])
        self.play(FadeTransform(cphi_empty, cphi), run_time=0.9)

        # ---- result ----
        self.wait(0.3)
        newcap("Two identical machines -- and no regress, because the COPY step never reads φ.", GREEN)
        done_box = SurroundingRectangle(VGroup(cc, cphi), color=GREEN, buff=0.25, stroke_width=3)
        self.play(Create(done_box), run_time=0.8)
        self.wait(0.5)

        # ---- the unification ----
        self.play(FadeOut(ia_lbl), FadeOut(ca_lbl), FadeOut(done_box),
                  FadeOut(ia), FadeOut(ca),
                  FadeOut(pc), FadeOut(pphi), FadeOut(p_lbl),
                  FadeOut(cc), FadeOut(cphi), FadeOut(c_lbl), run_time=0.7)
        newcap("The same trick, everywhere:", TXT)
        lines = VGroup(
            Text("von Neumann's machine:   interpret  +  copy", color=PURPLE).scale(0.42),
            Text("DNA (found 1953):   translation  +  replication", color=GREEN).scale(0.42),
            Text("a 2-line quine:   run the string  +  print the string", color=BLUE).scale(0.42),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([0, 0.2, 0])
        self.play(LaggedStart(*[FadeIn(l, shift=UP * 0.1) for l in lines], lag_ratio=0.4), run_time=1.8)
        self.wait(0.6)
        newcap("One blueprint, used two ways: interpreted to build, copied to inherit.", TXT)
        self.wait(1.4)
