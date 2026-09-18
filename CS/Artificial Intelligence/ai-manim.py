"""
ai-manim.py — two scenes for [[Artificial Intelligence]].

Scene 1  NetworkLearns  — a 2–10–10–10–1 network trained live on the two-spiral data; its
                          decision map redrawn every few epochs while the loss counter falls:
                          back propagation, watched.
Scene 2  AgentLearns    — Q-learning on the 5×5 grid: early episodes wander and fall in the
                          pit; the arrows firm up; the final greedy path is walked.

Smoke:   manim -ql --fps 15 ai-manim.py NetworkLearns AgentLearns
Final:   manim -qk ai-manim.py NetworkLearns AgentLearns
then concat with ffmpeg to ai-manim.mp4 and rm -rf media __pycache__.
"""
from manim import *
import numpy as np
import math

GREY = "#888888"
BLUE_, RED_, GREEN_, AMBER, PURPLE_, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"


def spiral(n=300, seed=1, turns=3.0):
    r = np.random.default_rng(seed); t = np.linspace(0.3, 3.5, n)
    x1 = np.c_[t * np.cos(turns * t), t * np.sin(turns * t)] + r.normal(0, 0.12, (n, 2))
    x2 = np.c_[t * np.cos(turns * t + math.pi), t * np.sin(turns * t + math.pi)] + r.normal(0, 0.12, (n, 2))
    return np.vstack([x1, x2]) / 3.5, np.vstack([np.zeros((n, 1)), np.ones((n, 1))])

def sigmoid(z): return 1 / (1 + np.exp(-z))

class Net:
    def __init__(self, hidden, seed=7):
        r = np.random.default_rng(seed); sizes = [2] + hidden + [1]
        self.W = [r.normal(0, 1 / math.sqrt(a), (a, b)) for a, b in zip(sizes[:-1], sizes[1:])]
        self.B = [np.zeros((1, b)) for b in sizes[1:]]
        self.vW = [np.zeros_like(w) for w in self.W]; self.vB = [np.zeros_like(b) for b in self.B]
    def forward(self, X):
        acts = [X]
        for i, (w, b) in enumerate(zip(self.W, self.B)):
            z = acts[-1] @ w + b; acts.append(sigmoid(z) if i == len(self.W) - 1 else np.tanh(z))
        return acts
    def step(self, X, Y, lr=0.05, mom=0.9):
        acts = self.forward(X); out = acts[-1]
        delta = 2 * (out - Y) / len(X) * out * (1 - out)
        for i in reversed(range(len(self.W))):
            gW = acts[i].T @ delta; gB = delta.sum(0, keepdims=True)
            if i > 0: delta = (delta @ self.W[i].T) * (1 - acts[i] ** 2)
            self.vW[i] = mom * self.vW[i] - lr * gW; self.vB[i] = mom * self.vB[i] - lr * gB
            self.W[i] += self.vW[i]; self.B[i] += self.vB[i]
        return float(((out - Y) ** 2).mean())


