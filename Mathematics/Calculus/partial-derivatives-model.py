"""Every number quoted in [[Partial Derivatives and the Gradient]], computed.

Run:  python3 partial-derivatives-model.py
Needs sympy and numpy.  Prints each result with the section of the card that quotes it.
"""
import numpy as np
import sympy as sp

x, y, t, r, hh = sp.symbols("x y t r h", real=True)


def hill():
    """The hill used throughout: h = 400 - 0.001 x^2 - 0.002 y^2, metres, hiker at P(100, 50)."""
    h = 400 - sp.Rational(1, 1000) * x**2 - sp.Rational(2, 1000) * y**2
    P = {x: 100, y: 50}
    hx, hy = sp.diff(h, x), sp.diff(h, y)
    print("== the hill ==")
    print("h(P) =", h.subs(P), " h_x =", hx, "=", hx.subs(P), " h_y =", hy, "=", hy.subs(P))
    g = sp.Matrix([hx.subs(P), hy.subs(P)])
    mag = sp.sqrt(g.dot(g))
    print("|grad h| =", mag, "=", float(mag), " slope angle =", float(sp.deg(sp.atan(mag))), "deg")
    print("compass bearing of grad (deg from east, anticlockwise) =", float(sp.deg(sp.atan2(g[1], g[0]))) % 360)
    to_summit = sp.Matrix([-100, -50])
    cosang = g.dot(to_summit) / (mag * sp.sqrt(to_summit.dot(to_summit)))
    print("angle between grad and the straight line to the summit =", float(sp.deg(sp.acos(cosang))), "deg")
    # a finite step, to show what the linear approximation is worth
    dx, dy = 3, 4
    exact = h.subs({x: 100 + dx, y: 50 + dy}) - h.subs(P)
    linear = hx.subs(P) * dx + hy.subs(P) * dy
    print(f"step ({dx},{dy}) m: exact dh = {float(exact):.4f}, linear = {float(linear):.4f}, error = {float(exact - linear):.4f}")
    dx, dy = 30, 40
    exact = h.subs({x: 100 + dx, y: 50 + dy}) - h.subs(P)
    linear = hx.subs(P) * dx + hy.subs(P) * dy
    print(f"step ({dx},{dy}) m: exact dh = {float(exact):.4f}, linear = {float(linear):.4f}, error = {float(exact - linear):.4f}")
    # directional derivatives
    for name, u in [("east", (1, 0)), ("north", (0, 1)), ("north-east", (1 / sp.sqrt(2), 1 / sp.sqrt(2))),
                    ("towards the summit", tuple(to_summit / sp.sqrt(to_summit.dot(to_summit)))),
                    ("along the gradient", tuple(g / mag)), ("along the contour", (1 / sp.sqrt(2), -1 / sp.sqrt(2)))]:
        d = g[0] * u[0] + g[1] * u[1]
        print(f"   D_u h, u {name:22s} = {sp.nsimplify(d)} = {float(d):+.4f}")


def example_partials():
    print("\n== Example 1: f = x^2 y + sin(xy) ==")
    f = x**2 * y + sp.sin(x * y)
    for name, d in [("f_x", sp.diff(f, x)), ("f_y", sp.diff(f, y)), ("f_xy", sp.diff(f, x, y)), ("f_yx", sp.diff(f, y, x))]:
        print(f"   {name} =", sp.simplify(d))
    print("   f_xy - f_yx =", sp.simplify(sp.diff(f, x, y) - sp.diff(f, y, x)))
    print("   f_x(1, pi) =", sp.diff(f, x).subs({x: 1, y: sp.pi}), "  f_y(1, pi) =", sp.diff(f, y).subs({x: 1, y: sp.pi}))


def example_can():
    print("\n== Example 2: a drinks can, V = pi r^2 h, r = 3.3 cm, h = 11.5 cm ==")
    V = sp.pi * r**2 * hh
    at = {r: sp.Rational(33, 10), hh: sp.Rational(115, 10)}
    Vr, Vh = sp.diff(V, r).subs(at), sp.diff(V, hh).subs(at)
    print("   V =", float(V.subs(at)), "cm^3   V_r =", float(Vr), "cm^2   V_h =", float(Vh), "cm^2")
    dr, dh = sp.Rational(1, 10), sp.Rational(1, 10)
    lin = Vr * dr + Vh * dh
    exact = V.subs({r: at[r] + dr, hh: at[hh] + dh}) - V.subs(at)
    print(f"   +1 mm on each: linear dV = {float(lin):.2f}, exact = {float(exact):.2f}; share from r = {float(Vr*dr/lin):.3f}")
    print("   ratio V_r / V_h = 2h/r =", float(Vr / Vh))


