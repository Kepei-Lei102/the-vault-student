"""Manim: manim -qk hubble-expansion.py HubbleExpansion.
Schematic comoving points, fixed-size galaxies. a=1+0.1t, not a fitted cosmology.
"""
from manim import *
import numpy as np
config.background_color='#1e1e1e'
TXT='#cccccc';DIM='#888888';BLUE='#2563eb';GREEN='#059669';AMBER='#f59e0b';PURPLE='#7c3aed'
def text(s,size=28):
    t=Text(s,font='Arial',font_size=size,color=TXT)
    if t.width>12.7:t.scale_to_fit_width(12.7)
    return t
class HubbleExpansion(Scene):
    def clear_scene(self):
        for m in list(self.mobjects):m.clear_updaters()
        self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.5)
    def flow(self,observer,label):
        q=np.array([[-1,-1,0],[-1,0,0],[-1,1,0],[0,-1,0],[0,0,0],[0,1,0],[1,-1,0],[1,0,0],[1,1,0]],float)
        obs=q[observer];rel=q-obs
        self.add(text('Expansion has no preferred observer',38).to_edge(UP,buff=.4))
        self.add(text(label,27).move_to([-3,2.3,0]))
        a=ValueTracker(1)
        # Fixed viewport, no apparent change of galaxy size.
        dots=VGroup(*[Dot(radius=.065,color=AMBER if i==observer else BLUE) for i in range(len(q))])
        for i,dot in enumerate(dots):dot.add_updater(lambda m,i=i:m.move_to(np.array([-3.4,0,0])+.75*a.get_value()*rel[i]))
        axes=Axes(x_range=[0,5,1],y_range=[0,.5,.1],x_length=5,y_length=3,axis_config={'color':DIM,'include_tip':False}).move_to([3,0,0])
        self.add(axes,text('Proper distance d / model units',20).move_to([3,-1.95,0]),text('Recession speed v / model units',20).move_to([3,1.95,0]))
        line=always_redraw(lambda:Line(axes.c2p(0,0),axes.c2p(5,5*.1/a.get_value()),color=GREEN))
        graph=VGroup(*[Dot(radius=.045,color=AMBER if i==observer else BLUE) for i in range(len(q))])
        for i,dot in enumerate(graph):dot.add_updater(lambda m,i=i:m.move_to(axes.c2p(a.get_value()*np.linalg.norm(rel[i]),.1*np.linalg.norm(rel[i]))))
        read=always_redraw(lambda:text(f'a = {a.get_value():.2f}     H = (da/dt)/a = {.1/a.get_value():.3f}',25).move_to([0,-2.6,0]))
        self.add(dots,line,graph,read,text('Every separation scales by a. Galaxy symbols keep their size.',24).to_edge(DOWN,buff=.4))
        self.wait(2);self.play(a.animate.set_value(1.6),run_time=6,rate_func=linear);self.wait(3)
        self.clear_scene()
    def construct(self):
        self.add(text('The farther galaxy gains more distance',38).to_edge(UP,buff=.5))
        for i,s in enumerate(['Two gaps both grow by 20%.','A 10-unit gap gains 2; a 30-unit gap gains 6.','Same fractional growth → speed proportional to distance.']):
            self.play(FadeIn(text(s,29).move_to([0,1.3-i*1.1,0])),run_time=.4);self.wait(1.6)
        self.wait(2);self.clear_scene()
        self.flow(4,'Observe from the middle galaxy')
        self.flow(1,'Now observe from its neighbour')
        self.add(text('Does 1/H₀ tell us the exact age?',38).to_edge(UP,buff=.4))
        ax=Axes(x_range=[-1.05,.2,.25],y_range=[0,1.3,.25],x_length=9,y_length=4,axis_config={'color':DIM,'include_tip':False}).move_to([-.6,-.15,0])
        self.add(ax,text('Past ←     time relative to now, in units of 1/H₀',23).move_to([0,-2.65,0]),text('Scale factor a',23).move_to([-4.9,2.3,0]))
        for p,col in [(1,BLUE),(2/3,GREEN),(.5,PURPLE)]:
            xs=np.linspace(-p,.15,250)
            curve=VMobject(color=col).set_points_as_corners([ax.c2p(x,max(0,1+x/p)**p) for x in xs])
            self.play(FadeIn(curve),run_time=.5)
        self.add(Dot(ax.c2p(0,1),color=AMBER),DashedLine(ax.c2p(-.25,.75),ax.c2p(.18,1.18),color=DIM),text('same present a and slope',24).move_to([2,2.3,0]))
        self.wait(3)
        for p,col,lab in [(1,BLUE,'Coasting: 1/H₀'),(2/3,GREEN,'Matter only: 2/(3H₀)'),(.5,PURPLE,'Radiation only: 1/(2H₀)')]:
            dot=Dot(ax.c2p(0,1),color=col,radius=.085);self.add(dot)
            path=VMobject().set_points_as_corners([ax.c2p(x,max(0,1+x/p)**p) for x in np.linspace(0,-p,180)])
            self.play(MoveAlongPath(dot,path),run_time=1.8)
            self.play(FadeIn(text(lab,22).set_color(col).move_to([2,-.2-(1-p)*3,0])),run_time=.3)
        self.add(text('The age depends on the whole expansion history.',28).to_edge(DOWN,buff=.35));self.wait(5)
