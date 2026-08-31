"""Manim: Binary Trees — see it run.

Act 1  Freeze the search: binary search on a sorted array asks the same first
       question every time; lift the decision map out of the array and it IS
       the binary search tree (mid = 20, then 10/26, then 8/22).
Act 2  Arrival order decides the shape: the same five values grow the bushy
       tree when they arrive as 20, 10, 26, 22, 8 — and a right-leaning spine
       (a linked list in disguise) when they arrive sorted.
Act 3  The walk that comes out sorted: trace the contour, emit each node at
       its bottom flag, and the output row assembles itself in order.

Paced slowly per house rule: one-clause captions, 2–4 s holds.

Render (from this folder):
    manim -ql binary-trees-see-it-run.py BinaryTreesSeeItRun    # smoke
    manim -qk binary-trees-see-it-run.py BinaryTreesSeeItRun    # 4K final
Copy media/videos/binary-trees-see-it-run/2160p60/BinaryTreesSeeItRun.mp4
  -> binary-trees-see-it-run.mp4 beside the card, then rm -rf media/ __pycache__/.
"""

from manim import (
    Scene, VGroup, VMobject, Text, Circle, Square, Line, Dot, DashedVMobject,
    FadeIn, FadeOut, Create, Transform, Indicate, MoveAlongPath,
    UP, DOWN, LEFT, RIGHT, ORIGIN, config,
)
import numpy as np

BG = "#1e1e1e"
TXT = "#cccccc"
GREY = "#9a9a9a"
BLUE = "#2563eb"
GREEN = "#059669"
AMBER = "#f59e0b"
RED = "#dc2626"
TEAL = "#0891b2"
FONT = "Helvetica Neue"
config.background_color = BG

# canonical bushy tree positions (same tree all three acts)
POS = {
    20: np.array([0.0, 2.1, 0.0]),
    10: np.array([-2.3, 0.7, 0.0]),
    26: np.array([2.3, 0.7, 0.0]),
    8:  np.array([-3.4, -0.8, 0.0]),
    22: np.array([1.2, -0.8, 0.0]),
}
EDGES = [(20, 10), (20, 26), (10, 8), (26, 22)]
R = 0.42


def tree_node(v, pos=ORIGIN, color=BLUE):
    c = Circle(radius=R, color=color, fill_color=color, fill_opacity=0.22,
               stroke_width=3).move_to(pos)
    t = Text(str(v), font=FONT, font_size=27, color=TXT).move_to(pos)
    return VGroup(c, t)


def tree_edge(a, b, pos=None):
    pos = pos or POS
    d = pos[b] - pos[a]
    u = d / np.linalg.norm(d)
    return Line(pos[a] + u * R, pos[b] - u * R, color=GREY, stroke_width=2.5)


def caption(s, size=27, color=TXT):
    return Text(s, font=FONT, font_size=size, color=color).to_edge(UP, buff=0.35)


