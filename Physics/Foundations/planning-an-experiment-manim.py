"""Manim scenes for [[Planning an Experiment]].
Scene 1  FanOfLines   — five noisy readings and a best-fit line, again and again.  With the
                        lengths bunched together the lines fan out; spread across the whole
                        wire, the same instruments give a tight bundle.
Scene 2  KettleDrift  — five cooling trials done in order while the kettle cools: each point
                        lands off the true curve, and the conclusion moves with the order.
Smoke:  manim -ql --fps 15 planning-an-experiment-manim.py FanOfLines KettleDrift
Final:  manim -qk planning-an-experiment-manim.py FanOfLines KettleDrift   then concat with ffmpeg."""
import numpy as np
from manim import *

GREY_T, BLUE_H, GREEN_H, RED_H, AMBER_H = "#888888", "#2563eb", "#059669", "#dc2626", "#f59e0b"
TRUE_K, SIGMA = 5.20, 0.08


class FanOfLines(Scene):
    def construct(self):
        title = Text("Same wire, same meters, same noise: only the plan differs", font_size=24, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        rng = np.random.default_rng(5)
        for lo, hi, label, col in [(0.40, 0.60, "plan A: five lengths between 0.40 m and 0.60 m", RED_H),
                                   (0.10, 1.00, "plan B: five lengths between 0.10 m and 1.00 m", GREEN_H)]:
            ax = Axes(x_range=[0, 1.05, 0.2], y_range=[0, 6, 1], x_length=9, y_length=4.6,
                      axis_config={"color": GREY_T, "include_tip": False}).shift(DOWN * 0.2)
            xl = Text("length of wire / m", font_size=16, color=GREY_T).next_to(ax.x_axis, DOWN, buff=0.15)
            yl = Text("resistance / Ω", font_size=16, color=GREY_T).rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.15)
            tag = Text(label, font_size=20, color=col).next_to(title, DOWN, buff=0.12)
            band = Rectangle(width=ax.c2p(hi, 0)[0] - ax.c2p(lo, 0)[0], height=4.6, stroke_width=0, fill_color=col, fill_opacity=0.10)
            band.move_to([(ax.c2p(lo, 0)[0] + ax.c2p(hi, 0)[0]) / 2, ax.c2p(0, 3)[1], 0])
            counter = Text("", font_size=20, color=GREY_T).to_edge(DOWN, buff=0.2)
            ticks = VGroup(*[Text(f"{v:.1f}", font_size=14, color=GREY_T).next_to(ax.c2p(v, 0), DOWN, buff=0.08) for v in (0.2, 0.4, 0.6, 0.8, 1.0)],
                           *[Text(str(v), font_size=14, color=GREY_T).next_to(ax.c2p(0, v), LEFT, buff=0.08) for v in range(1, 7)])
            xl.shift(DOWN * 0.2); yl.shift(LEFT * 0.25)
            self.add(ax, xl, yl, tag, band, counter, ticks)
            L = np.linspace(lo, hi, 5); grads = []; old = VGroup(); self.add(old)
            for k in range(24):
                R = TRUE_K * L + rng.normal(0, SIGMA, 5)
                m, c = np.polyfit(L, R, 1); grads.append(m)
                pts = VGroup(*[Cross(scale_factor=0.07, stroke_color=GREY_T, stroke_width=3).move_to(ax.c2p(x, y)) for x, y in zip(L, R)])
                y0, y1 = np.clip(c, 0, 6), np.clip(m * 1.05 + c, 0, 6)
                line = Line(ax.c2p(0, max(c, 0)), ax.c2p(1.05, min(m * 1.05 + c, 6)), color=col, stroke_width=2.5)
                self.add(pts, line)
                counter.become(Text(f"experiment {k+1}:  gradient {m:.2f} Ω/m     spread so far ±{np.std(grads):.2f}", font_size=20, color=GREY_T).to_edge(DOWN, buff=0.2))
                self.wait(0.5 if k < 4 else 0.22)
                self.remove(pts); line.set_stroke(width=1.2, opacity=0.4); old.add(line)
            self.wait(1.5)
            self.remove(ax, xl, yl, tag, band, counter, ticks, *old)
        end = Text("a wide range pins the line down: narrow ±0.4 Ω/m, wide ±0.1 Ω/m, true value 5.20", font_size=22, color=GREY_T)
        self.add(end); self.wait(2.5)


