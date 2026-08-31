"""Manim: circular motion — see it run.

Act 1  Uniform circular motion. The velocity arrow (green) is always tangent, the
       acceleration arrow (amber) always points at the centre. On the right the
       velocity is redrawn from one fixed origin: its tip traces a circle of radius
       v at the same ω, so the tip moves at speed vω — and the speed of the tip of
       v IS the acceleration: a = vω = v²/r, toward the centre.
Act 2  Cut the string: no force, no turning — the particle flies straight along the
       tangent, not outward.
Act 3  A vertical circle on a string, three launches from the bottom — u² = 4gr
       (the string goes slack at 132° and the particle becomes a projectile),
       u² = 5gr (tension grazes zero at the top: just complete), u² = 6gr (round
       with a margin; T_bottom − T_top = 6mg as always). Tension is read live.
       The motion is integrated from θ'' = −(g/r) sin θ; nothing is faked.

Render (from this folder):
    manim -ql circular-motion-see-it-run.py CircularMotionSeeItRun    # smoke
    manim -qk circular-motion-see-it-run.py CircularMotionSeeItRun    # 4K final
Copy media/videos/circular-motion-see-it-run/2160p60/CircularMotionSeeItRun.mp4
  -> circular-motion-see-it-run.mp4 beside the card, then rm -rf media/ __pycache__/.
"""

import numpy as np
from manim import (
    Scene, VGroup, VMobject, Text, MathTex, Dot, Line, Arrow, Circle, DashedLine,
    DashedVMobject, Rectangle, DecimalNumber, Integer, ValueTracker, always_redraw,
    FadeIn, FadeOut, Create, Transform, Write,
    UP, DOWN, LEFT, RIGHT, ORIGIN, config,
)

BG = "#1e1e1e"
TXT = "#cccccc"
GREY = "#9a9a9a"
BLUE = "#2563eb"
GREEN = "#059669"     # velocity / the truth
AMBER = "#f59e0b"     # acceleration, the 4gr run
RED = "#dc2626"       # the wrong idea
PURPLE = "#7c3aed"
FONT = "Helvetica Neue"
config.background_color = BG

# ------------------------------------------------------------------ Act 1/2 geometry
C = np.array([-3.6, -0.2, 0.0])      # centre of the position circle
R = 2.2                               # scene radius
OMEGA = 1.0                           # rad/s in scene time
H = np.array([3.1, 0.45, 0.0])        # hodograph origin
VLEN = 1.6                            # on-screen length of the velocity arrow

# ------------------------------------------------------------------ Act 3 dynamics
G, RP = 9.81, 1.0                     # physical g and radius
SLOW = 3.4                            # scene seconds per physical second (slowed so the tension can be read)
O3 = np.array([-3.7, 0.35, 0.0])      # pivot
R3 = 2.15                             # scene radius of the vertical circle


def integrate(q, dt=1e-3, t_max=3.0):
    """theta from the bottom, theta' from u^2 = q g r; RK4 on theta'' = -(g/r) sin theta.
    Returns t, theta, omega arrays up to t_max (we cut at slack / one circle later)."""
    u = np.sqrt(q * G * RP)
    def f(s):
        th, om = s
        return np.array([om, -(G / RP) * np.sin(th)])
    n = int(t_max / dt)
    t = np.linspace(0, t_max, n + 1)
    s = np.array([0.0, u / RP])
    TH = np.empty(n + 1); OM = np.empty(n + 1)
    TH[0], OM[0] = s
    for i in range(n):
        k1 = f(s); k2 = f(s + dt / 2 * k1); k3 = f(s + dt / 2 * k2); k4 = f(s + dt * k3)
        s = s + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        TH[i + 1], OM[i + 1] = s
    return t, TH, OM


