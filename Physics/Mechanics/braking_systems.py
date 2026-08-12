"""Braking Systems — Manim animation for the vault card.

Three scenes in one Scene class:
1. The mechanism — brake fluid → piston → pad clamps rotor → rotor decelerates.
2. Without ABS — slip ratio climbs to 100%, wheel locks, friction collapses
   from μ_s to μ_k, car overshoots its stopping target.
3. With ABS — slip ratio oscillates at the Stribeck peak (~0.15), pad pressure
   pulses, wheel keeps rolling, car stops at the target AND can steer.

Vault palette and helpers inlined per the Manim track convention until we
have 3+ scripts to factor out.

Render:
    manim -qk braking_systems.py BrakingSystems     # 4K final (showcase)
    manim -qh braking_systems.py BrakingSystems     # 1080p review
    manim -qm braking_systems.py BrakingSystems     # 720p iteration
"""
from manim import *
import numpy as np

# ---------- Vault palette (Manim track, dark MP4 background) ----------
BG       = "#1e1e1e"
TXT      = "#cccccc"
TXT_DIM  = "#888888"
BLUE     = "#2563eb"
RED      = "#dc2626"
GREEN    = "#059669"
AMBER    = "#f59e0b"
GREY     = "#888888"
PURPLE   = "#7c3aed"
ORANGE   = "#c86432"

config.background_color = BG


# ---------- Tiny text helpers ----------------------------------------

def title_card(text, color=TXT, size=44):
    return Text(text, color=color, font_size=size, weight=BOLD)


def body(text, color=TXT, size=28):
    return Text(text, color=color, font_size=size)


def small(text, color=TXT_DIM, size=22):
    return Text(text, color=color, font_size=size)


