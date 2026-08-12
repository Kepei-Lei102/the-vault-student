# Manim Community Edition — Kinetic Theory gas simulation
# stack: Manim (long-form animation track)
#
# Renders the molecular-dynamics explainer embedded in
#   Physics/Thermal/Kinetic Theory and the Ideal Gas.md
#
# A real little 2-D molecular dynamics sim (random motion, elastic wall bounces,
# optional elastic molecule–molecule collisions) driven by a per-frame updater.
# It shows three things, in order:
#   1. random motion with the NET-momentum arrow staying ~0  → "no wind"
#   2. the right wall flashing on every impact                → "that drumbeat IS pressure"
#   3. HEATING the gas: speeds rise, the live speed histogram slides right & flattens
#      into the Maxwell–Boltzmann shape.
#
# RENDER (on Kepei's Mac, where LaTeX + manimpango live):
#   cd "/Users/kepeilei/Desktop/The_Vault/Physics/Thermal"
#   manim -qk kinetic-theory-gas-simulation.py KineticTheoryGas      # 4K, committed showcase
#   # iterate first with -qm (720p) or -qh (1080p) if you want speed
#   # output lands in media/videos/.../KineticTheoryGas.mp4 — copy/rename to
#   # kinetic-theory-gas-simulation.mp4 in THIS folder so the [[embed]] resolves.
#
# If molecule–molecule collisions ever look jittery on your machine, set
# ENABLE_PAIR_COLLISIONS = False — wall-only bouncing is already stable and
# tells the whole story (speeds are seeded from Maxwell–Boltzmann either way).

import numpy as np
from manim import *

config.background_color = "#1e1e1e"

# ---- vault palette --------------------------------------------------------
GREY   = "#aaaaaa"      # labels (lighter than the SVG #888 for a dark video bg)
SLOW   = "#2563eb"      # blue  — slow molecules
FAST   = "#dc2626"      # red   — fast molecules
GREEN  = "#059669"
AMBER  = "#f59e0b"
PURPLE = "#7c3aed"

# ---- simulation knobs -----------------------------------------------------
N_MOL                  = 70
MOL_RADIUS             = 0.075
ENABLE_PAIR_COLLISIONS = True
SPEED_SCALE            = 1.0     # sim-units per second multiplier
DT_CAP                 = 1 / 30  # clamp dt so a slow frame can't tunnel a molecule through a wall
SEED                   = 7

# box geometry (Manim scene units)
BOX_CX, BOX_CY = -3.1, -0.1
BOX_HALF       = 2.3             # half-side → box spans ±2.3 about its centre
# histogram panel geometry
HIST_X0, HIST_X1 = 0.7, 6.4
HIST_Y0          = -2.1          # baseline
HIST_H           = 3.4           # max bar height
N_BINS           = 11


