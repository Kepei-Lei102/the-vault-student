"""Manim scene for [[Recording and Analysing Experimental Data]].
Scene  BestFitAndTriangle — five plotted points (Cambridge 0625, June 2024 Paper 62, Q1).  A ruler line is
        swung and slid until the points are balanced on either side; then the gradient is read from a
        SMALL triangle several times, each reading off by up to half a small square, and the answer
        jumps about; then from a LARGE triangle with the same reading errors, and it hardly moves.
Smoke:  manim -ql --fps 15 experimental-data-manim.py BestFitAndTriangle
Final:  manim -qk experimental-data-manim.py BestFitAndTriangle"""
import numpy as np
from manim import *

GREY_T, BLUE_H, GREEN_H, RED_H, AMBER_H = "#888888", "#2563eb", "#059669", "#dc2626", "#f59e0b"
M = np.array([100, 200, 300, 400, 500.0]); L = np.array([6.1, 10.0, 14.3, 18.3, 22.4])
G, C = np.polyfit(M, L, 1)


class BestFitAndTriangle(Scene):
    def construct(self):
        title = Text("A best-fit line, and the triangle that reads it", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        origin = np.array([-5.6, -2.6, 0]); W, H = 7.8, 5.0

        def P(m, l):
            return origin + np.array([m / 600 * W, l / 25 * H, 0])

        grid = VGroup()
        for k in range(0, 31):
            grid.add(Line(P(k * 20, 0), P(k * 20, 25), color=GREY_T, stroke_width=0.6 if k % 5 else 1.4, stroke_opacity=0.35 if k % 5 else 0.6))
        for k in range(0, 26):
            grid.add(Line(P(0, k), P(600, k), color=GREY_T, stroke_width=0.6 if k % 5 else 1.4, stroke_opacity=0.35 if k % 5 else 0.6))
        labels = VGroup(Text("m / g", font_size=18, color=GREY_T).next_to(P(300, 0), DOWN, buff=0.35),
                        Text("l / cm", font_size=18, color=GREY_T).rotate(PI / 2).next_to(P(0, 12.5), LEFT, buff=0.45))
        for m in (0, 200, 400, 600):
            labels.add(Text(str(m), font_size=16, color=GREY_T).next_to(P(m, 0), DOWN, buff=0.1))
        for l in (0, 10, 20):
            labels.add(Text(str(l), font_size=16, color=GREY_T).next_to(P(0, l), LEFT, buff=0.1))
        pts = VGroup(*[VGroup(Line(P(m, l) + 0.09 * (UL), P(m, l) + 0.09 * (DR), color=BLUE_H, stroke_width=4),
                              Line(P(m, l) + 0.09 * (UR), P(m, l) + 0.09 * (DL), color=BLUE_H, stroke_width=4)) for m, l in zip(M, L)])
        self.add(grid, labels, pts)
        side = np.array([4.6, 0, 0])
        g = ValueTracker(0.062); c = ValueTracker(-3.0)
        line = always_redraw(lambda: Line(P(0, c.get_value()), P(560, g.get_value() * 560 + c.get_value()), color=GREEN_H, stroke_width=3))

        def tally():
            above = int(np.sum(L > g.get_value() * M + c.get_value() + 0.06)); below = int(np.sum(L < g.get_value() * M + c.get_value() - 0.06))
            return VGroup(Text(f"points above the line: {above}", font_size=22, color=GREY_T).move_to(side + UP * 1.6),
                          Text(f"points below the line: {below}", font_size=22, color=GREY_T).move_to(side + UP * 1.05))
        t = always_redraw(tally)
        cap = Text("slide and swing the ruler until the points balance, all along the line", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(line, t, cap); self.wait(1.5)
        self.play(g.animate.set_value(0.030), c.animate.set_value(5.5), run_time=3)
        self.play(g.animate.set_value(G), c.animate.set_value(C), run_time=3.5)
        self.wait(1.5)
        self.remove(t, cap)
        rng = np.random.default_rng(3)

        def read(x1, x2, name, colour, n=9):
            head = Text(name, font_size=22, color=colour).move_to(side + UP * 1.6)
            cap2 = Text("each corner is read to within half a small square", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
            self.add(head, cap2)
            values = []
            shown = VGroup()
            for k in range(n):
                y1 = G * x1 + C + rng.normal(0, 0.1); y2 = G * x2 + C + rng.normal(0, 0.1)
                tri = VGroup(DashedLine(P(x1, y1), P(x2, y1), color=colour, stroke_width=3), DashedLine(P(x2, y1), P(x2, y2), color=colour, stroke_width=3),
                             Dot(P(x1, y1), color=colour, radius=0.06), Dot(P(x2, y2), color=colour, radius=0.06))
                val = (y2 - y1) / (x2 - x1); values.append(val)
                txt = Text(f"gradient = {val:.4f}", font_size=24, color=colour).move_to(side + UP * 0.9)
                self.add(tri, txt); self.wait(0.75); self.remove(tri, txt)
            spread = Text(f"from {min(values):.4f} to {max(values):.4f}", font_size=22, color=colour).move_to(side + UP * 0.9)
            pc = Text(f"a spread of {100*(max(values)-min(values))/G:.0f} %", font_size=22, color=colour).move_to(side + UP * 0.35)
            self.add(spread, pc); self.wait(2.2)
            self.remove(head, cap2)
            return VGroup(spread, pc)

        a = read(200, 300, "small triangle", RED_H)
        self.play(a.animate.shift(DOWN * 2.2).scale(0.85), run_time=0.8)
        small_tag = Text("small triangle", font_size=18, color=RED_H).next_to(a, UP, buff=0.12); self.add(small_tag)
        b = read(50, 500, "large triangle", GREEN_H)
        cap = Text("same line, same care: the long base divides the reading error away", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(cap); self.wait(3.5)
