"""Particle-model teaching schematic, not a molecular-dynamics solver.
Render: manim -qk particle-model-motion.py ParticleModel
All dots keep their radius. Same 24 particles through solid/liquid/gas.
Gas trajectories reflect at walls; compression is a rescaled, isothermal
spacing illustration, not a simulated thermodynamic piston process.
"""
from manim import *
import numpy as np

config.background_color = '#1e1e1e'
TXT, GREY, BLUE, TEAL, AMBER = '#cccccc', '#888888', '#2563eb', '#0891b2', '#f59e0b'

class ParticleModel(Scene):
    def label(self, text, y, size=28):
        return Text(text, color=TXT, font_size=size, font="Arial").move_to([0,y,0])

    def construct(self):
        title = self.label('Matter changes its arrangement', 3.25, 40)
        caption = self.label('SOLID: close neighbours; vibration about fixed positions', -2.65)
        footer = self.label('Schematic • dot size is unchanged • distances are not to scale', -3.4, 20)
        box = Rectangle(width=8, height=4, color=GREY).move_to([0,0,0])
        positions = np.array([[.43*(i-2.5), .43*(j-1.5),0] for j in range(4) for i in range(6)])
        dots = VGroup(*[Dot(p, radius=.115, color=BLUE) for p in positions])
        self.play(FadeIn(title), FadeIn(box), FadeIn(dots), FadeIn(caption), FadeIn(footer))
        clock = ValueTracker(0)
        for i,d in enumerate(dots):
            d.add_updater(lambda m,i=i: m.move_to(positions[i]+.045*np.array([np.sin(clock.get_value()*8+i),np.cos(clock.get_value()*7+i),0])))
        self.play(clock.animate.set_value(7), run_time=7, rate_func=linear)
        for d in dots: d.clear_updaters()
        self.play(Transform(caption, self.label('LIQUID: still close; neighbours can rearrange', -2.65)), run_time=1)
        # Offset rows and rotate small local quartets to show neighbour exchange.
        liquid = np.array([[.52*(i-2.5)+(.18 if j%2 else 0), .48*(j-1.5)-.6,0] for j in range(4) for i in range(6)])
        self.play(*[d.animate.move_to(p) for d,p in zip(dots,liquid)], run_time=2)
        for _ in range(2):
            groups = [VGroup(*[dots[j*6+i],dots[j*6+i+1],dots[(j+1)*6+i+1],dots[(j+1)*6+i]]) for j in (0,2) for i in (0,2,4)]
            self.play(*[Rotate(g, PI/2, about_point=g.get_center()) for g in groups],run_time=2)
        self.wait(2)
        gas = np.array([[1.25*(i-2.5),.92*(j-1.5),0] for j in range(4) for i in range(6)])
        self.play(Transform(caption,self.label('GAS: far apart; random motion fills the container', -2.65)),*[d.animate.move_to(p) for d,p in zip(dots,gas)],run_time=2)
        rng = np.random.default_rng(625)
        vel = rng.uniform(-1.5,1.5,(24,2))
        t = ValueTracker(0)
        def bounce(a, half):
            return half-np.abs((a+half)%(4*half)-2*half)
        for i,d in enumerate(dots):
            d.add_updater(lambda m,i=i: m.move_to([bounce(gas[i,0]+vel[i,0]*t.get_value(),3.85),bounce(gas[i,1]+vel[i,1]*t.get_value(),1.85),0]))
        self.play(t.animate.set_value(7),run_time=7,rate_func=linear)
        for d in dots: d.clear_updaters()
        self.play(Transform(title,self.label('Squeeze the space, not the particles',3.25,40)),Transform(caption,self.label('Same number • same dot size • less space between particles',-2.65)),run_time=1)
        self.wait(2)
        self.play(box.animate.stretch_to_fit_width(4),*[d.animate.move_to(d.get_center()*np.array([.48,1,1])) for d in dots],run_time=4)
        self.play(Transform(caption,self.label('At fixed temperature: half the volume → twice the pressure',-2.65)),run_time=1)
        self.wait(4)
        self.play(*[FadeOut(m) for m in (box,dots,title,caption,footer)],run_time=1)
        title=self.label('Brownian motion: the visible speck is not a molecule',3.25,34)
        caption=self.label('Invisible molecules deliver unequal kicks from changing directions',-2.6,25)
        footer=self.label('Illustrative kicks • molecule sizes and times greatly exaggerated',-3.35,20)
        speck=Dot(ORIGIN,radius=.34,color=AMBER)
        self.play(FadeIn(title),FadeIn(caption),FadeIn(footer),FadeIn(speck))
        # Each incoming molecule reaches the speck before the kick is shown.
        offsets=[RIGHT,UP,LEFT,DOWN,UR,LEFT,DR,UP]
        shifts=[LEFT*.45,DOWN*.3,RIGHT*.6,UP*.4,DL*.3,RIGHT*.3,UL*.3,DOWN*.2]
        for direction,shift in zip(offsets,shifts):
            unit=direction/np.linalg.norm(direction)
            old=speck.get_center().copy()
            molecule=Dot(old+unit*1.6,radius=.065,color=TEAL)
            self.add(molecule)
            self.play(molecule.animate.move_to(old+unit*.41),run_time=.35,rate_func=linear)
            trail=Line(old,old+shift,color=AMBER,stroke_width=2)
            self.add(trail)
            self.play(speck.animate.shift(shift),molecule.animate.move_to(old+unit*1.4),run_time=.5)
            self.remove(molecule)
            self.wait(.25)
        self.play(Transform(caption,self.label('The jitter is evidence of molecular motion, not life in the speck',-2.6,25)),run_time=1)
        self.wait(5)
