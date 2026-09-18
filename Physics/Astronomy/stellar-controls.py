"""Manim companion: manim -qk stellar-controls.py StellarControls.
Requires adjacent stellar-model.py; schematic sizes/colours, calculated curves/readouts.
"""
from manim import *
from pathlib import Path
import importlib.util
import numpy as np
sp=importlib.util.spec_from_file_location('stellar',Path(__file__).with_name('stellar-model.py'));m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
config.background_color='#1e1e1e'
TXT='#cccccc';DIM='#888888';BLUE='#2563eb';AMBER='#f59e0b';TEAL='#0891b2'
def txt(s,size=29):
 t=Text(s,font='Arial',font_size=size,color=TXT)
 if t.width>12.8:t.scale_to_fit_width(12.8)
 return t
class StellarControls(Scene):
 def wipe(self):self.play(*[FadeOut(x) for x in list(self.mobjects)],run_time=.7)
 def construct(self):
  self.add(txt('One bright dot. Three different causes.',40).to_edge(UP,buff=.4))
  for i,s in enumerate(['Distance controls how widely the light is spread.','Radius controls how much surface emits.','Temperature controls the emission from each square metre.']):
   self.play(FadeIn(txt(s).move_to([0,1.5-i*1.2,0])),run_time=.5);self.wait(2)
  self.wait(2);self.wipe()
  self.add(txt('1. Move the same star farther away',38).to_edge(UP,buff=.4))
  d=ValueTracker(1)
  self.add(Dot([-4,0,0],radius=.22,color=AMBER),txt('same luminosity',24).move_to([-4,1,0]))
  detector=always_redraw(lambda:Rectangle(width=.15,height=1.1,color=TEAL).move_to([-4+2*d.get_value(),0,0]))
  ray=always_redraw(lambda:Line([-3.75,0,0],[-4+2*d.get_value(),0,0],color=DIM))
  value=always_redraw(lambda:txt(f'distance = {d.get_value():.2f} ×     received flux = {1/d.get_value()**2:.3f} ×',30).move_to([0,-1.6,0]))
  self.add(detector,ray,value,txt('F = L / (4πd²)',36).move_to([0,-2.55,0]));self.wait(2)
  self.play(d.animate.set_value(2),run_time=4,rate_func=linear);self.wait(3)
  self.add(txt('Twice the distance: one quarter of the flux.',27).move_to([0,2,0]));self.wait(3);self.wipe()
  self.add(txt('2. Enlarge the star at the same temperature',38).to_edge(UP,buff=.4))
  r=ValueTracker(1)
  star=always_redraw(lambda:Circle(radius=.7*r.get_value(),color=AMBER,fill_opacity=.2).move_to([-3,0,0]))
  values=always_redraw(lambda:VGroup(txt(f'Radius: {r.get_value():.2f} ×',30),txt(f'Luminosity: {r.get_value()**2:.2f} ×',30)).arrange(DOWN,buff=.5).move_to([2.5,.25,0]))
  self.add(star,values,txt('Same T and distance: L and received F both scale as R².',27).move_to([0,-2.4,0]));self.wait(2)
  self.play(r.animate.set_value(2),run_time=4,rate_func=linear);self.wait(4);self.wipe()
  self.add(txt('3. Heat the same surface: the spectrum changes',37).to_edge(UP,buff=.4))
  axes=Axes(x_range=[0,2500,500],y_range=[0,110,25],x_length=9,y_length=3.6,axis_config={'color':DIM,'include_tip':False}).move_to([-.5,-.2,0])
  temp=ValueTracker(3000)
  wave=np.linspace(100,2500,250)
  def curve(t,col):
   points=[axes.c2p(w,float(m.spectrum(w*1e-9,t))*1e-12) for w in wave]
   return VMobject(color=col,stroke_width=4).set_points_as_corners(points)
  baseline=curve(3000,DIM)
  live=always_redraw(lambda:curve(temp.get_value(),BLUE))
  peak=always_redraw(lambda:Dot(axes.c2p(m.B/temp.get_value()*1e9,float(m.spectrum(m.B/temp.get_value(),temp.get_value()))*1e-12),color=AMBER,radius=.07))
  read=always_redraw(lambda:txt(f'T = {temp.get_value():.0f} K     peak = {m.B/temp.get_value()*1e9:.0f} nm     L = {(temp.get_value()/3000)**4:.1f} ×',27).move_to([0,2.3,0]))
  self.add(axes,baseline,live,peak,read,txt('Wavelength / nm     (horizontal ticks: 500 nm)',23).move_to([0,-2.45,0]),txt('Vertical: surface spectral power / kW m⁻² nm⁻¹',23).move_to([0,-2.95,0]))
  self.wait(2);self.play(temp.animate.set_value(6000),run_time=6,rate_func=linear);self.wait(4);self.wipe()
  self.add(txt('Choose the route your measurements support',37).to_edge(UP,buff=.4))
  for i,s in enumerate(['Spectrum peak → temperature T','Calibrated candle: known L + flux → distance d','Independent distance + flux → luminosity L','Luminosity + temperature → radius R']):
   self.play(FadeIn(txt(s,29).move_to([0,1.7-i*.95,0])),run_time=.4);self.wait(1.3)
  self.add(txt('Without an independent distance: only R/d is determined.',26).to_edge(DOWN,buff=.5));self.wait(4)
