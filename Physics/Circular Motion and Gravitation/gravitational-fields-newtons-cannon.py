"""Manim: Newton's cannon — an orbit is a fall that keeps missing.

Act 1  A cannon on a mountain fires horizontally, faster each time. Every path is
       integrated from the inverse-square law (RK4); nothing is drawn by hand.
       0.6 v_c and 0.85 v_c fall to the ground; at v_c = √(GM/r) the ball falls all
       the way round — a circular orbit; at 1.2 v_c an ellipse with the launch
       point as its lowest point; at √2 v_c it never returns — escape.
Act 2  Kepler's second law on the ellipse: sectors swept in equal times have equal
       areas — fast near the planet, slow far out — the face of angular-momentum
       conservation.

Paced slowly: short captions, long holds.

Render (from this folder):
    manim -ql gravitational-fields-newtons-cannon.py NewtonsCannon    # smoke
    manim -qk gravitational-fields-newtons-cannon.py NewtonsCannon    # 4K final
Copy media/videos/gravitational-fields-newtons-cannon/2160p60/NewtonsCannon.mp4
  -> gravitational-fields-newtons-cannon.mp4 beside the card, then rm -rf media/ __pycache__/.
"""

import numpy as np
from manim import (
    Scene, VGroup, VMobject, Text, MathTex, Dot, Line, Circle, Polygon, DashedVMobject,
    ValueTracker, always_redraw, FadeIn, FadeOut, Transform, Create,
    UP, DOWN, LEFT, RIGHT, config,
)

BG = "#1e1e1e"
TXT = "#cccccc"
GREY = "#9a9a9a"
BLUE = "#2563eb"
GREEN = "#059669"
AMBER = "#f59e0b"
RED = "#dc2626"
PURPLE = "#7c3aed"
TEAL = "#0891b2"
FONT = "Helvetica Neue"
config.background_color = BG

C = np.array([-2.4, 1.2, 0.0])       # Earth's centre (scene units)
R_E = 1.35                            # Earth's radius
R_L = 1.47                            # launch radius (mountain top)
T_CIRC = 6.0                          # scene seconds for one circular orbit at R_L
GM = 4 * np.pi**2 * R_L**3 / T_CIRC**2
V_C = np.sqrt(GM / R_L)


def integrate(v_factor, t_max=20.0, dt=5e-3):
    """launch from the top of the Earth, horizontal to the right, speed v_factor * V_C.
    Returns arrays t, pos (N,2) relative to C; stops on hitting the surface or leaving the frame."""
    pos = np.array([0.0, R_L]); vel = np.array([v_factor * V_C, 0.0])
    def acc(p):
        r = np.linalg.norm(p); return -GM * p / r**3
    ts = [0.0]; ps = [pos.copy()]
    t = 0.0
    while t < t_max:
        k1v = acc(pos); k1p = vel
        k2v = acc(pos + dt / 2 * k1p); k2p = vel + dt / 2 * k1v
        k3v = acc(pos + dt / 2 * k2p); k3p = vel + dt / 2 * k2v
        k4v = acc(pos + dt * k3p); k4p = vel + dt * k3v
        pos = pos + dt / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
        vel = vel + dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
        t += dt
        ts.append(t); ps.append(pos.copy())
        if np.linalg.norm(pos) < R_E:                    # hit the ground
            break
        sx, sy = C[0] + pos[0], C[1] + pos[1]
        if sx > 7.6 or sx < -7.6 or sy > 4.6 or sy < -4.6:  # left the frame
            break
        if v_factor <= 1.0 and t > 0.3 and np.linalg.norm(pos - np.array([0.0, R_L])) < 0.02 and vel[0] > 0:
            break                                          # one full circle
        if 1.0 < v_factor < 1.4 and t > 1.0 and abs(pos[1] - R_L) < 8e-3 and abs(pos[0]) < 0.06 and vel[0] > 0:
            break                                          # one full ellipse
    return np.array(ts), np.array(ps)


def scene_pts(ps):
    return [C + np.array([p[0], p[1], 0.0]) for p in ps]


def note(s, size=26, color=TXT):
    return Text(s, font=FONT, font_size=size, color=color)


