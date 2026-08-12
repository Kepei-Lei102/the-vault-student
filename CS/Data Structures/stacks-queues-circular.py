"""Stacks and Queues — the walking-queue bug and the circular fix.

Beat 1: a linear array queue inchworms right — "full" while holding
        four items and four ghosts.
Beat 2: bend the array into a ring — (p + 1) MOD 8 — and the ghosts
        come back around.
Beat 3: full and empty give identical pointers; only the count can tell.

Render:  manim -qk stacks-queues-circular.py CircularQueue
House style: bg #1a1a1a, captions #9a9a9a, teal data, amber pointers.
Deterministic (no random data), so no seed stamp.
"""

from manim import *

BG = "#1a1a1a"
GRAYT = "#9a9a9a"
TEAL = "#0891b2"
AMBER = "#f59e0b"
RED = "#dc2626"

config.background_color = BG

N = 8
RING_R = 2.05
RING_C = np.array([0, 0.48, 0])


def ring_pos(i, r=RING_R):
    a = PI / 2 - i * TAU / N
    return RING_C + r * np.array([np.cos(a), np.sin(a), 0])


class CircularQueue(Scene):
    def swap_caption(self, text, color=GRAYT, font_size=30):
        cap = Text(text, color=color, font_size=font_size, line_spacing=0.9)
        cap.move_to(DOWN * 3.35)
        anims = [FadeIn(cap, run_time=0.35)]
        if getattr(self, "_cap", None) is not None:
            anims.append(FadeOut(self._cap, run_time=0.25))
        self._cap = cap
        self.play(*anims)

    def make_marker(self, letter):
        tri = Triangle(color=AMBER, fill_opacity=1, stroke_width=0).scale(0.13)
        lab = Text(letter, color=AMBER, font_size=26)
        lab.next_to(tri, DOWN, buff=0.12)
        return VGroup(tri, lab)

    def set_count(self, k):
        new = Text(f"NumberInQueue = {k}", color=GRAYT, font_size=26)
        new.to_corner(UL).shift(DOWN * 0.1)
        if getattr(self, "_count", None) is None:
            self._count = new
            return FadeIn(new, run_time=0.3)
        old, self._count = self._count, new
        return AnimationGroup(FadeOut(old, run_time=0.2),
                              FadeIn(new, run_time=0.3))

    # ------------------------------------------------------------------
    def marker_target(self, marker, i):
        if self.linear:
            x = -3.5 + i
            y = 0.72 if marker is self.h_marker else 0.10
            return [x, y, 0]
        r = RING_R + (0.78 if marker is self.h_marker else 1.32)
        return ring_pos(i, r)

    def do_enqueue(self, val, run_time=0.5):
        self.tail = (self.tail + 1) % N
        i = self.tail
        self.count += 1
        cell = self.cellgrp[i]
        anims = [self.t_marker.animate.move_to(self.marker_target(self.t_marker, i)),
                 cell[0].animate.set_fill(TEAL, 0.22),
                 self.set_count(self.count)]
        old = self.values[i]
        if old is not None:
            cell.remove(old)
            anims.append(FadeOut(old, run_time=run_time * 0.6))
        txt = Text(str(val), color=TEAL, font_size=30)
        txt.move_to(cell[0].get_center())
        self.values[i] = txt
        cell.add(txt)
        anims.append(FadeIn(txt))
        self.play(*anims, run_time=run_time)

    def do_dequeue(self, run_time=0.5):
        i = self.head
        txt = self.values[i]
        cell = self.cellgrp[i]
        self.head = (self.head + 1) % N
        self.count -= 1
        anims = [self.h_marker.animate.move_to(self.marker_target(self.h_marker, self.head)),
                 cell[0].animate.set_fill(TEAL, 0.05),
                 self.set_count(self.count)]
        if txt is not None:
            anims.append(txt.animate.set_color(GRAYT).set_opacity(0.3))
        self.play(*anims, run_time=run_time)

    # ------------------------------------------------------------------
    def construct(self):
        self.cellgrp = []
        self.values = [None] * N
        self.idx_labels = VGroup()
        for i in range(N):
            sq = Square(0.88).set_stroke(GRAYT, 2)
            grp = VGroup(sq).move_to([-3.5 + i, 1.5, 0])
            self.cellgrp.append(grp)
            lab = Text(str(i), color=GRAYT, font_size=22).set_opacity(0.7)
            lab.move_to([-3.5 + i, 2.28, 0])
            self.idx_labels.add(lab)

        self.h_marker = self.make_marker("H").move_to([-3.5, 0.60, 0])
        self.t_marker = self.make_marker("T").move_to([-3.5, -0.02, 0])
        self.linear = True
        self.head, self.tail, self.count = 0, -1, 0

        self.play(*[Create(g[0]) for g in self.cellgrp],
                  FadeIn(self.idx_labels), run_time=1.2)
        self.play(FadeIn(self.h_marker), FadeIn(self.t_marker),
                  self.set_count(0), run_time=0.6)
        self.swap_caption("a queue in a plain array — watch the pointers:\nthey only ever move right")

        for op, val in [("E", 5), ("E", 12), ("E", 9), ("D", None), ("D", None),
                        ("E", 4), ("E", 7), ("D", None), ("D", None),
                        ("E", 8), ("E", 3), ("E", 6)]:
            if op == "E":
                self.do_enqueue(val, run_time=0.42)
            else:
                self.do_dequeue(run_time=0.42)

        cross = VGroup(Line([4.1, 1.9, 0], [4.9, 1.1, 0]),
                       Line([4.1, 1.1, 0], [4.9, 1.9, 0])).set_stroke(RED, 6)
        self.swap_caption("Enqueue(2)? the tail is at the wall — refused as FULL,\nwhile holding four items and four unreachable ghosts")
        self.play(Create(cross), run_time=0.7)
        self.wait(2.4)
        self.play(FadeOut(cross), run_time=0.4)

        # ---------- bend into a ring ----------
        self.swap_caption("the fix is geometric — bend the array into a ring:\nevery pointer move becomes  (pointer + 1) MOD 8")
        moves = []
        for i in range(N):
            moves.append(self.cellgrp[i].animate.move_to(ring_pos(i)))
            moves.append(self.idx_labels[i].animate.move_to(
                ring_pos(i, RING_R - 0.92)))
        self.linear = False
        moves.append(self.h_marker.animate.move_to(
            self.marker_target(self.h_marker, self.head)))
        moves.append(self.t_marker.animate.move_to(
            self.marker_target(self.t_marker, self.tail)))
        self.play(*moves, run_time=2.2)
        self.wait(0.6)

        self.swap_caption("Enqueue(2): tail = (7 + 1) MOD 8 = 0 —\nthe ghost cells come back around")
        for val in [2, 11, 9, 5]:
            self.do_enqueue(val, run_time=0.55)
        self.wait(0.8)

        # ---------- full vs empty ----------
        self.swap_caption("FULL:  H = 4,  T = 3,  NumberInQueue = 8 —\nremember those two pointers")
        self.wait(2.2)
        self.swap_caption("now dequeue everything, all the way to empty")
        for _ in range(N):
            self.do_dequeue(run_time=0.3)
        self.swap_caption("EMPTY:  H = 4,  T = 3 — the SAME pointers;\nonly the count can tell full from empty")
        self.wait(3.2)
