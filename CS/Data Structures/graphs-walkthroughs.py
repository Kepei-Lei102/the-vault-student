# Animation stack: Manim (the bay's standard). Two SLOW exam-paced scenes,
# built because Dijkstra and A* are trace-by-hand exam questions - the pacing
# here is deliberately step-by-step, one decision per beat.
# Render:  manim -qk graphs-walkthroughs.py DijkstraWalkthrough
#          manim -qk graphs-walkthroughs.py AStarWalkthrough
# then copy the MP4s beside the card and delete media/ and __pycache__/.
"""Slow walkthroughs of the two real exam questions.

DijkstraWalkthrough: November 2025 Paper 33 - the answer table fills one
settlement at a time, with every relaxation spoken as arithmetic.
AStarWalkthrough: June 2026 Paper 33 - the exam's own f = g + h table built
row by row, the smallest-f choice highlighted before every expansion.
"""
from manim import *
import numpy as np

GREY = ManimColor("#888888")
BLUE = ManimColor("#2563eb")
GREEN = ManimColor("#059669")
AMBER = ManimColor("#f59e0b")
RED = ManimColor("#dc2626")
TEAL = ManimColor("#0891b2")


def make_node(label, pos, color=BLUE, r=0.30, fs=20):
    c = Circle(radius=r, color=color, fill_opacity=0.18, stroke_width=3).move_to(pos)
    t = Text(label, font_size=fs, color=GREY).move_to(pos)
    return VGroup(c, t)


