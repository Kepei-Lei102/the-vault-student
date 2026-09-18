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
        self.heading("RADIOACTIVE DECAY: random lives, predictable populations")
        rng=np.random.default_rng(9702);N=160;half=4.;rate=np.log(2)/half
        lifetimes=rng.exponential(1/rate,N);clock=ValueTracker(0)
        dots=VGroup()
        for i,life in enumerate(lifetimes):
            dot=Dot([-5.9+(i%16)*.28,1.8-(i//16)*.31,0],radius=.075,color=B)
            dot.add_updater(lambda m,life=life:m.set_color(B if clock.get_value()<life else DIM).set_opacity(1 if clock.get_value()<life else .16))
            dots.add(dot)
        self.add(dots,label("Blue: undecayed nuclei",22).move_to([-3.8,-1.65,0]))
        axes=Axes(x_range=[0,12,4],y_range=[0,160,40],x_length=5.2,y_length=3.6,axis_config={'color':DIM,'include_tip':False,'font_size':20}).move_to([3,.3,0])
        axes.add_coordinates()
        self.add(axes,label("Time / s",21).move_to([3,-2,0]),label("Number remaining",22).move_to([3,2.55,0]))
        expected=axes.plot(lambda t:N*np.exp(-rate*t),x_range=[0,12],color=G)
        actual=always_redraw(lambda: VMobject(color=A,stroke_width=3).set_points_as_corners([axes.c2p(t,np.sum(lifetimes>t)) for t in np.linspace(0,max(.001,clock.get_value()),140)]))
        self.add(expected,actual)
        self.add(label("Green: expectation",18,color=G).move_to([1.5,-2.5,0]),label("Amber: this sample",18,color=A).move_to([4.4,-2.5,0]))
        self.caption("Each nucleus has a random waiting time. Half-life is 4 s, not a personal expiry date.")
        self.play(clock.animate.set_value(4),run_time=10,rate_func=linear);self.wait(4)
        self.caption("After one half-life, roughly half remain. A particular sample need not split exactly in half.")
        self.play(clock.animate.set_value(8),run_time=10,rate_func=linear);self.wait(3)
        self.caption("The survivors still have the same decay probability per unit time; they are not overdue.")
        self.play(clock.animate.set_value(12),run_time=10,rate_func=linear);self.wait(4)
        self.clear_scene();self.heading("HALF-LIFE IS A POPULATION STATEMENT")
        for i,s in enumerate(["Survival probability: P(t) = exp(−λt)","At T½:  exp(−λT½) = 1/2","Therefore:  λT½ = ln 2"]):
            self.play(FadeIn(label(s,34).move_to([0,1.5-i*1.2,0])),run_time=.8);self.wait(3)
        self.caption("An idealised sample: no daughter decay or background counts included.")
        self.wait(5)