class KineticTheoryGas(Scene):
    def construct(self):
        rng = np.random.default_rng(SEED)

        # ---------- box ----------
        box = Square(side_length=2 * BOX_HALF, stroke_color=GREY, stroke_width=2.5)
        box.move_to([BOX_CX, BOX_CY, 0])
        self.lo = np.array([BOX_CX - BOX_HALF, BOX_CY - BOX_HALF])
        self.hi = np.array([BOX_CX + BOX_HALF, BOX_CY + BOX_HALF])

        # right-wall "impact glow" — opacity decays each frame, bumped on a hit
        self.wall_glow = Line(
            [self.hi[0], self.lo[1], 0], [self.hi[0], self.hi[1], 0],
            stroke_color=AMBER, stroke_width=8,
        ).set_opacity(0.0)

        # ---------- molecules ----------
        # positions: uniform in box (kept a hair off the walls)
        pos = rng.uniform(self.lo + MOL_RADIUS, self.hi - MOL_RADIUS, size=(N_MOL, 2))
        # speeds: Maxwell–Boltzmann in 2-D → each velocity component ~ Normal(0, s)
        s0 = 1.7
        vel = rng.normal(0.0, s0, size=(N_MOL, 2))
        self.pos, self.vel = pos, vel

        speeds0 = np.linalg.norm(vel, axis=1)
        self.smax = float(speeds0.max()) * 1.6   # colour/hist scale headroom for heating

        dots = VGroup(*[
            Dot([p[0], p[1], 0], radius=MOL_RADIUS, color=self._speed_color(np.linalg.norm(v)))
            for p, v in zip(pos, vel)
        ])
        self.dots = dots

        # ---------- net-momentum arrow (from box centre) ----------
        self.arrow_gain = 6.0   # amplify the tiny mean so it's visible at all
        net_arrow = always_redraw(self._make_net_arrow)

        # ---------- live speed histogram ----------
        hist = always_redraw(self._make_histogram)
        hist_axis = Line([HIST_X0, HIST_Y0, 0], [HIST_X1, HIST_Y0, 0],
                         stroke_color=GREY, stroke_width=2)
        hist_xlabel = Text("molecular speed →", font_size=20, color=GREY)
        hist_xlabel.next_to(hist_axis, DOWN, buff=0.18)

        # ---------- the physics updater ----------
        driver = Mobject()  # invisible carrier for the stepping updater
        driver.add_updater(lambda m, dt: self._step(dt))
        self.add(driver)

        # ---------- titles / captions ----------
        title = Text("A gas is molecules bouncing in a box", font_size=30, color=GREY)
        title.to_edge(UP, buff=0.35)

        # ============ SCENE 1 — random motion ============
        self.play(Create(box), run_time=1.0)
        self.add(self.wall_glow)
        self.play(FadeIn(dots, scale=0.5), Write(title), run_time=1.2)
        self.wait(4.5)

        # ============ SCENE 2 — net momentum ≈ 0 → no wind ============
        net_label = Text("average velocity ≈ 0  →  no wind", font_size=24, color=GREEN)
        net_label.next_to(box, DOWN, buff=0.35)
        self.add(net_arrow)
        self.play(FadeIn(net_label), run_time=0.8)
        self.wait(4.5)

        # ============ SCENE 3 — the wall drumbeat is pressure ============
        press_label = Text("each wall hit = a kick;  their sum = pressure",
                           font_size=22, color=AMBER)
        press_label.next_to(box, UP, buff=0.18).shift(RIGHT * 0.0)
        # tuck it just under the title
        press_label.next_to(title, DOWN, buff=0.18)
        self.play(FadeIn(press_label), run_time=0.8)
        self.wait(4.5)

        # ============ SCENE 4 — the speed histogram ============
        hist_title = Text("speed distribution", font_size=22, color=GREY)
        hist_title.move_to([(HIST_X0 + HIST_X1) / 2, HIST_Y0 + HIST_H + 0.45, 0])
        self.play(Create(hist_axis), FadeIn(hist_xlabel), FadeIn(hist_title), run_time=1.0)
        self.add(hist)
        self.wait(4.0)

        # ============ SCENE 5 — heat it ============
        heat_label = Text("HEAT IT:  T → 2T", font_size=26, color=FAST)
        heat_label.next_to(hist_title, UP, buff=0.3)
        self.play(FadeIn(heat_label), run_time=0.6)
        # raise every molecule's speed by √2  (KE → 2×, so ⟨c²⟩ → 2×, T → 2T)
        self.vel *= np.sqrt(2.0)
        self.wait(5.5)

        # final beat
        closer = Text("faster molecules → curve slides right & flattens",
                      font_size=22, color=GREY)
        closer.next_to(hist_xlabel, DOWN, buff=0.3)
        self.play(FadeIn(closer), run_time=0.8)
        self.wait(3.0)

    # ------------------------------------------------------------------ #
    #  helpers
    # ------------------------------------------------------------------ #
    def _speed_color(self, s):
        t = float(np.clip(s / self.smax, 0.0, 1.0))
        return interpolate_color(ManimColor(SLOW), ManimColor(FAST), t)

    def _step(self, dt):
        dt = min(dt, DT_CAP)
        if dt <= 0:
            return
        step = dt * SPEED_SCALE
        self.pos += self.vel * step

        # --- elastic wall reflection (clamp back inside, flip the normal component) ---
        for ax in (0, 1):
            lo, hi = self.lo[ax] + MOL_RADIUS, self.hi[ax] - MOL_RADIUS
            below = self.pos[:, ax] < lo
            above = self.pos[:, ax] > hi
            if np.any(below):
                self.pos[below, ax] = lo
                self.vel[below, ax] = np.abs(self.vel[below, ax])
            if np.any(above):
                self.pos[above, ax] = hi
                self.vel[above, ax] = -np.abs(self.vel[above, ax])
                if ax == 0:                       # a hit on the RIGHT wall → glow
                    self.wall_glow.set_opacity(min(1.0, self.wall_glow.get_stroke_opacity() + 0.6))

        # --- optional equal-mass elastic molecule–molecule collisions ---
        if ENABLE_PAIR_COLLISIONS:
            self._pair_collisions()

        # decay the wall glow
        self.wall_glow.set_opacity(max(0.0, self.wall_glow.get_stroke_opacity() - 4.0 * dt))

        # --- repaint dots at new positions, recolour by speed ---
        speeds = np.linalg.norm(self.vel, axis=1)
        for i, d in enumerate(self.dots):
            d.move_to([self.pos[i, 0], self.pos[i, 1], 0])
            d.set_color(self._speed_color(speeds[i]))

    def _pair_collisions(self):
        # O(N^2) but N is small; equal masses → exchange velocity along the line of centres
        d = 2 * MOL_RADIUS
        for i in range(N_MOL):
            for j in range(i + 1, N_MOL):
                delta = self.pos[i] - self.pos[j]
                dist2 = delta @ delta
                if dist2 < d * d and dist2 > 1e-9:
                    dist = np.sqrt(dist2)
                    n = delta / dist
                    dv = self.vel[i] - self.vel[j]
                    approaching = dv @ n
                    if approaching < 0:                 # only if moving toward each other
                        self.vel[i] -= approaching * n
                        self.vel[j] += approaching * n
                    overlap = d - dist                  # separate so they don't stick
                    self.pos[i] += 0.5 * overlap * n
                    self.pos[j] -= 0.5 * overlap * n

    def _make_net_arrow(self):
        mean_v = self.vel.mean(axis=0) * self.arrow_gain
        start = np.array([BOX_CX, BOX_CY, 0])
        end = start + np.array([mean_v[0], mean_v[1], 0])
        if np.linalg.norm(end - start) < 0.05:
            end = start + np.array([0.05, 0.0, 0])
        return Arrow(start, end, buff=0, color=GREEN, stroke_width=6,
                     max_tip_length_to_length_ratio=0.4)

    def _make_histogram(self):
        speeds = np.linalg.norm(self.vel, axis=1)
        edges = np.linspace(0.0, self.smax, N_BINS + 1)
        counts, _ = np.histogram(speeds, bins=edges)
        cmax = max(counts.max(), 1)
        bar_w = (HIST_X1 - HIST_X0) / N_BINS
        bars = VGroup()
        for k, c in enumerate(counts):
            h = HIST_H * (c / cmax)
            if h <= 1e-3:
                continue
            x = HIST_X0 + (k + 0.5) * bar_w
            mid_speed = 0.5 * (edges[k] + edges[k + 1])
            bar = Rectangle(
                width=bar_w * 0.86, height=h,
                stroke_width=0,
                fill_color=interpolate_color(ManimColor(SLOW), ManimColor(FAST),
                                             float(np.clip(mid_speed / self.smax, 0, 1))),
                fill_opacity=0.85,
            )
            bar.move_to([x, HIST_Y0 + h / 2, 0])
            bars.add(bar)
        return bars
