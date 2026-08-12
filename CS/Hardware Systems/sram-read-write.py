# SRAM cell — hold / read / write (write = overpower the loop).
# Vault Manim source. Render on the Mac:
#   manim -qk sram-read-write.py SRAMReadWrite      # 4K showcase
#   manim -qh sram-read-write.py SRAMReadWrite      # 1080p quick
# then: cp media/videos/sram-read-write/*/SRAMReadWrite.mp4 sram-read-write.mp4 && rm -rf media
from manim import *

TXT = "#c8c8c8"; MUTE = "#9ca3af"
PURPLE = "#7c3aed"; GREEN = "#059669"; TEAL = "#0891b2"; AMBER = "#f59e0b"
RED = "#dc2626"; BLUE = "#2563eb"


class SRAMReadWrite(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"

        title = Text("SRAM cell — hold, read, write", color=TXT).scale(0.7).to_edge(UP)
        conv = Text("right node = Q   ·   left node = Q̄ (NOT Q)   ·   always opposite",
                    color=MUTE).scale(0.36).next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(conv))

        # --- build the cell ---------------------------------------------------
        A = Polygon([-0.75, 1.4, 0], [-0.75, 0.6, 0], [0.15, 1.0, 0],
                    color=PURPLE, fill_color=PURPLE, fill_opacity=0.15)
        B = Polygon([0.75, -0.6, 0], [0.75, -1.4, 0], [-0.15, -1.0, 0],
                    color=PURPLE, fill_color=PURPLE, fill_opacity=0.15)
        A_lbl = Text("NOT", color=PURPLE).scale(0.32).move_to([-0.45, 1.0, 0])
        B_lbl = Text("NOT", color=PURPLE).scale(0.32).move_to([0.45, -1.0, 0])

        # loop wires
        qbar = VMobject().set_points_as_corners(
            [[-0.75, 1.0, 0], [-1.15, 1.0, 0], [-1.15, -1.0, 0], [-0.15, -1.0, 0]]).set_stroke(MUTE, 3)
        q = VMobject().set_points_as_corners(
            [[0.15, 1.0, 0], [1.15, 1.0, 0], [1.15, -1.0, 0], [0.75, -1.0, 0]]).set_stroke(GREEN, 3)

        # word line + bit lines
        word = Line([-2.7, 2.4, 0], [2.7, 2.4, 0], color=MUTE)
        word_lbl = Text("word line", color=MUTE).scale(0.3).next_to(word, UP, buff=0.08).align_to(word, LEFT)
        blL = Line([-2.7, 2.4, 0], [-2.7, 0.7, 0], color=BLUE)
        blR = Line([2.7, 2.4, 0], [2.7, 0.7, 0], color=BLUE)
        blL_lbl = Text("bit line", color=MUTE).scale(0.3).next_to(blL, DOWN, buff=0.1)
        blR_lbl = Text("bit line", color=MUTE).scale(0.3).next_to(blR, DOWN, buff=0.1)

        # access transistors (gated by word line)
        atL = Square(0.36, color=PURPLE, fill_color=PURPLE, fill_opacity=0.10).move_to([-1.9, 1.0, 0])
        atR = Square(0.36, color=PURPLE, fill_color=PURPLE, fill_opacity=0.10).move_to([1.9, 1.0, 0])
        wL1 = Line([-1.15, 1.0, 0], [-1.72, 1.0, 0], color=MUTE)
        wL2 = Line([-2.08, 1.0, 0], [-2.7, 1.0, 0], color=MUTE)
        wR1 = Line([1.15, 1.0, 0], [1.72, 1.0, 0], color=MUTE)
        wR2 = Line([2.08, 1.0, 0], [2.7, 1.0, 0], color=MUTE)
        gL = Line([-1.9, 1.18, 0], [-1.9, 2.4, 0], color=PURPLE, stroke_width=2)
        gR = Line([1.9, 1.18, 0], [1.9, 2.4, 0], color=PURPLE, stroke_width=2)

        # node value labels
        qv = Text("1", color=GREEN).scale(0.5).move_to([1.5, 0.0, 0])
        qbarv = Text("0", color=MUTE).scale(0.5).move_to([-1.5, 0.0, 0])
        qtag = Text("Q", color=GREEN).scale(0.34).move_to([1.5, 0.42, 0])
        qbartag = Text("Q̄", color=MUTE).scale(0.34).move_to([-1.5, 0.42, 0])

        cell = VGroup(word, word_lbl, blL, blR, blL_lbl, blR_lbl,
                      atL, atR, wL1, wL2, wR1, wR2, gL, gR,
                      A, B, A_lbl, B_lbl, qbar, q, qv, qbarv, qtag, qbartag)
        self.play(FadeIn(cell, run_time=1.8))

        # --- beat 1: holds itself --------------------------------------------
        c1 = Text("each inverter drives the other → the state locks itself", color=TXT).scale(0.42).to_edge(DOWN)
        self.play(FadeIn(c1))
        for _ in range(2):
            self.play(Indicate(A, color=GREEN, scale_factor=1.12), Indicate(q, color=GREEN), run_time=0.7)
            self.play(Indicate(B, color=GREEN, scale_factor=1.12), Indicate(qbar, color=GREEN), run_time=0.7)
        self.wait(0.3)

        # --- beat 2: read -----------------------------------------------------
        c2 = Text("READ: open the word line; the 0-side tugs its bit line down", color=TEAL).scale(0.42).to_edge(DOWN)
        self.play(FadeOut(c1), FadeIn(c2))
        self.play(Flash(word, color=AMBER), atL.animate.set_fill(AMBER, 0.25),
                  atR.animate.set_fill(AMBER, 0.25), run_time=0.8)
        drop = Arrow([-2.7, 1.6, 0], [-2.7, 0.9, 0], color=RED, buff=0.05, stroke_width=5)
        self.play(blL.animate.set_color(RED), GrowArrow(drop), run_time=0.8)
        read = Text("sense amp: left dipped → reads  1", color=GREEN).scale(0.4).move_to([0, -2.2, 0])
        self.play(FadeIn(read))
        self.wait(0.6)
        self.play(FadeOut(read), FadeOut(drop), blL.animate.set_color(BLUE),
                  atL.animate.set_fill(PURPLE, 0.10), atR.animate.set_fill(PURPLE, 0.10))

        # --- beat 3: write 0 (overpower) -------------------------------------
        c3 = Text("WRITE 0: drive the bit lines hard — they overpower the loop", color=AMBER).scale(0.42).to_edge(DOWN)
        self.play(FadeOut(c2), FadeIn(c3))
        # strong drivers: left bit line -> 1, right bit line -> 0
        dL = Arrow([-3.4, 1.0, 0], [-2.7, 1.0, 0], color=AMBER, buff=0.05, stroke_width=7)
        dR = Arrow([3.4, 1.0, 0], [2.7, 1.0, 0], color=AMBER, buff=0.05, stroke_width=7)
        dL_lbl = Text("drive 1", color=AMBER).scale(0.3).next_to(dL, LEFT, buff=0.05)
        dR_lbl = Text("drive 0", color=AMBER).scale(0.3).next_to(dR, RIGHT, buff=0.05)
        self.play(GrowArrow(dL), GrowArrow(dR), FadeIn(dL_lbl), FadeIn(dR_lbl),
                  blL.animate.set_color(GREEN), blR.animate.set_color(MUTE),
                  Flash(word, color=AMBER))
        # the flip: nodes swap, feedback re-locks
        self.play(
            qbar.animate.set_color(GREEN), q.animate.set_color(MUTE),
            Transform(qbarv, Text("1", color=GREEN).scale(0.5).move_to([-1.5, 0.0, 0])),
            Transform(qv, Text("0", color=MUTE).scale(0.5).move_to([1.5, 0.0, 0])),
            Transform(qbartag, Text("Q̄", color=GREEN).scale(0.34).move_to([-1.5, 0.42, 0])),
            Transform(qtag, Text("Q", color=MUTE).scale(0.34).move_to([1.5, 0.42, 0])),
            run_time=1.2)
        relock = Text("flipped — the loop re-locks, now holding 0", color=GREEN).scale(0.4).move_to([0, -2.2, 0])
        self.play(FadeIn(relock))
        for _ in range(2):
            self.play(Indicate(B, color=GREEN, scale_factor=1.12), Indicate(qbar, color=GREEN), run_time=0.6)
            self.play(Indicate(A, color=GREEN, scale_factor=1.12), Indicate(q, color=GREEN), run_time=0.6)
        self.wait(0.5)
        self.play(FadeOut(VGroup(dL, dR, dL_lbl, dR_lbl, relock, c3)))
        self.wait(0.6)
