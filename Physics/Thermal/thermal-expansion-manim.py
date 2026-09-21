"""Manim scene for [[Thermal Expansion]].
Scene  Well — a particle oscillating in the potential well of a real bond (steep near wall, gentle far
              slope).  Each time its energy is raised it swings wider, but much further OUT than in,
              so its average separation (red marker) drifts outward: that drift is thermal expansion.
              Then the same energies in a symmetric well: the average does not move.
Smoke:  manim -ql --fps 15 thermal-expansion-manim.py Well
Final:  manim -qk thermal-expansion-manim.py Well
The motion is integrated numerically from the force, not drawn by hand."""
import numpy as np
from manim import *

GREY_T, BLUE_H, GREEN_H, RED_H, AMBER_H = "#888888", "#2563eb", "#059669", "#dc2626", "#f59e0b"
R0 = 2 ** (1 / 6)
K = 57.15 / R0**2


def lj(r):
    return 4 * (r**-12 - r**-6)


def lj_force(r):
    return 24 * (2 * r**-13 - r**-7)


def spring(r):
    return -1 + 0.5 * K * (r - R0) ** 2


def spring_force(r):
    return -K * (r - R0)


def trajectory(U, F, E, n_periods=3, dt=2e-4):
    """Start at the inner turning point with total energy E; velocity-Verlet; return r(t) over whole periods."""
    grid = np.linspace(0.9, R0, 200_001)
    r = grid[np.argmin(np.abs(U(grid) - E))] + 1e-6
    v, rs, returns = 0.0, [], 0
    while returns < n_periods and len(rs) < 600_000:
        a = F(r); r_new = r + v * dt + 0.5 * a * dt * dt
        v_new = v + 0.5 * (a + F(r_new)) * dt
        if v < 0 <= v_new:                                # back at the inner turning point: one whole period
            returns += 1
        r, v = r_new, v_new; rs.append(r)
    return np.array(rs)


class Well(Scene):
    def construct(self):
        title = Text("Why heating makes matter bigger", font_size=26, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        x0, x1, y0, y1 = 0.95, 1.75, -1.08, 0.0
        W, H = 9.0, 4.4
        origin = np.array([-4.5, -2.3, 0])

        def P(r, u):
            return origin + np.array([(r - x0) / (x1 - x0) * W, (u - y0) / (y1 - y0) * H, 0])

        def run(U, F, label, conclusion, colour):
            rr = np.linspace(0.90, x1, 340)
            pts = [P(r, U(r)) for r in rr if U(r) < y1 + 0.0]
            curve = VMobject(color=BLUE_H, stroke_width=4).set_points_smoothly(pts)
            axis = Line(P(x0, y0), P(x1, y0), color=GREY_T, stroke_width=2)
            xl = Text("separation of two neighbouring particles", font_size=18, color=GREY_T).next_to(axis, DOWN, buff=0.12)
            yl = Text("energy", font_size=18, color=GREY_T).rotate(PI / 2).next_to(P(x0, -0.5), LEFT, buff=0.15)
            rest = DashedLine(P(R0, y0), P(R0, y1), color=GREY_T, stroke_width=1.5, dash_length=0.08)
            restl = Text("cold spacing", font_size=16, color=GREY_T).next_to(P(R0, y1), UP, buff=0.05)
            lab = Text(label, font_size=22, color=colour).next_to(title, DOWN, buff=0.18)
            group = VGroup(curve, axis, xl, yl, rest, restl, lab)
            self.add(group)
            marks = VGroup()
            cap = Text("", font_size=22, color=GREY_T)
            for E, word in ((-0.9, "cool"), (-0.6, "warmer"), (-0.3, "hot")):
                rs = trajectory(U, F, E)
                mean = rs.mean()
                level = Line(P(rs.min(), E), P(rs.max(), E), color=AMBER_H, stroke_width=2)
                ball = Dot(P(rs[0], E), color=AMBER_H, radius=0.13)
                new_cap = Text(f"{word}: more energy, a wider swing", font_size=22, color=GREY_T).to_edge(DOWN, buff=0.3)
                self.remove(cap); cap = new_cap
                self.add(level, ball, cap)
                tr = ValueTracker(0)
                ball.add_updater(lambda m, rs=rs, E=E: m.move_to(P(rs[min(len(rs) - 1, int(tr.get_value() * (len(rs) - 1)))], E)))
                self.play(tr.animate.set_value(1), run_time=4.2, rate_func=linear)
                ball.clear_updaters(); self.remove(ball)
                mk = Dot(P(mean, E), color=RED_H, radius=0.1)
                marks.add(mk, level); self.add(mk); self.wait(0.5)
            self.remove(cap)
            cap = Text(conclusion, font_size=22, color=RED_H).to_edge(DOWN, buff=0.3)
            self.add(cap); self.wait(3.2)
            self.remove(group, cap, *marks)

        run(lj, lj_force, "a real bond: steep wall inside, gentle slope outside",
            "red: the average spacing. It drifts outward as the energy rises. That is expansion.", BLUE_H)
        run(spring, spring_force, "an imaginary, perfectly symmetric bond",
            "the swing widens equally both ways: the average stays put, and nothing would expand", GREEN_H)
