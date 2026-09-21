"""Manim scenes for [[Data Protection and Privacy]].
Scene 1  Linkage       — a hospital release with the names removed meets a public list with
                         names.  Rows join on (district, birth date, sex); a name lands
                         beside a diagnosis.
Scene 2  Differencing  — two harmless totals whose difference is one person's salary; then
                         the same two questions answered with Laplace noise.
Smoke:  manim -ql --fps 15 data-protection-privacy-manim.py Linkage Differencing
Final:  manim -qk data-protection-privacy-manim.py Linkage Differencing   then concat with ffmpeg.
All people are invented."""
import numpy as np
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b"


def table(rows, header, col_x, top, size=20, colour=GREY_T):
    out = VGroup()
    head = VGroup(*[Text(h, font_size=size - 2, color=colour, weight=BOLD).move_to([x, top, 0]) for h, x in zip(header, col_x)])
    out.add(head)
    for r, row in enumerate(rows):
        line = VGroup(*[Text(str(c), font_size=size, color=GREY_T).move_to([x, top - 0.55 * (r + 1), 0]) for c, x in zip(row, col_x)])
        out.add(line)
    return out


class Linkage(Scene):
    def construct(self):
        title = Text("The names were removed. Were the people?", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        hospital = [("D07", "1988-03-14", "F", "asthma"), ("D12", "2001-11-02", "M", "depression"), ("D07", "1975-06-30", "M", "diabetes"),
                    ("D31", "1993-01-09", "F", "HIV"), ("D12", "1964-08-21", "F", "hypertension"), ("D19", "2006-05-17", "M", "asthma")]
        public = [("Chen Yu", "D12", "2001-11-02", "M"), ("Li Na", "D31", "1993-01-09", "F"), ("Wang Lei", "D19", "1990-02-28", "M"), ("Zhao Min", "D07", "1988-03-14", "F")]
        lx = [-6.1, -4.6, -3.15, -1.75]; rx = [1.5, 3.2, 4.7, 6.2]
        lt = Text("hospital release: no names", font_size=20, color=BLUE_H).move_to([-3.9, 2.55, 0])
        rt = Text("marathon results: public, with names", font_size=20, color=PURPLE_H).move_to([3.85, 2.55, 0])
        L = table(hospital, ["district", "born", "sex", "diagnosis"], lx, 2.0)
        R = table(public, ["name", "district", "born", "sex"], rx, 2.0)
        self.add(lt, rt, L, R); self.wait(2)
        note = Text("join the two on district + birth date + sex", font_size=22, color=AMBER_H).to_edge(DOWN, buff=0.9)
        counter = Text("names beside a diagnosis: 0", font_size=22, color=RED_H).to_edge(DOWN, buff=0.35)
        self.add(note, counter)
        found = 0
        for pi, person in enumerate(public):
            prow = R[pi + 1]
            box_r = SurroundingRectangle(VGroup(*prow[1:]), color=AMBER_H, buff=0.08, stroke_width=2)
            self.add(box_r); self.wait(0.5)
            hit = None
            for hi, h in enumerate(hospital):
                hrow = L[hi + 1]
                box_l = SurroundingRectangle(VGroup(*hrow[:3]), color=AMBER_H, buff=0.08, stroke_width=2)
                self.add(box_l); self.wait(0.22)
                if h[:3] == person[1:]:
                    hit = (hrow, box_l); break
                self.remove(box_l)
            if hit:
                hrow, box_l = hit
                found += 1
                link = Line(box_l.get_right(), box_r.get_left(), color=RED_H, stroke_width=3)
                verdict = Text(f"{person[0]}: {hospital[hi][3]}", font_size=22, color=RED_H).move_to([0, -1.75 - 0.0 * found, 0]).shift(DOWN * 0.42 * (found - 1))
                box_l.set_color(RED_H); box_r.set_color(RED_H); prow[0].set_color(RED_H); hrow[3].set_color(RED_H)
                self.add(link, verdict)
                counter.become(Text(f"names beside a diagnosis: {found}", font_size=22, color=RED_H).to_edge(DOWN, buff=0.35))
                self.wait(1.4)
                self.remove(link)
            else:
                miss = Text("no match", font_size=18, color=GREEN_H).next_to(box_r, RIGHT, buff=0.1)
                self.add(miss); self.wait(0.8); self.remove(miss, box_r)
        self.remove(note)
        end = Text("no single column names anyone; three columns together name almost everyone", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.9)
        self.add(end); self.wait(3)


class Differencing(Scene):
    def construct(self):
        title = Text("Two harmless questions, one private answer", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        q1 = Text("Q1  total payroll, all 5 000 staff", font_size=24, color=BLUE_H).move_to([-2.2, 2.2, 0]).align_to([-5.6, 0, 0], LEFT)
        q2 = Text("Q2  total payroll, everyone except employee #7", font_size=24, color=BLUE_H).move_to([-1.18, 1.5, 0]).align_to([-5.6, 0, 0], LEFT)
        a1 = Text("56 738 400", font_size=24, color=GREY_T).move_to([4.6, 2.2, 0])
        a2 = Text("56 734 900", font_size=24, color=GREY_T).move_to([4.6, 1.5, 0])
        self.add(q1); self.wait(0.8); self.add(a1); self.wait(0.8); self.add(q2); self.wait(0.8); self.add(a2); self.wait(1)
        rule = Line([3.4, 1.15, 0], [5.8, 1.15, 0], color=GREY_T)
        diff = Text("Q1 − Q2 = 3 500", font_size=26, color=RED_H).move_to([4.2, 0.75, 0])
        who = Text("employee #7's salary, exactly. No record was ever opened.", font_size=22, color=RED_H).move_to([0, 0.1, 0])
        self.add(rule, diff); self.wait(1.2); self.add(who); self.wait(2.5)
        fix = Text("now answer every query with a little random noise (differential privacy, ε = 1)", font_size=22, color=GREEN_H).move_to([0, -0.8, 0])
        self.add(fix); self.wait(1.5)
        rng = np.random.default_rng(4)
        for k in range(9):
            n1, n2 = 56738400 + rng.laplace(0, 60000), 56734900 + rng.laplace(0, 60000)
            a1.become(Text(f"{n1:,.0f}".replace(",", " "), font_size=24, color=GREEN_H).move_to([4.6, 2.2, 0]))
            a2.become(Text(f"{n2:,.0f}".replace(",", " "), font_size=24, color=GREEN_H).move_to([4.6, 1.5, 0]))
            diff.become(Text(f"Q1 − Q2 = {n1 - n2:,.0f}".replace(",", " "), font_size=26, color=GREEN_H).move_to([4.2, 0.75, 0]))
            who.become(Text("the difference is now noise, often negative: it says nothing about employee #7", font_size=22, color=GREEN_H).move_to([0, 0.1, 0]))
            self.wait(0.9)
        cost = Text("cost to the honest analyst: the total is off by about 0.1 %", font_size=22, color=GREY_T).move_to([0, -1.6, 0])
        dial = Text("privacy here is a dial you set, not a column you delete", font_size=22, color=GREY_T).move_to([0, -2.3, 0])
        self.add(cost); self.wait(1.5); self.add(dial); self.wait(3)