# ---------------------------------------------------------------- Dijkstra
class DijkstraWalkthrough(Scene):
    def construct(self):
        title = Text("Dijkstra, step by step - November 2025 Paper 33",
                     font_size=30, color=GREY).to_edge(UP, buff=0.35)
        self.play(FadeIn(title), run_time=0.8)

        # graph on the left half
        pos = {"Start": np.array([-6.0, -2.2, 0]), "T": np.array([-5.4, 0.6, 0]),
               "V": np.array([-3.4, 1.7, 0]), "W": np.array([-2.6, 0.0, 0]),
               "X": np.array([-0.6, 0.8, 0]), "Y": np.array([-1.2, -2.3, 0]),
               "Z": np.array([1.4, -1.2, 0])}
        Wt = {("Start", "T"): 6, ("Start", "Y"): 22, ("T", "V"): 4, ("V", "W"): 3,
              ("V", "X"): 9, ("W", "X"): 5, ("X", "Y"): 3, ("X", "Z"): 10,
              ("Y", "Z"): 8}
        nodes = {l: make_node(l, pos[l], r=0.40 if l == "Start" else 0.30)
                 for l in pos}
        edge_mob = {}
        wlabels = []
        for (a, b), w in Wt.items():
            e = Line(pos[a], pos[b], color=GREY, stroke_width=2.5, buff=0.32)
            edge_mob[(a, b)] = e
            mid = (pos[a] + pos[b]) / 2 + np.array([0.06, 0.24, 0])
            wlabels.append(Text(str(w), font_size=20, color=GREY).move_to(mid))
        self.play(*[FadeIn(n) for n in nodes.values()],
                  *[Create(e) for e in edge_mob.values()],
                  *[FadeIn(t) for t in wlabels], run_time=1.2)

        # the answer table on the right: one column per town, rows appended
        cols = ["T", "V", "W", "X", "Y", "Z"]
        x_right = 4.15
        col_x = {c: x_right - 0.92 * (len(cols) - 1) / 2 + 0.92 * i
                 for i, c in enumerate(cols)}
        header = VGroup(*[Text(c, font_size=24, color=BLUE).move_to(
            [col_x[c], 1.9, 0]) for c in cols])
        header_line = Line([x_right - 2.9, 1.62, 0], [x_right + 2.9, 1.62, 0],
                           color=GREY, stroke_width=1.5)
        self.play(FadeIn(header), Create(header_line), run_time=0.8)

        commentary = Text("initialise: Start is 0, every town starts at ∞",
                          font_size=26, color=AMBER).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(commentary), run_time=0.8)

        row_y = [1.15, 0.55, -0.05, -0.65, -1.25, -1.85]
        current = {c: "∞" for c in cols}
        row0 = VGroup(*[Text("∞", font_size=23, color=GREY).move_to(
            [col_x[c], row_y[0], 0]) for c in cols])
        self.play(FadeIn(row0), run_time=0.7)
        self.wait(1.2)

        def say(msg, color=GREY):
            nonlocal commentary
            new = Text(msg, font_size=26, color=color).to_edge(DOWN, buff=0.4)
            self.play(ReplacementTransform(commentary, new), run_time=0.7)
            commentary = new

        # (settle, [(town, "arithmetic", newval)], row_index, message)
        script = [
            ("Start", [("T", "0+6", "6"), ("Y", "0+22", "22")], 1,
             "settle Start (0). Relax its neighbours: T becomes 0+6, Y becomes 0+22"),
            ("T", [("V", "6+4", "10")], 2,
             "nearest unsettled is T (6). Relax: V becomes 6+4 = 10"),
            ("V", [("W", "10+3", "13"), ("X", "10+9", "19")], 3,
             "nearest is V (10). Relax: W = 10+3 = 13, X = 10+9 = 19"),
            ("W", [("X", "13+5", "18")], 4,
             "nearest is W (13). Relax: 13+5 = 18 beats 19 - X improves!"),
        ]

        for settle, updates, r, msg in script:
            say(msg, AMBER)
            self.play(nodes[settle][0].animate.set_fill(GREEN, opacity=0.7),
                      run_time=0.6)
            self.wait(0.9)
            for town, arith, newval in updates:
                current[town] = newval
            row = VGroup(*[
                Text(current[c], font_size=23,
                     color=AMBER if any(c == u[0] for u in updates) else GREY
                     ).move_to([col_x[c], row_y[r], 0]) for c in cols])
            self.play(FadeIn(row), run_time=0.7)
            self.wait(1.1)

        # X settles, then the Y trap in slow motion
        say("nearest is X (18). Relax: Y = 18+3 = 21... but Y already says 22", AMBER)
        self.play(nodes["X"][0].animate.set_fill(GREEN, opacity=0.7), run_time=0.6)
        self.wait(0.9)
        say("21 beats 22 - the DIRECT Start-Y road loses by one. Keep relaxing!", RED)
        self.play(edge_mob[("Start", "Y")].animate.set_color(RED), run_time=0.6)
        self.wait(1.4)
        for town, val in (("Y", "21"), ("Z", "28")):
            current[town] = val
        row = VGroup(*[Text(current[c], font_size=23,
                            color=AMBER if c in ("Y", "Z") else GREY
                            ).move_to([col_x[c], row_y[5], 0]) for c in cols])
        self.play(FadeIn(row), run_time=0.7)
        self.wait(0.9)

        say("settle Y (21): Z via Y would be 21+8 = 29 - worse than 28, no change", GREY)
        self.play(nodes["Y"][0].animate.set_fill(GREEN, opacity=0.7), run_time=0.6)
        self.wait(1.3)
        say("settle Z (28). Everything is certain now", GREY)
        self.play(nodes["Z"][0].animate.set_fill(GREEN, opacity=0.7), run_time=0.6)
        self.wait(0.8)

        final = Text("T6  V10  W13  X18  Y21  Z28 - the published mark scheme's answers",
                     font_size=27, color=GREEN).to_edge(DOWN, buff=0.4)
        box = SurroundingRectangle(
            VGroup(*[m for m in self.mobjects if isinstance(m, VGroup)][-1]),
            color=GREEN, buff=0.18, stroke_width=2.5)
        self.play(ReplacementTransform(commentary, final), Create(box), run_time=0.9)
        self.wait(2.4)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.9)


