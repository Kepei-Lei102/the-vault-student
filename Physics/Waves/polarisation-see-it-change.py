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
        self.heading("POLARISATION: project the field, then square")
        theta=ValueTracker(0)
        origin=np.array([-3.,-.4,0]); scale=2.4
        self.add(Line(origin+LEFT*2.8,origin+RIGHT*2.8,color=DIM))
        self.add(label("Transmission axis",22).move_to([-3,-1.25,0]))
        field=always_redraw(lambda: Arrow(origin,origin+scale*np.array([np.cos(theta.get_value()),np.sin(theta.get_value()),0]),buff=0,color=B,stroke_width=7))
        projection=always_redraw(lambda: Line(origin,origin+RIGHT*(max(.001,scale*np.cos(theta.get_value()))),color=G,stroke_width=10))
        self.add(field,projection,label("Incoming electric-field amplitude",22,color=B).move_to([-3,2.55,0]))
        self.add(label("I / I₀ = cos² θ",36).move_to([3,1.6,0]))
        frame=Rectangle(width=3.2,height=.55,color=DIM).move_to([3,.4,0]);self.add(frame)
        bar=always_redraw(lambda: Rectangle(width=max(.001,3.2*np.cos(theta.get_value())**2),height=.5,fill_color=G,fill_opacity=.8,stroke_width=0).move_to(frame.get_center()).align_to(frame,LEFT).shift(RIGHT*.02))
        number=DecimalNumber(1,num_decimal_places=2,color=TXT,font_size=40).move_to([3,-.7,0])
        number.add_updater(lambda m:m.set_value(np.cos(theta.get_value())**2))
        self.add(bar,number)
        self.caption("Looking along the beam. The green length is the component that passes.")
        self.wait(4);self.play(theta.animate.set_value(PI/2),run_time=8,rate_func=linear)
        self.caption("At 90°, the component vanishes: crossed filters give extinction.")
        self.wait(4);self.caption("Turn back towards 45°: the transmitted component grows again.");self.play(theta.animate.set_value(PI/4),run_time=4)
        self.caption("At 45°, amplitude is 0.707 of the input; intensity is 0.50.")
        self.wait(5);self.clear_scene()
        self.heading("ADD A THIRD FILTER — AND LIGHT RETURNS")
        xs=[-4.4,0,4.4]
        for x,angle,title in zip(xs,[PI/2,PI/4,0],["Vertical input","45° filter","Horizontal analyser"]):
            circle=Circle(radius=.72,color=DIM).move_to([x,.6,0])
            v=.65*np.array([np.cos(angle),np.sin(angle),0])
            axis=Line(circle.get_center()-v,circle.get_center()+v,color=P,stroke_width=7)
            group=VGroup(circle,axis,label(title,23,width=3.7).move_to([x,1.8,0]))
            if x==0:middle=group
            else:self.add(group)
        self.caption("First compare the crossed pair: vertical light cannot pass a horizontal axis.")
        blocked=label("Without the middle filter: 0",32,color=R).move_to([0,-1.25,0])
        self.add(blocked);self.wait(5);self.remove(blocked)
        self.caption("Insert a 45° filter: two successive projections now transmit some light.")
        self.play(FadeIn(middle,shift=DOWN),run_time=1.2)
        vals=["I₀","I₀ / 2","I₀ / 4"]
        for i,x in enumerate(xs):
            self.play(FadeIn(label(vals[i],34).move_to([x,-.65,0])),run_time=.6)
            if i<2:self.play(GrowArrow(Arrow([x+.85,.6,0],[xs[i+1]-.85,.6,0],color=G,buff=0)),run_time=1.4)
            self.wait(2)
        self.caption("Each filter prepares the direction received by the next. No step creates energy.")
        self.wait(6)
