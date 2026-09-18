"""
paradigms-manim.py — two scenes for [[Programming Paradigms]].

Scene 1  PrologSearch  — the engine answering grandparent(tom, Who): the goal stack, the facts
                         tried in order, bindings appearing, a dead branch backtracked, two answers.
Scene 2  MachineSteps  — the register machine running the low-level loop: memory cells light up
                         as each addressing mode reads them; the accumulator and index register tick.

Smoke:   manim -ql --fps 15 paradigms-manim.py PrologSearch MachineSteps
Final:   manim -qk paradigms-manim.py PrologSearch MachineSteps
then concat with ffmpeg to paradigms-manim.mp4 and rm -rf media __pycache__.
"""
from manim import *

GREY = "#888888"
BLUE_, RED_, GREEN_, AMBER, PURPLE_, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"


class PrologSearch(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("Declarative: you state the goal — the engine searches facts and rules for whatever satisfies it", font_size=26, color=GREY).to_edge(UP, buff=0.25)
        self.play(FadeIn(title))
        facts = ["parent(tom, bob).", "parent(tom, liz).", "parent(bob, ann).", "parent(bob, pat).", "parent(pat, jim)."]
        rule = "grandparent(X, Z) :- parent(X, Y), parent(Y, Z)."
        kb = VGroup(Text("knowledge base", font_size=20, color=AMBER), *[Text(f, font_size=20, color=GREY, font="Menlo") for f in facts], Text(rule, font_size=19, color=PURPLE_, font="Menlo")).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(LEFT, buff=0.5).shift(DOWN * 0.3)
        self.play(FadeIn(kb))
        goal = Text("?- grandparent(tom, Who).", font_size=24, color=AMBER, font="Menlo").move_to([3.2, 2.3, 0])
        self.play(Write(goal))
        steps = [
            ("match the rule: X = tom, Z = Who", PURPLE_, 6),
            ("new goals: parent(tom, Y), parent(Y, Who)", BLUE_, None),
            ("parent(tom, Y): try fact 1 → Y = bob", GREEN_, 1),
            ("parent(bob, Who): try fact 3 → Who = ann  ✓", GREEN_, 3),
            ("answer 1:  Who = ann", AMBER, None),
            ("backtrack: parent(bob, Who) again → fact 4 → Who = pat  ✓", GREEN_, 4),
            ("answer 2:  Who = pat", AMBER, None),
            ("backtrack: parent(tom, Y) again → fact 2 → Y = liz", GREEN_, 2),
            ("parent(liz, Who): no fact matches  ✗  — branch dies", RED_, None),
            ("no more choices: search complete — 2 answers", GREY, None),
        ]
        shown = VGroup(); highlight = None
        for text, col, fact_idx in steps:
            t = Text(text, font_size=19, color=col, font="Menlo")
            shown.add(t); shown.arrange(DOWN, aligned_edge=LEFT, buff=0.16).next_to(goal, DOWN, buff=0.35).align_to(goal, LEFT)
            if highlight is not None: self.remove(highlight); highlight = None
            if fact_idx is not None:
                highlight = SurroundingRectangle(kb[fact_idx], color=col, buff=0.06, stroke_width=2); self.add(highlight)
            self.play(FadeIn(t), run_time=0.6); self.wait(1.1)
        cap = Text("no loop, no if, no order of steps was written — only what must be true", font_size=20, color=GREY).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(cap)); self.wait(1.5)


class MachineSteps(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("Low-level: every step is an instruction and an address — the five addressing modes at work", font_size=26, color=GREY).to_edge(UP, buff=0.25)
        self.play(FadeIn(title))
        mem = [2, 12, 1, 5, 30, 0, 0, 0, 0, 0, 5, 0, 13, 6]
        cells = VGroup(); vals = []
        for i, v in enumerate(mem):
            sq = Square(0.62, color=GREY, stroke_width=1.2).move_to([-6.2 + i * 0.95, 1.6, 0])
            val = Text(str(v), font_size=20, color=GREY, font="Menlo").move_to(sq); idx = Text(str(i), font_size=13, color=GREY).next_to(sq, DOWN, buff=0.08)
            cells.add(VGroup(sq, idx)); vals.append(val)
        self.add(cells, *vals)
        acc = Text("ACC = 0", font_size=22, color=AMBER, font="Menlo").move_to([-4.2, -0.3, 0]); ix = Text("IX = 0", font_size=22, color=TEAL, font="Menlo").move_to([-1.2, -0.3, 0])
        self.add(acc, ix)
        prog = Text("", font_size=20, color=GREY).move_to([2.8, -0.3, 0]); self.add(prog)
        note = Text("", font_size=18, color=GREY).to_edge(DOWN, buff=0.5); self.add(note)
        state = {"acc": 0, "ix": 0, "mem": list(mem)}
        def show(ins, col, cell=None, a=None, i=None, why=""):
            nonlocal acc, ix, prog, note
            newprog = Text(ins, font_size=22, color=col, font="Menlo").move_to([2.8, -0.3, 0])
            newnote = Text(why, font_size=18, color=col).to_edge(DOWN, buff=0.5)
            anims = [Transform(prog, newprog), Transform(note, newnote)]
            if a is not None:
                state["acc"] = a; newacc = Text(f"ACC = {a}", font_size=22, color=AMBER, font="Menlo").move_to([-4.2, -0.3, 0]); anims.append(Transform(acc, newacc))
            if i is not None:
                state["ix"] = i; newix = Text(f"IX = {i}", font_size=22, color=TEAL, font="Menlo").move_to([-1.2, -0.3, 0]); anims.append(Transform(ix, newix))
            self.play(*anims, run_time=0.5)
            if cell is not None:
                r = SurroundingRectangle(cells[cell][0], color=col, buff=0.03, stroke_width=3); self.add(r); self.wait(0.9); self.remove(r)
            else:
                self.wait(0.9)
        def setmem(cell, v):
            state["mem"][cell] = v; new = Text(str(v), font_size=20, color=GREY, font="Menlo").move_to(cells[cell][0]); self.remove(vals[cell]); vals[cell] = new; self.add(new)
        show("LDM  #0", RED_, None, a=0, why="immediate: the operand IS the value — no memory read")
        show("STO  11", TEAL, 11, why="direct: write the accumulator into cell 11 (the total)"); setmem(11, 0)
        show("LDR  #0", TEAL, None, i=0, why="the index register starts at 0")
        total = 0
        for k in range(5):
            price = mem[k]
            show(f"LDX  0,IX", AMBER, k, a=price, why=f"indexed: cell 0 + IX = cell {k} — price[{k}] = {price}")
            show("SUB  (12)", PURPLE_, 12, a=price - 6, why="indirect: cell 12 holds 13, so read cell 13 — the limit, 6")
            if price - 6 < 0:
                total += price
                show("JLT  ADDIT → ADD 5 → STO 11", GREEN_, 11, a=total, why=f"negative, so it is cheap: total becomes {total}"); setmem(11, total)
            else:
                show("JLT  not taken → JMP NEXT", GREY, None, why="not negative: skip it (a jump relative to the program)")
            show("INC  IX", TEAL, None, i=k + 1, why="next item")
        show("LDD  11 → END", AMBER, 11, a=total, why=f"the answer, {total}, is in the accumulator after 66 instructions")
        self.wait(1.5)
