"""Automated Systems and Robotics — the numbers behind the card.

Three experiments, each one a claim the card makes:

1. room_robot()     — the exam's robot ("move forward until an object is within 10 cm,
                      then turn right 90°") driven round a room.  A fixed program that
                      cannot adapt traces the same loop forever; a second rule (turn by a
                      random angle) covers the floor.  Coverage measured for both.
2. sensor_voting()  — one noisy proximity sensor versus two or three that vote.  False
                      stops per hour at 100 readings a second, simulated and by formula.
                      This is the lesson of the 737 MAX's single angle-of-attack sensor.
3. breakeven()      — what a robot costs against what it replaces: months to break even
                      under stated assumptions, so "expensive to purchase" has a size.

Run:  python3 automated-systems-sim.py
Saves the robot paths and the room to the scratchpad for the figure script.
"""
import os
import numpy as np

S = os.environ.get("VAULT_SCRATCH", "/tmp")
rng = np.random.default_rng(7)

# --------------------------------------------------------------------------------------
# 1. The exam's robot in a room
# --------------------------------------------------------------------------------------
W, H = 40, 30            # room in 10-cm cells: 4.0 m by 3.0 m
CELL = 10                # cm per cell
STEP = 2.0               # cm the robot moves per tick


def make_room():
    room = np.zeros((H, W), dtype=bool)      # True = obstacle
    room[0, :] = room[-1, :] = True
    room[:, 0] = room[:, -1] = True
    room[8:12, 10:14] = True                 # a table
    room[18:26, 24:27] = True                # a bookcase
    room[4:6, 28:36] = True                  # a low bench
    return room


def blocked(room, x, y):
    return room[int(y // CELL), int(x // CELL)]


def sensor(room, x, y, th, max_cm=400):
    """Distance in cm from the robot to the first obstacle along its heading (a ray)."""
    c, s_ = np.cos(th), np.sin(th)
    for r in np.arange(1.0, max_cm, 1.0):
        if blocked(room, x + r * c, y + r * s_):
            return r
    return max_cm


def run(room, policy, ticks=15000, start=(205.0, 155.0, 0.0)):
    """The exam's rule: move forward until an object is within 10 cm, then turn.
    `policy` says how to turn.  Returns floor coverage and the path."""
    x, y, th = start
    visited = np.zeros_like(room)
    path = [(x, y)]
    for _ in range(ticks):
        visited[int(y // CELL), int(x // CELL)] = True
        reading = sensor(room, x, y, th)     # sensor: continuously sends the distance
        if reading <= 10:                    # microprocessor: compare with stored value 10 cm
            th = policy(th)                  # actuator: turn
        else:
            x, y = x + STEP * np.cos(th), y + STEP * np.sin(th)   # actuator: forward
        path.append((x, y))
    free = (~room).sum()
    return visited.sum() / free, np.array(path)


def turn_right(th):
    return th + np.pi / 2


def bounce(th):
    """Turn by a random angle between 90 and 270 degrees, the way a floor robot does."""
    return th + rng.uniform(np.pi / 2, 3 * np.pi / 2)


def room_robot():
    room = make_room()
    out = {}
    for name, pol in [("always turn right 90°", turn_right), ("bounce at a random angle", bounce)]:
        cov, path = run(room, pol)
        out[name] = cov
        np.save(f"{S}/robot-path-{name.split()[0]}.npy", path)
        print(f"  {name:28s} coverage after 15000 ticks (300 m of travel): {100*cov:5.1f}% of the floor")
    np.save(f"{S}/robot-room.npy", room)
    # coverage against travel for the bouncing robot
    room = make_room()
    for ticks in (2500, 5000, 15000, 50000):
        cov, _ = run(room, bounce, ticks=ticks)
        print(f"    bounce after {ticks*STEP/100:5.0f} m of travel: {100*cov:5.1f}%")
    # how long until the fixed rule repeats itself?
    _, path = run(room, turn_right, ticks=3000)
    cells = [(int(px // CELL), int(py // CELL)) for px, py in path]
    first = {}
    for i, c in enumerate(cells):
        if c in first and i - first[c] > 50:
            print(f"  the always-right robot re-enters cell {c} after {i - first[c]} ticks: a closed loop of {(i-first[c])*STEP/100:.1f} m, repeated forever")
            break
        first[c] = i
    return out


# --------------------------------------------------------------------------------------
# 2. One sensor versus a vote
# --------------------------------------------------------------------------------------
def sensor_voting(p_glitch=0.001, rate=100, hours=1.0, n_trials=20):
    """A proximity sensor reading a 50 cm gap, with Gaussian noise and rare glitch
    readings (a reflection, a speck of dust, a loose wire) that look like 5 cm.
    Threshold 10 cm.  Count false 'stop' decisions per hour."""
    n = int(rate * 3600 * hours)
    print(f"  {n} readings per hour per sensor, glitch probability {p_glitch} per reading")
    results = {}
    for name, k, m in [("one sensor", 1, 1), ("two sensors, both must agree", 2, 2), ("three sensors, majority", 3, 2)]:
        counts = []
        for _ in range(n_trials):
            readings = 50 + 2 * rng.standard_normal((k, n))
            glitch = rng.random((k, n)) < p_glitch
            readings[glitch] = 5
            below = (readings <= 10).sum(axis=0)
            counts.append((below >= m).sum())
        sim = np.mean(counts)
        if k == 1:
            formula = n * p_glitch
        elif k == 2:
            formula = n * p_glitch**2
        else:
            formula = n * 3 * p_glitch**2
        results[name] = (sim, formula)
        print(f"  {name:30s} false stops per hour: simulated {sim:8.2f}   formula {formula:8.2f}")
    # the other side: a real object with one sensor dead (stuck reading 50 cm)
    print("  with a real object at 5 cm and one sensor stuck at 50 cm:")
    print("     one sensor (the stuck one): never stops.  two-must-agree: never stops.  three-majority: stops.")
    return results


# --------------------------------------------------------------------------------------
# 3. Break-even
# --------------------------------------------------------------------------------------
def breakeven(robot_cost=150_000, robot_maint_per_year=12_000, robot_energy_per_year=6_000,
              worker_wage_per_year=40_000, workers_replaced=2.5, integration=50_000):
    """A welding cell on a car line.  Assumptions are stated, not asserted:
    installed robot plus integration ~ $200k; maintenance 8 %/yr; it runs three shifts,
    so it replaces ~2.5 workers' output (one per shift, minus the tending it still needs)."""
    upfront = robot_cost + integration
    saving_per_year = workers_replaced * worker_wage_per_year - robot_maint_per_year - robot_energy_per_year
    months = 12 * upfront / saving_per_year
    print(f"  upfront ${upfront:,}; net saving ${saving_per_year:,}/yr; break-even {months:.0f} months")
    # sensitivity: halve the wage (a low-wage economy)
    saving2 = workers_replaced * worker_wage_per_year / 2 - robot_maint_per_year - robot_energy_per_year
    print(f"  at half the wage: net saving ${saving2:,}/yr; break-even {12*upfront/saving2:.0f} months")
    return months


if __name__ == "__main__":
    print("1. the exam's robot in a room")
    room_robot()
    print("\n2. one sensor versus a vote")
    sensor_voting()
    print("\n3. break-even")
    breakeven()
