"""Manim: Hash Tables — see it run.

Act 1  Calculate, don't search: key 528 goes through MOD 100 straight to its
       slot while a linear search crawls.
Act 2  Collisions arrive on schedule (the birthday paradox), and the three
       policies answer: walk the row, use the spare, probe onward.
Act 3  The load factor climbs, probes lengthen — then the REHASH: double the
       slots, re-scatter everything, and the table breathes again.

Paced slowly per house rule.

Render (from this folder):
    manim -ql hash-tables-see-it-run.py HashTablesSeeItRun    # smoke
    manim -qk hash-tables-see-it-run.py HashTablesSeeItRun    # 4K final
Copy media/videos/hash-tables-see-it-run/2160p60/HashTablesSeeItRun.mp4
  -> hash-tables-see-it-run.mp4 beside the card, then rm -rf media/ __pycache__/.
"""

import numpy as np
from manim import (
    Scene, VGroup, Text, Square, Rectangle, RoundedRectangle, Line, Dot,
    SurroundingRectangle, FadeIn, FadeOut, Create, Transform, Indicate, Flash,
    UP, DOWN, LEFT, RIGHT, config,
)

BG = "#1e1e1e"; TXT = "#cccccc"; GREY = "#9a9a9a"
BLUE = "#2563eb"; GREEN = "#059669"; AMBER = "#f59e0b"; RED = "#dc2626"; TEAL = "#0891b2"; PURPLE = "#7c3aed"
FONT = "Helvetica Neue"
config.background_color = BG


def caption(s, size=25):
    return Text(s, font=FONT, font_size=size, color=TXT).to_edge(UP, buff=0.3)


def slot_row(n, y, w=0.82, labels=None, x0=None):
    g = VGroup()
    x0 = -(n * w) / 2 + w / 2 if x0 is None else x0
    cells = []
    for i in range(n):
        sq = Square(side_length=w, color=GREY, stroke_width=2).move_to(np.array([x0 + i * w, y, 0]))
        idx = Text(str(i), font=FONT, font_size=14, color=GREY).next_to(sq, UP, buff=0.08)
        g.add(sq, idx)
        cells.append(sq)
    return g, cells


def key_chip(k, pos, color=BLUE):
    r = RoundedRectangle(corner_radius=0.1, width=1.1, height=0.5, color=color,
                         fill_color=color, fill_opacity=0.18, stroke_width=2.4).move_to(pos)
    t = Text(str(k), font=FONT, font_size=19, color=TXT).move_to(pos)
    return VGroup(r, t)