# ---------------------------------------------------------------- A*
class AStarWalkthrough(Scene):
    def construct(self):
        title = Text("A*, step by step - June 2026 Paper 33",
                     font_size=30, color=GREY).to_edge(UP, buff=0.32)
        self.play(FadeIn(title), run_time=0.8)

        pos = {"W": np.array([-6.1, 0.3, 0]), "N1": np.array([-4.9, 1.9, 0]),
               "N2": np.array([-4.3, -0.6, 0]), "N3": np.array([-5.0, -2.2, 0]),
               "N5": np.array([-2.4, -0.1, 0]), "N4": np.array([-1.8, -2.0, 0]),
               "N6": np.array([-0.8, 1.2, 0]), "E": np.array([0.9, -0.4, 0])}
        Wt = {("W", "N1"): 6, ("W", "N2"): 4, ("W", "N3"): 7, ("N2", "N5"): 7,
              ("N5", "N4"): 2, ("N5", "N6"): 4, ("N5", "E"): 11, ("N6", "E"): 3}
        H = {"W": 18, "N1": 15, "N2": 14, "N3": 13, "N5": 7, "N4": 9, "N6": 3, "E": 0}
        nodes = {l: make_node(l, pos[l], r=0.36 if l in ("W", "E") else 0.28,
                              fs=18) for l in pos}
        for (a, b), w in Wt.items():
            pass
        edges = [Line(pos[a], pos[b], color=GREY, stroke_width=2.5, buff=0.30)
                 for (a, b) in Wt]
        wlabels = [Text(str(w), font_size=19, color=GREY).move_to(
            (pos[a] + pos[b]) / 2 + np.array([0.05, 0.22, 0])) for (a, b), w in Wt.items()]
        hlabels = [Text(f"h={H[l]}", font_size=17, color=TEAL).next_to(
            nodes[l], DOWN, buff=0.08) for l in pos]
        self.play(*[FadeIn(n) for n in nodes.values()], *[Create(e) for e in edges],
                  *[FadeIn(t) for t in wlabels], *[FadeIn(t) for t in hlabels],
                  run_time=1.3)

        note = Text("every node carries h: the estimated distance still to go",
                    font_size=25, color=TEAL).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(1.3)

        # the exam's table, built row by row on the right
        hdr = VGroup(
            Text("path", font_size=20, color=BLUE).move_to([2.3, 2.15, 0]),
            Text("g", font_size=20, color=BLUE).move_to([4.35, 2.15, 0]),
            Text("h", font_size=20, color=BLUE).move_to([5.25, 2.15, 0]),
            Text("f=g+h", font_size=20, color=BLUE).move_to([6.25, 2.15, 0]))
        hline = Line([1.3, 1.9, 0], [6.9, 1.9, 0], color=GREY, stroke_width=1.5)
        self.play(FadeIn(hdr), Create(hline), run_time=0.7)

        rows = [
            ("W", "0", "18", "18", False),
            ("W-N1", "6", "15", "21", False),
            ("W-N2", "4", "14", "18", True),
            ("W-N3", "7", "13", "20", False),
            ("W-N2-N5", "11", "7", "18", True),
            ("W-N2-N5-N4", "13", "9", "22", False),
            ("W-N2-N5-N6", "15", "3", "18", True),
            ("W-N2-N5-E", "22", "0", "22", False),
            ("W-N2-N5-N6-E", "18", "0", "18", True),
        ]
        beats = [
            (0, "start at W: nothing spent, everything estimated - f = 0 + 18",
             None),
            (1, "expand W: three roads out. Each gets one row - spent + estimate",
             "W"),
            (4, "smallest f is 18 at W-N2: expand N2. Through it, N5 keeps f = 18",
             "N2"),
            (6, "smallest f is 18 again: expand N5. Three new rows",
             "N5"),
            (8, "look at row W-N2-N5-E: f = 22. The DIRECT road is not expanded -",
             "N6"),
            (9, "the detour through N6 reaches E with f = 18. Smallest f AND at the target: done",
             None),
        ]

        note_ref = [note]
        def say(msg, color=AMBER):
            new = Text(msg, font_size=24, color=color).to_edge(DOWN, buff=0.35)
            self.play(ReplacementTransform(note_ref[0], new), run_time=0.7)
            note_ref[0] = new

        y0, dy = 1.55, 0.42
        drawn = 0
        row_mobs = []
        for upto, msg, expand in beats:
            say(msg)
            if expand:
                self.play(nodes[expand][0].animate.set_fill(AMBER, opacity=0.6),
                          run_time=0.5)
            while drawn < upto:
                p_, g_, h_, f_, best = rows[drawn]
                col = AMBER if best else GREY
                rm = VGroup(
                    Text(p_, font_size=18, color=col).move_to([2.3, y0 - drawn * dy, 0]),
                    Text(g_, font_size=18, color=col).move_to([4.35, y0 - drawn * dy, 0]),
                    Text(h_, font_size=18, color=col).move_to([5.25, y0 - drawn * dy, 0]),
                    Text(f_, font_size=18, color=col).move_to([6.25, y0 - drawn * dy, 0]))
                row_mobs.append(rm)
                self.play(FadeIn(rm), run_time=0.5)
                drawn += 1
            self.wait(1.5)

        # highlight the winning path on the graph
        path = ["W", "N2", "N5", "N6", "E"]
        for a, b in zip(path, path[1:]):
            seg = Line(pos[a], pos[b], color=GREEN, stroke_width=6, buff=0.30)
            self.play(Create(seg), run_time=0.5)
        say("best path W-N2-N5-N6-E, cost 18 - the published answer", GREEN)
        self.wait(2.4)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.9)