def run_data(q):
    """Everything the animation needs for one launch: times, angles, T/mg, the slack
    instant (if any) and a projectile tail after it."""
    t, TH, OM = integrate(q)
    v2 = (RP * OM) ** 2
    Tmg = v2 / (G * RP) + np.cos(TH)          # T/(mg) = v^2/(gr) + cos(theta)
    slack = np.where(Tmg < -1e-6)[0]
    one_circle = np.where(TH >= 2 * np.pi)[0]
    if len(slack):
        i_end = slack[0]
        kind = "slack"
    elif len(one_circle):
        i_end = one_circle[0]
        kind = "circle"
    else:
        i_end = len(t) - 1
        kind = "end"
    d = dict(q=q, t=t[:i_end + 1], th=TH[:i_end + 1], Tmg=np.maximum(Tmg[:i_end + 1], 0), kind=kind)
    if kind == "slack":
        th_s, om_s = TH[i_end], OM[i_end]
        # position (physical, pivot at origin, theta from the bottom): (r sin th, -r cos th)
        pos = np.array([RP * np.sin(th_s), -RP * np.cos(th_s)])
        vel = RP * om_s * np.array([np.cos(th_s), np.sin(th_s)])     # tangent direction
        tp = np.linspace(0, 0.75, 200)
        px = pos[0] + vel[0] * tp
        py = pos[1] + vel[1] * tp - 0.5 * G * tp ** 2
        d.update(t_slack=t[i_end], th_slack=th_s, proj_t=tp, proj_x=px, proj_y=py)
    return d


def note(s, size=24, color=GREY):
    return Text(s, font=FONT, font_size=size, color=color)


