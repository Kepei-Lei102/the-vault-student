# stack: Manim Community v0.20.1
#
# Resistance, in three beats:
#   1. a cool lattice      — the electron accelerates, crashes, accelerates
#   2. a white-hot lattice — same field, crashes come far sooner, drift collapses
#   3. a perfect lattice   — nothing to scatter from, and R has nothing to be
#
# The controlled variable is the field: the ramp slope is identical in all three
# beats, and every beat runs for the same length of animation time. So how far
# the electron gets across the arena IS the resistance, with no readout needed.
#
# Render:  manim -qk resistance-lattice.py ResistanceLattice
# then:    cp media/videos/resistance-lattice/2160p60/ResistanceLattice.mp4 \
#             resistance-lattice.mp4
#          (the committed file is that render re-encoded at -crf 26 — visually
#           identical at 4K, about 60% of the size)

from manim import *
import numpy as np

# ---------- Vault palette (Manim track, dark MP4 background) ----------
BG = "#1e1e1e"
TXT = "#cccccc"
TXT_DIM = "#888888"
BLUE = "#2563eb"
RED = "#dc2626"
GREEN = "#059669"
AMBER = "#f59e0b"
GREY = "#888888"
PURPLE = "#7c3aed"
TRACE = "#60a5fa"        # BLUE lifted for the dark background
ELECTRON = AMBER

config.background_color = BG

# ---------- arena geometry ----------
ARENA_L, ARENA_R = -6.35, 6.35
LANE = 1.62                       # the row-gap the electron runs along
ROWS = [0.72, 1.32, 1.92, 2.52]
COL_STEP = 0.635
START_X = ARENA_L + 0.30
USABLE = 11.25                    # screen units of runway

# ---------- the three beats ----------
# gaps between collisions, in animation seconds; each list sums to BEAT_T
BEAT_T = 10.0
GAPS_COOL = [1.1, 1.8, 1.1, 2.2, 0.9, 2.2, 0.7]
GAPS_HOT = [0.5, 0.9, 0.4, 0.8, 0.6, 1.0, 0.45, 0.7, 0.55,
            0.85, 0.5, 0.75, 0.6, 0.9, 0.5]
ACC = 1.0                         # the field — identical in every beat


def schedule(gaps):
    """(collision times, mean drift velocity, cumulative displacement at each
    collision). Mean drift is the exact time-average of the sawtooth."""
    ts, d, disp = [0.0], 0.0, [0.0]
    for g in gaps:
        ts.append(ts[-1] + g)
        d += 0.5 * ACC * g * g
        disp.append(d)
    mean_v = sum(0.5 * ACC * g * g for g in gaps) / ts[-1]
    return ts, mean_v, disp


TS_COOL, VBAR_COOL, D_COOL = schedule(GAPS_COOL)
TS_HOT, VBAR_HOT, D_HOT = schedule(GAPS_HOT)
# spatial scale: the cool beat uses the full runway
KSCALE = USABLE / (VBAR_COOL * BEAT_T)


def title_card(text, color=TXT, size=42):
    return Text(text, color=color, font_size=size, weight=BOLD)


def body(text, color=TXT, size=27):
    return Text(text, color=color, font_size=size)


def small(text, color=TXT_DIM, size=21):
    return Text(text, color=color, font_size=size)


