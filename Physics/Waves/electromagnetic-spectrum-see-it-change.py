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
        self.heading("ONE WAVE FAMILY: frequency changes, vacuum speed does not")
        cycles=ValueTracker(2);phase=ValueTracker(0)
        axes=Axes(x_range=[0,10,2],y_range=[-1.2,1.2,1],x_length=11.5,y_length=2.4,axis_config={'color':DIM,'include_tip':False}).move_to([0,.6,0])
        self.add(axes,label("Position — illustrative scale",23).move_to([0,-1.1,0]))
        # phi=2π f t, k=2π f/c with c=1 display unit/s: constant phase speed.
        wave=always_redraw(lambda: axes.plot(lambda x: .9*np.sin(TAU*cycles.get_value()*(x-phase.get_value())/10),x_range=[0,10,.03],color=B))
        self.add(wave)
        self.caption("A travelling electric-field component. The changing pattern is slowed down for viewing.")
        self.play(phase.animate.set_value(5),run_time=6,rate_func=linear)
        self.wait(3);self.caption("Compare a new source frequency: more cycles fit in the same distance.")
        self.play(cycles.animate.set_value(5),run_time=4)
        self.play(phase.animate.set_value(10),run_time=6,rate_func=linear)
        self.add(label("c = fλ       higher f → shorter λ",32).move_to([0,-2,0]));self.wait(5)
        self.clear_scene();self.heading("PHOTON ENERGY AND BEAM POWER ARE DIFFERENT")
        self.add(label("Same power: 1.0 W = 1.0 J each second",30).move_to([0,2.15,0]))
        data=[("650 nm red",650,R),("450 nm blue",450,B)]
        for i,(name,lam,col) in enumerate(data):
            x=-3.1 if i==0 else 3.1
            energy=6.62607015e-34*299792458/(lam*1e-9);rate=1/energy
            self.add(label(name,30,color=col).move_to([x,1.05,0]))
            self.add(label(f"Each photon: {energy/1.602176634e-19:.2f} eV",26).move_to([x,.15,0]))
            self.add(label(f"{rate/1e18:.2f} × 10¹⁸ photons/s",25).move_to([x,-.7,0]))
        self.caption("At equal power, blue carries more energy per photon, so fewer photons arrive each second.")
        self.wait(9)
        self.play(FadeIn(label("P = photon rate × hf",34,color=G).move_to([0,-1.9,0])),run_time=1)
        self.wait(6);self.clear_scene();self.heading("THE SPECTRUM IS CONTINUOUS")
        names=["Radio","Microwave","Infrared","Visible","Ultraviolet","X-ray","Gamma"]
        for i,name in enumerate(names):
            x=-5.7+i*1.9
            self.play(FadeIn(label(name,23,width=1.75).move_to([x,.6,0])),run_time=.35)
        self.play(GrowArrow(Arrow([-6,-.6,0],[6,-.6,0],color=G,buff=0)),run_time=1.5)
        self.add(label("Increasing frequency and photon energy; decreasing wavelength",26).move_to([0,-1.4,0]))
        self.caption("Naming regions are approximate; microwaves are radio, and X-ray/gamma energies overlap.")
        self.wait(6)
