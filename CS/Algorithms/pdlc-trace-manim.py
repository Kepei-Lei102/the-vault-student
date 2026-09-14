"""A dry run, watched: the March 2024 Paper 22 flowchart as pseudocode on the left,
the trace table filling on the right, one cell at a time, as the pointer moves.

Render:  manim -qk pdlc-trace-manim.py TraceTable
"""
from manim import *

BLUE, AMBER, GREEN, GREY, RED = "#2563eb", "#f59e0b", "#059669", "#888888", "#dc2626"
config.background_color = "#1e1e1e"

CODE = [
    "NumberGroups ← 0",
    "Total ← 0",
    "INPUT GroupSize",
    "WHILE GroupSize <> 0",
    "    NumberGroups ← NumberGroups + 1",
    "    Total ← Total + GroupSize",
    "    INPUT GroupSize",
    "ENDWHILE",
    "Average ← DIV(Total, NumberGroups)",
    'OUTPUT "Average group size ", Average',
]
DATA = [7, 10, 2, 8, 3, 9, 0, 6]
COLS = ["NumberGroups", "Total", "GroupSize", "Average", "OUTPUT"]

class TraceTable(Scene):
    def construct(self):
        title = Text("Dry run: 0478 March 2024 Paper 22 Q7  —  input 7, 10, 2, 8, 3, 9, 0, 6", font_size=26, color=GREY).to_edge(UP, buff=0.3)
        self.add(title)
        # code block
        lines = VGroup(*[Text(l, font="Menlo", font_size=20, color=GREY) for l in CODE]).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        lines.to_edge(LEFT, buff=0.5).shift(DOWN * 0.2)
        self.add(lines)
        pointer = Triangle(fill_color=AMBER, fill_opacity=1, stroke_width=0).scale(0.13).rotate(-90 * DEGREES)
        pointer.next_to(lines[0], LEFT, buff=0.15); self.add(pointer)
        # table
        x0, y0 = -1.3, 2.4; colw = [1.7, 0.95, 1.25, 1.05, 2.4]; rowh = 0.42
        xs = [x0 + sum(colw[:i]) for i in range(len(COLS))]
        heads = VGroup(*[Text(c, font_size=17, color=GREY).move_to([xs[i] + colw[i] / 2, y0, 0]) for i, c in enumerate(COLS)])
        self.add(heads)
        self.add(Line([x0, y0 - 0.24, 0], [x0 + sum(colw), y0 - 0.24, 0], color=GREY, stroke_width=1.5))
        for i in range(1, len(COLS)):
            self.add(Line([xs[i], y0 + 0.2, 0], [xs[i], y0 - 0.24 - rowh * 8, 0], color=GREY, stroke_width=0.8))
        caption = Text("one column per variable; a value is written only when it changes", font_size=22, color=GREY).to_edge(DOWN, buff=0.3)
        self.add(caption)

        row = [0]; used = [set()]
        def point(i, t=0.35):
            self.play(pointer.animate.next_to(lines[i], LEFT, buff=0.15), lines[i].animate.set_color(AMBER), run_time=t)
            for j, l in enumerate(lines):
                if j != i: l.set_color(GREY)
        def write(col, val, color=BLUE):
            c = COLS.index(col)
            if c in used[0] or col == "OUTPUT":
                row[0] += 1; used[0] = set()
            used[0].add(c)
            y = y0 - 0.24 - rowh * (row[0] + 0.5)
            cell = Text(str(val), font_size=(18 if col != "OUTPUT" else 15), color=color).move_to([xs[c] + colw[c] / 2, y, 0])
            self.play(FadeIn(cell, shift=DOWN * 0.15), run_time=0.3)

        data = DATA[:]
        NumberGroups = 0; Total = 0
        point(0); write("NumberGroups", 0)
        point(1); write("Total", 0)
        GroupSize = data.pop(0); point(2); write("GroupSize", GroupSize)
        point(3)
        while GroupSize != 0:
            NumberGroups += 1; point(4, 0.25); write("NumberGroups", NumberGroups)
            Total += GroupSize; point(5, 0.25); write("Total", Total)
            GroupSize = data.pop(0); point(6, 0.25); write("GroupSize", GroupSize)
            point(3, 0.25)
        self.play(Transform(caption, Text("GroupSize is 0: the condition fails, the loop ends — the 6 after the 0 is never read", font_size=22, color=AMBER).to_edge(DOWN, buff=0.3)), run_time=0.5)
        self.wait(1.2)
        point(7); Average = Total // NumberGroups
        point(8); write("Average", Average, GREEN)
        point(9); write("OUTPUT", f"Average group size {Average}", GREEN)
        self.play(Transform(caption, Text("scheme: one mark for the NumberGroups and GroupSize columns, one each for Total, Average, OUTPUT", font_size=22, color=GREEN).to_edge(DOWN, buff=0.3)), run_time=0.5)
        self.wait(2.5)
