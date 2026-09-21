"""Stack: Manim CE. A4 oscillator-bank listening ladder; render qm, qh, qk.
Audio comes only from fourier-piano-lab.py. The recipe is an illustrative model.
"""
from pathlib import Path
import importlib.util
import numpy as np
from manim import *
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('piano',ROOT/'fourier-piano-lab.py');p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
config.background_color='#1e1e1e'
TXT='#cccccc';DIM='#999999';BLUE='#60a5fa';PINK='#ed78b3';AMBER='#f4b44c'
class AdditivePiano(Scene):
 def text(self,s,y,size=28):
  m=Text(s,font='DejaVu Sans',font_size=size,color=TXT).move_to([0,y,0])
  if m.width>12.8:m.scale_to_fit_width(12.8)
  return m
 def curve(self,ax,t,y,color=BLUE):
  line=VMobject(color=color,stroke_width=3);line.set_points_as_corners([ax.c2p(float(a),float(b)) for a,b in zip(t,y)]);return line
 def construct(self):
  self.add(self.text('Build A4 from sine waves',3.35,36))
  eq=self.text('sample = sine 1 + sine 2 + sine 3 + ...',2.55,27);self.play(FadeIn(eq));self.wait(2)
  waveax=Axes(x_range=[0,4.55,1],y_range=[-.5,.5,.25],x_length=6,y_length=2.8,axis_config={'color':DIM,'include_tip':False}).move_to([-3.4,-.25,0])
  specax=Axes(x_range=[0,13,2],y_range=[0,.26,.1],x_length=5,y_length=2.8,axis_config={'color':DIM,'include_tip':False}).move_to([3.7,-.25,0])
  wavlabel=self.text('Two cycles of the repeating waveform',-2.35,22).move_to([-3.4,-2.35,0])
  speclabel=Text('Harmonic amplitudes',font='DejaVu Sans',font_size=22,color=TXT).move_to([3.7,-2.35,0])
  self.play(FadeIn(waveax),FadeIn(specax),FadeIn(wavlabel),FadeIn(speclabel))
  time_label=Text('time / ms',font_size=18,color=DIM).move_to([-3.4,-1.93,0]);self.add(time_label)
  numbers=VGroup(*[Text(str(n),font_size=17,color=DIM).move_to(specax.c2p(n,0)+DOWN*.22) for n in [1,4,8,12]])
  self.add(numbers)
  snapshot=np.linspace(0,2/p.F0,700);wave=VMobject();bars=VGroup();subtitle=None;footer=None
  names=['1. A single 440 Hz sine','2. Add 880, 1320 and 1760 Hz','3. Add through the 12th harmonic: 5280 Hz','4. A strike: rapid attack, then different decays','5. Add a little string-like complexity']
  notes=['One pitch, almost no spectral variety.','Add the values at each instant; do not play them one after another.','A richer steady buzz still lacks the shape of a struck note.','Higher partials fade faster in this chosen recipe.','36 sines: 3 nearby strings, slightly stretched partials. Still a model.']
  for i,(key,count,struck,strings,seconds) in enumerate(p.STAGES):
   if subtitle is not None:self.play(FadeOut(subtitle),FadeOut(footer),run_time=.25)
   subtitle=self.text(names[i],1.85,25);footer=self.text(notes[i],-3.25,22)
   self.play(FadeIn(subtitle),FadeIn(footer),run_time=.5)
   if not struck:
    newwave=self.curve(waveax,snapshot*1000,p.partials(snapshot,count).sum(axis=1))
    newbars=VGroup(*[Line(specax.c2p(n,0),specax.c2p(n,p.GAIN*a),color=PINK,stroke_width=9) for n,a in zip(p.N[:count],p.A[:count])])
    if i==0:self.play(FadeIn(newwave),FadeIn(newbars),run_time=.6);wave=newwave;bars=newbars
    else:self.play(Transform(wave,newwave),Transform(bars,newbars),run_time=.6)
    self.add_sound(str(ROOT/f'fourier-piano-{key}.wav'));self.wait(seconds+.4)
   else:
    if i==3:
     self.play(FadeOut(wave),FadeOut(bars),FadeOut(waveax),FadeOut(wavlabel),run_time=.5)
     # Axes labels are added explicitly for seconds; remove the old ms label.
     self.remove(time_label)
     envax=Axes(x_range=[0,5,1],y_range=[0,1,.5],x_length=6,y_length=2.8,axis_config={'color':DIM,'include_tip':False}).move_to([-3.4,-.25,0])
     ts=np.linspace(0,5,700);curves=VGroup(*[self.curve(envax,ts,p.envelope(ts)[:,j],c) for j,c in [(0,BLUE),(3,AMBER),(11,PINK)]])
     labels=VGroup(Text('Time since strike / s (0 to 5)',font_size=21,color=TXT).move_to([-3.4,-2.35,0]),Text('Envelopes: n = 1, 4, 12',font_size=21,color=TXT).move_to([-3.4,1.35,0]))
     self.play(FadeIn(envax),FadeIn(curves),FadeIn(labels),run_time=.6)
    if i==4:
     replacement=Text('Amplitude per partial family',font='DejaVu Sans',font_size=21,color=TXT).move_to(speclabel)
     self.play(Transform(speclabel,replacement),run_time=.4)
    pos=ValueTracker(0)
    cursor=always_redraw(lambda:Line(envax.c2p(pos.get_value(),0),envax.c2p(pos.get_value(),1),color=DIM,stroke_width=2))
    live=always_redraw(lambda:VGroup(*[Line(specax.c2p(n,0),specax.c2p(n,max(1e-7,p.GAIN*a*e)),color=PINK,stroke_width=9) for n,a,e in zip(p.N,p.A,p.envelope(np.array([pos.get_value()]))[0])]))
    self.add(cursor,live);self.add_sound(str(ROOT/f'fourier-piano-{key}.wav'));self.play(pos.animate.set_value(seconds),run_time=seconds,rate_func=linear);self.wait(.6);cursor.clear_updaters();live.clear_updaters();self.remove(cursor,live)
  self.play(*[FadeOut(m) for m in self.mobjects],run_time=.6)
  self.play(FadeIn(self.text('Synthesis adds the ingredients.',.6,34)),FadeIn(self.text('An FFT analyses which frequencies are present.',-.35,27)))
  self.wait(4)
