"""Round robin with the three process states, run live.

Three processes share one CPU: slices expire (timer interrupt), one
process blocks on a disk read and later returns to the READY queue --
never straight to the CPU. Deterministic; no randomness.

Render (from this folder):
    manim -qm os-round-robin.py RoundRobin   # smoke
    manim -qk os-round-robin.py RoundRobin   # 4K final
Copy the output beside the card as os-round-robin.mp4, then clear
media/ + __pycache__/.
"""

from manim import *

BG = "#1a1a1a"
GRAY = "#9a9a9a"
BLUE = "#2563eb"
GREEN = "#059669"
TEAL = "#0891b2"
AMBER = "#f59e0b"
PURPLE = "#7c3aed"
RED = "#dc2626"

config.background_color = BG

CPU_POS = UP * 2.1
READY_BASE = LEFT * 4.6 + DOWN * 1.6
READY_STEP = RIGHT * 1.35
BLOCK_POS = RIGHT * 4.3 + DOWN * 1.6


class RoundRobin(Scene):
    def swap_caption(self, text, color=GRAY):
        cap = Text(text, font_size=25, color=color).to_edge(DOWN, buff=0.3)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.2), FadeIn(cap, run_time=0.3))
        else:
            self.play(FadeIn(cap, run_time=0.3))
        self._cap = cap

    def chip(self, name, color):
        c = VGroup(
            RoundedRectangle(corner_radius=0.12, width=1.05, height=0.62,
                             stroke_color=color, stroke_width=2.5,
                             fill_color=color, fill_opacity=0.25),
            Text(name, font_size=26, color=GRAY, weight=BOLD),
        )
        c[1].move_to(c[0])
        return c

    def construct(self):
        cpu_box = RoundedRectangle(corner_radius=0.15, width=2.1, height=1.15,
                                   stroke_color=PURPLE, stroke_width=4)
        cpu_box.move_to(CPU_POS)
        cpu_lab = Text("CPU — RUNNING", font_size=24, color=PURPLE,
                       weight=BOLD).next_to(cpu_box, UP, buff=0.18)

        ready_zone = RoundedRectangle(corner_radius=0.15, width=4.6, height=1.25,
                                      stroke_color=BLUE, stroke_width=2.5,
                                      stroke_opacity=0.8).move_to(READY_BASE + READY_STEP)
        ready_lab = Text("READY queue (waiting for a turn)", font_size=21,
                         color=BLUE).next_to(ready_zone, DOWN, buff=0.15)
        block_zone = RoundedRectangle(corner_radius=0.15, width=2.6, height=1.25,
                                      stroke_color=AMBER, stroke_width=2.5,
                                      stroke_opacity=0.8).move_to(BLOCK_POS)
        block_lab = Text("BLOCKED (awaiting I/O)", font_size=21,
                         color=AMBER).next_to(block_zone, DOWN, buff=0.15)

        p1 = self.chip("P1", BLUE)
        p2 = self.chip("P2", GREEN)
        p3 = self.chip("P3", TEAL)
        ready = [p1, p2, p3]

        def ready_pos(i):
            return READY_BASE + READY_STEP * i

        for i, c in enumerate(ready):
            c.move_to(ready_pos(i))

        self.play(FadeIn(cpu_box), FadeIn(cpu_lab), FadeIn(ready_zone),
                  FadeIn(ready_lab), FadeIn(block_zone), FadeIn(block_lab),
                  *[FadeIn(c) for c in ready], run_time=1.0)
        self.swap_caption("one CPU, three processes — the timer interrupt ends each turn")

        def relayout(extra=None):
            anims = [c.animate.move_to(ready_pos(i)) for i, c in enumerate(ready)]
            if extra:
                anims += extra
            self.play(*anims, run_time=0.7)

        # P1 runs a slice, slice expires -> back of queue
        ready.remove(p1)
        self.play(p1.animate.move_to(CPU_POS), *[c.animate.move_to(ready_pos(i))
                  for i, c in enumerate(ready)], run_time=0.7)
        self.wait(0.9)
        ready.append(p1)
        self.swap_caption("slice over (timer interrupt) — P1 rejoins the BACK of the queue", color=PURPLE)
        relayout()

        # P2 runs, asks for I/O -> BLOCKED
        ready.remove(p2)
        self.play(p2.animate.move_to(CPU_POS), *[c.animate.move_to(ready_pos(i))
                  for i, c in enumerate(ready)], run_time=0.7)
        self.wait(0.5)
        self.swap_caption("P2 asks for a disk read — it cannot use the CPU while waiting", color=AMBER)
        self.play(p2.animate.move_to(BLOCK_POS), run_time=0.7)

        # P3 runs immediately
        ready.remove(p3)
        self.play(p3.animate.move_to(CPU_POS), *[c.animate.move_to(ready_pos(i))
                  for i, c in enumerate(ready)], run_time=0.7)
        self.swap_caption("nobody idles waiting for P2 — the CPU moves straight on (blocked costs nothing)")
        self.wait(0.9)
        ready.append(p3)
        relayout()

        # disk interrupt: P2 -> READY (not CPU)
        self.swap_caption("the disk interrupt: P2's data is ready — it earns the QUEUE, never the CPU directly", color=GREEN)
        ready.append(p2)
        relayout()
        self.wait(0.4)

        # one more rotation, moral
        nxt = ready.pop(0)
        self.play(nxt.animate.move_to(CPU_POS), *[c.animate.move_to(ready_pos(i))
                  for i, c in enumerate(ready)], run_time=0.7)
        self.swap_caption("round and round, many times a second — fast turn-taking IS the illusion of 'simultaneous'")
        self.wait(1.8)
