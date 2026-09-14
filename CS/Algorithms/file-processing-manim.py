"""
file-processing-manim.py — two scenes for [[File Processing and Exception Handling]].

Scene 1  FindRecord    — one key, three file organisations, one file pointer each.
                         Serial walks; sequential walks and stops; random jumps.
Scene 2  StackUnwind   — an exception raised three frames deep climbs the stack:
                         once with no handler (program halts), once with a
                         handler in main (frames discarded, program continues).

Smoke:   manim -ql --fps 15 file-processing-manim.py FindRecord StackUnwind
Final:   manim -qk file-processing-manim.py FindRecord StackUnwind
then concat with ffmpeg to file-processing-manim.mp4 and rm -rf media __pycache__.
"""
from manim import *

GREY = "#888888"
BLUE, PURPLE, GREEN, RED, AMBER = "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b"

SERIAL = [4471, 1030, 8812, 2207, 6153, 3390, 7722, 5092]      # arrival order
SEQ = sorted(SERIAL)                                            # key order
TARGET = 2207
SLOTS = 11                                                      # random file size


def hash_slot(k):
    return k % SLOTS


class FindRecord(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("Find account 2207 — three files, three costs", font_size=34, color=GREY).to_edge(UP, buff=0.3)
        self.play(FadeIn(title))

        cols = []
        labels = ["SERIAL\narrival order", "SEQUENTIAL\nkey order", "RANDOM\nslot = key MOD 11"]
        colors = [BLUE, PURPLE, GREEN]
        xs = [-4.4, 0, 4.4]
        data = [SERIAL, SEQ, None]
        cell_h, cell_w = 0.36, 2.6

        # random file layout: 11 slots, keys placed by hash with linear probing
        rslots = [None] * SLOTS
        for k in SERIAL:
            s = hash_slot(k)
            while rslots[s] is not None:
                s = (s + 1) % SLOTS
            rslots[s] = k

        groups = []
        for x, lab, col, d in zip(xs, labels, colors, data):
            head = Text(lab, font_size=20, color=col, line_spacing=0.8).move_to([x, 2.55, 0])
            cells = VGroup()
            keys = d if d is not None else rslots
            n = len(keys)
            top = 1.85
            for i, k in enumerate(keys):
                r = Rectangle(width=cell_w, height=cell_h, stroke_color=col, stroke_width=2,
                              fill_color=col, fill_opacity=0.12).move_to([x, top - i * cell_h, 0])
                t = Text(str(k) if k is not None else "—", font_size=18, color=GREY if k is not None else "#555555").move_to(r)
                idx = Text(str(i), font_size=13, color=GREY).next_to(r, LEFT, buff=0.12)
                cells.add(VGroup(r, t, idx))
            groups.append((cells, col, keys))
            self.play(FadeIn(head), FadeIn(cells), run_time=0.6)

        # file pointers
        pointers = []
        for (cells, col, keys) in groups:
            p = Triangle(color=AMBER, fill_color=AMBER, fill_opacity=1).scale(0.13).rotate(-PI / 2)
            p.next_to(cells[0], RIGHT, buff=0.12)
            pointers.append(p)
        self.play(*[FadeIn(p) for p in pointers])
        ptr_lab = Text("file pointer", font_size=16, color=AMBER).next_to(pointers[0], RIGHT, buff=0.1)
        self.play(FadeIn(ptr_lab), run_time=0.4)
        self.wait(0.4)
        self.play(FadeOut(ptr_lab), run_time=0.3)

        reads = [0, 0, 0]
        counters = VGroup()
        for i, x in enumerate(xs):
            c = Text("reads: 0", font_size=20, color=GREY).move_to([x, -2.4, 0])
            counters.add(c)
        self.play(FadeIn(counters))

        def step(gi, to_index, hit=False, miss_stop=False):
            cells, col, keys = groups[gi]
            reads[gi] += 1
            p = pointers[gi]
            newc = Text(f"reads: {reads[gi]}", font_size=20, color=GREY).move_to(counters[gi])
            anims = [p.animate.next_to(cells[to_index], RIGHT, buff=0.12), Transform(counters[gi], newc)]
            self.play(*anims, run_time=0.35)
            cell = cells[to_index][0]
            if hit:
                self.play(cell.animate.set_fill(GREEN, opacity=0.6).set_stroke(GREEN, width=4), run_time=0.3)
            else:
                self.play(Indicate(cell, color=RED, scale_factor=1.0), run_time=0.25)

        # SERIAL: walk until found (index 3)
        for i in range(len(SERIAL)):
            step(0, i, hit=(SERIAL[i] == TARGET))
            if SERIAL[i] == TARGET:
                break
        # SEQUENTIAL: walk; 2207 is at index 2 in sorted order
        for i in range(len(SEQ)):
            step(1, i, hit=(SEQ[i] == TARGET))
            if SEQ[i] == TARGET:
                break
        # RANDOM: hash and jump
        s = hash_slot(TARGET)
        calc = Text(f"2207 MOD 11 = {s}: taken, so the next slot", font_size=18, color=GREEN).move_to([4.4, -2.9, 0])
        self.play(FadeIn(calc), run_time=0.4)
        probe = s
        while rslots[probe] != TARGET:
            step(2, probe, hit=False)
            probe = (probe + 1) % SLOTS
        step(2, probe, hit=True)

        self.wait(0.6)
        verdict = Text("serial: read until it turns up  ·  sequential: read until the keys pass it  ·  random: compute, seek, read once",
                       font_size=16, color=GREY).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(verdict))
        self.wait(1.2)

        # the missing key: serial reads all; sequential stops early; random one read
        self.play(FadeOut(verdict), FadeOut(calc), run_time=0.3)
        miss = Text("Now look for 5000, which is not there", font_size=24, color=AMBER).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(miss))
        for gi in range(3):
            reads[gi] = 0
            newc = Text("reads: 0", font_size=20, color=GREY).move_to(counters[gi])
            self.play(Transform(counters[gi], newc), run_time=0.2)
            for cell in groups[gi][0]:
                cell[0].set_fill(groups[gi][1], opacity=0.12).set_stroke(groups[gi][1], width=2)
        for i in range(len(SERIAL)):
            step(0, i)
        for i in range(len(SEQ)):
            step(1, i)
            if SEQ[i] > 5000:
                stop = Text("keys passed 5000: stop", font_size=16, color=PURPLE).move_to([0, -2.9, 0])
                self.play(FadeIn(stop), run_time=0.3)
                break
        s = hash_slot(5000)
        calc2 = Text(f"5000 MOD 11 = {s}", font_size=20, color=GREEN).move_to([4.4, -2.9, 0])
        self.play(FadeIn(calc2), run_time=0.3)
        probe = s
        while rslots[probe] is not None and rslots[probe] != 5000:
            step(2, probe)
            probe = (probe + 1) % SLOTS
        step(2, probe)
        empty = Text("empty slot: not there", font_size=16, color=GREEN).next_to(calc2, DOWN, buff=0.1)
        self.play(FadeIn(empty), run_time=0.3)
        self.wait(1.5)


