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
        self.heading("DOPPLER: the wave speed stays the same")
        time=ValueTracker(0);speed=.35;c=.85;period=1.25
        start=-3.8; centre_y=.15
        source=always_redraw(lambda: Dot([start+speed*time.get_value(),centre_y,0],radius=.10,color=A))
        def fronts():
            t=time.get_value();g=VGroup()
            for emitted in np.arange(0,12.6,period):
                age=t-emitted
                if age>.02:
                    # Clip the circles to the demonstration window; the centres remain at emission sites.
                    origin=np.array([start+speed*emitted,centre_y,0]);rad=c*age
                    points=[]
                    for angle in np.linspace(0,TAU,401):
                        pt=origin+rad*np.array([np.cos(angle),np.sin(angle),0])
                        if -6.4<pt[0]<6.4 and -1.9<pt[1]<2.1: points.append(pt)
                        elif len(points)>1:
                            g.add(VMobject(color=B,stroke_width=2).set_points_as_corners(points));points=[]
                        else:points=[]
                    if len(points)>1:g.add(VMobject(color=B,stroke_width=2).set_points_as_corners(points))
            return g
        rings=always_redraw(fronts);self.add(rings,source)
        self.add(label("Behind: wider spacing",23).move_to([-3,-2.4,0]),label("Ahead: closer spacing",23).move_to([3,-2.4,0]))
        self.caption("Each crest expands from where it was emitted — not from where the source is now.")
        self.play(time.animate.set_value(12),run_time=16,rate_func=linear)
        self.wait(4);self.clear_scene()
        self.heading("ONE SOURCE PERIOD: follow two successive crests")
        self.add(label("In one period T:",30).move_to([0,2.35,0]))
        lines=[("The old crest travels", "vT",B),("The source advances", r"u_s T",A),("Gap ahead", r"\lambda = (v-u_s)T",G),("Arrivals per second", r"f_o = v/\lambda = f_s v/(v-u_s)",G)]
        for i,(name,formula,col) in enumerate(lines):
            y=1.3-i*.85
            self.play(FadeIn(label(name,25).move_to([-3.2,y,0])),FadeIn(MathTex(formula,font_size=34,color=col).move_to([2.5,y,0])),run_time=.7)
            self.wait(3)
        self.caption("The source changes the spacing. It does not carry the sound faster through the air.")
        self.wait(4);self.clear_scene()
        self.heading("MOVING OBSERVER: same spacing, faster encounters")
        t=ValueTracker(0)
        crests=always_redraw(lambda: VGroup(*[Line([x+.55*t.get_value(),-1.2,0],[x+.55*t.get_value(),1.2,0],color=B) for x in np.arange(-12,7,1.3) if -6<x+.55*t.get_value()<6]))
        observer=always_redraw(lambda: Dot([3.4-.25*t.get_value(),0,0],radius=.17,color=A))
        self.add(crests,observer,label("Observer moves into the approaching fronts",25).move_to([0,2,0]))
        self.caption("Here λ is unchanged; the encounter speed is v + observer speed. Sound formulas are medium-relative.")
        self.play(t.animate.set_value(10),run_time=10,rate_func=linear);self.wait(4)