class NewtonsCannon(Scene):
    def construct(self):
        title = Text("Newton's cannon — an orbit is a fall that keeps missing", font=FONT, font_size=34, color=TXT)
        title.to_edge(UP, buff=0.3)
        earth = Circle(radius=R_E, color=BLUE, fill_color=BLUE, fill_opacity=0.25, stroke_width=2).move_to(C)
        mountain = Polygon(C + np.array([-0.18, R_E - 0.02, 0]), C + np.array([0.18, R_E - 0.02, 0]),
                           C + np.array([0.0, R_L, 0]), color=GREY, fill_color=GREY, fill_opacity=0.8, stroke_width=1)
        centre = Dot(C, radius=0.04, color=GREY)
        self.play(FadeIn(title), FadeIn(earth), FadeIn(mountain), FadeIn(centre), run_time=1.0)
        cap = note("fire a ball horizontally from a high mountain — faster each time", 26)
        cap.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(1.6)

        shots = [
            (0.70, RED,    "v = 0.70 × √(GM/r)", "too slow — it falls to the ground", 0.35),
            (0.90, AMBER,  "v = 0.90 × √(GM/r)", "faster — farther, but still a fall", 0.35),
            (1.00, GREEN,  "v = √(GM/r)",         "it falls all the way round: a circular orbit", 1.0),
            (1.20, TEAL,   "v = 1.2 × √(GM/r)",   "faster still — an ellipse; the launch point is its lowest point", 1.55),
            (1.42, PURPLE, "v = √2 × √(GM/r)",    "at √2 times the circular speed it never comes back — escape", 1.0),
        ]
        readout_x = 4.3
        label_rows = VGroup()
        kept = []
        ellipse_data = None
        ell_trail = None
        for vf, col, lab_txt, cap_txt, speedup in shots:
            ts, ps = integrate(vf)
            if abs(vf - 1.20) < 1e-6:
                ellipse_data = (ts, ps)
            pts = scene_pts(ps)
            tr = ValueTracker(0.0)
            n = len(pts)

            def idx(tr=tr, n=n):
                return int(min(n - 1, max(0, round(tr.get_value()))))

            trail = always_redraw(lambda pts=pts, idx=idx: VMobject(color=col, stroke_width=3).set_points_as_corners(
                pts[:max(2, idx() + 1)]))
            ball = always_redraw(lambda pts=pts, idx=idx: Dot(pts[idx()], radius=0.09, color=col))
            lab = note(lab_txt, 26, col)
            lab.move_to(np.array([readout_x, 2.6 - 0.55 * len(label_rows), 0]))
            cap_new = note(cap_txt, 26)
            cap_new.to_edge(DOWN, buff=0.4)
            self.play(FadeIn(lab), Transform(cap, cap_new), run_time=0.6)
            self.add(trail, ball)
            flight = ts[-1] / speedup
            self.play(tr.animate.set_value(n - 1), run_time=max(1.2, flight), rate_func=lambda s: s)
            trail.clear_updaters(); ball.clear_updaters()
            label_rows.add(lab)
            if abs(vf - 1.20) < 1e-6:
                ell_trail = trail
            else:
                kept.append(trail)
            self.wait(1.8)
            if vf < 1.0:
                self.play(FadeOut(ball), trail.animate.set_stroke(opacity=0.35), run_time=0.5)
            elif vf > 1.3:
                self.play(FadeOut(ball), run_time=0.4)
            else:
                self.play(FadeOut(ball), trail.animate.set_stroke(opacity=0.6), run_time=0.5)

        summary = VGroup(
            note("same cannon, same height — only the speed changes", 24, GREY),
            note("below √(GM/r): back to Earth.   at it: a circle.   above: an ellipse.   at √2 × it: gone", 24, GREY),
        ).arrange(DOWN, buff=0.12).to_edge(DOWN, buff=0.4)
        self.play(Transform(cap, summary), run_time=0.8)
        self.wait(3.0)

        # ============================================================ Act 2 — Kepler II on the ellipse
        self.play(FadeOut(label_rows), *[FadeOut(t) for t in kept], run_time=0.8)
        title2 = Text("Kepler's second law — equal areas in equal times", font=FONT, font_size=34, color=TXT).to_edge(UP, buff=0.3)
        self.play(Transform(title, title2), run_time=0.6)
        ts, ps = ellipse_data
        pts = scene_pts(ps)
        self.play(ell_trail.animate.set_stroke(opacity=1.0), run_time=0.4)

        # sectors swept in equal time windows: pick windows at perigee (start), a quarter, and apogee
        T_e = ts[-1]
        dt_win = T_e * 0.07
        starts = [0.0, T_e * 0.22, T_e * 0.5 - dt_win / 2]
        colors = [AMBER, GREEN, PURPLE]

        def sector_pts(t0):
            m = (ts >= t0) & (ts <= t0 + dt_win)
            seg = pts[m.argmax(): m.argmax() + m.sum()]
            return [C] + seg + [C]

        def sector_area(t0):
            m = (ts >= t0) & (ts <= t0 + dt_win)
            P = ps[m]
            return 0.5 * np.abs(np.sum(P[:-1, 0] * P[1:, 1] - P[1:, 0] * P[:-1, 1]))

        tr2 = ValueTracker(0.0)
        n = len(pts)
        ball2 = always_redraw(lambda: Dot(pts[int(min(n - 1, max(0, round(tr2.get_value()))))], radius=0.09, color=TEAL))
        radius_line = always_redraw(lambda: Line(C, pts[int(min(n - 1, max(0, round(tr2.get_value()))))], color=GREY, stroke_width=1.5))
        self.add(radius_line, ball2)
        cap2 = note("the radius line sweeps out area — compare three equal time slices", 26)
        cap2.to_edge(DOWN, buff=0.4)
        self.play(Transform(cap, cap2), run_time=0.6)

        area_labels = VGroup()
        for t0, colr in zip(starts, colors):
            i0 = int(np.searchsorted(ts, t0)); i1 = int(np.searchsorted(ts, t0 + dt_win))
            self.play(tr2.animate.set_value(i0), run_time=max(0.6, (i0 - tr2.get_value()) / n * T_e * 1.2), rate_func=lambda s: s)
            sec = Polygon(*sector_pts(t0), color=colr, fill_color=colr, fill_opacity=0.45, stroke_width=1)
            self.add(sec)
            self.play(tr2.animate.set_value(i1), run_time=dt_win * 2.2, rate_func=lambda s: s)
            A = sector_area(t0)
            lab = note(f"area = {A:.2f}", 26, colr)
            lab.move_to(np.array([readout_x, 2.6 - 0.6 * len(area_labels), 0]))
            self.play(FadeIn(lab), run_time=0.4)
            area_labels.add(lab)
            self.wait(0.8)
        self.play(tr2.animate.set_value(n - 1), run_time=2.5, rate_func=lambda s: s)

        fin = VGroup(
            note("equal areas in equal times: fast near the planet, slow far out", 26, TXT),
            note("gravity pulls along the radius, so it has no torque: angular momentum is conserved", 22, GREY),
        ).arrange(DOWN, buff=0.12).to_edge(DOWN, buff=0.4)
        self.play(Transform(cap, fin), run_time=0.8)
        self.wait(4.0)
