"""The laser printer — drawing with static electricity, in five stages.

Renders io-laser-printer.mp4 (embed beside the card).
Smoke: manim -qm io-laser-printer.py LaserPrinter
Final: manim -qk io-laser-printer.py LaserPrinter
"""
import numpy as np
from manim import *

BLUE_ = "#2563eb"
AMBER = "#f59e0b"
TEAL = "#0891b2"
GREEN = "#059669"
RED_ = "#dc2626"
GRAY = "#9a9a9a"

config.background_color = "#1a1a1a"

CENTER_D = np.array([-1.6, 0.75, 0])


def rim(angle_deg, radius=1.42):
    a = angle_deg * DEGREES
    return CENTER_D + radius * np.array([np.cos(a), np.sin(a), 0])


class LaserPrinter(Scene):
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=28, color=color).to_edge(DOWN, buff=0.3)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap), FadeIn(cap), run_time=0.6)
        else:
            self.play(FadeIn(cap), run_time=0.6)
        self._cap = cap

    def construct(self):
        title = Text("The laser printer - drawing with static electricity",
                     font_size=32, color=GRAY).to_edge(UP, buff=0.25)

        # ---- the machine ----
        drum = Circle(radius=1.55, stroke_color=GRAY, stroke_width=3).move_to(CENTER_D)
        lab_drum = Text("drum", font_size=24, color=GRAY).move_to(CENTER_D + np.array([0, 0.35, 0]))
        rot_arrow = CurvedArrow(CENTER_D + np.array([0.55, -0.75, 0]),
                                CENTER_D + np.array([-0.55, -0.75, 0]),
                                angle=-0.9, color=GRAY, stroke_width=2.5, tip_length=0.18)

        corona = Dot(rim(135, 2.1), radius=0.1, color=TEAL)
        lab_cor = Text("corona wire", font_size=22, color=TEAL).move_to([-4.65, 2.6, 0])

        laser_box = Rectangle(width=1.5, height=0.6, stroke_color=RED_, stroke_width=2.5,
                              fill_color=RED_, fill_opacity=0.12).move_to([2.9, 2.8, 0])
        lab_las = Text("laser", font_size=22, color=RED_).move_to([2.9, 2.8, 0])

        toner = Circle(radius=0.6, stroke_color=AMBER, stroke_width=2.5,
                       fill_color=AMBER, fill_opacity=0.3).move_to(rim(-15, 2.35))
        lab_ton = Text("toner", font_size=22, color=AMBER).next_to(toner, RIGHT, buff=0.25)

        paper = Rectangle(width=3.4, height=0.34, stroke_color=GRAY, stroke_width=2,
                          fill_color=GRAY, fill_opacity=0.12).move_to([-5.2, -1.75, 0])
        lab_pap = Text("paper", font_size=22, color=GRAY).move_to([-5.2, -2.35, 0])

        fus1 = Circle(radius=0.34, stroke_color=RED_, stroke_width=2.5,
                      fill_color=RED_, fill_opacity=0.15).move_to([3.1, -1.42, 0])
        fus2 = fus1.copy().move_to([3.1, -2.08, 0])
        lab_fus = Text("fuser - heat", font_size=22, color=RED_).move_to([3.1, -2.75, 0])

        self.play(FadeIn(title), run_time=0.8)
        self.play(Create(drum), FadeIn(lab_drum), FadeIn(rot_arrow),
                  FadeIn(corona), FadeIn(lab_cor),
                  FadeIn(laser_box), FadeIn(lab_las),
                  FadeIn(toner), FadeIn(lab_ton),
                  FadeIn(paper), FadeIn(lab_pap),
                  FadeIn(fus1), FadeIn(fus2), FadeIn(lab_fus),
                  run_time=2.0)
        self.swap_caption("Five stations around a spinning drum. No ink anywhere.")
        self.wait(1.8)

        # ---- 1. CHARGE ----
        self.swap_caption("1. charge - the corona wire sprays the drum with uniform static.", TEAL)
        angles = [100 + 8.75 * i for i in range(9)]
        charge_dots = VGroup(*[Dot(rim(a), radius=0.075, color=TEAL) for a in angles])
        self.play(Flash(corona, color=TEAL, flash_radius=0.5),
                  LaggedStart(*[FadeIn(d) for d in charge_dots], lag_ratio=0.1),
                  run_time=1.4)
        self.wait(1.2)

        # ---- 2. WRITE ----
        self.play(Rotate(charge_dots, angle=-PI / 2, about_point=CENTER_D), run_time=1.4)
        self.swap_caption("2. write - the laser erases charge where the page stays white.", RED_)
        beam_end = rim(45, 1.55)
        erased = [charge_dots[2], charge_dots[5], charge_dots[7]]
        for tgt in erased:
            beam = Line([2.15, 2.7, 0], tgt.get_center(), color=RED_, stroke_width=3.5)
            self.play(Create(beam), run_time=0.25)
            self.play(FadeOut(beam), FadeOut(tgt), run_time=0.35)
        charge_dots.remove(*erased)
        self.wait(1.2)

        # ---- 3. DUST ----
        self.play(Rotate(charge_dots, angle=-PI / 3, about_point=CENTER_D), run_time=1.2)
        self.swap_caption("3. dust - charged toner powder clings only where charge remains.", AMBER)
        toner_dots = VGroup(*[Dot(d.get_center(), radius=0.1, color=AMBER) for d in charge_dots])
        self.play(Rotate(toner, angle=-PI / 2, about_point=toner.get_center()),
                  LaggedStart(*[GrowFromCenter(t) for t in toner_dots], lag_ratio=0.12),
                  run_time=1.4)
        self.wait(1.2)

        # ---- 4. TRANSFER ----
        self.swap_caption("4. transfer - the page rolls the pattern onto the paper.", GRAY)
        both = VGroup(charge_dots, toner_dots)
        self.play(paper.animate.move_to([-1.6, -1.75, 0]),
                  FadeOut(lab_pap),
                  Rotate(both, angle=-75 * DEGREES, about_point=CENTER_D),
                  run_time=1.5)
        drops = []
        for t in toner_dots:
            x = t.get_center()[0]
            drops.append(t.animate.move_to([x, -1.58, 0]))
        self.play(*drops, *[FadeOut(c) for c in charge_dots], run_time=1.1)
        self.wait(1.0)

        # ---- 5. FUSE ----
        self.swap_caption("5. fuse - heat and pressure melt the toner in. It is permanent.", RED_)
        sheet = VGroup(paper, toner_dots)
        self.play(sheet.animate.shift(RIGHT * 5.5),
                  Succession(
                      AnimationGroup(fus1.animate(run_time=0.7).set_fill(RED_, opacity=0.5),
                                     fus2.animate(run_time=0.7).set_fill(RED_, opacity=0.5)),
                      AnimationGroup(fus1.animate(run_time=1.0).set_fill(RED_, opacity=0.15),
                                     fus2.animate(run_time=1.0).set_fill(RED_, opacity=0.15)),
                  ),
                  run_time=2.2)
        xs = [t.get_center()[0] for t in toner_dots]
        bar = RoundedRectangle(corner_radius=0.06, width=max(xs) - min(xs) + 0.35, height=0.16,
                               stroke_color=AMBER, stroke_width=2,
                               fill_color=AMBER, fill_opacity=0.8)
        bar.move_to([(max(xs) + min(xs)) / 2, -1.58, 0])
        self.play(ReplacementTransform(toner_dots, bar), run_time=0.9)
        self.wait(1.0)

        # ---- closing ----
        verdict = Text("toner, not ink", font_size=36, color=AMBER, weight=BOLD).move_to([4.6, 1.5, 0])
        self.play(FadeIn(verdict), run_time=0.7)
        self.swap_caption("Dry powder, charge, light and heat - the page comes out warm.")
        self.wait(2.8)
