"""Pressure grows with depth; upthrust is the difference; floating is the balance.

Scene 1  PressureAndUpthrust : a tank; pressure arrows lengthen with depth; a block is
                               lowered in, the side pushes cancel, the bottom push beats
                               the top push; released, it rises and settles at the level
                               where the displaced water weighs what it does.
Scene 2  SteelShip            : the same steel as a cube (sinks) and as a hull (floats).

Render:  manim -qk density-pressure-manim.py PressureAndUpthrust SteelShip
"""
from manim import *
import math

BLUE, AMBER, GREEN, GREY, RED, PURPLE = "#2563eb", "#f59e0b", "#059669", "#888888", "#dc2626", "#7c3aed"
config.background_color = "#1e1e1e"

class PressureAndUpthrust(Scene):
    def construct(self):
        tank = Rectangle(width=6.0, height=5.0, stroke_color=GREY, stroke_width=3).shift(LEFT * 3 + DOWN * 0.3)
        water = Rectangle(width=6.0, height=4.4, fill_color=BLUE, fill_opacity=0.18, stroke_width=0).move_to(tank.get_bottom(), aligned_edge=DOWN)
        surface_y = water.get_top()[1]; bottom_y = water.get_bottom()[1]
        caption = Text("water: pressure comes from the weight of what is above", font_size=24, color=GREY).to_edge(DOWN, buff=0.3)
        self.add(tank, water, caption)
        # pressure arrows at three depths, pointing in all four directions, growing with depth
        arrows = VGroup()
        for depth in (0.6, 1.9, 3.4):
            y = surface_y - depth; L = 0.15 + 0.32 * depth
            c = np.array([-3.0, y, 0])
            for d in (LEFT, RIGHT, UP, DOWN):
                arrows.add(Arrow(c, c + d * L, buff=0, color=PURPLE, stroke_width=4, max_tip_length_to_length_ratio=0.3))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.05), run_time=2.5)
        lab = Text("equal in every direction; larger the deeper you go", font_size=22, color=PURPLE).next_to(tank, RIGHT, buff=0.4).shift(UP * 1.5)
        self.play(FadeIn(lab)); self.wait(1.5)
        self.play(FadeOut(arrows), FadeOut(lab))
        # block lowered in
        block = Square(side_length=1.2, fill_color=AMBER, fill_opacity=0.5, stroke_color=AMBER, stroke_width=2).move_to([-3.0, surface_y + 1.6, 0])
        self.play(Transform(caption, Text("lower a block in: the water pushes on every face", font_size=24, color=GREY).to_edge(DOWN, buff=0.3)))
        self.play(FadeIn(block)); self.play(block.animate.move_to([-3.0, surface_y - 2.0, 0]), run_time=2)
        top_d = surface_y - block.get_top()[1]; bot_d = surface_y - block.get_bottom()[1]
        k = 0.45
        top_arrows = VGroup(*[Arrow(block.get_top() + RIGHT * x + UP * 0.02, block.get_top() + RIGHT * x + DOWN * k * top_d, buff=0, color=PURPLE, stroke_width=4, max_tip_length_to_length_ratio=0.3) for x in (-0.35, 0, 0.35)])
        bot_arrows = VGroup(*[Arrow(block.get_bottom() + RIGHT * x + DOWN * 0.02, block.get_bottom() + RIGHT * x + UP * k * bot_d, buff=0, color=GREEN, stroke_width=4, max_tip_length_to_length_ratio=0.3) for x in (-0.35, 0, 0.35)])
        side_arrows = VGroup(*[Arrow(block.get_left() + UP * y, block.get_left() + UP * y + RIGHT * k * (top_d + 0.6 + y * -1), buff=0, color=GREY, stroke_width=3, max_tip_length_to_length_ratio=0.3) for y in (0.35, 0, -0.35)] +
                             [Arrow(block.get_right() + UP * y, block.get_right() + UP * y + LEFT * k * (top_d + 0.6 + y * -1), buff=0, color=GREY, stroke_width=3, max_tip_length_to_length_ratio=0.3) for y in (0.35, 0, -0.35)])
        # side arrows start outside, point inward: rebuild so they start away from the block
        side_arrows = VGroup()
        for y in (0.35, 0, -0.35):
            L = k * (top_d + 0.6 - y)
            side_arrows.add(Arrow(block.get_left() + UP * y + LEFT * L, block.get_left() + UP * y, buff=0, color=GREY, stroke_width=3, max_tip_length_to_length_ratio=0.3))
            side_arrows.add(Arrow(block.get_right() + UP * y + RIGHT * L, block.get_right() + UP * y, buff=0, color=GREY, stroke_width=3, max_tip_length_to_length_ratio=0.3))
        # top arrows should start above the block and point down onto it
        top_arrows = VGroup(*[Arrow(block.get_top() + RIGHT * x + UP * k * top_d, block.get_top() + RIGHT * x, buff=0, color=PURPLE, stroke_width=4, max_tip_length_to_length_ratio=0.3) for x in (-0.35, 0, 0.35)])
        bot_arrows = VGroup(*[Arrow(block.get_bottom() + RIGHT * x + DOWN * k * bot_d, block.get_bottom() + RIGHT * x, buff=0, color=GREEN, stroke_width=4, max_tip_length_to_length_ratio=0.3) for x in (-0.35, 0, 0.35)])
        self.play(LaggedStart(*[GrowArrow(a) for a in side_arrows], lag_ratio=0.1), run_time=1.2)
        t1 = Text("sides: equal and opposite, cancel", font_size=22, color=GREY).next_to(tank, RIGHT, buff=0.4).shift(UP * 1.8)
        self.play(FadeIn(t1)); self.wait(0.8)
        self.play(LaggedStart(*[GrowArrow(a) for a in top_arrows], lag_ratio=0.1), run_time=0.8)
        t2 = Text("top: pushed down by ρ g h₁ A", font_size=22, color=PURPLE).next_to(t1, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(t2)); self.wait(0.6)
        self.play(LaggedStart(*[GrowArrow(a) for a in bot_arrows], lag_ratio=0.1), run_time=0.8)
        t3 = Text("bottom: pushed up by ρ g h₂ A\n— deeper, so bigger", font_size=22, color=GREEN, line_spacing=0.9).next_to(t2, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(t3)); self.wait(1.2)
        self.play(FadeOut(side_arrows), FadeOut(top_arrows), FadeOut(bot_arrows))
        up = Arrow(block.get_center(), block.get_center() + UP * 1.6, buff=0, color=GREEN, stroke_width=8, max_tip_length_to_length_ratio=0.25)
        w = Arrow(block.get_center(), block.get_center() + DOWN * 1.0, buff=0, color=RED, stroke_width=8, max_tip_length_to_length_ratio=0.25)
        t4 = Text("the difference is the upthrust:\nρ g (h₂ − h₁) A = ρ g V", font_size=22, color=GREEN, line_spacing=0.9).next_to(t3, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(GrowArrow(up), GrowArrow(w), FadeIn(t4)); self.wait(1.5)
        # release: block rises and settles with 62 % submerged (rho_block = 0.62 rho_water)
        self.play(Transform(caption, Text("released: upthrust beats weight, the block rises until the water it displaces weighs what it does", font_size=22, color=GREY).to_edge(DOWN, buff=0.3)))
        self.play(FadeOut(t1), FadeOut(t2), FadeOut(t3), FadeOut(t4))
        frac = 0.62; target_y = surface_y - frac * 1.2 + 0.6
        def upd(m, alpha):
            y = interpolate(surface_y - 2.0, target_y, smooth(alpha)); block.move_to([-3.0, y, 0])
            sub = max(0.0, min(1.2, surface_y - block.get_bottom()[1]))
            up.put_start_and_end_on(block.get_center(), block.get_center() + UP * 1.6 * sub / 1.2 + UP * 0.001)
            w.put_start_and_end_on(block.get_center(), block.get_center() + DOWN * 1.0)
        self.play(UpdateFromAlphaFunc(block, upd), run_time=3)
        t5 = Text("62 % of it is under:\nits density is 0.62 of the water's", font_size=22, color=AMBER, line_spacing=0.9).next_to(tank, RIGHT, buff=0.4).shift(UP * 1.2)
        t6 = Text("an ice cube shows 8 %;\na person, lungs full, about 2 %", font_size=22, color=GREY, line_spacing=0.9).next_to(t5, DOWN, aligned_edge=LEFT, buff=0.35)
        self.play(FadeIn(t5)); self.play(FadeIn(t6)); self.wait(2.5)


class SteelShip(Scene):
    def construct(self):
        tank = Rectangle(width=12.0, height=4.2, stroke_color=GREY, stroke_width=3).shift(DOWN * 0.9)
        water = Rectangle(width=12.0, height=3.3, fill_color=BLUE, fill_opacity=0.18, stroke_width=0).move_to(tank.get_bottom(), aligned_edge=DOWN)
        surface_y = water.get_top()[1]
        caption = Text("the same 110 kg of steel, twice", font_size=24, color=GREY).to_edge(DOWN, buff=0.3)
        self.add(tank, water, caption)
        cube = Square(side_length=0.7, fill_color=GREY, fill_opacity=0.9, stroke_width=0).move_to([-3.5, surface_y + 1.2, 0])
        lab1 = Text("as a cube: 0.014 m³, 7900 kg/m³", font_size=22, color=GREY).to_edge(UP, buff=0.25).to_edge(LEFT, buff=0.6)
        self.play(FadeIn(cube), FadeIn(lab1))
        self.play(cube.animate.move_to([-3.5, tank.get_bottom()[1] + 0.35, 0]), run_time=2.0, rate_func=rush_into)
        s1 = Text("sinks: displaces only 0.014 m³ of water,\n14 kg of it", font_size=20, color=RED, line_spacing=0.9).next_to(lab1, DOWN, buff=0.15, aligned_edge=LEFT)
        self.play(FadeIn(s1)); self.wait(1.2)
        # hull: an open box of the same steel, much bigger volume
        hull = VMobject(stroke_color=GREY, stroke_width=10).set_points_as_corners([[2.2, 1.2, 0], [2.4, -0.3, 0], [4.6, -0.3, 0], [4.8, 1.2, 0]]).shift(UP * 0.9)
        lab2 = Text("as a hull: steel plus the air it encloses, 0.23 m³", font_size=22, color=GREY).to_edge(UP, buff=0.25).to_edge(RIGHT, buff=0.6)
        self.play(FadeIn(hull), FadeIn(lab2))
        self.play(hull.animate.shift(DOWN * (0.9 + 0.55 + 0.5)), run_time=2.5, rate_func=smooth)
        s2 = Text("floats: displaces 110 kg of water;\naverage density 480 kg/m³", font_size=20, color=GREEN, line_spacing=0.9).next_to(lab2, DOWN, buff=0.15, aligned_edge=LEFT)
        self.play(FadeIn(s2)); self.wait(1.0)
        self.play(Transform(caption, Text("what floats is not the material but the average density of the whole shape, air included", font_size=22, color=GREY).to_edge(DOWN, buff=0.3)))
        self.wait(2.5)
