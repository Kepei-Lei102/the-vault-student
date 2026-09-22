"""Manim scene for [[Java Arrays and ArrayList]].

SkipOnRemove — remove every 8 from [3, 8, 8, 8, 5] with a forward indexed loop.  After remove(1) the list closes up, the
               second 8 slides into index 1, and the loop's i++ steps over it.  Result: one 8 survives.  Then the same
               loop run backwards: what slides is already behind the index, so nothing is skipped.
Smoke:  manim -ql --fps 15 java-arrays-manim.py SkipOnRemove
Final:  manim -qk java-arrays-manim.py SkipOnRemove
"""
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b"
W = 1.2


def cells(vals, y, x0=-3.0):
    g = VGroup()
    for k, v in enumerate(vals):
        box = RoundedRectangle(width=1.05, height=0.8, corner_radius=0.08, color=BLUE_H, stroke_width=3, fill_color=BLUE_H, fill_opacity=0.12).move_to([x0 + k * W, y, 0])
        txt = Text(str(v), font="Menlo", font_size=30, color=GREY_T).move_to(box)
        idx = Text(str(k), font_size=20, color=GREY_T).next_to(box, DOWN, buff=0.08)
        g.add(VGroup(box, txt, idx))
    return g


class SkipOnRemove(Scene):
    def run_pass(self, vals, y, forward, label_col):
        row = cells(vals, y)
        self.add(row)
        ptr = Triangle(color=AMBER_H, fill_opacity=1).scale(0.18).rotate(PI)
        i = 0 if forward else len(vals) - 1
        ptr.next_to(row[i][0], UP, buff=0.08)
        itxt = Text(f"i = {i}", font="Menlo", font_size=24, color=AMBER_H).move_to([4.2, y + 0.2, 0])
        self.add(ptr, itxt); self.wait(0.6)
        live = list(vals)
        while 0 <= i < len(live):
            if live[i] == 8:
                self.play(row[i][0].animate.set_fill(RED_H, opacity=0.5).set_stroke(RED_H), run_time=0.35)
                self.play(FadeOut(row[i]), run_time=0.35)
                del live[i]; row.remove(row[i])
                # close the gap: everything after slides left, and its index label changes
                anims = [row[k].animate.shift(LEFT * W) for k in range(i, len(live))]
                if anims: self.play(*anims, run_time=0.6)
                for k in range(i, len(live)):
                    row[k][2].become(Text(str(k), font_size=20, color=AMBER_H).next_to(row[k][0], DOWN, buff=0.08))
                if forward:
                    i += 1
                else:
                    i -= 1
            else:
                if forward:
                    i += 1
                else:
                    i -= 1
            if 0 <= i < len(live):
                self.play(ptr.animate.next_to(row[i][0], UP, buff=0.08), Transform(itxt, Text(f"i = {i}", font="Menlo", font_size=24, color=AMBER_H).move_to(itxt)), run_time=0.45)
            else:
                self.play(FadeOut(ptr), Transform(itxt, Text("loop over", font="Menlo", font_size=24, color=label_col).move_to(itxt)), run_time=0.45)
        return live

    def construct(self):
        self.add(Text("remove every 8 from the list, by index", font_size=26, color=GREY_T).to_edge(UP, buff=0.25))
        code1 = Text("for (int i = 0; i < a.size(); i++) { if (a.get(i) == 8) { a.remove(i); } }", font="Menlo", font_size=20, color=RED_H).move_to([0, 2.5, 0])
        self.add(code1)
        cap = Text("forward: after a removal, the next element slides INTO index i, and i++ steps over it", font_size=24, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(cap)
        left = self.run_pass([3, 8, 8, 8, 5], 1.3, True, RED_H)
        self.remove(cap); cap = Text(f"one 8 survived: {left}", font_size=24, color=RED_H).to_edge(DOWN, buff=0.3); self.add(cap); self.wait(2.0)

        code2 = Text("for (int i = a.size() - 1; i >= 0; i--) { if (a.get(i) == 8) { a.remove(i); } }", font="Menlo", font_size=20, color=GREEN_H).move_to([0, -0.4, 0])
        self.add(code2)
        self.remove(cap); cap = Text("backward: what slides is already behind i, so nothing is skipped", font_size=24, color=GREY_T).to_edge(DOWN, buff=0.3); self.add(cap)
        left = self.run_pass([3, 8, 8, 8, 5], -1.6, False, GREEN_H)
        self.remove(cap); cap = Text(f"all three gone: {left}.  Walk backwards, or only advance i when you did not remove.", font_size=24, color=GREEN_H).to_edge(DOWN, buff=0.3); self.add(cap); self.wait(4)