class BrakingSystems(Scene):
    def construct(self):
        self.scene1_mechanism()
        self.scene2_without_abs()
        self.scene3_with_abs()

    # ---------- Scene 1 : the mechanism ------------------------------
    def scene1_mechanism(self):
        title = title_card("Disc brake — how it grips", size=42)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Rotor: outer annulus + inner hub
        rotor_outer = Circle(radius=2.2, color=BLUE, stroke_width=3,
                             fill_color=BLUE, fill_opacity=0.12)
        rotor_inner_ring = Circle(radius=0.85, color=GREY, stroke_width=2,
                                   stroke_opacity=0.6)
        rotor_inner_ring.set_z_index(1)
        hub = Circle(radius=0.6, color=GREY, stroke_width=2,
                     fill_color=GREY, fill_opacity=0.20)
        hub.set_z_index(2)
        # 5 lug-bolt dots inside hub
        lugs = VGroup(*[
            Dot([0.34 * np.cos(a), 0.34 * np.sin(a), 0], radius=0.05,
                color=GREY)
            for a in np.linspace(0, 2 * np.pi, 5, endpoint=False)
        ])
        lugs.set_z_index(3)
        rotor_group = VGroup(rotor_outer, rotor_inner_ring, hub, lugs)
        rotor_group.shift(DOWN * 0.3)

        # A radial reference line inside the rotor so rotation is visible
        ref_line = Line(rotor_inner_ring.get_center(),
                        rotor_inner_ring.get_center() + UP * 2.0,
                        color=AMBER, stroke_width=3)
        ref_line.set_z_index(0)

        # Caliper: U-shape bracket at the top of the rotor
        cal_w = 1.6; cal_h = 1.4; cal_thick = 0.20
        cal_y_bottom = rotor_outer.get_top()[1] - 0.30  # caliper straddles rotor edge
        cal_x_left = -cal_w / 2
        cal_left = Rectangle(width=cal_thick, height=cal_h,
                             color=BLUE, stroke_width=2,
                             fill_color=BLUE, fill_opacity=0.20)
        cal_left.move_to([cal_x_left, cal_y_bottom + cal_h / 2, 0])
        cal_right = cal_left.copy().shift(RIGHT * (cal_w - cal_thick))
        cal_top = Rectangle(width=cal_w, height=cal_thick,
                            color=BLUE, stroke_width=2,
                            fill_color=BLUE, fill_opacity=0.20)
        cal_top.move_to([0, cal_y_bottom + cal_h - cal_thick / 2, 0])
        caliper = VGroup(cal_left, cal_right, cal_top)

        # Pad — orange bar at the bottom of the caliper, just above the rotor
        pad_w = 1.2; pad_h = 0.18
        pad_y_start = cal_y_bottom + 0.30   # initially OPEN (not touching rotor)
        pad = Rectangle(width=pad_w, height=pad_h,
                        color=AMBER, stroke_width=2,
                        fill_color=AMBER, fill_opacity=0.55)
        pad.move_to([0, pad_y_start, 0])

        # Piston — orange-tertiary rectangle above the pad
        piston = Rectangle(width=0.5, height=0.55,
                           color=ORANGE, stroke_width=2,
                           fill_color=ORANGE, fill_opacity=0.40)
        piston.move_to([0, pad_y_start + 0.40, 0])

        # Brake-fluid arrow from above
        fluid_arrow = Arrow(start=[0, cal_y_bottom + cal_h + 1.1, 0],
                            end=[0, cal_y_bottom + cal_h + 0.15, 0],
                            color=ORANGE, stroke_width=6,
                            max_tip_length_to_length_ratio=0.18)
        fluid_label = small("brake fluid", color=ORANGE).next_to(
            fluid_arrow, RIGHT, buff=0.2)

        # Labels
        rotor_label = body("rotor", color=BLUE, size=24).next_to(
            rotor_group, RIGHT, buff=0.3).shift(DOWN * 0.5)
        cal_label = small("caliper", color=BLUE).next_to(
            caliper, LEFT, buff=0.25)
        pad_label = small("pad", color=AMBER).move_to(
            pad.get_center() + LEFT * 1.15)
        piston_label = small("piston", color=ORANGE).next_to(
            piston, RIGHT, buff=0.25)

        # Reveal the mechanism progressively
        self.play(FadeIn(rotor_group), FadeIn(rotor_label), run_time=1.0)
        self.play(FadeIn(ref_line), run_time=0.4)

        # Start the rotor spinning (will run continuously via an updater)
        rotor_rate = ValueTracker(2.0)   # rad/s, will tween down later
        def spin_ref(mob, dt):
            mob.rotate(rotor_rate.get_value() * dt,
                       about_point=rotor_inner_ring.get_center())
        ref_line.add_updater(spin_ref)
        self.wait(1.5)   # let the student see it spinning

        self.play(FadeIn(caliper), FadeIn(cal_label), run_time=0.8)
        self.play(FadeIn(pad), FadeIn(pad_label),
                  FadeIn(piston), FadeIn(piston_label), run_time=0.8)
        self.play(FadeIn(fluid_arrow), FadeIn(fluid_label), run_time=0.6)
        self.wait(0.8)

        # Caption: fluid → piston → pad
        cap1 = body("Brake fluid pressure → piston pushes pad onto rotor",
                    size=26).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(cap1), run_time=0.6)

        # Animate: pad clamps down (moves down), piston shifts down, fluid pulses
        clamp_dist = 0.30
        self.play(
            pad.animate.shift(DOWN * clamp_dist),
            piston.animate.shift(DOWN * clamp_dist),
            fluid_arrow.animate.set_color(RED),
            run_time=1.2,
        )

        # Friction torque arrow shows up tangent to the rotor at the pad
        fr_arrow = Arrow(
            start=[0.55, rotor_outer.get_top()[1] - 0.05, 0],
            end=[-0.55, rotor_outer.get_top()[1] - 0.05, 0],
            color=RED, stroke_width=6,
            max_tip_length_to_length_ratio=0.18,
        )
        fr_label = small("F_friction (torque)", color=RED).next_to(
            fr_arrow, DOWN, buff=0.15)
        self.play(FadeIn(fr_arrow), FadeIn(fr_label), run_time=0.6)

        # Rotor decelerates visibly
        self.play(rotor_rate.animate.set_value(0.4), run_time=2.5)
        self.wait(0.8)

        cap2 = body("Friction torque opposes wheel rotation → wheel decelerates",
                    size=26).to_edge(DOWN, buff=0.7)
        self.play(ReplacementTransform(cap1, cap2), run_time=0.6)
        self.wait(1.5)

        # Clean up
        ref_line.clear_updaters()
        self.play(
            FadeOut(rotor_group), FadeOut(ref_line),
            FadeOut(caliper), FadeOut(pad), FadeOut(piston),
            FadeOut(fluid_arrow), FadeOut(fluid_label),
            FadeOut(rotor_label), FadeOut(cal_label),
            FadeOut(pad_label), FadeOut(piston_label),
            FadeOut(fr_arrow), FadeOut(fr_label),
            FadeOut(cap2), FadeOut(title),
            run_time=0.8,
        )

    # ---------- Scene 2 : without ABS — lock + slide ------------------
    def scene2_without_abs(self):
        title = title_card("Without ABS — wheel locks, friction collapses",
                           size=36, color=RED)
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title))

        # Road line across the screen
        road = Line([-6.5, -2.6, 0], [6.5, -2.6, 0],
                    color=GREY, stroke_width=2)
        self.add(road)

        # Stopping target — vertical dashed line on the right
        target = DashedLine([3.5, -2.95, 0], [3.5, -1.6, 0],
                            color=GREEN, stroke_width=3, dash_length=0.12)
        target_lbl = small("target", color=GREEN).next_to(target, UP, buff=0.05)
        self.play(FadeIn(target), FadeIn(target_lbl), run_time=0.4)

        # Car — rectangle body + two wheels
        car_body = Rectangle(width=1.8, height=0.6, color=BLUE,
                             stroke_width=2,
                             fill_color=BLUE, fill_opacity=0.25)
        car_body.move_to([-5.0, -1.95, 0])
        wheel_l = Circle(radius=0.25, color=AMBER, stroke_width=2,
                         fill_color=AMBER, fill_opacity=0.30)
        wheel_l.move_to(car_body.get_center() + LEFT * 0.55 + DOWN * 0.45)
        wheel_r = wheel_l.copy().shift(RIGHT * 1.10)
        # Radial line inside each wheel so rotation is visible
        wmark_l = Line(wheel_l.get_center(),
                       wheel_l.get_center() + UP * 0.22,
                       color=RED, stroke_width=3)
        wmark_r = Line(wheel_r.get_center(),
                       wheel_r.get_center() + UP * 0.22,
                       color=RED, stroke_width=3)
        car = VGroup(car_body, wheel_l, wheel_r, wmark_l, wmark_r)

        # Slip-ratio gauge on the left (vertical bar)
        gauge_x = -5.8
        gauge_y = 0.5
        gauge_h = 2.2
        gauge_w = 0.45
        gauge_bg = Rectangle(width=gauge_w, height=gauge_h,
                             color=GREY, stroke_width=2,
                             fill_color=GREY, fill_opacity=0.10)
        gauge_bg.move_to([gauge_x, gauge_y, 0])
        gauge_fill = Rectangle(width=gauge_w - 0.04, height=0.05,
                               color=RED, stroke_width=0,
                               fill_color=RED, fill_opacity=0.75)
        gauge_fill.move_to([gauge_x, gauge_y - gauge_h/2 + 0.025, 0])

        gauge_top_lbl = small("100%\n(locked)", color=RED).next_to(
            gauge_bg, UP, buff=0.15)
        gauge_bot_lbl = small("0%\n(rolling)", color=GREEN).next_to(
            gauge_bg, DOWN, buff=0.15)
        gauge_title = small("slip ratio",
                            color=TXT).next_to(gauge_bg, LEFT, buff=0.15)

        # Friction-force arrow on car (backward)
        fr_arrow = Arrow(
            start=car.get_left() + RIGHT * 0.0,
            end=car.get_left() + LEFT * 1.0,
            color=GREEN, stroke_width=5,
            max_tip_length_to_length_ratio=0.20,
        )
        fr_lbl = small("F_friction ≈ μ_s N", color=GREEN).next_to(
            fr_arrow, UP, buff=0.10)

        self.play(FadeIn(car), run_time=0.6)
        self.play(FadeIn(gauge_bg), FadeIn(gauge_fill),
                  FadeIn(gauge_top_lbl), FadeIn(gauge_bot_lbl),
                  FadeIn(gauge_title), run_time=0.6)
        self.play(FadeIn(fr_arrow), FadeIn(fr_lbl), run_time=0.4)

        # Rolling-into-frame animation: car moves right, wheels rotate
        car_x = ValueTracker(-5.0)
        slip = ValueTracker(0.0)   # 0 = rolling, 1 = locked

        # Wheel spin: angular velocity scales with (1 - slip) * forward speed
        # We'll just rotate the wheel marks via an updater each frame.
        prev_x = [-5.0]
        def update_wheels(mob, dt):
            x = car_x.get_value()
            dx = x - prev_x[0]
            prev_x[0] = x
            r = 0.25
            s = slip.get_value()
            # Wheel rotation = (1 - slip) * dx / r  (negative because rolling forward)
            d_theta = -(1 - s) * dx / r
            for wm, wc in [(wmark_l, wheel_l), (wmark_r, wheel_r)]:
                wm.rotate(d_theta, about_point=wc.get_center())

        # Whole-car position updater
        def update_car(mob, dt):
            x = car_x.get_value()
            # Move car as a whole to keep all parts together
            for part, offset in [
                (car_body, LEFT * 0.0),
                (wheel_l, LEFT * 0.55 + DOWN * 0.45),
                (wheel_r, RIGHT * 0.55 + DOWN * 0.45),
                (wmark_l, LEFT * 0.55 + DOWN * 0.45),
                (wmark_r, RIGHT * 0.55 + DOWN * 0.45),
            ]:
                # car_body anchor
                pass
            shift_to = np.array([x, car_body.get_center()[1], 0])
            current = car_body.get_center()
            delta = shift_to - current
            car_body.shift(delta)
            wheel_l.shift(delta)
            wheel_r.shift(delta)
            wmark_l.shift(delta)
            wmark_r.shift(delta)

        car_body.add_updater(update_car)
        wheel_l.add_updater(update_wheels)   # piggyback the wheel-spin update

        # Update fr_arrow position to track car
        def update_fr(mob, dt):
            new_start = car_body.get_left() + RIGHT * 0.0
            new_end = new_start + LEFT * fr_arrow_len[0]
            mob.put_start_and_end_on(new_end, new_start)
        fr_arrow_len = [1.0]
        fr_arrow.add_updater(update_fr)
        fr_lbl.add_updater(lambda m, dt: m.next_to(fr_arrow, UP, buff=0.10))

        # Update gauge fill height. Use a threshold-based colour pick (not
        # interpolate_color) so we avoid having to wrap hex strings in
        # ManimColor each frame — same visual gist (green→amber→red as slip
        # climbs) with simpler call surface.
        def update_gauge(mob, dt):
            s = slip.get_value()
            h_max = gauge_h - 0.10
            new_h = 0.05 + s * h_max
            if s < 0.30:
                col = GREEN
            elif s < 0.70:
                col = AMBER
            else:
                col = RED
            new_rect = Rectangle(width=gauge_w - 0.04, height=new_h,
                                 color=col, stroke_width=0,
                                 fill_color=col, fill_opacity=0.75)
            new_rect.move_to([gauge_x,
                              gauge_y - gauge_h/2 + new_h/2 + 0.025, 0])
            mob.become(new_rect)
        gauge_fill.add_updater(update_gauge)

        # Caption
        cap = body("Driver brakes hard — slip ratio climbs", size=24)
        cap.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(cap), run_time=0.4)

        # Phase A : roll forward a bit, slip ratio still ~0 (good braking)
        self.play(car_x.animate.set_value(-2.5),
                  slip.animate.set_value(0.12),
                  run_time=2.0, rate_func=linear)

        # Phase B : wheels lock — slip jumps to ~1.0; friction arrow shrinks
        cap2 = body("Wheels lock → friction drops from μ_s to μ_k",
                    size=24, color=RED).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(cap, cap2), run_time=0.4)
        fr_arrow_len[0] = 0.55       # friction arrow gets shorter
        fr_lbl_new = small("F_friction ≈ μ_k N  (smaller)", color=RED)
        fr_lbl_new.next_to(fr_arrow, UP, buff=0.10)
        self.play(slip.animate.set_value(0.97), run_time=1.0)
        self.play(Transform(fr_lbl, fr_lbl_new), run_time=0.4)

        # Phase C : car slides past the target (because friction is now smaller)
        self.play(car_x.animate.set_value(4.6),
                  run_time=2.6, rate_func=rate_functions.ease_out_sine)

        # Caption update: missed the target
        cap3 = body("→ Longer stop. No steering authority.",
                    size=26, color=RED).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(cap2, cap3), run_time=0.5)
        # Red cross over target to emphasise miss
        miss_x1 = Line([3.5 - 0.18, -0.95 - 0.18, 0],
                       [3.5 + 0.18, -0.95 + 0.18, 0],
                       color=RED, stroke_width=4)
        miss_x2 = Line([3.5 - 0.18, -0.95 + 0.18, 0],
                       [3.5 + 0.18, -0.95 - 0.18, 0],
                       color=RED, stroke_width=4)
        self.play(FadeIn(miss_x1), FadeIn(miss_x2), run_time=0.4)
        self.wait(1.4)

        # Clean up
        car_body.clear_updaters()
        wheel_l.clear_updaters()
        fr_arrow.clear_updaters()
        fr_lbl.clear_updaters()
        gauge_fill.clear_updaters()
        self.play(
            FadeOut(car), FadeOut(road), FadeOut(target), FadeOut(target_lbl),
            FadeOut(gauge_bg), FadeOut(gauge_fill),
            FadeOut(gauge_top_lbl), FadeOut(gauge_bot_lbl),
            FadeOut(gauge_title),
            FadeOut(fr_arrow), FadeOut(fr_lbl),
            FadeOut(cap3), FadeOut(title),
            FadeOut(miss_x1), FadeOut(miss_x2),
            run_time=0.7,
        )

    # ---------- Scene 3 : with ABS — live at the Stribeck peak --------
    def scene3_with_abs(self):
        title = title_card("With ABS — slip held at the Stribeck peak",
                           size=36, color=GREEN)
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title))

        # Same scene: road, target, car
        road = Line([-6.5, -2.6, 0], [6.5, -2.6, 0],
                    color=GREY, stroke_width=2)
        self.add(road)
        target = DashedLine([3.5, -2.95, 0], [3.5, -1.6, 0],
                            color=GREEN, stroke_width=3, dash_length=0.12)
        target_lbl = small("target", color=GREEN).next_to(target, UP, buff=0.05)
        self.play(FadeIn(target), FadeIn(target_lbl), run_time=0.4)

        car_body = Rectangle(width=1.8, height=0.6, color=BLUE,
                             stroke_width=2,
                             fill_color=BLUE, fill_opacity=0.25)
        car_body.move_to([-5.0, -1.95, 0])
        wheel_l = Circle(radius=0.25, color=AMBER, stroke_width=2,
                         fill_color=AMBER, fill_opacity=0.30)
        wheel_l.move_to(car_body.get_center() + LEFT * 0.55 + DOWN * 0.45)
        wheel_r = wheel_l.copy().shift(RIGHT * 1.10)
        wmark_l = Line(wheel_l.get_center(),
                       wheel_l.get_center() + UP * 0.22,
                       color=RED, stroke_width=3)
        wmark_r = Line(wheel_r.get_center(),
                       wheel_r.get_center() + UP * 0.22,
                       color=RED, stroke_width=3)
        car = VGroup(car_body, wheel_l, wheel_r, wmark_l, wmark_r)
        self.play(FadeIn(car), run_time=0.5)

        # Slip-ratio gauge with PEAK band highlighted
        gauge_x = -5.8
        gauge_y = 0.5
        gauge_h = 2.2
        gauge_w = 0.45
        gauge_bg = Rectangle(width=gauge_w, height=gauge_h,
                             color=GREY, stroke_width=2,
                             fill_color=GREY, fill_opacity=0.10)
        gauge_bg.move_to([gauge_x, gauge_y, 0])
        # Highlight band for 8-22% (the ABS target window)
        band_lo_h = 0.08 * (gauge_h - 0.10)
        band_hi_h = 0.22 * (gauge_h - 0.10)
        band_y_lo = gauge_y - gauge_h/2 + 0.05 + band_lo_h
        band_y_hi = gauge_y - gauge_h/2 + 0.05 + band_hi_h
        band = Rectangle(width=gauge_w - 0.04, height=band_hi_h - band_lo_h,
                         color=GREEN, stroke_width=0,
                         fill_color=GREEN, fill_opacity=0.30)
        band.move_to([gauge_x, (band_y_lo + band_y_hi) / 2, 0])

        slip_val = ValueTracker(0.0)
        gauge_fill = Rectangle(width=gauge_w - 0.04, height=0.05,
                               color=GREEN, stroke_width=0,
                               fill_color=GREEN, fill_opacity=0.75)
        gauge_fill.move_to([gauge_x, gauge_y - gauge_h/2 + 0.025, 0])

        gauge_top_lbl = small("100%", color=RED).next_to(
            gauge_bg, UP, buff=0.15)
        gauge_bot_lbl = small("0%", color=GREEN).next_to(
            gauge_bg, DOWN, buff=0.15)
        gauge_title = small("slip ratio",
                            color=TXT).next_to(gauge_bg, LEFT, buff=0.15)
        peak_lbl = small("Stribeck\npeak",
                         color=GREEN, size=18).next_to(band, RIGHT, buff=0.15)

        self.play(FadeIn(gauge_bg), FadeIn(band), FadeIn(gauge_fill),
                  FadeIn(gauge_top_lbl), FadeIn(gauge_bot_lbl),
                  FadeIn(gauge_title), FadeIn(peak_lbl), run_time=0.6)

        # Friction arrow stays at full μ_s magnitude
        fr_arrow_len = [1.05]
        fr_arrow = Arrow(
            start=car_body.get_left(),
            end=car_body.get_left() + LEFT * fr_arrow_len[0],
            color=GREEN, stroke_width=5,
            max_tip_length_to_length_ratio=0.20,
        )
        fr_lbl = small("F_friction ≈ μ_s N  (at peak)", color=GREEN)
        fr_lbl.next_to(fr_arrow, UP, buff=0.10)
        self.play(FadeIn(fr_arrow), FadeIn(fr_lbl), run_time=0.4)

        # Car-position tracker + wheel-spin updater (slip-aware)
        car_x = ValueTracker(-5.0)
        prev_x = [-5.0]
        def update_wheels(mob, dt):
            x = car_x.get_value()
            dx = x - prev_x[0]
            prev_x[0] = x
            r = 0.25
            s = slip_val.get_value()
            d_theta = -(1 - s) * dx / r
            for wm, wc in [(wmark_l, wheel_l), (wmark_r, wheel_r)]:
                wm.rotate(d_theta, about_point=wc.get_center())

        def update_car(mob, dt):
            x = car_x.get_value()
            shift_to = np.array([x, car_body.get_center()[1], 0])
            delta = shift_to - car_body.get_center()
            car_body.shift(delta)
            wheel_l.shift(delta); wheel_r.shift(delta)
            wmark_l.shift(delta); wmark_r.shift(delta)
        car_body.add_updater(update_car)
        wheel_l.add_updater(update_wheels)
        fr_arrow.add_updater(lambda m, dt: m.put_start_and_end_on(
            car_body.get_left() + LEFT * fr_arrow_len[0],
            car_body.get_left()))
        fr_lbl.add_updater(lambda m, dt: m.next_to(fr_arrow, UP, buff=0.10))

        # Gauge fill updater (oscillates around the green band)
        def update_gauge(mob, dt):
            s = slip_val.get_value()
            h_max = gauge_h - 0.10
            new_h = 0.05 + s * h_max
            # Colour green if inside band, amber if straying high
            color = GREEN if 0.07 <= s <= 0.23 else AMBER
            new_rect = Rectangle(width=gauge_w - 0.04, height=new_h,
                                 color=color, stroke_width=0,
                                 fill_color=color, fill_opacity=0.75)
            new_rect.move_to([gauge_x,
                              gauge_y - gauge_h/2 + new_h/2 + 0.025, 0])
            mob.become(new_rect)
        gauge_fill.add_updater(update_gauge)

        # Pulse-pressure indicator: small circle near the wheel that
        # blinks AMBER (release) / GREEN (clamp) at ~5 Hz
        pulse_dot = Dot(wheel_l.get_center() + UP * 0.55, radius=0.10,
                        color=GREEN)
        pulse_dot.add_updater(lambda m, dt: m.move_to(
            wheel_l.get_center() + UP * 0.55))
        pulse_lbl = small("pad pressure", color=TXT_DIM, size=18)
        pulse_lbl.add_updater(lambda m, dt: m.next_to(pulse_dot, UP, buff=0.10))
        self.play(FadeIn(pulse_dot), FadeIn(pulse_lbl), run_time=0.4)

        cap = body("ABS pulses pressure 5–20× per second — slip stays at peak",
                   size=22).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(cap), run_time=0.4)

        # Make the slip ratio oscillate around 0.15 with small wiggle
        # Implementation: use ValueTracker + a time-driven updater on slip_val.
        # Simpler — drive it through 3 sub-animations of varying value while
        # also progressing the car position.

        # Phase A : initial rise to peak
        self.play(slip_val.animate.set_value(0.15),
                  car_x.animate.set_value(-3.8),
                  run_time=1.2)

        # Phase B : oscillate around the peak while the car decelerates
        for s_low, s_high, x_target in [
            (0.10, 0.22, -2.5),
            (0.11, 0.19, -1.2),
            (0.10, 0.21, 0.2),
            (0.12, 0.18, 1.4),
            (0.11, 0.20, 2.5),
            (0.13, 0.17, 3.5),
        ]:
            self.play(slip_val.animate.set_value(s_high),
                      pulse_dot.animate.set_color(AMBER),
                      car_x.animate.set_value(
                          car_x.get_value() + (x_target - car_x.get_value()) * 0.5),
                      run_time=0.35)
            self.play(slip_val.animate.set_value(s_low),
                      pulse_dot.animate.set_color(GREEN),
                      car_x.animate.set_value(x_target),
                      run_time=0.35)

        # Phase C : final settling — slip goes to 0 as car stops
        self.play(slip_val.animate.set_value(0.0),
                  pulse_dot.animate.set_color(GREEN),
                  car_x.animate.set_value(3.5),
                  run_time=0.8)

        # Caption update — stopped at the target with wheel still rolling
        cap2 = body("→ Car stops at the target. Wheel never locked.",
                    size=24, color=GREEN).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(cap, cap2), run_time=0.5)

        # Tick the target line
        tick = Text("✓", color=GREEN, font_size=46).move_to(
            [3.5, -0.95, 0])
        self.play(FadeIn(tick), run_time=0.4)
        self.wait(2.0)

        # Final beat — bay-synthesis line
        car_body.clear_updaters()
        wheel_l.clear_updaters()
        fr_arrow.clear_updaters()
        fr_lbl.clear_updaters()
        gauge_fill.clear_updaters()
        pulse_dot.clear_updaters()
        pulse_lbl.clear_updaters()

        closer = body(
            "Same tire-road friction limit — different control strategy.",
            size=26, color=AMBER,
        ).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(cap2, closer), run_time=0.6)
        self.wait(2.2)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