class StackUnwind(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("An exception climbs the call stack until someone catches it", font_size=30, color=GREY).to_edge(UP, buff=0.3)
        self.play(FadeIn(title))

        def frame(name, sub, y, col=GREY):
            r = Rectangle(width=5.2, height=0.9, stroke_color=col, stroke_width=2,
                          fill_color=col, fill_opacity=0.08).move_to([0, y, 0])
            t1 = Text(name, font_size=22, color=col).move_to(r.get_center() + UP * 0.18)
            t2 = Text(sub, font_size=15, color=GREY).move_to(r.get_center() + DOWN * 0.22)
            return VGroup(r, t1, t2)

        ys = [1.9, 0.8, -0.3, -1.4]
        f_main = frame("main()", "load(lines)", ys[0])
        f_load = frame("load(lines)", "[parse_line(l) for l in lines]", ys[1])
        f_parse = frame('parse_line("pear,ten")', "return name, int(qty)", ys[2])
        f_int = frame('int("ten")', "cannot make an integer of that", ys[3], RED)

        # frames are pushed in call order, top of stack at the bottom of the screen
        for f, cap in [(f_main, "call"), (f_load, "call"), (f_parse, "call"), (f_int, "raise ValueError")]:
            self.play(FadeIn(f, shift=UP * 0.3), run_time=0.45)
        boom = Text("raise ValueError", font_size=20, color=RED).next_to(f_int, RIGHT, buff=0.3)
        self.play(Write(boom), run_time=0.5)
        self.wait(0.4)

        # PASS 1: no handler — unwind everything, halt
        note = Text("no try anywhere", font_size=20, color=RED).to_edge(LEFT, buff=0.5).shift(UP * 0.8)
        self.play(FadeIn(note))
        ball = Dot(color=RED, radius=0.14).move_to(f_int[0].get_right() + RIGHT * 0.15)
        self.play(FadeIn(ball), FadeOut(boom), run_time=0.3)
        for f in [f_parse, f_load, f_main]:
            self.play(ball.animate.move_to(f[0].get_right() + RIGHT * 0.15), run_time=0.45)
            self.play(f[0].animate.set_stroke(RED, width=3), Indicate(f, color=RED, scale_factor=1.02), run_time=0.35)
            self.play(FadeOut(f, shift=RIGHT * 0.5), run_time=0.3)
        self.play(FadeOut(f_int, shift=RIGHT * 0.5), ball.animate.move_to([0, 2.6, 0]), run_time=0.4)
        halt = Text('Traceback (most recent call last): ...\nValueError: invalid literal for int() with base 10: \'ten\'\n\nprogram halted, exit code 1',
                    font_size=20, color=RED, line_spacing=0.9).move_to([0, 0.3, 0])
        self.play(FadeOut(ball), Write(halt), run_time=1.2)
        self.wait(1.4)
        self.play(FadeOut(halt), FadeOut(note), run_time=0.4)

        # PASS 2: handler in main
        f_main2 = frame("main()", "try: load(lines)   except ValueError: report and go on", ys[0], GREEN)
        f_load2 = frame("load(lines)", "no try here: the error passes through", ys[1])
        f_parse2 = frame('parse_line("pear,ten")', "no try here either", ys[2])
        f_int2 = frame('int("ten")', "raise ValueError", ys[3], RED)
        note2 = Text("try in main()", font_size=20, color=GREEN).to_edge(LEFT, buff=0.5).shift(UP * 0.8)
        self.play(FadeIn(note2))
        for f in [f_main2, f_load2, f_parse2, f_int2]:
            self.play(FadeIn(f, shift=UP * 0.3), run_time=0.4)
        ball = Dot(color=RED, radius=0.14).move_to(f_int2[0].get_right() + RIGHT * 0.15)
        self.play(FadeIn(ball), run_time=0.3)
        for f in [f_parse2, f_load2]:
            self.play(ball.animate.move_to(f[0].get_right() + RIGHT * 0.15), run_time=0.45)
            self.play(FadeOut(f, shift=RIGHT * 0.5), run_time=0.3)
        self.play(FadeOut(f_int2, shift=RIGHT * 0.5), ball.animate.move_to(f_main2[0].get_right() + RIGHT * 0.15), run_time=0.45)
        self.play(ball.animate.set_color(GREEN), f_main2[0].animate.set_stroke(GREEN, width=4), run_time=0.4)
        caught = Text('except ValueError as e:\n    print("bad line skipped:", e)\n    ... the program continues', font_size=20, color=GREEN,
                      line_spacing=0.9).move_to([0, 0.0, 0])
        self.play(Write(caught), run_time=1.0)
        moral = Text("detected three frames down, decided here: the exception carried the news between them",
                     font_size=18, color=GREY).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(moral))
        self.wait(2.0)