class HashTablesSeeItRun(Scene):
    def construct(self):
        # ================= Act 1 — calculate, don't search
        cap = caption("one structure searches; the other calculates")
        self.play(FadeIn(cap), run_time=0.9)
        row_g, cells = slot_row(10, -2.2)
        self.play(FadeIn(row_g), run_time=0.8)
        fnbox = RoundedRectangle(corner_radius=0.12, width=2.9, height=0.9, color=PURPLE,
                                 fill_color=PURPLE, fill_opacity=0.15, stroke_width=2.6)
        fnbox.move_to(np.array([0, 0.4, 0]))
        fntxt = Text("key MOD 10", font=FONT, font_size=22, color=TXT).move_to(fnbox)
        self.play(FadeIn(fnbox), FadeIn(fntxt), run_time=0.7)

        chip = key_chip(528, np.array([0, 2.2, 0]))
        self.play(FadeIn(chip), run_time=0.6)
        self.wait(1.2)
        self.play(chip.animate.move_to(fnbox.get_center() + UP * 0.0), run_time=0.9)
        result = Text("= 8", font=FONT, font_size=22, color=AMBER).next_to(fnbox, RIGHT, buff=0.25)
        self.play(FadeIn(result), Flash(fnbox, color=PURPLE, flash_radius=1.6), run_time=0.8)
        self.play(chip.animate.scale(0.72).move_to(cells[8].get_center()), run_time=1.1)
        cells[8].set_stroke(GREEN)
        cap2 = caption("528 MOD 10 = 8 — straight to slot 8, one step, any table size")
        self.play(Transform(cap, cap2), run_time=0.8)
        self.wait(2.4)

        # the crawling comparison
        crawler = Dot(cells[0].get_center() + UP * 0.0, radius=0.09, color=RED)
        cap3 = caption("a search would have interviewed every slot on the way")
        self.play(Transform(cap, cap3), FadeIn(crawler), run_time=0.6)
        for i in range(1, 9):
            self.play(crawler.animate.move_to(cells[i].get_center()), run_time=0.28,
                      rate_func=lambda s: s)
        self.play(FadeOut(crawler), run_time=0.5)
        self.wait(1.6)
        self.play(FadeOut(chip), FadeOut(result), run_time=0.5)

        # ================= Act 2 — collisions, three answers
        cap4 = caption("more keys arrive — and by the birthday paradox, a clash comes early")
        self.play(Transform(cap, cap4), run_time=0.8)
        c17 = key_chip(17, np.array([-2.4, 2.2, 0]), GREEN)
        self.play(FadeIn(c17), run_time=0.5)
        self.play(c17.animate.scale(0.72).move_to(cells[7].get_center()), run_time=0.9)
        cells[7].set_stroke(GREEN)
        c27 = key_chip(27, np.array([2.4, 2.2, 0]), AMBER)
        self.play(FadeIn(c27), run_time=0.5)
        self.play(c27.animate.scale(0.72).move_to(cells[7].get_center() + UP * 0.75), run_time=0.9)
        clash = SurroundingRectangle(cells[7], color=RED, buff=0.03, stroke_width=3)
        cap5 = caption("27 MOD 10 = 7 as well — the slot is taken. three answers:")
        self.play(Transform(cap, cap5), Create(clash), run_time=0.9)
        self.wait(1.4)

        a1 = Text("1 walk the bucket row (N25/41)", font=FONT, font_size=20, color=TEAL)
        a2 = Text("2 put it in the Spare array (J25/42)", font=FONT, font_size=20, color=TEAL)
        a3 = Text("3 probe to the next slot — MOD wraps (classic)", font=FONT, font_size=20, color=TEAL)
        a1.move_to(np.array([-3.6, 1.35, 0])); a2.move_to(np.array([-3.45, 0.9, 0])); a3.move_to(np.array([-2.85, 0.45, 0]))
        self.play(FadeIn(a1), run_time=0.7); self.wait(0.7)
        self.play(FadeIn(a2), run_time=0.7); self.wait(0.7)
        self.play(FadeIn(a3), run_time=0.7); self.wait(0.9)
        self.play(FadeOut(clash), c27.animate.move_to(cells[8].get_center() + UP * 0.75), run_time=0.9)
        self.play(c27.animate.move_to(cells[8].get_center()), FadeOut(chip) if False else FadeIn(VGroup()), run_time=0.7)
        cap6 = caption("probing chosen: 27 slides to slot 8 — remember the path it took")
        self.play(Transform(cap, cap6), run_time=0.8)
        self.wait(2.2)
        self.play(FadeOut(a1), FadeOut(a2), FadeOut(a3), FadeOut(fnbox), FadeOut(fntxt), run_time=0.6)

        # ================= Act 3 — load factor and the rehash
        cap7 = caption("the table fills — the load factor climbs, and probes grow teeth")
        self.play(Transform(cap, cap7), run_time=0.8)
        fillers = []
        for i in (0, 1, 2, 4, 5, 9):
            f = Square(side_length=0.82, color=AMBER, fill_color=AMBER, fill_opacity=0.25,
                       stroke_width=2).move_to(cells[i].get_center())
            fillers.append(f)
        self.play(*[FadeIn(f) for f in fillers], run_time=1.1)
        alpha = Text("load factor = 9/10", font=FONT, font_size=21, color=AMBER)
        alpha.move_to(np.array([4.6, 1.2, 0]))
        self.play(FadeIn(alpha), run_time=0.6)
        probe = Dot(cells[3].get_center(), radius=0.09, color=RED)
        cap8 = caption("a find that hashes to 3 must now walk 3, 4, 5 … the clusters have merged")
        self.play(Transform(cap, cap8), FadeIn(probe), run_time=0.8)
        for i in (4, 5, 6):
            self.play(probe.animate.move_to(cells[i].get_center()), run_time=0.45,
                      rate_func=lambda s: s)
        self.play(FadeOut(probe), run_time=0.4)
        self.wait(1.2)

        cap9 = caption("the cure: REHASH — double the slots, re-scatter every key")
        self.play(Transform(cap, cap9), run_time=0.9)
        big_g, big_cells = slot_row(16, -3.2, w=0.62)
        self.play(FadeIn(big_g), run_time=0.9)
        movers = [chip, c17, c27] + fillers
        import random
        random.seed(3)
        targets = random.sample(range(16), len(movers))
        self.play(*[m.animate.scale(0.8).move_to(big_cells[t].get_center())
                    for m, t in zip(movers, targets)],
                  FadeOut(row_g), run_time=1.8)
        cap10 = caption("every index changes — MOD 16 is a new world — and lookups are one step again")
        self.play(Transform(cap, cap10), run_time=0.9)
        na = Text("load factor = 9/16", font=FONT, font_size=21, color=GREEN).move_to(alpha)
        self.play(Transform(alpha, na), run_time=0.6)
        self.wait(2.2)
        cap11 = caption("average O(1), amortised across the rare expensive evening — a dict's whole life")
        self.play(Transform(cap, cap11), run_time=0.9)
        self.wait(3.4)
