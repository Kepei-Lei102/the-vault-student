"""Stack: Manim CE. Render: manim -qk raid-manim.py RAIDRecovery.
Layout matches raid-lab.py, all byte labels calculated rather than hand-copied.
"""
from manim import *
from functools import reduce
from operator import xor

config.background_color = '#1e1e1e'
TXT, DIM = '#cccccc', '#888888'
BLUE, PURPLE, GREEN, RED, AMBER = '#2563eb', '#7c3aed', '#059669', '#dc2626', '#f59e0b'


def text(s, size=28, color=TXT):
    return Text(s, font_size=size, color=color, font='DejaVu Sans')


def block(label, color):
    box = RoundedRectangle(width=2.35, height=.70, corner_radius=.10,
                           stroke_color=color, fill_color=color, fill_opacity=.18)
    return VGroup(box, text(label, 25))


class RAIDRecovery(Scene):
    def caption(self, line):
        new = text(line, 27).move_to([0, -2.7, 0])
        if hasattr(self, 'cap'):
            self.play(FadeOut(self.cap), run_time=.3)
            self.play(FadeIn(new), run_time=.3)
        else:
            self.play(FadeIn(new), run_time=.6)
        self.cap = new

    def construct(self):
        title = text('Lose a drive. Keep the data.', 43).to_edge(UP, buff=.45)
        subtitle = text('RAID 5  /  four drives  /  hexadecimal byte labels', 23, DIM).next_to(title, DOWN, buff=.18)
        self.play(FadeIn(title), FadeIn(subtitle))
        xs = [-4.35, -1.45, 1.45, 4.35]
        labels = VGroup(*[text(f'Drive {d}', 26).move_to([x, 1.7, 0]) for d,x in enumerate(xs)])
        self.play(FadeIn(labels))
        values = [(0x3c,0xa5,0x66),(0x0f,0x33,0xcc),(0xaa,0x55,0x0f)]
        rows, cells, parities = [], [], []
        for r,data in enumerate(values):
            pcol = 3-r
            it = iter(enumerate(data))
            row, objs = [], []
            for d,x in enumerate(xs):
                if d == pcol:
                    v = reduce(xor,data); label=f'P{r} = {v:02X}'; color=PURPLE
                else:
                    j,v = next(it); label=f'{chr(65+r)}{j} = {v:02X}'; color=BLUE
                row.append(v)
                obj=block(label,color).move_to([x,.85-r*.95,0]);objs.append(obj)
                if d == pcol: parities.append(obj)
            rows.append(row);cells.append(objs)
        self.caption('Each row is a stripe: three data blocks and one parity block.')
        for row in cells:
            self.play(LaggedStart(*[FadeIn(c,shift=DOWN*.15) for c in row], lag_ratio=.16),run_time=1.5)
        self.wait(3)
        self.caption('Parity rotates between drives. There is no dedicated parity drive.')
        self.play(*[Indicate(p,color=PURPLE) for p in parities],run_time=2)
        self.wait(3)
        self.caption('First stripe: 3C XOR A5 XOR 66 = FF. Repeat at every byte offset.')
        equation=text('3C  XOR  A5  XOR  66  =  FF',32).move_to([0,-1.95,0])
        self.play(FadeIn(equation));self.wait(4)
        self.play(FadeOut(equation))
        self.caption('Drive 1 fails. Its location is known; its contents are missing.')
        lost=[]
        for r in range(3):
            missing=block('MISSING',RED).move_to(cells[r][1]);lost.append(missing)
        self.play(*[ReplacementTransform(cells[r][1],lost[r]) for r in range(3)],
                  labels[1].animate.set_color(RED),run_time=1.2)
        self.wait(4)
        self.caption('The surviving blocks determine the missing block in each stripe.')
        for r in range(3):
            survivors=[d for d in range(4) if d != 1]
            val=reduce(xor,(rows[r][d] for d in survivors))
            assert val == rows[r][1]
            eq=text('  XOR  '.join(f'{rows[r][d]:02X}' for d in survivors)+f'  =  {val:02X}',32).move_to([0,-1.95,0])
            restored=block(('P2' if r==2 else f'{chr(65+r)}1')+f' = {val:02X}',GREEN).move_to(lost[r])
            self.play(FadeIn(eq),*[Indicate(cells[r][d],color=AMBER) for d in survivors],run_time=1.1)
            self.wait(2)
            self.play(ReplacementTransform(lost[r],restored),run_time=.8)
            self.wait(1);self.play(FadeOut(eq),run_time=.4)
        self.caption('A5, 33 and F0 rebuilt: data AND parity restored on the replacement.')
        self.play(labels[1].animate.set_color(GREEN));self.wait(4)
        self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.8)
        del self.cap
        heading=text('What if two drives are missing?',41).to_edge(UP,buff=.7)
        self.play(FadeIn(heading))
        lines=VGroup(text('A XOR B = 99',40),text('3C XOR A5 = 99',31),text('00 XOR 99 = 99',31),
                     text('256 possible byte pairs. One equation is not enough.',27,AMBER)).arrange(DOWN,buff=.5)
        self.play(FadeIn(lines));self.wait(5)
        self.caption('RAID 6 adds a second independent relation, not another copy of P.')
        self.wait(5)
        self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.8);del self.cap
        title=text('A mirror has no undo button.',42).to_edge(UP,buff=.65)
        left=block('photo.jpg',BLUE).move_to([-2,0,0]);right=block('photo.jpg',BLUE).move_to([2,0,0])
        self.play(FadeIn(title),FadeIn(left),FadeIn(right))
        self.caption('An ordinary deletion is faithfully applied to both mirror members.')
        self.wait(3)
        self.play(ReplacementTransform(left,block('deleted',RED).move_to(left)),
                  ReplacementTransform(right,block('deleted',RED).move_to(right)),run_time=1.2)
        self.wait(2)
        self.caption('Availability needs redundancy. Recovery also needs independent history.')
        self.wait(5)