class BinaryTreesSeeItRun(Scene):
    def construct(self):
        # ============================== Act 1 — freeze the search
        cap = caption("binary search always asks the same first question")
        vals = [8, 10, 20, 22, 26]
        cells = VGroup()
        for i, v in enumerate(vals):
            sq = Square(side_length=0.95, color=GREY, stroke_width=2)
            sq.move_to(np.array([-2.6 + i * 1.3, -2.7, 0.0]))
            tv = Text(str(v), font=FONT, font_size=26, color=TXT).move_to(sq)
            cells.add(VGroup(sq, tv))
        self.play(FadeIn(cap), FadeIn(cells), run_time=1.0)
        self.wait(2.2)

        # lift the middle
        self.play(Indicate(cells[2], color=AMBER, scale_factor=1.15), run_time=1.2)
        n20 = tree_node(20)
        n20.move_to(cells[2].get_center())
        self.add(n20)
        self.play(n20.animate.move_to(POS[20]), run_time=1.6)
        self.wait(1.4)

        cap2 = caption("smaller goes left, larger goes right — always to the same next question")
        self.play(Transform(cap, cap2), run_time=0.7)
        e1, e2 = tree_edge(20, 10), tree_edge(20, 26)
        n10, n26 = tree_node(10), tree_node(26)
        n10.move_to(cells[1].get_center()); n26.move_to(cells[4].get_center())
        self.add(n10, n26)
        self.play(Indicate(cells[1], color=AMBER), Indicate(cells[4], color=AMBER), run_time=1.0)
        self.play(n10.animate.move_to(POS[10]), n26.animate.move_to(POS[26]), run_time=1.6)
        self.play(Create(e1), Create(e2), run_time=0.8)
        self.wait(1.2)
        e3, e4 = tree_edge(10, 8), tree_edge(26, 22)
        n8, n22 = tree_node(8), tree_node(22)
        n8.move_to(cells[0].get_center()); n22.move_to(cells[3].get_center())
        self.add(n8, n22)
        self.play(n8.animate.move_to(POS[8]), n22.animate.move_to(POS[22]), run_time=1.6)
        self.play(Create(e3), Create(e4), run_time=0.8)
        self.wait(1.0)

        cap3 = caption("the map never changes — store it: each answer becomes a pointer")
        self.play(Transform(cap, cap3), cells.animate.set_opacity(0.25), run_time=0.9)
        self.wait(3.0)

        tree1 = VGroup(e1, e2, e3, e4, n20, n10, n26, n8, n22)
        self.play(FadeOut(cells), FadeOut(tree1), run_time=0.8)

        # ============================== Act 2 — arrival order decides the shape
        cap4 = caption("grow it by arrivals: 20, 10, 26, 22, 8")
        self.play(Transform(cap, cap4), run_time=0.7)

        nodes = {}
        def insert_animated(v, parent_chain, side_note=None):
            # flash the comparison chain, then drop the node in
            for p in parent_chain:
                self.play(Indicate(nodes[p], color=AMBER, scale_factor=1.12), run_time=0.65)
            n = tree_node(v, POS[v])
            self.play(FadeIn(n, shift=DOWN * 0.4), run_time=1.0)
            nodes[v] = n
            if parent_chain:
                e = tree_edge(parent_chain[-1], v)
                self.play(Create(e), run_time=0.5)
                nodes[(parent_chain[-1], v)] = e
            self.wait(0.6)

        insert_animated(20, [])
        insert_animated(10, [20])
        insert_animated(26, [20])
        insert_animated(22, [20, 26])
        insert_animated(8, [20, 10])
        self.wait(1.6)

        bushy = VGroup(*[m for m in nodes.values()])
        self.play(bushy.animate.scale(0.62).shift(LEFT * 3.6 + DOWN * 0.4), run_time=1.1)
        lab_b = Text("arrivals: 20, 10, 26, 22, 8", font=FONT, font_size=22, color=GREY)
        lab_b.move_to(np.array([-3.6, -3.1, 0.0]))
        self.play(FadeIn(lab_b), run_time=0.5)

        cap5 = caption("same five values, arriving sorted: 8, 10, 20, 22, 26")
        self.play(Transform(cap, cap5), run_time=0.7)

        spine_pos = {v: np.array([0.9 + i * 0.95, 2.0 - i * 1.05, 0.0])
                     for i, v in enumerate([8, 10, 20, 22, 26])}
        snodes = {}
        prev = None
        for v in [8, 10, 20, 22, 26]:
            if prev is not None:
                for p in [8, 10, 20, 22, 26][: [8, 10, 20, 22, 26].index(v)]:
                    self.play(Indicate(snodes[p], color=RED, scale_factor=1.1), run_time=0.42)
            n = tree_node(v, spine_pos[v], color=RED)
            self.play(FadeIn(n), run_time=0.55)
            snodes[v] = n
            if prev is not None:
                d = spine_pos[v] - spine_pos[prev]
                u = d / np.linalg.norm(d)
                e = Line(spine_pos[prev] + u * R, spine_pos[v] - u * R, color=GREY, stroke_width=2.5)
                self.play(Create(e), run_time=0.4)
                snodes[(prev, v)] = e
            prev = v
        cap6 = caption("every insert walks the whole spine — the tree has become a linked list")
        self.play(Transform(cap, cap6), run_time=0.8)
        self.wait(3.2)

        spine = VGroup(*[m for m in snodes.values()])
        self.play(FadeOut(spine), FadeOut(lab_b), run_time=0.8)
        self.play(bushy.animate.scale(1 / 0.62).shift(RIGHT * 3.6 + UP * 0.4), run_time=1.1)

        # ============================== Act 3 — the walk that comes out sorted
        cap7 = caption("walk the contour — emit each node as you pass under it")
        self.play(Transform(cap, cap7), run_time=0.8)

        # output row
        slots = VGroup()
        for i in range(5):
            sq = Square(side_length=0.95, color=GREY, stroke_width=2)
            sq.move_to(np.array([-2.6 + i * 1.3, -3.0, 0.0]))
            slots.add(sq)
        self.play(FadeIn(slots), run_time=0.7)

        under = {v: POS[v] + DOWN * (R + 0.18) for v in POS}
        waypoints = [
            POS[20] + UP * (R + 0.25),                 # start above root
            POS[20] + LEFT * (R + 0.25),
            POS[10] + LEFT * (R + 0.30) + UP * 0.3,
            POS[8] + LEFT * (R + 0.28),
            under[8],                                   # emit 8
            POS[8] + RIGHT * (R + 0.28),
            under[10],                                  # emit 10
            POS[10] + RIGHT * (R + 0.30) + UP * 0.1,
            under[20],                                  # emit 20
            POS[26] + LEFT * (R + 0.30) + DOWN * 0.1,
            POS[22] + LEFT * (R + 0.28),
            under[22],                                  # emit 22
            POS[22] + RIGHT * (R + 0.28),
            under[26],                                  # emit 26
            POS[26] + RIGHT * (R + 0.30),
            POS[20] + UP * (R + 0.25) + RIGHT * 0.3,
        ]
        emit_at = {4: (8, 0), 6: (10, 1), 8: (20, 2), 11: (22, 3), 13: (26, 4)}

        walker = Dot(waypoints[0], radius=0.09, color=AMBER)
        trail = VMobject(color=AMBER, stroke_width=2.5)
        trail.set_points_as_corners([waypoints[0], waypoints[0]])
        self.add(trail, walker)

        pts_so_far = [waypoints[0]]
        for i in range(1, len(waypoints)):
            seg = Line(waypoints[i - 1], waypoints[i])
            dist = np.linalg.norm(waypoints[i] - waypoints[i - 1])
            self.play(MoveAlongPath(walker, seg), run_time=max(0.45, dist * 0.55),
                      rate_func=lambda s: s)
            pts_so_far.append(waypoints[i])
            trail.set_points_as_corners(pts_so_far)
            if i in emit_at:
                v, slot = emit_at[i]
                out = Text(str(v), font=FONT, font_size=26, color=GREEN)
                out.move_to(walker.get_center())
                self.add(out)
                self.play(out.animate.move_to(slots[slot].get_center()), run_time=0.9)
                self.wait(0.5)

        cap8 = caption("in-order traversal of a binary search tree: sorted — every time")
        self.play(Transform(cap, cap8), run_time=0.9)
        self.wait(4.0)
