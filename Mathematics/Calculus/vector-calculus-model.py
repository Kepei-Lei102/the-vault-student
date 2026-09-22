"""Every number quoted in [[Vector Calculus]], computed.

Run:  python3 vector-calculus-model.py        (sympy, numpy)
"""
import numpy as np
import sympy as sp
from sympy.vector import CoordSys3D, gradient, divergence, curl

N = CoordSys3D("N")
x, y, z = N.x, N.y, N.z
i, j, k = N.i, N.j, N.k
t, s, u, v, R, a = sp.symbols("t s u v R a", positive=True)


def fields():
    print("== div, grad, curl on the example fields ==")
    F = x * i + y * j                                   # the spreading field
    G = -y * i + x * j                                  # the rotating field
    H = y * i                                           # the shear
    E = (x * i + y * j + z * k) / (x**2 + y**2 + z**2) ** sp.Rational(3, 2)   # a point charge's field, up to a constant
    for name, f in (("spreading  x i + y j", F), ("rotating  -y i + x j", G), ("shear  y i", H), ("point charge  r-hat / r^2", E)):
        print(f"   {name:28s} div = {sp.simplify(divergence(f))}    curl = {sp.simplify(curl(f))}")
    phi = x**2 * y + sp.sin(z)
    print("   grad(x^2 y + sin z) =", gradient(phi), " | curl grad =", curl(gradient(phi)))
    A = x * y * i + y * z * j + z * x * k
    print("   div curl (xy i + yz j + zx k) =", sp.simplify(divergence(curl(A))))
    print("   temperature T = 20 + 0.001(x^2 + y^2): grad =", gradient(20 + sp.Rational(1, 1000) * (x**2 + y**2)))


def line_integrals():
    print("\n== line integrals ==")
    # work by F = (y, x) along three paths from (0,0) to (1,1): straight, parabola, two legs
    Fx = lambda X, Y: Y; Fy = lambda X, Y: X
    def work(path, tt):
        X, Y = path
        integrand = Fx(X, Y) * sp.diff(X, tt) + Fy(X, Y) * sp.diff(Y, tt)
        return sp.integrate(integrand, (tt, 0, 1))
    print("   F = (y, x), conservative:", work((t, t), t), work((t, t**2), t), work((t, sp.Integer(0)), t) + work((sp.Integer(1), t), t))
    Gx = lambda X, Y: -Y; Gy = lambda X, Y: X
    def workG(path, tt):
        X, Y = path
        return sp.integrate(Gx(X, Y) * sp.diff(X, tt) + Gy(X, Y) * sp.diff(Y, tt), (tt, 0, 1))
    print("   G = (-y, x), not conservative:", workG((t, t), t), workG((t, t**2), t), workG((t, sp.Integer(0)), t) + workG((sp.Integer(1), t), t))
    circ = sp.integrate((-R * sp.sin(t)) * (-R * sp.sin(t)) + (R * sp.cos(t)) * (R * sp.cos(t)), (t, 0, 2 * sp.pi))
    print("   circulation of G round a circle of radius R:", sp.simplify(circ), " = 2 x area, and curl G = 2 everywhere")
    # gravity: work against g from ground to height h along any path
    print("   lifting 1 kg by 3 m against F = -9.8 k, any path: work =", 9.8 * 3, "J")


