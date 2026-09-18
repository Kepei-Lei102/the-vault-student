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
        self.heading("ENERGY LEVELS: the photon is the gap")
        levels={1:-13.6,2:-3.4,3:-13.6/9,4:-.85}
        def y(n):return -2.0+(levels[n]+13.6)*.31
        for n in [1,2,3]:
            line=Line([-5,y(n),0],[-.7,y(n),0],color=DIM)
            self.add(line,label(f"n = {n}    {levels[n]:.2f} eV",21,width=3.3).move_to([-3.6,y(n)+.22,0]))
        self.add(label("Hydrogen energy ladder (not an orbit picture)",23).move_to([0,2.6,0]))
        state=Dot([-2.5,y(3),0],radius=.12,color=A);self.add(state)
        self.caption("Dot = energy, not position. Each trial starts from a prepared excited state.")
        self.wait(5)
        for high,low,col in [(3,2,R),(3,1,B),(2,1,P)]:
            self.remove(state);state.move_to([-2.5,y(high),0]);self.add(state)
            gap=levels[high]-levels[low];lam=1239.841984/gap
            desc=label(f"{high} → {low}:  ΔE = {gap:.2f} eV",30).move_to([3.1,1.4,0])
            wave=label(f"λ = {lam:.0f} nm" + (" (ultraviolet)" if lam<400 else " (red light)"),27).move_to([3.1,.45,0])
            self.play(FadeIn(desc),FadeIn(wave),run_time=.6)
            self.caption("Larger gap → shorter wavelength. Photon colours are symbolic for ultraviolet.")
            photon=Dot([-2.5,y(low),0],radius=.11,color=col)
            self.play(state.animate.move_to([-2.5,y(low),0]),run_time=1.3)
            self.add(photon);self.play(photon.animate.move_to([5.8,y(low),0]),run_time=2)
            self.wait(3);self.remove(desc,wave,photon)
        self.clear_scene();self.heading("CASCADES: conserve energy, not photon count")
        direct=levels[3]-levels[1];a=levels[3]-levels[2];b=levels[2]-levels[1]
        self.add(label("Same initial state n = 3. Same final state n = 1.",28).move_to([0,2.2,0]))
        self.play(FadeIn(label(f"Direct: one photon, {direct:.2f} eV",32,color=P).move_to([0,1,0])),run_time=1)
        self.wait(4)
        self.play(FadeIn(label(f"Via n = 2: two photons, {a:.2f} + {b:.2f} eV",32,color=A).move_to([0,-.15,0])),run_time=1)
        self.wait(4)
        self.play(FadeIn(label("The energy sums agree. The wavelengths do not add.",30).move_to([0,-1.5,0])),run_time=1)
        self.caption("An atomic line spectrum measures allowed energy differences, not the sizes of orbits.")
        self.wait(7)
