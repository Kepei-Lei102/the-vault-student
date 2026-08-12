"""Electric Current — the drift-velocity shock.

Beat 1: inside the wire — thermal chaos at ~10^6 m/s, then the tiny drift bias.
Beat 2: the circuit — the field sweeps the loop at near light-speed; every
        electron starts at once; the lamp lights when the news arrives.

Render:  manim -qk electric-current-drift.py ElectricCurrentDrift
House style: bg #1a1a1a, captions #9a9a9a, teal carriers, amber highlights.
Date-seeded (2026-08-07) for the random thermal motion; seed stamped in-frame.
"""

from manim import *
import random

BG = "#1a1a1a"
GRAYT = "#9a9a9a"
TEAL = "#0891b2"
AMBER = "#f59e0b"
BLUE = "#2563eb"

SEED = 20260807
random.seed(SEED)

config.background_color = BG

X_MAX, Y_MAX = 6.0, 1.45
THERMAL_SPEED = 2.8
REAIM_RATE = 10.0


class ElectricCurrentDrift(Scene):
    def swap_caption(self, text, color=GRAYT, font_size=30):
        cap = Text(text, color=color, font_size=font_size, line_spacing=0.9)
        cap.move_to(DOWN * 3.35)
        anims = [FadeIn(cap, run_time=0.4)]
        if getattr(self, "_cap", None) is not None:
            anims.append(FadeOut(self._cap, run_time=0.3))
        self._cap = cap
        self.play(*anims)

    def construct(self):
        seed_tag = Text("seed 20260807", color=GRAYT, font_size=16)
        seed_tag.set_opacity(0.4).to_corner(DR).shift(DOWN * 0.05)
        self.add(seed_tag)
        self.beat_wire()
        self.beat_circuit(seed_tag)

    # ------------------------------------------------------------------
    def beat_wire(self):
        top = Line([-X_MAX, Y_MAX + 0.15, 0], [X_MAX, Y_MAX + 0.15, 0],
                   color=GRAYT, stroke_width=3, stroke_opacity=0.7)
        bot = Line([-X_MAX, -Y_MAX - 0.15, 0], [X_MAX, -Y_MAX - 0.15, 0],
                   color=GRAYT, stroke_width=3, stroke_opacity=0.7)
        title = Text("inside the wire", color=GRAYT, font_size=26)
        title.move_to(UP * 2.3)
        self.play(Create(top), Create(bot), FadeIn(title), run_time=1)

        drift = ValueTracker(0.0)

        def make_jitter(dot):
            def jitter(mob, dt):
                if random.random() < dt * REAIM_RATE:
                    ang = random.uniform(0, TAU)
                    mob.vel = np.array(
                        [np.cos(ang), np.sin(ang), 0]) * THERMAL_SPEED
                p = mob.get_center() + \
                    (mob.vel + np.array([drift.get_value(), 0, 0])) * dt
                if p[0] > X_MAX:
                    p[0] -= 2 * X_MAX
                elif p[0] < -X_MAX:
                    p[0] += 2 * X_MAX
                if abs(p[1]) > Y_MAX:
                    mob.vel[1] *= -1
                    p[1] = np.clip(p[1], -Y_MAX, Y_MAX)
                mob.move_to(p)
            return jitter

        electrons = VGroup()
        for _ in range(34):
            d = Dot(radius=0.06, color=TEAL)
            d.move_to([random.uniform(-X_MAX, X_MAX),
                       random.uniform(-Y_MAX, Y_MAX), 0])
            ang = random.uniform(0, TAU)
            d.vel = np.array([np.cos(ang), np.sin(ang), 0]) * THERMAL_SPEED
            electrons.add(d)

        marked = Dot(radius=0.1, color=AMBER, z_index=3)
        marked.move_to([-2.5, 0.3, 0])
        ang = random.uniform(0, TAU)
        marked.vel = np.array([np.cos(ang), np.sin(ang), 0]) * THERMAL_SPEED

        start_line = DashedLine([-2.5, -Y_MAX, 0], [-2.5, Y_MAX, 0],
                                color=AMBER, stroke_opacity=0.5)
        trail = TracedPath(marked.get_center, stroke_color=AMBER,
                           stroke_width=2.5, stroke_opacity=0.6)

        self.play(FadeIn(electrons), FadeIn(marked), FadeIn(start_line),
                  run_time=0.8)
        self.add(trail)
        for d in electrons:
            d.add_updater(make_jitter(d))
        marked.add_updater(make_jitter(marked))

        self.swap_caption(
            "the free electrons rattle at about a million metres per second\n"
            "in random directions — no net flow")
        self.wait(4)

        self.swap_caption(
            "switch on: the same chaos, plus a whisper of drift to the right")
        self.play(drift.animate.set_value(0.3), run_time=0.5)
        self.wait(8)

        for d in electrons:
            d.clear_updaters()
        marked.clear_updaters()

        end_x = marked.get_center()[0]
        end_line = DashedLine([end_x, -Y_MAX, 0], [end_x, Y_MAX, 0],
                              color=AMBER, stroke_opacity=0.8)
        self.play(Create(end_line), run_time=0.6)
        self.swap_caption(
            "twelve seconds of fury, a few steps of progress —\n"
            "the drift is under a millimetre per second")
        self.wait(3)

        everything = VGroup(top, bot, title, electrons, marked,
                            start_line, end_line, self._cap)
        self.remove(trail)
        self.play(FadeOut(everything), run_time=0.8)
        self._cap = None

    # ------------------------------------------------------------------
    def beat_circuit(self, seed_tag):
        W, H, YC = 9.0, 5.0, 0.2
        x0, y0 = -W / 2, YC - H / 2
        total = 2 * (W + H)

        def perim(s):
            d = (s % 1.0) * total
            if d < W:
                return np.array([x0 + d, y0, 0])
            d -= W
            if d < H:
                return np.array([x0 + W, y0 + d, 0])
            d -= H
            if d < W:
                return np.array([x0 + W - d, y0 + H, 0])
            d -= W
            return np.array([x0, y0 + H - d, 0])

        loop = Rectangle(width=W, height=H, color=GRAYT, stroke_width=3)
        loop.move_to(UP * YC)

        s_batt = (W / 2) / total
        s_lamp = (W + H + W / 2) / total
        sw_x = 2.55
        s_switch = (sw_x + W / 2) / total

        batt_mask = Rectangle(width=0.5, height=0.3, fill_color=BG,
                              fill_opacity=1, stroke_opacity=0)
        batt_mask.move_to(perim(s_batt))
        batt_long = Line(ORIGIN, UP * 0.55, color=GRAYT, stroke_width=3)
        batt_long.move_to(perim(s_batt) + LEFT * 0.12)
        batt_short = Line(ORIGIN, UP * 0.28, color=GRAYT, stroke_width=5)
        batt_short.move_to(perim(s_batt) + RIGHT * 0.12)

        sw_mask = Rectangle(width=0.9, height=0.3, fill_color=BG,
                            fill_opacity=1, stroke_opacity=0)
        sw_mask.move_to([sw_x + 0.375, y0, 0])
        pivot = np.array([sw_x, y0, 0])
        sw_dot = Dot(pivot, radius=0.05, color=GRAYT)
        arm = Line(pivot, pivot + 0.86 * np.array(
            [np.cos(35 * DEGREES), np.sin(35 * DEGREES), 0]),
            color=GRAYT, stroke_width=3)

        lamp_c = perim(s_lamp)
        lamp = Circle(radius=0.42, color=GRAYT, stroke_width=3,
                      fill_color=BG, fill_opacity=1).move_to(lamp_c)
        cross1 = Line(lamp_c + 0.42 * (LEFT * 0.707 + DOWN * 0.707),
                      lamp_c + 0.42 * (RIGHT * 0.707 + UP * 0.707),
                      color=GRAYT, stroke_width=2)
        cross2 = Line(lamp_c + 0.42 * (LEFT * 0.707 + UP * 0.707),
                      lamp_c + 0.42 * (RIGHT * 0.707 + DOWN * 0.707),
                      color=GRAYT, stroke_width=2)
        glow = Circle(radius=0.62, color=AMBER, stroke_width=8,
                      stroke_opacity=0).move_to(lamp_c)

        self.play(Create(loop), run_time=1)
        self.add(batt_mask, sw_mask)
        self.play(FadeIn(batt_long), FadeIn(batt_short), FadeIn(sw_dot),
                  FadeIn(arm), FadeIn(lamp), FadeIn(cross1), FadeIn(cross2),
                  run_time=0.8)
        self.add(glow)

        rate = ValueTracker(0.0)
        masks = [perim(s_batt), pivot + RIGHT * 0.375, lamp_c]

        electrons = VGroup()
        for i in range(26):
            d = Dot(radius=0.07, color=TEAL, z_index=2)
            d.s = (i + random.uniform(-0.2, 0.2)) / 26

            def mover(mob, dt):
                mob.s += rate.get_value() * dt
                p = perim(mob.s)
                mob.move_to(p)
                hidden = any(np.linalg.norm(p - m) < 0.55 for m in masks)
                mob.set_opacity(0 if hidden else 1)
            d.add_updater(mover)
            mover(d, 0)
            electrons.add(d)

        self.play(FadeIn(electrons), run_time=0.8)
        self.swap_caption(
            "a circuit is a pipe already full —\n"
            "packed with free electrons before you touch anything")
        self.wait(2.5)

        self.swap_caption("close the switch")
        self.play(Rotate(arm, angle=-35 * DEGREES, about_point=pivot),
                  run_time=0.5)

        s_pulse = ValueTracker(s_switch)
        pulse = Dot(radius=0.13, color=AMBER, z_index=4)
        pulse.add_updater(lambda m: m.move_to(perim(s_pulse.get_value())))
        halo = TracedPath(pulse.get_center, stroke_color=AMBER,
                          stroke_width=6, stroke_opacity=0.5,
                          dissipating_time=0.3)

        def light_lamp(m):
            lit = np.clip((s_pulse.get_value() - s_lamp) * 12, 0, 1)
            lamp.set_fill(AMBER, opacity=0.85 * lit)
            m.set_stroke(opacity=0.5 * lit)
        glow.add_updater(light_lamp)

        self.add(halo, pulse)
        self.play(s_pulse.animate.set_value(s_switch + 1.0),
                  run_time=1.2, rate_func=linear)
        pulse.clear_updaters()
        self.remove(pulse, halo)
        glow.clear_updaters()
        lamp.set_fill(AMBER, opacity=0.85)
        glow.set_stroke(opacity=0.5)

        rate.set_value(0.011)
        self.swap_caption(
            "the field sweeps the loop at near light-speed —\n"
            "every electron, everywhere, starts drifting at once")
        self.wait(5)

        self.swap_caption(
            "the lamp lights when the news arrives — not the messengers;\n"
            "the messengers themselves would need hours")
        self.wait(3.5)

        for d in electrons:
            d.clear_updaters()
        self.play(*[FadeOut(m) for m in self.mobjects if m is not seed_tag],
                  run_time=1)