def flux():
    print("\n== flux ==")
    # point-charge field through a sphere of radius R: E = r-hat / r^2 -> flux 4 pi, independent of R
    ph, th = sp.symbols("phi theta")
    fl = sp.integrate((1 / R**2) * R**2 * sp.sin(ph), (ph, 0, sp.pi), (th, 0, 2 * sp.pi))
    print("   flux of r-hat / r^2 through any sphere:", fl)
    # F = (x, y, z) through the unit cube: each face contributes 1 on the far side, 0 on the near side
    print("   F = (x, y, z) through the unit cube [0,1]^3: 3 faces x 1 = 3;  div F = 3, volume 1, so the divergence theorem gives 3")
    # F = (x^2, y^2, z^2) through unit cube
    print("   F = (x^2, y^2, z^2): flux = 3 (x=1 face gives 1, each);  int div F = int 2(x+y+z) dV =", sp.integrate(2 * (u + v + s), (u, 0, 1), (v, 0, 1), (s, 0, 1)))
    # Green's theorem check: F = (-y, x) round the unit square -> 2 x area = 2
    P = lambda X, Y: -Y; Q = lambda X, Y: X
    legs = [((t, 0), t), ((1, t), t), ((1 - t, 1), t), ((0, 1 - t), t)]
    total = 0
    for (X, Y), tt in legs:
        X = sp.sympify(X); Y = sp.sympify(Y)
        total += sp.integrate(P(X, Y) * sp.diff(X, tt) + Q(X, Y) * sp.diff(Y, tt), (tt, 0, 1))
    print("   Green: (-y, x) round the unit square =", total, "; double integral of (Qx - Py) = 2 over area 1 = 2")
    # area of an ellipse by Green: (1/2) oint (x dy - y dx)
    A = sp.Rational(1, 2) * sp.integrate(a * sp.cos(t) * (R * sp.cos(t)) - R * sp.sin(t) * (-a * sp.sin(t)), (t, 0, 2 * sp.pi))
    print("   area of an ellipse by the planimeter formula (1/2) oint x dy - y dx:", sp.simplify(A))


def stokes():
    print("\n== Stokes on a hemisphere ==")
    # F = (-y, x, 0): curl = (0,0,2). Through the upper unit hemisphere, curl.n dS = 2 cos(phi) * sin(phi) dphi dtheta
    ph, th = sp.symbols("phi theta")
    surf = sp.integrate(2 * sp.cos(ph) * sp.sin(ph), (ph, 0, sp.pi / 2), (th, 0, 2 * sp.pi))
    rim = sp.integrate((-sp.sin(t)) * (-sp.sin(t)) + sp.cos(t) * sp.cos(t), (t, 0, 2 * sp.pi))
    print("   surface integral of curl F over the hemisphere:", surf, " | line integral round the rim:", rim, " | over the flat disc: 2 x pi =", 2 * sp.pi)


def numerics():
    print("\n== a numerical divergence, from a grid ==")
    # F = (x^3, sin y) at (1, 2): div = 3x^2 + cos y = 3 + cos 2 = 2.5839.  Flux out of a small square, midpoint rule per side
    exact = 3 + np.cos(2.0)
    for h in (0.5, 0.1, 0.01):
        X0, Y0 = 1.0, 2.0
        fx = lambda X, Y: X**3; fy = lambda X, Y: np.sin(Y)
        out = (fx(X0 + h / 2, Y0) - fx(X0 - h / 2, Y0)) * h + (fy(X0, Y0 + h / 2) - fy(X0, Y0 - h / 2)) * h
        print(f"   square of side {h}: flux out / area = {out / (h * h):.5f}   (exact div = {exact:.5f})")
    print("\n== a numerical curl: the paddle wheel ==")
    # F = (-y^3, x^2) at (0.7, 0.3): curl = 2x + 3y^2 = 1.67
    exact = 2 * 0.7 + 3 * 0.3**2
    for h in (0.5, 0.1, 0.01):
        X0, Y0 = 0.7, 0.3
        fx = lambda X, Y: -Y**3; fy = lambda X, Y: X**2
        circ = (fx(X0, Y0 - h / 2) - fx(X0, Y0 + h / 2)) * h + (fy(X0 + h / 2, Y0) - fy(X0 - h / 2, Y0)) * h
        print(f"   loop of side {h}: circulation / area = {circ / (h * h):.5f}   (exact curl = {exact:.5f})")


if __name__ == "__main__":
    fields(); line_integrals(); flux(); stokes(); numerics()
