"""Pre-rendered student companion. Stack: Manim, chosen by Kepei 2026-09-16.
Regenerate: manim -qk --media_dir /tmp/vault-manim <this-file.py> Companion
Copy the final MP4 beside this source using the matching kebab-case filename.
No external data or temporary-path dependencies; deterministic where stochastic.
"""
from manim import *
import numpy as np
import math

config.background_color = "#1e1e1e"
TXT="#cccccc"; DIM="#888888"; B="#60a5fa"; G="#34d399"
R="#dc2626"; A="#f59e0b"; P="#a78bfa"
def label(s, size=28, color=TXT, width=12.5):
    m=Text(s, font="DejaVu Sans", font_size=size, color=color)
    if m.width>width: m.scale_to_fit_width(width)
    return m
class Companion(Scene):
    def heading(self,s):
        self.add(label(s,38).move_to([0,3.35,0]))
    def caption(self,s):
        if hasattr(self,"cap"): self.remove(self.cap)
        self.cap=label(s,25,width=12.7).move_to([0,-3.30,0])
        self.add(self.cap)
    def clear_scene(self):
        self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.6)
    def construct(self):
        self.heading("TWO SPELLINGS. ONE EXECUTION TRACE.")
        pseudo=["Total ← 0","FOR Index ← 1 TO 3","    Total ← Total + Values[Index]","NEXT Index","OUTPUT Total"]
        python=["total = 0","for value in [4, 7, 2]:","    total = total + value","", "print(total)"]
        groups=[]
        for x,title,lines in [(-3.45,"Cambridge pseudocode",pseudo),(3.45,"Runnable Python",python)]:
            self.add(label(title,27,color=A).move_to([x,2.4,0]))
            code=VGroup()
            for j,line in enumerate(lines):
                m=Text(line.strip() or ".",font="DejaVu Sans Mono",font_size=20,color=TXT)
                if not line:m.set_opacity(0)
                m.move_to([0,1.85-j*.43,0]).align_to([x-3.1,0,0],LEFT)
                if line.startswith("    "):m.shift(RIGHT*.32)
                code.add(m)
            self.add(code);groups.append(code)
        self.add(label("Values[1..3] = [4, 7, 2]",25).move_to([-3.45,-.85,0]))
        self.add(label("total",25).move_to([2.5,-.85,0]))
        number=label("0",39,color=G).move_to([4.2,-.85,0]);self.add(number)
        self.caption("Pseudocode declares Total, Index and Values separately; this trace focuses on execution.")
        self.wait(5)
        total=0
        for step,value in enumerate([4,7,2],1):
            boxes=VGroup(*[SurroundingRectangle(g[2],color=A,buff=.10) for g in groups]);self.add(boxes)
            self.caption(f"Iteration {step}: first read the old total {total}; add the next value {value}.")
            calc=label(f"{total} + {value} = {total+value}",35,color=A).move_to([0,-2.0,0]);self.play(FadeIn(calc),run_time=.6)
            self.wait(3)
            total+=value;new=label(str(total),39,color=G).move_to(number)
            self.play(ReplacementTransform(number,new),run_time=1);number=new
            self.caption(f"Now store {total}. Invariant: total equals the sum of the {step} values processed so far.")
            self.wait(4);self.remove(calc,boxes)
        self.add(VGroup(*[SurroundingRectangle(g[4],color=G,buff=.10) for g in groups]))
        self.caption("The output is 13. Assignment changes state; it does not claim old total = new total.")
        self.wait(6);self.clear_scene();self.heading("CHANGE THE DATA. KEEP THE PROMISE.")
        self.add(label("[4, 7, 2] → 13",40,color=G).move_to([0,1.4,0]))
        self.add(label("[4, −7, 2] → −1",40,color=A).move_to([0,.1,0]))
        self.caption("The same loop still works: it adds each value once. The invariant explains why.")
        self.wait(9)
