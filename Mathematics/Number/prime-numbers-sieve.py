"""Manim companion: sieve invariant, square-root stopping rule, Euclid escape.
Render: manim -qk prime-numbers-sieve.py PrimeSieve
"""
from manim import *
from math import isqrt, prod
config.background_color='#1e1e1e'
TXT, DIM, BLUE, GREEN, RED, AMBER='#cccccc','#888888','#2563eb','#059669','#dc2626','#f59e0b'
class PrimeSieve(Scene):
    def text(self,s,y,size=30):
        return Text(s,font='Arial',font_size=size,color=TXT).move_to([0,y,0])
    def replace_caption(self,new):
        self.play(FadeOut(self.caption),run_time=.3)
        self.caption=new
        self.play(FadeIn(new),run_time=.3)
    def construct(self):
        title=self.text('Find primes by crossing out products',3.4,38)
        self.caption=self.text('1 is neither prime nor composite',-3.25,27)
        cells={}
        for n in range(1,101):
            cells[n]=Text(str(n),font='Arial',font_size=24,color=TXT).move_to([-4.5+((n-1)%10),2.35-((n-1)//10)*.49,0])
        self.play(FadeIn(title),FadeIn(VGroup(*cells.values())),FadeIn(self.caption))
        self.play(cells[1].animate.set_color(DIM).set_opacity(.3))
        self.wait(2)
        crossed=set()
        for p in (2,3,5,7):
            ring=SurroundingRectangle(cells[p],color=AMBER,buff=.1)
            self.replace_caption(self.text(f'{p} survives: it is prime. Cross out multiples from {p*p}.',-3.25,27))
            self.play(FadeIn(ring),cells[p].animate.set_color(GREEN))
            self.wait(1)
            new=[n for n in range(p*p,101,p) if n not in crossed]
            self.play(LaggedStart(*[cells[n].animate.set_color(RED).set_opacity(.3) for n in new],lag_ratio=.09),run_time=4)
            crossed.update(range(p*p,101,p))
            self.wait(2)
            self.play(FadeOut(ring),run_time=.4)
        self.replace_caption(self.text('Next survivor: 11. But 11² > 100, so the sieve is complete.',-3.25,26))
        remaining=[n for n in range(2,101) if n not in crossed]
        assert len(remaining)==25
        self.play(*[cells[n].animate.set_color(GREEN) for n in remaining],run_time=2)
        self.wait(4)
        self.play(*[FadeOut(m) for m in self.mobjects],run_time=1)
        title=self.text('Why can we stop at the square root?',3.3,38)
        eq=self.text('If n = a × b and BOTH factors exceed √n ...',1.2,34)
        result=self.text('... then a × b > n. Impossible.',0,36)
        note=self.text('Every composite has a prime factor at most √n.',-1.5,31)
        self.play(FadeIn(title),FadeIn(eq));self.wait(3)
        self.play(FadeIn(result));self.wait(3)
        self.play(FadeIn(note));self.wait(4)
        self.play(*[FadeOut(m) for m in self.mobjects])
        title=self.text('A finite list of primes can never be complete',3.3,36)
        row=self.text('2     3     5     7     11     13',1.8,38)
        product=self.text('2 × 3 × 5 × 7 × 11 × 13 = 30030',.6,33)
        plus=self.text('Add one: 30031',-.5,37)
        self.play(FadeIn(title),FadeIn(row));self.wait(2)
        self.play(FadeIn(product));self.wait(2)
        self.play(FadeIn(plus));self.wait(2)
        self.caption=self.text('Division by every listed prime leaves remainder 1.',-2,28)
        self.play(FadeIn(self.caption));self.wait(4)
        self.replace_caption(self.text('30031 = 59 × 509. Neither prime was on the list.',-2,28))
        assert prod([2,3,5,7,11,13])+1==59*509
        self.wait(4)
        punch=self.text('The new number need not be prime. A new prime factor is enough.',-3,24)
        self.play(FadeIn(punch));self.wait(5)