class CircularMotionSeeItRun(Scene):
    def construct(self):
        # ============================================================ Act 1
        title = Text("Going round at constant speed is still accelerating", font=FONT,
                     font_size=36, color=TXT).to_edge(UP, buff=0.3)
        self.play(FadeIn(title), run_time=0.8)

        circ = Circle(radius=R, color=GREY, stroke_width=2).move_to(C)
        circ_d = DashedVMobject(circ, num_dashes=48)
        centre = Dot(C, radius=0.05, color=GREY)
        tt = ValueTracker(0.0)

        def pos():
            a = OMEGA * tt.get_value()
            return C + R * np.array([np.cos(a), np.sin(a), 0])

        def vhat():
            a = OMEGA * tt.get_value()
            return np.array([-np.sin(a), np.cos(a), 0])

        def rhat():
            a = OMEGA * tt.get_value()
            return np.array([np.cos(a), np.sin(a), 0])

        P = always_redraw(lambda: Dot(pos(), radius=0.11, color=BLUE))
        varr = always_redraw(lambda: Arrow(pos(), pos() + 1.35 * vhat(), buff=0, color=GREEN,
                                           stroke_width=5, max_tip_length_to_length_ratio=0.2))
        aarr = always_redraw(lambda: Arrow(pos(), pos() - 1.0 * rhat(), buff=0, color=AMBER,
                                           stroke_width=5, max_tip_length_to_length_ratio=0.25))
        vlab = always_redraw(lambda: MathTex("v", color=GREEN, font_size=40)
                             .move_to(pos() + 1.35 * vhat() + 0.32 * rhat()))
        alab = always_redraw(lambda: MathTex("a", color=AMBER, font_size=40)
                             .move_to(pos() - 1.0 * rhat() - 0.3 * vhat()))
        string = always_redraw(lambda: Line(C, pos(), color=GREY, stroke_width=1.5))

        self.play(Create(circ_d), FadeIn(centre), run_time=0.8)
        self.add(string, P, varr, aarr, vlab, alab)
        cap = note("velocity (green): always tangent.   acceleration (amber): always toward the centre.", 26, TXT)
        cap.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(cap), tt.animate.set_value(3.6), run_time=3.6, rate_func=lambda s: s)
        self.play(tt.animate.set_value(5.2), run_time=1.6, rate_func=lambda s: s)

        # hodograph: the velocity redrawn from one fixed origin
        hod_c = Circle(radius=VLEN, color=GREEN, stroke_width=1.5).move_to(H)
        hod_d = DashedVMobject(hod_c, num_dashes=40)
        hod_o = Dot(H, radius=0.05, color=GREY)
        hv = always_redraw(lambda: Arrow(H, H + VLEN * vhat(), buff=0, color=GREEN, stroke_width=5,
                                         max_tip_length_to_length_ratio=0.2))
        hv_lab = always_redraw(lambda: MathTex(r"\vec v", color=GREEN, font_size=38)
                               .move_to(H + (VLEN + 0.35) * vhat()))
        # the tip of v moves perpendicular to v — i.e. along -rhat: the acceleration direction
        tip_arr = always_redraw(lambda: Arrow(H + VLEN * vhat(), H + VLEN * vhat() - 0.8 * rhat(),
                                              buff=0, color=AMBER, stroke_width=4,
                                              max_tip_length_to_length_ratio=0.3))
        hod_title = note("the same v, redrawn from one fixed origin", 22, GREEN).next_to(hod_d, UP, buff=0.25)
        self.play(Create(hod_d), FadeIn(hod_o), FadeIn(hod_title), run_time=0.8)
        self.add(hv, hv_lab, tip_arr)
        cap2 = note("the same v, drawn from one fixed point: its tip circles at the same ω — at speed v·ω", 26, TXT)
        cap2.to_edge(DOWN, buff=0.4)
        self.play(Transform(cap, cap2), tt.animate.set_value(9.4), run_time=4.2, rate_func=lambda s: s)

        eq = VGroup(
            MathTex(r"a = \frac{|\Delta \vec v|}{\Delta t} = v\,\omega = \frac{v^2}{r} = r\omega^2", font_size=36, color=AMBER),
            note("and the tip moves at right angles to v — toward the centre", 19, GREY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(hod_d, DOWN, buff=0.25)
        eq.set_x(H[0])
        self.play(Write(eq[0]), tt.animate.set_value(11.8), run_time=2.4, rate_func=lambda s: s)
        self.play(FadeIn(eq[1]), tt.animate.set_value(14.6), run_time=2.8, rate_func=lambda s: s)
        cap3 = note("the force never changes the speed — it only turns the velocity", 26, TXT)
        cap3.to_edge(DOWN, buff=0.4)
        self.play(Transform(cap, cap3), tt.animate.set_value(17.8), run_time=3.2, rate_func=lambda s: s)
        self.wait(0.8)

        # ============================================================ Act 2 — cut the string
        self.play(FadeOut(hod_d), FadeOut(hod_o), FadeOut(hod_title), FadeOut(hv), FadeOut(hv_lab),
                  FadeOut(tip_arr), FadeOut(eq), run_time=0.6)
        title2 = Text("Cut the string", font=FONT, font_size=36, color=TXT).to_edge(UP, buff=0.3)
        self.play(Transform(title, title2), tt.animate.set_value(18.3), run_time=1.0, rate_func=lambda s: s)
        self.wait(0.6)
        # freeze the release point
        t_rel = tt.get_value()
        a_rel = OMEGA * t_rel
        p_rel = C + R * np.array([np.cos(a_rel), np.sin(a_rel), 0])
        v_rel = np.array([-np.sin(a_rel), np.cos(a_rel), 0])
        r_rel = np.array([np.cos(a_rel), np.sin(a_rel), 0])
        for m in (P, varr, aarr, vlab, alab, string):
            m.clear_updaters()
        self.remove(aarr, alab, string, varr, vlab)
        ghost_string = DashedLine(C, p_rel, color=GREY, stroke_width=1.5)
        s2 = ValueTracker(0.0)
        P2 = always_redraw(lambda: Dot(p_rel + s2.get_value() * v_rel, radius=0.11, color=BLUE))
        v2arr = always_redraw(lambda: Arrow(p_rel + s2.get_value() * v_rel,
                                            p_rel + s2.get_value() * v_rel + 1.35 * v_rel, buff=0,
                                            color=GREEN, stroke_width=5, max_tip_length_to_length_ratio=0.2))
        wrong = Arrow(p_rel, p_rel + 1.6 * r_rel, buff=0, color=RED, stroke_width=4,
                      max_tip_length_to_length_ratio=0.2)
        wrong_lab = note("not outward", 22, RED).next_to(wrong.get_end(), RIGHT if r_rel[0] > 0 else LEFT, buff=0.15)
        tangent = DashedLine(p_rel - 0.3 * v_rel, p_rel + 4.2 * v_rel, color=GREEN, stroke_width=1.5)
        self.remove(P)
        self.add(ghost_string, tangent, P2, v2arr)
        cap4 = note("no force, no turning: it flies straight along the tangent — not outward", 26, TXT)
        cap4.to_edge(DOWN, buff=0.4)
        self.play(Transform(cap, cap4), FadeIn(wrong), FadeIn(wrong_lab), run_time=0.6)
        self.play(s2.animate.set_value(3.4), run_time=3.2, rate_func=lambda s: s)
        self.play(Transform(wrong, wrong.copy().set_opacity(0.25)), wrong_lab.animate.set_opacity(0.25), run_time=0.5)
        self.wait(2.0)

        # ============================================================ Act 3 — the vertical circle
        self.play(FadeOut(ghost_string), FadeOut(tangent), FadeOut(P2), FadeOut(v2arr), FadeOut(wrong),
                  FadeOut(wrong_lab), FadeOut(circ_d), FadeOut(centre), FadeOut(cap), run_time=0.7)
        title3 = Text("A vertical circle on a string — three launches from the bottom",
                      font=FONT, font_size=34, color=TXT).to_edge(UP, buff=0.3)
        self.play(Transform(title, title3), run_time=0.6)

        pivot = Dot(O3, radius=0.06, color=GREY)
        vcirc = DashedVMobject(Circle(radius=R3, color=GREY, stroke_width=1.5).move_to(O3), num_dashes=48)
        gl = Arrow(np.array([-0.9, 1.9, 0]), np.array([-0.9, 0.9, 0]), buff=0, color=GREY, stroke_width=3,
                   max_tip_length_to_length_ratio=0.3)
        glab = MathTex("g", color=GREY, font_size=36).next_to(gl, RIGHT, buff=0.1)
        self.play(FadeIn(pivot), Create(vcirc), FadeIn(gl), FadeIn(glab), run_time=0.8)

        # readout panel (right)
        panel_x = 3.2
        bar_base = np.array([5.9, -2.6, 0.0])
        bar_frame = Rectangle(width=0.5, height=3.6, color=GREY, stroke_width=1.5).move_to(bar_base + np.array([0, 1.8, 0]))
        bar_lab = note("T / mg", 22, TXT).next_to(bar_frame, DOWN, buff=0.12)
        zero_tick = Line(bar_base + np.array([-0.35, 0, 0]), bar_base + np.array([0.35, 0, 0]), color=GREY, stroke_width=2)
        self.add(bar_frame, bar_lab, zero_tick)

        runs = [(4.0, AMBER, "u² = 4gr", "tension hits zero at 132° — the string goes slack and the particle flies off as a projectile"),
                (5.0, GREEN, "u² = 5gr", "tension grazes zero exactly at the top — just complete"),
                (6.0, BLUE, "u² = 6gr", "round with a margin — T at the top is mg, and T_bottom − T_top = 6mg for every launch")]

        for q, col, name, cap_txt in runs:
            d = run_data(q)
            tr = ValueTracker(0.0)

            def th_now(d=d, tr=tr):
                return float(np.interp(tr.get_value(), d["t"], d["th"]))

            def T_now(d=d, tr=tr):
                return float(np.interp(tr.get_value(), d["t"], d["Tmg"]))

            def p_now(d=d, tr=tr):
                th = th_now(d, tr)
                return O3 + R3 * np.array([np.sin(th), -np.cos(th), 0])

            run_lab = note(name, 30, col).move_to(np.array([panel_x, 2.3, 0]))
            T_num = DecimalNumber(0, num_decimal_places=2, color=col, font_size=40)
            T_num.add_updater(lambda m, T_now=T_now: m.set_value(T_now()))
            T_row = VGroup(note("tension  T / mg  =", 24, TXT), T_num).arrange(RIGHT, buff=0.2)
            T_row.move_to(np.array([panel_x, 1.5, 0]))
            th_num = Integer(0, color=TXT, font_size=36)
            th_num.add_updater(lambda m, th_now=th_now: m.set_value(int(round(np.degrees(th_now()) % 360))))
            th_row = VGroup(note("angle from the bottom  θ  =", 24, TXT), th_num, note("°", 24, TXT)).arrange(RIGHT, buff=0.12)
            th_row.move_to(np.array([panel_x, 0.8, 0]))
            bar = always_redraw(lambda col=col, T_now=T_now: Rectangle(
                width=0.42, height=max(0.5 * T_now(), 0.001), color=col, fill_color=col, fill_opacity=0.85,
                stroke_width=0).move_to(bar_base + np.array([0, 0.25 * T_now(), 0])))

            string3 = always_redraw(lambda p_now=p_now: Line(O3, p_now(), color=col, stroke_width=3))
            ball = always_redraw(lambda p_now=p_now: Dot(p_now(), radius=0.12, color=col))
            trail = VMobject(color=col, stroke_width=2, stroke_opacity=0.5)
            trail.set_points_as_corners([p_now(), p_now()])

            def trail_upd(m, p_now=p_now):
                pts = m.get_points()
                m.add_points_as_corners([p_now()])
            trail.add_updater(trail_upd)

            cap_run = note(cap_txt, 25, TXT).to_edge(DOWN, buff=0.4)
            self.add(bar, string3, ball, trail)
            self.play(FadeIn(run_lab), FadeIn(T_row), FadeIn(th_row), FadeIn(cap_run), run_time=0.6)
            self.wait(1.8)
            self.play(tr.animate.set_value(d["t"][-1]), run_time=SLOW * d["t"][-1], rate_func=lambda s: s)

            if d["kind"] == "slack":
                # freeze the string as a slack dashed line and send the particle along its parabola
                string3.clear_updaters(); ball.clear_updaters(); trail.clear_updaters()
                T_num.clear_updaters(); th_num.clear_updaters()
                self.remove(string3)
                slack_line = DashedLine(O3, p_now(), color=col, stroke_width=2)
                self.add(slack_line)
                pt = ValueTracker(0.0)

                def proj_pos(d=d, pt=pt):
                    x = float(np.interp(pt.get_value(), d["proj_t"], d["proj_x"]))
                    y = float(np.interp(pt.get_value(), d["proj_t"], d["proj_y"]))
                    return O3 + R3 * np.array([x, y, 0])     # physical r = 1 -> scene R3
                self.remove(ball)
                ball_p = always_redraw(lambda proj_pos=proj_pos: Dot(proj_pos(), radius=0.12, color=col))
                path_p = VMobject(color=col, stroke_width=2, stroke_opacity=0.5)
                path_p.set_points_as_corners([proj_pos(), proj_pos()])
                path_p.add_updater(lambda m, proj_pos=proj_pos: m.add_points_as_corners([proj_pos()]))
                slack_lab = note("slack — T = 0", 24, col).next_to(p_now(), UP, buff=0.25)
                self.add(ball_p, path_p)
                self.play(FadeIn(slack_lab), pt.animate.set_value(d["proj_t"][-1]),
                          run_time=SLOW * d["proj_t"][-1], rate_func=lambda s: s)
                self.wait(2.2)
                self.play(FadeOut(ball_p), FadeOut(path_p), FadeOut(slack_line), FadeOut(slack_lab),
                          FadeOut(trail), FadeOut(run_lab), FadeOut(T_row), FadeOut(th_row), FadeOut(cap_run),
                          FadeOut(bar), run_time=0.6)
            else:
                self.wait(2.2)
                string3.clear_updaters(); ball.clear_updaters(); trail.clear_updaters()
                T_num.clear_updaters(); th_num.clear_updaters()
                self.play(FadeOut(string3), FadeOut(ball), FadeOut(trail), FadeOut(run_lab), FadeOut(T_row),
                          FadeOut(th_row), FadeOut(cap_run), FadeOut(bar), run_time=0.6)

        coda = VGroup(
            note("Complete circles on a string:  v_top² ≥ gr,  i.e.  u² ≥ 5gr.", 26, GREEN),
            note("On a rod or inside a tube only v_top ≥ 0 is needed:  u² ≥ 4gr.", 24, GREY),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(coda), FadeOut(bar_frame), FadeOut(bar_lab), FadeOut(zero_tick), run_time=0.8)
        self.wait(4.0)