class ResistanceLattice(Scene):

    # ------------------------------------------------------------------ setup
    def build_lattice(self):
        self.amp = ValueTracker(0.05)
        self.wall = ValueTracker(0.0)
        self.wall.add_updater(lambda m, dt: m.increment_value(dt))
        self.add(self.wall)

        ions = VGroup()
        rng = np.random.default_rng(7)
        x = ARENA_L
        while x <= ARENA_R:
            for y in ROWS:
                home = np.array([x, y, 0.0])
                ion = Dot(point=home, radius=0.085, color=GREY, fill_opacity=0.9)
                ph = rng.uniform(0, TAU, 2)
                w = rng.uniform(5.5, 9.0, 2)

                def upd(m, home=home, ph=ph, w=w):
                    t = self.wall.get_value()
                    a = self.amp.get_value()
                    m.move_to(home + np.array([a * np.cos(w[0] * t + ph[0]),
                                               a * np.sin(w[1] * t + ph[1]),
                                               0.0]))
                ion.add_updater(upd)
                ions.add(ion)
            x += COL_STEP
        self.ions = ions
        return ions

    def build_axes(self):
        ax = Axes(
            x_range=[0, BEAT_T, 2], y_range=[0, 2.5, 1],
            x_length=8.4, y_length=2.35,
            axis_config=dict(color=GREY, stroke_width=2,
                             include_ticks=True, tip_length=0.16),
            tips=False,
        ).move_to(np.array([-2.10, -2.25, 0.0]))
        xlab = small("time").next_to(ax.x_axis, DOWN, buff=0.18)
        ylab = small("drift velocity").rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.16)
        self.ax = ax
        return VGroup(ax, xlab, ylab)

    CEIL = 2.55

    def trace_for(self, ts, tracker, crash=True):
        """Live sawtooth up to tracker's value. With crash=False (the perfect
        lattice) the ramp never resets — it simply leaves through the ceiling."""
        def maker():
            t_now = tracker.get_value()
            pts = []
            for i in range(len(ts) - 1):
                t0, t1 = ts[i], min(ts[i + 1], t_now)
                if t0 >= t_now:
                    break
                n = max(2, int(30 * (t1 - t0)))
                for tt in np.linspace(t0, t1, n):
                    v = ACC * (tt - t0)
                    if v > self.CEIL:            # ran off the top; stop drawing
                        break
                    pts.append(self.ax.c2p(tt, v))
                if crash and ts[i + 1] <= t_now:
                    pts.append(self.ax.c2p(ts[i + 1], 0))
            if len(pts) < 2:
                return VMobject()
            return VMobject(stroke_color=TRACE, stroke_width=3.2
                            ).set_points_as_corners(pts)
        return always_redraw(maker)

    def electron_for(self, ts, disp, tracker, free=False):
        e = Dot(radius=0.105, color=ELECTRON, fill_opacity=1.0)
        e.set_stroke(ELECTRON, width=6, opacity=0.30)

        def place(m):
            t = tracker.get_value()
            if free:
                d = 0.5 * ACC * t * t
            else:
                i = 0
                while i < len(ts) - 2 and ts[i + 1] <= t:
                    i += 1
                d = disp[i] + 0.5 * ACC * (t - ts[i]) ** 2
            x = START_X + KSCALE * d
            y = LANE + 0.135 * np.sin(10.1 * (x - START_X))
            m.move_to(np.array([min(x, ARENA_R + 1.9), y, 0.0]))
        e.add_updater(place)
        return e

    # ------------------------------------------------------------------ scenes
    def construct(self):
        self.scene1_open()
        self.scene2_cool()
        self.scene3_hot()
        self.scene4_perfect()
        self.scene5_close()

    def scene1_open(self):
        t1 = title_card("What resistance actually is")
        t2 = body("Accelerate. Crash. Accelerate. Crash.", color=TXT_DIM).next_to(t1, DOWN, buff=0.42)
        self.play(FadeIn(t1, shift=UP * 0.3), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.9)
        self.wait(1.8)
        t3 = small("The field is the same in all three. So is the clock.\n"
                   "How far the electron gets is the answer.", size=24).move_to(t2)
        self.play(FadeOut(t1, shift=UP * 0.3), Transform(t2, t3), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(t2), run_time=0.7)

        self.add(self.build_lattice())
        self.axes_group = self.build_axes()
        self.add(self.axes_group)
        self.readout = VGroup(
            small("drift velocity", size=20),
            body("—", color=ELECTRON, size=30),
            small("resistance", size=20),
            body("—", color=RED, size=30),
        ).arrange(DOWN, buff=0.16).move_to(np.array([5.55, -2.25, 0.0]))
        self.play(FadeIn(self.ions, lag_ratio=0.004), run_time=1.6)

    def run_beat(self, ts, disp, vbar, caption, sub, ion_color, amp,
                 flash_time, ref=None, free=False):
        cap = title_card(caption, size=36).move_to(np.array([0, 3.48, 0]))
        subt = small(sub, size=23).move_to(np.array([0, 3.02, 0]))
        self.play(FadeIn(cap), FadeIn(subt),
                  self.amp.animate.set_value(amp),
                  self.ions.animate.set_color(ion_color),
                  run_time=1.3)

        t = ValueTracker(0.0)
        trace = self.trace_for(ts if not free else [0.0, 6.0], t, crash=not free)
        e = self.electron_for(ts, disp, t, free=free)
        self.add(trace, e)

        if free:
            self.play(t.animate.set_value(4.4), run_time=4.4, rate_func=linear)
        else:
            for i in range(len(ts) - 1):
                self.play(t.animate.set_value(ts[i + 1]),
                          run_time=max(0.28, ts[i + 1] - ts[i]), rate_func=linear)
                self.play(Flash(e.get_center(), color=RED, line_length=0.14,
                                num_lines=9, flash_radius=0.22,
                                line_stroke_width=2.6, run_time=flash_time))
        return cap, subt, trace, e, t

    def scene2_cool(self):
        cap, subt, trace, e, t = self.run_beat(
            TS_COOL, D_COOL, VBAR_COOL,
            "1 — a cool lattice",
            "long free flights: the electron gets a good run between crashes",
            GREY, 0.038, 0.20)

        mean = DashedLine(self.ax.c2p(0, VBAR_COOL), self.ax.c2p(BEAT_T, VBAR_COOL),
                          color=TXT, stroke_width=2.4, dash_length=0.11)
        mlab = small("average", size=20).next_to(
            self.ax.c2p(BEAT_T, VBAR_COOL), RIGHT, buff=0.16)
        self.play(Create(mean), FadeIn(mlab), run_time=1.1)

        rule = MathTex(r"R=\frac{V}{I}=\frac{V}{nAvq}\ \Rightarrow\ R\propto\frac{1}{v}",
                       color=TXT, font_size=34).move_to(np.array([0, 0.06, 0]))
        self.play(Write(rule), run_time=1.6)
        self.readout[1].become(body("reference", color=ELECTRON, size=27).move_to(self.readout[1]))
        self.readout[3].become(body("reference", color=RED, size=27).move_to(self.readout[3]))
        self.play(FadeIn(self.readout), run_time=0.8)
        self.wait(2.2)

        self.carry = dict(rule=rule)
        self.play(FadeOut(cap), FadeOut(subt), FadeOut(trace), FadeOut(e),
                  FadeOut(mean), FadeOut(mlab), run_time=0.8)

    def scene3_hot(self):
        cap, subt, trace, e, t = self.run_beat(
            TS_HOT, D_HOT, VBAR_HOT,
            "2 — the same lattice, white hot",
            "same push, same clock — but the ions thrash and cut every flight short",
            RED, 0.105, 0.13)

        mean = DashedLine(self.ax.c2p(0, VBAR_HOT), self.ax.c2p(BEAT_T, VBAR_HOT),
                          color=TXT, stroke_width=2.4, dash_length=0.11)
        ghost = DashedLine(self.ax.c2p(0, VBAR_COOL), self.ax.c2p(BEAT_T, VBAR_COOL),
                           color=TXT_DIM, stroke_width=1.8, dash_length=0.09).set_opacity(0.55)
        glab = small("beat 1", size=18).next_to(
            self.ax.c2p(BEAT_T, VBAR_COOL), RIGHT, buff=0.16)
        self.play(Create(mean), Create(ghost), FadeIn(glab), run_time=1.1)

        ratio = VBAR_COOL / VBAR_HOT
        frac = VBAR_HOT / VBAR_COOL
        self.readout[1].become(body(f"{frac:.2f}×", color=ELECTRON, size=30).move_to(self.readout[1]))
        self.readout[3].become(body(f"{ratio:.1f}×", color=RED, size=30).move_to(self.readout[3]))
        punch = body(f"the electron reached {frac:.0%} as far — "
                     f"so R is {ratio:.1f} times larger",
                     color=RED, size=26).move_to(np.array([0, 0.06, 0]))
        self.play(FadeOut(self.carry["rule"]), FadeIn(punch), run_time=1.0)
        self.wait(2.6)

        self.play(FadeOut(cap), FadeOut(subt), FadeOut(trace), FadeOut(e),
                  FadeOut(mean), FadeOut(ghost), FadeOut(glab), FadeOut(punch),
                  run_time=0.8)

    def scene4_perfect(self):
        note = small("The pinball picture says the ions do the scattering.\n"
                     "So freeze them — perfectly still, perfectly periodic.",
                     size=23).move_to(np.array([0, 0.06, 0]))
        self.play(FadeIn(note), run_time=1.0)
        self.wait(1.6)
        self.play(FadeOut(note), run_time=0.5)

        cap, subt, trace, e, t = self.run_beat(
            [0.0, 4.4], [0.0], 0.0,
            "3 — a perfect lattice",
            "an electron is a wave, and a perfect periodic lattice does not scatter waves",
            BLUE, 0.0, 0.0, free=True)

        arrow = Arrow(self.ax.c2p(3.3, 1.55), self.ax.c2p(4.3, 2.45),
                      color=TXT, buff=0.05, stroke_width=3,
                      max_tip_length_to_length_ratio=0.22)
        nolim = small("no ceiling —\nthe drift never terminates", size=19).next_to(
            arrow, DR, buff=0.10)
        self.play(GrowArrow(arrow), FadeIn(nolim), run_time=1.0)

        self.readout[1].become(body("unbounded", color=ELECTRON, size=27).move_to(self.readout[1]))
        self.readout[3].become(body("zero", color=BLUE, size=30).move_to(self.readout[3]))
        punch = body("No terminal drift means no ratio to take. R has nothing to be.",
                     color=BLUE, size=26).move_to(np.array([0, 0.06, 0]))
        self.play(FadeIn(punch), run_time=1.0)
        self.wait(2.8)
        self.play(FadeOut(cap), FadeOut(subt), FadeOut(trace), FadeOut(e),
                  FadeOut(arrow), FadeOut(nolim), FadeOut(punch), run_time=0.8)
        self.perfect_ions = True

    def scene5_close(self):
        self.play(FadeOut(self.ions, lag_ratio=0.004),
                  FadeOut(self.readout), FadeOut(self.axes_group), run_time=1.2)

        l1 = title_card("Resistance is not the ions.", size=40)
        l2 = title_card("It is their imperfections.", size=40, color=AMBER)
        l3 = small("thermal vibration · impurity atoms · crystal defects\n"
                   "take those away and there is nothing left to resist",
                   size=24)
        grp = VGroup(l1, l2, l3).arrange(DOWN, buff=0.45)
        self.play(FadeIn(l1, shift=UP * 0.25), run_time=1.1)
        self.play(FadeIn(l2, shift=UP * 0.25), run_time=1.1)
        self.play(FadeIn(l3), run_time=0.9)
        self.wait(3.0)
        self.play(FadeOut(grp), run_time=1.0)
