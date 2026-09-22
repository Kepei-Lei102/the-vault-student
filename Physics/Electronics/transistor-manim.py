"""Stack: Manim Community. Educational toy transfer curve and RC load.
Render: manim -qk --media_dir /tmp/transistor-manim transistor-manim.py DigitalPromise
"""
from manim import *
import numpy as np
config.background_color='#1e1e1e'
TXT='#cccccc'; DIM='#999999'; BLUE='#2563eb'; GREEN='#059669'; AMBER='#f59e0b'; RED='#dc2626'; PURPLE='#7c3aed'

def label(s,size=26,color=TXT):
    return Text(s,font='Arial',font_size=size,color=color)

def transfer(v):
    if v<=.8:return 3.3-.2*v/.8
    if v>=2:return .2*(3.3-v)/1.3
    return 3.1-2.9*(v-.8)/1.2

class DigitalPromise(Scene):
    def heading(self,title,sub):
        self.add(label(title,38).to_edge(UP,buff=.35),label(sub,23,DIM).move_to([0,2.75,0]))
    def swap(self,old,new,duration):
        self.play(FadeOut(old),run_time=duration/2)
        self.play(FadeIn(new),run_time=duration/2)
        return new
    def construct(self):
        self.heading('Analog voltages. Digital promises.','A settled toy inverter: real interfaces use data-sheet guarantees.')
        vin=ValueTracker(.2)
        # Three nodes in ONE causal chain, with two inverter symbols.
        nodes=[-4.5,0,4.5]
        values=[lambda:vin.get_value(),lambda:transfer(vin.get_value()),lambda:transfer(transfer(vin.get_value()))]
        for x,f,name in zip(nodes,values,['Input','After NOT','After NOT again']):
            self.add(label(name,25).move_to([x,1.7,0]))
            num=always_redraw(lambda x=x,f=f: label(f'{f():.3f} V',33,AMBER if .8<f()<2 else GREEN).move_to([x,.7,0]))
            self.add(num)
            bit=always_redraw(lambda x=x,f=f:label('LOW' if f()<=.8 else 'HIGH' if f()>=2 else 'UNSPECIFIED',21).move_to([x,-.1,0]))
            self.add(bit)
        for x in [-2.25,2.25]:
            tri=Polygon([x-.5,.3,0],[x-.5,1.1,0],[x+.3,.7,0],color=PURPLE)
            self.add(tri,Circle(.07,color=PURPLE).move_to([x+.37,.7,0]),Arrow([x-.9,.7,0],[x-.52,.7,0],buff=0,color=DIM),Arrow([x+.45,.7,0],[x+.9,.7,0],buff=0,color=DIM))
        contract=label('LOW input: 0–0.8 V     |     HIGH input: 2.0–3.3 V',27).move_to([0,-1.2,0])
        self.add(contract)
        cap=label('A LOW output may be as high as 0.2 V.',26).move_to([0,-2.15,0]);self.add(cap)
        self.wait(4)
        cap=self.swap(cap,label('Add 0.45 V of noise: still inside the LOW range.',26).move_to(cap),1)
        self.play(vin.animate.set_value(.65),run_time=4,rate_func=linear);self.wait(5)
        cap=self.swap(cap,label('Each powered stage produces a fresh valid output.',26).move_to(cap),1);self.wait(4)
        cap=self.swap(cap,label('Now add too much noise. The input guarantee is lost.',26).move_to(cap),1)
        self.play(vin.animate.set_value(1.1),run_time=4,rate_func=linear);self.wait(3)
        caution=label('This curve still predicts an output. A real part need not agree.',25,AMBER).move_to([0,-2.85,0]);self.add(caution);self.wait(5)
        self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=1)
        self.heading('Restoration requires moving charge','A 1 kΩ pull-up charges a 10 pF load from a 3.3 V supply.')
        ax=Axes(x_range=[0,50,10],y_range=[0,3.3,1],x_length=8,y_length=3.4,axis_config={'color':DIM,'include_tip':False}).move_to([-.9,-.1,0])
        self.add(ax,label('time / ns',23).next_to(ax,DOWN,buff=.3),label('output / V',23).move_to([-5.2,2.0,0]))
        for x in [0,10,20,30,40,50]:self.add(label(str(x),18,DIM).next_to(ax.c2p(x,0),DOWN,buff=.1))
        for y in [1,2,3]:self.add(label(str(y),18,DIM).next_to(ax.c2p(0,y),LEFT,buff=.12))
        self.add(DashedLine(ax.c2p(0,3.3),ax.c2p(50,3.3),color=DIM),label('3.3 V',21,DIM).next_to(ax.c2p(50,3.3),RIGHT))
        t=ValueTracker(.001)
        curve=always_redraw(lambda:ax.plot(lambda x:3.3*(1-np.exp(-x/10)),x_range=[0,max(.002,t.get_value()),.2],color=BLUE))
        dot=always_redraw(lambda:Dot(ax.c2p(t.get_value(),3.3*(1-np.exp(-t.get_value()/10))),color=GREEN))
        self.add(curve,dot)
        self.play(t.animate.set_value(10),run_time=5,rate_func=linear)
        fact=label('At RC = 10 ns: 63.2% charged, not finished.',25).move_to([0,-2.65,0]);self.add(fact);self.wait(4)
        self.play(t.animate.set_value(50),run_time=7,rate_func=linear);self.wait(2)
        self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=1)
        self.heading('One charge. Then one discharge.','Ordinary resistive switching: follow all the energy.')
        supply=label('Supply delivers\n108.9 pJ',30,TXT).move_to([-4,1,0])
        stored=label('Stored in C\n54.45 pJ',30,TXT).move_to([3,1.6,0])
        heat=label('Charging heat\n54.45 pJ',30,AMBER).move_to([3,-.4,0])
        self.play(FadeIn(supply));self.play(FadeIn(stored),FadeIn(heat),FadeIn(Arrow([-2.3,1.2,0],[1.1,1.6,0],color=GREEN)),FadeIn(Arrow([-2.3,.8,0],[1.1,-.4,0],color=AMBER)),run_time=2);self.wait(5)
        stored=self.swap(stored,label('Discharge heat\n54.45 pJ',30,AMBER).move_to(stored),2);self.wait(3)
        self.add(label('Full LOW → HIGH → LOW cycle: 108.9 pJ dissipated.',27).move_to([0,-2,0]));self.wait(4)
        self.add(label('More charging events per second → more power.',27).move_to([0,-2.85,0]));self.wait(4)
