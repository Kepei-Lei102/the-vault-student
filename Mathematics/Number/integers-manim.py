"""Stack: Manim Community. Render: manim -qk integers-manim.py Integers.
Counter cancellation and the distributive-law argument; no narration.
"""
from manim import *
BG='#1e1e1e'; TXT='#cccccc'; DIM='#888888'; GREEN='#059669'; RED='#dc2626'; BLUE='#2563eb'; AMBER='#f59e0b'
config.background_color=BG

def text(s,size=30):
    t=Text(s,font='Arial',font_size=size,color=TXT)
    assert t.width<13.2,s
    return t

def chip(positive,pos):
    c=Circle(radius=.28,color=GREEN if positive else RED,fill_opacity=.18)
    sign=Text('+' if positive else '−',font='Arial',font_size=27,color=TXT)
    return VGroup(c,sign).move_to(pos)

class Integers(Scene):
    def heading(self,s):self.play(FadeIn(text(s,40).move_to([0,3.2,0])),run_time=.6)
    def caption(self,s):
        if hasattr(self,'cap'):self.play(FadeOut(self.cap),run_time=.2)
        self.cap=text(s,27).move_to([0,-3.1,0]);self.play(FadeIn(self.cap),run_time=.4)
    def clean(self):
        self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.6)
        if hasattr(self,'cap'):del self.cap
    def construct(self):
        self.heading('A debt removed is a gain')
        labels=VGroup(text('Assets: +1 each',25).move_to([-3,1.8,0]),text('Debts: −1 each',25).move_to([3,1.8,0]))
        positive=VGroup(*[chip(True,[-3.4+i*.8,.7,0]) for i in range(2)])
        negative=VGroup(*[chip(False,[2.2+i*.8,.7,0]) for i in range(3)])
        eq=MathTex('2-3=-1',font_size=48,color=TXT).move_to([0,-.8,0])
        self.play(FadeIn(labels),FadeIn(positive),FadeIn(negative),FadeIn(eq))
        self.caption('Two units owned, three owed: the net balance is −1.');self.wait(4)
        self.caption('Cancel the three debts. No new asset has been handed over.');self.wait(2)
        self.play(negative.animate.shift(UP*1.1).set_opacity(0),run_time=2)
        new=MathTex('-1-(-3)=2',font_size=48,color=TXT).move_to(eq)
        self.play(Transform(eq,new),run_time=1)
        self.caption('Subtracting a negative raises the balance.');self.wait(4);self.clean()

        self.heading('Different records. The same integer.')
        labels=VGroup(text('Positive counters',25).move_to([-3,2,0]),text('Negative counters',25).move_to([3,2,0]))
        self.play(FadeIn(labels))
        pos=VGroup();neg=VGroup(*[chip(False,[2.6+i*.8,.8,0]) for i in range(2)])
        self.play(FadeIn(neg))
        eq=MathTex('[0,2]=-2',font_size=44,color=TXT).move_to([0,-1.1,0]);self.play(FadeIn(eq))
        self.caption('The pair [a,b] records a positives and b negatives.');self.wait(3)
        for k in (1,2):
            p=chip(True,[-3.4+(k-1)*.8,.8,0]);n=chip(False,[2.6+(k-1)*.8,-.1,0])
            self.caption('Add one of each: +1 and −1 cancel in the net value.')
            self.play(FadeIn(p,shift=UP),FadeIn(n,shift=UP),run_time=1.4)
            pos.add(p);neg.add(n)
            self.play(Transform(eq,MathTex(f'[{k},{k+2}]=-2',font_size=44,color=TXT).move_to(eq)),run_time=.8);self.wait(2.2)
        self.caption('An integer is the whole family of equivalent records.');self.wait(3);self.clean()

        self.heading('The multiplication rule has to distribute')
        a=MathTex('3(2+(-2))=0',font_size=43,color=TXT).move_to([0,1.6,0])
        b=MathTex('6+3(-2)=0',font_size=43,color=TXT).move_to([0,.35,0])
        c=MathTex('3(-2)=-6',font_size=43,color=TXT).move_to([0,-.9,0])
        self.caption('A product with zero is zero. Expand the same quantity.')
        self.play(FadeIn(a));self.wait(2);self.play(FadeIn(b));self.wait(2);self.play(FadeIn(c));self.wait(3)
        self.play(FadeOut(a),FadeOut(b),FadeOut(c))
        a=MathTex('(-3)(2+(-2))=0',font_size=43,color=TXT).move_to([0,1.6,0])
        b=MathTex('-6+(-3)(-2)=0',font_size=43,color=TXT).move_to([0,.35,0])
        c=MathTex('(-3)(-2)=6',font_size=46,color=TXT).move_to([0,-.9,0])
        self.caption('Now multiply by −3. What must cancel the −6?')
        self.play(FadeIn(a));self.wait(2);self.play(FadeIn(b));self.wait(3)
        self.play(FadeIn(c));self.play(Create(SurroundingRectangle(c,color=AMBER,buff=.22)))
        self.caption('Keep distributivity, and the positive answer is forced.');self.wait(5)