class KettleDrift(Scene):
    def construct(self):
        title = Text("An uncontrolled variable: the kettle cools while you work", font_size=24, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        ROOM = 22.0
        def rate(t, s, minutes=5.0):
            k = 0.060 / (1 + 0.35 * t); return (s - (ROOM + (s - ROOM) * np.exp(-k * minutes))) / minutes
        thick = np.array([0, 2, 4, 6, 8.0]); start = 88.0 - 4.0 * np.arange(5)
        ax = Axes(x_range=[0, 9, 2], y_range=[0, 4, 1], x_length=8, y_length=4.4, axis_config={"color": GREY_T, "include_tip": False}).shift(DOWN * 0.5 + LEFT * 1.2)
        xl = Text("thickness of insulation / mm", font_size=16, color=GREY_T).next_to(ax.x_axis, DOWN, buff=0.15)
        yl = Text("rate of cooling / °C per minute", font_size=16, color=GREY_T).rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.15)
        tt = np.linspace(0, 8, 60)
        true_curve = ax.plot_line_graph(tt, rate(tt, 80.0), line_color=GREEN_H, add_vertex_dots=False, stroke_width=3)
        lab = Text("start held at 80 °C", font_size=18, color=GREEN_H).next_to(ax.c2p(3.2, rate(3.2, 80)), UR, buff=0.25)
        ticks = VGroup(*[Text(str(v), font_size=14, color=GREY_T).next_to(ax.c2p(v, 0), DOWN, buff=0.08) for v in (2, 4, 6, 8)],
                       *[Text(str(v), font_size=14, color=GREY_T).next_to(ax.c2p(0, v), LEFT, buff=0.08) for v in (1, 2, 3, 4)])
        xl.shift(DOWN * 0.2); yl.shift(LEFT * 0.25)
        self.add(ax, xl, yl, true_curve, lab, ticks)
        kettle = Text("kettle: 88 °C", font_size=22, color=AMBER_H).to_corner(UR, buff=0.5).shift(DOWN * 0.6)
        self.add(kettle); self.wait(1)
        for order, col, name in [(range(5), RED_H, "thin first"), (range(4, -1, -1), AMBER_H, "thick first")]:
            note = Text(f"trials done {name}", font_size=20, color=col).next_to(kettle, DOWN, buff=0.25)
            self.add(note); dots = VGroup(); self.add(dots)
            for n, i in enumerate(order):
                s = start[n]
                kettle.become(Text(f"kettle: {s:.0f} °C", font_size=22, color=AMBER_H).move_to(kettle))
                d = Dot(ax.c2p(thick[i], rate(thick[i], s)), color=col, radius=0.09)
                gap = DashedLine(ax.c2p(thick[i], rate(thick[i], 80.0)), d.get_center(), color=col, stroke_width=2)
                dots.add(d, gap); self.wait(0.9)
            first, last = rate(thick[0], start[list(order).index(0)]), rate(thick[4], start[list(order).index(4)])
            verdict = Text(f"8 mm appears to cut the rate by {100*(1-last/first):.0f} %   (truth: 71 %)", font_size=20, color=col).to_edge(DOWN, buff=0.25)
            self.add(verdict); self.wait(2.2)
            self.remove(note, verdict); dots.set_opacity(0.3)
        end = Text("control the start temperature, and the order stops mattering", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.25)
        self.add(end); self.wait(2.5)
