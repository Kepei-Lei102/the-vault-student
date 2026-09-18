"""Figures for [[Automated Systems and Robotics]].  Run automated-systems-sim.py first
(it saves the robot paths to $VAULT_SCRATCH); then  python3 automated-systems-figures.py
Every SVG: text #888, width=100%, no background, checked in light and dark."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

S = os.environ.get("VAULT_SCRATCH", "/tmp")
GREY, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": GREY, "axes.labelcolor": GREY, "xtick.color": GREY,
                     "ytick.color": GREY, "axes.edgecolor": GREY, "svg.fonttype": "none", "font.size": 9.5})


def style(ax):
    ax.set_facecolor("none")
    for sp in ax.spines.values():
        sp.set_color(GREY)


def save(fig, name):
    fig.patch.set_alpha(0)
    fig.savefig(name, format="svg", bbox_inches="tight", transparent=True)
    plt.close(fig)
    txt = open(name).read()
    txt = txt.replace('width="', 'data-w="', 1).replace('height="', 'data-h="', 1)
    txt = txt.replace("<svg ", '<svg width="100%" ', 1)
    open(name, "w").write(txt)


def box(ax, xy, w, h, text, col, fs=10):
    ax.add_patch(FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.02,rounding_size=0.06", fc=col + "26", ec=col, lw=1.6))
    ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center", fontsize=fs, color=GREY, linespacing=1.4)


def arrow(ax, a, b, col, text=None, rad=0.0, tpos=0.5, toff=(0, 0.14), fs=8.5):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=14, color=col, lw=1.6, connectionstyle=f"arc3,rad={rad}"))
    if text:
        mx, my = a[0] + tpos * (b[0] - a[0]) + toff[0], a[1] + tpos * (b[1] - a[1]) + toff[1]
        ax.text(mx, my, text, ha="center", va="center", fontsize=fs, color=col)


# 1. the collaboration: sensor → microprocessor → actuator → the world → sensor
fig, ax = plt.subplots(figsize=(10, 4.6)); style(ax); ax.set_xlim(0, 10); ax.set_ylim(0, 4.6); ax.axis("off")
box(ax, (0.4, 2.4), 2.2, 1.3, "SENSOR\nmeasures a physical\nquantity, sends digitised\ndata continuously", BLUE, 9)
box(ax, (3.9, 2.4), 2.4, 1.3, "MICROPROCESSOR\ncompares the reading\nwith a stored value;\ndecides", PURPLE, 9)
box(ax, (7.4, 2.4), 2.2, 1.3, "ACTUATOR\nturns the decision\ninto a physical action:\nmotor, valve, heater", GREEN, 9)
box(ax, (3.6, 0.3), 3.0, 1.0, "THE WORLD\nwater level · distance · temperature · position", AMBER, 9)
arrow(ax, (2.6, 3.05), (3.9, 3.05), BLUE, "digitised data", toff=(0, 0.2))
arrow(ax, (6.3, 3.05), (7.4, 3.05), PURPLE, "signal", toff=(0, 0.2))
arrow(ax, (8.5, 2.4), (6.6, 1.1), GREEN, "changes it", rad=-0.25, toff=(0.55, -0.1))
arrow(ax, (3.6, 1.1), (1.5, 2.4), AMBER, "is measured again", rad=-0.25, toff=(-0.75, -0.1))
ax.text(5.1, 4.3, "An automated system: sensor, microprocessor and actuator in collaboration, and no human in the ring", ha="center", fontsize=10.5, color=GREY)
ax.text(5.1, 1.95, "the ring runs again and again until the system is switched off", ha="center", fontsize=8.5, color=GREY, style="italic")
save(fig, "automated-systems-loop.svg")

# 2. what makes a robot a robot: three layers, and the smart speaker that fails two of them
fig, ax = plt.subplots(figsize=(10, 4.8)); style(ax); ax.set_xlim(0, 10); ax.set_ylim(0, 4.8); ax.axis("off")
layers = [("PROGRAMMABLE", "instructions it follows, and that can be changed", PURPLE),
          ("ELECTRICAL COMPONENTS", "sensors · microprocessor · actuators", BLUE),
          ("MECHANICAL STRUCTURE", "a framework: arm, chassis, wheels, rotors, joints", AMBER)]
for i, (t, sub, col) in enumerate(layers):
    y = 0.5 + i * 1.25
    box(ax, (0.5, y), 4.2, 1.0, f"{t}\n{sub}", col, 9.5)
    ax.text(0.25, y + 0.5, "yes", ha="center", va="center", fontsize=9, color=GREEN)
ax.text(2.6, 4.35, "a robot: all three layers,\nwhether it steers itself or a person steers it", ha="center", va="center", fontsize=10, color=GREY)
# the speaker
verdict = [("PROGRAMMABLE", "voice commands, updates", PURPLE, "yes"),
           ("ELECTRICAL COMPONENTS", "microphone · microprocessor · but no actuator", BLUE, "half"),
           ("MECHANICAL STRUCTURE", "a case is not a framework; nothing moves", AMBER, "no")]
for i, (t, sub, col, v) in enumerate(verdict):
    y = 0.5 + i * 1.25
    box(ax, (5.6, y), 4.0, 1.0, f"{t}\n{sub}", col, 9.5)
    ax.text(9.85, y + 0.5, v, ha="center", va="center", fontsize=9, color=GREEN if v == "yes" else RED)
ax.text(7.6, 4.35, "a smart speaker: programmable,\nbut no framework and no actuator, so not a robot", ha="center", va="center", fontsize=10, color=GREY)
ax.text(5.15, 0.15, "movement is the tell: a robot can act on the physical world; a speaker can only talk to you", ha="center", fontsize=8.5, color=GREY, style="italic")
save(fig, "automated-systems-robot-anatomy.svg")

# 3. the exam's robot in a room: fixed rule vs bounce
room = np.load(f"{S}/robot-room.npy")
paths = [("always turn right 90°: a 12.5 m loop, forever — 14.5 % of the floor", np.load(f"{S}/robot-path-always.npy"), RED),
         ("bounce at a random angle: 300 m of travel — about 90 % of the floor", np.load(f"{S}/robot-path-bounce.npy"), GREEN)]
fig, axes = plt.subplots(1, 2, figsize=(12, 4.9))
for ax, (title, path, col) in zip(axes, paths):
    style(ax)
    ys, xs = np.where(room)
    ax.scatter(xs * 10 + 5, ys * 10 + 5, s=14, marker="s", color=GREY, alpha=0.55, lw=0)
    ax.plot(path[:, 0], path[:, 1], color=col, lw=0.7, alpha=0.75)
    ax.plot(path[0, 0], path[0, 1], "o", color=BLUE, ms=6)
    ax.set_xlim(0, 400); ax.set_ylim(300, 0); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(title, fontsize=9.5)
fig.suptitle("The same sensor, microprocessor and actuator; only the rule in the program differs", fontsize=10.5, color=GREY)
fig.tight_layout(); save(fig, "automated-systems-coverage.svg")

# 4. one sensor vs a vote
p = np.logspace(-4, -1.5, 60); n = 360000
fig, ax = plt.subplots(figsize=(8, 4.4)); style(ax)
ax.loglog(p, n * p, color=RED, lw=2, label="one sensor: n·p")
ax.loglog(p, n * p**2, color=BLUE, lw=2, label="two sensors, both must agree: n·p²")
ax.loglog(p, n * 3 * p**2, color=GREEN, lw=2, label="three sensors, majority of two: 3n·p²")
ax.scatter([1e-3, 1e-3, 1e-3], [362.6, 0.50, 1.15], color=[RED, BLUE, GREEN], zorder=5, s=30, label="simulated, p = 0.001")
ax.axhline(1, color=GREY, lw=0.8, ls=":"); ax.text(1.2e-4, 1.25, "one false stop an hour", fontsize=8, color=GREY)
ax.set_xlabel("probability that a single reading glitches, p"); ax.set_ylabel("false stops per hour  (100 readings/s)")
ax.set_title("A glitch that one sensor believes, two sensors must both suffer at the same instant", fontsize=10)
ax.legend(frameon=False, fontsize=8.5, labelcolor=GREY)
fig.tight_layout(); save(fig, "automated-systems-voting.svg")

# 5. timeline
events = [(1920, "R.U.R. — Čapek's play\ncoins 'robot' (robota: drudgery)", AMBER, 1),
          (1961, "Unimate at General Motors:\nthe first industrial robot, die-casting", BLUE, -1),
          (1969, "Stanford Arm: six joints,\nelectric, computer-controlled", BLUE, 1),
          (1997, "Sojourner drives on Mars,\ncommands ten minutes old", PURPLE, -1),
          (2000, "da Vinci surgical robot\napproved: the surgeon at a console", GREEN, 1),
          (2002, "Roomba: bounce and spiral\nin a million living rooms", GREEN, -1),
          (2011, "Fukushima: the robots sent in\nfail on stairs and radiation", RED, 1),
          (2012, "Amazon buys Kiva: shelves\nthat walk to the picker", BLUE, -1),
          (2016, "Zipline drones deliver\nblood to Rwandan clinics", GREEN, 1),
          (2019, "737 MAX grounded: one sensor,\nan automated system, 346 dead", RED, -1),
          (2023, "cobots and warehouse fleets\nnumber in the millions", TEAL, 1)]
fig, ax = plt.subplots(figsize=(12, 4.6)); style(ax); ax.axis("off"); ax.set_xlim(1912, 2034); ax.set_ylim(-3.4, 3.4)
ax.plot([1915, 2030], [0, 0], color=GREY, lw=1.2)
ups = [e for e in events if e[3] > 0]; downs = [e for e in events if e[3] < 0]
for group in (ups, downs):
    slots = np.linspace(1922, 2024, len(group))
    for (yr, txt, col, sgn), sx in zip(group, slots):
        ax.plot(yr, 0, "o", color=col, ms=6)
        ax.plot([yr, yr, sx, sx], [0, 0.45 * sgn, 1.0 * sgn, 1.35 * sgn], color=col, lw=1.0, alpha=0.8)
        ax.text(sx, 1.5 * sgn, txt, ha="center", va="bottom" if sgn > 0 else "top", fontsize=7.6, color=GREY)
        ax.text(sx, 1.42 * sgn, str(yr), ha="center", va="top" if sgn > 0 else "bottom", fontsize=7.2, color=col)
ax.text(1973, 3.3, "A century of machines that sense, decide and act — the triumphs, and the two failures not to skip", ha="center", fontsize=10, color=GREY)
save(fig, "automated-systems-timeline.svg")
print("five SVGs written")