def example_chain():
    print("\n== Example 4: a drone through a temperature field ==")
    T = 20 + sp.Rational(4, 10000) * x * y - sp.Rational(2, 10000) * y**2   # deg C, x and y in metres
    path = {x: 6 * t, y: t**2}
    direct = sp.diff(T.subs(path), t)
    chain = (sp.diff(T, x) * sp.diff(path[x], t) + sp.diff(T, y) * sp.diff(path[y], t)).subs(path)
    print("   T along the path =", sp.expand(T.subs(path)))
    print("   dT/dt directly   =", sp.expand(direct), "  by the chain rule =", sp.expand(chain))
    print("   at t = 5: position", (path[x].subs(t, 5), path[y].subs(t, 5)), " T_x =", sp.diff(T, x).subs(path).subs(t, 5),
          " T_y =", sp.diff(T, y).subs(path).subs(t, 5), " velocity", (sp.diff(path[x], t).subs(t, 5), sp.diff(path[y], t).subs(t, 5)),
          " dT/dt =", direct.subs(t, 5), "deg C per s")


def example_critical():
    print("\n== Example 5: f = x^3 - 3x + y^2 ==")
    f = x**3 - 3 * x + y**2
    crit = sp.solve([sp.diff(f, x), sp.diff(f, y)], [x, y], dict=True)
    for c in crit:
        H = sp.hessian(f, (x, y)).subs(c)
        print("   ", c, " f =", f.subs(c), " f_xx =", H[0, 0], " f_yy =", H[1, 1], " f_xy =", H[0, 1], " D =", H.det())


def not_differentiable():
    print("\n== partials exist, function is not even continuous: f = xy/(x^2+y^2), f(0,0) = 0 ==")
    f = lambda a, b: 0.0 if a == 0 and b == 0 else a * b / (a * a + b * b)
    for s in (1e-1, 1e-3, 1e-6):
        print(f"   along the x-axis f({s},0) = {f(s, 0)}   along y = x f({s},{s}) = {f(s, s)}")
    print("   f_x(0,0) = lim (f(s,0)-f(0,0))/s = 0,  f_y(0,0) = 0, yet f -> 1/2 along y = x")


def triple_product():
    print("\n== the triple product rule on PV = nRT ==")
    P, V, Tm, n, R = sp.symbols("P V T n R", positive=True)
    dP_dV = sp.diff(n * R * Tm / V, V)          # T fixed
    dV_dT = sp.diff(n * R * Tm / P, Tm)         # P fixed
    dT_dP = sp.diff(P * V / (n * R), P)         # V fixed
    prod = sp.simplify((dP_dV * dV_dT * dT_dP).subs(P, n * R * Tm / V))
    print("   (dP/dV)_T (dV/dT)_P (dT/dP)_V =", prod)


def descent():
    print("\n== gradient descent on f = x^2 + 10 y^2 from (10, 1) ==")
    grad = lambda p: np.array([2 * p[0], 20 * p[1]])
    f = lambda p: p[0] ** 2 + 10 * p[1] ** 2
    for eta in (0.02, 0.09, 0.11):
        p = np.array([10.0, 1.0])
        for k in range(30):
            p = p - eta * grad(p)
        print(f"   eta = {eta}: after 30 steps p = ({p[0]:.4g}, {p[1]:.4g}), f = {f(p):.4g};  per-step factors x: {1-2*eta:+.2f}, y: {1-20*eta:+.2f}")
    print("   stable only while |1 - 20 eta| < 1, i.e. eta < 0.1")


def edges():
    print("\n== an image's gradient is its edges ==")
    n = 200
    yy, xx = np.mgrid[0:n, 0:n]
    img = ((xx - 70) ** 2 + (yy - 80) ** 2 < 45 ** 2).astype(float) * 0.9 + ((xx > 120) & (xx < 175) & (yy > 110) & (yy < 170)) * 0.6
    gy, gx = np.gradient(img)
    mag = np.hypot(gx, gy)
    print(f"   pixels: {n*n}; pixels where |grad I| > 0.1: {(mag > 0.1).sum()} ({100*(mag > 0.1).mean():.1f} %)")


if __name__ == "__main__":
    hill(); example_partials(); example_can(); example_chain(); example_critical(); not_differentiable(); triple_product(); descent(); edges()
