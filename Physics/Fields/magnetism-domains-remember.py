"""Stack: Manim CE. Schematic domain response, not a micromagnetic simulation."""
from manim import *
import numpy as np
config.background_color='#1e1e1e'
TXT='#cccccc'; DIM='#888888'; BLUE='#2563eb'; GREEN='#059669'; AMBER='#f59e0b'; PURPLE='#7c3aed'
def label(t,y,size=28):
 m=Text(t,font_size=size,color=TXT).move_to([0,y,0]);
 if m.width>12.5:m.scale_to_fit_width(12.5)
 return m
def regions(cx,signs):
 g=VGroup()
 for i,sg in enumerate(signs):
  x=cx+(i%4-1.5)*1.05;y=(.5-i//4)*1.1
  box=Square(.95,stroke_color=DIM,stroke_width=1.2,fill_color=BLUE,fill_opacity=.08).move_to([x,y,0])
  ar=Arrow([x-.32*sg,y,0],[x+.32*sg,y,0],buff=0,color=AMBER,stroke_width=5,max_tip_length_to_length_ratio=.28)
  g.add(VGroup(box,ar))
 return g
class DomainsRemember(Scene):
 def change_caption(self,mob,new):
  self.play(FadeOut(mob),run_time=.25);mob.become(new);self.play(FadeIn(mob),run_time=.25)
 def construct(self):
  title=label('A magnet changes the balance',3.25,40)
  sub=label('Each arrow represents a region containing many aligned atomic moments.',2.55,23)
  self.play(FadeIn(title),FadeIn(sub));self.wait(2)
  a=regions(0,[1,-1,1,-1,-1,1,-1,1]);cap=label('Locally ordered. Almost cancelling as a whole.',-2.2)
  self.play(FadeIn(a),FadeIn(cap));self.wait(4)
  field=VGroup(Arrow([-2,1.7,0],[2,1.7,0],color=GREEN,buff=0),Text('Applied field',font_size=22,color=GREEN).move_to([0,2.05,0]))
  self.play(FadeIn(field));self.change_caption(cap,label('Growth and rotation favour the field direction.',-2.2));self.play(Transform(a,regions(0,[1]*8)),run_time=4);self.wait(3)
  self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=1)
  title=label('A domain wall moves',3.25,40);cap=label('The favourable region grows; the atoms do not slide across the sample.',-2.25,26)
  left=Rectangle(width=2,height=2,fill_color=BLUE,fill_opacity=.18,stroke_width=0).move_to([-2,0,0]);right=Rectangle(width=4,height=2,fill_color=PURPLE,fill_opacity=.18,stroke_width=0).move_to([1,0,0]);wall=Line([-1,-1,0],[-1,1,0],color=TXT)
  arr1=Arrow([-2.6,0,0],[-1.4,0,0],buff=0,color=AMBER);arr2=Arrow([1.6,0,0],[.4,0,0],buff=0,color=AMBER)
  self.play(FadeIn(VGroup(title,cap,left,right,wall,arr1,arr2)));self.wait(3)
  self.play(left.animate.stretch_to_fit_width(4.8).move_to([-.6,0,0]),right.animate.stretch_to_fit_width(1.2).move_to([2.4,0,0]),wall.animate.shift(RIGHT*2.8),arr2.animate.shift(RIGHT*1.4),run_time=5);self.wait(3)
  self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=1)
  title=label('What remains when the field is removed?',3.3,38)
  names=VGroup(Text('Soft sample',font_size=29,color=TXT).move_to([-3.1,2.05,0]),Text('Hard sample',font_size=29,color=TXT).move_to([3.1,2.05,0]))
  aa=regions(-3.1,[1]*8);bb=regions(3.1,[1]*8)
  cap=label('Both have been magnetised in the same direction.',-2.1,27)
  status=label('FIELD ON →',2.7,23)
  self.play(FadeIn(VGroup(title,names,aa,bb,cap,status)));self.wait(4)
  self.change_caption(status,label('APPLIED FIELD OFF',2.7,23))
  self.change_caption(cap,label('Less retained in this soft sample; much more in this hard sample.',-2.1,25))
  self.play(Transform(aa,regions(-3.1,[1,-1,1,1,-1,1,-1,1])),Transform(bb,regions(3.1,[1,1,1,1,1,-1,1,1])),run_time=4);self.wait(5)
  note=label('Schematic only: retention also depends on shape and magnetic history.',-2.75,21)
  self.play(FadeIn(note));self.wait(3)
  self.change_caption(status,label('SMALL REVERSE FIELD ←',2.7,23));self.change_caption(cap,label('Soft means easy reversal. Hard means resistance to reversal.',-2.1,26));self.play(Transform(aa,regions(-3.1,[-1]*8)),run_time=4);self.wait(4)
  self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=1)
  self.play(FadeIn(label('The material is chosen for the job.',2.4,40)))
  self.play(FadeIn(label('Relay / transformer: change readily.',.8,32)),FadeIn(label('Permanent magnet / stored bit: remember reliably.',-.3,32)))
  self.play(FadeIn(label('Easy to change and hard to erase are different design goals.',-2,26)));self.wait(5)
