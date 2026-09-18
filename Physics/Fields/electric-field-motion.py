"""Stack: Manim Community. Field superposition and motion are different questions.
Render: manim -qk electric-field-motion.py ElectricFieldMotion
Coordinates and time in the animation are dimensionless; displayed formulae give SI physics.
"""
from manim import *
import numpy as np
config.background_color = '#1e1e1e'
TXT, BLUE, RED, GREEN, AMBER = '#cccccc', '#2563eb', '#dc2626', '#059669', '#f59e0b'

def label(s, size=28, color=TXT):
    return Text(s, font='Arial', font_size=size, color=color)

class ElectricFieldMotion(Scene):
    def heading(self, title, subtitle):
        self.add(label(title,38).to_edge(UP,buff=.35),label(subtitle,24).to_edge(DOWN,buff=.38))
    def reset(self):
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=1)
    def construct(self):
        self.heading('1. Add fields at the SAME point','The source charges stay fixed. Move the observation point.')
        left=np.array([-3.,0,0]); right=np.array([3.,0,0])
        sources=VGroup(Dot(left,radius=.16,color=BLUE),Dot(right,radius=.16,color=RED),label('+Q',28,BLUE).move_to(left+DOWN*.5),label('-Q',28,RED).move_to(right+DOWN*.5))
        self.play(FadeIn(sources)); self.wait(2)
        theta=ValueTracker(.35)
        def point():return np.array([1.6*np.cos(theta.get_value()),1.8*np.sin(theta.get_value()),0])
        def fields():
            p=point(); a=p-left;b=p-right
            return 5*a/np.linalg.norm(a)**3,-5*b/np.linalg.norm(b)**3
        def arrow(v,c,start=None):return Arrow(point() if start is None else start,(point() if start is None else start)+v,buff=0,color=c,stroke_width=5,max_tip_length_to_length_ratio=.18)
        p=always_redraw(lambda:Dot(point(),color=TXT,radius=.07))
        ea=always_redraw(lambda:arrow(fields()[0],BLUE))
        eb=always_redraw(lambda:arrow(fields()[1],RED))
        net=always_redraw(lambda:arrow(sum(fields()),GREEN))
        legend=VGroup(label('blue: from +Q',23,BLUE),label('red: from -Q',23,RED),label('green: vector sum',23,GREEN)).arrange(DOWN,aligned_edge=LEFT).move_to([-4.6,2.25,0])
        self.play(FadeIn(p),FadeIn(ea),FadeIn(eb),FadeIn(legend)); self.wait(3)
        self.play(FadeIn(net));self.wait(3)
        self.play(theta.animate.set_value(2.8),run_time=9,rate_func=linear)
        self.wait(3); self.reset()
        self.heading('2. The field stays; the force can reverse','E describes the sources. F = qE also depends on the test charge.')
        arrows=VGroup(*[Arrow([x,1.7,0],[x,-1.7,0],buff=0,color=BLUE,stroke_width=3) for x in np.linspace(-4.7,4.7,9)])
        plates=VGroup(Line([-5,2,0],[5,2,0],color=RED),Line([-5,-2,0],[5,-2,0],color=BLUE),label('+ plate',24).move_to([5.7,2,0]),label('- plate',24).move_to([5.7,-2,0]))
        self.play(FadeIn(arrows),FadeIn(plates));self.wait(2)
        plus=Dot([-1.7,.3,0],color=AMBER,radius=.14);minus=Dot([1.7,.3,0],color=AMBER,radius=.14)
        labels=VGroup(label('+q',26).next_to(plus,LEFT),label('-q',26).next_to(minus,RIGHT))
        forces=VGroup(Arrow(plus.get_center(),plus.get_center()+DOWN*1.5,buff=0,color=AMBER),Arrow(minus.get_center(),minus.get_center()+UP*1.5,buff=0,color=AMBER))
        self.play(FadeIn(plus),FadeIn(minus),FadeIn(labels));self.wait(2);self.play(FadeIn(forces));self.wait(5);self.reset()
        self.heading('3. A field line is NOT a flight path','Negative charge: acceleration UP; initial velocity RIGHT. No gravity or drag.')
        xs=np.linspace(-5,5,11)
        field=VGroup(*[Arrow([x,1.7,0],[x,-1.7,0],buff=0,color=BLUE,stroke_width=2).set_opacity(.4) for x in xs])
        self.play(FadeIn(field));self.wait(2)
        t=ValueTracker(0)
        def pos():return np.array([-4.7+2*t.get_value(),-1.5+.125*t.get_value()**2,0])
        ball=always_redraw(lambda:Dot(pos(),color=AMBER,radius=.13))
        trajectory=always_redraw(lambda:ParametricFunction(lambda z:np.array([-4.7+2*z,-1.5+.125*z*z,0]),t_range=[0,max(.001,t.get_value())],color=GREEN))
        velocity=always_redraw(lambda:Arrow(pos(),pos()+np.array([1,.125*t.get_value(),0]),buff=0,color=GREEN))
        accel=always_redraw(lambda:Arrow(pos(),pos()+UP*.75,buff=0,color=AMBER))
        legend=VGroup(label('green: velocity / trajectory',23,GREEN),label('amber: acceleration',23,AMBER)).arrange(DOWN,aligned_edge=LEFT).move_to([-3.6,2.3,0])
        self.play(FadeIn(ball),FadeIn(trajectory),FadeIn(velocity),FadeIn(accel),FadeIn(legend));self.wait(2)
        self.play(t.animate.set_value(4.7),run_time=10,rate_func=linear);self.wait(4)
        self.reset()
        self.heading('Follow the causal chain','Charges create E. E gives F = qE. F changes velocity; velocity changes position.')
        chain=VGroup(label('source charges',32,BLUE),label('→  field  →  force  →  acceleration',32),label('→  changing velocity  →  trajectory',32,GREEN)).arrange(DOWN,buff=.55)
        self.play(FadeIn(chain));self.wait(6)
