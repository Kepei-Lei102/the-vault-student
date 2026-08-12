"""The interrupt detour, animated: the F-E cycle's hidden fourth beat.

Render (on the Mac, from this folder):
    manim -qm interrupt-cycle.py InterruptCycle   # smoke
    manim -qk interrupt-cycle.py InterruptCycle   # 4K final
Then copy the output MP4 beside the card as interrupt-cycle.mp4 and
clear media/ + __pycache__/.
"""

from manim import *

BG = "#1a1a1a"
GRAY = "#9a9a9a"
PURPLE = "#7c3aed"
BLUE = "#2563eb"
GREEN = "#059669"
AMBER = "#f59e0b"
TEAL = "#0891b2"
RED = "#dc2626"

config.background_color = BG


def node(label, color=PURPLE, w=2.0, h=0.7, fs=24):
    box = RoundedRectangle(
        corner_radius=0.12, width=w, height=h,
        stroke_color=color, stroke_width=3,
        fill_color=color, fill_opacity=0.12,
    )
    txt = Text(label, font_size=fs, color=GRAY, weight=BOLD).move_to(box)
    return VGroup(box, txt)


class InterruptCycle(Scene):
    def swap_caption(self, new_text, color=GRAY):
        cap = Text(new_text, font_size=27, color=color).to_edge(DOWN, buff=0.4)
        if self._cap is not None:
            self.play(FadeOut(self._cap, run_time=0.25), FadeIn(cap, run_time=0.35))
        else:
            self.play(FadeIn(cap, run_time=0.35))
        self._cap = cap

    def set_pc(self, value, color=GRAY):
        new_val = Text(value, font_size=26, color=color, weight=BOLD).move_to(self.pc_val)
        self.play(Transform(self.pc_val, new_val, run_time=0.35))

    def beat(self, target, dwell=0.35):
        self.play(self.hl.animate.become(
            SurroundingRectangle(target[0], color=YELLOW, corner_radius=0.14, buff=0.07, stroke_width=4)
        ), run_time=0.4)
        self.wait(dwell)

    def construct(self):
        self._cap = None

        # ---------- the cycle, left ----------
        center = LEFT * 3.3 + UP * 0.4
        R = 1.85
        fetch = node("FETCH").move_to(center + UP * R)
        decode = node("DECODE").move_to(center + LEFT * R * 1.28)
        execu = node("EXECUTE").move_to(center + DOWN * R)
        check = node("CHECK", color=AMBER).move_to(center + RIGHT * R * 1.28)

        arcs = VGroup(*[
            CurvedArrow(a.get_center() + (b.get_center() - a.get_center()) * 0.32,
                        b.get_center() - (b.get_center() - a.get_center()) * 0.32,
                        angle=-0.7, color=GRAY, stroke_width=2.5, tip_length=0.18)
            for a, b in [(fetch, decode), (decode, execu), (execu, check), (check, fetch)]
        ])
        cycle = VGroup(fetch, decode, execu, check, arcs)

        # ---------- PC register, top right ----------
        pc_box = RoundedRectangle(corner_radius=0.12, width=3.1, height=1.0,
                                  stroke_color=TEAL, stroke_width=3,
                                  fill_color=TEAL, fill_opacity=0.10).move_to(RIGHT * 4.3 + UP * 2.7)
        pc_lab = Text("PC", font_size=24, color=GRAY, weight=BOLD).next_to(pc_box, LEFT, buff=0.25)
        self.pc_val = Text("0x0100", font_size=26, color=GRAY, weight=BOLD).move_to(pc_box)

        # ---------- the stack, right ----------
        floor = Line(RIGHT * 2.9 + DOWN * 1.7, RIGHT * 5.7 + DOWN * 1.7, color=GRAY, stroke_width=4)
        stack_lab = Text("the stack", font_size=22, color=GRAY).next_to(floor, DOWN, buff=0.18)

        # ---------- interrupt flag, beside CHECK ----------
        flag = Square(side_length=0.34, stroke_color=GRAY, stroke_width=2.5,
                      fill_color=BG, fill_opacity=1.0).next_to(check, UP, buff=0.22)
        flag_lab = Text("flag", font_size=17, color=GRAY).next_to(flag, RIGHT, buff=0.12)

        self.play(FadeIn(cycle), FadeIn(pc_box), FadeIn(pc_lab), FadeIn(self.pc_val),
                  FadeIn(floor), FadeIn(stack_lab), FadeIn(flag), FadeIn(flag_lab), run_time=1.0)

        self.hl = SurroundingRectangle(fetch[0], color=YELLOW, corner_radius=0.14, buff=0.07, stroke_width=4)
        self.play(Create(self.hl), run_time=0.4)

        self.swap_caption("the cycle you know has a hidden fourth beat: check")

        # two calm loops
        for pc in ["0x0104", "0x0108"]:
            self.beat(decode)
            self.beat(execu)
            self.beat(check, dwell=0.45)
            self.beat(fetch)
            self.set_pc(pc)

        # ---------- the bell rings mid-instruction ----------
        device = node("keyboard", color=BLUE, w=2.0, h=0.6, fs=20).move_to(LEFT * 0.4 + DOWN * 2.9)
        self.beat(decode)
        self.play(FadeIn(device), run_time=0.4)
        bell = DashedLine(device.get_top(), flag.get_bottom(), color=BLUE, stroke_width=3)
        self.beat(execu, dwell=0.1)
        self.play(Create(bell), Flash(device, color=BLUE, flash_radius=0.9), run_time=0.6)
        self.play(flag.animate.set_fill(RED, opacity=1.0), run_time=0.35)
        self.swap_caption("a bell rings mid-instruction — the CPU finishes what it started", color=AMBER)
        self.wait(0.8)

        # ---------- the check catches it ----------
        self.beat(check, dwell=0.2)
        self.play(Indicate(check, color=AMBER, scale_factor=1.15), run_time=0.8)
        self.swap_caption("flag set — take the detour")

        # ---------- protect the scene ----------
        chip = VGroup(
            RoundedRectangle(corner_radius=0.1, width=2.6, height=0.62,
                             stroke_color=AMBER, stroke_width=3, fill_color=AMBER, fill_opacity=0.15),
            Text("PC 0x0108 + FLAGS", font_size=19, color=GRAY, weight=BOLD),
        )
        chip[1].move_to(chip[0])
        chip.move_to(pc_box.get_center())
        self.swap_caption("protect the scene — PC and registers go to the stack")
        self.play(FadeIn(chip, run_time=0.3))
        self.play(chip.animate.move_to(floor.get_center() + UP * 0.42), run_time=0.9)
        self.wait(0.4)

        # ---------- vector table ----------
        rows = VGroup(*[
            Text(s, font_size=20, color=GRAY)
            for s in ["IRQ 0   0x8000", "IRQ 1   0x8400", "IRQ 2   0x9000", "IRQ 3   0x9C00"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        table_box = SurroundingRectangle(rows, color=TEAL, corner_radius=0.12, buff=0.22, stroke_width=3)
        table_lab = Text("vector table", font_size=20, color=GRAY, weight=BOLD)
        table = VGroup(rows, table_box, table_lab).move_to(RIGHT * 4.3 + UP * 0.7)
        table_lab.next_to(table_box, UP, buff=0.15)
        self.swap_caption("the vector table turns a number into an address")
        self.play(FadeIn(table), run_time=0.6)
        row_hl = SurroundingRectangle(rows[2], color=AMBER, buff=0.08, stroke_width=3)
        self.play(Create(row_hl), run_time=0.5)
        self.set_pc("0x9000", color=AMBER)
        self.wait(0.5)

        # ---------- the ISR runs ----------
        isr_badge = Text("running: ISR", font_size=22, color=AMBER, weight=BOLD).move_to(center)
        self.swap_caption("the ISR — short and specific")
        self.play(FadeIn(isr_badge), run_time=0.4)
        for pc in ["0x9004", "0x9008"]:
            self.beat(decode, dwell=0.12)
            self.beat(execu, dwell=0.12)
            self.beat(check, dwell=0.12)
            self.beat(fetch, dwell=0.12)
            self.set_pc(pc, color=AMBER)

        # ---------- restore ----------
        self.swap_caption("restore — resume as if nothing had happened", color=GREEN)
        self.play(FadeOut(isr_badge), FadeOut(row_hl), FadeOut(table),
                  flag.animate.set_fill(BG, opacity=1.0), FadeOut(bell), run_time=0.6)
        self.play(chip.animate.move_to(pc_box.get_center()), run_time=0.9)
        self.play(FadeOut(chip), run_time=0.3)
        self.set_pc("0x0108", color=GREEN)
        self.wait(0.3)

        # one calm loop to close
        self.beat(decode)
        self.beat(execu)
        self.beat(check, dwell=0.4)
        self.beat(fetch)
        self.set_pc("0x010C")
        self.wait(1.2)
