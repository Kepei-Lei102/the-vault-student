"""Manim scenes for [[Automated Systems and Robotics]].
Scene 1  RoomRobot   — the exam's robot: sensor reading → compare with 10 cm → actuator.
                       Always-turn-right traces one loop; bounce covers the room.
Scene 2  SensorVote  — one glitching sensor stops the machine; three that vote do not.
Smoke:  manim -ql --fps 15 automated-systems-manim.py RoomRobot SensorVote
Final:  manim -qk automated-systems-manim.py RoomRobot SensorVote   then concat with ffmpeg."""
import numpy as np
from manim import *

GREY_T, BLUE_H, PURPLE_H, GREEN_H, RED_H, AMBER_H = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b"
W, H, CELL, STEP = 40, 30, 10, 2.0


def make_room():
    room = np.zeros((H, W), dtype=bool)
    room[0, :] = room[-1, :] = True; room[:, 0] = room[:, -1] = True
    room[8:12, 10:14] = True; room[18:26, 24:27] = True; room[4:6, 28:36] = True
    return room


def sensor(room, x, y, th, max_cm=400):
    c, s = np.cos(th), np.sin(th)
    for r in np.arange(1.0, max_cm, 1.0):
        if room[int((y + r * s) // CELL), int((x + r * c) // CELL)]:
            return r
    return max_cm


def simulate(policy, ticks, seed=7):
    rng = np.random.default_rng(seed)
    room = make_room(); x, y, th = 205.0, 155.0, 0.0
    out = []
    for _ in range(ticks):
        r = sensor(room, x, y, th)
        turned = r <= 10
        if turned:
            th = th + np.pi / 2 if policy == "right" else th + rng.uniform(np.pi / 2, 3 * np.pi / 2)
        else:
            x, y = x + STEP * np.cos(th), y + STEP * np.sin(th)
        out.append((x, y, th, r, turned))
    return room, out


class RoomRobot(Scene):
    def construct(self):
        title = Text("The exam's robot: forward until the sensor reads 10 cm or less, then turn", font_size=24, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        room, _ = simulate("right", 1)
        SC = 0.019  # scene units per cm  → room 7.6 × 5.7
        origin = np.array([-3.8, 2.35, 0])
        def P(x, y):
            return origin + np.array([x * SC, -y * SC, 0])
        walls = VGroup()
        ys, xs = np.where(room)
        for cx, cy in zip(xs, ys):
            walls.add(Square(side_length=CELL * SC, color=GREY_T, fill_color=GREY_T, fill_opacity=0.35, stroke_width=0).move_to(P(cx * CELL + 5, cy * CELL + 5)))
        self.add(walls)
        status = VGroup().to_edge(DOWN, buff=0.3)
        for policy, label, col, ticks, per_frame in [("right", "rule: always turn right 90°", RED_H, 1300, 6), ("bounce", "rule: turn by a random angle", GREEN_H, 4200, 14)]:
            _, run = simulate(policy, ticks)
            tag = Text(label, font_size=22, color=col).next_to(title, DOWN, buff=0.12)
            self.add(tag)
            bot = Dot(P(run[0][0], run[0][1]), radius=0.08, color=BLUE_H)
            beam = Line(bot.get_center(), bot.get_center(), color=AMBER_H, stroke_width=2)
            trail = VMobject(color=col, stroke_width=1.5); trail.set_points_as_corners([bot.get_center(), bot.get_center()])
            readout = Text("", font_size=20, color=GREY_T).to_edge(DOWN, buff=0.3)
            self.add(trail, beam, bot, readout)
            pts = [bot.get_center()]
            i = 0
            last_turn = -100
            while i < len(run):
                x, y, th, r, turned = run[i]
                pts.append(P(x, y)); trail.set_points_as_corners(pts)
                bot.move_to(P(x, y))
                beam.put_start_and_end_on(P(x, y), P(x + min(r, 400) * np.cos(th), y + min(r, 400) * np.sin(th)))
                if turned:
                    last_turn = i
                    msg, mcol = f"sensor: {r:.0f} cm   ≤ 10   →   actuator: turn", col
                else:
                    msg, mcol = f"sensor: {r:.0f} cm   > 10   →   actuator: forward", GREY_T
                newr = Text(msg, font_size=20, color=mcol).to_edge(DOWN, buff=0.3)
                readout.become(newr)
                self.wait(1 / 15)
                i += 1 if turned or i - last_turn < 3 else per_frame
            self.wait(1.0)
            self.remove(tag, trail, beam, bot, readout)
        end = Text("same sensor, same microprocessor, same actuator: only the program differs", font_size=22, color=GREY_T).next_to(title, DOWN, buff=0.12)
        self.add(end); self.wait(2)


class SensorVote(Scene):
    def construct(self):
        title = Text("One sensor believes every glitch; three that vote do not", font_size=24, color=GREY_T).to_edge(UP, buff=0.25)
        self.add(title)
        rng = np.random.default_rng(3)
        n = 240
        readings = 50 + 2 * rng.standard_normal((3, n))
        glitch_at = {0: [60, 150], 1: [105], 2: [190]}
        for s, idxs in glitch_at.items():
            for j in idxs:
                readings[s, j] = 5
        ax = Axes(x_range=[0, n, 60], y_range=[0, 60, 10], x_length=8.5, y_length=3.6, axis_config={"color": GREY_T, "include_tip": False, "font_size": 18}).shift(DOWN * 0.3 + LEFT * 1.4)
        ax.add(Text("reading (cm)", font_size=16, color=GREY_T).next_to(ax.y_axis, UP, buff=0.1))
        ax.add(Text("time (readings at 100 per second)", font_size=16, color=GREY_T).next_to(ax.x_axis, DOWN, buff=0.15))
        thr = DashedLine(ax.c2p(0, 10), ax.c2p(n, 10), color=AMBER_H, stroke_width=2)
        self.add(ax, thr, Text("stored value: 10 cm", font_size=16, color=AMBER_H).next_to(thr, UP, buff=0.05).shift(RIGHT * 3))
        cols = [BLUE_H, PURPLE_H, GREEN_H]
        lines = [VMobject(color=c, stroke_width=1.8) for c in cols]
        panel = VGroup(Text("one sensor:", font_size=20, color=GREY_T), Text("false stops: 0", font_size=20, color=RED_H),
                       Text("three, majority:", font_size=20, color=GREY_T), Text("false stops: 0", font_size=20, color=GREEN_H)).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(RIGHT, buff=0.3).shift(UP * 0.4)
        self.add(panel, *lines)
        one = vote = 0
        for j in range(1, n):
            for s in range(3):
                lines[s].set_points_as_corners([ax.c2p(k, readings[s, k]) for k in range(j + 1)])
            below = (readings[:, j] <= 10)
            if below[0]:
                one += 1
                panel[1].become(Text(f"false stops: {one}", font_size=20, color=RED_H).move_to(panel[1], aligned_edge=LEFT))
                self.add(Text("STOP", font_size=18, color=RED_H).move_to(ax.c2p(j, 55)))
            if below.sum() >= 2:
                vote += 1
                panel[3].become(Text(f"false stops: {vote}", font_size=20, color=GREEN_H).move_to(panel[3], aligned_edge=LEFT))
            self.wait(1 / 30)
        end = Text("the first sensor alone stopped the machine twice for nothing; the vote never did", font_size=20, color=GREY_T).to_edge(DOWN, buff=0.25)
        self.add(end); self.wait(2.5)
