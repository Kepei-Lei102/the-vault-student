"""Stack: Manim Community. Ideal spin-1/2 fermions, 1-D infinite well.
Render: manim -qk pauli-manim.py PauliFilling
No electron trajectories are drawn: arrows indicate occupied spin states.
"""
from manim import *
import numpy as np

BG='#1e1e1e'; TXT='#cccccc'; DIM='#888888'
BLUE='#2563eb'; GREEN='#059669'; AMBER='#f59e0b'; RED='#dc2626'; PURPLE='#7c3aed'
config.background_color=BG


def prose(s, size=28, color=TXT):
    return Text(s,font="Arial",font_size=size,color=color)


def arrow_state(pos,up=True,color=BLUE):
    sign=1 if up else -1
    return Arrow(pos+DOWN*.19*sign,pos+UP*.19*sign,buff=0,color=color,
                 stroke_width=4,max_tip_length_to_length_ratio=.3)


class PauliFilling(Scene):
    def caption(self, line):
        if hasattr(self,'cap'):
            self.play(FadeOut(self.cap),run_time=.25)
        self.cap=prose(line,26).move_to([0,-3.25,0])
        assert self.cap.width < 13.3, line
        self.play(FadeIn(self.cap),run_time=.4)

    def clear_scene(self):
        self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.7)
        if hasattr(self,'cap'):del self.cap

    def construct(self):
        self.orbital()
        self.filling()
        self.compress()
        self.conclusion()

    def orbital(self):
        title=prose('One orbital is not one complete state',40).to_edge(UP,buff=.4)
        box=RoundedRectangle(width=3.2,height=1.5,corner_radius=.15,color=DIM).move_to(LEFT*2)
        label=prose('one spatial orbital',25).next_to(box,UP,buff=.35)
        spins=VGroup(arrow_state(np.array([-2.6,0,0]),True,GREEN),arrow_state(np.array([-1.4,0,0]),False,GREEN)).scale(1.65)
        # Keep scaled group centred in its orbital.
        spinlabels=VGroup(prose('spin up',22),prose('spin down',22)).arrange(RIGHT,buff=.7).move_to([-2,-1.25,0])
        self.play(FadeIn(title),FadeIn(box),FadeIn(label),run_time=1)
        self.caption('A complete state includes the spatial wavefunction AND spin.')
        self.play(FadeIn(spins[0]),FadeIn(spinlabels[0]),run_time=.8);self.wait(1.8)
        self.play(FadeIn(spins[1]),FadeIn(spinlabels[1]),run_time=.8);self.wait(2)
        third=arrow_state(np.array([3.,0,0]),True,RED).scale(1.65)
        msg=prose('A third needs\nanother orbital.',30).move_to([3,1.25,0])
        self.play(FadeIn(third),FadeIn(msg),run_time=.8)
        self.caption('Two independent spin states. No third copy of either state.')
        self.wait(4)
        self.clear_scene()

    def filling(self):
        title=prose('Fill the lowest available states',40).to_edge(UP,buff=.4)
        subtitle=prose('Six noninteracting fermions in a 1-D infinite well, T = 0',25).move_to([0,2.65,0])
        self.play(FadeIn(title),FadeIn(subtitle),run_time=1)
        ladder=VGroup();states=[]
        for j,y in [(1,-1.5),(2,-.45),(3,1.3)]:
            line=Line([-3.8,y,0],[-.3,y,0],color=DIM)
            lab=prose(f'j = {j}   E = {j*j} E₁',23).move_to([-5.25,y,0])
            ladder.add(line,lab)
            states.extend([arrow_state(np.array([-3.2,y+.26,0]),True,BLUE),arrow_state(np.array([-1.7,y+.26,0]),False,BLUE)])
        self.play(FadeIn(ladder),run_time=1)
        self.caption('Each spatial mode has two spin states. Then move up.')
        for i,state in enumerate(states):
            self.play(FadeIn(state),run_time=.4);self.wait(.5)
        equation=MathTex(r'U=2(1+4+9)E_1=28E_1',font_size=34,color=TXT).move_to([3.,.4,0])
        equation.scale_to_fit_width(5.3)
        self.play(FadeIn(equation),run_time=.7)
        self.caption('Zero temperature means the lowest ALLOWED total energy.')
        self.wait(4)
        boson=prose('Six ideal spinless bosons:\nall may occupy j = 1; U = 6E₁',23).move_to([3,-1.15,0])
        self.play(FadeIn(boson),run_time=.7);self.wait(4)
        self.clear_scene()

    def compress(self):
        ratio=ValueTracker(1.)
        title=prose('Now squeeze the occupied states',40).to_edge(UP,buff=.4)
        sub=prose('Slow compression; mode occupations stay fixed',25).move_to([0,2.65,0])
        self.play(FadeIn(title),FadeIn(sub),run_time=1)
        baseline=-2.2; energy_scale=.24
        def level(j):
            y=baseline+energy_scale*j*j/ratio.get_value()**2
            line=Line([-5.2,y,0],[-1.5,y,0],color=DIM)
            a=arrow_state(np.array([-4.,y+.25,0]),True,BLUE)
            b=arrow_state(np.array([-2.7,y+.25,0]),False,BLUE)
            return VGroup(line,a,b,prose(f'j = {j}',22).move_to([-5.9,y,0]))
        levels=VGroup(*[always_redraw(lambda j=j:level(j)) for j in [1,2,3]])
        # Right-hand curves are wavefunction shapes, vertically offset; not energy.
        def modes():
            L=4.4*ratio.get_value(); centre=3.4; left=centre-L/2; right=centre+L/2
            group=VGroup(Line([left,-2.35,0],[left,1.75,0],color=GREEN),Line([right,-2.35,0],[right,1.75,0],color=GREEN))
            for j,y0 in [(1,-1.6),(2,-.35),(3,.9)]:
                group.add(Line([left,y0,0],[right,y0,0],color=DIM,stroke_opacity=.4))
                group.add(ParametricFunction(lambda t,j=j,y0=y0:np.array([left+L*t,y0+.36*np.sin(j*PI*t),0]),t_range=[0,1],color=GREEN))
            return group
        waves=always_redraw(modes)
        labels=VGroup(prose('Occupied energies',25).move_to([-3.7,2.1,0]),prose('Spatial mode shapes',25).move_to([3.4,2.1,0]))
        self.play(FadeIn(levels),FadeIn(waves),FadeIn(labels),run_time=1)
        self.caption('The same number of wave lobes must fit in a shorter well.')
        self.wait(4)
        self.play(ratio.animate.set_value(.8),run_time=7,rate_func=smooth)
        self.caption('Every energy rises by 1 / 0.8² = 1.5625. This costs work.')
        self.wait(4)
        self.play(FadeOut(waves),FadeOut(labels[1]),run_time=.7)
        result=VGroup(MathTex(r'E_j\propto L^{-2}',color=TXT,font_size=40),MathTex(r'U:28E_1(L_0)\to43.75E_1(L_0)',color=TXT,font_size=30),MathTex(r'F=-dU/dL=2U/L',color=AMBER,font_size=35)).arrange(DOWN,buff=.5).move_to([3.35,-.15,0])
        self.play(FadeIn(result),run_time=.8)
        self.caption('The gas resists compression even at zero temperature.')
        self.wait(5)
        for m in levels:m.clear_updaters()
        waves.clear_updaters()
        self.clear_scene()

    def conclusion(self):
        title=prose('The bridge to a white dwarf',40).to_edge(UP,buff=.7)
        steps=VGroup(prose('More electrons per volume',32),prose('Higher occupied momenta',32),prose('More energy needed to compress',32)).arrange(DOWN,buff=.55).move_to([0,.75,0])
        self.play(FadeIn(title),run_time=.7)
        for step in steps:self.play(FadeIn(step),run_time=.6);self.wait(1)
        formula=MathTex(r'P=\frac25n_eE_F\ \propto\ n_e^{5/3}',font_size=42,color=AMBER).move_to([0,-1.5,0])
        self.play(FadeIn(formula),run_time=.8)
        self.caption('3-D ideal gas, nonrelativistic electrons, T = 0.')
        self.wait(5)
