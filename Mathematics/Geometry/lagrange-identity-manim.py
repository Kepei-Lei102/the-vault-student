"""Stack: Manim Community. Render: manim -qk lagrange-identity-manim.py LagrangeIdentity.
Unit-vector geometry -> sum of squares -> centred data and residuals.
Keep the finished MP4 beside the card; use an external media_dir for caches.
"""
from manim import *
import numpy as np

config.background_color = '#1e1e1e'
TXT, DIM = '#cccccc', '#888888'
BLUE, GREEN, AMBER = '#2563eb', '#059669', '#f59e0b'

def text(s, size=28):
    return Text(s, font='Arial', font_size=size, color=TXT)

def math(s, size=36):
    return MathTex(s, font_size=size, color=TXT)

class LagrangeIdentity(Scene):
    def clear_scene(self):
        self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=1)

    def construct(self):
        self.geometry()
        self.clear_scene()
        self.squares()
        self.clear_scene()
        self.data()
        self.wait(3)

    def geometry(self):
        title=text('Same lengths. Changing alignment.',40).to_edge(UP,buff=.45)
        sub=text('Two unit vectors; the drawing is magnified.',24).next_to(title,DOWN)
        self.play(FadeIn(title),FadeIn(sub))
        o=np.array([-3.8,-1.2,0]); radius=1.9; angle=ValueTracker(20*DEGREES)
        tip=lambda:o+radius*np.array([np.cos(angle.get_value()),np.sin(angle.get_value()),0])
        arrowa=Arrow(o,o+radius*RIGHT,buff=0,color=BLUE)
        arrowb=always_redraw(lambda:Arrow(o,tip(),buff=0,color=AMBER))
        patch=always_redraw(lambda:Polygon(o,o+radius*RIGHT,tip()+radius*RIGHT,tip(),stroke_width=1,stroke_color=GREEN,fill_color=GREEN,fill_opacity=.2))
        shadow=always_redraw(lambda:DashedLine(tip(),np.array([tip()[0],o[1],0]),color=DIM))
        la=math(r'\mathbf a').move_to(o+radius*RIGHT+DOWN*.4)
        lb=always_redraw(lambda:math(r'\mathbf b').move_to(tip()+UP*.35))
        self.play(FadeIn(patch),FadeIn(arrowa),FadeIn(arrowb),FadeIn(shadow),FadeIn(la),FadeIn(lb))
        eq=math(r'(\mathbf a\cdot\mathbf b)^2+\mathrm{area}^2=1',34).move_to([2.85,1.7,0])
        self.play(FadeIn(eq))
        base=np.array([.7,-1.35,0]); width=4.5
        outline=Rectangle(width=width,height=.65,color=DIM).move_to(base+RIGHT*width/2+UP*.325)
        def bars():
            c=float(np.cos(angle.get_value())**2)
            first=Rectangle(width=max(width*c,.0001),height=.65,stroke_width=0,fill_color=BLUE,fill_opacity=1).move_to(base+RIGHT*width*c/2+UP*.325)
            second=Rectangle(width=max(width*(1-c),.0001),height=.65,stroke_width=0,fill_color=GREEN,fill_opacity=1).move_to(base+RIGHT*(width*c+width*(1-c)/2)+UP*.325)
            return VGroup(first,second)
        moving=always_redraw(bars)
        labels=VGroup(text('squared dot',23).move_to([1.7,-1.95,0]),text('squared area',23).move_to([4.05,-1.95,0]))
        labels[0].set_color(BLUE); labels[1].set_color(GREEN)
        value=DecimalNumber(np.cos(angle.get_value()),num_decimal_places=2,font_size=32,color=TXT).move_to([3.8,.55,0])
        value.add_updater(lambda m:m.set_value(np.cos(angle.get_value())))
        signed=text('dot product =',26).move_to([1.95,.55,0])
        footer=text('Track the sum; keep the sign of the dot product separate.',25).to_edge(DOWN,buff=.5)
        self.play(FadeIn(outline),FadeIn(moving),FadeIn(labels),FadeIn(signed),FadeIn(value),FadeIn(footer))
        self.wait(2)
        for degrees in [0,60,90,135,180]:
            self.play(angle.animate.set_value(degrees*DEGREES),run_time=2.2,rate_func=smooth)
            self.wait(1)
        # Freeze all redraws before fading, so their regenerated children do not ignore opacity.
        for m in [patch,arrowb,shadow,lb,moving,value]:
            m.clear_updaters()

    def squares(self):
        title=text('The picture becomes algebra in any dimension.',37).to_edge(UP,buff=.5)
        self.play(FadeIn(title))
        left=math(r'\|\mathbf a\|^2\|\mathbf b\|^2-(\mathbf a\cdot\mathbf b)^2',43).move_to([0,1.7,0])
        right=math(r'=\sum_{i<j}(a_i b_j-a_j b_i)^2',43).move_to([0,.3,0])
        self.play(FadeIn(left)); self.wait(2)
        self.play(FadeIn(right)); self.wait(3)
        note=text('Cancel the diagonal terms. Pair the off-diagonal terms.',27).move_to([0,-.8,0])
        self.play(FadeIn(note)); self.wait(3)
        bound=math(r'|\mathbf a\cdot\mathbf b|\leq\|\mathbf a\|\,\|\mathbf b\|',43).move_to([0,-2,0])
        reason=text('Every square is non-negative.',27).move_to([0,-3.15,0])
        self.play(FadeIn(bound),FadeIn(reason)); self.wait(4)
        equal=text('Equality: proportional vectors, or either vector is zero.',25).move_to(reason)
        self.play(FadeOut(reason),FadeIn(equal)); self.wait(3)

    def data(self):
        title=text('Now the arrows are lists of measurements.',37).to_edge(UP,buff=.5)
        self.play(FadeIn(title))
        ax=Axes(x_range=[0,5,1],y_range=[0,7,1],x_length=5.4,y_length=4.4,axis_config={'color':DIM,'include_tip':False,'include_numbers':True,'font_size':20}).move_to([-3,-.2,0])
        x=np.array([1,2,3,4]);y=np.array([2,4,4,6]);pred=1+1.2*x
        dots=VGroup(*[Dot(ax.c2p(xx,yy),color=GREEN,radius=.07) for xx,yy in zip(x,y)])
        fit=ax.plot(lambda z:1+1.2*z,x_range=[.5,4.5],color=BLUE)
        residuals=VGroup(*[Line(ax.c2p(xx,yy),ax.c2p(xx,pp),color=AMBER,stroke_width=5) for xx,yy,pp in zip(x,y,pred)])
        axes_labels=VGroup(text('reference x (V)',22).next_to(ax,DOWN,buff=.12),text('sensor y (V)',22).next_to(ax,UP,buff=.1))
        self.play(FadeIn(ax),FadeIn(axes_labels),FadeIn(dots));self.wait(2)
        center=text('Subtract each list’s own mean.',26).move_to([3.2,1.8,0])
        r=math(r'r=\frac{\mathbf a\cdot\mathbf b}{\|\mathbf a\|\,\|\mathbf b\|}',38).move_to([3.2,.65,0])
        self.play(FadeIn(center),FadeIn(r));self.wait(3)
        self.play(Create(fit),FadeIn(residuals));self.wait(2)
        numbers=VGroup(math(r'r^2=0.9',36),math(r'\mathrm{SSE}=8(1-r^2)=0.8',32)).arrange(DOWN,buff=.5).move_to([3.2,-1.15,0])
        self.play(FadeIn(numbers));self.wait(3)
        sums=math(r'\mathbf a\cdot\mathbf a=5,\quad\mathbf b\cdot\mathbf b=8,\quad\mathbf a\cdot\mathbf b=6',25).move_to([3.2,-2.5,0])
        self.play(FadeIn(sums));self.wait(2)
        footer=text('The sum of squares measures what the fitted line misses.',25).to_edge(DOWN,buff=.55)
        self.play(FadeIn(footer));self.wait(3)
        warning=text('Perfect correlation still need not mean matching readings.',25).move_to(footer)
        self.play(FadeOut(footer),FadeIn(warning));self.wait(3)
