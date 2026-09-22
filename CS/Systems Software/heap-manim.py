"""heap-manim.py — mark and sweep on an object graph, and the cycle reference counting cannot free.

Render:  manim -qk heap-manim.py MarkAndSweep
Then copy media/videos/heap-manim/2160p60/MarkAndSweep.mp4 to heap-mark-and-sweep.mp4
beside the card and delete media/ and __pycache__/.
"""
from manim import *
import textwrap

BLUE_, RED_, AMBER_, GREEN_, PURPLE_, TEAL_, GREY_ = "#60a5fa", "#f87171", "#fbbf24", "#34d399", "#c4b5fd", "#67e8f9", "#9ca3af"

# the graph of heap-lab.py part B: root->A->B->C, A->D<->E, root->F
POS = {"root": (-5.2, 0.6), "A": (-2.6, 1.6), "B": (0.0, 1.6), "C": (2.6, 1.6), "D": (-1.0, -0.9), "E": (1.6, -0.9), "F": (-2.6, -1.4)}
EDGES = [("root", "A"), ("A", "B"), ("B", "C"), ("A", "D"), ("D", "E"), ("E", "D"), ("root", "F")]


class MarkAndSweep(Scene):
    def cap(self, text, old=None):
        c = Text("\n".join(textwrap.wrap(text, 84)), font_size=22, color=GREY_, line_spacing=0.8).to_edge(DOWN, buff=0.3)
        self.play(*([FadeOut(old)] if old else []), FadeIn(c)); return c

    def node(self, name):
        x, y = POS[name]
        if name == "root":
            shape = Rectangle(width=1.5, height=0.7, stroke_color=WHITE, fill_color=WHITE, fill_opacity=0.12).move_to([x, y, 0])
            label = Text("roots\n(the stack)", font_size=16, color=WHITE, line_spacing=0.8).move_to(shape)
        else:
            shape = Circle(radius=0.42, stroke_color=GREY_, fill_color=GREY_, fill_opacity=0.15).move_to([x, y, 0])
            label = Text(name, font_size=26, color=WHITE).move_to(shape)
        return VGroup(shape, label)

    def edge(self, a, b, bend=0.0):
        pa, pb = self.nodes[a][0], self.nodes[b][0]
        if bend:
            return CurvedArrow(pa.get_center(), pb.get_center(), angle=bend, color=GREY_, stroke_width=3, tip_length=0.18).set_z_index(-1)
        return Arrow(pa.get_center(), pb.get_center(), buff=0.45, color=GREY_, stroke_width=3, max_tip_length_to_length_ratio=0.12)

    def rc_badge(self, name, n):
        x, y = POS[name]
        return Text(str(n), font_size=18, color=AMBER_).move_to([x + 0.55, y + 0.42, 0])

    def construct(self):
        title = Text("The heap: what is still reachable, and what is garbage", font_size=32, color=WHITE).to_edge(UP, buff=0.25)
        self.add(title)
        self.nodes = {n: self.node(n) for n in POS}
        self.play(LaggedStart(*[FadeIn(v, scale=0.8) for v in self.nodes.values()], lag_ratio=0.1, run_time=1.2))
        self.edges = {}
        for a, b in EDGES:
            bend = 0.0
            if (a, b) == ("D", "E"): bend = -0.9
            if (a, b) == ("E", "D"): bend = -0.9
            self.edges[(a, b)] = self.edge(a, b, bend)
        # the D<->E pair drawn as two curved arrows
        self.edges[("D", "E")] = CurvedArrow(self.nodes["D"][0].get_center() + UP * 0.25 + RIGHT * 0.35, self.nodes["E"][0].get_center() + UP * 0.25 + LEFT * 0.35, angle=-0.8, color=GREY_, stroke_width=3, tip_length=0.18)
        self.edges[("E", "D")] = CurvedArrow(self.nodes["E"][0].get_center() + DOWN * 0.25 + LEFT * 0.35, self.nodes["D"][0].get_center() + DOWN * 0.25 + RIGHT * 0.35, angle=-0.8, color=GREY_, stroke_width=3, tip_length=0.18)
        self.play(LaggedStart(*[Create(e) for e in self.edges.values()], lag_ratio=0.1, run_time=1.6))
        counts = {"A": 1, "B": 1, "C": 1, "D": 2, "E": 1, "F": 1}
        badges = {n: self.rc_badge(n, c) for n, c in counts.items()}
        c = self.cap("Seven objects on the heap. The number by each is its reference count: how many arrows point at it.")
        self.play(*[FadeIn(b) for b in badges.values()]); self.wait(1.5)

        # the program drops two references
        c = self.cap("The program drops two references: A no longer needs D, and the roots no longer hold F.", c)
        self.play(FadeOut(self.edges[("A", "D")]), FadeOut(self.edges[("root", "F")]))
        counts["D"] -= 1; counts["F"] -= 1
        newD, newF = self.rc_badge("D", 1), self.rc_badge("F", 0)
        self.play(Transform(badges["D"], newD), Transform(badges["F"], newF)); self.wait(0.8)
        c = self.cap("Reference counting frees F at once: its count is zero. D and E each still have a count of 1, from each other.", c)
        self.play(self.nodes["F"][0].animate.set_fill(RED_, opacity=0.5).set_stroke(RED_), badges["F"].animate.set_color(RED_))
        self.play(FadeOut(self.nodes["F"]), FadeOut(badges["F"]))
        cyc = SurroundingRectangle(VGroup(self.nodes["D"], self.nodes["E"]), color=AMBER_, buff=0.35, corner_radius=0.2)
        self.play(Create(cyc)); self.wait(1.6)
        c = self.cap("Nothing the program can still reach points at D or E, yet their counts never reach zero. A cycle is the leak reference counting cannot see.", c)
        self.wait(2.2)

        # mark and sweep
        c = self.cap("Mark and sweep asks a different question: not \"who points at you?\" but \"can the roots reach you?\" Start at the roots and follow every arrow.", c)
        self.play(FadeOut(cyc), *[FadeOut(b) for n, b in badges.items() if n != "F"])
        order = ["A", "B", "C"]
        pulse = Dot(color=GREEN_, radius=0.12).move_to(self.nodes["root"][0].get_center())
        self.play(FadeIn(pulse))
        for a, b in [("root", "A"), ("A", "B"), ("B", "C")]:
            self.play(pulse.animate.move_to(self.nodes[b][0].get_center()), run_time=0.6)
            self.play(self.nodes[b][0].animate.set_fill(GREEN_, opacity=0.45).set_stroke(GREEN_), run_time=0.3)
        self.play(FadeOut(pulse))
        marked = Text("marked: A, B, C", font_size=20, color=GREEN_).move_to([4.6, -0.9, 0])
        self.play(FadeIn(marked)); self.wait(1.0)
        c = self.cap("Sweep: walk the whole heap and free everything that was not marked. D and E go, cycle and all.", c)
        self.play(self.nodes["D"][0].animate.set_fill(RED_, opacity=0.5).set_stroke(RED_), self.nodes["E"][0].animate.set_fill(RED_, opacity=0.5).set_stroke(RED_))
        self.play(FadeOut(self.nodes["D"]), FadeOut(self.nodes["E"]), FadeOut(self.edges[("D", "E")]), FadeOut(self.edges[("E", "D")]))
        swept = Text("swept: D, E (and F)", font_size=20, color=RED_).next_to(marked, DOWN, buff=0.2)
        self.play(FadeIn(swept)); self.wait(1.2)
        c = self.cap("The price: while the collector walks the graph the program waits. That pause is the cost of never having to call free.", c)
        self.wait(2.5)
