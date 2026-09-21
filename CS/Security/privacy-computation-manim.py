"""Manim scenes for [[Privacy-Preserving Computation]].
Scene 1  SecureSum — three hospitals each cut a private number into three random shares (arithmetic
                     mod 10 000 so the numbers fit on screen), deal them out, add what they hold, and
                     publish only those partial sums.  The total is exact; no private number ever moved.
Scene 2  Cave      — the zero-knowledge cave.  A ring-shaped cave has a locked door at the back.  The
                     prover walks in by a side of her choosing; the verifier then calls a side to come out
                     of.  With the key she always can.  Without it she survives each round with
                     probability 1/2, and is soon caught.  The verifier never sees the key.
Smoke:  manim -ql --fps 15 privacy-computation-manim.py SecureSum Cave
Final:  manim -qk privacy-computation-manim.py SecureSum Cave      (two separate clips)"""
import numpy as np
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H, TEAL_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
MOD = 10_000


class SecureSum(Scene):
    def construct(self):
        title = Text("Adding three numbers that nobody is allowed to see", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        note = Text("all arithmetic is mod 10 000", font_size=16, color=GREY_T).move_to([5.3, 3.1, 0])
        self.add(title, note)
        rng = np.random.default_rng(11)
        names, secrets_, cols = ["hospital A", "hospital B", "hospital C"], [1204, 877, 2310], [BLUE_H, PURPLE_H, TEAL_H]
        pos = [np.array([-4.6, 1.3, 0]), np.array([4.6, 1.3, 0]), np.array([0, -1.2, 0])]
        boxes = VGroup(); labels = VGroup()
        for n, s, c, p in zip(names, secrets_, cols, pos):
            boxes.add(RoundedRectangle(width=3.0, height=1.25, corner_radius=0.15, color=c, fill_opacity=0.12).move_to(p))
            labels.add(VGroup(Text(n, font_size=20, color=c).move_to(p + UP * 0.33), Text(f"private: {s}", font_size=22, color=GREY_T).move_to(p + DOWN * 0.2)))
        self.add(boxes, labels)
        cap = Text("each hospital cuts its number into three random pieces that add up to it", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(cap); self.wait(2)
        shares = []
        for s in secrets_:
            a, b = int(rng.integers(0, MOD)), int(rng.integers(0, MOD)); shares.append([a, b, (s - a - b) % MOD])
        chips = [[None] * 3 for _ in range(3)]
        for i in range(3):
            row = VGroup()
            for j in range(3):
                chip = VGroup(RoundedRectangle(width=0.95, height=0.42, corner_radius=0.08, color=cols[i], fill_opacity=0.3, stroke_width=2),
                              Text(f"{shares[i][j]:04d}", font_size=18, color=GREY_T))
                chip.move_to(pos[i] + np.array([(j - 1) * 1.0, -1.0 if i < 2 else 1.0, 0])); chips[i][j] = chip; row.add(chip)
            eq = Text(f"{shares[i][0]:04d} + {shares[i][1]:04d} + {shares[i][2]:04d} = {secrets_[i]}  (mod 10 000)", font_size=18, color=cols[i]).move_to([0, 2.55 - 0.0 * i, 0])
            self.play(FadeIn(row, shift=DOWN * 0.2 if i < 2 else UP * 0.2), FadeIn(eq), run_time=0.9); self.wait(1.1); self.remove(eq)
        self.remove(cap)
        cap = Text("piece j goes to hospital j: each piece alone is just a random number", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(cap)
        slot = lambda j, k: pos[j] + np.array([(k - 1) * 1.0, -1.0 if j < 2 else 1.0, 0])
        self.play(*[chips[i][j].animate.move_to(slot(j, i)) for i in range(3) for j in range(3)], run_time=3); self.wait(1.5)
        self.remove(cap)
        cap = Text("each hospital adds the three pieces it now holds, and publishes only that", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(cap)
        partial = [sum(shares[i][j] for i in range(3)) % MOD for j in range(3)]
        outs = VGroup()
        for j in range(3):
            t = Text(f"publishes {partial[j]:04d}", font_size=20, color=AMBER_H).move_to(pos[j] + np.array([0, -1.6 if j < 2 else 1.6, 0])); outs.add(t)
        self.play(FadeIn(outs), run_time=1); self.wait(2)
        self.remove(cap)
        total = sum(partial) % MOD
        res = Text(f"{partial[0]:04d} + {partial[1]:04d} + {partial[2]:04d} = {total}  (mod 10 000)", font_size=26, color=GREEN_H).move_to([0, 2.5, 0])
        cap = Text(f"the true total, 1204 + 877 + 2310 = {sum(secrets_)}: exact, and no private number ever left its box", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(res)); self.add(cap); self.wait(4)


class Cave(Scene):
    def construct(self):
        title = Text("Proving you hold a key without showing it", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        c = np.array([-2.6, -0.2, 0]); R = 2.0
        ring_out = Circle(radius=R + 0.35, color=GREY_T, stroke_width=3).move_to(c); ring_in = Circle(radius=R - 0.35, color=GREY_T, stroke_width=3).move_to(c)
        gap = Rectangle(width=0.9, height=0.9, color=BLACK, fill_color=BLACK, fill_opacity=1, stroke_width=0).move_to(c + DOWN * R)
        door = Line(c + UP * (R - 0.35), c + UP * (R + 0.35), color=AMBER_H, stroke_width=8)
        dl = Text("locked door", font_size=16, color=AMBER_H).next_to(door, UP, buff=0.1)
        la = Text("A", font_size=24, color=GREY_T).move_to(c + LEFT * (R + 0.75)); lb = Text("B", font_size=24, color=GREY_T).move_to(c + RIGHT * (R + 0.75))
        entrance = c + DOWN * (R + 1.0)
        verifier = Dot(entrance + RIGHT * 1.3, color=BLUE_H, radius=0.13); vl = Text("verifier waits outside", font_size=16, color=BLUE_H).next_to(verifier, RIGHT, buff=0.15)
        self.add(ring_out, ring_in, gap, door, dl, la, lb, verifier, vl)
        side = np.array([3.6, 0, 0])
        def point(angle):                       # angle measured from the entrance (bottom), positive = side B (right)
            return c + R * np.array([np.sin(angle), -np.cos(angle), 0])

        def walk(dot, a0, a1, t=1.2):
            tr = ValueTracker(a0); dot.add_updater(lambda m: m.move_to(point(tr.get_value())))
            self.play(tr.animate.set_value(a1), run_time=t, rate_func=linear); dot.clear_updaters()

        def run(has_key, script, colour, who):
            head = Text(who, font_size=22, color=colour).move_to(side + UP * 2.0)
            self.add(head)
            passed = 0
            for k, (enter, call) in enumerate(script):                     # 0 = A (left), 1 = B (right); in reality both are coin tosses
                sgn = lambda s: 1 if s == 1 else -1
                p = Dot(entrance, color=colour, radius=0.13); self.add(p)
                info = Text(f"round {k+1}: she goes in by {'AB'[enter]}, unseen", font_size=20, color=GREY_T).move_to(side + UP * 1.2)
                self.add(info)
                self.play(p.animate.move_to(point(0)), run_time=0.4)
                walk(p, 0, sgn(enter) * 2.6, 1.0)
                shout = Text(f"verifier calls: come out by {'AB'[call]}!", font_size=20, color=BLUE_H).move_to(side + UP * 0.6)
                self.add(shout); self.wait(0.5)
                if enter == call:
                    walk(p, sgn(enter) * 2.6, 0, 1.0); ok = True
                elif has_key:
                    walk(p, sgn(enter) * 2.6, sgn(enter) * PI, 0.4)
                    self.play(door.animate.set_color(GREEN_H), run_time=0.2)
                    p.move_to(point(sgn(call) * PI)); walk(p, sgn(call) * PI, 0, 1.2)
                    self.play(door.animate.set_color(AMBER_H), run_time=0.2); ok = True
                else:
                    walk(p, sgn(enter) * 2.6, sgn(enter) * PI * 0.97, 0.4); ok = False
                verdict = Text("came out where called" if ok else "stuck at the door: CAUGHT", font_size=20, color=GREEN_H if ok else RED_H).move_to(side)
                passed += ok
                chance = Text(f"a cheat would have survived this far with probability 1/{2**passed}" if ok else "", font_size=18, color=GREY_T).move_to(side + DOWN * 0.6)
                self.add(verdict, chance); self.wait(1.3 if ok else 2.5)
                self.remove(p, info, shout, verdict, chance)
                if not ok:
                    break
            self.remove(head)

        run(True, [(0, 1), (1, 1), (1, 0)], GREEN_H, "a prover who HAS the key")
        run(False, [(1, 1), (0, 0), (0, 1)], RED_H, "a prover who does NOT")
        end = Text("the verifier is convinced and has learned nothing about the key", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
        self.add(end); self.wait(3)