class NetworkLearns(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("Back propagation, watched — a 2·10·10·10·1 network learning the two spirals", font_size=28, color=GREY).to_edge(UP, buff=0.25)
        self.play(FadeIn(title))
        X, Y = spiral(); net = Net([10, 10, 10])
        g = np.linspace(-1.1, 1.1, 120); GX, GY = np.meshgrid(g, g); G = np.c_[GX.ravel(), GY.ravel()]
        side = 5.2; centre = np.array([-1.6, -0.3, 0])
        def img_from(pred):
            p = pred.reshape(GX.shape)
            rgb = np.zeros((*p.shape, 3), dtype=np.uint8)
            rgb[..., 0] = (40 + 170 * p).astype(np.uint8); rgb[..., 1] = 40; rgb[..., 2] = (40 + 170 * (1 - p)).astype(np.uint8)
            im = ImageMobject(rgb[::-1]); im.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
            im.stretch_to_fit_width(side).stretch_to_fit_height(side).move_to(centre)
            return im
        pic = img_from(net.forward(G)[-1].ravel()); self.add(pic)
        dots = VGroup(*[Dot(centre + np.array([x * side / 2.2, y * side / 2.2, 0]), radius=0.035, color=(BLUE_ if yy == 0 else RED_)) for (x, y), yy in zip(X, Y.ravel())])
        self.add(dots)
        # loss curve axes on the right
        ax = Axes(x_range=[0, 8000, 2000], y_range=[0, 0.3, 0.1], x_length=4.6, y_length=3.2, axis_config={"color": GREY, "include_tip": False, "font_size": 18}).move_to([3.6, -0.2, 0])
        ax.add_coordinates()
        self.add(ax, Text("epoch", font_size=18, color=GREY).next_to(ax.x_axis, DOWN, buff=0.15), Text("loss", font_size=18, color=GREY).next_to(ax.y_axis, LEFT, buff=0.1).shift(UP * 1.2))
        counter = Text("epoch 0    loss —", font_size=22, color=AMBER).to_edge(DOWN, buff=0.3)
        self.add(counter)
        losses = []; pts = []
        epoch = 0
        schedule = [50] * 20 + [100] * 20 + [50] * 40 + [100] * 30   # 1000 + 2000 + 2000 + 3000 = 8000 epochs; the fine steps sit where the loss falls
        for n in schedule:
            for _ in range(n):
                losses.append(net.step(X, Y)); epoch += 1
            newpic = img_from(net.forward(G)[-1].ravel())
            pts.append(ax.c2p(epoch, min(losses[-1], 0.3)))
            curve = VMobject(color=PURPLE_, stroke_width=3).set_points_as_corners(pts) if len(pts) > 1 else VMobject()
            newcounter = Text(f"epoch {epoch}    loss {losses[-1]:.4f}", font_size=22, color=AMBER).to_edge(DOWN, buff=0.3)
            self.remove(pic); pic = newpic; self.add(pic); self.add(dots)
            self.remove(counter); counter = newcounter; self.add(counter)
            if len(pts) > 1:
                self.add(curve)
            self.wait(0.2)
            if len(pts) > 1: self.remove(curve)
        self.add(VMobject(color=PURPLE_, stroke_width=3).set_points_as_corners(pts))
        cap = Text("every frame: compare outputs with the labels, send the error's gradient backwards, nudge every weight — 8000 times", font_size=18, color=GREY).next_to(counter, UP, buff=0.12)
        self.play(FadeIn(cap)); self.wait(1.5)


class AgentLearns(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("Reinforcement learning — no labels, only reward: Q-learning on a grid with a pit", font_size=28, color=GREY).to_edge(UP, buff=0.25)
        self.play(FadeIn(title))
        N = 5; goal = (4, 4); pit = (2, 2); cell = 0.95; origin = np.array([-2.2 - 2 * cell, 1.6 + 0.2, 0])
        def P(r, c): return origin + np.array([c * cell, -r * cell, 0])
        grid = VGroup()
        for r in range(N):
            for c in range(N):
                sq = Square(cell, color=GREY, stroke_width=1).move_to(P(r, c))
                if (r, c) == goal: sq.set_fill(GREEN_, 0.4)
                if (r, c) == pit: sq.set_fill(RED_, 0.4)
                grid.add(sq)
        self.add(grid, Text("+10", font_size=18, color=GREY).move_to(P(*goal)), Text("−10", font_size=18, color=GREY).move_to(P(*pit)))
        Q = np.zeros((N, N, 4)); moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        alpha, gamma, eps = 0.5, 0.9, 0.2
        rng = np.random.default_rng(4)
        def step(s, a):
            r, c = s; dr, dc = moves[a]
            n = (min(max(r + dr, 0), N - 1), min(max(c + dc, 0), N - 1))
            if n == goal: return n, 10.0, True
            if n == pit: return n, -10.0, True
            return n, -1.0, False
        def arrows():
            g = VGroup()
            for r in range(N):
                for c in range(N):
                    if (r, c) in (goal, pit): continue
                    if Q[r, c].max() == 0 and Q[r, c].min() == 0: continue
                    a = int(np.argmax(Q[r, c])); dr, dc = moves[a]
                    conf = min(1.0, (Q[r, c].max() - Q[r, c].min()) / 8)
                    g.add(Arrow(P(r, c) - np.array([dc, -dr, 0]) * 0.25, P(r, c) + np.array([dc, -dr, 0]) * 0.28, buff=0, color=TEAL, stroke_width=3, max_tip_length_to_length_ratio=0.35).set_opacity(0.3 + 0.7 * conf))
            return g
        agent = Dot(P(0, 0), radius=0.16, color=AMBER); self.add(agent)
        label = Text("episode 0", font_size=22, color=AMBER).move_to([3.4, 1.2, 0]); self.add(label)
        note = Text("reward: −1 per step, +10 at the goal, −10 in the pit\nthe agent knows none of it in advance", font_size=18, color=GREY, line_spacing=0.9).move_to([3.4, 0.0, 0]); self.add(note)
        arr = arrows(); self.add(arr)
        shown = {0, 1, 2, 5, 10, 20, 40, 80, 150, 300, 599}
        for ep in range(600):
            s = (0, 0); done = False; path = [s]
            while not done and len(path) < 60:
                a = rng.integers(4) if rng.random() < eps else int(np.argmax(Q[s]))
                n, rew, done = step(s, a)
                Q[s][a] += alpha * (rew + gamma * (0 if done else Q[n].max()) - Q[s][a]); s = n; path.append(s)
            if ep in shown:
                self.remove(label); label = Text(f"episode {ep + 1}", font_size=22, color=AMBER).move_to([3.4, 1.2, 0]); self.add(label)
                agent.move_to(P(0, 0))
                for s_ in path[1:]:
                    self.play(agent.animate.move_to(P(*s_)), run_time=0.08 if ep < 40 else 0.12, rate_func=linear)
                self.remove(arr); arr = arrows(); self.add(arr)
                self.wait(0.2)
        cap = Text("after 600 episodes: the arrows are the policy, the bright path is the 8-step route that skirts the pit", font_size=18, color=GREY).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(cap)); self.wait(1.5)
