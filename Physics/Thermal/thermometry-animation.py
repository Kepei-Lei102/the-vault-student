"""Manim: synthetic sensor calibration, followed by thermal response. Final -qk."""
from manim import *
import numpy as np
config.background_color='#1e1e1e'
GREY='#bbbbbb'; BLUE='#2563eb'; GREEN='#059669'; PURPLE='#7c3aed'; AMBER='#f59e0b'
class Thermometry(Scene):
    def label(self,text,size=29,color=GREY): return Text(text,font="Helvetica",font_size=size,color=color)
    def construct(self):
        title=self.label('Different signals. One temperature.',42).to_edge(UP)
        self.play(FadeIn(title))
        axes=Axes(x_range=[0,100,20],y_range=[0,100,20],x_length=7,y_length=3.7,tips=False,axis_config={'color':'#888888','include_numbers':True,'font_size':20}).shift(LEFT*2+UP*.1)
        labels=VGroup(self.label('Bath temperature / °C',23).next_to(axes,DOWN),self.label('Endpoint-normalised signal / %',23).next_to(axes,UP))
        straight=axes.plot(lambda t:t,x_range=[0,100],color=GREEN)
        curved=axes.plot(lambda t:t+.002*t*(t-100),x_range=[0,100],color=PURPLE)
        note=self.label('Synthetic sensor laws\nEndpoints: 0 °C and 100 °C',23).move_to(RIGHT*4+UP*1.6)
        legend=VGroup(self.label('Liquid:  L = 10 + 0.4 θ',23,BLUE),self.label('Metal:  R = 100 + 0.385 θ',23,GREEN),self.label('Curved emf response',23,PURPLE)).arrange(DOWN,aligned_edge=LEFT).move_to(RIGHT*4+UP*.2)
        foot=self.label('Normalising endpoints does not straighten a curved response.',25).to_edge(DOWN)
        self.play(FadeIn(axes),FadeIn(labels),FadeIn(straight),FadeIn(curved),FadeIn(note),FadeIn(legend),FadeIn(foot))
        t=ValueTracker(0)
        dots=always_redraw(lambda:VGroup(Dot(axes.c2p(t.get_value(),t.get_value()),color=GREEN),Dot(axes.c2p(t.get_value(),t.get_value()+.002*t.get_value()*(t.get_value()-100)),color=PURPLE)))
        read=always_redraw(lambda:self.label(f'Bath: {t.get_value():.0f} °C\nLinear reading: {t.get_value():.0f} °C\nCurved reading: {t.get_value()+.002*t.get_value()*(t.get_value()-100):.0f} °C',25).move_to(RIGHT*4+DOWN*1.7))
        self.add(dots,read)
        self.play(t.animate.set_value(50),run_time=5,rate_func=linear);self.wait(4)
        self.play(t.animate.set_value(100),run_time=5,rate_func=linear);self.wait(3)
        self.play(*[FadeOut(m) for m in list(self.mobjects)])
        title=self.label('A correct calibration cannot remove thermal lag.',38).to_edge(UP)
        axes=Axes(x_range=[0,40,10],y_range=[20,80,20],x_length=9,y_length=3.7,tips=False,axis_config={'color':'#888888','include_numbers':True,'font_size':22}).shift(LEFT*.9+UP*.15)
        labs=VGroup(self.label('Time after entering an 80 °C bath / s',24).next_to(axes,DOWN),self.label('Probe temperature / °C',24).next_to(axes,UP))
        clock=ValueTracker(0); colors=[BLUE,GREEN,PURPLE];taus=[2,6,10]
        curves=VGroup(*[axes.plot(lambda x,tau=tau:80-60*np.exp(-x/tau),x_range=[0,40],color=c) for tau,c in zip(taus,colors)])
        legends=VGroup(*[self.label(f'τ = {tau} s',25,c) for tau,c in zip(taus,colors)]).arrange(DOWN).to_edge(RIGHT).shift(UP*.4)
        dots=always_redraw(lambda:VGroup(*[Dot(axes.c2p(clock.get_value(),80-60*np.exp(-clock.get_value()/tau)),color=c) for tau,c in zip(taus,colors)]))
        foot=self.label('Illustrative probes: same final reading, different response times.',25).to_edge(DOWN)
        self.play(FadeIn(title),FadeIn(axes),FadeIn(labs),FadeIn(curves),FadeIn(legends),FadeIn(foot));self.add(dots)
        self.play(clock.animate.set_value(40),run_time=10,rate_func=linear);self.wait(5)
