"""Manim companion: namespace deletion versus allocation and SSD discard.
Stack: Manim Community. Final: manim -qk file-systems-deletion.py FileDeletion
Schematic model: last name, no open handles, snapshots or retained copies.
TRIM timing and read-after-discard are deliberately not specified.
"""
from manim import *

config.background_color = '#1e1e1e'
TXT, DIM = '#cccccc', '#888888'
BLUE, GREEN, AMBER, RED, PURPLE = '#60a5fa', '#34d399', '#fbbf24', '#f87171', '#a78bfa'


def label(s, size=25, color=TXT):
    return Text(s, font='DejaVu Sans', font_size=size, color=color)


def box(s, pos, color=BLUE, width=3.4):
    shape = RoundedRectangle(width=width, height=0.85, corner_radius=0.12,
                             stroke_color=color, fill_color=color, fill_opacity=0.12)
    return VGroup(shape, label(s, 24)).move_to(pos)


class FileDeletion(Scene):
    def caption(self, s):
        new = label(s, 25).move_to([0, -3.1, 0])
        if hasattr(self, 'cap'):
            self.play(FadeOut(self.cap), FadeIn(new), run_time=0.6)
        else:
            self.play(FadeIn(new), run_time=0.6)
        self.cap = new

    def clear_stage(self):
        self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=0.7)
        if hasattr(self, 'cap'):
            del self.cap

    def construct(self):
        title = label('When a file disappears', 39).move_to([0, 3.25, 0])
        subtitle = label('One file. Three different states.', 25, DIM).move_to([0, 2.55, 0])
        self.play(FadeIn(title), FadeIn(subtitle))
        name = box('photo.jpg', [-3, 1.25, 0])
        meta = box('file record: blocks 2–4', [2.4, 1.25, 0], PURPLE, 4.5)
        arrow = Arrow(name.get_right(), meta.get_left(), buff=0.15, color=DIM)
        self.play(FadeIn(name), FadeIn(meta), GrowArrow(arrow))
        cells = VGroup()
        for i in range(8):
            color = BLUE if 2 <= i <= 4 else DIM
            cell = VGroup(Square(side_length=0.92, stroke_color=color,
                                fill_color=color, fill_opacity=0.18),
                          label('PHOTO' if 2 <= i <= 4 else '—', 17, color),
                          label(str(i), 18, DIM).shift(DOWN * 0.72))
            cells.add(cell)
        cells.arrange(RIGHT, buff=0.12).move_to([0, -0.65, 0])
        state = label('Allocation: blocks 2–4 belong to the photo', 25, BLUE).move_to([0, -1.95, 0])
        self.play(FadeIn(cells), FadeIn(state))
        self.caption('The name leads to a record; the record locates the bytes.')
        self.wait(4)
        self.play(FadeOut(name), FadeOut(arrow), run_time=0.8)
        self.caption('Unlink removes the name. It need not visit every byte.')
        self.wait(4)
        condition = label('Assume: last name, no open handles, no snapshots', 22, AMBER).move_to([0, 1.25, 0])
        available = label('Allocation: blocks 2–4 are now available', 25, AMBER).move_to(state)
        self.play(FadeOut(meta), FadeIn(condition), FadeOut(state), FadeIn(available), run_time=0.8)
        for i in range(2, 5):
            self.play(cells[i][0].animate.set_stroke(AMBER).set_fill(AMBER, opacity=0.10), run_time=0.25)
        self.caption('Simplified HDD: old content may remain in free space.')
        self.wait(5)
        for i in (2, 3):
            newword = label('NEW', 19, GREEN).move_to(cells[i][1])
            self.play(Transform(cells[i][1], newword), cells[i][0].animate.set_stroke(GREEN).set_fill(GREEN, opacity=0.20), run_time=0.7)
        self.play(FadeOut(available), FadeIn(label('Allocation: blocks 2–3 reused; block 4 still free', 25, GREEN).move_to(available)))
        self.caption('Reuse overwrites pieces. A surviving fragment is not a whole photo.')
        self.wait(5)
        self.clear_stage()

        self.play(FadeIn(label('An SSD has a second map', 39).move_to([0, 3.25, 0])))
        logical = box('logical addresses 2–4', [-3.1, 1.6, 0], BLUE, 4.2)
        physical = box('physical flash pages', [3.1, 1.6, 0], PURPLE, 4.2)
        mapping = Arrow(logical.get_right(), physical.get_left(), buff=0.15, color=DIM)
        self.play(FadeIn(logical), FadeIn(physical), GrowArrow(mapping))
        pages = VGroup()
        for word, color in [('PHOTO', BLUE), ('LIVE', GREEN), ('PHOTO', BLUE), ('LIVE', GREEN)]:
            pages.add(box(word, [0, 0, 0], color, 2.0))
        pages.arrange(RIGHT, buff=0.22).move_to([0, -0.05, 0])
        bracket = SurroundingRectangle(pages, buff=0.2, color=DIM)
        blocklabel = label('one schematic flash erase block', 22, DIM).move_to([0, -0.95, 0])
        self.play(FadeIn(pages), Create(bracket), FadeIn(blocklabel))
        self.caption('The controller maps logical addresses to physical pages.')
        self.wait(4)
        trim = label('TRIM: these logical ranges are no longer needed', 25, AMBER).move_to([0, 2.45, 0])
        self.play(FadeIn(trim), FadeOut(mapping), logical.animate.set_opacity(0.4))
        for i in (0, 2):
            self.play(Transform(pages[i], box('INVALID', pages[i].get_center(), AMBER, 2.0)), run_time=0.4)
        self.caption('Host access may vanish before physical erasure.')
        self.wait(5)
        dest = label('valid pages copied elsewhere', 23, GREEN).move_to([0, -2.4, 0])
        self.play(FadeOut(blocklabel), FadeIn(dest), pages[1].animate.shift(DOWN * 1.35).set_opacity(0.55),
                  pages[3].animate.shift(DOWN * 1.35).set_opacity(0.55), run_time=1.2)
        self.caption('Later: garbage collection preserves live data, then erases the block.')
        self.wait(4)
        erased = box('ERASED — ready for reuse', [0, -0.05, 0], DIM, 8.65)
        self.play(FadeOut(pages[0]), FadeOut(pages[2]), FadeIn(erased), run_time=1)
        self.wait(3)
        self.clear_stage()
        lines = VGroup(label('Name gone', 38, BLUE), label('Space available', 38, AMBER),
                       label('Physical contents erased', 38, PURPLE)).arrange(DOWN, buff=0.65)
        self.play(FadeIn(lines))
        self.caption('Three events. No universal recovery window. TRIM is not sanitisation.')
        self.wait(6)
