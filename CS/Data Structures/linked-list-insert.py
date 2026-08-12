"""Linked List — what an insert actually costs.

Beat 1: the array pays the shuffle — every later item moves to record one fact.
Beat 2: the linked insert — two pointer writes, nothing moves.
Beat 3: the wrong order — reverse the two writes and the tail is orphaned.
Beat 4: delete — one write on the predecessor; the node is unlinked, not erased.

Render:  manim -qk linked-list-insert.py LinkedListInsert
House style: bg #1a1a1a, captions #9a9a9a, teal data, amber pointers, blue newcomer.
Deterministic — no seed stamp.
"""

from manim import *

BG = "#1a1a1a"
GRAYT = "#9a9a9a"
TEAL = "#0891b2"
AMBER = "#f59e0b"
BLUE = "#2563eb"

config.background_color = BG


class LinkedListInsert(Scene):
    def swap_caption(self, text, color=GRAYT, font_size=30):
        cap = Text(text, color=color, font_size=font_size, line_spacing=0.9)
        cap.move_to(DOWN * 3.35)
        anims = [FadeIn(cap, run_time=0.35)]
        if getattr(self, "_cap", None) is not None:
            anims.append(FadeOut(self._cap, run_time=0.25))
        self._cap = cap
        self.play(*anims)

    def make_node(self, letter, pos, color=TEAL):
        box = RoundedRectangle(width=0.95, height=0.72, corner_radius=0.12)
        box.set_stroke(GRAYT, 2).set_fill(color, 0.20)
        txt = Text(letter, color=color, font_size=30)
        g = VGroup(box, txt).move_to(pos)
        return g

    def link(self, a, b):
        return Arrow(a.get_center(), b.get_center(), buff=0.62,
                     color=AMBER, stroke_width=3.5,
                     max_tip_length_to_length_ratio=0.12)

    def construct(self):
        self.beat_array()
        self.beat_linked()

    # ------------------------------------------------------------------
    def beat_array(self):
        cells = VGroup(*[Square(0.8).set_stroke(GRAYT, 2)
                         .move_to([-4.5 + i, 0.8, 0]) for i in range(10)])
        letters = "ABCEFGHIJ"
        vals = [Text(ch, color=TEAL, font_size=30).move_to(cells[i])
                for i, ch in enumerate(letters)]
        self.play(Create(cells), *[FadeIn(v) for v in vals], run_time=1.2)
        self.swap_caption("an ordered array — insert D where it belongs,\nbetween C and E")

        d = Text("D", color=BLUE, font_size=34).move_to([-1.5, 2.4, 0])
        self.play(FadeIn(d), run_time=0.5)
        self.wait(0.8)

        # shift E..J one cell right, last first
        for i in range(8, 2, -1):
            self.play(vals[i].animate.move_to(cells[i + 1]), run_time=0.32)
        self.play(d.animate.move_to(cells[3]), run_time=0.6)
        self.swap_caption("six moves to record one fact — at a million items,\na million moves. The structure charges for what DIDN'T change")
        self.wait(2.6)

        self.play(FadeOut(cells), *[FadeOut(v) for v in vals], FadeOut(d),
                  run_time=0.7)

    # ------------------------------------------------------------------
    def beat_linked(self):
        pos = {"A": [-3.9, 1.6, 0], "B": [2.9, 2.0, 0],
               "C": [-1.9, -0.6, 0], "E": [3.8, -1.2, 0],
               "D": [0.6, -1.7, 0]}
        nodes = {k: self.make_node(k, p) for k, p in pos.items() if k != "D"}
        head_lab = Text("head", color=AMBER, font_size=26).move_to([-5.7, 1.6, 0])
        arrows = {
            "hA": Arrow(head_lab.get_right(), nodes["A"].get_left(), buff=0.1,
                        color=AMBER, stroke_width=3.5,
                        max_tip_length_to_length_ratio=0.2),
            "AB": self.link(nodes["A"], nodes["B"]),
            "BC": self.link(nodes["B"], nodes["C"]),
            "CE": self.link(nodes["C"], nodes["E"]),
        }
        self.play(*[FadeIn(m) for m in nodes.values()], FadeIn(head_lab),
                  *[Create(a) for a in arrows.values()], run_time=1.2)
        self.swap_caption("the same list as a chain — scattered across memory,\nordered only by its pointers")
        self.wait(1.8)

        newD = self.make_node("D", pos["D"], color=BLUE)
        self.play(FadeIn(newD), run_time=0.6)
        self.swap_caption("insert D: point D at E...")
        dE = self.link(newD, nodes["E"])
        self.play(Create(dE), run_time=0.7)
        self.swap_caption("...and point C at D. Two writes — nothing moved,\nbecause order never lived in the geography")
        cD = self.link(nodes["C"], newD)
        self.play(Create(cD), FadeOut(arrows["CE"]), run_time=0.8)
        self.wait(2.6)

        # ---- the wrong order: rewind, then reverse the two writes ----
        self.swap_caption("rewind — same insert, but the two writes reversed:\npoint C at D first")
        ce2 = self.link(nodes["C"], nodes["E"])
        self.play(FadeOut(cD), FadeOut(dE), Create(ce2), run_time=0.8)
        self.wait(0.8)
        nodes["E"].save_state()
        cD2 = self.link(nodes["C"], newD)
        self.play(Create(cD2), FadeOut(ce2), run_time=0.8)
        self.swap_caption("C's pointer was the only record of where E lives —\noverwritten before anyone saved it")
        self.play(nodes["E"].animate.shift(DOWN * 0.8 + RIGHT * 0.5)
                  .set_opacity(0.2), run_time=1.2)
        self.wait(0.6)
        qm = Text("?", color="#dc2626", font_size=42).move_to([2.85, -1.4, 0])
        stub = Arrow(newD.get_center(), [2.55, -1.45, 0], buff=0.62,
                     color="#dc2626", stroke_width=3.5,
                     max_tip_length_to_length_ratio=0.25)
        self.swap_caption("now point D at... what? The address is gone —\nthe whole tail is orphaned in the sea, unreachable")
        self.play(Create(stub), FadeIn(qm), run_time=0.7)
        self.wait(2.6)
        self.swap_caption("grip first — D takes hold of the chain —\nthen relink. The order of the two writes is everything")
        self.play(FadeOut(qm), FadeOut(stub), FadeOut(cD2),
                  Restore(nodes["E"]), run_time=0.8)
        dE2 = self.link(newD, nodes["E"])
        cD3 = self.link(nodes["C"], newD)
        self.play(Create(dE2), Create(cD3), run_time=0.9)
        self.wait(2.2)

        self.swap_caption("delete B: one write — A points past it")
        aC = self.link(nodes["A"], nodes["C"])
        self.play(Create(aC),
                  FadeOut(arrows["AB"]), FadeOut(arrows["BC"]),
                  nodes["B"].animate.set_opacity(0.25), run_time=0.9)
        self.wait(1.5)
        self.swap_caption("unlinked, not erased — B is a ghost in the sea;\nthe list pays only for the facts that change")
        self.wait(3)
